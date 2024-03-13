---
hide:
  - toc
---

# shop_drawing_controller
## export 2d wireframe drawing from current view

```python 
import cadwork
import shop_drawing_controller as sdc

clipboard_number = 3
with_layout = False # boolean to export with or without layout

sdc.export_2d_wireframe_with_clipboard(clipboard_number, with_layout)

```

## export 2d wireframe drawing from current view

```python 
import attribute_controller as ac
import cadwork
import geometry_controller as gc
import element_controller as ec
import shop_drawing_controller as sdc

element_id = ec.get_user_element_ids()
if len(element_id) != 1:
    uc.print_error('Please select just one wall element')
    exit()
if not ac.is_wall(*element_id):
    uc.print_error('Please select a wall element')
    exit()
    
position_vector = gc.get_p1(*element_id)
position_vector += (gc.get_xl(*element_id) * 500.)


sdc.add_wall_section_vertical(*element_id, position_vector)

```
![Backup Text](../img/section.png "Example Menu"){: style="width:600px"}

