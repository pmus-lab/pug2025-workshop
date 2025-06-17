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

# <i class="fa-brands fa-python"></i> Control Flow

Control flow allows you to dictate the order in which statements are executed, enabling your programs to make decisions and perform repetitive actions.


## Conditionals

Conditional statements (if-else statements) are essential for writing programs that can make decisions based on varying inputs and conditions. They help in implementing logic that responds differently depending on the circumstances.

### Conditionals as "if-then" decisions

Conditionals work like everyday decisions. Imagine you’re deciding what to wear based on the weather. You check if it’s raining, and if it is, you wear a raincoat. This is the essence of an `if` statement: it allows a program to choose an action based on whether a condition is true or false:

```{code-cell} ipython3
weather = "rainy"

if weather == "rainy":
    print("Take an umbrella!")
```

Here, we’re saying: *“If the weather is rainy, then take an umbrella.”* If it’s not rainy, this code does nothing, and no message is printed.

However, conditionals often need a backup plan if the initial condition isn’t met. Continuing the weather example, what if it’s not raining? You might want to say, *“If it’s not raining, wear sunglasses.”* This is where `else` comes in:

```{code-cell} ipython3
weather = "sunny"

if weather == "rainy":
    print("Take an umbrella!")
else:
    print("Wear sunglasses!")
```

 The `else` statement is what we call a *fallback* option, which means it will run only if none of the previous conditions are met. Both *elif* (which is short for *else if*) and *else* statements are optional; you could simply use *if* statements to handle every possible scenario. However, this can lead to worse code readability, especially if many decisions are possible. Now, regardless of the weather, you’re covered with either an umbrella or sunglasses.

Real decisions often involve more than two choices. Let’s say you want to decide what to wear based on three types of weather: rain, snow, or sun. You could use an `if` for the first option, `elif` (short for “else if”) for the second, and an `else` for anything else (so this is always your *fallback*, covering anything not included in your other statements):

```{code-cell} ipython3
weather = "snowy"

if weather == "rainy":
    print("Take an umbrella!")
elif weather == "snowy":
    print("Wear a warm coat!")
else:
    print("Wear sunglasses!")
```

### Decisions with multiple conditions

Sometimes, a decision depends on multiple factors. For example, if you’re deciding to go for a run, you might only go if the weather is sunny and you have enough time. This uses both conditions combined with `and`:

```{code-cell} ipython3
weather = "sunny"
time = "enough"

if weather == "sunny" and time == "enough":
    print("Go for a run!")
else:
    print("Maybe stay home.")
```

Now, both `weather == "sunny"` and `time == "enough"` must be true to go for a run. If either one is false, the code will suggest staying home.

There are times when you want to act if either of two conditions is true. For instance, if you’ll go out if it’s either sunny or warm, you can use `or` in the conditional:

```{code-cell} ipython3
weather = "cloudy"
temperature = "warm"

if weather == "sunny" or temperature == "warm":
    print("Let's go outside!")
else:
    print("Stay inside.")
```

Now, as long as it’s sunny or warm, you’ll go outside. If neither condition is true, you’ll stay inside.

```{admonition} Summary
:class: tip

- `if`: "If this condition is true, do something."
- `else`: "Otherwise, do something else."
- `elif`: "If the first condition isn’t true, check another condition."
- `and` / `or`: Combine multiple conditions for more complex decisions.
```


## Loops

Now, we will have a look at how we cann use looping operations to simplify repetition, allowing us to perform tasks across items or count through fixed numbers efficiently.

### Loops are repetition instructions

We can loop (or *iterate*) over elements in a collection. You can think about loops as a way of acting on each item one by one. In a `for` loop, we can read it as "for each item in a group". For example, if we want to read each page in a book, the following `for` loop acts means "for each page in the book, read it.":

```{code-cell} ipython3
pages = [1, 2, 3, 4, 5]

for page in pages:
    print(f"Reading page {page}")
```

Here, we loop over each item/element of the list starting from the first. In each iteration of the loop, we assign the value to a variable called `page` which is then printed. `page` is a temporary variable, which means it will only exist whithin the scope of the loop and not anymore after.


### Counting loops: Doing something a fixed number of times

