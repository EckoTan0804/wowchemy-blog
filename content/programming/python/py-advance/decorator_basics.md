---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 20
# ============================================================

# ========== Basic metadata ==========
title: "Decorator: Basics"
date: 2022-05-21
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - Basics
  - Decorator  
categories:
  - Coding
toc: true # Show table of contents
# ====================================

# ========== Advanced metadata =========
profile: false  # Show author profile?
reading_time: true # Show estimated reading time?
share: true  # Show social sharing links?
featured: true
comments: true  # Show comments?
disable_comment: false
commentable: true  # Allow visitors to comment? Supported by the Page, Post, and Book content types.
editable: false  # Allow visitors to edit the page? Supported by the Page, Post, and Book content types.

# Optional header image (relative to `assets/media/` folder).
header:
  caption: 
  image:  
---

**TL;DR**

- Decorators define reusable building blocks you can apply to a callable to modify its behavior *without* permanently modifying the callable itself.
- The @ syntax is just a shorthand (syntax sugar) for calling the decorator on an input function. 
  - Multiple decorators on a single function are applied bottom to top (*decorator stacking*).
- Use the `functools.wraps` helper in every decorator to carry over metadata from the undecorated callable to the decorated one.
- Decorators are not a cure-all and they should not be overused

------

## What is decorator?

Decorators provide a simple syntax for calling [higher-order functions](http://en.wikipedia.org/wiki/Higher-order_function).

By definition, a decorator is a function that **takes another function and extends the behavior of the latter function *without* explicitly modifying it**. 

In other words, decorators “decorate” or “wrap” another function and let you execute code before and after the wrapped function runs.

- Allow you to define reusable building blocks that can change or extend the behavior of other functions
- Let you do that without permanently modifying the wrapped function itself. The function’s behavior changes only when it’s *decorated*.

**Under the hood, a decorator is *a callable that takes a callable as input and returns another callable*.**

## Functions

Before you can understand decorators, you must first understand how functions work.

In Python, functions

- return a value based on the given arguments
- are **first-class** objects. *I.e.*, functions can be passed around and used as arguments.

### Inner Functions

Inner functions are functions defined **inside** other functions.

Example:

```python
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()
```

- The order in which the inner functions are defined does not matter.

- The inner functions are not defined until the parent function is called. They are locally scoped to `parent()`, i.e., they only exist inside the `parent()` function as local variables.

### Returning Functions From Functions

Python also allows you to use functions as return values. For example:

```python
def parent(num):
    def first_child():
        return "Hi, I am the first child."

    def second_child():
        return "Hi, I am the second child."

    # Return function name without the parentheses means returning a reference to the function
    # In contrast, function name with parentheses refers to the result of evaluating the functions.
    return first_child if num == 1 else second_child
```



## Simple Decorators

Put simply: **decorators wrap a function, modifying its behavior.**

Example:

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

def say_hi():
    print("Hi")
    
say_hi = my_decorator(say_hi)
```

```python
>>> say_hi()
Before function
Hi
After function
```

### Syntactic Sugar

The way we decorated `say_hi()` above is a little clunky.

- We type the function name `say_hi()` three times
- The decoration gets a bit hidden away below the definition of the function.

To facilitate, Python allows you to **use decorators in a simpler way with the `@` symbol** (sometimes called the [“pie” syntax](https://www.python.org/dev/peps/pep-0318/#background)).

The followings are equivalent:

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

def say_hi():
    print("Hi")

say_hi = my_decorator(say_hi)
```

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator # an easier way of say_hi = my_decorator(say_hi)
def say_hi():
    print("Hi")
```

```python
>>> say_hi()
Before function
Hi
After function
```

### Naming of the Inner Function

You can name your inner function whatever you want, and a generic name like `wrapper()` is usually okay. You can also name the inner function with the same name as the decorator but with a `wrapper_` prefix.

Example:

```python
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
```

### Decorating Functions With Arguments

To allow the decorator accept an arbitrary number of positional and keyword arguments, use [`*args` and `**kwargs`](https://realpython.com/python-kwargs-and-args/) in the inner wrapper function.

- It use the `*` and `**` operators in the `wrapper` closure definition to collect all positional and keyword arguments and stores them in variables (`args `and `kwargs`).

-  The `wrapper  `closure then forwards the collected arguments to the original input function using the * and ** “argument unpacking” operators.

Example:

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice
```

```python
@do_twice
def say_hi():
    print("Hi")
    
@do_twice
def greet(name):
    print(f"Hello {name}")
```

```python
>>> say_hi()
Hi
Hi
>>> greet("World")
Hello World
Hello World
```

### Returning Values From Decorated Functions

Make sure the wrapper function returns the return value of the decorated function.

Example

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
```

```python
@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"
```

```python
>>> hi_adam = return_greeting("Adam")
Creating greeting
Creating greeting
>>> print(hi_adam)
Hi Adam        
```

Another example

```python
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return "Hello!"
```



### Getting the Indentity Information

What a decorator do is replacing one function with another. One downside of this process is that it “hides” some of the metadata attached to the original (undecorated) function.

For example, the original function name, its docstring, and parameter list are hidden by the wrapper closure:

```python
def greet():
    """Return a friendly greeting.""" 
    return 'Hello!'

decorated_greet = uppercase(greet)
```

If you try to access any of that function metadata, you’ll see the wrap- per closure’s metadata instead:

```python
>>> greet.__name__
'greet'
>>> greet.__doc__
'Return a friendly greeting.'

>>> decorated_greet.__name__ 
'wrapper'
>>> decorated_greet.__doc__ 
None
```

This makes debugging and working with the Python interpreter awkward and challenging 🤪.

A quick fix for this is to use the `@functools.wraps` decorator in Python’s standard library, which will preserve information about the original function.

{{% callout note %}}
**Technical Detail**

The `@functools.wraps` decorator uses the function `functools.update_wrapper()` to update special attributes like `__name__` and `__doc__` that are used in the introspection.
{{% /callout %}}


Example

```python
import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
```

```python
>>> say_hi
<function __main__.say_hi>
>>> say_hi.__name__
say_hi
>>> help(say_hi)
Help on function say_hi in module __main__:

say_hi()
```

As a best practice, **you should use `functools.wraps` in all of the decorators you write yourself**. It doesn’t take much time and it will save you (and others) debugging headaches down the road.

## Real World Examples

A good boilerplate template for building more complex decorators:

```python
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
```

### Timing Functions

```python
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        runtime = end_time - start_time
        print(f"Finished {func.__name__!r}: in {runtime:.4f} secs.")
        return value

    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i * 2 for i in range(100)])
