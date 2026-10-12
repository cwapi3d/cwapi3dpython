#!/usr/bin/env python3
"""Inventory the existing .pyi stubs.

A .pyi is valid Python, so the declaration inventory comes from ``ast`` rather
than regex. Alongside the names, each file's local formatting habits are
measured -- blank lines between defs, import idiom -- because the repo is not
uniformly formatted and appended code has to match its host file.
"""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass, field
from pathlib import Path

import _files


@dataclass
class ControllerStub:
    module: str
    path: Path
    functions: set[str] = field(default_factory=set)
    imported_names: set[str] = field(default_factory=set)
    star_imports_api_types: bool = False
    blank_lines_between_defs: int = 1
    last_import_line: int = 0  # 1-based; 0 when the file has no imports


@dataclass
class TypeStub:
    name: str
    path: Path
    classes: set[str] = field(default_factory=set)
    members: dict[str, set[str]] = field(default_factory=dict)
    # class name -> (line of the first method, last line of the class); both 1-based.
    first_def_line: dict[str, int] = field(default_factory=dict)
    end_line: dict[str, int] = field(default_factory=dict)


@dataclass
class StubInventory:
    controllers: dict[str, ControllerStub]
    types: dict[str, TypeStub]
    cadwork_init: Path
    exported_types: set[str]


def _measure_blank_lines(source: str) -> int:
    """Dominant number of blank lines between top-level ``def``s in this file."""
    lines = source.splitlines()
    counts: dict[int, int] = {}
    previous_def = None
    for index, line in enumerate(lines):
        if not line.startswith('def '):
            continue
        if previous_def is not None:
            blanks = 0
            cursor = index - 1
            while cursor > previous_def and not lines[cursor].strip():
                blanks += 1
                cursor -= 1
            counts[blanks] = counts.get(blanks, 0) + 1
        previous_def = index
    if not counts:
        return 1
    return max(counts.items(), key=lambda item: (item[1], -item[0]))[0]


def _parse_controller(module: str, path: Path) -> ControllerStub:
    source = _files.read_text(path)
    tree = ast.parse(source)
    stub = ControllerStub(module=module, path=path)
    stub.blank_lines_between_defs = _measure_blank_lines(source)

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            stub.functions.add(node.name)
        elif isinstance(node, ast.ImportFrom):
            stub.last_import_line = max(stub.last_import_line, node.end_lineno or 0)
            for alias in node.names:
                if alias.name == '*':
                    if node.module == 'cadwork.api_types':
                        stub.star_imports_api_types = True
                else:
                    stub.imported_names.add(alias.asname or alias.name)
        elif isinstance(node, ast.Import):
            stub.last_import_line = max(stub.last_import_line, node.end_lineno or 0)
            for alias in node.names:
                stub.imported_names.add(alias.asname or alias.name.split('.')[0])
    return stub


def _parse_type(path: Path) -> TypeStub:
    stub = TypeStub(name=path.stem, path=path)
    tree = ast.parse(_files.read_text(path))
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            stub.classes.add(node.name)
            members: set[str] = set()
            for child in node.body:
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    members.add(child.name)
                    # Hand-written stubs declare fields as `self.x = x` in __init__.
                    for inner in ast.walk(child):
                        if isinstance(inner, (ast.Assign, ast.AnnAssign)):
                            targets = inner.targets if isinstance(inner, ast.Assign) else [inner.target]
                            for target in targets:
                                if (
                                    isinstance(target, ast.Attribute)
                                    and isinstance(target.value, ast.Name)
                                    and target.value.id == 'self'
                                ):
                                    members.add(target.attr)
                elif isinstance(child, ast.AnnAssign) and isinstance(child.target, ast.Name):
                    members.add(child.target.id)
                elif isinstance(child, ast.Assign):
                    for target in child.targets:
                        if isinstance(target, ast.Name):
                            members.add(target.id)
            stub.members[node.name] = members
            stub.end_line[node.name] = node.end_lineno or node.lineno
            defs = [c.lineno for c in node.body if isinstance(c, (ast.FunctionDef, ast.AsyncFunctionDef))]
            if defs:
                stub.first_def_line[node.name] = min(defs)
    return stub


