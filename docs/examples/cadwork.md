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

## add 3D points

```python 
import  cadwork                                 # import module

pt1 = cadwork.point_3d(100, 200, 300)

pt1 += cadwork.point_3d(800, 700, 600)

print(pt1)
```

<noscript>
    <img src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/pixel.gif">
</noscript>
<script defer src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/script.js"></script>