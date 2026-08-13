#!/usr/bin/env python3
"""Render missing declarations and patch the surrounding repo files.

Rendering follows the host repo's conventions exactly:
  * no function bodies -- the Google docstring IS the body
  * ``Parameters:`` (never ``Args:``), ``Returns:`` LAST, omitted for ``-> None``
  * blank lines between defs matched per host file

Doxygen ``@par Example`` blocks are C++ and are deliberately NOT machine-translated
into Python doctests: a wrong example in the published docs is worse than none.
Methods that had one available are reported so a human can port it.

Companion edits are all surgical line splices. mkdocs.yml in particular is never
round-tripped through a YAML writer -- the stdlib has none, and re-serialising
would destroy the file's comments and hand-tuned ordering.
"""

from __future__ import annotations

import keyword
import re
from dataclasses import dataclass, field
from pathlib import Path

import _files
from _cpp_bindings import Binding, CadworkType, EnumMember, Trampoline
from _doxygen import DocBlock, camel_to_snake

_INDENT = "    "
_API_TYPE_ALIASES = {
    "ElementId",
    "MaterialId",
    "ColorId",
    "EndtypeId",
    "AxisId",
    "MenuIndex",
    "ReferenceSide",
    "MultiLayerSetId",
    "UserAttributeId",
    "UnsignedInt",
}


# ---------------------------------------------------------------------------
# type resolution
# ---------------------------------------------------------------------------


@dataclass
class TypeResolver:
    type_map: dict[str, str]
    cadwork_types: dict[str, str]  # normalised C++ type -> python type name
    hint_map: dict[str, str] = field(default_factory=dict)
    stub_types: set[str] = field(default_factory=set)
    unresolved: set[str] = field(default_factory=set)

    @classmethod
    def build(
        cls,
        type_map: dict[str, str],
        types: list[CadworkType],
        hint_map: dict[str, str] | None = None,
        stub_types: set[str] | None = None,
    ) -> "TypeResolver":
        registry: dict[str, str] = {}
        for entry in types:
            registry[entry.cpp_type] = entry.python_name
            registry[entry.cpp_type.split("::")[-1]] = entry.python_name
            registry[entry.python_name] = entry.python_name
        return cls(
            type_map=dict(type_map),
            cadwork_types=registry,
            hint_map=dict(hint_map or {}),
            stub_types=set(stub_types or set()),
        )

    def resolve_hint(self, name: str) -> str | None:
        """Resolve a Doxygen ``@ref`` name / static_cast target to an annotation.

        The interface headers name the SPECIFIC type a parameter carries
        (``multiLayerSetID``, ``multiLayerSubType``) where the pybind11 trampoline
        has already flattened it to ``uint64_t`` / ``int32_t``. That naming is
        authored per parameter, so it beats the flattened type when both exist.
        """
        bare = name.split("::")[-1].strip()
        if not bare:
            return None
        if bare in self.hint_map:
            return self.hint_map[bare]
        if bare in self.cadwork_types:
            return self.cadwork_types[bare]
        snake = camel_to_snake(bare)
        # A type the repo already ships a hand-written stub for, even though the
        # bindings never register it (e.g. multi_layer_subtype).
        if snake in self.stub_types:
            return snake
        return None

    def resolve(self, cpp_type: str, quiet: bool = False) -> tuple[str, str | None]:
        """Return (python annotation, cadwork type name needing an import).

        `quiet` suppresses the unresolved-type warning for speculative lookups
        (a static_cast target or a @param hint that may not name a real type).
        """
        text = cpp_type.strip().removeprefix("const ").strip()
        if text in self.type_map:
            return (self.type_map[text], None)

        vector = re.fullmatch(r"std::vector<(.+)>", text)
        if vector:
            inner, needed = self.resolve(vector.group(1), quiet)
            return (f"list[{inner}]", needed)

        for candidate in (text, text.rstrip("*").strip()):
            if candidate in self.cadwork_types:
                name = self.cadwork_types[candidate]
                return (name, name)
            if candidate in self.type_map:
                return (self.type_map[candidate], None)

        if not quiet:
            self.unresolved.add(text)
        return ("Any", None)


