---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 522
# ============================================================

# ========== Basic metadata ==========
title: String Conversion
date: 2022-12-04
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - Basics
  - OOP
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

- Control to-string conversion in your own classes using the `__str__` and `__repr__` "dunder" methods
- The result of `__str__` should be readable. The result of `__repr__ `should be unambiguous.
- Always add a `__repr__ `to your classes. The default implemen- tation for `__str__` just calls `__repr__`.

------

When you define a custom class in Python and then try to print one of its instances to the console (or inspect it in an interpreter session), by default you will get a string containing the class name and the `id `of the object instance (which is the object’s memory address in CPython.) → This default "to string" conversion behavior is basic and lacks detail.

Example

```python
class Car:
    def __init__(self, color, mileage):
        self.color = color 
        self.mileage = mileage
        
>>> my_car = Car('red', 37281)
>>> print(my_car)
<__console__.Car object at 0x109b73da0> 
>>> my_car
<__console__.Car object at 0x109b73da0>
```

nstead of building your own to-string conversion machinery, you’ll be better off **adding the` __str__` and` __repr__` “dunder” methods to your class**. They are the Pythonic way to control how objects are converted to strings in different situations

```python
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        # return f"a {self.color} car"
		return f'a {self.color} car'
```

```python
>>> my_car = Car('red', 37281) 
>>> print(my_car)
'a red car'
>>> my_car
<__console__.Car object at 0x109ca24e0>
```

## `__str__` vs. `__repr__`

- When `print()` an object, or involving string, the `__str__` method will be called.
- inspecting an object in a Python inter- preter session simply prints the result of the object’s` __repr__`.

Example:

```python
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        # return f"a {self.color} car"
        return "__str__ for Car"

    def __repr__(self):
        return "__repr__ for Car"
```

```python
>>> my_car = Car('red', 37281) 

>>> print(my_car)
__str__ for Car

>>> '{}'.format(my_car) 
'__str__ for Car'

>>> my_car 
__repr__ for Car
```

Interestingly, containers like lists and dicts always use the result of `__repr__` to represent the objects they contain. Even if you call str on the container itself:

```python
>>> str([my_car])
'[__repr__ for Car]'
```

**To express your code’s intent more clearly, it’s best to use the built-in `str()` and `repr()` functions.** Using them is preferable over calling the object’s `__str__` or `__repr__` directly, as it looks nicer and gives the same result:

```python
>>> str(my_car) 
'__str__ for Car' 

>>> repr(my_car) 
'__repr__ for Car'
```

Difference of usage of `__str__` and `__repr__`:

- The result of the date object’s` __str__` function should primarily be ***readable***.

  - It’s meant to return a concise textual representation for human consumption—something you’d feel comfortable displaying to a user.

- With `__repr__`, the idea is that its result should be, above all, ***unambiguous***. 

  - The resulting string is intended more as a debugging aid for developers.

    → It needs to be as explicit as possible about what this object is.

  - **Rule of thumb: make `__repr__` strings unambiguous and helpful for developers** 💪

Example:

```python
>>> import datetime
>>> today = datetime.date.today()

>>> str(today)
'2022-12-04'

>>> repr(today)
'datetime.date(2022, 12, 4)'
```

## Why Every Class Needs a `__repr__`

If you don’t add a `__str__ `method, Python falls back on the result of `__repr__` when looking for `__str__`. Therefore, it is recommended to **always add at least a `__repr__` method to your classes**. This will <span style="color:  ForestGreen">guarantee a useful string conversion result in almost all cases, with a minimum of implementation work</span> 👏.

Example:

```python
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"a {self.color} car"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.color!r}, {self.mileage!r})"
```

Note:  using the `!r` conversion flag makes sure the output string uses `repr(self.color)` and `repr(self.mileage)` instead of `str(self.color)` and `str(self.mileage)`