# Run cadwork from the Command Line

Besides starting cadwork by double-clicking a file, you can launch it from **cmd** or
**PowerShell** with `ci_start.exe`. Command-line arguments let you open a file, pick a specific
cadwork version, automatically run a Python script, or print plans — without touching the UI.

Combined with a PowerShell loop, this turns cadwork into a tool you can drive over a **whole folder
of files at once** (batch processing) for exports, printing or any custom Python automation.

!!! note
    Exact paths (drive letter, version folder name) depend on your local installation. Replace the
    paths in the examples below with the ones on your machine.

## Locating `ci_start.exe`

`ci_start.exe` is the cadwork launcher and lives in your `cadwork.dir` folder:

```text
...\cadwork.dir\ci_start.exe
```

Each installed version has its own program folder next to it, named `exe_<year>`:

```text
...\cadwork.dir\exe_2026
...\cadwork.dir\exe_2027
```

## Opening a file and selecting the version (`/EXE=`)

To open a `.3d` file, pass the file path to `ci_start.exe`. Use the `/EXE=` argument to choose
**which installed cadwork version** should open the file:

=== "ci_start.exe"

    ```powershell
    D:\cadwork.dir\ci_start.exe "C:\Users\Me\Downloads\timber-framed-elements.3d" /EXE=D:\cadwork.dir\exe_2026
    ```

=== "Start-Process"

    PowerShell's `Start-Process` returns the prompt immediately and gives you control over the
    window state:

    ```powershell
    Start-Process "C:\Users\Me\Downloads\timber-framed-elements_2027.3d" -ArgumentList '/EXE=D:\cadwork.dir\exe_2027'
    ```

!!! note
    `/EXE=` is especially useful when several cadwork versions are installed side by side — it
    decides whether the file opens in, for example, the 2026 or the 2027 program.

## Auto-running a Python script (`/PLUGIN=`)

The `/PLUGIN=` argument runs one of your Python plugins automatically right after the file opens.

```cmd
...\cadwork.dir\ci_start.exe "C:\path\to\myFile.3d" /PLUGIN=MyScript
```

The plugin name is the **name of the plugin folder** in your `API.x64` directory (the same folder
and script name you set up for the plugin bar). See [Getting Started](get_started.md) for how to
create and place a plugin.

!!! tip
    For unattended processing, let the script do its work and then save or export the result — for
    example `utility_controller.save_3d_file_silently()` or an export function — so each file is
    processed start to finish without any clicks. When cadwork was started with `/PLUGIN=` or
    `/RUNPROGRAM`, it closes itself once the script has finished; you don't need to close it.

## Running a plugin from any directory (`/RUNPROGRAM`)

Where `/PLUGIN=` only runs plugins that are **registered in the `API.x64` directory**, the
`/RUNPROGRAM` argument runs a plugin from **any directory you define**. The plugin does **not**
have to be registered in `API.x64` — you point directly at the file you want to run:

```cmd
...\cadwork.dir\ci_start.exe "C:\path\to\myFile.3d" /RUNPROGRAM="C:\my_plugins\export.py"
```

The target can be either a **`.py`** (Python) or a **`.dll`** (compiled) plugin:

```cmd
ci_start.exe "C:\path\to\myFile.3d" /RUNPROGRAM="D:\tools\my_plugin.py"    :: run a Python plugin
ci_start.exe "C:\path\to\myFile.3d" /RUNPROGRAM="D:\tools\my_plugin.dll"   :: run a compiled C++ plugin
```

!!! note
    Because `/RUNPROGRAM` takes a full path, you can keep plugins **anywhere** — on a network share,
    in a project folder, or in a development directory — without copying them into `API.x64` first.
    This is handy for testing a plugin during development or for running project-specific scripts.

### Running headless (`/NO-GUI`)

Combine `/RUNPROGRAM` with `/NO-GUI` to run the plugin **without the graphical user interface**.
cadwork starts, executes the plugin, and no window is shown — ideal for fully unattended and
server-side automation:

```cmd
ci_start.exe "C:\path\to\myFile.3d" /RUNPROGRAM="C:\my_plugins\export.py" /NO-GUI
```

!!! warning
    In headless mode there is no UI to interact with, so the plugin must do all of its work on its
    own and save or export its result.
    Avoid any dialogs or calls that wait for user input, as there is no window to answer them.

