# Set upt Python in cadwork - Step by Step

To use Python scripts in cadwork, they must be located in the userprofile in the folder api.x64. 

A folder must be created in the api.x64 directory for each script. The Python script must have the same name as the folder so that it can be executed.  

![Screenshot](img/directory.png){: style="width:600px"}

![Screenshot](img/script.png){: style="width:600px"}


Once you have placed a folder and a script in the directory, you can start a cadwork 3D file. 

Now show the plugin bar (Window -> Plugins). For the moment you see a button with the name of the plugin/script folder. 

Instead of this name you can place an icon in the api.x64 folder under the plugin directory.

!!! important "Scripts that should be callable from the plugin bar must be placed in the folder<br> ..\userprofile_28\3d\API.x64. <br>A folder must be created in this directory. The name of the folder must have the same name as the script."
    
    * ..\userprofile_28\3d\API.x64 (Directory)
        * MyFirstScript (Folder)
            * MyFirstScript.py (Python File)
            * Icon.png (Plugin Icon, size ~30x30 pixel)

## easy start with Python IDLE :bulb:
IDLE is Python’s Integrated Development and Learning Environment.

The IDLE allows you to run Python scripts directly in cadwork. 


IDLE has the following features:

* coded in 100% pure Python, using the tkinter GUI toolkit
* cross-platform: works mostly the same on Windows, Unix, and macOS
* Python shell window (interactive interpreter) with colorizing of code input, output, and error messages
* multi-window text editor with multiple undo, Python colorizing, smart indent, call tips, auto completion, and other features
* search within any window, replace within editor windows, and search through multiple files (grep)
* debugger with persistent breakpoints, stepping, and viewing of global and local namespaces
configuration, browsers, and other dialogs

Menus
IDLE has two main window types, the Shell window and the Editor window. It is possible to have multiple editor windows simultaneously. On Windows and Linux, each has its own top menu. Each menu documented below indicates which window type it is associated with.
Output windows, such as used for Edit => Find in Files, are a subtype of editor window. They currently have the same top menu but a different default title and context menu.
On macOS, there is one application menu. It dynamically changes according to the window currently selected. It has an IDLE menu, and some entries described below are moved around to conform to Apple guidelines.

### download / clone IDLE in cadwork userprofile

Go to [Github - cadwork](https://github.com/CadworkMontreal/PythonConsole) -> click on Button **Code** and clone or Download ZIP into your directory -> c:\users\public\documents\cadwork\userprofil_28\API.x64\PythonConsole'. 

![Screenshot](img/clone.png){: style="width:800px"}

### add an icon
You can add an icon into the directory c:\users\public\documents\cadwork\userprofil_27\API.x64\PythonConsole'. The file must have the following name **Icon.png** . The icon should be scaled down to 30x30 pixels.

### run Code
Open cadwork 3D and open the Python Console (IDLE) from the plugin bar. 

Save your .py script an hit key F5 oder go via Menu -> Run -> Run Module
![Screenshot](img/run.png){: style="width:800px"}

Example Code:

```python
# import modules
import  cadwork   
import  element_controller      as ec
import  attribute_controller    as ac

# get active element_ids
element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    subgroup = ac.get_subgroup(element_id) # get subgroup name of active element_ids
    print(subgroup) # print the subgroup names
```



## Use your prefered IDE (advanced user)
Of course, you can also use any other Python IDE. 
For this purpose e.g. PyCharm is recommended. 
Install the CWAPI3D package into your environment via ```pip install cwapi3d```. Open your IDE and start with your script.


### Python version used in cadwork :bulb:  <br>
Cadwork uses CPython version 3.8.6 

### Install CWAPI3D package on your device

```python
pip install cwapi3d
```
[Github - cwapi3d python](https://github.com/cwapi3d/cwapi3dpython){target=_blank}

The script cannot be run from the IDE (PyCharm, VS Code, ...). The script call must be made in cadwork (Plugin Bar). 

[Example Video - How to Python in cadwork](example.md#Videos) :tv: <br>


## Import Packages and Modules

**Import packages** <br>
As CPython is used in cadwork, it is possible to work with external modules. The modules included in Python as standard can be integrated normally by loading the modules. 

```python
# import modules
import  cadwork  
import  math
import  csv
import  tkinter
...
...
```

**Import external packages** <br>
```python
# import modules
import  sys                                 
import  utility_controller as uc

USERPROFIL = uc.get_3d_userprofil_path()   # get userprofil path

paths = [(USERPROFIL + '\\api.x64\\FolderName\\PackageFolder'),
        ("C:\\Program Files\\cadwork.dir\\EXE_28\\Pclib.x64\\python38\\site-packages")
          ]

for path in paths:
    if path not in sys.path:
        sys.path.append(path)

# import external modules
import external_package1                    
import external_package2
import external_package3

```





