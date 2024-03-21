---
hide:
  - toc
---

# connector_axis_controller

## check if axis are valid

```python 
import  cadwork                                 # import module
import attribute_controller as ac
import connector_axis_controller as ca
import element_controller as ec

element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    if ac.is_connector_axis(element_id):
        if ca.check_axis(element_id) == False:
            print(f"Element {element_id} has invlid axis")
```

## check settings - ignore vba calculation
```python 
import  attribute_controller  as ac     # import module
import  cadwork
import  element_controller    as ec   
import visualization_controller as vc

element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    if ac.get_ignore_in_vba_calculation(element_id):
        vc.set_color([element_id], 90)

```

