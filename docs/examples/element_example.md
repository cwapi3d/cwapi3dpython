# element_controller

## create_node

```python 
import  cadwork                                 # import module
import  element_controller as ec

point = cadwork.point_3d(100, 200, 300)         # create a cadwork Point   
node = ec.create_node(point)
```
## create_square_beam_vectors
```python 
import  cadwork                                 # import module
import  element_controller  as ec

point      = cadwork.point_3d(100, 200, 300)    # create a cadwork Point   
vector_x   = cadwork.point_3d(1., 0., 0.)       # x vector length direction
vector_z   = cadwork.point_3d(0., 0., 1.)       # z vecotr height orientation 
width      = 200.                               # width/heigth of beam section
length     = 2600.                              # beam length

beam       = ec.create_square_beam_vectors(width, length, 
                                            point, vector_x, 
                                            vector_z) # returns element_id
```

## stretch facet
```python 
import element_controller as ec                 # import module
import cadwork
import geometry_controller as gc


element_ids = ec.get_active_identifiable_element_ids()

distance = 75.

for element_id in element_ids:
    xl = gc.get_xl(element_id) * distance
    ec.stretch_end_facet([element_id], xl)
```


<noscript>
    <img src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/pixel.gif">
</noscript>
<script defer src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/script.js"></script>