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

```powershell
D:\cadwork.dir\ci_start.exe "C:\Users\Me\Downloads\timber-framed-elements.3d" /EXE=D:\cadwork.dir\exe_2026
```

You can also launch it with PowerShell's `Start-Process`, which lets the prompt return immediately
and gives you control over the window state:

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
    example `file_controller.save_3d_file()` or an export controller call — so each file is
    processed start to finish without any clicks.

## Batch printing / export

For `.2d` files you can print plotter or laser frames directly from the command line:

```cmd
ci_start.exe "C:\path\plan.2d" /P A         :: print all plotter frames to the default plotter
ci_start.exe "C:\path\plan.2d" /P 1-2;5;7   :: print plotter frames 1, 2, 5, 7 (and following)
ci_start.exe "C:\path\plan.2d" /L A         :: print all laser frames to the default laser
ci_start.exe "C:\path\plan.2d" /L PDF       :: print all laser frames to the default PDF driver
```

| Argument        | Effect                                                   |
| --------------- | -------------------------------------------------------- |
| `/P A`          | Print **all** plotter frames to the default plotter      |
| `/P 1-2;5;7`    | Print the **selected** plotter frames                    |
| `/L A`          | Print **all** laser frames to the default laser          |
| `/L PDF`        | Print **all** laser frames to the default PDF driver     |

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
    instances at once. For a fully unattended run, the plugin should save/export its result and
    then close the file.

## Other useful arguments

A few additional arguments that are handy for everyday use:

| Argument            | Effect                                              |
| ------------------- | --------------------------------------------------- |
| `/GET_LICENCE`      | Print the currently selected default licence type   |

## See also

- [Getting Started](get_started.md) — set up Python plugins in cadwork.
- [Videos](videos.md) — example videos, including how to use Python in cadwork.
