---
hide:
  - toc
---

# geometry_controller
## get beam points and vetors

```python
import cadwork  # import module
import element_controller as ec
import geometry_controller as gc

# get active element_ids
element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    vector_x = gc.get_xl(element_id)  # returns local vector
    vector_y = gc.get_yl(element_id)  # returns local vector
    vector_z = gc.get_zl(element_id)  # returns local vector
    get_p1 = gc.get_p1(element_id)  # returns cartesian point
    get_p2 = gc.get_p2(element_id)  # returns cartesian point
    get_p3 = gc.get_p3(element_id)  # returns cartesian point

    print(f"""the elements local vecotr z is: {vector_z} \n'
            the coordinates of the point_3 are {get_p3}""")
```

## filter elements according to a limit value
```python
import attribute_controller as ac
import element_controller as ec
import cadwork
import geometry_controller as gc

element_ids = ec.get_active_identifiable_element_ids()

# max area
area = 1500000.0

# list comprehension
filtered_ids = [
    element for element in element_ids if ac.is_panel(element) and gc.get_element_reference_face_area(element) < area
]

value = 'area smaller than '

ac.set_user_attribute(filtered_ids, 10, f'{value, area} mm2')
```

## total volume and weight

```python
import element_controller as ec
import geometry_controller as gc

element_ids = ec.get_active_identifiable_element_ids()

volume = sum(gc.get_volume(element_id) for element_id in element_ids)
weight = sum(gc.get_weight(element_id) for element_id in element_ids)

print(f'{len(element_ids)} elements, {volume / 1e9:.3f} m3, {weight:.1f} kg')
```

## extents of the element axes

```python
import cadwork
import element_controller as ec
import geometry_controller as gc

points = []
for element_id in ec.get_active_identifiable_element_ids():
    points.extend([gc.get_p1(element_id), gc.get_p2(element_id)])

minimum = cadwork.point_3d(min(p.x for p in points), min(p.y for p in points), min(p.z for p in points))
maximum = cadwork.point_3d(max(p.x for p in points), max(p.y for p in points), max(p.z for p in points))

print(f'min {minimum}, max {maximum}, diagonal {minimum.distance(maximum):.0f} mm')
```

## find the longest element

```python
import element_controller as ec
import geometry_controller as gc
import visualization_controller as vc

element_ids = ec.get_active_identifiable_element_ids()
longest = max(element_ids, key=gc.get_length)

vc.set_inactive(element_ids)
vc.set_active([longest])
vc.zoom_active_elements()
print(f'Element {longest}: {gc.get_length(longest):.0f} mm')
```
