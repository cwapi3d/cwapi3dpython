#!/usr/bin/env python3
"""Collect the facts for the rolling API release notes.

A release of ``cwapi3d`` is a ``[project].version`` bump in ``pyproject.toml``
on ``main`` -- every such merge is published to PyPI and there are no tags. So
the release history is re-derived from git each run, and the public API is the
set of ``src/**/*.pyi`` stubs, compared with ``ast`` between two releases.

Two subcommands, both stdlib-only and read-only:

    release_diff.py list [--count N] [--worktree]
    release_diff.py diff <version|WORKTREE> [--json]

``WORKTREE`` stands for the uncommitted version bump of a release PR that is
not on ``main`` yet; ``--worktree`` makes ``list`` include it.
"""

from __future__ import annotations

import argparse
import ast
import atexit
import datetime as dt
import json
import re
import subprocess
import sys
import tomllib
from dataclasses import asdict, dataclass, field
from pathlib import Path

WORKTREE = 'WORKTREE'
REPO_URL = 'https://github.com/cwapi3d/cwapi3dpython'

_PR_RE = re.compile(r'\(#(\d+)\)|pull request #(\d+)', re.IGNORECASE)
_JIRA_RE = re.compile(r'\bAPI[-_ ](\d+)\b', re.IGNORECASE)
_VERSION_RE = re.compile(r'^version\s*=\s*"([^"]+)"', re.MULTILINE)
_TYPING_ALIASES = {'List': 'list', 'Dict': 'dict', 'Tuple': 'tuple', 'Set': 'set', 'Type': 'type'}
_ENUM_BASES = {'Enum', 'IntEnum', 'IntFlag', 'Flag', 'StrEnum'}


# ---------------------------------------------------------------- git access


def _git(*args: str, root: Path | None = None) -> str:
    result = subprocess.run(['git', *args], cwd=root, capture_output=True, text=True, encoding='utf-8', check=True)
    return result.stdout


def repo_root() -> Path:
    return Path(_git('rev-parse', '--show-toplevel').strip())


class _BlobReader:
    """One long-lived ``git cat-file --batch``: a release diff reads a few hundred blobs."""

    def __init__(self) -> None:
        self._processes: dict[Path, subprocess.Popen[bytes]] = {}
        atexit.register(self.close)

    def close(self) -> None:
        for process in self._processes.values():
            process.stdin.close()
            process.wait()
            process.stdout.close()
        self._processes.clear()

    def read(self, root: Path, spec: str) -> str | None:
        process = self._processes.get(root)
        if process is None:
            process = self._processes[root] = subprocess.Popen(
                ['git', 'cat-file', '--batch'], cwd=root, stdin=subprocess.PIPE, stdout=subprocess.PIPE
            )
        stdin, stdout = process.stdin, process.stdout
        stdin.write(spec.encode('utf-8') + b'\n')
        stdin.flush()
        header = stdout.readline().split()
        if len(header) < 3 or header[1] == b'missing':
            return None
        content = stdout.read(int(header[2]))
        stdout.read(1)  # the newline cat-file puts after every object
        return content.decode('utf-8')


_blobs = _BlobReader()


def read_file(root: Path, rev: str, path: str) -> str | None:
    """File content at ``rev``; ``rev == WORKTREE`` reads the working tree."""
    if rev == WORKTREE:
        file = root / path
        return file.read_text(encoding='utf-8') if file.is_file() else None
    return _blobs.read(root, f'{rev}:{path}')


def parse_version(pyproject: str | None) -> str | None:
    if pyproject is None:
        return None
    try:
        return tomllib.loads(pyproject)['project']['version']
    except tomllib.TOMLDecodeError, KeyError:
        match = _VERSION_RE.search(pyproject)
        return match.group(1) if match else None


# ---------------------------------------------------------------- releases


@dataclass
class Release:
    version: str
    date: str
    commit: str
    subject: str
    pr: int | None


def _pr_number(subject: str) -> int | None:
    match = _PR_RE.search(subject)
    return int(match.group(1) or match.group(2)) if match else None