def _exported_from_cadwork_init(path: Path) -> set[str]:
    if not path.is_file():
        return set()
    tree = ast.parse(_files.read_text(path))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == '__all__':
                    if isinstance(node.value, (ast.List, ast.Tuple)):
                        return {
                            element.value
                            for element in node.value.elts
                            if isinstance(element, ast.Constant) and isinstance(element.value, str)
                        }
    return set()


def parse(src_dir: Path) -> StubInventory:
    controllers: dict[str, ControllerStub] = {}
    for init in sorted(src_dir.glob('*/__init__.pyi')):
        module = init.parent.name
        if module == 'cadwork':
            continue
        controllers[module] = _parse_controller(module, init)

    cadwork_dir = src_dir / 'cadwork'
    types: dict[str, TypeStub] = {}
    if cadwork_dir.is_dir():
        for stub_path in sorted(cadwork_dir.glob('*.pyi')):
            if stub_path.stem == '__init__':
                continue
            types[stub_path.stem] = _parse_type(stub_path)

    cadwork_init = cadwork_dir / '__init__.pyi'
    return StubInventory(
        controllers=controllers,
        types=types,
        cadwork_init=cadwork_init,
        exported_types=_exported_from_cadwork_init(cadwork_init),
    )


def append_block(path: Path, block: str, blank_lines: int) -> None:
    """Append `block` to `path`, separated by `blank_lines` blank lines."""
    existing = _files.read_text(path) if path.is_file() else ''
    trimmed = existing.rstrip('\n')
    separator = '\n' * (blank_lines + 1) if trimmed else ''
    _files.write_text(path, f'{trimmed}{separator}{block.rstrip()}\n')


def insert_members(path: Path, class_name: str, lines: list[str], *, before_first_def: bool) -> None:
    """Add `lines` (already indented for the class body) to an existing class.

    Enum members go in front of the first method so ``__int__`` stays last; method
    stubs are appended after the last line of the class.
    """
    if not lines:
        return
    source = _files.read_text(path)
    tree = ast.parse(source)
    node = next(
        (n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == class_name),
        None,
    )
    if node is None:
        raise ValueError(f'{path}: class {class_name} not found')
    existing = source.split('\n')
    defs = [c.lineno for c in node.body if isinstance(c, (ast.FunctionDef, ast.AsyncFunctionDef))]
    if before_first_def and defs:
        # Decorators and the blank line above the def stay attached to it.
        index = min(defs) - 1
        while index > 0 and not existing[index - 1].strip():
            index -= 1
        existing[index:index] = ['', *lines]
    else:
        index = node.end_lineno or node.lineno
        existing[index:index] = ['', *lines]
    _files.write_text(path, '\n'.join(existing).rstrip('\n') + '\n')


def insert_imports(path: Path, imports: list[str]) -> None:
    """Insert `imports` after the file's existing import block, skipping dupes."""
    if not imports:
        return
    source = _files.read_text(path)
    lines = source.splitlines()
    wanted = [line for line in imports if line not in lines]
    if not wanted:
        return

    insert_at = 0
    for index, line in enumerate(lines):
        if re.match(r'^(from|import)\s', line):
            insert_at = index + 1
    if insert_at == 0:
        # No imports yet: land just after the module docstring.
        tree = ast.parse(source)
        if tree.body and isinstance(tree.body[0], ast.Expr) and isinstance(tree.body[0].value, ast.Constant):
            insert_at = tree.body[0].end_lineno or 1
            lines.insert(insert_at, '')
            insert_at += 1

    lines[insert_at:insert_at] = wanted
    _files.write_text(path, '\n'.join(lines) + '\n')
