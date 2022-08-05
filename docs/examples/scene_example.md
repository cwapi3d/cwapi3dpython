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
<noscript>
    <img src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/pixel.gif">
</noscript>
<script defer src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/script.js"></script>