def discover_releases(root: Path, ref: str = 'HEAD', worktree: bool = False, limit: int | None = None) -> list[Release]:
    """Distinct versions on the first-parent history of ``ref``, newest first.

    A release's commit is the one that *introduced* its version: later commits
    that touch pyproject.toml without bumping it belong to the next release.
    ``limit`` stops the walk once that many committed releases are settled.
    """
    log = _git(
        'log', '--first-parent', '--format=%H%x09%ad%x09%s', '--date=short', ref, '--', 'pyproject.toml', root=root
    )
    releases: list[Release] = []
    for line in log.splitlines():
        sha, date, subject = line.split('\t', 2)
        version = parse_version(read_file(root, sha, 'pyproject.toml'))
        if version is None:
            continue
        if releases and releases[-1].version == version:
            # Same version further back: the bump happened earlier, move the release there.
            releases[-1] = Release(version, date, sha, subject, _pr_number(subject))
        else:
            if limit is not None and len(releases) == limit:
                break  # the oldest kept release is settled now that an older version showed up
            releases.append(Release(version, date, sha, subject, _pr_number(subject)))

    if worktree:
        version = parse_version(read_file(root, WORKTREE, 'pyproject.toml'))
        if version and (not releases or version != releases[0].version):
            releases.insert(
                0,
                Release(
                    version, dt.datetime.now().astimezone().date().isoformat(), WORKTREE, '(uncommitted release)', None
                ),
            )
    return releases


# ---------------------------------------------------------------- stub inventory


@dataclass
class Symbol:
    name: str  # what a reader types: ``file_controller.export_file``, ``cadwork.point_3d.__add__``
    ref: str  # mkdocstrings identifier: ``cadwork.point_3d.point_3d.__add__``
    kind: str  # function | class | enum | method | attribute | enum_member
    signature: str
    params: list[dict] = field(default_factory=list)
    returns: str | None = None
    doc: str | None = None
    owner: str | None = None  # name of the enclosing class, for members


def _norm_annotation(node: ast.expr | None) -> str | None:
    if node is None:
        return None
    text = ast.unparse(node).replace('typing.', '')
    for alias, builtin in _TYPING_ALIASES.items():
        text = re.sub(rf'\b{alias}\[', f'{builtin}[', text)
    return text.strip('\'"')


def _params(args: ast.arguments) -> list[dict]:
    positional = args.posonlyargs + args.args
    defaults = [None] * (len(positional) - len(args.defaults)) + list(args.defaults)
    params = [
        {
            'name': a.arg,
            'annotation': _norm_annotation(a.annotation),
            'default': ast.unparse(d) if d else None,
            'kwonly': False,
        }
        for a, d in zip(positional, defaults)
    ]
    params += [
        {
            'name': a.arg,
            'annotation': _norm_annotation(a.annotation),
            'default': ast.unparse(d) if d else None,
            'kwonly': True,
        }
        for a, d in zip(args.kwonlyargs, args.kw_defaults)
    ]
    for star, prefix in ((args.vararg, '*'), (args.kwarg, '**')):
        if star is not None:
            params.append(
                {
                    'name': prefix + star.arg,
                    'annotation': _norm_annotation(star.annotation),
                    'default': None,
                    'kwonly': False,
                }
            )
    return [p for p in params if p['name'] not in ('self', 'cls')]


def _signature(name: str, params: list[dict], returns: str | None) -> str:
    rendered = []
    for p in params:
        text = p['name'] + (f': {p["annotation"]}' if p['annotation'] else '')
        if p['default'] is not None:
            text += f' = {p["default"]}'
        rendered.append(text)
    return f'{name}({", ".join(rendered)})' + (f' -> {returns}' if returns else '')


def _function(
    node: ast.FunctionDef | ast.AsyncFunctionDef, name: str, ref: str, kind: str, owner: str | None
) -> Symbol:
    params = _params(node.args)
    returns = _norm_annotation(node.returns)
    return Symbol(
        name, ref, kind, _signature(node.name, params, returns), params, returns, ast.get_docstring(node), owner
    )


