**Debugging python script in cadwork**<br>
This section refers to calling the plugins from the Plugin Bar.
If you want to debug a script in cadwork, then you can enable the console in User Test in the user settings. When cadwork is restarted, the console opens. 
In the console you will see the screen output (print('hello world'), or errors. 

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