---
hide:
  - toc
---

# endtype_controller

## get endtype name at start point of the element

```python
import cadwork  # import module
import endtype_controller as etc
import element_controller as ec

element_ids = ec.get_active_identifiable_element_ids()
for element_id in element_ids:
    endtype_name = etc.get_endtype_name_start(element_id)
    print(endtype_name)
```


## get endtype name at start point of the element

```python
import cadwork  # import module
import endtype_controller as etc
import element_controller as ec
import utility_controller as uc

element_ids = ec.get_active_identifiable_element_ids()

new_endtype = uc.get_user_string('name of the new end-type')

i = 0
for element_id in element_ids:
    endtype_name = etc.get_endtype_name_start(element_id)
    if endtype_name == 'V_8':  # V_8 = name of an endtpye
        etc.set_endtype_name_start(element_id, new_endtype)
        i += 1
uc.print_error('Number of end-type replaced:%d' % i)
```

## create a tenon endtype and assign it to both ends

```python
import cadwork
import element_controller as ec
import endtype_controller as etc

endtype_id = etc.create_new_endtype('Tenon_80x40', cadwork.end_type.Tenon, 'Custom_Joints')

for element_id in ec.get_active_identifiable_element_ids():
    etc.set_endtype_id_start(element_id, endtype_id)
    etc.set_endtype_id_end(element_id, endtype_id)
```

## list existing tenons and lengthenings

```python
import endtype_controller as etc

for title, endtype_ids in (
    ('Tenons', etc.get_existing_tenon_ids()),
    ('Lengthenings', etc.get_existing_lengthening_ids()),
):
    print(title)
    for endtype_id in endtype_ids:
        print(f'  {endtype_id}: {etc.get_endtype_name(endtype_id)}')
```

## show endtypes at both ends

```python
import attribute_controller as ac
import element_controller as ec
import endtype_controller as etc

for element_id in ec.get_active_identifiable_element_ids():
    start = etc.get_endtype_name_start(element_id) or '-'
    end = etc.get_endtype_name_end(element_id) or '-'
    print(f'{ac.get_name(element_id)} ({element_id}): {start} | {end}')
```
