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
    drillings.append(ec.create_drilling_vectors(40, 50, 
                    cadwork.point_3d(p, 0., 0.), cadwork.point_3d(0., 0.,  -1.)))

vc.set_color(drillings, 5)

uc.enable_auto_display_refresh()
ec.recreate_elements(drillings)

end = timer()
print(timedelta(seconds=end-start))

# measuring time in seconds when disable display refresh    0:00:00.057018s
# without disabling, the exucation duration is              0:00:01.831747s

```

## user interactions
```python 
import cadwork
import utility_controller as uc
import element_controller as ec

drill_bool = uc.get_user_bool("Do u want to create a drilling ?", True)

if drill_bool:
    pt = uc.get_user_point()
    length = uc.get_user_double('Enter the drilling length')
    drilling = ec.create_drilling_vectors(40, length, pt, cadwork.point_3d(0., 0.,  -1.))

```




