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

<noscript>
    <img src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/pixel.gif">
</noscript>
<script defer src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/script.js"></script>