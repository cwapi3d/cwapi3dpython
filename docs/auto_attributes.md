---
hide:
  - toc
---

# Auto Attributes

## Script filled attributes
Each component in cadwork is described geometrically and with regard to its position in the 
entire construction project. On the other hand there is an almost unlimited number 
of further attributes is available. Some of these attributes like color, material, name, 
building (building) and storey (storey) have to be set during the generation of the component. 
during the generation of the component. Others are optionally available to the user. Each of these 
attributes are explicitly defined by the user by setting them via Modify.
Attributes are used to fully describe the part properties. 

Furthermore, they are used for the creation of a suitable structure of the construction project 
and for the transfer of specific information to downstream systems such as an 
such as an ERP system.

Often, the content of an attribute is dependent on the content of other attributes or even 
geometric information. In this case, it is tedious to define the content manually. 
manually. For this reason cadwork provides in version 29 attributes which can 
which calculate their content independently with the help of a script at runtime. 
These are the so-called script-filled attributes. As script language Python 
is used. The Python script has access to various properties of the parts via the cadwork API. 
of the parts. These can be evaluated in the script and the content of the attribute 
can be calculated.

In contrast to all previous attributes, the content of a script-filled 
attribute is not defined manually by the user. The task of the user is to create a 
Python script, which on the basis of other element properties (geometry and attributes) to calculate the content of the script-filled attribute. The 
calculated content is displayed as for all other attributes (Modify, 
info window, plan outputs), can be used for activating/deactivating as well as showing/hiding 
can be used for activating/deactivating and hiding, can be used as a comparison and sorting criterion for the 
list calculation and is exported to the different lists. 
The only difference to the known attributes is the automated generation of the 
content via a Python script.

## Creation of script-filled attributes
These attributes are created similar to the user-defined attributes in the Attributes dialog
(User profile -> Wood... -> Attributes) in the new Script Filled -> Configuration tab.

<figure markdown="1">
![Backup Text](img/auto.jpg "script-filled attributes"){: style="width:700px"}
</figure>

A created script-filled attribute is available for each element type in cadwork. In the tab "Type 
script populated" the evaluation of the script can be limited to single element types. Tjis can be useful if, for example 
different evaluations are required for plates and beams. If the evaluation is intended only for elements of the type beam, the content of this 
attribute remains empty for all other element types. If the element type is subsequently changed, a recalculation of the attributes is triggered.

## execution status
The execution status of the scripts can be controlled.
The icon for configuring the script-filled attributes is visualized in the Windows menu bar to the left of the message center icon. This display hides a button that can be used to subsequently change the selected status. 

<figure markdown="1">
![Backup Text](img/auto_button.jpg "script-filled attributes settings"){: style="width:700px"}
</figure>

## available functions
The available functions are marked in the documentation with an info description. 

## example code

### group and length

In this example, the group as well as the component length is concatenated. The length is rounded to 4 decimal digits.

```python title="group_length.py"
import cadwork
import attribute_controller
import geometry_controller

element_ids = cadwork.get_auto_attribute_elements()#gets the specified element

for element_id in element_ids:
    length = geometry_controller.get_length(element_id)
    group = attribute_controller.get_group(element_id)
    result = ' Group:' + group + 'Length:' + str(length)
    cadwork.set_auto_attribute([element_id], result)#sets the attribute
```

### dimension check

This script checks whether the cross-sections are standard dimensions or not.

```python title="dimension_check.py"
import cadwork
import element_controller as ec
import attribute_controller as ac
import geometry_controller as gc

element_ids = cadwork.get_auto_attribute_elements()

for element_id in element_ids:
    height = round(gc.get_height(element_id),3)
    width = round(gc.get_width(element_id),3)
    if height % 20 == 0 and width % 20 == 0:
        cadwork.set_auto_attribute([element_id], 'Standard cross-section')
    else:
        cadwork.set_auto_attribute([element_id], 'Special cross-section')
```

### concatenate attributes and round dimension

In this example, the attributes name and material are concatenated with the geometric properties width and height. 
The width and height are rounded to the nearest 10.

```python title="attributes_dimension.py"
import cadwork
import element_controller as ec
import attribute_controller as ac
import geometry_controller as gc


element_ids = cadwork.get_auto_attribute_elements()

for element_id in element_ids:
    name = ac.get_name(element_id)
    material = ac.get_element_material_name(element_id)
    width = round(gc.get_width(element_id), -1)
    height = round(gc.get_height(element_id), -1)

    cadwork.set_auto_attribute([element_id], f'{name};{material};{width};{height}')
```

### material and storey

Concatenation of the Building Storey with the material. 

```python title="material_storey.py"
import cadwork
import attribute_controller as ac
import bim_controller as bc

element_ids = cadwork.get_auto_attribute_elements()

for element_id in element_ids:
    storey = bc.get_storey(element_id)
    material = ac.get_element_material_name(element_id)

    cadwork.set_auto_attribute([element_id], f'{material} - {storey}')
```