# ---------------------------------------------------------------------------
# function rendering
# ---------------------------------------------------------------------------


def docstring_safe(text: str) -> str:
    """Make prose safe to sit inside a ``\"\"\"`` docstring.

    Doxygen prose routinely contains quoted labels (``GUI label "X"``). A triple
    quote inside, or a trailing double quote adjacent to the closer, would produce
    a stub that does not parse.
    """
    cleaned = text.replace('"""', "'''").replace("\\", "\\\\")
    return cleaned[:-1] + "'" if cleaned.endswith('"') else cleaned


def _default_literal(cpp_default: str | None) -> str | None:
    if cpp_default is None:
        return None
    text = cpp_default.strip()
    if text == "true":
        return "True"
    if text == "false":
        return "False"
    if text == "nullptr":
        return "None"
    return text


def _safe_name(name: str, used: set[str], index: int) -> str:
    candidate = name or f"arg{index}"
    candidate = re.sub(r"\W", "_", candidate)
    if not candidate or candidate[0].isdigit():
        candidate = f"arg{index}"
    if keyword.iskeyword(candidate):
        candidate = f"{candidate}_"
    while candidate in used:
        candidate = f"{candidate}_{index}"
    used.add(candidate)
    return candidate


_TYPING_NAMES = {"Any", "Callable", "Iterator", "Optional", "Union"}


@dataclass
class RenderedFunction:
    text: str
    imports: set[str]  # cadwork type / api_types alias names
    typing_names: set[str]  # names needing `from typing import ...`
    had_cpp_example: bool
    thin_doc: bool


def _referenced_names(annotations: list[str], resolver: TypeResolver) -> tuple[set[str], set[str]]:
    """Split the identifiers used in `annotations` into cadwork and typing names.

    Derived from the rendered annotation strings rather than threaded through the
    resolver, so a name introduced anywhere -- inside ``list[...]``, via an enum
    upgrade, or straight from the type map -- still gets its import.
    """
    known = set(resolver.cadwork_types.values()) | _API_TYPE_ALIASES
    identifiers: set[str] = set()
    for annotation in annotations:
        identifiers.update(re.findall(r"\w+", annotation))
    return (identifiers & known, identifiers & _TYPING_NAMES)


