---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 21
# ============================================================

# ========== Basic metadata ==========
title: "Function: First Class Object"
date: 2022-12-03
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - Basics
  - Function
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

- Everything in Python is an object, including functions. You can
  - assign them to variables
  - store them in data structures
  - pass or return them to and from ohter functions
- First-class functions allow you to abstract away and pass around behavior in your programs.
- Functions can be nested and they can capture and carry some of the parent function’s state with them.
- Objects can be made callable, which allows you to treat them like functions.

------

Python’s functions are **first-class** objects. You can

- [assign them to variables](#functions-are-objects)
- [store them in data structures](#functions-can-be-stored-in-data-structures)
- [pass them as arguments to other functions](#functions-can-be-passed-to-other-functions)
- [return them as values from other functions](#functions-can-be-nested)

Example throughout:

```python
def yell(text):
    return text.upper() + '!'
```

```python
>>> yell('hello') 
'HELLO!'
```

## Functions Are Objects

Like strings, lists, modules, functions in Python are also just objects.

Becaus the `yell` function is an object in Python, we can assign it to another variable:

```python
bark = yell
```

> This line doesn’t call the function. It takes the function object referenced by `yell` and creates a second name, `bark`, that points to it. 

You could now also execute the same underlying function object by calling `bark`:

```python
>>> bark('woof') 
'WOOF!'
```

Function objects and their names are two separate concerns. We can delete the function’s original name (`yell`). Since another name (`bark`) still points to the underlying function, you can still call the function through it:

```python
>>> del yell

>>> yell('hello?')
NameError: "name 'yell' is not defined"

>>> bark('hey') 
'HEY!'
```

For debugging purposes, Python attaches a string identifier to every function at creation time. We can access this internal identifier with the `__name__` attribute:

```python
>>> bark.__name__ 
'yell'
```

## Functions Can Be Stored in Data Structures

We can store functions in data structures, just like we can do with other objects.

Example:

```python
>>> funcs = [bark, str.lower, str.capitalize] 

>>> funcs
[<function yell at 0x10ff96510>,
 <method 'lower' of 'str' objects>, 
 <method 'capitalize' of 'str' objects>]
```

**Accessing** the function objects stored inside the list works like it would with any other type of object:

```python
>>> for f in funcs:
... 	print(f, f('hey there'))

<function yell at 0x10ff96510> 'HEY THERE!' 
<method 'lower' of 'str' objects> 'hey there' 
<method 'capitalize' of 'str' objects> 'Hey there'
```

We can do the lookup and then immediately call the resulting “disembodied” function object within a single expres- sion:

```python
>>> funcs[0]('heyho') 
'HEYHO!'
```

## Functions Can Be Passed to Other Functions

We can pass functions as arguments to other functions.

Example:

```python
def greet(func):
    greeting = func('Hi, I am a Python program') 
    print(greeting)
```

We pass the `bark` functon to `greet`:

```python
>>> greet(bark)
'HI, I AM A PYTHON PROGRAM!'
```

The ability to pass function objects as arguments to other functions is powerful. It allows you to abstract away and pass around *behavior* in your programs. :thumbsup:

Functions that can accept other functions as arguments are also called ***higher-order functions***. They are a necessity for the functional programming style. The classical example for higher-order functions in Python is the built-in `map` function: It takes a function object and an iterable, and then calls the function on each element in the iterable, yielding the results as it goes along.

Example

```python
>>> list(map(bark, ['hello', 'hey', 'hi'])) 
['HELLO!', 'HEY!', 'HI!']
```

## Functions Can Be Nested

Python allows functions to be defined inside other functions. These are often called ***nested functions*** or ***inner functions***. 

Example:

```python
def speak(text): 
    def whisper(t):
        return t.lower() + '...' 
    return whisper(text)
```

```python
>>> speak('Hello, World') 
'hello, world...'
```

Notice that the inner function is "nested". In other words, `whisper` does NOT exist outside `speak`.

```python
>>> whisper('Yo')
NameError:
"name 'whisper' is not defined"

>>> speak.whisper
AttributeError:
"'function' object has no attribute 'whisper'"
```

Is it possible to access that nested `whisper`? Yes. Remember that function are just objects - we can return the inner function to the caller of the parent function.

Example:

```python
def get_speak_func(volume):
    def whisper(text):
        return text.lower() + "..."  
    
    def yell(text):
        return text.upper() + "!"
        
    return yell if volume > 0.5 else whisper
```

Our `get_speak_funct` does NOT actually call any of its inner functions. Instead, it simply selects the appropriate inner function based on the `volume` argument and then returns the function object.

```python
>>> get_speak_func(0.3)
<function get_speak_func.<locals>.whisper at 0x10ae18>

>>> get_speak_func(0.7)
<function get_speak_func.<locals>.yell at 0x1008c8>
```

```python
>>> speak_func = get_speak_func(0.7) 
>>> speak_func('Hello')
'HELLO!'
```

## Functions Can Capture Local State

Not only can functions return other functions, these inner functions can also *capture and carry some of the parent function’s state* with them.

Let's slightly rewrite the `get_speak_func` above:

```python
def get_speak_func(text, volume):
    def whisper():
        return text.lower() + "..."

    def yell():
        return text.upper() + "!"

    return yell if volume > 0.5 else whisper
```

```python
>>> get_speak_func('Hello, World', 0.7)() 
'HELLO, WORLD!'
```

Notice that the inner functions `whisper` and `yell` do not have a `text` parameter. But somehow they can still access the text parameter defined in the parent function. They seem to capture and “remember” the value of that argument.

Functions that do this are called **lexical closures** (or just **closures**). A closure remembers the values from its enclosing lexical scope even when the program flow is no longer in that scope.

This means not only can functions return behaviors but they can also pre-configure those behaviors. Example:

```python
def make_adder(n): 
    def add(x):
		return x + n 
    return add
```

```python
>>> plus_3 = make_adder(3)

>>> plus_3(4) 
7

>>> make_adder(5)(4)
9
```

Here `make_adder` serves as a *factory* to create and configure “adder” functions. Notice that the inner `add` function can still access the `n` argument of the `make_adder`function, since it is in thee enclosing scope.

## Object can behave like functions

Objects can be made *callable*, which allows us to *treat them like functions* in many cases.

If an object is callable, we can use the round parentheses function call syntax on it and even pass in function call arguments. This is powered by the `__call__` dunder method. Under the hood, “calling” an object instance as a function attempts to execute the object’s `__call__` method.

Example: 

```python
class Adder:
    def __init__(self, n):
    	self.n = n
        
    def __call__(self, x):
    	return self.n + x
```

```python
>>> plus_3 = Adder(3) 
>>> plus_3(4)
7
```

Notice that NOT all objects are callable. We can use the built-in `callable` function to check whether an object appears to be callable or not. 