One very common use case of loops is to perform a specific action a set number of times. In Python, we can use the built-in `range()` function to count for us, so we don’t have to write each number ourselves. It’s like setting a timer for an exercise, where you know you’ll do an activity for 10 seconds or repeat it 5 times.

```{code-cell} ipython3
for i in range(5):
    print(f"Jumping jack #{i}")
```

Here, `range(5)` tells the loop to repeat 5 times. The variable `i` is called an index variable. Remember, `range()` starts at the first number and stops just before the last number, making the final value exclusive:

```{code-cell} ipython3
for i in range(5,10):
    print(f"Jumping jack #{i}")
```

Note that, as with the `len()` function, the end point of the `range()` function is exclusive, meaning it will create a sequence of numbers from 0 to 3. You can further also provide only a single number (like the length of a list) and use the numbers created by range as *indices* to index another variable:

```{code-cell} ipython3
my_list = ["apple", "banana", 3, 4]
list_length = len(my_list)

for i in range(list_length):
  print(my_list[i])
```

```{admonition} Question
:class: hint

Do you remember the differences between a tuple and a list? Why do you think does the `range()` function return a tuple instead of a list?
```

#### Using enumerate()

You have previously seen two ways of looping over a list. Either by indexing the items directly, or through indexing by usinge the `range(len())` expression. Python also provides a nice way of combining these two through the `enumerate()` function:

```{code-cell} ipython3
for index, value in enumerate(my_list):
    print(f"Index {index} contains: {value}")
```

In cases where you need to keep track of the index, this approach is often preferred because it avoids manual indexing, making the code cleaner and less prone to errors.

### While loops: "Keep going until..."

`While` loops are like a task that repeats until a certain condition is met. For example, think of heating water in a kettle. You’ll keep heating the water until it reaches boiling point. In code, this looks like a `while` loop, which keeps running until a specified condition is no longer true.


```{code-cell} ipython3
temperature = 20  # starting temperature
while temperature < 100:
    print(f"Heating... temperature is {temperature}°C")
    temperature += 10  # increase temperature
print("Water is boiling!")
```

In this example, the loop keeps increasing the temperature until it reaches 100°C. Then, it stops. 

Be careful with `while` loops because if the condition never becomes `False`, the loop will run indefinitely, leading to an infinite loop.


### Using counters

Sometimes it can be useful to keep track to things happening in a loop. A concept you will see often is the use of counters:

```{code-cell} ipython3
counter = 0
while counter < 5:
    print(f"Counter is {counter}")
    counter += 1
```

Here, `counter` is a counting variable which is initialized and set to `0` before the loop. It then keep strack of something within a loop (in this case it makes sure the) and, importantly, lets you access this result later on in your script.

### Nested statements

In more complex analyses, you often need to nest multiple statements inside one another. If you for example want to iterate over an entire list and perform an action only for specific items of the list you could to this as follows:

```{code-cell} ipython3
my_list = ["apple", "banana", 3, 4]

for item in my_list:
  if item == "banana":
    print("Banana!")
  else:
    print("Not a banana.")
```

### Whitespace is syntactically required

One important thing which we have not yet covered explicitly is how the code whithin if-statements or for-loops is indented (shifted to the right). You might think this is just a way of making the code easier to read, and that would be true for almost all other programming languages. However, Python is a bit different in that regard by **requiring** you to use whitespace with certain rules.

Simply put, whenever you use a *compound statement* (which includes for-loops, conditionals, and also classes and functions which we will cover later), you need to increase the indentation of your code. Once you exit the compound statement, you decrease the indentation level by the same amount. The amound of this indentation is technically up to you, however the Python style guide recommends you to use four spaces. As an example, if we want to continue with the script after the for-loop, we would reset the indentation to the same level as the first for:

```{code-cell} ipython3
for item in my_list:
  if item == "banana":
    print("Banana!")

print("Continue after the for-loop...")
```

```{admonition} Summary
:class: tip

- For Loops: "For each" item in a group, do something.
- Range Loops: "Do this action X times" by counting up to a certain number.
- While Loops: "Keep doing this until..." a certain condition changes.

It is helpful to follow good coding practices:

- Avoid deep nesting. If you find your code nesting too deeply, consider refactoring parts of it into functions (which we will learn about next week).
- Use meaningful variable names. This helps others (and yourself) understand what the code is doing.
```
