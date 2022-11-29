---
hide:
  - toc
---

**Debugging python script in cadwork**<br>
This section refers to calling the plugins from the Plugin Bar.
If you want to debug a script in cadwork, then you can enable the console in User Test in the user settings. When cadwork is restarted, the console opens.
In the console you will see the screen output, or errors.

User Test -> Userprofile -> Test Options... -> Console

![GIF](img/console.gif){: style="width:900px"}

## Console

Bugs present in the script can be detected in the console.

Any print statements are also visible in the console.

```python
print("hello world")
```

Print output in console:

![Screenshot](img/hello.png){: style="width:300px"}

Displayed Bug in console:

![Screenshot](img/console_cw.png){: style="width:800px"}

or use the debugger from Python IDLE.

![Screenshot](img/debug.jpg)

# Pycharm Professional

## Remote debugging with the Python remote debug server configuration

[Pycharm debug server configuration :bulb:](https://www.jetbrains.com/help/pycharm/remote-debugging-with-product.html#remote-debug-config)

- Install the pydevd-pycharm package on the remote machine by running the following command:

  pip install pydevd-pycharm~=<version of PyCharm on the local machine>

  for example, pip install pydevd-pycharm~=191.3490)

- Modify the source code file as follows:

```python

import math
#==============this code added==================================================================:
import pydevd_pycharm

pydevd_pycharm.settrace('172.20.208.95', port=12345, stdoutToServer=True,
                        stderrToServer=True)
#================================================================================================
class Solver:

    def demo(self, a, b, c):
        d = b ** 2 - 4 * a * c
        if d > 0:
            disc = math.sqrt(d)
            root1 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)
            return root1, root2
        elif d == 0:
            return -b / (2 * a)
        else:
            return "This equation has no roots"

if __name__ == '__main__':
    solver = Solver()

while True:
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    result = solver.demo(a, b, c)
    print(result)


```

<noscript>
    <img src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/pixel.gif">
</noscript>
<script defer src="https://analytics.cadwork.ca/ingress/e6b1702b-6224-4e93-94b7-9e4c2cd7ae06/script.js"></script>
