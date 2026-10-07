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

## material report

```python
import material_controller as mc

print(f'{"Name":30} {"Group":25} {"Weight":>10} {"Price":>10}')
for material_id in mc.get_all_materials():
    print(
        f'{mc.get_name(material_id):30} {mc.get_group(material_id):25} '
        f'{mc.get_weight(material_id):>10.1f} {mc.get_price(material_id):>10.2f}'
    )
```

## create a material with physical properties

```python
import material_controller as mc

material_id = mc.get_material_id('GL24h')
if not material_id:
    material_id = mc.create_material('GL24h')

mc.set_code(material_id, 'GL24h')
mc.set_weight(material_id, 420.0)
mc.set_thermal_conductivity(material_id, 0.13)
mc.set_price(material_id, 650.0)
```

## materials grouped by material group

```python
from collections import defaultdict

import material_controller as mc

materials_by_group = defaultdict(list)
for material_id in mc.get_all_materials():
    materials_by_group[mc.get_group(material_id)].append(mc.get_name(material_id))

for group in mc.get_all_material_groups():
    print(group)
    for name in sorted(materials_by_group.get(group, [])):
        print(f'  {name}')
```
