---
name: sync-cwapi3d-stubs
description: "Sync this repo's .pyi stubs with the CwAPI3D pybind11 bindings in the cadwork 3d C++ source. Extracts every controller module, bound function and cadwork type from CCwAPI3DPythonController.cpp, diffs it against main, and writes the missing declarations with docstrings derived from the Doxygen contracts on the ICwAPI3D* interface headers. Use when the C++ API has gained functions or types that cwapi3d does not expose yet, or to audit how far the stubs have drifted."
allowed-tools: Read, Grep, Glob, Edit, Write, Bash
model: sonnet
---

# Sync CwAPI3D Python stubs

The `cwapi3d` package is a **stub-only** distribution hand-maintained against
`CCwAPI3DPythonController.cpp`. Nothing keeps the two in sync, so a new `m.def(...)`
in C++ silently never reaches the stubs. This skill closes that gap: it re-derives
the full binding inventory from the C++ source and writes what is missing.

**All C++-side access is read-only.** The only files written are inside this repo.

| Writes | Role |
| ------ | ---- |
| `src/<controller>/__init__.pyi` | the missing `def`s, appended |
| `src/<controller>/` (+ `py.typed`) | a whole module the stubs never had |
| `src/cadwork/<type>.pyi` | a registered `py::class_` / `py::enum_` with no stub |
| `src/cadwork/__init__.pyi` | re-export line + `__all__` entry for a new type |
| `docs/documentation/*.md`, `mkdocs.yml` | docs page + nav entry for a new module/type |
| `pyproject.toml` | `packages` entry for a new module, and the version bump |

## Invocation

```
/sync-cwapi3d-stubs [--only <module>] [--report-only] [--on-main]
```

- `--only <module>` — restrict to one module (repeatable). `cadwork` covers the types.
- `--report-only` — stop after step 4; write nothing.
- `--on-main` — write the changes straight onto `main` instead of a working branch
  (see step 3 for why that is not the default).

## Step 1 — Preflight

Resolve the config pair. `config.toml` ships with the skill; `config.personal.toml`
is git-ignored and holds only machine paths.

```powershell
python "<skill-path>/scripts/sync_stubs.py" --dry-run --json
```

Exit `2` means a config or parse error — read the message on stderr and stop:

- **`[paths].cadlib_root is not set`** → the operator has no `config.personal.toml`.
  Tell them to copy `config.personal.toml.example` next to it and set `cadlib_root`
  to their cadwork 3d source root (e.g. `D:\source\cadlib\v_33.0\3d`). Do not guess
  the path and do not write the file for them without asking.
- **`binding source not found`** → `cadlib_root` points somewhere without
  `CwAPI3D/CCwAPI3DPythonController.cpp`. Ask which checkout to use.

Then check the working tree:

```powershell
git -C "<repo>" status --porcelain
```

If it is dirty, **stop and report**. Never stash, reset, or check out over the
operator's uncommitted work.

## Step 2 — Land on `main`

`main` is the comparison baseline, so the run starts there regardless of the branch
the checkout is sitting on. Report the branch being left.

```powershell
git -C "<repo>" fetch origin
git -C "<repo>" checkout main
git -C "<repo>" pull --ff-only
```

A non-fast-forward `pull` means local `main` has diverged — stop and report; do not
merge or rebase it.

## Step 3 — Cut a working branch

```powershell
git -C "<repo>" switch -c sync/cwapi3d-stubs-<yyyy-mm-dd>
```

The publish workflow uploads to **real PyPI on every push to `main`** that touches
`src/**`, so generated stubs do not land on `main` directly. Skip this step only when
the operator passed `--on-main`.

## Step 4 — Report the gap

Run the dry-run from step 1 again if needed and present the result as a table
grouped by controller: how many declarations are missing, which are whole missing
modules, which cadwork types have no stub. Also relay:

- **blacklisted** — skipped by `[blacklist]` in `config.toml` (per-controller
  `get_last_error` / `clear_errors` and similar plumbing). Say how many, not each one.
  Name any **whole module** in `[blacklist].modules` explicitly, though: today
  `event_controller` is skipped entirely, and a reader should not mistake that for
  "already in sync". Enabling one is a config edit, never a hand-written stub.
- **orphans** — stub functions with no C++ binding. These are **reported, never
  deleted**; they usually mean a binding was removed upstream or renamed.

Stop here on `--report-only`.

## Step 5 — Apply

```powershell
python "<skill-path>/scripts/sync_stubs.py" --apply
```

The script re-parses every `.pyi` it touched with `ast` before returning; a syntax
error is reported as a `SYNTAX ERROR` warning and exits `2`. Nothing else in this
repo catches a broken stub — there are no tests, and setuptools does not compile
`.pyi`, so treat that exit as a hard failure and report it verbatim.

Re-running is safe: the tool is additive and idempotent, and the version bumps only
when something under `src/` actually changed.

## Step 6 — Hand off

Leave the changes **uncommitted** on the working branch. Report:

1. The files written and the version bump (`33.322.0` → `33.322.1`).
2. Every warning, in full. The ones that need a human are:
   - *"no Doxygen @brief — docstring is a placeholder"* — the C++ side has no
     documentation to derive from. The stub is syntactically fine but the prose is
     a stand-in.
   - *"carries a C++ @par Example that was NOT translated"* — the interface header
     has a worked example in C++. It is deliberately not machine-translated; a wrong
     example in the published docs is worse than none. Offer to port it by hand.
   - *"C++ types with no Python mapping (annotated Any)"* — add an entry to
     `[type_map]` or `[doxygen_hint_map]` in `config.toml` and re-run.
   - *"no member of C++ enum ... could be resolved"* — the declaring header is
     outside `[source].enum_search_dirs`. The enum is **not** written in that case.
3. For a brand-new module, the `TODO` module docstring left in
   `src/<module>/__init__.pyi` — the bindings carry no module-level documentation,
   so that one paragraph has to be written by a human.

Do not commit, push, or open a PR unless the operator asks.

## Constraints

- **Run this skill on Sonnet.** The work is mechanical — a script run plus a report.
  If the session is on another model, switch to Sonnet (`/model sonnet`) before step 1.
- **Additive only.** Never delete or rewrite an existing stub declaration; drift in
  the other direction is reported, not resolved.
- **Never hand-edit the stubs to "fix" a generator gap.** Fix `config.toml` and
  re-run, so the next sync stays correct.
- Do not reformat, re-sort, or re-serialise `mkdocs.yml`, `pyproject.toml`, or
  `src/cadwork/__init__.pyi`. The script splices single lines and preserves each
  file's CRLF endings; a whole-file rewrite buries the real change.
- Do not touch anything under `cadlib_root`. The C++ side is the source of truth.
- Do not put paths, or anything else machine-specific, into the versioned
  `config.toml` — that belongs in `config.personal.toml`.
