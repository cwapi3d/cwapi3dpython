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
| `pyproject.toml` | `packages` entry for a new module, and `[project].version` |

## The roundtrip — how one function reaches Python

Four layers, three of them C++. `attribute_controller.get_name` end to end:

**1. The contract** — `CwAPI3D/include/ICwAPI3DAttributeController.h`. The interface
headers are the documentation surface plugin authors read, and the only place a
parameter still has a real name, a prose description, and the *specific* type it
carries. Everything below flattens all three away.

```cpp
/// @brief Gets the element name.
/// @param[in] aElementId [@ref elementID] The element id.
/// @return [@ref ICwAPI3DString*] The element name.
/// @par Example :
/// @code{.cpp}
/// ICwAPI3DElementIDList* activeElements = aFactory->getElementController()->getActiveIdentifiableElementIDs();
/// elementID element = activeElements->at(0);
///
/// ICwAPI3DString* name = aFactory->getAttributeController()->getName(element);
/// @endcode
virtual ICwAPI3DString* getName(elementID aElementId) = 0;
```

(`getName` carries no `@par Example` today — the block above is what one looks like
when it does, e.g. on `setMachineCalculationSet` in the same header.) It is parsed
and kept, but **never emitted**: the example is C++ against `aFactory`, and the
mechanical translation to `attribute_controller.get_name(element_id)` is wrong often
enough that a missing example beats a misleading one. That is the *carries a C++
`@par Example` that was NOT translated* warning in step 6 — the `Examples:` block in
layer 4 below is a **hand** port, done after the run, not something the tool wrote.

**2. The trampoline** — `CwAPI3D/CCwAPI3DPythonController.cpp`. Plain C++ in, plain
C++ out: `elementID` is an anonymous `uint64_t a0`, the `ICwAPI3DString*` is a
`std::string`. The `getAttributeController()->getName(...)` in the body is the join
key back to layer 1 — accessor plus method name, nothing else connects them.

```cpp
std::string cwp_attribute_controller_get_name(uint64_t a0)
{
  return get_string_from_istring(CwAPI3DPythonController().getFactory()->getAttributeController()->getName(a0));
}
```

**3. The binding** — same file, further down. The module name and the Python name
are literals here and nowhere else; `get_name` is not derivable from `getName`
without this line (`set_framed_floor` binds `cwp_attribute_controller_set_floor`).

```cpp
PYBIND11_EMBEDDED_MODULE(attribute_controller, m)
{
  ...
  m.def("get_name", &cwp_attribute_controller_get_name);
  ...
}
```

**4. The stub** — `src/attribute_controller/__init__.pyi`, the only layer this skill
writes. Nothing at runtime enforces that it matches; that is the whole problem.

```python
def get_name(element_id: ElementId) -> str:
    """Gets the element name.

    Parameters:
        element_id: The element id.

    Examples:
        >>> import attribute_controller as ac
        >>> import element_controller as ec
        >>> [element] = ec.get_active_identifiable_element_ids()
        >>> name = ac.get_name(element)

    Returns:
        The element name.
    """
```

Everything there except the `Examples:` block is generated. The block follows the
convention already in the repo — `>>>` lines, module aliases, sitting between
`Parameters:` and `Returns:`; see `set_machine_calculation_set` in the same file for
a real one, ported from the C++ example quoted above. Adding one by hand is fine and
expected; it is documentation the C++ side has and the generator cannot carry over,
not a generator gap being papered over (see the constraints).

Which layer each piece of that declaration came from:

| Piece | Source |
| ----- | ------ |
| `src/attribute_controller/` | the module name in `PYBIND11_EMBEDDED_MODULE` (3) |
| `def get_name` | the `"get_name"` literal in `m.def` (3) |
| the arity | the `cwp_*` signature (2) — never the header, which has overloads pybind11 dropped |
| `: ElementId` | `uint64_t` (2) through `[type_map]`, then upgraded by the trampoline's `static_cast` or the `[@ref elementID]` hint (1) through `[doxygen_hint_map]`. Both agree here; for `[@ref multiLayerSetID]` only the hint knows it is not a plain int |
| `-> str` | `std::string` (2) through `[type_map]` |
| `element_id` | `aElementId` (1), snake_cased — a `py::arg` on the `m.def` would win, and `[param_names]` is the last resort |
| every line of prose | `@brief`, `@param`, `@return` (1) |

So a binding whose interface method carries no Doxygen still emits — layers 2 and 3
carry the signature — but with a placeholder docstring, positional-ish parameter
names and coarser annotations. That is the *no Doxygen `@brief`* warning in step 6.

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
- **`binding source not found`** / **`version header not found`** → `cadlib_root`
  points somewhere without `CwAPI3D/CCwAPI3DPythonController.cpp` or
  `CwAPI3D/include/CwAPI3DVersion.h`. Ask which checkout to use.

The first line of the report echoes the `versionMinor` the run read out of that
header. Sanity-check it against the checkout the operator meant to sync against —
it is what the published version will carry (step 5).

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

Re-running is safe: the tool is additive and idempotent, and the version only moves
when something under `src/` actually changed — no `src/**` change means no publish
run, so no new version is needed.

### The version comes from the C++ header

`[project].version` in `pyproject.toml` is never invented and never carried over by
hand. Every run reads the `versionMinor` tag out of `[source].version_header`
(`CwAPI3D/include/CwAPI3DVersion.h`) and derives the new version from it:

| `versionMinor` vs. the version in `pyproject.toml` | New version |
| -------------------------------------------------- | ----------- |
| higher — the stubs have not shipped for this build yet | `<major>.<versionMinor>.0` (`33.322.7` → `33.328.0`) |
| **the same** — another sync against a build already shipped for | patch + 1 (`33.328.0` → `33.328.1`) |

The major is **never** taken from the header. `versionMajor` there is the marketing
year (2026) while the package's major is the cadwork product major (`33`), and PyPI
accepts no version sorting below one already uploaded. Two cases produce a warning
instead of following the header, and both need a human:

- **`versionMinor` is *lower* than the packaged minor** — the run is pointed at an
  older cadlib checkout. The higher minor is kept and the patch bumped; fix
  `[paths].cadlib_root` if that was not intended.
- **no `versionMinor` found** — the header moved or was reshaped. The run falls back
  to a patch bump; the version is a guess until someone confirms it.

## Step 6 — Hand off

Leave the changes **uncommitted** on the working branch. Report:

1. The files written, and the version change with the `versionMinor` it came from
   (`33.322.0` → `33.328.0`, from `versionMinor = 328`).
2. Every warning, in full. The ones that need a human are:
   - the two version warnings from step 5 — a `versionMinor` below the packaged
     minor, or no `versionMinor` at all.
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
- **Never hand-write `[project].version`.** It is derived from the C++
  `versionMinor` (step 5). If it looks wrong, the checkout or the header is wrong.
- Do not reformat, re-sort, or re-serialise `mkdocs.yml`, `pyproject.toml`, or
  `src/cadwork/__init__.pyi`. The script splices single lines and preserves each
  file's CRLF endings; a whole-file rewrite buries the real change.
- Do not touch anything under `cadlib_root`. The C++ side is the source of truth.
- Do not put paths, or anything else machine-specific, into the versioned
  `config.toml` — that belongs in `config.personal.toml`.
