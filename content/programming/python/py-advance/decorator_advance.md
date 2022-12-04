---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 21
# ============================================================

# ========== Basic metadata ==========
title: "Decorator: Advance" 
date: 2022-05-23
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

In [Decorator: Basics]({{< relref "decorator_basics" >}}), we have seen the basics of decorators. 

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

The key is to remember the following two expressions are equivalent (the latter uses the syntactic sugar):

```python
def function():
    pass

function = decorator(function)
```

```python
@decorator
def function():
    pass
```

Here we will explore more advanced features

- [Decorating classes](#decorating-classes)
- [Nesting decorators](#nesting-decorators)
- [Decorators with arguments](#decorators-with-arguments)
- [Stateful decorators](#stateful-decorators)
- [Classes as Decorators](#classes-as-decorators)

We will resue some custom decorators defined before:

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


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
```



## Decorating Classes

There are two different ways to use decorators on classes

- [Decorate the methods of a class](#deocrate-the-methods-of-a-class)
- [Decorate the whole class](#decorate-the-whole-class)

### Decorate the methods of a class

Some commonly used decorators (that are even built-ins in Pythons)

- [`@classmethod`, `@staticmethod`](https://realpython.com/instance-class-and-static-methods-demystified/)

  Define methods inside a class namespace that are not connected to a particular instance of that class

- [`@property`](https://docs.python.org/library/functions.html#property)

  Customize getters and setters for class attribute


{{< spoiler text="Example" >}}
```python
class Circle:

    def __init__(self, radius):
        self._radius = radius

    # radius is a mutable property: it can be set to a different value.
    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    # area is an immutable property 
    # since preperties without setter methods can not be changed
    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius ** 2

    # regular method
    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    # Class method, which is not bound to one particular instance of Circle.
    # Class methods are often used as factory methods that can create specific instances of the class.
    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    # Static method.
    # It’s not really dependent on the Circle class, except that it is part of its namespace. 
    # Static methods can be called on either an instance or the class.
    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.14155926535
```

```python
>>> c = Circle(5)
>>> c.radius
5

>>> c.area
78.5398163375

>>> c.radius = 2
>>> c.area
12.566370614

>>> c.area = 100
AttributeError: can't set attribute
```

```python
>>> c.cylinder_volume(height=4)
50.265482456

>>> c.radius = -1
ValueError: Radius must be positive

>>> c = Circle.unit_circle()
>>> c.radius
1

>>> c.pi()
3.1415926535

>>> Circle.pi()
3.1415926535
```
{{< /spoiler >}}


We can also apply custom decoraters to decorate methods.

{{< spoiler text="Example" >}}
```python
class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
```

```python
>>> tw = TimeWaster(1000)
Calling __init__(<time_waster.TimeWaster object at 0x7efccce03908>, 1000)
'__init__' returned None

>>> tw.waste_time(999)
Finished 'waste_time' in 0.3376 secs
```
{{< /spoiler >}}

### Decorate the whole class

A [common use of class decorators](https://www.python.org/dev/peps/pep-3129/#rationale) is to be a simpler alternative to some use-cases of [metaclasses](https://realpython.com/python-metaclasses/). For example, the new [`dataclasses` module](https://realpython.com/python-data-classes/) in [Python 3.7](https://realpython.com/python37-new-features/)

```python
from dataclasses import dataclass

@dataclass
class PlayingCard:
    rank: str
    suit: str
```

The meaning of the syntax is similar to the function decorators: In the example above, you could have done the decoration by writing `PlayingCard = dataclass(PlayingCard)`.

Writing a class decorator is very similar to writing a function decorator. The only difference is that the decorator will receive a **class** and not a function as an argument.

{{< spoiler text="Example" >}}
```python
@timer # a shorthand for TimeWaster = timer(TimeWaster)
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
```
Decorating a class does NOT decorate its methods. Here, `@timer` only measures the time it takes to instantiate the class:

```python
>>> tw = TimeWaster(1000)
Finished 'TimeWaster' in 0.0000 secs

>>> tw.waste_time(999)
>>>
```

{{< /spoiler >}}

## Nesting Decorators

You can apply more than one decorator to a function. This accumulates their effects and it’s what makes decorators so helpful as reusable building blocks.

The order of application of decorators is **from bottom to top**. It is sometimes called **decorator stacking**: You start building the stack at the bottom and then keep adding new blocks on top to work your way upwards.

{{< spoiler text="Example" >}}
```python
@debug
@do_twice
def greet(name):
    print(f"Hello {name}")
```
The decorators will be executed in the order they are listed. In other words, `@debug` calls `@do_twice`, which calls `greet()`, or `debug(do_twice(greet()))`.

```python
>>> greet("Eva")
Calling greet('Eva')
Hello Eva
Hello Eva
'greet' returned None
```

Change the order of `@debug` and `@do_twice`:

```python
from decorators import debug, do_twice

@do_twice
@debug
def greet(name):
    print(f"Hello {name}")
```

In this case, `@do_twice` will be applied to `@debug` as well (do_twice(debug(greet()))):

```
>>> greet("Eva")
Calling greet('Eva')
Hello Eva
'greet' returned None
Calling greet('Eva')
Hello Eva
'greet' returned None
```

{{< /spoiler >}}

{{< spoiler text="Example" >}}

We define two decorators which wrap the output string of the decorated function in HTML tags.

```python
def strong(func):
    def wrapper():
        return f"<strong> {func()} </strong>"
    return wrapper


def emphasis(func):
    def wrapper():
        return f"<em> {func} </em>"
    return wrapper
```

Apply them to the `greet()` function at the sme time:

```python
@strong
@emphasis
def greet():
    return "Hello!"
```

```python
>>> greet() 
'<strong><em>Hello!</em></strong>'
```

{{< /spoiler >}}

## Decorators With Arguments

Syntax for decorators with parameters:

```python
@decorator(params)
def func_name():
    ''' Function implementation'''
```

The above code is equivalent to 

```python
def func_name():
    ''' Function implementation'''

func_name = (decorator(params))(func_name)
```

To create a decorator that accepts arguments, you need to create a *"meta-decorator"* function that

- takes arguments and
- returns a regular decorator (which in turns returns a function)

Example: Extend `@do_twice` to a `@repeat(num_times)` decorator, where the number of times to execute the decorated function could then be given as an argument.

```python
import functools

def repeat(num_times):
    # By passing num_times, a closure is created, 
    # where the value of num_times is stored until it will be used later by wrapper_repeat()
    
    ### Just a common regular decorator ###
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    #######################################
    
    return decorator_repeat
	
```

```python
@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")
```

```python
>>> greet("World")
Hello World
Hello World
Hello World
Hello World
```

### More flexible: optionally take arguments

We can also define decorator that can be used both with and without arguments.

```python
import functools

def name(
    original_func=None, 
    *, # enforce that following parameters are keyword-only
    kw1=val1,
    kw2=val2,
    ...
):
    def decorator_name(function):
        @functools.wraps(function)
        def wrapper_function(*args, **kwargs):
            ...
            
        return wrapper_function
    
    if original_func:
        return decorator_name(original_func)
    
    return decorator_name
    
```

{{< spoiler text="Explanation" >}}

- When the `name` is called with no optional arguments

    ```python
    @name
    def function():
        ...
    ```

    The function is passed as the first argument and the decorated function will be returned:

    ```python
    function = name(original_func=function)
    ```

    As `name(original_func=function)` returns `decorator_name(function)`, the code above is equivalent to 

    ```python
    function = decorator_name(function)
    ```

    which is the same as a regular decorator.

- When the decorator is called with one or more optional arguments

  ```python
  @name(kw1="some value")
  def function():
      ...
  ```

  The `name` is called with `original_func=None` and `kw1="some value"`:

  ```python
  function = (name(original_func=None, * kw1="some value"))(function)
  ```

  As `name(original_func=None, * kw1="some value")` returns `decorator_name`, the code above is equivalent to 

  ```python
  function = decorator_name(function)
  ```

  , as expected.

{{< /spoiler >}}

Example: Apply this boilerplate on the `@repeat` decorator

```python
def repeat(original_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func):
            def wrapper_repeat(*args, **kwargs):
                for _ in range(num_times):
                    value = func(*args, **kwargs)
                return value
            return wrapper_repeat
        
    if original_func:
        return decorator_repeat(original_func)
    
    return decorator_repeat
```

```python
@repeat
def say_whee():
    print("Whee!")

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")
```

```python
>>> say_whee()
Whee!
Whee!

>>> greet("Penny")
Hello Penny
Hello Penny
Hello Penny
```

## Stateful Decorators

Sometimes it’s useful to have a decorator that can keep track of state. We can use the function attribute of the wrapper function to store the state.

Example: create a decorator that counts the number of times a function is called.

```python
import functools

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1 # update the state
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0 # store the initialized state using the function attribute
    return wrapper_count_calls

@count_calls
def say_whee():
    print("Whee!")
```

```python
>>> say_whee()
Call 1 of 'say_whee'
Whee!

>>> say_whee()
Call 2 of 'say_whee'
Whee!

>>> say_whee.num_calls
2
```

## Classes as Decorators

The typical way to maintain state is by using classes.

A typical implementation of a decorator class needs to implement

- `.__init__()`
  - stores a reference to the function
  - do any other necessary initialization
- `.__call__()`: the class instance needs to be [callable](https://docs.python.org/reference/datamodel.html#emulating-callable-objects) so that it can stand in for the decorated function

Example: implement `count_calls` in the previous section

```python
import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_whee():
    print("Whee!")
```

```python
>>> say_whee()
Call 1 of 'say_whee'
Whee!

>>> say_whee()
Call 2 of 'say_whee'
Whee!

>>> say_whee.num_calls
2
```

## Real World Examples / Use Cases

### Slowing Down Code

```python
import functools
import time

def slow_down(_func=None, *, rate=1):
    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            print(f"Sleep for {rate} second.")
            value = func(*args, **kwargs)
            return value
        return wrapper_slow_down
    if _func:
        return decorator_slow_down(_func)
    
    return decorator_slow_down
```

```python
@slow_down(rate=2)
def countdown(from_number):
    if from_number < 1:
        print("Lift off!")
    else:
        print(from_number)
        return countdown(from_number - 1)
```

```python
>>> countdown(5)
Sleep for 2 second.
5
Sleep for 2 second.
4
Sleep for 2 second.
3
Sleep for 2 second.
2
Sleep for 2 second.
1
Sleep for 2 second.
Lift off!
```

### Creating Singletons

A singleton is a class with **only ONE** instance.

The idea of turning a class into a singleton 

- Store the first instance of the class as an attribute
- Simply freturn the stored instance if later attempts at creating an instance

Example:

```python
import functools

def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass
```

```python
>>> first_one = TheOne()
>>> another_one = TheOne()
>>> id(first_one) == id(another_one)
True
>>> first_one is another_one
True
```

We can also implement singleton with class decorator:

```python
import functools

class Singleton:
    
    def __init__(self, cls):
        functools.update_wrapper(self, cls)
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if not self.instance:
            self.instance = self.cls(*args, **kwargs)

        return self.instance
```

```python
@Singleton
class OnlyOne:
    pass
```

```python
>>> first_one = OnlyOne()
>>> another_one = OnlyOne()
>>> id(first_one) == id(another_one)
True
>>> first_one is another_one
True
```

### Caching Return Values

Decorators can provide a nice mechanism for [caching](https://en.wikipedia.org/wiki/Cache_(computing)) and [memoization](https://en.wikipedia.org/wiki/Memoization). We can use the function attribute of the inner wrapper function to store a cache lookup table.

Example: Fibonacci

```python
def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        # args_repr = [repr(arg) for arg in args]
        # kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        # signature = ", ".join(args_repr + kwargs_repr)
        # print(f"{func.__name__}({signature}) cache: {wrapper_cache.cache}")

        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)
```

The function attribute `wrapper_cache.cache` works a s a lookup table, which use the function argument(s) as the key. So now `fibonacci()` only does the necessary calculations ONCE.

For example, if we have called `fibonacci(2)` (which returns `1`) before, the item `{(2, ): 1}` will be stored in `wrapper_cache.cache`, the lookup table. Next time when we call `fibonacci(2)`, we do not need to execute the whole function again. Instead, we just retrieve the value from the lookup table.

```python
>>> fibonacci(10)
Call 1 of 'fibonacci'
...
Call 11 of 'fibonacci'
55

>>> fibonacci(8)
21
```

Note: in the final call to `fibonacci(8)`, no new calculations were needed, since the eighth Fibonacci number had already been calculated for `fibonacci(10)`.

In the standard library, a [Least Recently Used (LRU) cache](https://realpython.com/lru-cache-python/) is available as [`@functools.lru_cache`](https://docs.python.org/library/functools.html#functools.lru_cache).

- has more features 
- You should use `@functools.lru_cache` instead of writing your own cache decorator

```python
import functools

@functools.lru_cache(maxsize=4)
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)
```

## Reference

- [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/#fancy-decorators): detailed and clear tutorial for Python decorators

- Decorators with arguments
  
  - Python Tutorial: Decorators With Arguments
  
    {{< youtube KlBPCzcQNU8 >}}
  
  - Python Decorators 2: Decorators with arguments
  
    {{< youtube pr1xfd6oTwY>}}
  
  - [Making decorators with optional arguments](https://stackoverflow.com/a/24617244/4891826)
