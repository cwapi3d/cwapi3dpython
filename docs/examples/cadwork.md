---
hide:
  - toc
---

# cadwork

## create a cadwork point

In Python, a cadwork point_3d is represented as a 3D Point structure -> represented by the x, y and z coordinate values of the point.
Find more information about points and vectors in tab geometry examples.

```python
import cadwork  # import module

point = cadwork.point_3d(100, 200, 300)  # create a cadwork Point
```

## move a cadwork point

```python
import cadwork  # import module

vector_x = cadwork.point_3d(1.0, 0.0, 0.0)  # define vector
distance = 1500.0  # moving distance

moved_point = point + (vector_x * distance)
```

## distance between two 3D points

```python
import cadwork  # import module

point1 = cadwork.point_3d(100, 200, 300)
point2 = cadwork.point_3d(300, 100, 200)

distance = point1.distance(point2)
```

## add 3D points

```python
import cadwork  # import module

pt1 = cadwork.point_3d(100, 200, 300)

pt1 += cadwork.point_3d(800, 700, 600)

print(pt1)
```

## process type - ifc2x3 element_type

```python
import cadwork  # import module
import attribute_controller as ac
import bim_controller as bc
import element_controller as ec


element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    output_type = ac.get_output_type(element_id)
    ifc_type = bc.get_ifc2x3_element_type(element_id)

    if cadwork.process_type.is_rough_volume_framed_wall(output_type):
        ifc_type.set_ifc_wall()
        bc.set_ifc2x3_element_type([element_id], ifc_type)
```

## output type
```python
import element_controller as ec
import attribute_controller as ac
import cadwork


element_ids = ec.get_active_identifiable_element_ids()

for element in element_ids:
    if ac.is_panel(element):
        get_output_tpye = ac.get_output_type(element)
        get_output_tpye.set_panel_2()
        ac.set_output_type([element], get_output_tpye)
```

```python
import element_controller as ec
import attribute_controller as ac
import cadwork


element_ids = ec.get_active_identifiable_element_ids()


for element in element_ids:
    element_type = ac.get_element_type(element)
    print(cadwork.element_type.isWall(element_type))
```

## local axis system from two points

```python
import cadwork
import element_controller as ec

start = cadwork.point_3d(0.0, 0.0, 0.0)
end = cadwork.point_3d(3000.0, 1500.0, 800.0)

x_dir = (end - start).normalized()
y_dir = cadwork.point_3d(0.0, 0.0, 1.0).cross(x_dir).normalized()
z_dir = x_dir.cross(y_dir)

beam = ec.create_rectangular_beam_vectors(120.0, 240.0, start.distance(end), start, x_dir, z_dir)
```

## midpoint of an element axis

```python
import cadwork
import element_controller as ec
import geometry_controller as gc

for element_id in ec.get_active_identifiable_element_ids():
    midpoint = (gc.get_p1(element_id) + gc.get_p2(element_id)) / 2.0
    print(element_id, midpoint)
```

## classify the selection by element type

```python
from collections import defaultdict

import cadwork
import attribute_controller as ac
import element_controller as ec

checks = {
    'rectangular beam': lambda t: t.is_rectangular_beam(),
    'panel': lambda t: t.is_panel(),
    'drilling': lambda t: t.is_drilling_axis(),
    'line': lambda t: t.is_line(),
    'auxiliary': lambda t: t.is_auxiliary(),
}

groups = defaultdict(list)
for element_id in ec.get_active_identifiable_element_ids():
    element_type = ac.get_element_type(element_id)
    label = next((name for name, check in checks.items() if check(element_type)), 'other')
    groups[label].append(element_id)

for label, ids in groups.items():
    print(f'{label}: {len(ids)}')
```
