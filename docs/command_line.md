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

## Running a script from anywhere (`/RUNPROGRAM=`)

Where `/PLUGIN=` runs a plugin by its folder name in `API.x64`, `/RUNPROGRAM=` runs a **`.py` or
`.dll` from any location** — the file does not have to be installed as a plugin. Pass the full path
to the script:

```powershell
D:\cadwork.dir\ci_start.exe ".\Downloads\test_elements_walls.3d" /EXE=D:\cadwork.dir\exe_2026 /RUNPROGRAM="C:\Users\JonDoe\Downloads\export_elements_jsonl.py"
```

!!! tip
Quote the path if it contains spaces. As with `/PLUGIN=`, have the script save or export its
result so each file is processed start to finish without any clicks.

!!! warning
The full `/RUNPROGRAM=` token is subject to the 127-character switch limit described in
[Switch argument length limit](#switch-argument-length-limit-127-characters) below — a long
script path can be silently truncated.

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
instances at once. For a fully unattended run, the plugin should save/export its result and
then close the file.

## Other useful arguments

A few additional arguments that are handy for everyday use:

| Argument       | Effect                                            |
| -------------- | ------------------------------------------------- |
| `/GET_LICENCE` | Print the currently selected default licence type |
| `/USP`         | Define the directory for the Userprofile          |
| `/CATDIR`      | Define the directory for the Catalog              |
| `/WORKDIR`     | Define the directory for the Work folder          |

## Switch argument length limit (127 characters)

`ci_start.exe` forwards each switch argument to the detached `3d.exe` through a fixed **128-byte
buffer**, so every switch token is **silently truncated to 127 characters**. The bare model path
is passed through intact — only the switch tokens (`/EXE=…`, `/PLUGIN=…`, and the like) are
affected.

The truncation is silent: there is no error message. When an over-long token is cut mid-value —
for example a `/RUNPROGRAM=` or `/PLUGIN=` script path that ends up pointing at a nonexistent
script — `3d.exe` finds nothing to run and cadwork simply **closes about 3 seconds after
starting**, without having done anything. This was verified on 2026-07-06 by capturing the spawned
`3d.exe` command line: a 128-character `/RUNPROGRAM=` token arrived cut mid-filename, while the
bare model path passed through intact.

!!! warning
Keep every switch token at or below **127 characters**. This includes the `/EXE=` and
`/PLUGIN=` prefixes themselves, not just the path or name after them. If a token would be too
long, shorten the path (for example by installing to a shorter directory, or by using the plugin
folder name rather than a long absolute path) so the whole token fits.

If you drive `ci_start.exe` from a script, validate the length before launching:

```powershell
$MaxSwitchLength = 127   # ci_start.exe truncates each switch token to 127 characters

$switches = @("/EXE=$exeDir", "/RUNPROGRAM=$scriptPath")
foreach ($switch in $switches) {
    if ($switch.Length -gt $MaxSwitchLength) {
        throw "Switch token exceeds $MaxSwitchLength characters and will be truncated: $switch"
    }
}
```

## See also

- [Getting Started](get_started.md) — set up Python plugins in cadwork.
- [Videos](videos.md) — example videos, including how to use Python in cadwork.
