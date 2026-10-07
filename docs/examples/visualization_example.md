---
hide:
  - toc
---

# visualization_controller
## assign color to beam
```python
import cadwork  # import module
import element_controller as ec
import visualization_controller as vc

point = cadwork.point_3d(100, 200, 300)  # create a cadwork Point
vector_x = cadwork.point_3d(1.0, 0.0, 0.0)  # x vector length direction
vector_z = cadwork.point_3d(0.0, 0.0, 1.0)  # z vecotr height orientation
width = 200.0  # width/heigth of beam section
length = 2600.0  # beam length
color = 3  # color number as an int

beam = ec.create_square_beam_vectors(width, length, point, vector_x, vector_z)  # returns element_id

add_beam_color = vc.set_color([beam], color)  # input beam id (list), color (int)
```

## mutable - immutable
```python
import cadwork
import element_controller as ec
import visualization_controller as vc

element_ids = ec.get_active_identifiable_element_ids()

immutable = uc.get_user_bool('Do you want to set the elements to immutable ?', True)

if immutable:
    vc.set_immutable(element_ids)
```

## color elements by subgroup

```python
import attribute_controller as ac
import element_controller as ec
import visualization_controller as vc

colors = {}
for element_id in ec.get_active_identifiable_element_ids():
    subgroup = ac.get_subgroup(element_id)
    color = colors.setdefault(subgroup, len(colors) % 255 + 1)
    vc.set_color([element_id], color)
```

## show only panels

```python
import attribute_controller as ac
import element_controller as ec
import visualization_controller as vc

panel_ids = [element_id for element_id in ec.get_all_identifiable_element_ids() if ac.is_panel(element_id)]

vc.hide_all_elements()
vc.set_visible(panel_ids)
vc.zoom_all_elements()
```

## temporarily make the surroundings transparent

```python
import element_controller as ec
import utility_controller as uc
import visualization_controller as vc

active_ids = set(ec.get_active_identifiable_element_ids())
other_ids = [element_id for element_id in ec.get_all_identifiable_element_ids() if element_id not in active_ids]

original = {element_id: vc.get_element_transparency(element_id) for element_id in other_ids}
vc.set_element_transparency(other_ids, 80)
vc.refresh()

uc.get_user_bool('Restore transparency?', True)

for element_id, value in original.items():
    vc.set_element_transparency([element_id], value)
vc.refresh()
```
