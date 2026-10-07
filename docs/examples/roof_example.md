---
hide:
  - toc
---

# roof_controller

## list roof elements with profile length

```python
import attribute_controller as ac
import roof_controller as rc

for element_id in rc.get_all_caddy_element_ids():
    print(f'{ac.get_name(element_id)} ({element_id}): {rc.get_profile_length(element_id):.0f} mm')
```

## total edge lengths per edge type

Useful to estimate flashing and tile accessories.

```python
import roof_controller as rc

edge_types = ['ridge', 'eave', 'hip', 'valley', 'vergeleft', 'vergeright']
caddy_ids = rc.get_all_caddy_element_ids()

for edge_type in edge_types:
    total = sum(rc.get_edge_length(element_id, edge_type) for element_id in caddy_ids)
    print(f'{edge_type:12} {total / 1000:8.2f} m')
```

## write eave length into a user attribute

```python
import attribute_controller as ac
import roof_controller as rc

attribute_number = 15
ac.set_user_attribute_name(attribute_number, 'Eave length [m]')

for element_id in rc.get_all_caddy_element_ids():
    eave_length = rc.get_edge_length(element_id, 'eave') / 1000
    ac.set_user_attribute([element_id], attribute_number, f'{eave_length:.2f}')
```
