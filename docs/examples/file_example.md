---
hide:
  - toc
---

# File_controller

## Export Rhino File

```python
import file_controller as fc  # import module
import element_controller as ec

element_ids = ec.get_active_identifiable_element_ids()

# list: aElementIdList, str: aFilePath, int: aVersion, bool: aUseDefaultAssignment, bool: aWriteStandardAttributes
fc.export_rhino_file(element_ids, 'C:\Downloads\RhinoExport.3dm', 6, True, True)
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
except FileExistsError:  # excepiton handling - if folder exists
    print('Folder already exists!')

# path to the new file
file_name = target_path + 'TestExport.3dm'


element_ids = ec.get_active_identifiable_element_ids()

fc.export_rhino_file(element_ids, file_name, 6, True, True)
```

## Import Step File

```python
import file_controller as fc  # import module
import element_controller as ec

import_file = uc.get_new_user_file_from_dialog('*.stp')
# str: aFilePath, float: aScale, bool: aMesageOption
fc.import_step_file_with_message_option(import_file, 0.0001, True)
```

## export a STEP file

```python
import element_controller as ec
import file_controller as fc
import utility_controller as uc

element_ids = ec.get_active_identifiable_element_ids()
if not element_ids:
    uc.print_error('Please activate the elements to export')
    raise SystemExit

step_ap214 = 214
fc.export_step_file(element_ids, r'C:\Exports\model.stp', 1.0, step_ap214, False)
```

## export the active elements in several formats

```python
import os

import element_controller as ec
import file_controller as fc
import utility_controller as uc

element_ids = ec.get_active_identifiable_element_ids()
target_dir = uc.get_user_path_from_dialog()
base_name = os.path.splitext(uc.get_3d_file_name())[0]

fc.export_stl_file(element_ids, os.path.join(target_dir, f'{base_name}.stl'))
fc.export_glb_file(element_ids, os.path.join(target_dir, f'{base_name}.glb'))
fc.export_webgl(element_ids, os.path.join(target_dir, f'{base_name}.html'))
```

## export visible elements to DXF by subgroup layers

```python
import cadwork
import file_controller as fc
import utility_controller as uc

file_path = r'C:\Exports\model.dxf'
success = fc.export_dxf_file(file_path, cadwork.dxf_layer_format_type.subgroup, cadwork.dxf_export_version.auto_cad_r27)

if not success:
    uc.print_error(f'DXF export failed: {file_path}')
```