def render_function(
    binding: Binding,
    trampoline: Trampoline,
    doc: DocBlock | None,
    resolver: TypeResolver,
    param_name_fallbacks: dict[str, str],
) -> RenderedFunction:
    doc_params = doc.params if doc else []
    aligned_doc = doc_params if len(doc_params) == len(trampoline.param_types) else []

    annotations: list[str] = []
    for index, cpp_type in enumerate(trampoline.param_types):
        annotation, needed = resolver.resolve(cpp_type)
        # Ids and enums cross the pybind11 boundary flattened to uint64_t/int32_t.
        # When the primary type is one of those scalars, prefer the specific type
        # named by the trampoline's static_cast, then by the interface header's
        # @param hint. A parameter that already resolved to a real cadwork class is
        # left alone -- nothing more specific exists.
        if needed is None:
            upgrades = [
                trampoline.param_casts[index]
                if index < len(trampoline.param_casts)
                else None,
                aligned_doc[index][1] if aligned_doc else None,
            ]
            for candidate in upgrades:
                upgraded = resolver.resolve_hint(candidate) if candidate else None
                if upgraded:
                    annotation = upgraded
                    break
        annotations.append(annotation)

    used: set[str] = set()
    names: list[str] = []
    descriptions: list[str] = []
    for index, annotation in enumerate(annotations):
        raw_name = ""
        description = ""
        if index < len(binding.arg_names):
            raw_name = binding.arg_names[index]
        if aligned_doc:
            doc_name, _hint, doc_desc = aligned_doc[index]
            raw_name = raw_name or camel_to_snake(doc_name)
            description = doc_desc
        if not raw_name:
            raw_name = param_name_fallbacks.get(annotation, "")
        if not raw_name and index < len(trampoline.param_names):
            candidate = trampoline.param_names[index]
            if not re.fullmatch(r"a\d+", candidate):
                raw_name = camel_to_snake(candidate)
        names.append(_safe_name(raw_name, used, index))
        descriptions.append(description)

    defaults = [
        _default_literal(binding.arg_defaults[index])
        if index < len(binding.arg_defaults)
        else None
        for index in range(len(annotations))
    ]

    signature_parts: list[str] = []
    for name, annotation, default in zip(names, annotations, defaults):
        part = f"{name}: {annotation}"
        if default is not None:
            part += f" = {default}"
        signature_parts.append(part)

    return_annotation, return_needed = resolver.resolve(trampoline.return_type)
    if return_needed is None and doc and doc.returns_hint:
        upgraded = resolver.resolve_hint(doc.returns_hint)
        if upgraded:
            return_annotation = upgraded
    imports, typing_names = _referenced_names(
        [*annotations, return_annotation], resolver
    )

    lines = [
        f"def {binding.python_name}({', '.join(signature_parts)}) -> {return_annotation}:"
    ]
    brief = docstring_safe(
        (doc.brief if doc else "") or binding.python_name.replace("_", " ")
    )
    if not brief.endswith((".", "!", "?")):
        brief += "."
    lines.append(f'{_INDENT}"""{brief}')

    if doc and doc.deprecated:
        lines.append("")
        lines.append(f"{_INDENT}Deprecated : ")
        lines.append(f"{_INDENT * 2}{docstring_safe(doc.deprecated)}")

    if names:
        lines.append("")
        lines.append(f"{_INDENT}Parameters:")
        for name, description in zip(names, descriptions):
            text = docstring_safe(description) or name.replace("_", " ") + "."
            lines.append(f"{_INDENT * 2}{name}: {text}")

    if doc and doc.note:
        lines.append("")
        lines.append(f"{_INDENT}Note:")
        lines.append(f"{_INDENT * 2}{docstring_safe(doc.note)}")

    if return_annotation != "None":
        lines.append("")
        lines.append(f"{_INDENT}Returns:")
        returns_text = docstring_safe(doc.returns if doc else "") or return_annotation
        lines.append(f"{_INDENT * 2}{returns_text}")

    lines.append(f'{_INDENT}"""')

    return RenderedFunction(
        text="\n".join(lines),
        imports=imports,
        typing_names=typing_names,
        had_cpp_example=bool(doc and doc.example),
        thin_doc=not (doc and doc.brief),
    )


def import_lines(names: set[str], stub_star_imports: bool, known: set[str]) -> list[str]:
    """``from cadwork.x import x`` lines for the types this file now needs."""
    lines: list[str] = []
    for name in sorted(names):
        if name in known:
            continue
        if name in _API_TYPE_ALIASES:
            if stub_star_imports:
                continue
            lines.append(f"from cadwork.api_types import {name}")
            continue
        lines.append(f"from cadwork.{name} import {name}")
    return lines


# ---------------------------------------------------------------------------
# cadwork type rendering
# ---------------------------------------------------------------------------


@dataclass
class RenderedType:
    text: str
    imports: set[str]
    warnings: list[str] = field(default_factory=list)
    # False when the type could not be rendered faithfully and must not be written.
    ok: bool = True


