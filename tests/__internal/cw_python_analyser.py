import re
import ast
import sys
import os
import importlib.util
from typing import Dict, Any, List
from difflib import get_close_matches

class CwAPICallVisitor(ast.NodeVisitor):
    """
    AST NodeVisitor to extract API call information from Python code.
    Tracks import aliases, variable types, and collects function/method calls with resolved module/class context.
    """
    def __init__(self, import_aliases: dict, variable_types: dict):
        """
        Args:
            import_aliases: Mapping of alias -> real module name
            variable_types: Mapping of variable -> module.class or module
        """
        super().__init__()
        self.calls: list = []
        self.imports: dict = import_aliases.copy()
        self.imported_modules: set = set(import_aliases.values())
        self.variable_types: dict = variable_types.copy()

    def visit_Assign(self, node: ast.Assign):
        """
        Track variable assignments from function/method calls to infer types.
        """
        if isinstance(node.value, ast.Call):
            func = node.value.func
            name_parts = []
            while isinstance(func, ast.Attribute):
                name_parts.insert(0, func.attr)
                func = func.value
            if isinstance(func, ast.Name):
                name_parts.insert(0, func.id)
            full_type = ".".join(name_parts)
            for target in node.targets:
                if isinstance(target, ast.Name):
                    self.variable_types[target.id] = full_type
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        """
        Collect function/method calls, resolving aliases and variable types where possible.
        """
        func = node.func
        name_parts = []
        while isinstance(func, ast.Attribute):
            name_parts.insert(0, func.attr)
            func = func.value
        if isinstance(func, ast.Name):
            name_parts.insert(0, func.id)
        full_name = ".".join(name_parts)
        # Resolve alias to module if possible
        if name_parts and name_parts[0] in self.imports:
            name_parts[0] = self.imports[name_parts[0]]
            full_name = ".".join(name_parts)
        arg_names = []
        for arg in node.args:
            if isinstance(arg, ast.Name):
                arg_names.append(arg.id)
            elif isinstance(arg, ast.Constant):
                arg_names.append(repr(arg.value))
            else:
                try:
                    arg_names.append(ast.unparse(arg))
                except Exception:
                    arg_names.append(ast.dump(arg))
        # If this is a method call on a variable, try to resolve its type
        if len(name_parts) >= 2 and name_parts[0] in self.variable_types:
            resolved_type = self.variable_types[name_parts[0]]
            resolved_full_name = f"{resolved_type}.{'.'.join(name_parts[1:])}"
            self.calls.append((resolved_type, f"{resolved_full_name}({', '.join(arg_names)})"))
        else:
            self.calls.append((name_parts[0] if name_parts else '', f"{full_name}({', '.join(arg_names)})"))
        self.generic_visit(node)

