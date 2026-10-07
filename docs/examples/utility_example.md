---
hide:
  - toc
---

# utility_controller
## display refresh

Speed up the process within cadwork by disabling the display refresh.

```python
import cadwork
import utility_controller as uc
import element_controller as ec
import visualization_controller as vc
from timeit import default_timer as timer
from datetime import timedelta

start = timer()
uc.disable_auto_display_refresh()

drillings = []
points_range = range(1, 15000, 120)
for p in points_range:
    drillings.append(
        ec.create_drilling_vectors(40, 50, cadwork.point_3d(p, 0.0, 0.0), cadwork.point_3d(0.0, 0.0, -1.0))
    )

vc.set_color(drillings, 5)

uc.enable_auto_display_refresh()
ec.recreate_elements(drillings)

end = timer()
print(timedelta(seconds=end - start))

# measuring time in seconds when disable display refresh    0:00:00.057018s
# without disabling, the exucation duration is              0:00:01.831747s
```

## user interactions
```python
import cadwork
import utility_controller as uc
import element_controller as ec

drill_bool = uc.get_user_bool('Do u want to create a drilling ?', True)

if drill_bool:
    pt = uc.get_user_point()
    length = uc.get_user_double('Enter the drilling length')
    drilling = ec.create_drilling_vectors(40, length, pt, cadwork.point_3d(0.0, 0.0, -1.0))
```

## project information

```python
import utility_controller as uc

info = {
    'File': uc.get_3d_file_name(),
    'Project': uc.get_project_name(),
    'Number': uc.get_project_number(),
    'Customer': uc.get_project_customer(),
    'Architect': uc.get_project_architect(),
    'City': uc.get_project_city(),
    'cadwork': f'{uc.get_3d_version_name()} (build {uc.get_3d_build()})',
}

for key, value in info.items():
    uc.print_to_console(f'{key:10} {value}')
```

## pick points and create beams between them

```python
import cadwork
import element_controller as ec
import utility_controller as uc

points = uc.get_user_points()
width = uc.get_user_double('Beam width [mm]')
height = uc.get_user_double('Beam height [mm]')
z_dir = cadwork.point_3d(0.0, 0.0, 1.0)

for start, end in zip(points, points[1:]):
    ec.create_rectangular_beam_points(width, height, start, end, start + z_dir)
```

## number the active elements

```python
import attribute_controller as ac
import element_controller as ec
import utility_controller as uc

prefix = uc.get_user_string('Name prefix')
start = uc.get_user_int('Start number')

for number, element_id in enumerate(ec.get_active_identifiable_element_ids(), start=start):
    ac.set_name([element_id], f'{prefix}{number:03d}')
```
