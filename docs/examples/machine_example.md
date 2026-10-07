---
hide:
  - toc
---

# machine_controller
## check production list discrepancies

```python
import machine_controller as mac
import cadwork

btl_enum = 5  # VERSION: "BTL V10.6"
# The enumeration is done according to the machine export listing in the export menu.
file_path = 'C:\\Downloads\\api_btl.btl'
mac.export_btl(btl_enum, file_path)
```

```python
import machine_controller as mac
import cadwork

hundegger_enum = 3  # Hundegger K2
# The enumeration is done according to the machine export listing in the export menu.
mac.export_hundegger(hundegger_enum)
```

## list BTL processings per element

```python
import attribute_controller as ac
import cadwork
import element_controller as ec
import machine_controller as mac

btl_version = cadwork.btl_version.btlx_2_1

for element_id in ec.get_active_identifiable_element_ids():
    print(ac.get_name(element_id), element_id)
    for processing_id in mac.get_element_btl_processings(element_id, btl_version):
        name = mac.get_processing_name(element_id, processing_id)
        code = mac.get_processing_code(element_id, processing_id)
        print(f'  {code}: {name}')
```

## calculate BTL machine data

```python
import cadwork
import element_controller as ec
import machine_controller as mac

element_ids = ec.get_active_identifiable_element_ids()
mac.calculate_btl_machine_data(element_ids, cadwork.btl_version.btlx_2_1)
```

## silent Hundegger export

```python
import os

import cadwork
import machine_controller as mac
import utility_controller as uc

base_name = os.path.splitext(uc.get_3d_file_name())[0]
file_path = os.path.join(r'C:\Exports\Hundegger', base_name)

mac.export_hundegger_with_file_path_silent(cadwork.hundegger_machine_type.k2, file_path)
```
