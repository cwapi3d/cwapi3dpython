---
hide:
  - toc
---

# scene_controller
## create and add elements to scene

```python
import element_controller as ec
import cadwork
import scene_controller as sc

element_ids = ec.get_active_identifiable_element_ids()
new_scene = sc.add_scene('NewScene')

if new_scene:
    sc.add_elements_to_scene('NewScene', element_ids)
    sc.activate_scene('NewScene')
```

## get elements from scene

```python
element_ids_scene = sc.get_elements_from_scene('NewScene')

element_subgroup_scene = []
for element_id in element_ids_scene:
    group = ac.get_group(element_id)
    element_subgroup_scene.append(group)


print(len(element_ids_scene))
print(set(element_subgroup_scene))
```

## one scene per subgroup

```python
from collections import defaultdict

import attribute_controller as ac
import element_controller as ec
import scene_controller as sc

elements_by_subgroup = defaultdict(list)
for element_id in ec.get_active_identifiable_element_ids():
    subgroup = ac.get_subgroup(element_id)
    if subgroup:
        elements_by_subgroup[subgroup].append(element_id)

for subgroup, element_ids in elements_by_subgroup.items():
    if not sc.is_scene_present(subgroup):
        sc.add_scene(subgroup)
    sc.add_elements_to_scene(subgroup, element_ids)
```

## remove elements from a scene and delete empty scenes

```python
import element_controller as ec
import scene_controller as sc

scene_name = 'NewScene'

if sc.is_scene_present(scene_name):
    sc.remove_elements_from_scene(scene_name, ec.get_active_identifiable_element_ids())

for name in sc.get_scene_list():
    if not sc.get_elements_from_scene(name):
        sc.delete_scene(name)
```

## group scenes under a colored tab

```python
import scene_controller as sc

level_scenes = [name for name in sc.get_scene_list() if name.startswith('Level_')]

if level_scenes:
    sc.group_scences_with_name(level_scenes, 'Levels')
    sc.set_group_tab_color('Levels', 70, 130, 180, 255)
```
