---
hide:
  - toc
---

# Import Packages and Modules

!!! important "The module cadwork is to be loaded into the namespace at any time. This module is needed for many processes.<br> ```import cadwork``` "

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

For external modules, their path variable must be added to the system.

sys.path in Python

Sys is a built-in Python module that contains parameters specific to the system i.e. it contains variables and methods that interact with the interpreter and are also governed by it. 

sys.path
sys.path is a built-in variable within the sys module. It contains a list of directories that the interpreter will search in for the required module. 

When a module(a module is a python file) is imported within a Python file, the interpreter first searches for the specified module among its built-in modules. If not found it looks through the list of directories(a directory is a folder that contains related modules) defined by sys.path.

source: [GeeksforGeeks](https://www.geeksforgeeks.org/sys-path-in-python/)

Initializing sys.path 

By default, the interpreter looks for a module within the current directory. To make the interpreter search in some other directory **you just simply have to change the current directory**. The following example depicts a default path taken by the interpreter:

```python
# import modules
import  sys                                 
import  utility_controller as uc

# get userprofil path
USERPROFIL = uc.get_3d_userprofil_path()   

# appending a path
sys.path.append(USERPROFIL + '\\api.x64\\FolderName\\PackageFolder')

# printing all paths
print(sys.path)


# import external modules
import PackageFolder                    

```