## Batch printing / export

For `.2d` files you can print plotter or laser frames directly from the command line:

```cmd
ci_start.exe "C:\path\plan.2d" /P A         :: print all plotter frames to the default plotter
ci_start.exe "C:\path\plan.2d" /P 1-2;5;7   :: print plotter frames 1, 2, 5, 7 (and following)
ci_start.exe "C:\path\plan.2d" /L A         :: print all laser frames to the default laser
ci_start.exe "C:\path\plan.2d" /L PDF       :: print all laser frames to the default PDF driver
```

| Argument     | Effect                                               |
| ------------ | ---------------------------------------------------- |
| `/P A`       | Print **all** plotter frames to the default plotter  |
| `/P 1-2;5;7` | Print the **selected** plotter frames                |
| `/L A`       | Print **all** laser frames to the default laser      |
| `/L PDF`     | Print **all** laser frames to the default PDF driver |

## Batch processing with PowerShell

Put it together to process every file in a folder. The example below opens each `.3d` file with a
fixed cadwork version and runs an export plugin on it:

```powershell
$exe    = 'D:\cadwork.dir\ci_start.exe'
$exeDir = 'D:\cadwork.dir\exe_2026'
$files  = Get-ChildItem 'C:\Projects\Batch' -Filter *.3d

foreach ($file in $files) {
    Write-Host "Processing $($file.Name)"
    Start-Process -FilePath $exe `
        -ArgumentList "`"$($file.FullName)`"", "/EXE=$exeDir", '/PLUGIN=MyExportScript' `
        -Wait
}
```

!!! warning
    The `-Wait` flag is important: it makes PowerShell wait until cadwork closes before opening the
    next file, so the files are processed **one at a time** instead of launching dozens of cadwork
    instances at once. Because cadwork closes itself after a `/PLUGIN=` script, the loop moves on
    as soon as the plugin has finished. Make sure the plugin saves or exports its result first.

## Troubleshooting batch runs

There is no console in a headless or unattended run, so problems are hard to see. A few habits
make them easy to find:

- **Test interactively first.** Run the plugin from the plugin bar on one file with the
  [console turned on](debug.md#enable-the-cadwork-console) before you start a batch.
- **Log to a file.** Write progress and errors to a log file next to the plugin, see
  [Debugging → Log to a file](debug.md#log-to-a-file). Include the file name in every message.
- **Never wait for input.** Dialogs, `input()` or message boxes block an unattended run forever.
- **Save before the script ends.** cadwork closes itself after a `/PLUGIN=` or `/RUNPROGRAM`
  script. Unsaved changes are lost, so call `save_3d_file_silently()` or an export function
  before the end. `close_cadwork_document_saved()` is skipped in these runs.
- **The loop hangs.** cadwork is waiting for something: a dialog, a licence prompt or an error
  message box. Run that file interactively to see what appears.
- **cadwork opens but the plugin doesn't run.** With `/PLUGIN=`, the value must be the exact
  plugin folder name in `API.x64` of the userprofile that this cadwork version uses. With
  `/RUNPROGRAM`, use the full path in quotes.

```python title="End of an unattended plugin"
import logging
from pathlib import Path

import utility_controller as uc

logging.basicConfig(
    filename=Path(__file__).resolve().parent / 'MyExportScript.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    force=True,
)
log = logging.getLogger('MyExportScript')
file_name = uc.get_3d_file_name()

try:
    ...  # do the work, export, ...
    uc.save_3d_file_silently()
    log.info('done: %s', file_name)
except Exception:
    log.exception('failed: %s', file_name)  # full traceback in the log file
```

## Other useful arguments

A few additional arguments that are handy for everyday use:

| Argument       | Effect                                            |
| -------------- | ------------------------------------------------- |
| `/GET_LICENCE` | Print the currently selected default licence type |
| `/USP`         | Define the directory for the Userprofile          |
| `/CATDIR`      | Define the directory for the Catalog              |
| `/WORKDIR`     | Define the directory for the Work folder          |

## See also

- [Getting Started](get_started.md): set up Python plugins in cadwork.
- [Debugging](debug.md): console, log files and IDE debuggers.
- [Videos](videos.md): example videos, including how to use Python in cadwork.
