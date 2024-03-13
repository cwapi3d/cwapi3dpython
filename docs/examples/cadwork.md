---
hide:
  - toc
---

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

## process type - ifc2x3 element_type

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

## output type
```python
import      element_controller      as ec
import      attribute_controller    as ac
import      cadwork


element_ids = ec.get_active_identifiable_element_ids()

for element in element_ids:
    if ac.is_panel(element):
        get_output_tpye = ac.get_output_type(element)
        get_output_tpye.set_panel_2()
        ac.set_output_type([element], get_output_tpye)
```

```python
import      element_controller      as ec
import      attribute_controller    as ac
import      cadwork


element_ids = ec.get_active_identifiable_element_ids()


for element in element_ids:
    element_type = ac.get_element_type(element)
    print(cadwork.element_type.isWall(element_type))
```

