---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# <i class="fa-brands fa-python"></i> Functions and Objects

In the previous sessions you learned about basic variables and data types. Now, we will build on that by discussing more building blocks like flow control and functions. We will also dive into some more detailed features of Python and learn about objects and classes.


## Everything is an Object

So far, and analogous to many other programming languages, you might think of data types like strings or integers as *primitive* data types, which means that they are built into the core of the language to behave in special ways and to not be changed or modified in any way. And this is true in many
other programming languages like C++. where you will have to explicitly tell the program what type of variable you want to create.

In Python this is a bit different and there aren't *really* any primitive datata types, as it is a deeply *object-oriented* programming language. In Python, *everything is an object*. Strings are objects, integers are objects, lists are objects, dictionairies are objects, and so fourth. We will come back to that concept in detail later today, but for now let us just focus on some practical implications this will bring.


### The dot notation

Let's start with the dot (.) notation. As you probably already noticed, we previously worked with our variables in two different ways. First, there is a functional syntax, where we pass an object (e.g. a list) as an argument to a function:

```{code-cell} ipython3
len([4,3,2,1])
```

A function is a specific, reusable piece of code, that performs a specific action. In this case, the `len()` function calculates the length of the list given to it as an argument. It then returns some kind of result, which we can print or save as a new variable. Second, there is the object-oriented syntax which you previously saw when working with strings:

```{code-cell} ipython3
text = "Hello World"
text.lower()
```

If you have previously only worked with data-centric languages like MATLAB you might find this a bit confusing. But don't worry, it essentially means that we simply call a function attached to the object (in this case the string). Such object specfic functions are called *methods*, so if you use `text.lower()` it will simply call the `.lower()` method of the string object. The dot operator expresses a relationship of belonging, so you can intuitively read `text.lower()` as "on the text variable, use the .lower() method which belongs to it".


### Inspecting objects

One implication of everything being an object in Python is that we might need to find out what kind of data an object contains and which methods it implements, as this might not always be obvious from just looking at the variable itself. We will not go into too much detail, but briefly introduce some simple ways for you to interrogate objects.

First, you can always see the type of an object by using the built-in `type()` function:

```{code-cell} ipython3
my_list = [1, 2, 3]
type(my_list)
```

Second, the `dir()` function will show you all methods implemented by an object as well as their *static attributes*, which are variables stored whithin the object (they often start and end with two underscores).

```{code-cell} ipython3
dir(my_list)
```

Here you can see, that the list object implements 11 different methods starting with `append`. All of these attributes and methods are available to you to access through the dot notation (e.g. `my_list.__class__` or `my_list.append()`).

```{code-cell} ipython3
my_list.__class__
```

```{code-cell} ipython3
my_list.append(4)
my_list
```

```{admonition} Summary
:class: tip

Everything in Python is an object!

- Functions like `len()` are standalone blocks of code that can be called independently of objects.
- Methods like `.lower()` are functions that belong to objects.
- You can inspect the type and content of objects with the `type()` and `dir()` functions.
```


## Namespaces and imports

Python is a high-level, dynamic programming language often associated with flexibility (for example, you do  not need to explicitly declare the type of your variables), but there are other cases in which Python is very strict (for example when it comes to the whitespace). Another strict thing about Python is that it takes *namespaces* very seriously.

If you require any additional functions, you will need to *import* it from whatever module it is in via the `import` statement. While this might seem strange at first, you will see that it significantly improves readability. As an example, you might want to use the square root for some kind of calculations. The corresponding function would be `sqrt()` in the `math` module:

```{code-cell} ipython3
import math

result = math.sqrt(9)
print(f"The square root of 9 is {result}")
```

The previous code cell imports the entire math module, which means you will also have access to all its other functions (e.g. the sine function `math.sin()`). You can also import specific functions:

```{code-cell} ipython3
from math import sqrt

sqrt(9)
```

or you can rename them:

```{code-cell} ipython3
import numpy as np

np.sqrt(9)
```

