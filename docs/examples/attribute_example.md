# attribute_controller

## Conditions 

```python
import  attribute_controller  as ac     # import module
import  element_controller    as ec   


# get active element_ids
element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    if ac.is_panel(element_id): # returns boolean
        print (True)
    else:
        print (False)
```

## set attributes
```python
import  attribute_controller  as ac     # import module
import  element_controller    as ec   

element_ids = ec.get_active_identifiable_element_ids()

ac.set_user_attribute_name(11, "ExampleAttribute")
ac.set_user_attribute(element_ids, 11, "Hello World!")
```

## get attributes
```python
import  attribute_controller  as ac     # import module
import  element_controller    as ec   


# get active element_ids
element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    user_attr = ac.get_user_attribute(element_id, 20) # 20 = attribute number
    user_attr_name = ac.get_user_attribute_name(20)
    element_guid = ec.get_element_cadwork_guid(element_id)
    
    print(user_a_name, 
          user_a,
          element_guid
          )
```


## assign attributes to beam
```python 
import  cadwork                                 # import module
import  attribute_controller  as ac
import  element_controller    as ec

point      = cadwork.point_3d(100, 200, 300)         # create a cadwork Point   
vector_x   = cadwork.point_3d(1., 0., 0.)            # x vector length direction
vector_z   = cadwork.point_3d(0., 0., 1.)            # z vecotr height orientation 
width      = 200.                                    # width/heigth of beam section
length     = 2600.                                   # beam length
name       = 'My first beam :)'                      # name as a string

beam            = ec.create_square_beam_vectors(width, length, 
                                                point, vector_x,
                                                vector_z) # returns element_id

add_beam_name   = ac.set_name([beam], name) # input beam id (list), name (string)

```

<noscript>
    <img src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/pixel.gif">
</noscript>
<script defer src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/script.js"></script>