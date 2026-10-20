import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).parents[1] / '.claude' / 'skills' / 'release-notes' / 'scripts' / 'release_diff.py'
_spec = importlib.util.spec_from_file_location('release_diff', _SCRIPT)
assert _spec is not None and _spec.loader is not None
release_diff = sys.modules['release_diff'] = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(release_diff)

CONTROLLER = 'src/demo_controller/__init__.pyi'
OLD_CONTROLLER = '''
def kept(element_id: int) -> str:
    """Gets the name."""

def reordered(color: int, material_id: int) -> None:
    """Sets it."""

def removed() -> None:
    """Gone soon."""

def optional_added(a: int) -> List[int]:
    """Old doc.
    """
'''
NEW_CONTROLLER = '''
def kept(element_id: int) -> str:
    """Gets the name."""

def reordered(material_id: int, transparency: int) -> None:
    """Sets it."""

def optional_added(a: int, b: int = 0) -> list[int]:
    """New doc."""

def brand_new(x: float) -> None:
    """Brand new function.

    More detail.
    """
'''
OLD_ENUM = """
from enum import IntEnum

class colour(IntEnum):
    red = 1
    def __int__(self) -> int: ...
"""
NEW_ENUM = """
from enum import IntEnum

class colour(IntEnum):
    red = 1
    green = 2
    def __int__(self) -> int: ...
"""
NEW_TYPE = '''
class options:
    """Export options."""

    def __init__(self) -> None: ...
    def get_scale(self) -> float: ...
'''


def _inventory(*files: tuple[str, str]) -> dict:
    symbols = {}
    for path, source in files:
        symbols.update(release_diff.parse_stub(path, source))
    return symbols


@pytest.fixture
def diff():
    old = _inventory((CONTROLLER, OLD_CONTROLLER), ('src/cadwork/colour.pyi', OLD_ENUM))
    new = _inventory(
        (CONTROLLER, NEW_CONTROLLER),
        ('src/cadwork/colour.pyi', NEW_ENUM),
        ('src/cadwork/options.pyi', NEW_TYPE),
    )
    return release_diff.diff_inventories(old, new, {'demo_controller', 'cadwork.options'})


def _names(entries: list[dict]) -> list[str]:
    return [e['name'] for e in entries]


def test_module_of_maps_paths_to_import_names():
    assert release_diff.module_of('src/file_controller/__init__.pyi') == 'file_controller'
    assert release_diff.module_of('src/cadwork/point_3d.pyi') == 'cadwork.point_3d'


def test_added_lists_new_functions_types_and_members(diff):
    assert _names(diff['added']) == ['cadwork.colour.green', 'cadwork.options', 'demo_controller.brand_new']
    new_type = next(e for e in diff['added'] if e['name'] == 'cadwork.options')
    assert new_type['kind'] == 'class'
    assert new_type['members'] == ['get_scale']  # dunders are left out, members not repeated
    assert new_type['ref'] == 'cadwork.options.options'
    assert (
        next(e for e in diff['added'] if e['name'] == 'demo_controller.brand_new')['summary'] == 'Brand new function.'
    )


def test_removed_counts_as_breaking(diff):
    assert _names(diff['removed']) == ['demo_controller.removed']
    assert 'demo_controller.removed' in _names(diff['breaking'])


def test_reordered_parameters_are_breaking(diff):
    changed = {e['name']: e for e in diff['changed']}
    reasons = changed['demo_controller.reordered']['breaking']
    assert any('`color` removed or renamed' in r for r in reasons)
    assert any('new required parameter `transparency`' in r for r in reasons)


def test_new_optional_parameter_is_compatible(diff):
    changed = {e['name']: e for e in diff['changed']}
    entry = changed['demo_controller.optional_added']
    assert entry['breaking'] == []  # List[int] -> list[int] is the same type
    assert entry['old_signature'] == 'optional_added(a: int) -> list[int]'


def test_docstring_reflow_is_not_a_change(diff):
    assert _names(diff['docstring_only']) == []
    old = _inventory((CONTROLLER, 'def f() -> None:\n    """Doc A."""\n'))
    new = _inventory((CONTROLLER, 'def f() -> None:\n    """Doc B."""\n'))
    assert _names(release_diff.diff_inventories(old, new)['docstring_only']) == ['demo_controller.f']


def test_unchanged_symbol_is_not_reported(diff):
    everything = [n for entries in diff.values() for n in _names(entries)]
    assert 'demo_controller.kept' not in everything


def _git(repo: Path, *args: str) -> None:
    subprocess.run(['git', *args], cwd=repo, check=True, capture_output=True)


def _commit(repo: Path, version: str, stub: str, message: str) -> None:
    (repo / 'pyproject.toml').write_text(f'[project]\nname = "demo"\nversion = "{version}"\n', encoding='utf-8')
    (repo / 'src' / 'demo_controller').mkdir(parents=True, exist_ok=True)
    (repo / CONTROLLER).write_text(stub, encoding='utf-8')
    _git(repo, 'add', '-A')
    _git(repo, 'commit', '-q', '-m', message)


def test_releases_are_discovered_from_version_bumps(tmp_path):
    _git(tmp_path, 'init', '-q')
    _git(tmp_path, 'config', 'user.email', 'test@example.com')
    _git(tmp_path, 'config', 'user.name', 'test')
    _commit(tmp_path, '1.0.0', OLD_CONTROLLER, 'first (#1)')
    _commit(tmp_path, '1.1.0', OLD_CONTROLLER, 'bump (#2)')
    _commit(tmp_path, '1.1.0', NEW_CONTROLLER, 'same version, not a release (#3)')
    _commit(tmp_path, '1.2.0', NEW_CONTROLLER, 'bump again (#4)')

    releases = release_diff.discover_releases(tmp_path)
    assert [r.version for r in releases] == ['1.2.0', '1.1.0', '1.0.0']
    assert releases[1].pr == 2  # the commit that introduced the version
    assert [r.version for r in release_diff.discover_releases(tmp_path, limit=2)] == ['1.2.0', '1.1.0']

    result = release_diff.diff_release(tmp_path, '1.2.0', releases)
    assert result['prs'] == [3, 4]
    assert 'demo_controller.brand_new' in _names(result['api']['added'])

    (tmp_path / 'pyproject.toml').write_text('[project]\nversion = "1.3.0"\n', encoding='utf-8')
    with_worktree = release_diff.discover_releases(tmp_path, worktree=True)
    assert with_worktree[0].version == '1.3.0'
    assert with_worktree[0].commit == release_diff.WORKTREE