def render_enum(
    entry: CadworkType, definitions: dict[str, list[EnumMember]]
) -> RenderedType:
    """Emit an IntEnum matching the shape of the repo's existing enum stubs.

    Numeric values come from the C++ enum definition, never from the
    registration order -- ``py::enum_`` chains carry no values at all.
    """
    warnings: list[str] = []
    bare = entry.cpp_type.split("::")[-1]
    members = definitions.get(bare, [])
    by_name = {member.name: member for member in members}

    resolved: list[tuple[str, int, str]] = []
    for python_name, cpp_expression in entry.values:
        member = by_name.get(cpp_expression.split("::")[-1])
        if member is None:
            warnings.append(
                f"cadwork.{entry.python_name}.{python_name}: no C++ value found for "
                f"{cpp_expression}"
            )
            continue
        resolved.append((python_name, member.value, member.doc))

    if not resolved:
        return RenderedType(
            text="",
            imports=set(),
            ok=False,
            warnings=[
                f"cadwork.{entry.python_name}: no member of C++ enum '{bare}' could be "
                "resolved to a value -- NOT written. Add the declaring header's "
                "directory to [source].enum_search_dirs."
            ],
        )
    if len(resolved) != len(entry.values):
        warnings.append(
            f"cadwork.{entry.python_name}: {len(resolved)}/{len(entry.values)} members "
            "resolved -- review before publishing"
        )

    title = entry.python_name.replace("_", " ")
    lines = [
        "from enum import IntEnum, unique",
        "",
        "",
        "@unique",
        f"class {entry.python_name}(IntEnum):",
        f'{_INDENT}"""{title}',
    ]
    if resolved:
        lines += [
            "",
            f"{_INDENT}Examples:",
            f"{_INDENT * 2}>>> cadwork.{entry.python_name}.{resolved[0][0]}",
            f"{_INDENT * 2}{resolved[0][0]}",
        ]
    lines.append(f'{_INDENT}"""')
    for python_name, value, doc in resolved:
        lines.append(f"{_INDENT}{python_name} = {value}")
        lines.append(f'{_INDENT}"""{docstring_safe(doc)}"""')
    lines += ["", f"{_INDENT}def __int__(self) -> int:", f"{_INDENT * 2}return self.value"]

    return RenderedType(text="\n".join(lines) + "\n", imports=set(), warnings=warnings)


def render_class(entry: CadworkType, resolver: TypeResolver) -> RenderedType:
    """Emit a value-object stub.

    ``.def_readwrite``/``.def`` registrations carry a member pointer, not a type,
    so field and return annotations are not recoverable from the bindings. Those
    land as ``Any`` and the type is reported for a human pass.
    """
    imports: set[str] = set()
    warnings: list[str] = []
    body: list[str] = []

    for signature in entry.init_signatures:
        if not signature:
            continue
        parts = []
        for index, cpp_type in enumerate(signature):
            annotation, needed = resolver.resolve(cpp_type)
            if needed:
                imports.add(needed)
            parts.append(f"arg{index}: {annotation}")
        body.append(f"{_INDENT}def __init__(self, {', '.join(parts)}) -> None:")
        body.append(f'{_INDENT * 2}"""Initialize a {entry.python_name}."""')
        body.append("")
        break

    if entry.fields:
        for name, _member, writable in entry.fields:
            body.append(f"{_INDENT}{name}: Any")
            body.append(f'{_INDENT}"""{"read/write" if writable else "read-only"}."""')
        body.append("")
        warnings.append(
            f"cadwork.{entry.python_name}: field types are not recoverable from the "
            "bindings -- annotated Any"
        )

    for name, _member in entry.methods:
        if name.startswith("__"):
            continue
        body.append(f"{_INDENT}def {name}(self) -> Any:")
        body.append(f'{_INDENT * 2}"""{name.replace("_", " ")}."""')
        body.append("")
    if entry.methods:
        warnings.append(
            f"cadwork.{entry.python_name}: method signatures are not recoverable from "
            "the bindings -- parameters omitted, returns annotated Any"
        )

    header = [
        f"class {entry.python_name}:",
        f'{_INDENT}"""{entry.python_name.replace("_", " ")}."""',
        "",
    ]
    prefix = ["from typing import Any"]
    prefix += [f"from cadwork.{name} import {name}" for name in sorted(imports)]
    lines = [*prefix, "", ""] + header + body
    return RenderedType(
        text="\n".join(lines).rstrip() + "\n", imports=imports, warnings=warnings
    )


