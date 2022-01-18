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

## IfcType - getter/setter

```
is_ifc_beam
is_ifc_building_element_part
is_ifc_building_element_proxy
is_ifc_chimney
is_ifc_column
is_ifc_covering
is_ifc_curtain_wall
is_ifc_discrete_accessory
is_ifc_door
is_ifc_fastener
is_ifc_flow_segment
is_ifc_footing
is_ifc_furnishing_element
is_ifc_mechanical_fastener
is_ifc_member
is_ifc_opening_element
is_ifc_plate
is_ifc_railing
is_ifc_ramp
is_ifc_ramp_flight
is_ifc_roof
is_ifc_slab
is_ifc_space
is_ifc_stair
is_ifc_stair_flight
is_ifc_wall
is_ifc_wall_standard_case
is_ifc_window
is_none

set_ifc_beam
set_ifc_building_element_part
set_ifc_building_element_proxy
set_ifc_chimney
set_ifc_column
set_ifc_covering
set_ifc_curtain_wall
set_ifc_discrete_accessory
set_ifc_door
set_ifc_fastener
set_ifc_flow_segment
set_ifc_footing
set_ifc_furnishing_element
set_ifc_mechanical_fastener
set_ifc_member
set_ifc_opening_element
set_ifc_plate
set_ifc_railing
set_ifc_ramp
set_ifc_ramp_flight
set_ifc_roof
set_ifc_slab
set_ifc_space
set_ifc_stair
set_ifc_stair_flight
set_ifc_wall
set_ifc_wall_standard_case
set_ifc_window
set_none
```

<noscript>
    <img src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/pixel.gif">
</noscript>
<script defer src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/script.js"></script>