def _is_enum(node: ast.ClassDef) -> bool:
    return any(ast.unparse(base).split('.')[-1] in _ENUM_BASES for base in node.bases)


def _add(symbols: dict[str, Symbol], symbol: Symbol) -> None:
    previous = symbols.get(symbol.name)
    if previous is not None and previous.kind in ('function', 'method') and symbol.kind == previous.kind:
        # @overload: keep every variant in one comparable signature.
        previous.signature += ' | ' + symbol.signature
        previous.params = previous.params + symbol.params
        return
    symbols[symbol.name] = symbol


def module_of(path: str) -> str:
    """``src/file_controller/__init__.pyi`` -> ``file_controller``; ``src/cadwork/point_3d.pyi`` -> ``cadwork.point_3d``."""
    parts = Path(path).with_suffix('').parts[1:]
    if parts[-1] == '__init__':
        parts = parts[:-1]
    return '.'.join(parts)


def parse_stub(path: str, source: str) -> dict[str, Symbol]:
    module = module_of(path)
    # A cadwork type lives in its own file but is used as ``cadwork.<type>``.
    public = 'cadwork' if module.startswith('cadwork.') else module
    tree = ast.parse(source)
    symbols: dict[str, Symbol] = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not node.name.startswith('_'):
            _add(symbols, _function(node, f'{public}.{node.name}', f'{module}.{node.name}', 'function', None))
        elif isinstance(node, ast.ClassDef):
            enum = _is_enum(node)
            cls_name, cls_ref = f'{public}.{node.name}', f'{module}.{node.name}'
            _add(
                symbols,
                Symbol(
                    cls_name, cls_ref, 'enum' if enum else 'class', f'class {node.name}', doc=ast.get_docstring(node)
                ),
            )
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if item.name.startswith('_') and not _is_dunder(item.name):
                        continue
                    _add(
                        symbols,
                        _function(item, f'{cls_name}.{item.name}', f'{cls_ref}.{item.name}', 'method', cls_name),
                    )
                elif isinstance(item, (ast.Assign, ast.AnnAssign)):
                    targets = item.targets if isinstance(item, ast.Assign) else [item.target]
                    for target in targets:
                        if isinstance(target, ast.Name) and not target.id.startswith('_'):
                            kind = 'enum_member' if enum else 'attribute'
                            value = ast.unparse(item.value) if item.value is not None else ''
                            _add(
                                symbols,
                                Symbol(
                                    f'{cls_name}.{target.id}',
                                    f'{cls_ref}.{target.id}',
                                    kind,
                                    f'{target.id} = {value}'.strip(' ='),
                                    owner=cls_name,
                                ),
                            )
    return symbols


def stub_paths(root: Path, rev: str) -> list[str]:
    if rev == WORKTREE:
        return sorted(p.relative_to(root).as_posix() for p in (root / 'src').rglob('*.pyi'))
    listing = _git('ls-tree', '-r', '--name-only', rev, '--', 'src', root=root)
    return sorted(p for p in listing.splitlines() if p.endswith('.pyi'))


def inventory(root: Path, rev: str) -> tuple[dict[str, Symbol], set[str]]:
    symbols: dict[str, Symbol] = {}
    modules: set[str] = set()
    for path in stub_paths(root, rev):
        source = read_file(root, rev, path)
        if source is None:
            continue
        modules.add(module_of(path))
        try:
            parsed = parse_stub(path, source)
        except SyntaxError as error:
            print(f'warning: cannot parse {path}@{rev[:10]}: {error}', file=sys.stderr)
            continue
        for symbol in parsed.values():
            symbols.setdefault(symbol.name, symbol)
    return symbols, modules


# ---------------------------------------------------------------- diff


