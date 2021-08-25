## Install CWAPI3D
```python
pip install cwapi3d
```
[Github - cwapi3d python](https://github.com/cwapi3d/cwapi3dpython){target=_blank}

## Module cadwork

### create a cadwork point

```python
import  cadwork                                 # import module

point = cadwork.point_3d(100, 200, 300)         # create a cadwork Point
```

### move a cadwork point 

```python 
import  cadwork                                 # import module

vector_x = cadwork.point_3d(1., 0., 0.)            # define vector
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

## Videos

<figure class="video_container">
  <iframe src="https://www.youtube.com/embed/hn3AtHPqEqE" frameborder="0" width="960" height="569"  allowfullscreen="true"> </iframe>
</figure>