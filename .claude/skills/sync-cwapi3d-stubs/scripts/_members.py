#!/usr/bin/env python3
"""Members added to cadwork types that already have a stub.

``_cpp_bindings`` parses every ``.def`` / ``.def_readwrite`` / ``.value`` of a
``py::class_`` / ``py::enum_`` and ``_stubs`` knows which members each stub class
declares, but a type that is *present* was never compared member by member. This
module closes that gap: it diffs the two, and renders the missing members in the
shape the hand-written stubs already use.

Everything is additive: existing members are never touched or reordered.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import _cpp_bindings
import _emit
import _stubs

_INDENT = '    '

_STRUCT_RE = re.compile(r'^(?:struct|class)\s+(\w+)\b[^;{]*\{', re.M)
_MEMBER_RE = re.compile(
    r'^[ \t]+(?:inline\s+|static\s+|virtual\s+)*([\w:<>,\s\*&]+?)\s+(\w+)\s*\(([^)]*)\)\s*(?:const\s*)?(?:noexcept\s*)?\{',
    re.M,
)
_NOT_A_TYPE = {'return', 'if', 'else', 'while', 'for', 'switch', 'new', 'delete', 'throw', 'case'}


@dataclass(frozen=True)
class MemberSignature:
    return_type: str
    params: tuple[tuple[str, str], ...]  # (cpp type, name)


def _struct_body(text: str, open_brace: int) -> str:
    depth = 0
    index = open_brace
    while index < len(text):
        char = text[index]
        if char == '/':
            skipped = _cpp_bindings._skip_comment(text, index)
            if skipped != index:
                index = skipped
                continue
        if char in '"\'':
            index = _cpp_bindings._skip_string(text, index)
            continue
        if char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
            if depth == 0:
                break
        index += 1
    return text[open_brace + 1 : index]


def parse_member_signatures(controller: Path) -> dict[str, dict[str, MemberSignature]]:
    """``{struct: {member: signature}}`` for the wrapper structs the controller defines.

    ``.def("is_point_cloud", &element_type::is_point_cloud)`` carries a member
    pointer and nothing else, so the declaration is the only place the return type
    and the parameters exist.
    """
    text = controller.read_text(encoding='utf-8')
    result: dict[str, dict[str, MemberSignature]] = {}
    for match in _STRUCT_RE.finditer(text):
        body = _struct_body(text, match.end() - 1)
        members: dict[str, MemberSignature] = {}
        for member in _MEMBER_RE.finditer(body):
            return_type = _cpp_bindings._normalize_type(member.group(1))
            if return_type.split(' ')[0] in _NOT_A_TYPE:
                continue
            params: list[tuple[str, str]] = []
            for raw in _cpp_bindings._split_top_level(member.group(3)):
                raw = raw.split('=')[0].strip()
                parts = re.match(r'^(.*?)(\w+)$', raw)
                if raw and parts and parts.group(1).strip():
                    params.append((_cpp_bindings._normalize_type(parts.group(1)), parts.group(2)))
                elif raw:
                    params.append((_cpp_bindings._normalize_type(raw), f'arg{len(params)}'))
            members.setdefault(member.group(2), MemberSignature(return_type, tuple(params)))
        result[match.group(1)] = members
    return result


def missing_members(
    entry: _cpp_bindings.CadworkType,
    stub: _stubs.TypeStub,
    skip_patterns: list[re.Pattern[str]],
    definitions: dict[str, list[_cpp_bindings.EnumMember]] | None = None,
) -> list[str]:
    """Bound member names the stub's class does not declare, in C++ registration order."""
    declared = stub.members.get(entry.python_name)
    if declared is None:
        # The stub file holds a class under another name (alias) -- not comparable.
        return []
    if entry.kind == 'enum':
        names = [name for name, _ in entry.values]
        if definitions is not None:
            # A C++ alias (btl_1_0 == btlx_1_0) cannot be added to a @unique stub enum, so
            # it is not a gap -- reporting it would keep every run at "gaps found".
            stub_values = {
                int(value) for value in re.findall(r'^\s+\w+ = (-?\d+)\s*$', _read(stub.path), re.M)
            }
            by_name = {member.name: member.value for member in definitions.get(entry.cpp_type.split('::')[-1], [])}
            cpp_for = dict(entry.values)
            names = [
                name
                for name in names
                if by_name.get(cpp_for[name].split('::')[-1]) not in stub_values
            ]
    else:
        names = [name for name, _ in entry.methods if not name.startswith('__')]
        names += [name for name, _member, _writable in entry.fields]
        names = [name for name in names if not any(pattern.search(name) for pattern in skip_patterns)]
    seen: set[str] = set()
    result: list[str] = []
    for name in names:
        if name in declared or name in seen:
            continue
        seen.add(name)
        result.append(name)
    return result


