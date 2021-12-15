# cadwork

## create a cadwork point

In Python, a cadwork point_3d is represented as a 3D Point structure -> represented by the x, y and z coordinate values of the point. 
Find more information about points and vectors in tab geometry examples.

```python
import  cadwork                                 # import module

point = cadwork.point_3d(100, 200, 300)         # create a cadwork Point
```

## move a cadwork point 

```python 
import  cadwork                                 # import module

vector_x = cadwork.point_3d(1., 0., 0.)         # define vector
distance = 1500.0                               # moving distance

moved_point = point + (vector_x * distance)    
```

## distance between two 3D points

```python 
import  cadwork                                 # import module

point1 = cadwork.point_3d(100, 200, 300) 
point2 = cadwork.point_3d(300, 100, 200)                            

distance = point1.distance(point2)  
```