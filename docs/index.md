---
hide:
  - toc
---

# Cadwork Python Documentation

In front of you, you see the first version of the Cadwork Python Guide.
This document is written in cooperation of the Cadwork branches.
Since version 27 Cadwork offers an API connection to the script language Python.
By scripting in Cadwork with Python you can automate and customize your operations.

The API provides a multitude of basic functions of Cadwork 3D.
On the basis of the API external programs can be written, with which it is possible to e.g. create and manipulate parts.

List calculations, list outputs, various import and export functions and much more is available via the API.
This allows the implementation of customer specific functions without changing the program code of Cadwork.
By using the API, a wide range of helpers for various areas can be created and directly integrated into Cadwork 3D.
Cadwork itself delivers some of these small helpers by default.
But also the development of small and large helpers by you as a user is possible.

The Python Guide should enable you to start scripting in Cadwork 3D.
We hope we can convince you of the great potential with Python in Cadwork.

## Discussions

[GitHub Discussion - Ask and answer questions from the Community](https://github.com/cwapi3d/cwapi3dpython/discussions){target=_blank}

## Introduction

### What Is an API?

An application programming interface (API) is a connection between computers or between computer programs.
It is a type of software interface, offering a service to other pieces of software.
A document or standard that describes how to build such a connection or interface is called an API specification.
A computer system that meets this standard is said to implement or expose an API.
The term API may refer either to the specification or to the implementation.

<figure markdown="1">
![Cadwork API](img/python.png){ width="500" }
</figure>

### Why Python?

* Python is easy to learn. Its syntax is easy and code is very readable.
* Python has a lot of applications. It's used for developing web applications, data science, rapid application development, and so on.
* Python allows you to write programs in fewer lines of code than most of the programming languages.
* The popularity of Python is growing rapidly. Now it's one of the most popular programming languages.

### What Is Python?

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.
Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

Often, programmers fall in love with Python because of the increased productivity it provides.
Since there is no compilation step, the edit-test-debug cycle is incredibly fast.
Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault.
Instead, when the interpreter discovers an error, it raises an exception.
When the program doesn't catch the exception, the interpreter prints a stack trace.
A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on.
The debugger is written in Python itself, testifying to Python's introspective power.
On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective.[^1]

[^1]: [Python](https://www.python.org/doc/essays/blurb/){target=_blank}

```python
print("Hello Cadwork! Let's get started!")
```

Python provides some built-in data types, in particular, [dict](https://docs.python.org/3/library/stdtypes.html#dict){target=_blank}, [list](https://docs.python.org/3/library/stdtypes.html#list){target=_blank}, [set and frozenset](https://docs.python.org/3/library/stdtypes.html#set){target=_blank}, and [tuple](https://docs.python.org/3/library/stdtypes.html#tuple){target=_blank}.
The [str](https://docs.python.org/3/library/stdtypes.html#str){target=_blank} class is used to hold Unicode strings, and the [bytes](https://docs.python.org/3/library/stdtypes.html#bytes){target=_blank} and [bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray){target=_blank} classes are used to hold binary data.[^2]

[^2]: [Data Types](https://docs.python.org/3/library/datatypes.html){target=_blank}

We recommend following a tutorial and coming back afterward if you are unfamiliar with Python. :woman_student:

* [The Python Tutorial](https://docs.python.org/3.4/tutorial/){target=_blank}
* [LearnPython](https://www.learnpython.org/){target=_blank}
* [RealPython](https://realpython.com/){target=_blank}
