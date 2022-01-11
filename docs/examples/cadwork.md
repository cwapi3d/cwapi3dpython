# cadwork

## create a cadwork point

In Python, a cadwork point_3d is represented as a 3D Point structure -> represented by the x, y and z coordinate values of the point. 
Find more information about points and vectors in tab geometry examples.

```python
import  cadwork                                 # import module

point = cadwork.point_3d(100, 200, 300)         # create a cadwork Point
```

## move a cadwork point 

```python 
import  cadwork                                 # import module

vector_x = cadwork.point_3d(1., 0., 0.)         # define vector
distance = 1500.0                               # moving distance

moved_point = point + (vector_x * distance)    
```

## distance between two 3D points

```python 
import  cadwork                                 # import module

point1 = cadwork.point_3d(100, 200, 300) 
point2 = cadwork.point_3d(300, 100, 200)                            

distance = point1.distance(point2)  
```

## add 3D points

```python 
import  cadwork                                 # import module

pt1 = cadwork.point_3d(100, 200, 300)

pt1 += cadwork.point_3d(800, 700, 600)

print(pt1)
```

## process types - ifc2x3 element_type

```python 
import  cadwork                                 # import module
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

### Process Type - getter/setter
```

is_hip_valley
is_jack_rafter
is_log
is_none
is_panel_1
is_panel_2
is_panel_3
is_panel_4
is_panel_5
is_purlin
is_rafter
is_rough_volume_framed_wall
is_rough_volume_log_home
is_rough_volume_solid_wood_wall
is_stud
is_tread
is_truss
is_user_1
is_user_2
is_user_3
is_user_4
is_user_5

set_hip_valley
set_jack_rafter
set_log
set_none
set_panel_1
set_panel_2
set_panel_3
set_panel_4
set_panel_5
set_purlin
set_rafter
set_rough_volume_framed_wall
set_rough_volume_log_home
set_rough_volume_solid_wood_wall
set_stud
set_tread
set_truss
set_user_1
set_user_2
set_user_3
set_user_4
set_user_5
```

<noscript>
    <img src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/pixel.gif">
</noscript>
<script defer src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/script.js"></script>