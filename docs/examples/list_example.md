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
    uc.print_error('No discrepancies in production list')
else:
    vc.set_active(checked_element_ids)
    uc.print_error('Active elements have discrepancies in the production list !')
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

## renumber the production list silently

```python
import element_controller as ec
import list_controller as lc

element_ids = ec.get_all_identifiable_element_ids()

starting_number = 1
keep_existing_numbers = True
with_containers = False

lc.generate_new_production_list_silently(element_ids, starting_number, keep_existing_numbers, with_containers)
```

## export the production list with a settings file

```python
import element_controller as ec
import list_controller as lc
import utility_controller as uc

element_ids = ec.get_active_identifiable_element_ids()
settings_file = uc.get_user_file_from_dialog('*.xml')

lc.export_production_list_with_settings(element_ids, r'C:\Exports\production_list.xlsx', settings_file)
```

## check part list numbers

```python
import list_controller as lc
import utility_controller as uc
import visualization_controller as vc

conflicting_ids = lc.check_position_numbers_part_list()

if conflicting_ids:
    vc.set_active(conflicting_ids)
    vc.zoom_active_elements()
    uc.print_error(f'{len(conflicting_ids)} elements have part list discrepancies')
else:
    uc.print_error('Part list is consistent')
```
