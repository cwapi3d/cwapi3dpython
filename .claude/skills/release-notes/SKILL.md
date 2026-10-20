---
name: release-notes
description: "Write the API release notes for cwapi3d and rotate docs/release_notes.md so it always holds exactly the last 10 releases. A release is a [project].version bump in pyproject.toml on main. A script diffs the .pyi stubs between releases (added, removed, signature-changed, docstring-only) and Claude turns that into Keep a Changelog style notes for plugin authors. Use after bumping the version in a release PR, after /sync-cwapi3d-stubs, or to backfill or refresh the release notes page."
allowed-tools: Read, Grep, Glob, Edit, Write, Bash
---

# Release notes (rolling last 10)

`cwapi3d` has no tags and no GitHub releases. **A release is a `[project].version`
bump in `pyproject.toml` that reaches `main`**: `publish.yml` pushes every such merge to
PyPI. The public API is the set of `src/**/*.pyi` stubs. The release history and the
API diff can therefore both be re-derived from git at any time. Nothing is kept in a
state file.

| Writes | Role |
| ------ | ---- |
| `docs/release_notes.md` | the rolling page: intro and exactly 10 release blocks, newest first |

Everything else is read-only.

## Tools

`scripts/release_diff.py` is stdlib only. Run it from the repo root with any
Python 3.11 or newer:

```bash
python .claude/skills/release-notes/scripts/release_diff.py list                 # newest 11 = window of 10 + baseline
python .claude/skills/release-notes/scripts/release_diff.py list --worktree      # include an uncommitted version bump
python .claude/skills/release-notes/scripts/release_diff.py diff 33.383.0        # human-readable summary
python .claude/skills/release-notes/scripts/release_diff.py diff 33.383.0 --json # the facts to write from
python .claude/skills/release-notes/scripts/release_diff.py diff WORKTREE --json # release PR not merged yet
```

`diff --json` returns:

| Key | Meaning |
| --- | ------- |
| `release`, `baseline` | version, date, commit, subject, PR of this release and of the previous one |
| `api.added` / `api.removed` | new or removed functions, classes, enums, methods and enum members. The members of a new class are listed in its `members` and not repeated. |
| `api.changed` | `old_signature` → `signature`, plus `breaking`: why an existing call could break (removed or renamed param, new required param, return type) |
| `api.breaking` | the `changed` entries with reasons, plus every removal |
| `api.docstring_only` | the doc text changed. Reflowing or re-quoting a docstring is ignored. |
| `new_modules` / `removed_modules` | stub modules that appeared or disappeared |
| `commits`, `prs`, `jira` | first-parent commits in the range, with PR numbers and `API-NNN` keys |
| `changed_files` | changed paths grouped by top directory, so docs-only or CI-only releases are easy to spot |
| `ref` (per entry) | the mkdocstrings identifier to link to, or `null` when no docs page renders it |

## Steps

1. **Find the window.** Run `list --worktree`. If the working tree carries a version
   that is not on `main` yet, the first row is `WORKTREE`, and that is the release being
   prepared. The **first 10 rows are the window**. The 11th row is only the baseline of
   the oldest entry and does not get an entry of its own.
2. **Read the page.** Split `docs/release_notes.md` on the
   `<!-- release:X -->` … `<!-- /release:X -->` markers. Keep every existing block that is
   still in the window **exactly as written**: entries may have been hand-edited after
   generation. Regenerate a block only when the user asks to refresh it.
3. **Write the missing entries.** For each version in the window without a block, run
   `diff <version> --json` (or `diff WORKTREE --json`) and fill `template.md`. Follow the
   writing rules below.
4. **Rotate.** Drop every block whose version is no longer in the window. Write the
   page: the intro (keep the existing one), then the 10 blocks in the window order,
   newest first.
5. **Verify.**
   - Exactly 10 `<!-- release:` markers, each with a matching close marker, and the
     versions in the same order as `list`.
   - Run `uv run mkdocs build 2>&1 | grep -i -E "release_notes|autorefs|could not find"`.
     The output must be empty, meaning no unresolved cross-references. If a reference
     does not resolve, drop the link and keep the code span.
   - Run `uv run --frozen ruff format docs/release_notes.md`. CI's `ruff format --check`
     also formats the Python snippets inside Markdown (single quotes, 120 columns).
   - Running the skill a second time without a new release must change nothing.

## Writing rules (API release-note best practices)

- **Audience: plugin authors.** Say what they can now do, or what they must change.
  Use present tense and no internal process ("synced stubs", "CI", "coverage badge",
  "switched to uv" are not news to them).
- **Sections** follow [Keep a Changelog](https://keepachangelog.com/) in this order:
  `⚠ Breaking changes`, `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`,
  `Documentation`. **Omit every empty section.**
- **Every API item is fully qualified, set in code style and linked** with
  autorefs:
  ``[`file_controller.export_file_with_options`][file_controller.export_file_with_options]``.
  Use the entry's `ref` as the link target. When `ref` is `null`, use a plain code span.
  For a new cadwork type, link the module (`[cadwork.end_type][cadwork.end_type]`), which
  the docs already do elsewhere.
- **Added**: one bullet per function, with its first docstring sentence. Group related
  items, for example "Navigation widget: `set_navigation_widget_axis`, `…_cube`,
  `…_size`, …", when there are more than about 5 of the same family. List the members of
  a new class or enum in the same bullet, not as separate bullets.
- **Stub corrections vs real breaks.** The stubs only describe the C++ binding. When a
  `changed` entry comes from a PR that *corrects documentation or a wrong signature*
  (a `Bugfix/…` or "Corrected …" subject, docs-only Jira), the runtime never changed:
  the stub was wrong. Put it under **Fixed** and show old → new so readers know their
  type hints or IDE hints shift. Use **⚠ Breaking changes** only when calling code that
  used to work stops working (a binding was removed or renamed, or its arguments changed).
  Every breaking item needs a **Migration** line, plus a before/after snippet when the
  change is not obvious.
- **Documentation**: collapse `docstring_only` entries to one bullet per controller with
  a count, and name a function only when its doc changed meaningfully (wrong parameter,
  new example).
- **No API changes**: when `api_changed` is false, still write the entry. Use one
  sentence (for example "Packaging-only release: no API changes.") and no sections.
- **Only facts from the JSON or the PR subjects.** Do not invent behaviour, parameters
  or motivation. When a summary is missing, describe the item by its name and signature.
- **No internal Jira keys** in the page. The PR link is the public trail.
- **Header line**: `[PR #N](…) · \`pip install cwapi3d==X\``. The WORKTREE release has
  no PR yet, so leave the PR link out and add it when the PR is opened.

## Gotchas

- `list` follows `--first-parent` of `HEAD`. Run the skill on `main`, or on a release
  branch cut from it. Otherwise the history of a feature branch shows up as releases.
- A release's commit is the commit that **introduced** the version. Later commits on
  `main` that touch `pyproject.toml` without a bump belong to the *next* release's range.
- A whole new type shows up once, as a class or enum with `members`. A member added to
  an existing type shows up as `cadwork.<type>.<member>`.
