#!/usr/bin/env python3
"""Text IO that preserves each file's existing line endings.

Every tracked file in the stub repo is CRLF. Writing LF back would turn a
three-line insertion into a whole-file diff and bury the actual change, so reads
are newline-agnostic and writes re-apply whatever terminator the file already
used (LF for files this tool creates).
"""

from __future__ import annotations

from pathlib import Path


_DEFAULT_NEWLINE = '\n'


def set_default_newline(anchor: Path) -> str:
    """Adopt `anchor`'s line ending for files this tool creates from scratch.

    New files should match the repo they land in, not the platform running the
    generator.
    """
    global _DEFAULT_NEWLINE
    _DEFAULT_NEWLINE = detect_newline(anchor)
    return _DEFAULT_NEWLINE


def detect_newline(path: Path, default: str | None = None) -> str:
    default = _DEFAULT_NEWLINE if default is None else default
    if not path.is_file():
        return default
    with path.open('rb') as handle:
        sample = handle.read(65536)
    if b'\r\n' in sample:
        return '\r\n'
    if b'\n' in sample:
        return '\n'
    return default


def read_text(path: Path) -> str:
    """Read with universal newlines: the returned text always uses ``\\n``."""
    return path.read_text(encoding='utf-8')


def write_text(path: Path, text: str, newline: str | None = None) -> None:
    """Write `text` (LF-separated) back using the file's own line ending."""
    terminator = newline if newline is not None else detect_newline(path)
    with path.open('w', encoding='utf-8', newline='') as handle:
        handle.write(text.replace('\r\n', '\n').replace('\n', terminator))


def write_lines(path: Path, lines: list[str], newline: str | None = None) -> None:
    write_text(path, '\n'.join(lines) + '\n', newline)