# ---------------------------------------------------------------------------
# companion-file patches
# ---------------------------------------------------------------------------


def patch_cadwork_init(path: Path, name: str, kind: str) -> bool:
    """Insert the re-export line and the ``__all__`` entry for a new type."""
    source = _files.read_text(path)
    if f"from .{name} import {name}" in source:
        return False
    lines = source.splitlines()
    section = "# --- Enumerations ---" if kind == "enum" else "# --- Data classes ---"
    import_line = f"from .{name} import {name} as {name}"

    try:
        section_index = lines.index(section)
    except ValueError:
        return False

    end = section_index + 1
    while end < len(lines) and lines[end].startswith("from ."):
        end += 1
    block = lines[section_index + 1 : end]
    position = section_index + 1 + sum(
        1 for line in block if line < import_line
    )
    lines.insert(position, import_line)

    all_start = next(
        (index for index, line in enumerate(lines) if line.startswith("__all__")), None
    )
    if all_start is not None:
        marker = "# Enumerations" if kind == "enum" else "# Data classes"
        try:
            marker_index = next(
                index
                for index in range(all_start, len(lines))
                if lines[index].strip() == marker
            )
        except StopIteration:
            marker_index = all_start
        entry = f'    "{name}",'
        end = marker_index + 1
        while end < len(lines) and lines[end].strip().startswith('"'):
            end += 1
        block = lines[marker_index + 1 : end]
        position = marker_index + 1 + sum(1 for line in block if line < entry)
        lines.insert(position, entry)

    _files.write_text(path, "\n".join(lines) + "\n")
    return True


def write_docs_page(docs_dir: Path, slug: str, title: str, target: str) -> Path:
    page = docs_dir / f"{slug}.md"
    _files.write_text(page, f"# {title}\n\n::: {target}\n    rendering:\n        show_root_heading: false\n"
        "        show_source: true\n")
    return page


def append_to_enums_page(docs_dir: Path, enums_page: str, name: str) -> Path:
    page = docs_dir / enums_page
    existing = _files.read_text(page) if page.is_file() else "# Enumerations\n"
    if f"::: cadwork.{name}" in existing:
        return page
    block = f"\n## {name}\n\n::: cadwork.{name}\n"
    _files.write_text(page, existing.rstrip("\n") + "\n" + block)
    return page


def _title_case(slug: str) -> str:
    return " ".join(word.capitalize() for word in slug.split("_"))


def patch_mkdocs_nav(path: Path, slug: str, title: str, under: str) -> bool:
    """Splice one nav line into the ``Reference:`` or ``Cadwork:`` block.

    Line-based on purpose: the stdlib ships no YAML writer, and a round-trip
    would drop every comment and the hand-tuned ordering in this file.
    """
    lines = _files.read_text(path).splitlines()
    entry_suffix = f"documentation/{slug}.md"
    if any(entry_suffix in line for line in lines):
        return False

    if under == "Cadwork":
        anchor = next(
            (index for index, line in enumerate(lines) if line.strip() == "- Cadwork:"),
            None,
        )
    else:
        anchor = next(
            (index for index, line in enumerate(lines) if line.strip() == "- Reference:"),
            None,
        )
    if anchor is None:
        return False

    indent = len(lines[anchor]) - len(lines[anchor].lstrip()) + 4
    entry = f"{' ' * indent}- {title}: {entry_suffix}"

    insert_at = anchor + 1
    cursor = anchor + 1
    while cursor < len(lines):
        line = lines[cursor]
        if not line.strip():
            cursor += 1
            continue
        current_indent = len(line) - len(line.lstrip())
        if current_indent < indent:
            break
        if current_indent == indent and line.strip().startswith("- "):
            if line.strip() < entry.strip():
                insert_at = cursor + 1
            else:
                insert_at = cursor
                break
        cursor += 1
    else:
        insert_at = cursor

    lines.insert(insert_at, entry)
    _files.write_text(path, "\n".join(lines) + "\n")
    return True


