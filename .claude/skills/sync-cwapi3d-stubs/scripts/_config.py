#!/usr/bin/env python3
"""Config loader for the cwapi3d stub sync.

Two files, discovered by independent upward walks from CWD (falling back to the
directory holding this script), deep-merged with the personal file winning:

    config.toml           versioned, shared
    config.personal.toml  git-ignored, machine paths only

Env overrides (absolute paths): CWSTUBS_CONFIG, CWSTUBS_PERSONAL_CONFIG.
Setting CWSTUBS_CONFIG suppresses the personal-file walk, so a pinned run cannot
pick up a stray personal file.

Exit codes used by callers: 2 = missing/invalid config.
"""

from __future__ import annotations

import os
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

CONFIG_FILENAME = "config.toml"
PERSONAL_CONFIG_FILENAME = "config.personal.toml"

_SKILL_DIR = Path(__file__).resolve().parent.parent


class ConfigError(Exception):
    """Config could not be located, parsed, or validated."""


def _walk_up(filename: str, start: Path) -> Path | None:
    for directory in (start, *start.parents):
        candidate = directory / filename
        if candidate.is_file():
            return candidate
    return None


def _find(filename: str, env_var: str) -> Path | None:
    override = os.environ.get(env_var)
    if override:
        path = Path(override)
        if not path.is_file():
            raise ConfigError(f"{env_var} points at a missing file: {path}")
        return path
    # The skill dir is checked first: it is where the pair actually lives.
    beside_skill = _SKILL_DIR / filename
    if beside_skill.is_file():
        return beside_skill
    return _walk_up(filename, Path.cwd().resolve())


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """Merge `override` INTO `base`, returning a new dict.

    Nested tables merge key-by-key so a personal file can override one field of a
    section without restating it. Every other value -- scalars and arrays alike --
    is replaced wholesale. `override` wins on every conflict.
    """
    merged = dict(base)
    for key, value in override.items():
        existing = merged.get(key)
        if isinstance(existing, dict) and isinstance(value, dict):
            merged[key] = _deep_merge(existing, value)
        else:
            merged[key] = value
    return merged


def _read_toml(path: Path) -> dict[str, Any]:
    try:
        return tomllib.loads(path.read_text(encoding="utf-8"))
    except (tomllib.TOMLDecodeError, UnicodeDecodeError) as error:
        raise ConfigError(f"{path}: {error}") from error


def _git_root(start: Path) -> Path | None:
    for directory in (start, *start.parents):
        if (directory / ".git").exists():
            return directory
    return None


@dataclass(frozen=True)
class Config:
    raw: dict[str, Any]
    config_path: Path
    personal_path: Path | None

    # --- resolved roots -------------------------------------------------
    cadlib_root: Path
    stub_repo: Path

    # --- resolved source files ------------------------------------------
    python_controller: Path
    interface_include_dir: Path
    enum_search_dirs: tuple[Path, ...]

    # --- resolved targets ------------------------------------------------
    src_dir: Path
    docs_dir: Path
    mkdocs: Path
    pyproject: Path
    compare_branch: str

    def section(self, name: str) -> dict[str, Any]:
        value = self.raw.get(name, {})
        return value if isinstance(value, dict) else {}

    @property
    def blacklist_modules(self) -> set[str]:
        return set(self.section("blacklist").get("modules", []))

    @property
    def blacklist_methods(self) -> set[str]:
        return set(self.section("blacklist").get("methods", []))

    @property
    def blacklist_qualified(self) -> set[str]:
        return set(self.section("blacklist").get("qualified", []))

    @property
    def blacklist_types(self) -> set[str]:
        return set(self.section("blacklist").get("types", []))

    @property
    def blacklist_class_method_patterns(self) -> list[str]:
        return list(self.section("blacklist").get("class_method_patterns", []))

    @property
    def type_map(self) -> dict[str, str]:
        return dict(self.section("type_map"))

    @property
    def param_names(self) -> dict[str, str]:
        return dict(self.section("param_names"))

    @property
    def hint_map(self) -> dict[str, str]:
        return dict(self.section("doxygen_hint_map"))

    @property
    def enums_page(self) -> str:
        return str(self.section("emit").get("enums_page", "enums.md"))

    @property
    def bump_version(self) -> bool:
        return bool(self.section("emit").get("bump_version", True))


def load() -> Config:
    config_path = _find(CONFIG_FILENAME, "CWSTUBS_CONFIG")
    if config_path is None:
        raise ConfigError(
            f"no {CONFIG_FILENAME} found beside the skill or above {Path.cwd()}"
        )
    raw = _read_toml(config_path)

    personal_path: Path | None = None
    if not os.environ.get("CWSTUBS_CONFIG"):
        personal_path = _find(PERSONAL_CONFIG_FILENAME, "CWSTUBS_PERSONAL_CONFIG")
        if personal_path is not None:
            raw = _deep_merge(raw, _read_toml(personal_path))

    paths = raw.get("paths", {})
    cadlib_raw = paths.get("cadlib_root")
    if not cadlib_raw:
        raise ConfigError(
            "[paths].cadlib_root is not set. Copy "
            f"{PERSONAL_CONFIG_FILENAME}.example to {PERSONAL_CONFIG_FILENAME} "
            f"in {_SKILL_DIR} and set it."
        )
    cadlib_root = Path(cadlib_raw).resolve()
    if not cadlib_root.is_dir():
        raise ConfigError(f"[paths].cadlib_root does not exist: {cadlib_root}")

    stub_raw = paths.get("stub_repo")
    if stub_raw:
        stub_repo = Path(stub_raw).resolve()
    else:
        discovered = _git_root(config_path.resolve().parent)
        if discovered is None:
            raise ConfigError(
                "[paths].stub_repo is unset and no git root was found above "
                f"{config_path}"
            )
        stub_repo = discovered
    if not stub_repo.is_dir():
        raise ConfigError(f"[paths].stub_repo does not exist: {stub_repo}")

    source = raw.get("source", {})
    target = raw.get("target", {})

    python_controller = cadlib_root / source.get(
        "python_controller", "CwAPI3D/CCwAPI3DPythonController.cpp"
    )
    interface_include_dir = cadlib_root / source.get(
        "interface_include_dir", "CwAPI3D/include"
    )
    if not python_controller.is_file():
        raise ConfigError(f"binding source not found: {python_controller}")
    if not interface_include_dir.is_dir():
        raise ConfigError(f"interface include dir not found: {interface_include_dir}")

    configured_enum_dirs = source.get("enum_search_dirs")
    if configured_enum_dirs:
        enum_dirs = tuple(cadlib_root / entry for entry in configured_enum_dirs)
    else:
        enum_dirs = (interface_include_dir, interface_include_dir.parent)
    missing_enum_dirs = [str(path) for path in enum_dirs if not path.is_dir()]
    if missing_enum_dirs:
        raise ConfigError(
            "[source].enum_search_dirs entries do not exist: "
            + ", ".join(missing_enum_dirs)
        )

    return Config(
        raw=raw,
        config_path=config_path,
        personal_path=personal_path,
        cadlib_root=cadlib_root,
        stub_repo=stub_repo,
        python_controller=python_controller,
        interface_include_dir=interface_include_dir,
        enum_search_dirs=enum_dirs,
        src_dir=stub_repo / target.get("src_dir", "src"),
        docs_dir=stub_repo / target.get("docs_dir", "docs/documentation"),
        mkdocs=stub_repo / target.get("mkdocs", "mkdocs.yml"),
        pyproject=stub_repo / target.get("pyproject", "pyproject.toml"),
        compare_branch=str(target.get("compare_branch", "main")),
    )