def breaking_reasons(old: Symbol, new: Symbol) -> list[str]:
    """Why upgrading could break an existing call site. Empty means compatible."""
    if old.kind == 'enum_member':
        return ['value changed'] if old.signature != new.signature else []
    if old.kind in ('attribute', 'class', 'enum'):
        return []
    reasons: list[str] = []
    old_names = [p['name'] for p in old.params]
    new_by_name = {p['name']: p for p in new.params}
    for index, name in enumerate(old_names):
        if name not in new_by_name:
            reasons.append(f'parameter `{name}` removed or renamed')
            continue
        new_positional = [p['name'] for p in new.params if not p['kwonly']]
        if name in new_positional and index < len(new_positional) and new_positional[index] != name:
            reasons.append(f'parameter `{name}` moved position')
        old_param = old.params[index]
        if old_param['default'] is not None and new_by_name[name]['default'] is None:
            reasons.append(f'parameter `{name}` is no longer optional')
    for param in new.params:
        if param['name'] not in old_names and param['default'] is None and not param['name'].startswith('*'):
            reasons.append(f'new required parameter `{param["name"]}`')
    if old.returns != new.returns:
        reasons.append(f'return type `{old.returns}` -> `{new.returns}`')
    return reasons


def _entry(symbol: Symbol, documented: set[str]) -> dict:
    module = symbol.ref.split('.')
    linkable = any('.'.join(module[:i]) in documented for i in range(1, len(module)))
    return {
        'name': symbol.name,
        'kind': symbol.kind,
        'signature': symbol.signature,
        'ref': symbol.ref if linkable else None,
        'summary': (symbol.doc or '').strip().split('\n\n')[0].replace('\n', ' ') or None,
    }


def _words(doc: str | None) -> list[str]:
    # Reflowing or re-quoting a docstring is not a documentation change.
    return (doc or '').split()


def _is_dunder(name: str) -> bool:
    return name.startswith('__') and name.endswith('__')


def diff_inventories(old: dict[str, Symbol], new: dict[str, Symbol], documented: set[str] = frozenset()) -> dict:
    added_names = sorted(new.keys() - old.keys())
    removed_names = sorted(old.keys() - new.keys())
    # A member of a class that is itself new/removed is reported through its class only.
    added = [_entry(new[n], documented) for n in added_names if new[n].owner not in added_names]
    removed = [_entry(old[n], documented) for n in removed_names if old[n].owner not in removed_names]
    for entry in added:
        if entry['kind'] in ('class', 'enum'):
            entry['members'] = sorted(
                m for n in added_names if new[n].owner == entry['name'] and not _is_dunder(m := n.rsplit('.', 1)[1])
            )
    for entry in removed:
        if entry['kind'] in ('class', 'enum'):
            entry['members'] = sorted(
                m for n in removed_names if old[n].owner == entry['name'] and not _is_dunder(m := n.rsplit('.', 1)[1])
            )

    changed, docs_only = [], []
    for name in sorted(old.keys() & new.keys()):
        before, after = old[name], new[name]
        if before.signature != after.signature:
            entry = _entry(after, documented)
            entry.update(old_signature=before.signature, breaking=breaking_reasons(before, after))
            changed.append(entry)
        elif _words(before.doc) != _words(after.doc):
            docs_only.append({'name': name, 'kind': after.kind, 'ref': _entry(after, documented)['ref']})

    return {
        'breaking': [c for c in changed if c['breaking']] + [dict(r, breaking=['removed']) for r in removed],
        'added': added,
        'removed': removed,
        'changed': changed,
        'docstring_only': docs_only,
    }


def documented_modules(root: Path) -> set[str]:
    modules = set()
    for page in (root / 'docs').rglob('*.md'):
        modules.update(re.findall(r'^:::\s+(\S+)', page.read_text(encoding='utf-8'), re.MULTILINE))
    return modules


def commits_between(root: Path, old: str, new: str) -> list[dict]:
    end = 'HEAD' if new == WORKTREE else new
    log = _git('log', '--first-parent', '--format=%H%x09%s', f'{old}..{end}', root=root)
    commits = []
    for line in log.splitlines():
        sha, subject = line.split('\t', 1)
        commits.append(
            {
                'sha': sha[:10],
                'subject': subject,
                'pr': _pr_number(subject),
                'jira': sorted({f'API-{n}' for n in _JIRA_RE.findall(subject)}),
            }
        )
    return commits