def patch_pyproject_packages(path: Path, package: str) -> bool:
    source = _files.read_text(path)
    if f'"{package}"' in source:
        return False
    match = re.search(r"(packages\s*=\s*\[)(.*?)(\])", source, re.S)
    if match is None:
        return False
    body = match.group(2)
    entries = [item.strip() for item in body.split(",") if item.strip()]
    entries.append(f'"{package}"')
    entries.sort(key=lambda item: item.strip('"'))
    rendered = "\n" + ",\n".join(f"    {entry}" for entry in entries) + "\n"
    source = source[: match.start(2)] + rendered + source[match.end(2) :]
    _files.write_text(path, source)
    return True


_VERSION_MINOR_RE = re.compile(
    r"^[^\S\n]*(?:const\s+)?(?:uint32_t|unsigned\s+int|int)\s+versionMinor\s*=\s*(\d+)",
    re.M,
)


def read_api_version_minor(path: Path) -> int | None:
    """The ``versionMinor`` tag in CwAPI3DVersion.h -- the cadwork build number.

    ``versionMajor`` is deliberately ignored: it carries the marketing year (2026)
    while the published package's major is the cadwork product major (33), and PyPI
    accepts no version that sorts below one already uploaded.
    """
    try:
        source = _files.read_text(path)
    except OSError:
        return None
    match = _VERSION_MINOR_RE.search(source)
    return int(match.group(1)) if match else None


@dataclass
class VersionChange:
    old: str
    new: str
    warning: str | None = None


def sync_version(path: Path, api_minor: int | None) -> VersionChange | None:
    """Set ``[project].version`` from the C++ ``versionMinor``, keeping the major.

    A build number the stubs have not shipped for yet resets the patch
    (``33.322.7`` -> ``33.328.0``). The same build number means this is another sync
    against an API the package already ships for, so only the patch moves
    (``33.328.0`` -> ``33.328.1``). Either way the version has to move: PyPI never
    accepts a re-upload, and the publish workflow fires on every push touching
    ``src/**``.

    Returns None when ``[project].version`` could not be found -- the caller warns.
    """
    source = _files.read_text(path)
    match = re.search(r'^(version\s*=\s*")(\d+)\.(\d+)\.(\d+)(")', source, re.M)
    if match is None:
        return None
    major, minor, patch = match.group(2), int(match.group(3)), int(match.group(4))
    old = f"{major}.{minor}.{patch}"
    warning: str | None = None
    if api_minor is None:
        new = f"{major}.{minor}.{patch + 1}"
        warning = (
            "no versionMinor found in the CwAPI3D version header -- fell back to a "
            f"patch bump ({old} -> {new}); confirm the version is right before release"
        )
    elif api_minor > minor:
        new = f"{major}.{api_minor}.0"
    else:
        new = f"{major}.{minor}.{patch + 1}"
        if api_minor < minor:
            # Syncing against an older cadlib checkout. Following it down would
            # produce a version PyPI has already seen.
            warning = (
                f"CwAPI3D versionMinor is {api_minor} but the package is already at "
                f"{old} -- kept the higher minor and bumped the patch instead "
                f"({old} -> {new}). Point [paths].cadlib_root at the newer source if "
                "that is not intended."
            )
    source = (
        source[: match.start()]
        + f"{match.group(1)}{new}{match.group(5)}"
        + source[match.end() :]
    )
    _files.write_text(path, source)
    return VersionChange(old=old, new=new, warning=warning)


def create_controller_package(src_dir: Path, module: str) -> Path:
    package = src_dir / module
    package.mkdir(parents=True, exist_ok=True)
    (package / "py.typed").write_bytes(b"")
    init = package / "__init__.pyi"
    if not init.is_file():
        title = _title_case(module)
        _files.write_text(init, f'"""{title}.\n\nTODO: describe this module\'s domain -- the C++ bindings carry no\n'
            f'module-level documentation to derive it from.\n"""\n')
    return init