```

```python
>>> waste_some_time(1000)
Finished 'waste_some_time': in 0.0130 secs.
```

### Debugging Code

```python
import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value

    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if not age:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"
```

```python
>>> make_greeting("Richard", age=20)
Calling make_greeting('Richard', age=20)
'make_greeting' returned 'Whoa Richard! 20 already, you are growing up!'
Whoa Richard! 20 already, you are growing up!
```

### Registering Plugins

Decorators don’t have to wrap the function they’re decorating. They can also simply register that a function exists and return it unwrapped.

*E.g.*, to create a light-weight plug-in architecture:

```python
import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    # Simply stores a reference to the decorated function in the global PLUGINS dict
    # Note that you do not have to write an inner function or use @functools.wraps in this example, 
    # as you are returning the original function unmodified.
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    print(f"Hello {name}")


@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def randomly_greet(name):
    """Randomly chooses one of the registered functions to use."""
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
```

{{< spoiler text="The `@register` decorator simply stores a reference to the decorated function in the global `PLUGINS` dict. " >}}
Because 

```python
@register
def be_awesome(name):
```

is equivalent to 

```python
be_awesome = register(be_awesome)
```

Therefore, whenever adding `@register` on top of the function, this function is registered in `PLUGINS`. In other words, the `PLUGINS` dictionary contains references to thefunction object.

{{< /spoiler >}}

Note that you do not have to write an inner function or use `@functools.wraps` in this example because you are returning the original function unmodified.

```python
>>> PLUGINS
{'be_awesome': <function __main__.be_awesome>,
 'say_hello': <function __main__.say_hello>}
>>> randomly_greet("Alice")
Using 'say_hello'
Hello Alice
```

👍 Main benefit: **You do not need to maintain a list of which plugins exist**. That list is created when the plugins register themselves. This makes it trivial to add a new plugin: **just define the function and decorate it with `@register`**.



## Reference

- [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/#fancy-decorators)
