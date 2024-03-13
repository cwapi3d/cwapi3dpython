---
hide:
  - toc
---

# File_controller

## Export Rhino File

```python                         
import file_controller as fc        # import module
import element_controller as ec

element_ids = ec.get_active_identifiable_element_ids()

# list: aElementIdList, str: aFilePath, int: aVersion, bool: aUseDefaultAssignment, bool: aWriteStandardAttributes
fc.export_rhino_file(element_ids, "C:\Downloads\RhinoExport.3dm", 6, True, True)

```

## Export Rhino File - create directory
```python
import file_controller as fc 
import element_controller as ec
import os

target_path = 'C:\\Users\\YourUsername\\Downloads\\RhinoExports\\'

try:
    create_direction = os.mkdir(target_path)
    # replace YourUsername with your username on your PC or add another directory 
    # mkdir will create a folder with the Name RhinoExports
except FileExistsError: # excepiton handling - if folder exists 
    print("Folder already exists!")

# path to the new file  
file_name = target_path + 'TestExport.3dm'


element_ids = ec.get_active_identifiable_element_ids()

fc.export_rhino_file(element_ids, file_name, 6, True, True)
```

## Import Step File

```python                         
import file_controller as fc        # import module
import element_controller as ec

import_file = uc.get_new_user_file_from_dialog("*.stp")
# str: aFilePath, float: aScale, bool: aMesageOption
fc.import_step_file_with_message_option(import_file, 0.0001, True)

```

