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


