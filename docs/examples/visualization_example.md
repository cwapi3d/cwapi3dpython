---
hide:
  - toc
---

# visualization_controller
## assign color to beam
```python 
import  cadwork                                 # import module
import  element_controller        as ec
import  visualization_controller  as vc

point      = cadwork.point_3d(100, 200, 300)         # create a cadwork Point   
vector_x   = cadwork.point_3d(1., 0., 0.)            # x vector length direction
vector_z   = cadwork.point_3d(0., 0., 1.)            # z vecotr height orientation 
width      = 200.                                    # width/heigth of beam section
length     = 2600.                                   # beam length
color     = 3                                       # color number as an int

beam            = ec.create_square_beam_vectors(width, length, 
                                                point, vector_x,
                                                vector_z) # returns element_id

add_beam_color = vc.set_color([beam], color) # input beam id (list), color (int)
```

## mutable - immutable
```python 
import cadwork
import element_controller as ec
import visualization_controller as vc

element_ids = ec.get_active_identifiable_element_ids()

immutable = uc.get_user_bool("Do you want to set the elements to immutable ?", True)

if immutable:
    vc.set_immutable(element_ids)

```

