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
        ifc_type.set_ifc_wall() # notation for setting ifc types
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

