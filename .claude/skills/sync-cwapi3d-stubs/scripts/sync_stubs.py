#!/usr/bin/env python3
"""Sync the cwapi3d Python stubs with the CwAPI3D pybind11 bindings.

Extracts every controller module, bound function and cadwork type from
CCwAPI3DPythonController.cpp, diffs it against the .pyi stubs in this repo, and
writes the missing declarations -- docstrings derived from the Doxygen contracts
on the ICwAPI3D* interface headers.

Usage:
    python sync_stubs.py --dry-run            human-readable gap report, no writes
    python sync_stubs.py --dry-run --json     machine-readable gap report
    python sync_stubs.py --apply              write the missing declarations
    python sync_stubs.py --apply --only bim_controller [--only cadwork]

Exit codes:
    0  in sync (--dry-run), or the requested writes were applied (--apply)
    1  gaps found (--dry-run only)
    2  configuration, path, or parse error
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import _config
import _cpp_bindings
import _doxygen
import _emit
import _files
import _stubs

EXIT_OK = 0
EXIT_GAPS = 1
EXIT_ERROR = 2


@dataclass
class Gap:
    kind: str  # "function" | "module" | "type"
    module: str
    name: str
    detail: str = ""


@dataclass
class Report:
    missing: list[Gap] = field(default_factory=list)
    blacklisted: list[Gap] = field(default_factory=list)
    orphans: list[Gap] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    written: list[str] = field(default_factory=list)
    version_bump: tuple[str, str] | None = None

    def as_dict(self) -> dict:
        def rows(items: list[Gap]) -> list[dict]:
            return [
                {
                    "kind": gap.kind,
                    "module": gap.module,
                    "name": gap.name,
                    "detail": gap.detail,
                }
                for gap in items
            ]

        return {
            "missing": rows(self.missing),
            "blacklisted": rows(self.blacklisted),
            "orphans": rows(self.orphans),
            "warnings": self.warnings,
            "written": self.written,
            "version_bump": list(self.version_bump) if self.version_bump else None,
        }


def _is_blacklisted(config: _config.Config, module: str, name: str) -> bool:
    return (
        module in config.blacklist_modules
        or name in config.blacklist_methods
        or f"{module}.{name}" in config.blacklist_qualified
    )


def build_report(
    config: _config.Config,
    inventory: _cpp_bindings.Inventory,
    stubs: _stubs.StubInventory,
    only: set[str],
) -> Report:
    report = Report()

    # A --only that names a blacklisted module would otherwise report "in sync",
    # which reads as "nothing to do" rather than "deliberately skipped".
    for module in sorted(only & config.blacklist_modules):
        report.warnings.append(
            f"{module} is blacklisted in [blacklist].modules -- nothing will be "
            "generated for it. Remove the entry to start syncing it."
        )

    for binding in inventory.bindings:
        if binding.module == "cadwork":
            continue
        if only and binding.module not in only:
            continue
        gap = Gap(kind="function", module=binding.module, name=binding.python_name)
        stub = stubs.controllers.get(binding.module)
        already_present = stub is not None and binding.python_name in stub.functions
        if already_present:
            continue
        # Only absent entries are worth reporting as skipped -- a blacklisted name the
        # stubs already carry is not a decision this run made.
        if _is_blacklisted(config, binding.module, binding.python_name):
            report.blacklisted.append(gap)
            continue
        if stub is None:
            gap.detail = "module missing"
        report.missing.append(gap)

    bound_by_module: dict[str, set[str]] = {}
    for binding in inventory.bindings:
        bound_by_module.setdefault(binding.module, set()).add(binding.python_name)
    for module, stub in stubs.controllers.items():
        if (only and module not in only) or module in config.blacklist_modules:
            continue
        for name in sorted(stub.functions - bound_by_module.get(module, set())):
            report.orphans.append(
                Gap(kind="function", module=module, name=name, detail="no C++ binding")
            )

    if not only or "cadwork" in only:
        known = set(stubs.types) | stubs.exported_types
        for entry in inventory.types:
            names = {entry.python_name, *entry.aliases}
            if entry.python_name in config.blacklist_types:
                report.blacklisted.append(
                    Gap(kind="type", module="cadwork", name=entry.python_name)
                )
                continue
            if names & known:
                continue
            report.missing.append(
                Gap(kind="type", module="cadwork", name=entry.python_name, detail=entry.kind)
            )

    for module in bound_by_module:
        if module == "cadwork" or (only and module not in only):
            continue
        if module in stubs.controllers:
            continue
        gap = Gap(kind="module", module=module, name=module, detail="package missing")
        if module in config.blacklist_modules:
            report.blacklisted.append(gap)
        else:
            report.missing.append(gap)

    return report


def apply_changes(
    config: _config.Config,
    inventory: _cpp_bindings.Inventory,
    stubs: _stubs.StubInventory,
    doxygen: _doxygen.DoxygenIndex,
    enum_definitions: dict[str, list[_cpp_bindings.EnumMember]],
    report: Report,
) -> None:
    _files.set_default_newline(config.pyproject)
    resolver = _emit.TypeResolver.build(
        config.type_map,
        inventory.types,
        hint_map=config.hint_map,
        stub_types=set(stubs.types),
    )
    touched_src = False

    new_modules = {gap.name for gap in report.missing if gap.kind == "module"}
    for module in sorted(new_modules):
        init = _emit.create_controller_package(config.src_dir, module)
        stubs.controllers[module] = _stubs.ControllerStub(module=module, path=init)
        report.written.append(str(init.relative_to(config.stub_repo)))
        if _emit.patch_pyproject_packages(config.pyproject, module):
            report.written.append(str(config.pyproject.relative_to(config.stub_repo)))
        page = _emit.write_docs_page(
            config.docs_dir, module, _emit._title_case(module), module
        )
        report.written.append(str(page.relative_to(config.stub_repo)))
        if _emit.patch_mkdocs_nav(
            config.mkdocs, module, _emit._title_case(module), "Reference"
        ):
            report.written.append(str(config.mkdocs.relative_to(config.stub_repo)))
        touched_src = True

    by_module: dict[str, list[str]] = {}
    imports_by_module: dict[str, set[str]] = {}
    typing_by_module: dict[str, set[str]] = {}
    wanted = {
        (gap.module, gap.name) for gap in report.missing if gap.kind == "function"
    }
    for binding in inventory.bindings:
        if (binding.module, binding.python_name) not in wanted:
            continue
        trampoline = inventory.trampolines.get(binding.symbol or "")
        if trampoline is None:
            report.warnings.append(
                f"{binding.module}.{binding.python_name}: no signature found -- skipped"
            )
            continue
        doc = doxygen.lookup(trampoline.accessor, trampoline.cpp_method)
        rendered = _emit.render_function(
            binding, trampoline, doc, resolver, config.param_names
        )
        by_module.setdefault(binding.module, []).append(rendered.text)
        imports_by_module.setdefault(binding.module, set()).update(rendered.imports)
        typing_by_module.setdefault(binding.module, set()).update(rendered.typing_names)
        if rendered.thin_doc:
            report.warnings.append(
                f"{binding.module}.{binding.python_name}: no Doxygen @brief -- "
                "docstring is a placeholder"
            )
        if rendered.had_cpp_example:
            report.warnings.append(
                f"{binding.module}.{binding.python_name}: the interface carries a C++ "
                "@par Example that was NOT translated -- port it by hand"
            )

    for module, blocks in sorted(by_module.items()):
        stub = stubs.controllers[module]
        lines = _emit.import_lines(
            imports_by_module.get(module, set()),
            stub.star_imports_api_types,
            stub.imported_names,
        )
        wanted_typing = sorted(typing_by_module.get(module, set()) - stub.imported_names)
        if wanted_typing:
            lines.insert(0, f"from typing import {', '.join(wanted_typing)}")
        _stubs.insert_imports(stub.path, lines)
        separator = "\n" * (stub.blank_lines_between_defs + 1)
        _stubs.append_block(
            stub.path, separator.join(blocks), stub.blank_lines_between_defs
        )
        report.written.append(str(stub.path.relative_to(config.stub_repo)))
        touched_src = True

    wanted_types = {gap.name for gap in report.missing if gap.kind == "type"}
    for entry in inventory.types:
        if entry.python_name not in wanted_types:
            continue
        if entry.kind == "enum":
            rendered = _emit.render_enum(entry, enum_definitions)
        else:
            rendered = _emit.render_class(entry, resolver)
        report.warnings.extend(rendered.warnings)
        if not rendered.ok:
            continue
        target = config.src_dir / "cadwork" / f"{entry.python_name}.pyi"
        _files.write_text(target, rendered.text)
        report.written.append(str(target.relative_to(config.stub_repo)))
        if _emit.patch_cadwork_init(stubs.cadwork_init, entry.python_name, entry.kind):
            report.written.append(str(stubs.cadwork_init.relative_to(config.stub_repo)))
        if entry.kind == "enum":
            page = _emit.append_to_enums_page(
                config.docs_dir, config.enums_page, entry.python_name
            )
            report.written.append(str(page.relative_to(config.stub_repo)))
        else:
            page = _emit.write_docs_page(
                config.docs_dir,
                entry.python_name,
                entry.python_name,
                f"cadwork.{entry.python_name}",
            )
            report.written.append(str(page.relative_to(config.stub_repo)))
            if _emit.patch_mkdocs_nav(
                config.mkdocs, entry.python_name, entry.python_name, "Cadwork"
            ):
                report.written.append(str(config.mkdocs.relative_to(config.stub_repo)))
        touched_src = True

    if resolver.unresolved:
        report.warnings.append(
            "C++ types with no Python mapping (annotated Any): "
            + ", ".join(sorted(resolver.unresolved))
        )

    if touched_src and config.bump_version:
        bump = _emit.bump_patch_version(config.pyproject)
        if bump is not None:
            report.version_bump = bump
            report.written.append(str(config.pyproject.relative_to(config.stub_repo)))
        else:
            report.warnings.append(
                "could not bump [project].version -- the publish workflow will reject "
                "a duplicate upload"
            )

    report.written = sorted(set(report.written))


def syntax_check(paths: list[Path]) -> list[str]:
    """Re-parse every touched .pyi. Nothing else in this repo catches a broken stub."""
    import ast

    problems: list[str] = []
    for path in paths:
        if path.suffix != ".pyi":
            continue
        try:
            ast.parse(_files.read_text(path))
        except SyntaxError as error:
            problems.append(f"{path}: {error}")
    return problems


def print_report(report: Report, applied: bool) -> None:
    by_module: dict[str, list[Gap]] = {}
    for gap in report.missing:
        by_module.setdefault(gap.module, []).append(gap)

    if not report.missing:
        print("In sync: no missing declarations.")
    else:
        total = len(report.missing)
        print(f"{total} missing declaration(s):\n")
        for module in sorted(by_module):
            gaps = by_module[module]
            print(f"  {module}  ({len(gaps)})")
            for gap in sorted(gaps, key=lambda item: item.name):
                suffix = f"  [{gap.detail}]" if gap.detail else ""
                print(f"      {gap.kind:8} {gap.name}{suffix}")
            print()

    if report.blacklisted:
        skipped_modules = sorted(
            gap.module for gap in report.blacklisted if gap.kind == "module"
        )
        suffix = (
            f" (whole module{'s' if len(skipped_modules) > 1 else ''}: "
            f"{', '.join(skipped_modules)})"
            if skipped_modules
            else ""
        )
        print(f"{len(report.blacklisted)} blacklisted entr(ies) skipped{suffix}.")
    if report.orphans:
        print(f"\n{len(report.orphans)} stub function(s) with no C++ binding (kept):")
        for gap in report.orphans:
            print(f"      {gap.module}.{gap.name}")

    if applied:
        if report.version_bump:
            print(f"\nversion {report.version_bump[0]} -> {report.version_bump[1]}")
        print(f"\n{len(report.written)} file(s) written:")
        for path in report.written:
            print(f"      {path}")

    if report.warnings:
        print(f"\n{len(report.warnings)} warning(s):")
        for warning in report.warnings:
            print(f"      - {warning}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Sync cwapi3d .pyi stubs with the CwAPI3D pybind11 bindings."
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="report gaps without writing (default)",
    )
    mode.add_argument("--apply", action="store_true", help="write missing declarations")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        metavar="MODULE",
        help="restrict to one module (repeatable); 'cadwork' covers the types",
    )
    args = parser.parse_args(argv)

    try:
        config = _config.load()
    except _config.ConfigError as error:
        print(f"config error: {error}", file=sys.stderr)
        return EXIT_ERROR

    try:
        inventory = _cpp_bindings.parse(config.python_controller)
        doxygen = _doxygen.parse(config.interface_include_dir)
        enum_definitions = _cpp_bindings.parse_enum_definitions(
            list(config.enum_search_dirs)
        )
        stubs = _stubs.parse(config.src_dir)
    except (OSError, ValueError, SyntaxError) as error:
        print(f"parse error: {error}", file=sys.stderr)
        return EXIT_ERROR

    only = set(args.only)
    known_modules = set(inventory.modules()) | set(stubs.controllers)
    unknown = sorted(only - known_modules)
    if unknown:
        print(
            "unknown --only module(s): "
            + ", ".join(unknown)
            + "\nknown: "
            + ", ".join(sorted(known_modules)),
            file=sys.stderr,
        )
        return EXIT_ERROR

    report = build_report(config, inventory, stubs, only)

    if args.apply:
        apply_changes(config, inventory, stubs, doxygen, enum_definitions, report)
        problems = syntax_check([config.stub_repo / path for path in report.written])
        if problems:
            report.warnings.extend(f"SYNTAX ERROR {problem}" for problem in problems)

    if args.json:
        print(json.dumps(report.as_dict(), indent=2))
    else:
        print_report(report, applied=args.apply)

    if args.apply:
        return EXIT_ERROR if any(
            warning.startswith("SYNTAX ERROR") for warning in report.warnings
        ) else EXIT_OK
    return EXIT_GAPS if report.missing else EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
