---
hide:
  - toc
---

# material_controller
## get material ids and names 

```python 
import cadwork
import material_controller as mc

material_ids_by_name = {}
for material_id in mc.get_all_materials():
    mat_name = mc.get_name(material_id)
    material_ids_by_name[mat_name] = material_id

```

## create new material

```python 
import material_controller as mc
    
material_id = mc.create_material('Cross-Laminated-Timber')
# the new created material is stored in the category "No groups"

mc.set_group(material_id, 'Plattenwerkstoffe')
# the new created material is now shifted in the category "Plattenwerkstoffe"

```

