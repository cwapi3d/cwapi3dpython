---
hide:
  - toc
---

# bim_controller

## get GlobalId (IfcGuid)

```python
import cadwork
import bim_controller as bc
import element_controller as ec

# get active element_ids
element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    guid = bc.get_ifc_guid(element_id)
    print(guid)
```

## set IfcTyp

```python
import cadwork
import attribute_controller as ac
import bim_controller as bc
import element_controller as ec

# get active element_ids
element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    if ac.is_wall(element_id):
        ifc_type = bc.get_ifc2x3_element_type(element_id)
        ifc_type.set_ifc_wall()  # notation for setting ifc types
        bc.set_ifc2x3_element_type([element_id], ifc_type)
```

## set Building and Storey

```python
import cadwork
import bim_controller as bc
import element_controller as ec

# get active element_ids
element_ids = ec.get_active_identifiable_element_ids()
bc.set_building_and_storey([element_ids], 'BuildingName', 'Level_1')
```

## get Building

```python
import cadwork
import bim_controller as bc
import element_controller as ec

# get active element_ids
element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    bc.get_building(element_id)
    storey_name = bc.get_storey(element_id)
```

## get Storey height

```python
import cadwork
import bim_controller as bc
import element_controller as ec

# get active element_ids
element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    building_name = bc.get_building(element_id)
    storey_name = bc.get_storey(element_id)
    storey_height = bc.get_storey_height(building_name, storey_name)
    print(storey_height)
```

## print IfcType to console

```python
import cadwork
import bim_controller as bc
import element_controller as ec

# get active element_ids
element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    ifc_type = bc.get_ifc2x3_element_type(element_id)
    print(f'Ifc{ifc_type}')
```

## IfcType getter

```python
import      element_controller      as ec
import      bim_controller          as bc
import      cadwork


element_ids = ec.get_active_identifiable_element_ids()


for element in element_ids:
    ifc_type = bc.get_ifc2x3_element_type(element)
    if cadwork.ifc_2x3_element_type.is_ifc_member(ifc_type):
        # do something
```

## list buildings and storeys

```python
import bim_controller as bc

for building in bc.get_all_buildings():
    print(building)
    for storey in bc.get_all_storeys(building):
        height = bc.get_storey_height(building, storey)
        count = len(bc.get_elements_for_storey(building, storey))
        print(f'  {storey}: height {height:.0f} mm, {count} elements')
```

## assign storeys by element height

```python
import bim_controller as bc
import element_controller as ec
import geometry_controller as gc

building = 'Building_A'
storeys = [('Level_0', 0.0), ('Level_1', 3000.0), ('Level_2', 6000.0)]

for element_id in ec.get_active_identifiable_element_ids():
    z = min(gc.get_p1(element_id).z, gc.get_p2(element_id).z)
    storey = storeys[0][0]
    for name, level in storeys:
        if z >= level:
            storey = name
    bc.set_building_and_storey([element_id], building, storey)
```

## export IFC4 per storey

```python
import os

import bim_controller as bc
import utility_controller as uc

target_dir = uc.get_user_path_from_dialog()

for building in bc.get_all_buildings():
    for storey in bc.get_all_storeys(building):
        element_ids = bc.get_elements_for_storey(building, storey)
        if not element_ids:
            continue
        file_path = os.path.join(target_dir, f'{building}_{storey}.ifc')
        if not bc.export_ifc4_silently(element_ids, file_path):
            uc.print_error(f'Export failed: {file_path}')
```