def changed_files(root: Path, old: str, new: str) -> dict[str, list[str]]:
    args = ['diff', '--name-only', old] + ([] if new == WORKTREE else [new])
    groups: dict[str, list[str]] = {}
    for path in _git(*args, root=root).splitlines():
        top = path.split('/', 1)[0] if '/' in path else '(root)'
        groups.setdefault(top, []).append(path)
    return groups


def diff_release(root: Path, version: str, releases: list[Release]) -> dict:
    index = next((i for i, r in enumerate(releases) if version in (r.version, r.commit)), None)
    if index is None:
        raise SystemExit(f'error: unknown release {version!r}; run `list` to see the known versions')
    if index + 1 >= len(releases):
        raise SystemExit(f'error: {version} is the oldest release, there is nothing to diff it against')
    release, baseline = releases[index], releases[index + 1]
    old_symbols, old_modules = inventory(root, baseline.commit)
    new_symbols, new_modules = inventory(root, release.commit)
    commits = commits_between(root, baseline.commit, release.commit)
    api = diff_inventories(old_symbols, new_symbols, documented_modules(root))
    return {
        'release': asdict(release),
        'baseline': asdict(baseline),
        'pr_url': f'{REPO_URL}/pull/{release.pr}' if release.pr else None,
        'new_modules': sorted(new_modules - old_modules),
        'removed_modules': sorted(old_modules - new_modules),
        'api': api,
        'api_changed': any(api.values()),
        'commits': commits,
        'prs': sorted({c['pr'] for c in commits if c['pr']}),
        'jira': sorted({k for c in commits for k in c['jira']}),
        'changed_files': changed_files(root, baseline.commit, release.commit),
    }


# ---------------------------------------------------------------- CLI


def _print_diff(result: dict) -> None:
    rel, base = result['release'], result['baseline']
    print(f'{rel["version"]} ({rel["date"]}, {rel["commit"][:10]}) vs {base["version"]}')
    for key in ('new_modules', 'removed_modules', 'prs', 'jira'):
        if result[key]:
            print(f'  {key}: {", ".join(map(str, result[key]))}')
    for section, entries in result['api'].items():
        if not entries:
            continue
        print(f'  {section} ({len(entries)}):')
        for entry in entries:
            extra = f'  [{"; ".join(entry["breaking"])}]' if entry.get('breaking') and section != 'breaking' else ''
            print(f'    {entry["name"]}{extra}')
    if not result['api_changed']:
        print('  no API changes')


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    p_list = sub.add_parser('list', help='releases newest first')
    p_list.add_argument(
        '--count',
        type=int,
        default=11,
        help='how many releases to print (default 11: the window of 10 plus its baseline)',
    )
    p_list.add_argument('--worktree', action='store_true', help='include an uncommitted version bump')
    p_list.add_argument('--json', action='store_true')
    p_diff = sub.add_parser('diff', help='API diff of one release against the previous one')
    p_diff.add_argument('version', help=f'a version from `list`, or {WORKTREE}')
    p_diff.add_argument('--json', action='store_true')
    for p in (p_list, p_diff):
        p.add_argument('--ref', default='HEAD', help='history to read releases from (default HEAD)')
    args = parser.parse_args(argv)

    root = repo_root()
    if args.command == 'list':
        releases = discover_releases(root, args.ref, args.worktree, limit=args.count)[: args.count]
        if args.json:
            print(json.dumps([asdict(r) for r in releases], indent=2))
        else:
            for r in releases:
                print(f'{r.version:<12} {r.date}  {r.commit[:10]:<10}  {r.subject}')
        return 0

    releases = discover_releases(root, args.ref, worktree=True)
    version = args.version
    if version == WORKTREE:
        if releases[0].commit != WORKTREE:
            raise SystemExit('error: the working tree carries no new version; bump [project].version first')
        version = releases[0].version
    result = diff_release(root, version, releases)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        _print_diff(result)
    return 0


if __name__ == '__main__':
    sys.exit(main())
