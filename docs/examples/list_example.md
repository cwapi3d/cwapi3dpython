---
hide:
  - toc
---

# list_controller
## check production list discrepancies

```python 
import cadwork
import list_controller as lc
import utility_controller as uc
import visualization_controller as vc


checked_element_ids = lc.check_position_numbers_production_list()

if not checked_element_ids:
    uc.print_error("No discrepancies in production list")
else:
    vc.set_active(checked_element_ids)
    uc.print_error("Active elements have discrepancies in the production list !")

```


## export part list 

```python 
import cadwork
import list_controller as lc
import utility_controller as uc
import visualization_controller as vc

element_ids = ec.get_active_identifiable_element_ids()
lc.export_part_list(element_ids, 'C:\\Downloads\\api_list.cwlm')

```

