#!/usr/bin/env python3
"""Index the Doxygen contracts on the ICwAPI3D* interface headers.

Those headers are the documentation surface plugin authors read, so they carry
everything a Python docstring needs that the pybind11 layer throws away: a
``@brief``, ``@param`` entries with REAL names and prose, a ``@return`` with
prose, and often a ``@par Example`` code block.

The join key back to a binding is (interface accessor, C++ method name), both
recovered from the ``cwp_*`` trampoline body -- see _cpp_bindings.Trampoline.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

_VIRTUAL_RE = re.compile(
    r"^\s*virtual\s+(?P<ret>[\w:<>,*&\s]+?)\s+(?P<name>\w+)\s*\((?P<params>[^;]*?)\)\s*"
    r"(?:const\s*)?=\s*0\s*;",
    re.M,
)
_PARAM_RE = re.compile(
    r"@param\s*(?:\[[^\]]*\])?\s*(?P<name>\w+)\s*(?:\[(?P<type>[^\]]*)\])?\s*(?P<desc>.*)"
)
_RETURN_RE = re.compile(
    r"@(?:return|result)s?\s*(?:\[(?P<type>[^\]]*)\])?\s*(?P<desc>.*)"
)
_REF_RE = re.compile(r"@ref\s+")


@dataclass
class DocBlock:
    interface: str
    method: str
    brief: str = ""
    # (name, doxygen type hint, description)
    params: list[tuple[str, str, str]] = field(default_factory=list)
    returns: str = ""
    returns_hint: str = ""
    note: str = ""
    example: list[str] = field(default_factory=list)
    deprecated: str = ""

    @property
    def is_thin(self) -> bool:
        return not self.brief


def camel_to_snake(name: str) -> str:
    """``aElementIDList`` -> ``element_id_list``; ``aP1`` -> ``p1``."""
    text = name
    if re.match(r"^a[A-Z0-9]", text):
        text = text[1:]
    text = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", text)
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)
    return text.lower().strip("_")


def _clean(text: str) -> str:
    text = _REF_RE.sub("", text)
    text = text.replace("@li", "-")
    return re.sub(r"\s+", " ", text).strip()


def _comment_lines_above(lines: list[str], index: int) -> list[str]:
    """The contiguous ``///`` or ``/** */`` block immediately above `index`."""
    collected: list[str] = []
    cursor = index - 1
    while cursor >= 0:
        stripped = lines[cursor].strip()
        if stripped.startswith("///"):
            collected.append(stripped[3:].strip())
            cursor -= 1
            continue
        if stripped.endswith("*/"):
            block: list[str] = []
            while cursor >= 0:
                inner = lines[cursor].strip()
                block.append(inner.removesuffix("*/").removeprefix("/**").lstrip("*").strip())
                if inner.startswith("/*"):
                    break
                cursor -= 1
            collected.extend(block)
            cursor -= 1
            continue
        break
    return list(reversed(collected))


def _normalize(raw_lines: list[str]) -> list[str]:
    """Neutralise the non-structural ``@`` commands before tag dispatch.

    A wrapped ``@param`` description routinely continues on a line that STARTS with
    ``@ref`` (see stretchFacet in ICwAPI3DGeometryController.h). Left alone, the
    dispatcher would read that as a new tag and drop the rest of the sentence.
    """
    normalized: list[str] = []
    for line in raw_lines:
        line = _REF_RE.sub("", line)
        line = re.sub(r"^@li\b\s*", "- ", line)
        line = line.replace("@li", "-")
        normalized.append(line.strip())
    return normalized


def _parse_block(interface: str, method: str, raw_lines: list[str]) -> DocBlock:
    block = DocBlock(interface=interface, method=method)
    raw_lines = _normalize(raw_lines)
    mode = ""
    buffer: list[str] = []

    def flush() -> None:
        nonlocal buffer
        text = _clean(" ".join(buffer))
        if text:
            if mode == "brief" and not block.brief:
                block.brief = text
            elif mode == "note":
                block.note = (block.note + " " + text).strip()
            elif mode == "deprecated":
                block.deprecated = (block.deprecated + " " + text).strip()
        buffer = []

    for line in raw_lines:
        if line.startswith("@code"):
            mode = "code"
            continue
        if line.startswith("@endcode"):
            mode = ""
            continue
        if mode == "code":
            block.example.append(line)
            continue
        if line.startswith("@brief"):
            flush()
            mode = "brief"
            buffer = [line[len("@brief") :]]
            continue
        if line.startswith("@param"):
            flush()
            mode = "param"
            match = _PARAM_RE.match(line)
            if match:
                block.params.append(
                    (
                        match.group("name"),
                        _clean(match.group("type") or ""),
                        _clean(match.group("desc") or ""),
                    )
                )
            continue
        if re.match(r"@(return|result)", line):
            flush()
            mode = "return"
            match = _RETURN_RE.match(line)
            if match:
                block.returns = _clean(match.group("desc") or "")
                block.returns_hint = _clean(match.group("type") or "")
            continue
        if line.startswith("@note"):
            flush()
            mode = "note"
            buffer = [line[len("@note") :]]
            continue
        if line.startswith("@deprecated"):
            flush()
            mode = "deprecated"
            buffer = [line[len("@deprecated") :]]
            continue
        if line.startswith("@par"):
            flush()
            mode = ""
            continue
        if line.startswith("@"):
            # @since / @author / @date / @ingroup / @interface -- not docstring material.
            flush()
            mode = ""
            continue
        if not line:
            flush()
            continue
        if mode == "param" and block.params:
            name, hint, desc = block.params[-1]
            block.params[-1] = (name, hint, _clean(f"{desc} {line}"))
            continue
        if mode == "return":
            block.returns = _clean(f"{block.returns} {line}")
            continue
        if mode in ("brief", "note", "deprecated"):
            buffer.append(line)
            continue
        if not block.brief:
            mode = "brief"
            buffer = [line]

    flush()
    return block


@dataclass
class DoxygenIndex:
    by_interface: dict[tuple[str, str], DocBlock]
    by_method: dict[str, list[DocBlock]]

    def lookup(self, accessor: str | None, method: str | None) -> DocBlock | None:
        if not method:
            return None
        if accessor:
            interface = "ICwAPI3D" + accessor.removeprefix("get")
            found = self.by_interface.get((interface, method))
            if found is not None:
                return found
        candidates = self.by_method.get(method, [])
        if len(candidates) == 1:
            return candidates[0]
        return None


def parse(include_dir: Path) -> DoxygenIndex:
    by_interface: dict[tuple[str, str], DocBlock] = {}
    by_method: dict[str, list[DocBlock]] = {}

    for header in sorted(include_dir.glob("ICwAPI3D*.h")):
        interface = header.stem
        text = header.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        for match in _VIRTUAL_RE.finditer(text):
            method = match.group("name")
            line_index = text.count("\n", 0, match.start())
            block = _parse_block(
                interface, method, _comment_lines_above(lines, line_index)
            )
            key = (interface, method)
            # Overloads share a name; keep the first (richest) documented one.
            if key not in by_interface or by_interface[key].is_thin:
                by_interface[key] = block
            by_method.setdefault(method, []).append(block)

    return DoxygenIndex(by_interface=by_interface, by_method=by_method)
