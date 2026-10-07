---
hide:
  - toc
---

# element_controller

## create_node

```python
import cadwork  # import module
import element_controller as ec

point = cadwork.point_3d(100, 200, 300)  # create a cadwork Point
node = ec.create_node(point)
```
## create_square_beam_vectors
```python
import cadwork  # import module
import element_controller as ec

point = cadwork.point_3d(100, 200, 300)  # create a cadwork Point
vector_x = cadwork.point_3d(1.0, 0.0, 0.0)  # x vector length direction
vector_z = cadwork.point_3d(0.0, 0.0, 1.0)  # z vecotr height orientation
width = 200.0  # width/heigth of beam section
length = 2600.0  # beam length

beam = ec.create_square_beam_vectors(width, length, point, vector_x, vector_z)  # returns element_id
```

## stretch facet
```python
import element_controller as ec  # import module
import cadwork
import geometry_controller as gc


element_ids = ec.get_active_identifiable_element_ids()

distance = 75.0

for element_id in element_ids:
    xl = gc.get_xl(element_id) * distance
    ec.stretch_end_facet([element_id], xl)
```

## create surface - element boundary

```python
import cadwork
import geometry_controller as gc
import element_controller as ec

element_ids = ec.get_active_identifiable_element_ids()
for element_id in element_ids:
    facets = gc.get_element_facets(element_id)
    for facet in facets:
        ec.create_surface(facet)  # create surface
```

## create a rectangular panel

```python
import cadwork
import element_controller as ec

origin = cadwork.point_3d(0.0, 0.0, 0.0)
x_dir = cadwork.point_3d(1.0, 0.0, 0.0)
z_dir = cadwork.point_3d(0.0, 0.0, 1.0)

width, thickness, length = 1250.0, 100.0, 3000.0

panel = ec.create_rectangular_panel_vectors(width, thickness, length, origin, x_dir, z_dir)
```

## copy elements along a vector

```python
import cadwork
import element_controller as ec
import utility_controller as uc

element_ids = ec.get_active_identifiable_element_ids()
if not element_ids:
    uc.print_error('Please activate at least one element')
    raise SystemExit

spacing = uc.get_user_double('Spacing between copies [mm]')
count = uc.get_user_int('Number of copies')

for i in range(1, count + 1):
    ec.copy_elements(element_ids, cadwork.point_3d(spacing * i, 0.0, 0.0))
```

## delete short elements

```python
import element_controller as ec
import geometry_controller as gc
import utility_controller as uc

element_ids = ec.get_active_identifiable_element_ids()
min_length = uc.get_user_double('Delete elements shorter than [mm]')

short_ids = [element_id for element_id in element_ids if gc.get_length(element_id) < min_length]

if short_ids and uc.get_user_bool(f'Delete {len(short_ids)} elements?', False):
    ec.delete_elements(short_ids)
```

## line segments

A line can be built from a mixed path of straight, arc and spline segments.
The first segment must be `straight`, because it sets the start point of the path.
An arc runs through `support_position` to `position`. Consecutive `spline` segments are fitted through a single curve.

```python
import cadwork
import element_controller as ec
import utility_controller as uc

straight = cadwork.element_segment_type.straight
arc = cadwork.element_segment_type.arc
spline = cadwork.element_segment_type.spline
unused = cadwork.point_3d(0.0, 0.0, 0.0)

segments = [
    cadwork.element_segment(straight, cadwork.point_3d(0.0, 0.0, 0.0), unused),
    cadwork.element_segment(straight, cadwork.point_3d(2000.0, 0.0, 0.0), unused),
    cadwork.element_segment(arc, cadwork.point_3d(3000.0, 1000.0, 0.0), cadwork.point_3d(2700.0, 300.0, 0.0)),
    cadwork.element_segment(spline, cadwork.point_3d(3500.0, 2000.0, 0.0), unused),
    cadwork.element_segment(spline, cadwork.point_3d(4500.0, 2500.0, 0.0), unused),
    cadwork.element_segment(spline, cadwork.point_3d(5500.0, 2000.0, 0.0), unused),
]

line_id = ec.create_line_from_segments(segments)
if line_id == 0:
    uc.print_error('Line could not be created')
```

## read the segments of a line

```python
import attribute_controller as ac
import cadwork
import element_controller as ec

line_ids = [element_id for element_id in ec.get_active_identifiable_element_ids() if ac.is_line(element_id)]

for line_id in line_ids:
    print(f'Line {line_id}')
    for segment in ec.get_line_segments(line_id):
        if segment.type == cadwork.element_segment_type.arc:
            print(f'  {segment.type}: {segment.position} via {segment.support_position}')
        else:
            print(f'  {segment.type}: {segment.position}')
```

## offset a copy of a line

```python
import attribute_controller as ac
import cadwork
import element_controller as ec

offset = cadwork.point_3d(0.0, 0.0, 500.0)

for element_id in ec.get_active_identifiable_element_ids():
    if not ac.is_line(element_id):
        continue

    shifted = [
        cadwork.element_segment(s.type, s.position + offset, s.support_position + offset)
        for s in ec.get_line_segments(element_id)
    ]
    ec.create_line_from_segments(shifted)
```