In the previous examples, we use the square root function from two different packages. First, directly from the math library so we can omit the `math.` prefix in the following code. Second, from the numpy library which we call `np` (so we don't have to write numpy all the time).

Sometimes it might also be the case that a module has submodules. For example, if we want to use `numpy` to generate a random integer number between 1 and 10, we can use the `randint()` function which is located in its `random` submodule. As you usually use many functions from the `numpy` package, you will see that people usually import the `numpy` module once at the top of the script and then use it as follows:

```{code-cell} ipython3
import numpy as np
random_integer = np.random.randint(1,10)
```

However, it would still work to just import the individual function:

```{code-cell} ipython3
from numpy.random import randint
random_integer = randint(1,10)
```

```{admonition} Note
:class: caution

While the dot notation is primarily used to access methods (functions belonging to an object), it is also used when working with modules and submodules to indicate relationships. When you import a module like `math` or `numpy`, the dot notation allows you to access the functions or submodules within it (e.g., `np.random.randint`). This consistent use of the dot notation across Python helps denote a hierarchy or belonging—whether for object methods or module functions/submodules.
```


## Functions

Functions are essential in programming as they allow you to encapsulate and reuse code efficiently. By breaking down complex problems into smaller, manageable parts, functions enhance code organization and readability. As we already saw you can use built-in functions or import them from specialized modules. Quite often it is also useful for you to *define* your own functions. In Python, this can be done by using the `def` keyword followed by a function name:

```{code-cell} ipython3
def my_function():
  print("I'm a custom function!")

my_function() # use the function
```

### Function arguments and returns

Functions can accept *arguments* (or parameters) that provide inputs or modify their behaviour. For example, if we want to add two numbers, we can pass both of them as arguments and further *return* the result to the user:

```{code-cell} ipython3
def add(a, b):
  return a + b

add(1, 2)
```

Python functions can have two different kinds of arguments: *positional* arguments, and *keyword* arguments. Positional arguments on the one hand are defined by their position whithin the round brackets and *must* be provided for the function to run without giving an error. In the previous example, both `a` and `b` are positional arguments and the function would not know what to do if any of them would be missing. Keyword arguments on the other hand are assigned a *default* value. This means that the function knows what to do even if the user does not explicitly provide a value for that argument. 

As an example, let's create a function that adds random gaussian noise to a given input `x`:

```{code-cell} ipython3
import random

def add_noise(x, mu=0, sd=1):
  """Adds gaussian noise to the input.

  Parameters
  ----------
  x : number
    The number to add noise to.
  mu : float, optional
    The mean of the gaussian noise distribution.
    Default: 0
  sd : float, optional
    The standard deviation of the noise distribution.
    Default: 1

  Returns
  -------
  float
  """

  noise = random.normalvariate(mu, sd)
  return x + noise
```

*Note:* So far, you have mostly seen comments within the code using the `#` sign. Another way to provide comments is by using triple double quotes `"""comment"""`, as shown in the previous code snippet. This approach is useful for providing larger portions of text, such as when documenting your functions. This is also the official way of documenting functions and classes in Python, so it is recommended to follow this convention.

If we now call this function by just providing a value for `x`it will still work as expected by using a mean of 0 and a standard deviation of 1 to calculate and add the noise.

```{code-cell} ipython3
add_noise(5)
```

If you decide you need different noise with a standard deviation of 5, you can simply add this new value. As positional arguments are optional, their order does not matter. You can provide any keyword argument in any order you like, as long as you provide its name and all positional arguments have been correctly provided before.

```{code-cell} ipython3
add_noise(5, sd=3)
```

You can also specify all arguments (including the positional one) by name (in this case the order of `sd` and `mu` doesnt matter)

```{code-cell} ipython3
add_noise(x=5, sd=3, mu=2)
```

or not use any name at all

```{code-cell} ipython3
add_noise(5, 3, 2)
```

However, the last example is differnet compared to the the previous one! This is because if no keywords are provided, Python will only be able to rely on the default order of arguments, which would result in the arguments being interpreted as `x=5`, `mu=2` and `sd=3` as defined in the function.

### Argument unpacking

Another feature of Python is the ability to provide a function with an unspecified number of arguments by using `*args` and `**kwargs`. While we will not cover this topic here, I want to mention it for completeness. If you are interested or encounter it in practice, feel free to explore this topic on your own (e.g., [here](https://book.pythontips.com/en/latest/args_and_kwargs.html)).


## Classes

As previously mentioned, [everything in Python is an object](1_Everything_is_an_object). The key cocept behind this is the object-oriented programming (OOP) paradigm central to many programming languages. You will get a brief introduction into these concepts in this chapter, however, do not worry if you feel like these concepts do not immediately make sense to you. Learning a programming language is like learning a real language and takes time. I am however convinced that once the semester goes on many of these newly introduced concepts will already start to click as you work your way through the exercises.

### So what is a class?

A class is, in a sense, a kind of template for an object. You can think of it as a set of rules and instructions what an object of a given kind can do. Let us start with the simplest example of a class and built on top of that.

```{code-cell} ipython3
class Circle:
  pass
```

These two lines of code already define a perfectly valid class called `Circle` (note that it starts with a capital C, which is a naming convention for classes). The `pass` statement is used as a placeholder to tell the Python interpreter that it should not expect any more code to follow for the class.

### Creating instances

So what can we do with the Circle class? It doesn't particularly look useful, does it? However, we can already do the most important thing we can do with a class, we can create a new *instance* of said class, which is to say we create objects whose behavior is defined by the `Circle` class. You can kind of imagine this as drawing different circles on a piece of paper. All of them are circles, but none of them would be the actual definition of a circle.

The syntax for creating an instance in Python is simple:

```{code-cell} ipython3
my_circle = Circle()
```

The `my_circle` variable contains an object, which is a specific instance of the `Circle` class. As of now, this object does neither contain any important information nor can it do anything.

### Making it do things

Let's start by providing some features to the `Circle` class:

```{code-cell} ipython3
from math import pi

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return pi * self.radius**2
```

We now defined two *methods* (functions whithin a class). First, there is the `__init()__` method, which might look fairly strange to you. This is a so called *magic method*, which is the basic initialization that is used every time we create an instance of our class. The `__init()__` method has two arguments. The first parameter is called `self`. It is a mandatory argument for any method whithin a class to take a reference to the current instance (*itself* so to say). The second argument `radius` then the first actual argument which has to be provided if a circle object is created. Whithin the `__init()__` method, this argument is assigned to a variable called `self.radius` which makes it an *attribute* of the class instance.

The `area()` method simply defines a way of calculating the area of the circle. As a method of the class it has access to all class attributes (variables starting with `self.`) and thus does not need any additional parameters other than the mandatory `self`.

We can then use this newly updated Circle class as follows:

```{code-cell} ipython3
my_circle = Circle(4)
my_circle.area()
```

The first line creates an object of the Circle class with radius 4. We can then use the `.area()` method of that object to calculate its area. Pretty cool, huh? If we change the radius of the given circle, then the area will change as well:

```{code-cell} ipython3
my_circle.radius = 9
my_circle.area()
```
