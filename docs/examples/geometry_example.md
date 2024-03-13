---
hide:
  - toc
---

# geometry_controller
## get beam points and vetors

```python 
import  cadwork                                 # import module
import  element_controller    as ec
import  geometry_controller   as gc

# get active element_ids
element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    vector_x = gc.get_xl(element_id) # returns local vector
    vector_y = gc.get_yl(element_id) # returns local vector
    vector_z = gc.get_zl(element_id) # returns local vector
    get_p1   = gc.get_p1(element_id) # returns cartesian point
    get_p2   = gc.get_p2(element_id) # returns cartesian point
    get_p3   = gc.get_p3(element_id) # returns cartesian point

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
area = 1500000.

# list comprehension 
filtered_ids = [element for element in element_ids if ac.is_panel(element)
                 and gc.get_element_reference_face_area(element) < area]

value = 'area smaller than '

ac.set_user_attribute(filtered_ids, 10, f'{value, area} mm2' )


```
