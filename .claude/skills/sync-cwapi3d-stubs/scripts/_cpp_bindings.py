#!/usr/bin/env python3
"""Extract the full pybind11 inventory.

Three passes over the translation unit:

  A  trampoline index  -- every ``<ret> cwp_<name>(<params>)`` free function, plus
                          the C++ interface accessor + method its body forwards to.
  B  module bodies     -- every ``PYBIND11_EMBEDDED_MODULE(<name>, m)`` and the
                          ``m.def("<python_name>", &<symbol>)`` calls inside it.
  C  cadwork types     -- ``py::class_<T>(m, "name")`` / ``py::enum_<E>(m, "name")``
                          chains and the one ``m.attr("alias") = <enum>`` alias.

Everything is resolved by SYMBOL, never by transforming the Python name: the
source contains genuine aliases (``set_framed_wall`` -> ``cwp_..._set_wall``) and
at least one upstream typo (``get_total_dimension`` -> ``..._get_total_direction``).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

_MODULE_RE = re.compile(r'^PYBIND11_EMBEDDED_MODULE\(\s*(\w+)\s*,\s*\w+\s*\)', re.M)
_TRAMPOLINE_START_RE = re.compile(r'^([A-Za-z_][\w:<>,*&\s]*?)\s+(cwp_\w+)\s*\(', re.M)
_FORWARD_RE = re.compile(r'getFactory\(\)\s*->\s*(\w+)\(\)\s*->\s*(\w+)\s*\(')
# Some trampolines cache the controller in a local first:
#   auto* lController = ...getFactory()->getElementController();
#   const auto lResult = lController->getElementActivePoint(a0);
_ACCESSOR_RE = re.compile(r'getFactory\(\)\s*->\s*(get\w+Controller)\(\)')
_LOCAL_CALL_RE = re.compile(r'\bl[A-Z]\w*\s*->\s*(\w+)\s*\(')
_STATIC_CAST_RE = re.compile(r'static_cast\s*<\s*([\w:]+)\s*>\s*\(\s*(\w+)\s*\)')
_CLASS_RE = re.compile(r'py::class_\s*<')
_ENUM_RE = re.compile(r'py::enum_\s*<')
_ATTR_ALIAS_RE = re.compile(r'^\s*m\.attr\("(\w+)"\)\s*=\s*(\w+)\s*;', re.M)
_ENUM_VAR_RE = re.compile(r'^\s*auto\s+(\w+)\s*=\s*$|^\s*auto\s+(\w+)\s*=\s*py::enum_')


@dataclass(frozen=True)
class Trampoline:
    """A ``cwp_*`` free function -- the signature carrier for one binding."""

    symbol: str
    return_type: str
    param_types: tuple[str, ...]
    param_names: tuple[str, ...]
    accessor: str | None  # e.g. "getBimController"
    cpp_method: str | None  # e.g. "getIfcGuid"
    # Enums cross the pybind11 boundary as plain ints and are cast back inside the
    # trampoline. This recovers the real type per parameter position:
    #   leaveWorkingPlane(static_cast<CwAPI3D::workingPlaneExitView>(a0))
    param_casts: tuple[str | None, ...] = ()


@dataclass(frozen=True)
class Binding:
    """One ``m.def(...)`` inside a ``PYBIND11_EMBEDDED_MODULE`` body."""

    module: str
    python_name: str
    symbol: str | None
    arg_names: tuple[str, ...]
    arg_defaults: tuple[str | None, ...]
    is_lambda: bool
    line: int


@dataclass
class CadworkType:
    """A ``py::class_`` or ``py::enum_`` registration in the ``cadwork`` module."""

    python_name: str
    cpp_type: str
    kind: str  # "class" | "enum"
    line: int
    methods: list[tuple[str, str]] = field(default_factory=list)  # (py_name, cpp_member)
    fields: list[tuple[str, str, bool]] = field(default_factory=list)  # (name, member, writable)
    init_signatures: list[tuple[str, ...]] = field(default_factory=list)
    # (python member name, C++ member expression)
    values: list[tuple[str, str]] = field(default_factory=list)
    aliases: list[str] = field(default_factory=list)


@dataclass
class Inventory:
    trampolines: dict[str, Trampoline]
    bindings: list[Binding]
    types: list[CadworkType]

    def modules(self) -> list[str]:
        seen: list[str] = []
        for binding in self.bindings:
            if binding.module not in seen:
                seen.append(binding.module)
        return seen


# ---------------------------------------------------------------------------
# small scanning helpers
# ---------------------------------------------------------------------------


def _skip_string(text: str, index: int) -> int:
    """Return the index just past the string literal starting at `index`."""
    quote = text[index]
    index += 1
    while index < len(text):
        if text[index] == '\\':
            index += 2
            continue
        if text[index] == quote:
            return index + 1
        index += 1
    return index


def _match_parens(text: str, open_index: int) -> int:
    """Index of the ``)`` matching the ``(`` at `open_index`, string/brace aware."""
    depth = 0
    index = open_index
    while index < len(text):
        char = text[index]
        if char in '"\'':
            index = _skip_string(text, index)
            continue
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
            if depth == 0:
                return index
        index += 1
    raise ValueError(f'unbalanced parentheses from offset {open_index}')


def _split_top_level(text: str, separator: str = ',') -> list[str]:
    """Split on `separator` at nesting depth 0 of ``()``, ``<>``, ``[]``, ``{}``."""
    parts: list[str] = []
    depth = 0
    current: list[str] = []
    index = 0
    while index < len(text):
        char = text[index]
        if char in '"\'':
            end = _skip_string(text, index)
            current.append(text[index:end])
            index = end
            continue
        if char in '(<[{':
            depth += 1
        elif char in ')>]}':
            depth -= 1
        elif char == separator and depth == 0:
            parts.append(''.join(current).strip())
            current = []
            index += 1
            continue
        current.append(char)
        index += 1
    tail = ''.join(current).strip()
    if tail:
        parts.append(tail)
    return parts


def _normalize_type(raw: str) -> str:
    """Strip cv/ref decoration and collapse whitespace on a C++ type."""
    text = raw.strip()
    text = re.sub(r'\bconst\b', ' ', text)
    text = text.replace('&', ' ')
    text = re.sub(r'\s*([<>,*])\s*', r'\1', text)
    text = re.sub(r',', ', ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def _split_param(raw: str) -> tuple[str, str]:
    """Split one C++ parameter declaration into (type, name)."""
    text = raw.strip()
    if not text or text == 'void':
        return ('', '')
    text = text.split('=', 1)[0].strip()
    match = re.search(r'(\w+)\s*$', text)
    if match and not re.fullmatch(r'[\w:]+', text):
        name = match.group(1)
        type_part = text[: match.start(1)]
        return (_normalize_type(type_part), name)
    return (_normalize_type(text), '')


# ---------------------------------------------------------------------------
# pass A -- trampolines
# ---------------------------------------------------------------------------


def _parse_trampolines(text: str) -> dict[str, Trampoline]:
    result: dict[str, Trampoline] = {}
    for match in _TRAMPOLINE_START_RE.finditer(text):
        return_type = _normalize_type(match.group(1))
        symbol = match.group(2)
        open_index = match.end() - 1
        try:
            close_index = _match_parens(text, open_index)
        except ValueError:
            continue
        # A declaration ends in ';', a definition in '{'. Only definitions carry a body.
        tail = text[close_index + 1 : close_index + 200].lstrip()
        if not tail.startswith('{'):
            continue
        params_raw = text[open_index + 1 : close_index]
        types: list[str] = []
        names: list[str] = []
        for chunk in _split_top_level(params_raw):
            param_type, param_name = _split_param(chunk)
            if not param_type:
                continue
            types.append(param_type)
            names.append(param_name)

        body_start = text.index('{', close_index)
        body_end = text.find('\n}', body_start)
        body = text[body_start : body_end if body_end != -1 else body_start + 4000]
        forward = _FORWARD_RE.search(body)
        if forward is not None:
            accessor: str | None = forward.group(1)
            cpp_method: str | None = forward.group(2)
        else:
            accessor_match = _ACCESSOR_RE.search(body)
            local_match = _LOCAL_CALL_RE.search(body)
            accessor = accessor_match.group(1) if accessor_match else None
            cpp_method = local_match.group(1) if local_match else None

        casts = {cast.group(2): cast.group(1) for cast in _STATIC_CAST_RE.finditer(body)}
        result[symbol] = Trampoline(
            symbol=symbol,
            return_type=return_type,
            param_types=tuple(types),
            param_names=tuple(names),
            accessor=accessor,
            cpp_method=cpp_method,
            param_casts=tuple(casts.get(name) for name in names),
        )
    return result


# ---------------------------------------------------------------------------
# pass B -- module bodies and m.def calls
# ---------------------------------------------------------------------------


def _module_spans(text: str) -> list[tuple[str, int, int]]:
    """(module_name, body_start, body_end) for every embedded module."""
    spans: list[tuple[str, int, int]] = []
    for match in _MODULE_RE.finditer(text):
        name = match.group(1)
        brace = text.index('{', match.end())
        # Inner braces are always indented in this file; the body terminator is the
        # first '}' at column 0 after the opening brace.
        end = text.find('\n}', brace)
        end = len(text) if end == -1 else end + 1
        spans.append((name, brace, end))
    return spans


def _parse_def_call(module: str, body: str, offset: int, base_line: int) -> Binding | None:
    open_index = body.index('(', offset)
    close_index = _match_parens(body, open_index)
    inner = body[open_index + 1 : close_index]
    parts = _split_top_level(inner)
    if not parts:
        return None
    name_match = re.match(r'^"([^"]+)"$', parts[0].strip())
    if name_match is None:
        return None
    python_name = name_match.group(1)

    symbol: str | None = None
    is_lambda = False
    if len(parts) > 1:
        target = parts[1].strip()
        if target.startswith('[') or '->' in target[:3]:
            is_lambda = True
            inner_call = re.search(r'\b(cwp_\w+)\s*\(', target)
            if inner_call:
                symbol = inner_call.group(1)
        else:
            symbol_match = re.match(r'^&?\s*([\w:]+)\s*$', target)
            if symbol_match:
                symbol = symbol_match.group(1).split('::')[-1]

    arg_names: list[str] = []
    arg_defaults: list[str | None] = []
    for part in parts[2:]:
        arg_match = re.match(r'py::arg\("(\w+)"\)\s*(?:=\s*(.+))?$', part.strip(), re.S)
        if arg_match:
            arg_names.append(arg_match.group(1))
            default = arg_match.group(2)
            arg_defaults.append(default.strip() if default else None)

    line = base_line + body.count('\n', 0, offset)
    return Binding(
        module=module,
        python_name=python_name,
        symbol=symbol,
        arg_names=tuple(arg_names),
        arg_defaults=tuple(arg_defaults),
        is_lambda=is_lambda,
        line=line,
    )


def _parse_bindings(text: str, spans: list[tuple[str, int, int]]) -> list[Binding]:
    bindings: list[Binding] = []
    for module, start, end in spans:
        body = text[start:end]
        base_line = text.count('\n', 0, start) + 1
        for match in re.finditer(r'\bm\.def\s*\(', body):
            try:
                binding = _parse_def_call(module, body, match.start(), base_line)
            except ValueError:
                continue
            if binding is not None:
                bindings.append(binding)
    return bindings


# ---------------------------------------------------------------------------
# pass C -- cadwork classes and enums
# ---------------------------------------------------------------------------


def _chain_end(text: str, start: int) -> int:
    """Index of the ``;`` closing a ``py::class_``/``py::enum_`` builder chain."""
    depth = 0
    index = start
    while index < len(text):
        char = text[index]
        if char in '"\'':
            index = _skip_string(text, index)
            continue
        if char in '([{':
            depth += 1
        elif char in ')]}':
            depth -= 1
        elif char == ';' and depth <= 0:
            return index
        index += 1
    return len(text)


def _template_arg(text: str, open_angle: int) -> tuple[str, int]:
    depth = 0
    index = open_angle
    while index < len(text):
        if text[index] == '<':
            depth += 1
        elif text[index] == '>':
            depth -= 1
            if depth == 0:
                return (text[open_angle + 1 : index], index)
        index += 1
    raise ValueError('unbalanced template brackets')


def _parse_types(text: str, span: tuple[str, int, int]) -> list[CadworkType]:
    _, start, end = span
    body = text[start:end]
    base_line = text.count('\n', 0, start) + 1
    types: list[CadworkType] = []
    by_variable: dict[str, CadworkType] = {}

    for kind, pattern in (('class', _CLASS_RE), ('enum', _ENUM_RE)):
        for match in pattern.finditer(body):
            angle = body.index('<', match.start())
            try:
                template_args, close_angle = _template_arg(body, angle)
            except ValueError:
                continue
            cpp_type = _split_top_level(template_args)[0].strip()
            paren = body.index('(', close_angle)
            call_end = _match_parens(body, paren)
            call_args = _split_top_level(body[paren + 1 : call_end])
            if len(call_args) < 2:
                continue
            name_match = re.match(r'^"([^"]+)"$', call_args[1].strip())
            if name_match is None:
                continue
            entry = CadworkType(
                python_name=name_match.group(1),
                cpp_type=cpp_type,
                kind=kind,
                line=base_line + body.count('\n', 0, match.start()),
            )
            chain = body[call_end : _chain_end(body, call_end)]
            _fill_chain(entry, chain)
            types.append(entry)

            # `auto <var> = py::enum_<...>` -- remember for m.attr alias resolution.
            line_start = body.rfind('\n', 0, match.start()) + 1
            prefix = body[line_start : match.start()]
            var_match = re.search(r'\bauto\s+(\w+)\s*=\s*$', prefix)
            if var_match:
                by_variable[var_match.group(1)] = entry

    for alias_match in _ATTR_ALIAS_RE.finditer(body):
        alias, variable = alias_match.group(1), alias_match.group(2)
        target = by_variable.get(variable)
        if target is not None:
            target.aliases.append(alias)

    types.sort(key=lambda entry: entry.line)
    return types


def _fill_chain(entry: CadworkType, chain: str) -> None:
    for match in re.finditer(r'\.def_(readwrite|readonly)\s*\(', chain):
        open_index = chain.index('(', match.start())
        args = _split_top_level(chain[open_index + 1 : _match_parens(chain, open_index)])
        if len(args) >= 2:
            name_match = re.match(r'^"([^"]+)"$', args[0].strip())
            if name_match:
                entry.fields.append(
                    (
                        name_match.group(1),
                        args[1].strip().lstrip('&'),
                        match.group(1) == 'readwrite',
                    )
                )

    for match in re.finditer(r'\.def\s*\(', chain):
        open_index = chain.index('(', match.start())
        try:
            args = _split_top_level(chain[open_index + 1 : _match_parens(chain, open_index)])
        except ValueError:
            continue
        if not args:
            continue
        first = args[0].strip()
        if first.startswith('py::init'):
            init_angle = first.find('<')
            if init_angle != -1:
                try:
                    template_args, _ = _template_arg(first, init_angle)
                except ValueError:
                    continue
                entry.init_signatures.append(
                    tuple(_normalize_type(part) for part in _split_top_level(template_args) if part.strip())
                )
            continue
        name_match = re.match(r'^"([^"]+)"$', first)
        if name_match is None:
            continue
        member = args[1].strip().lstrip('&') if len(args) > 1 else ''
        entry.methods.append((name_match.group(1), member))

    for match in re.finditer(r'\.value\s*\(\s*"(\w+)"\s*,\s*([\w:]+)', chain):
        entry.values.append((match.group(1), match.group(2)))


# ---------------------------------------------------------------------------
# C++ enum definitions -- the real numeric values and their trailing ///< docs
# ---------------------------------------------------------------------------

_ENUM_DEF_RE = re.compile(r'\benum\s+(?:class\s+|struct\s+)?(\w+)\s*(?::\s*[\w:]+\s*)?\{', re.M)


@dataclass(frozen=True)
class EnumMember:
    name: str
    value: int
    doc: str


def parse_enum_definitions(search_dirs: list[Path]) -> dict[str, list[EnumMember]]:
    """Map bare C++ enum name -> its members with resolved values.

    Values follow the C++ rule: implicit members continue from the previous one,
    an explicit ``= N`` (decimal or hex) resets the counter, and ``= OTHER``
    aliases an earlier member of the same enum. Anything else stops the enum
    from being emitted rather than guessing.

    More than one directory is searched because not every enum a binding exposes
    lives under include/ -- ``OnStateChange`` is declared in the project root's
    ICwAPI3DEventObserver.h.
    """
    result: dict[str, list[EnumMember]] = {}
    headers = sorted({header for directory in search_dirs for header in directory.glob('*.h')})
    for header in headers:
        text = header.read_text(encoding='utf-8', errors='replace')
        for match in _ENUM_DEF_RE.finditer(text):
            name = match.group(1)
            brace = text.index('{', match.start())
            close = text.find('};', brace)
            if close == -1:
                continue
            members: list[EnumMember] = []
            by_name: dict[str, int] = {}
            counter = 0
            failed = False
            for raw_line in text[brace + 1 : close].splitlines():
                line = raw_line.strip()
                doc = ''
                doc_match = re.search(r'///<\s*(.*)$', line)
                if doc_match:
                    doc = doc_match.group(1).strip()
                    line = line[: doc_match.start()].strip()
                line = re.sub(r'//.*$', '', line).strip().rstrip(',').strip()
                if not line or line.startswith('/'):
                    continue
                if '=' in line:
                    member, _, expression = line.partition('=')
                    member = member.strip()
                    expression = expression.strip()
                    if re.fullmatch(r'-?0[xX][0-9a-fA-F]+', expression):
                        counter = int(expression, 16)
                    elif re.fullmatch(r'-?\d+', expression):
                        counter = int(expression)
                    elif expression.split('::')[-1] in by_name:
                        counter = by_name[expression.split('::')[-1]]
                    else:
                        failed = True
                        break
                else:
                    member = line
                if not re.fullmatch(r'\w+', member):
                    failed = True
                    break
                members.append(EnumMember(name=member, value=counter, doc=doc))
                by_name[member] = counter
                counter += 1
            if not failed and members:
                result.setdefault(name, members)
    return result


# ---------------------------------------------------------------------------
# entry point
# ---------------------------------------------------------------------------


def parse(path: Path) -> Inventory:
    text = path.read_text(encoding='utf-8', errors='replace')
    spans = _module_spans(text)
    cadwork_span = next((span for span in spans if span[0] == 'cadwork'), None)
    return Inventory(
        trampolines=_parse_trampolines(text),
        bindings=_parse_bindings(text, spans),
        types=_parse_types(text, cadwork_span) if cadwork_span else [],
    )