class CwPythonAnalyser():
    """
    Utility class for Python code detection and analysis of code chunks and blocks especially in markdown.
    Usage: import CwPythonAnalyser / CwPythonAnalyser.func()
    """

    @classmethod
    def _extract_markdown_section_for_code_block(cls, text: str, match_start: int, headers: list[dict]) -> dict:
        """
        Find the section context for a code block, including the header and all text up to the code block.
        
        Parameters:
            text: The full markdown text
            match_start: Start position of the code block
            headers: List of headers from the document
            
        Returns:
            Dictionary containing section information and content
        """
        current_header, section_start = None, 0
        for header in headers:
            if header['start_pos'] < match_start and (not current_header or header['start_pos'] > current_header['start_pos']):
                current_header = header
                section_start = header['content_start']
        text_content = text[section_start:match_start].strip()
        has_formula = '$$' in text_content or text_content.count('$') >= 2 if text_content else False
        has_image = '![' in text_content and '](' in text_content if text_content else False
        return {
            'header': current_header['original'] if current_header else None,
            'section_start': section_start,
            'text_content': text_content if text_content and text_content != (current_header['original'] if current_header else None) else None,
            'has_formula': has_formula,
            'has_image': has_image
        }

    @classmethod
    def _get_pyi_stub_signatures(cls, stubs_root: str = "data/stubs/") -> Dict[str, str]:
        """
        Recursively parse all .pyi files in stubs_root and return a dict mapping
        'module.function' to signature string, e.g. 'bim_controller.get_building(element_id: ElementId) -> str'.
        """
        def _format_signature(node: ast.FunctionDef, class_name: str = None) -> str:
            """Format a function/method signature from an ast.FunctionDef node."""
            args = []
            for arg in node.args.args:
                if arg.arg == 'self':
                    continue
                if arg.annotation is not None:
                    ann = ast.unparse(arg.annotation) if hasattr(ast, 'unparse') else ''
                    args.append(f"{arg.arg}: {ann}")
                else:
                    args.append(arg.arg)
            arg_str = ", ".join(args)
            ret = ""
            if node.returns is not None:
                ret = ast.unparse(node.returns) if hasattr(ast, 'unparse') else ''
            if class_name:
                prefix = f"{class_name}."
            else:
                prefix = ""
            return f"{prefix}{node.name}({arg_str}){' -> ' + ret if ret else ''}"
        signatures = {}
        for dirpath, _, filenames in os.walk(stubs_root):
            for fname in filenames:
                if fname.endswith('.pyi'):
                    module = os.path.relpath(os.path.join(dirpath, fname), stubs_root)
                    module = module.replace(os.sep, ".")[:-4]  # remove .pyi
                    with open(os.path.join(dirpath, fname), encoding="utf-8") as f:
                        try:
                            tree = ast.parse(f.read(), filename=fname)
                        except Exception:
                            continue
                    for node in tree.body:
                        if isinstance(node, ast.FunctionDef):
                            sig = _format_signature(node)
                            signatures[f"{module}.{node.name}"] = sig
                        elif isinstance(node, ast.ClassDef):
                            class_key = f"{module}.{node.name}"
                            init_sig = None
                            for sub in node.body:
                                if isinstance(sub, ast.FunctionDef):
                                    sig = _format_signature(sub, class_name=node.name)
                                    signatures[f"{class_key}.{sub.name}"] = sig
                                    if sub.name == "__init__":
                                        init_sig = sig
                            # Also add the class key itself as a constructor signature if __init__ exists
                            if init_sig:
                                signatures[class_key] = init_sig
        return signatures

    @classmethod
    def extract_markdown_py_code_blocks(cls, text: str) -> List[Dict[str, Any]]:
        """
        Identify Python code blocks in markdown text.
        Returns a list of dictionaries containing block information, e.g.:
        [
            {
                'content': '```python \nimport the code..',  # the entire text split
                'context': None,                             # surrounding text context (if any)
                'code': 'import the code..',                 # the code block content only
                'start_pos': 50,                             # start position in the original text
                'end_pos': 975,                              # end position in the original text
                'language': 'python',                        # the language marker (if any)
                'has_formula': False,                        # whether the context has math formulas
                'has_image': False                           # whether the context has images
            },
            ...
        ]
        """

        def extract_markdown_headers(md_text: str) -> list[dict]:
            """
            Extract markdown headers with hierarchy, ignoring those inside code blocks.
            Returns a list of header dicts with metadata.
            """
            CODE_BLOCK_PATTERN = r'```.*?\n.*?```'  # Matches fenced code blocks
            code_blocks = list(re.compile(CODE_BLOCK_PATTERN, re.DOTALL).finditer(md_text))

            def is_in_code_block(pos: int) -> bool:
                return any(block.start() <= pos <= block.end() for block in code_blocks)

            HEADER_PATTERN = r'^(#{1,6})\s+(.+)$'  # Matches markdown headers
            header_pattern = re.compile(HEADER_PATTERN, re.MULTILINE)
            matches = [m for m in header_pattern.finditer(md_text) if not is_in_code_block(m.start())]
            headers = []
            for i, match in enumerate(matches):
                level = len(match.group(1))
                title = match.group(2).strip()
                start_pos, end_pos = match.start(), match.end()
                content_start = end_pos
                next_header_pos = matches[i + 1].start() if i < len(matches) - 1 else len(md_text)
                line_number = md_text.count('\n', 0, start_pos)
                headers.append({
                    'level': level,
                    'title': title,
                    'line_number': line_number,
                    'start_pos': start_pos,
                    'end_pos': end_pos,
                    'content_start': content_start,
                    'next_header_pos': next_header_pos,
                    'original': match.group(0)
                })
                if 'cw_rich_logger' in globals():
                    cw_rich_logger.debug(
                        f"Found header level {level}: {title} at position {start_pos}-{end_pos}, "
                        f"content from {content_start} to {next_header_pos}"
                    )
            return headers

        headers = extract_markdown_headers(text)
        MARKDOWN_CODE_BLOCK_PATTERN = r'```(.*?)\n(.*?)\n```'  # Matches markdown code blocks with language marker
        code_blocks_info = []
        matches = list(re.finditer(MARKDOWN_CODE_BLOCK_PATTERN, text, re.DOTALL))

        if 'cw_rich_logger' in globals():
            cw_rich_logger.debug(f"Found {len(matches)} code blocks to analyze")

        for match in matches:
            language_marker = match.group(1).strip()
            code_content = match.group(2).strip()
            if cls.is_python_code(code_content, language_marker):
                context = cls._extract_markdown_section_for_code_block(text, match.start(), headers)
                # Compose the full content: context text + code block
                full_content = "\n\n".join(
                    part for part in [context['text_content'], match.group(0)] if part and part.strip()
                )
                # Build a human-readable context description
                context_desc = []
                if context['text_content']:
                    context_desc.append(f"{len(context['text_content'])} chars")
                if context['has_formula']:
                    context_desc.append("math")
                if context['has_image']:
                    context_desc.append("image")
                context_str = f" with {', '.join(context_desc)}" if context_desc else "without context"
                if 'cw_rich_logger' in globals():
                    cw_rich_logger.debug(f"✓ Python block found{context_str}")
                code_blocks_info.append({
                    'content': full_content,
                    'code': code_content,
                    'context': context['text_content'],
                    'start_pos': context['section_start'],
                    'end_pos': match.end(),
                    'language': 'python',
                    'has_formula': context['has_formula'],
                    'has_image': context['has_image']
                })
            else:
                if 'cw_rich_logger' in globals():
                    cw_rich_logger.debug("Not a Python block - skipping")

        if 'cw_rich_logger' in globals():
            cw_rich_logger.debug(f"Identified {len(code_blocks_info)} Python blocks with context")
        return code_blocks_info

    @classmethod
    def extract_py_dotted_symbols_from_code(cls, code: str) -> list[str]:
        """
        Extracts dotted symbols, class instantiations, and attribute accesses from Python code, resolving import aliases.
        Returns a list of strings like 'module.func()', 'cadwork.point_3d(x, y, z)', or 'cadwork.point_3d.magnitude()'.
        Uses AST if possible, but falls back to regex for method calls if AST cannot resolve types (e.g., in code snippets).
        """
        import re
        ast_calls = []
        import_aliases = {}  # alias -> real module name
        var_types = {}       # variable -> module.class or module
        # 1. Parse import aliases using regex (to support partial/invalid code)
        # Matches 'import module' or 'import module as alias' at the start of a line
        IMPORT_PATTERN = r'^\s*import\s+([\w_]+)(?:\s+as\s+([\w_]+))?'  # import ... as ...
        import_pattern = re.compile(
            IMPORT_PATTERN,
            re.MULTILINE
        )
        for match in import_pattern.finditer(code):
            module, alias = match.groups()
            if alias:
                import_aliases[alias] = module
            else:
                import_aliases[module] = module
        # Matches 'from module.submodule import name' or 'from module import name as alias'
        FROM_IMPORT_PATTERN = r'^\s*from\s+([\w_\.]+)\s+import\s+([\w_]+)(?:\s+as\s+([\w_]+))?'  # from ... import ... as ...
        from_import_pattern = re.compile(
            FROM_IMPORT_PATTERN,
            re.MULTILINE
        )
        for match in from_import_pattern.finditer(code):
            module, name, alias = match.groups()
            if alias:
                import_aliases[alias] = f"{module}.{name}"
            else:
                import_aliases[name] = f"{module}.{name}"

        # 1b. Heuristically track variable assignments from known API calls (e.g., ifc_type = bc.get_ifc2x3_element_type(...))
        # Matches variable assignment from a method call, e.g. 'var = alias.method(...)'
        ASSIGN_PATTERN = r'^(\s*)([\w_]+)\s*=\s*([\w_]+)\.([\w_]+)\s*\(([^)]*)\)'  # var = alias.method(...)
        assign_pattern = re.compile(
            ASSIGN_PATTERN,
            re.MULTILINE
        )
        for match in assign_pattern.finditer(code):
            var = match.group(2)
            alias = match.group(3)
            method = match.group(4)
            # If alias is an import alias, expand it
            if alias in import_aliases:
                var_types[var] = f"{import_aliases[alias]}.{method}"
            else:
                var_types[var] = f"{alias}.{method}"

        # 2. AST-based extraction (as before)
        # ...existing code...
        try:
            tree = ast.parse(code)
            visitor = CwAPICallVisitor(import_aliases, var_types)
            visitor.visit(tree)
            stdlib_modules = set(sys.builtin_module_names)
            def is_stdlib(module):
                if module in stdlib_modules:
                    return True
                try:
                    spec = importlib.util.find_spec(module)
                except Exception:
                    return False
                if spec and spec.origin and 'site-packages' not in spec.origin and 'dist-packages' not in spec.origin:
                    return True
                return False
            non_stdlib_imports = {m for m in visitor.imported_modules if not is_stdlib(m)}
            filtered = []
            for root, call in visitor.calls:
                real_root = visitor.imports.get(root, root)
                # Accept calls if root is a known import alias or module, or a variable with a known type
                if real_root.split('.')[0] in import_aliases or real_root.split('.')[0] in non_stdlib_imports or root in var_types:
                    call_out = call.replace(root, real_root, 1)
                    filtered.append(call_out)
            ast_calls = filtered
        except Exception:
            ast_calls = []

        # 3. Regex fallback for aliased calls (e.g., ec.get_active_identifiable_element_ids())
        regex_calls = set()
        # Find all calls like alias.func(...)
        if import_aliases:
            # Matches calls like 'alias.func(...)' for all known import aliases
            ALIAS_PATTERN = r'\b(' + '|'.join(re.escape(a) for a in import_aliases.keys()) + r')\.(\w+)\s*\(([^)]*)\)'  # alias.func(...)
            alias_pattern = re.compile(
                ALIAS_PATTERN
            )
            for match in alias_pattern.finditer(code):
                alias, method, args = match.groups()
                real_mod = import_aliases[alias]
                call_str = f"{real_mod}.{method}({args.strip()})" if args.strip() else f"{real_mod}.{method}()"
                if not any(call_str.split('(')[0] in c for c in ast_calls):
                    regex_calls.add(call_str)

        # Also keep the point_3d and constructor heuristics
        # Matches 'point_3d.method(...)' calls, for Cadwork point_3d special case
        POINT3D_METHOD_PATTERN = r'\b(point_3d)\.(\w+)\s*\(([^)]*)\)'  # point_3d.method(...)
        method_pattern = re.compile(
            POINT3D_METHOD_PATTERN
        )
        for match in method_pattern.finditer(code):
            var, method, args = match.groups()
            call_str = f"cadwork.point_3d.{method}({args.strip()})" if args.strip() else f"cadwork.point_3d.{method}()"
            if not any(call_str.split('(')[0] in c for c in ast_calls):
                regex_calls.add(call_str)
        # Matches 'cadwork.point_3d(...)' constructor calls
        CADWORK_POINT3D_CTOR_PATTERN = r'\bcadwork\.point_3d\s*\(([^)]*)\)'  # cadwork.point_3d(...)
        ctor_pattern = re.compile(
            CADWORK_POINT3D_CTOR_PATTERN
        )
        for match in ctor_pattern.finditer(code):
            args = match.group(1)
            call_str = f"cadwork.point_3d({args.strip()})"
            if not any(call_str.split('(')[0] in c for c in ast_calls):
                regex_calls.add(call_str)

        # Heuristic: extract all method calls on variables (e.g., ifc_type.set_ifc_wall())
        # and chained calls (e.g., cadwork.process_type.is_rough_volume_framed_wall(...))
        # Matches generic method calls like 'obj.method(...)' or 'obj.sub.method(...)'
        GENERIC_METHOD_PATTERN = r'\b([a-zA-Z_][\w\.]*)\.(\w+)\s*\(([^)]*)\)'  # obj.method(...)
        generic_method_pattern = re.compile(
            GENERIC_METHOD_PATTERN
        )
        for match in generic_method_pattern.finditer(code):
            obj, method, args = match.groups()
            # If obj is a variable with a known type, expand it
            if obj in var_types:
                call_str = f"{var_types[obj]}.{method}({args.strip()})" if args.strip() else f"{var_types[obj]}.{method}()"
            else:
                call_str = f"{obj}.{method}({args.strip()})" if args.strip() else f"{obj}.{method}()"
            # Skip if already handled by alias or point_3d logic
            skip = False
            if import_aliases and obj in import_aliases:
                skip = True
            if obj == 'point_3d' or obj == 'cadwork.point_3d':
                skip = True
            if not skip and not any(call_str.split('(')[0] in c for c in ast_calls):
                regex_calls.add(call_str)

        return list(set(ast_calls) | regex_calls)
    
    @classmethod
    def match_symbols_to_api_signatures(
        cls,
        api_calls: list[str],
        stubs_root: str = "data/stubs/",
        max_close_matches: int = 5,
        min_parts_for_class: int = 2,
        min_parts_for_static: int = 3,
        close_match_cutoff: float = 0.5,
        max_uncertain_suggestions: int = 2,
        is_keep_double: bool = False
    ) -> tuple[list[str], list[tuple[str, list[str]]]]:
        stub_signatures = cls._get_pyi_stub_signatures(stubs_root)
        stub_lookup = {k.lower().replace(' ', ''): v for k, v in stub_signatures.items()}

        if not is_keep_double:
            seen_calls = set()
            api_calls = [x for x in api_calls if not (x in seen_calls or seen_calls.add(x))]

        matched_signatures = []
        uncertain_signatures = []

        def find_signature(parts: list[str]) -> str | None:
            module_prefix = parts[0] if len(parts) > 1 else None
            if module_prefix:
                candidates = [k for k in stub_lookup if k.startswith(f"{module_prefix}.") and k.endswith(parts[-1])]
                if candidates:
                    return max(candidates, key=len)
            for i in range(len(parts)):
                suffix = ".".join(parts[i:])
                matches = [k for k in stub_lookup if k.endswith(suffix)]
                if matches:
                    return max(matches, key=len)
            return None

        for call in api_calls:
            call_base = call.split("(")[0].replace(' ', '').lower()
            parts = call_base.split(".")
            found_key = find_signature(parts)
            found_signature = stub_lookup[found_key] if found_key else None

            if not found_signature and len(parts) >= min_parts_for_class:
                class_path = ".".join(parts)
                for key in (f"{class_path}.__init__", f"{class_path}.__new__", class_path):
                    if key in stub_lookup:
                        found_key = key
                        found_signature = stub_lookup[key]
                        break
                if not found_signature:
                    class_name = parts[-1]
                    matches = [k for k in stub_lookup if k.split(".")[-1] == class_name]
                    if matches:
                        found_key = max(matches, key=len)
                        found_signature = stub_lookup[found_key]

            if not found_signature and len(parts) >= min_parts_for_static:
                method = ".".join(parts[-2:])
                matches = [k for k in stub_lookup if k.endswith(method)]
                if matches:
                    found_key = max(matches, key=len)
                    found_signature = stub_lookup[found_key]
                else:
                    mod = ".".join(parts[:-1])
                    func = parts[-1]
                    func_snake = re.sub(r'(?<!^)(?=[A-Z])', '_', func).lower()
                    alt_key = f"{mod}.{mod.split('.')[-1]}.{func_snake}"
                    if alt_key in stub_lookup:
                        found_key = alt_key
                        found_signature = stub_lookup[alt_key]

            if not found_signature:
                func_name = parts[-1]
                matches = [k for k in stub_lookup if k.split(".")[-1] == func_name]
                if matches:
                    found_key = max(matches, key=len)
                    found_signature = stub_lookup[found_key]

            if found_signature:
                module = found_key.split(".")[0] if found_key else ""
                if found_signature.startswith(f"{module}."):
                    matched_signatures.append(found_signature)
                else:
                    matched_signatures.append(f"{module}.{found_signature}")
            else:
                call_key = call.split("(")[0].replace(' ', '').lower()
                close_matches = get_close_matches(call_key, list(stub_lookup.keys()), n=max_close_matches, cutoff=close_match_cutoff)
                if close_matches:
                    suggestions = [f"{k}: {stub_lookup[k]}" for k in close_matches[:max_uncertain_suggestions]]
                    uncertain_signatures.append((call, suggestions))
                else:
                    uncertain_signatures.append((call, []))

        if not is_keep_double:
            seen_sigs = set()
            matched_signatures = [x for x in matched_signatures if not (x in seen_sigs or seen_sigs.add(x))]
        return matched_signatures, uncertain_signatures

    @classmethod
    def is_python_code(cls, content: str, marker: str = "") -> bool:
        if marker and ("python" in marker.lower() or marker.strip().lower() == "py"):
            return True
        if re.search(r"```\s*(python|py)\b", content, re.IGNORECASE):
            return True
        patterns = [
            # import or from statements
            r'^\s*(import|from)\s+\w+',
            # function definitions
            r'^\s*def\s+\w+\s*\(',
            # class definitions
            r'^\s*class\s+\w+[:\(]',
            # self attribute access
            r'\bself\.[a-zA-Z_]',
            # print function
            r'print\s*\(',
            # decorators
            r'^\s*@\w+',
            # Python constants
            r'\b(True|False|None)\b',
            # if statement
            r'if\s+.*:\s*$',
            # for loop
            r'for\s+.*\s+in\s+.*:',
            # while loop
            r'while\s+.*:',
            # try statement
            r'try:\s*$',
            # comment lines
            r'^\s*#',
            # variable assignment
            r'^\s*\w+\s*=\s*.+'
        ]
        if any(re.search(p, content, re.MULTILINE) for p in patterns):
            return True
        try:
            ast.parse(content)
            return True
        except SyntaxError:
            try:
                fake_code = "def _():\n" + "\n".join(f"    {line}" for line in content.splitlines())
                ast.parse(fake_code)
                return True
            except Exception:
                pass
        except Exception:
            pass
        if re.match(r'^\s*```$', content, re.MULTILINE):
            return True
        expr_line = content.strip().split('#', 1)[0].strip()
        if re.match(r'^\w+(\.\w+)*\s*\(.*\)\s*$', expr_line):
            return True
        try:
            ast.parse(expr_line, mode='eval')
            return True
        except Exception:
            return False

