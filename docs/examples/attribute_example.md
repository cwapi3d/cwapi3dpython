---
hide:
  - toc
---

# attribute_controller

## Conditions

```python
import attribute_controller as ac  # import module
import element_controller as ec


# get active element_ids
element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    if ac.is_panel(element_id):  # returns boolean
        print(True)
    else:
        print(False)
```

```python
import  attribute_controller  as ac     # import module
import  element_controller    as ec
import  cadwork


# get active element_ids
element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    element_type = ac.get_element_type(element_id)
    if element_type.is_rectangular_beam():
        # do something
```

## set attributes
```python
import attribute_controller as ac  # import module
import element_controller as ec

element_ids = ec.get_active_identifiable_element_ids()

ac.set_user_attribute_name(11, 'ExampleAttribute')
ac.set_user_attribute(element_ids, 11, 'Hello World!')
```

## get attributes
```python
import attribute_controller as ac  # import module
import element_controller as ec


# get active element_ids
element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    user_attr = ac.get_user_attribute(element_id, 20)  # 20 = attribute number
    user_attr_name = ac.get_user_attribute_name(20)
    element_guid = ec.get_element_cadwork_guid(element_id)

    print(user_a_name, user_a, element_guid)
```


## assign attributes to beam
```python
import cadwork  # import module
import attribute_controller as ac
import element_controller as ec

point = cadwork.point_3d(100, 200, 300)  # create a cadwork Point
vector_x = cadwork.point_3d(1.0, 0.0, 0.0)  # x vector length direction
vector_z = cadwork.point_3d(0.0, 0.0, 1.0)  # z vecotr height orientation
width = 200.0  # width/heigth of beam section
length = 2600.0  # beam length
name = 'My first beam :)'  # name as a string

beam = ec.create_square_beam_vectors(width, length, point, vector_x, vector_z)  # returns element_id

add_beam_name = ac.set_name([beam], name)  # input beam id (list), name (string)
```

## count elements per subgroup

```python
from collections import Counter

import attribute_controller as ac
import element_controller as ec

element_ids = ec.get_active_identifiable_element_ids()
counts = Counter(ac.get_subgroup(element_id) for element_id in element_ids)

for subgroup, count in counts.most_common():
    print(f'{subgroup or "<no subgroup>"}: {count}')
```

## set name, group and subgroup in one step

```python
import attribute_controller as ac
import element_controller as ec
import utility_controller as uc

element_ids = ec.get_active_identifiable_element_ids()
if not element_ids:
    uc.print_error('Please activate at least one element')
    raise SystemExit

ac.set_name(element_ids, uc.get_user_string('Name'))
ac.set_group(element_ids, uc.get_user_string('Group'))
ac.set_subgroup(element_ids, uc.get_user_string('Subgroup'))
```

## write element dimensions into a user attribute

```python
import attribute_controller as ac
import element_controller as ec
import geometry_controller as gc

attribute_number = 12
ac.set_user_attribute_name(attribute_number, 'Dimensions')

for element_id in ec.get_active_identifiable_element_ids():
    width = gc.get_width(element_id)
    height = gc.get_height(element_id)
    length = gc.get_length(element_id)
    ac.set_user_attribute([element_id], attribute_number, f'{width:.0f} x {height:.0f} x {length:.0f}')
```
