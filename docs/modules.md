# Packages and Modules

A cadwork plugin is a normal Python script, so `import` works as you'd expect. This page explains
which modules are available inside cadwork, how to use third-party packages and how to split a
larger plugin into several files.

## The cadwork modules

!!! important "Always import `cadwork`"
    The `cadwork` module contains the core types (`point_3d`, `element_type`, enums, ...) that
    many controller functions expect or return. Import it in every plugin:

    ```python
    import cadwork
    ```

The controller modules (`element_controller`, `attribute_controller`, `geometry_controller`, ...)
are **built into cadwork**. They are always available inside cadwork and never need installing.
Outside cadwork they don't exist: the [`cwapi3d`](https://pypi.org/project/cwapi3d/){target=_blank}
package you install for your editor contains only type stubs for autocompletion, see
[Getting Started → Choose an editor](get_started.md#choose-an-editor).

```python
import cadwork
import element_controller as ec
import attribute_controller as ac
import geometry_controller as gc
import utility_controller as uc
```

The [Reference](documentation/element_controller.md) lists every controller and function.

## The standard library

cadwork uses a full CPython interpreter (see
[version facts](get_started.md#prerequisites)), so the whole Python standard library is available:

```python
import csv
import json
import math
import tkinter
from pathlib import Path
```

## Paths relative to your plugin

Don't rely on the current working directory inside cadwork. It is usually not your plugin folder.
Build paths from the location of the script instead:

```python
from pathlib import Path

PLUGIN_DIR = Path(__file__).resolve().parent      # ...\API.x64\MyPlugin
config_file = PLUGIN_DIR / 'settings.json'
```

## Splitting a plugin into several files

For larger plugins, put helper modules next to the main script and add the plugin folder to
`sys.path` once at the top:

```text
API.x64\
└── MyPlugin\
    ├── MyPlugin.py
    └── mylib\
        ├── __init__.py
        └── geometry_helpers.py
```

```python title="MyPlugin.py"
import sys
from pathlib import Path

PLUGIN_DIR = Path(__file__).resolve().parent
if str(PLUGIN_DIR) not in sys.path:
    sys.path.insert(0, str(PLUGIN_DIR))

from mylib import geometry_helpers  # noqa: E402
```

`sys.path` is the list of folders Python searches when you `import` something. Adding a folder to
it makes every module in that folder importable.

## Third-party packages

Packages from PyPI (for example `openpyxl`, `requests` or `numpy`) are **not** part of cadwork's
interpreter. The robust way to use them is to install them **into your plugin folder** and add
that folder to `sys.path`. Your plugin then carries its own dependencies and works on every
machine you copy it to.

1. Install Python 3.14 (64-bit) on your machine, the same version cadwork uses.
2. Install the package into a `lib` folder inside your plugin:

    ```bash
    py -3.14 -m pip install --target "C:\...\API.x64\MyPlugin\lib" openpyxl
    ```

3. Add the folder to `sys.path` before importing:

    ```python title="MyPlugin.py"
    import sys
    from pathlib import Path

    LIB_DIR = Path(__file__).resolve().parent / 'lib'
    if str(LIB_DIR) not in sys.path:
        sys.path.insert(0, str(LIB_DIR))

    import openpyxl  # noqa: E402
    ```

!!! warning "Compiled packages must match cadwork's Python"
    Pure-Python packages work with any Python 3 version. Packages with compiled parts (`numpy`,
    `shapely`, `pandas`, ...) must be built for **the same Python version (3.14) and 64-bit
    Windows** as cadwork. Install them with a matching Python as shown above. Otherwise the
    import fails with an error such as `ImportError: DLL load failed` or
    `No module named '..._multiarray_umath'`.

??? note "Advanced: sharing a library between several plugins"
    If several of your plugins use the same helper code, keep it in one shared folder (for
    example `API.x64\_shared`) and add that folder to `sys.path` from each plugin. Folders
    without a matching `.py` file don't show up on the plugin bar, so a shared folder doesn't
    create an extra button.

    ```python
    import sys
    from pathlib import Path

    SHARED_DIR = Path(__file__).resolve().parent.parent / '_shared'
    sys.path.insert(0, str(SHARED_DIR))
    ```

## Troubleshooting imports

| Error | Cause | Fix |
| ----- | ----- | --- |
| `ModuleNotFoundError: No module named 'element_controller'` | Script started outside cadwork | Run it from cadwork, see [Getting Started](get_started.md#troubleshooting) |
| `ModuleNotFoundError: No module named 'openpyxl'` | Package not installed in the plugin, or `sys.path` not set before the import | Install with `--target`, insert the folder into `sys.path` **before** the `import` |
| `ImportError: DLL load failed` | Compiled package built for another Python version or architecture | Reinstall it with Python 3.14, 64-bit |
| Changes to a helper module have no effect | Python caches imported modules for the whole cadwork session | Restart cadwork, or use `importlib.reload(module)` while developing |