def _read(path: Path) -> str:
    return path.read_text(encoding='utf-8')


@dataclass
class RenderedMembers:
    lines: list[str]
    imports: set[str]
    warnings: list[str]


def render_class_members(
    entry: _cpp_bindings.CadworkType,
    names: list[str],
    resolver: _emit.TypeResolver,
    signatures: dict[str, MemberSignature],
) -> RenderedMembers:
    """Method and field stubs in the style of the hand-written ``element_type`` stub."""
    lines: list[str] = []
    imports: set[str] = set()
    warnings: list[str] = []
    method_members = dict(entry.methods)
    field_names = {name for name, _member, _writable in entry.fields}

    for index, name in enumerate(names):
        if index:
            lines.append('')
        if name in field_names and name not in method_members:
            lines.append(f'{_INDENT}{name}: Any')
            lines.append(f'{_INDENT}"""{name.replace("_", " ")}."""')
            warnings.append(f'cadwork.{entry.python_name}.{name}: field type not recoverable -- annotated Any')
            continue

        member_name = method_members[name].split('::')[-1]
        signature = signatures.get(member_name)
        params: list[str] = []
        if signature is None:
            returns = 'Any'
            warnings.append(
                f'cadwork.{entry.python_name}.{name}: no C++ declaration found -- signature annotated Any'
            )
            doc_params: list[str] = []
        else:
            returns, needed = resolver.resolve(signature.return_type)
            if needed:
                imports.add(needed)
            doc_params = []
            for cpp_type, param_name in signature.params:
                annotation, needed = resolver.resolve(cpp_type)
                if needed:
                    imports.add(needed)
                params.append(f'{_snake(param_name)}: {annotation}')
                doc_params.append(f'{_INDENT * 3}{_snake(param_name)}: {annotation}')
        lines.append(f'{_INDENT}def {name}({", ".join(["self", *params])}) -> {returns}:')
        lines.append(f'{_INDENT * 2}"""{name.replace("_", " ")}')
        if doc_params:
            lines += ['', f'{_INDENT * 2}Parameters:', *doc_params]
        lines += ['', f'{_INDENT * 2}Returns:', f'{_INDENT * 3}{returns}', f'{_INDENT * 2}"""']
    return RenderedMembers(lines, imports, warnings)


def _snake(name: str) -> str:
    name = re.sub(r'^[a-z]?(?=[A-Z])', '', name) if re.match(r'^a[A-Z]', name) else name
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


def render_enum_members(
    entry: _cpp_bindings.CadworkType,
    names: list[str],
    definitions: dict[str, list[_cpp_bindings.EnumMember]],
    taken_values: set[int],
) -> RenderedMembers:
    """Enum members; a value the stub already uses is an alias and is not written.

    The repo's enum stubs are ``@unique``, which rejects two names for one value.
    """
    bare = entry.cpp_type.split('::')[-1]
    by_name = {member.name: member for member in definitions.get(bare, [])}
    cpp_for = dict(entry.values)
    lines: list[str] = []
    warnings: list[str] = []
    for name in names:
        member = by_name.get(cpp_for[name].split('::')[-1])
        if member is None:
            warnings.append(
                f'cadwork.{entry.python_name}.{name}: no C++ value found for {cpp_for[name]} -- NOT written'
            )
            continue
        if member.value in taken_values:
            warnings.append(
                f'cadwork.{entry.python_name}.{name}: value {member.value} is already taken by another '
                'member of the stub (@unique) -- C++ alias NOT written'
            )
            continue
        taken_values.add(member.value)
        lines.append(f'{_INDENT}{name} = {member.value}')
        lines.append(f'{_INDENT}"""{_emit.docstring_safe(member.doc)}"""')
    return RenderedMembers(lines, set(), warnings)
