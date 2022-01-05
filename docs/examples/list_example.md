# list_controller
## check production list discrepancies

```python 
import cadwork
import list_controller as lc
import utility_controller as uc
import visualization_controller as vc


checked_element_ids = lc.check_position_numbers_production_list()

if not checked_element_ids:
    uc.print_error("No discrepancies in proudction list")
else:
    vc.set_active(checked_element_ids)
    uc.print_error("Acitve elements have dscrepancies in the production list !")

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

<noscript>
    <img src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/pixel.gif">
</noscript>
<script defer src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/script.js"></script>