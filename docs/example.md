## Install CWAPI3D
```python
pip install cwapi3d
```
[Github - cwapi3d python](https://github.com/cwapi3d/cwapi3dpython){target=_blank}

## Module cadwork

### create a cadwork point

In Python, a cadwork point_3d is represented as a 3D Point structure -> represented by the x, y and z coordinate values of the point. 

```python
import  cadwork                                 # import module

point = cadwork.point_3d(100, 200, 300)         # create a cadwork Point
```

A cadwork point_3d list can be accessed like a simple python list.

```python hl_lines="5 6 7"
import  cadwork                                 # import module

point = cadwork.point_3d(100, 200, 300)         # create a cadwork Point

print(point[0])                                 # prints x coordinate
print(point[1])                                 # prints y coordinate
print(point[2])                                 # prints z coordinate
```

The coordinates of a cadwork point_3d can also be accessed by its .x, .y and .z attributes.

```python hl_lines="5 6 7"
import  cadwork                                 # import module

point = cadwork.point_3d(100, 200, 300)         # create a cadwork Point

print(point.x)                                 # prints x coordinate
print(point.y)                                 # prints y coordinate
print(point.z)                                 # prints z coordinate
```

### move a cadwork point 

```python 
import  cadwork                                 # import module

vector_x = cadwork.point_3d(1., 0., 0.)         # define vector
distance = 1500.0                               # moving distance

moved_point = point + (vector_x * distance)    
```

## Module element_controller

### create_node

```python 
import  cadwork                                 # import module
import  element_controller as ec

point = cadwork.point_3d(100, 200, 300)         # create a cadwork Point   
node = ec.create_node(point)
```
### create_square_beam_vectors
```python 
import  cadwork                                 # import module
import  element_controller  as ec

point      = cadwork.point_3d(100, 200, 300)         # create a cadwork Point   
vector_x   = cadwork.point_3d(1., 0., 0.)            # x vector length direction
vector_z   = cadwork.point_3d(0., 0., 1.)            # z vecotr height orientation 
width      = 200.                                    # width/heigth of beam section
length     = 2600.                                   # beam length

beam       = ec.create_square_beam_vectors(width, length, point, vector_x, vector_z)
```
## Module attribute_controller
### assign attributes to beam
```python 
import  cadwork                                 # import module
import  element_controller    as ec
import  attribute_controller  as ac

point      = cadwork.point_3d(100, 200, 300)         # create a cadwork Point   
vector_x   = cadwork.point_3d(1., 0., 0.)            # x vector length direction
vector_z   = cadwork.point_3d(0., 0., 1.)            # z vecotr height orientation 
width      = 200.                                    # width/heigth of beam section
length     = 2600.                                   # beam length
name       = 'My first beam :)'                      # name as a string
colour     = 3                                       # colour number as an int

beam            = ec.create_square_beam_vectors(width, length, point,
                     vector_x, vector_z) # returns element_id

add_beam_name   = ac.set_name([beam], name) # input beam id (list), name (string)

```
### Conditions 

```python
import  element_controller    as ec   # import module
import  attribute_controller  as ac

# get active element_ids
element_ids = ec.get_active_identifiable_element_ids()

for element in element_ids:
    if ac.is_panel(element): # returns boolean
        print (True)
    else:
        print (False)
```
## Module visualization_controller
### assign color to beam
```python 
import  cadwork                                 # import module
import  element_controller        as ec
import  visualization_controller  as vc

point      = cadwork.point_3d(100, 200, 300)         # create a cadwork Point   
vector_x   = cadwork.point_3d(1., 0., 0.)            # x vector length direction
vector_z   = cadwork.point_3d(0., 0., 1.)            # z vecotr height orientation 
width      = 200.                                    # width/heigth of beam section
length     = 2600.                                   # beam length
colour     = 3                                       # colour number as an int

beam            = ec.create_square_beam_vectors(width, length, point,
                     vector_x, vector_z) # returns element_id
add_beam_colour = vc.set_color([beam], colour) # input beam id (list), colour (int)
```
## Module geometry_controller
### get beam points and vetors

```python 
import  cadwork                                 # import module
import  element_controller    as ec
import  geometry_controller   as gc

# get active element_ids
element_ids = ec.get_active_identifiable_element_ids()

for element_id in element_ids:
    vector_x = gc.get_xl(element_id) # returns local vector
    vector_y = gc.get_yl(element_id) # returns local vector
    vector_z = gc.get_zl(element_id) # returns local vector
    get_p1   = gc.get_p1(element_id) # returns cartesian point
    get_p2   = gc.get_p2(element_id) # returns cartesian point
    get_p3   = gc.get_p3(element_id) # returns cartesian point

    print(f' the elements local vecotr z is: {vector_z} \n'
            f'the coordinates of the point_3 are {get_p3}')


```

## tkinter - GUI toolkit

### A Simple Hello World Program

```python
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello cadwork World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="blue",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
```

### Button

```python
import tkinter as tk

class MyApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.ok = tk.Button(self)
        self.ok["text"] = "cadwork"
        self.ok["command"] = self.handler
        self.ok.pack()
        
    def handler(self):
        print("Button clicked")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300")
    app = MyApp(root)
    app.mainloop()
``` 

## Create a frame (construction)

![Backup Text](img/framed_slab.png "cadwork framed slab"){: style="width:700px"}

```python
"""framedSlab.py: create a simple framed slab in cadwork...."""

# import modules
import      cadwork
import      attribute_controller       as ac
import      element_controller         as ec
import      geometry_controller        as gc
import      utility_controller         as uc
import      visualization_controller   as vc


WIDTH           = 60.           # beam width
HEIGHT          = 240.          # beam height
ORIGIN          = 0., 0., 0.    # start/origin point
DIVISION        = 5             # number of divsion -> distribution (beam distribution)
BEAM_LENGTH     = 3600.         # length (beam)
MEMBER_LENGTH   = 5000.         # length (member)


def main():
    """ main function that creates a simple framed slab"""
    
    global ORIGIN
    global BEAM_LENGTH
    global MEMBER_LENGTH
    global WIDTH
    
    beam_length = BEAM_LENGTH # uc.get_user_double('Input beam length')
    
    # create start beam of frame
    beam_1 = create_beam(beam_length, 
                        cadwork.point_3d(*ORIGIN), 
                        cadwork.point_3d(0., 1., 0.), 
                        cadwork.point_3d(0., 0., 1.), 
                        'beam')
    
    # get vectors (beam_1)
    x_dir_beam, y_dir_beam, z_dir_beam = get_beam_vectors(beam_1)
    
    # move cadwork point -> start point for beam_2 (Kopfholz)
    start_point_beam_2 = cadwork.point_3d(*ORIGIN) + y_dir_beam * (MEMBER_LENGTH + WIDTH)
    
    # create end beam of frame
    beam_2 = create_beam(beam_length, 
                        start_point_beam_2, 
                        cadwork.point_3d(0., 1., 0.), 
                        cadwork.point_3d(0., 0., 1.), 
                        'beam')
    
    # move cadwork point -> start point for members
    start_point_member = cadwork.point_3d(*ORIGIN) + y_dir_beam * .5 * WIDTH \
                        + cadwork.point_3d(*ORIGIN) + x_dir_beam * .5 * WIDTH
    
    global DIVISION
    # calculate division distance
    spacing = beam_spacing(beam_1, DIVISION)
    
    members = []
    # while loop to create members -> increase spacing division
    n = 0.
    while n <= beam_length:
        member = create_beam(MEMBER_LENGTH, 
                            start_point_member + 
                            x_dir_beam * n, y_dir_beam, 
                            z_dir_beam)
        members.append(member)
        n += spacing
    
    # assign subgroup name to created elements 
    subgroup_name = ac.set_subgroup([beam_1, beam_2, *members], 'frame')
        
    return

#---------------------------------------------------------------

def create_beam(length, p1, x_dir, z_dir, name='member', color=3):
    """Creates a rectangular member with attributes: name, color

    Parameters
    ----------
    length : int
        beam length
    p1 : point_3d
        start point x, y, z
    x_dir : point_3d
        local x-vector x, y, z e.g. -> cadwork.point_3d(0., 1., 0.)
    z_dir : point_3d
        local z-vector x, y, z e.g. -> cadwork.point_3d(1., 0., 0.)
    name : str, optional
        set a name -> default = beam

    Returns
    -------
    int
        returns cadwork element ID
    """
    global WIDTH
    global HEIGHT
    beam = ec.create_rectangular_beam_vectors(WIDTH, HEIGHT, 
                                              length, 
                                              p1, 
                                              x_dir, 
                                              z_dir)
    ac.set_name([beam], name)
    vc.set_color([beam], color)
    
    return beam


def get_beam_vectors(element_id):
    """Returns vectors (x,y,z) 

    Parameters
    ----------
    element_id : int
        cadwork element id
        
    Returns
    -------
    point_3d
        returns cadwork point_3d / vectors
    """
    x_dir_sill = gc.get_xl(element_id)
    y_dir_sill = gc.get_yl(element_id)
    z_dir_sill = gc.get_zl(element_id)
    
    return x_dir_sill, y_dir_sill, z_dir_sill


def beam_spacing(beam, subdivisions):
    """Calculates the beam/member spacing

    Parameters
    ----------
    element_id : int
        cadwork element id
    
    subdivisions: int
        number of divisions
        
    Returns
    -------
    float
        returns divison length
    """
    global WIDTH
    beam_length = gc.get_length(beam)
    distance = (beam_length - WIDTH) / subdivisions
    
    return distance
    
    
#---------------------------------------------------------------

if __name__ == '__main__':
    main()
    

```

## Videos

<figure class="video_container">
  <iframe src="https://www.youtube.com/embed/hn3AtHPqEqE" frameborder="0" width="960" height="569"  allowfullscreen="true"> </iframe>
</figure>