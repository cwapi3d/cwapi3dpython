## Package cadwork

### create a cadwork point

```python
import  cadwork                                 # import package

point = cadwork.point_3d(100, 200, 300)         # create a cadwork Point
```

### move a cadwork point 

```python 
import  cadwork                                 # import package

vector_x = cadwork.point_3d(1, 0, 0)            # define vector
distance = 1500.0                               # moving distance

moved_point = point + (vector_x * distance)    
```

## Package element_controller

### create_node

```python 
import  cadwork                                 # import package
import  element_controller

point = cadwork.point_3d(100, 200, 300)         # create a cadwork Point   
node = element_controller.create_node(point)
```
### create_square_beam_vectors
```python 
import  cadwork                                 # import package
import  element_controller

point      = cadwork.point_3d(100, 200, 300)         # create a cadwork Point   
vector_x   = cadwork.point_3d(1., 0., 0.)            # x vector length direction
vector_z   = cadwork.point_3d(0., 0., 1.)            # z vecotr height orientation 
width      = 200.                                    # width/heigth of beam section
length     = 2600.                                   # beam length

beam       = element_controller.create_square_beam_vectors(width, length, point, vector_x, vector_z)
```
## Package attribute_controller
### assign attributes to beam
```python 
import  cadwork                                 # import package
import  element_controller
import  attribute_controller

point      = cadwork.point_3d(100, 200, 300)         # create a cadwork Point   
vector_x   = cadwork.point_3d(1., 0., 0.)            # x vector length direction
vector_z   = cadwork.point_3d(0., 0., 1.)            # z vecotr height orientation 
width      = 200.                                    # width/heigth of beam section
length     = 2600.                                   # beam length
name       = 'My first beam :)'                      # name as a string
colour     = 3                                       # colour number as an int

beam            = element_controller.create_square_beam_vectors(width, length, point,
                     vector_x, vector_z) # returns element_id

add_beam_name   = attribute_controller.set_name([beam], name) # input beam id (list), name (string)

```
## Package visualization_controller
### assign color to beam
```python 
import  cadwork                                 # import package
import  element_controller
import  visualization_controller

point      = cadwork.point_3d(100, 200, 300)         # create a cadwork Point   
vector_x   = cadwork.point_3d(1., 0., 0.)            # x vector length direction
vector_z   = cadwork.point_3d(0., 0., 1.)            # z vecotr height orientation 
width      = 200.                                    # width/heigth of beam section
length     = 2600.                                   # beam length
colour     = 3                                       # colour number as an int

beam            = element_controller.create_square_beam_vectors(width, length, point,
                     vector_x, vector_z) # returns element_id
add_beam_colour = visualization_controller.set_color([beam], colour) # input beam id (list), colour (int)
```
## Package geometry_controller
### get beam points and vetors

```python 
import  cadwork                                 # import package
import  element_controller
import  geometry_controller

# get active element_ids
element_ids = element_controller.get_active_identifiable_element_ids()

for element_id in element_ids:
    vector_x = geometry_controller.get_xl(element_id) # returns local vector
    vector_y = geometry_controller.get_yl(element_id) # returns local vector
    vector_z = geometry_controller.get_zl(element_id) # returns local vector
    get_p1   = geometry_controller.get_p1(element_id) # returns cartesian point
    get_p2   = geometry_controller.get_p2(element_id) # returns cartesian point
    get_p3   = geometry_controller.get_p3(element_id) # returns cartesian point

    print(f' the elements local vecotr z is: {vector_z} \n'
            f'the coordinates of the point_3 are {get_p3}')


```


## Videos

<figure class="video_container">
  <iframe src="https://www.youtube.com/embed/hn3AtHPqEqE" frameborder="0" width="960" height="569"  allowfullscreen="true"> </iframe>
</figure>