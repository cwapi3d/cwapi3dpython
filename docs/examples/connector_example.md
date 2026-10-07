---
hide:
  - toc
---

# connector_axis_controller

## check if axis are valid

```python
import cadwork  # import module
import attribute_controller as ac
import connector_axis_controller as ca
import element_controller as ec

element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    if ac.is_connector_axis(element_id):
        if ca.check_axis(element_id) == False:
            print(f'Element {element_id} has invlid axis')
```

## check settings - ignore vba calculation
```python
import attribute_controller as ac  # import module
import cadwork
import element_controller as ec
import visualization_controller as vc

element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    if ac.get_ignore_in_vba_calculation(element_id):
        vc.set_color([element_id], 90)
```

## create a standard connector between two points

```python
import cadwork
import connector_axis_controller as ca
import menu_controller as mec
import utility_controller as uc

connector_name = mec.display_simple_menu(ca.get_standard_connector_list())
if connector_name:
    start = uc.get_user_point()
    end = uc.get_user_point()
    ca.create_standard_connector(connector_name, start, end)
```

## report bolts of connector axes

```python
import attribute_controller as ac
import connector_axis_controller as ca
import element_controller as ec

for element_id in ec.get_active_identifiable_element_ids():
    if not ac.is_connector_axis(element_id):
        continue

    items = ', '.join(ca.get_axis_item_name(guid) for guid in ca.get_axis_items_guids(element_id))
    print(
        f'Axis {element_id}: bolt d={ca.get_bolt_diameter(element_id):.1f} '
        f'l={ca.get_bolt_length(element_id):.1f}, sections={ca.get_section_count(element_id)}, items=[{items}]'
    )
```

## enable automatic bolt length

```python
import attribute_controller as ac
import connector_axis_controller as ca
import element_controller as ec

axis_ids = [element_id for element_id in ec.get_active_identifiable_element_ids() if ac.is_connector_axis(element_id)]

for axis_id in axis_ids:
    if not ca.get_bolt_length_automatic(axis_id):
        ca.set_bolt_length_automatic(axis_id, True)

ec.recreate_elements(axis_ids)
```
