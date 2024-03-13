---
hide:
  - toc
---

# endtype_controller

## get endtype name at start point of the element

```python 
import  cadwork                                 # import module
import endtype_controller as etc
import element_controller as ec

element_ids = ec.get_active_identifiable_element_ids()
for element_id in element_ids:
    endtype_name = etc.get_endtype_name_start(element_id)
    print(endtype_name)
```


## get endtype name at start point of the element

```python 
import  cadwork                                 # import module
import endtype_controller as etc
import element_controller as ec
import utility_controller as uc

element_ids = ec.get_active_identifiable_element_ids()

new_endtype = uc.get_user_string("name of the new end-type")

i = 0
for element_id in element_ids:
    endtype_name = etc.get_endtype_name_start(element_id)
    if endtype_name == "V_8": # V_8 = name of an endtpye
        etc.set_endtype_name_start(element_id, new_endtype)
        i += 1
uc.print_error("Number of end-type replaced:%d" % i)
```

