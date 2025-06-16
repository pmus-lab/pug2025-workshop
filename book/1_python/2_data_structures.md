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

# <i class="fa-brands fa-python"></i> Data Types and Strucutures

The Python programming language is a *general purpose* language, which means it is widely used in many fields, including statistics and neuroimaging. Python is a *high-level, interpreted* language, which means it offers a high level of abstraction and you usually do not need to worry about *low-level* things like memory management or variable types.

## Variables

As in other programming languages, variables are used to store data of different values or types (hence the name *variable*). In Python, you declare a variable by writing its name and then assigning its value with the equal (=) sign:

```{code-cell} ipython3
my_variable = 4
```

Notice that when we initialize a variable, we do not need to specify its *type* (e.g. it being an integer or a string), as Python is *dynamically typed*, which means it figures out your desired variable type by itself once you run the program. This means, you can also simply overwrite your previously created variable with for example a character string:

```{code-cell} ipython3
my_variable = "Hello World"
```

If you want to know what 's currently stored in your variable, you can use the `print()` function:

```{code-cell} ipython3
print(my_variable)
```

**Note:** If you are working in an interactive environment like the Jupyter notebooks which we will use in the exercises, you might not even need to write print as the last line of the code cell is automatically evaluated.


## Built-in types

All general-purpose languages provide the programmer with different *types* of variables as the basic building blocks of programs.

### Integers

Integers are the numbers zero (0), positive natural numbers (1, 2, 3, ...), or the negation of positive natural numbers (-1, -2, -3, ...)

```{code-cell} ipython3
subjects_group_1 = 10
subjects_group_2 = 20
measurements_total = 60
```

You can perform mathematical operations like addition

```{code-cell} ipython3
subjects_total = subjects_group_1 + subjects_group_2
print(subjects_total)
```

or division

```{code-cell} ipython3
measurements_per_subject = measurements_total / subjects_total
measurements_per_subject
```

*Note:* As already mentioned above, if we execute Python code in interactive notebooks (*.ipynb* files), the `print()` statement can be omitted if the variable to be printed is in the last line of the code block. We will use both options from time to time, as the automatic printing will perform some automatic formatting and sometimes one or the other will look nicer. However, please note that you will need to write the print statement explicitly if you work with normal Python (*.py*) scripts.

### Floating point numbers

Notice that while the previous addition of two integers resulted in another integer, the division resulted in a number with a decimal point. The latter is what we call a float (short for *floating point* number), which is a way computers represent real numbers.

All of the standard arithmetic operations that work on integers also work on floats (or on any combination of them):

```{code-cell} ipython3
roughly_pi = 3.14
radius = 2
circumference = 2 * roughly_pi * radius

print("The circumference of the cicle is", circumference)
```

### Strings

Strings are sequences of characters. In Python, we can define strings by enclosing zero or more characters in a pair of quotes. It does not matter whether you use single or double quotes and both work equally well as long as the opening and closing quotes match.

```{code-cell} ipython3
string1 = "Hello"
string2 = 'World'
```

There are many inbuilt functions you can use on strings, like figuring out their length:

```{code-cell} ipython3
len(string1)
```

Or converting them to lower case:

```{code-cell} ipython3
string1.lower()
```

One thing you might have noticed is that these examples seem to use two different syntaxes. In the first example, `len()` seems to be a function which takes a string as its parameter (or *argument*), while in the other examples the function comes after the string with a *dot* notation `.upper()`. If this is a bit confusing do not worry, we will talk about this difference a bit later.

Another useful thing about string is that you can use *formatted* strings (f-strings) to nicely format strings when printing results. For this you can just add an *f* before the opening quotation marks of the string and you can then print the value of any variable by enclosing it with curly brackets `{}` in the middle of your string:

```{code-cell} ipython3
num_neurons = 86
print(f"The human brain has {num_neurons} billion neurons.")
```

You can also do many more things like formatting the number of decimal points shown for a number. See for example the Python documentation for more information: https://docs.python.org/3/tutorial/inputoutput.html.


### Booleans

Handling Boolean values in Python is pretty much the same as in other programming languages. Boolean values can only take the value `True` (corresponding to 1) or `False` (corresonding to 0) and not other versions like `true` or `"False"`:

```{code-cell} ipython3
my_bool = True
my_bool
```

One of the ways Boolean values are typically generated in Python is through logical or comparison operations. For example, the statement "5 is larger than 3" can be answered in a binary way (it is either true or false):

```{code-cell} ipython3
5 > 3
```

Similarly, if we want to compare two numbers, this is also a logical operation that returns a Boolean value:

```{code-cell} ipython3
5 == 3
```

But what if the question you are trying to ask is not so simple? Python lets you built *conjunctions* of several subexpressions:

```{code-cell} ipython3
("shop" in "workshop") and (5 > 3) and (4 * 2 == 8)
```

In logical operations, *and* requires ALL statements to be true, wich is the case here. Alternatively, *or* requires only one of the statements to be true:

```{code-cell} ipython3
("shop" in "workshop") and (5 > 3) or (4 * 2 == 10)
```
This expression still returns `True` even though the last comparison is false due to it being joined with the previous expression through *or*.

*Note: The round brackets are not strictly necessary here, as Python will evaluate this expression left to right, following the logical and comparison operator precedence rules.*

### None

So what if you want to create a variable but not assign a specific value to it? This is where `None` comes in handy. *None* works similar as for example the *NaN* (not a number) value from MATLAB. However, please note that *None* and *False* are not the same thing!

```{code-cell} ipython3
None == False
```

```{admonition} Summary
:class: tip

The Python standard library includes the following data types:

- Integer values (1, 2, 3)
- Floating point values (1.0, 2.2)
- Charater strings ("Hello", "World")
- Boolean values (True, False)
- No value (None)
```
