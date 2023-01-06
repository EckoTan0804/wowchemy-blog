---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 212
# ============================================================

# ========== Basic metadata ==========
title: Records, Structs, and Data Transfer Objects
date: 2023-01-05
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - Basics
  - Data structures
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

- You only have a few (2-3) fields $\rightarrow$ Using a plain tuple object may be okay if the field order is easy to remember or field names are superfluous.
- You need immutable fields $\rightarrow$ plain tuples, `collections.namedtuple`, and `typing.NamedTuple` would all make good options 
- You need to lock down field names to avoid typos $\rightarrow$ Use `collections.namedtuple` and `typing.NamedTuple`
- You want to keep things simple $\rightarrow$ Try plain dictionary object
- You need full control over your data structure $\rightarrow$ Write a custom class with @property setters and getters.
- You need to add behavior (methods) to the object $\rightarrow$ You should write a custom class, either from scratch or by extending `collections.namedtuple` or `typing.NamedTuple`.
- You need to pack data tightly to serialize it to disk or to send it over the network $\rightarrow$ Use `struct.Struct`

------

Record data structures provide a fixed number of fields, where each field can have a name and may also have a different type.

## `dict` – Simple Data Objects

Python dictionaries store an arbitrary number of objects, each identified by a unique key. Dictionaries are also often called *maps* or *associative arrays* and allow for the efficient lookup, insertion, and deletion of any object associated with a given key.

Dictionaries are easy to create in Python, as they have their own syntactic sugar built into the language in the form of dictionary literals.

Data objects created using dictionaries are mutable, and there’s little protection against misspelled field names, as fields can be added and removed freely at any time. $\rightarrow$ These properties introduce suprising bugs.

Example:

```python
car1 = {
    'color': 'red',
    'mileage': 3812.4,
    'automatic': True,
}
car2 = {
    'color': 'blue',
    'mileage': 40231,
    'automatic': False,
}

# Dicts have a nice repr:
>>> car2
{'color': 'blue', 'automatic': False, 'mileage': 40231}

# Get mileage:
>>> car2['mileage']
40231

# Dicts are mutable:
>>> car2['mileage'] = 12
>>> car2['windshield'] = 'broken'
>>> car2
{'windshield': 'broken', 'color': 'blue',
 'automatic': False, 'mileage': 12}

# No protection against wrong field names,
# or missing/extra fields:
car3 = {
    'colr': 'green',
    'automatic': False,
    'windshield': 'broken',
}
```

## `tuple` – Immutable Groups of Objects

Python’s tuples are simple data structures for grouping arbitrary objects. They are immutable—they can NOT be modified once they’ve been created.

Performance-wise, tuples take up slightly less memory than lists in CPython,17 and they’re also faster to construct. However, In practice, the performance difference will often be negligible. Trying to squeeze extra performance out of a program by switching from lists to tuples will likely be the wrong approach.

Downside of plain tuple:

- <span style="color: Red">The data stored in tuples can only be pulled out by accessing it through integer indexes. ou can’t give names to individual properties stored in a tuple. $\rightarrow$ This can impact code readability.</span>
- <span style="color: Red">A tuple is always an *ad-hoc* structure: It’s difficult to ensure that two tuples have the same number of fields and the same properties stored on them. $\rightarrow$ This makes it easy to introduce “slip-of-the-mind” bugs, such as mixing up the field order.</span>

Example:

```python
# Fields: color, mileage, automatic
>>> car1 = ('red', 3812.4, True)
>>> car2 = ('blue', 40231.0, False)

# Tuple instances have a nice repr:
>>> car1
('red', 3812.4, True)
>>> car2
('blue', 40231.0, False)

# Get mileage:
>>> car2[1]
40231.0

# Tuples are immutable:
>>> car2[1] = 12
TypeError:
"'tuple' object does not support item assignment"

# No protection against missing/extra fields # or a wrong order:
>>> car3 = (3431.5, 'green', True, 'silver')
```

## Writing a Custom Class – More Work, But More Control

Classes allow you to define reusable “blueprints” for data objects to ensure each object provides the same set of fields.

However, this approach has some limitations:

- It takes manual work to get the convenience features of other implementations. E.g., adding new fields to the `__init__` constructor is verbose and takes time.
- The default string representation for objects instantiated from custom classes is not very helpful. To fix that you may have to add your own `__repr__` method, which again is usually quite verbose and must be updated every time you add a new field.
- Although it’s possible to provide more access control and to create read-only fields using the `@property` decorator, this requires writing more glue code.

When should we write a custom class?

Writing a custom class is a great option whenever you’d like to add business logic and behavior to your record objects using methods.

Example: we implement the `Car` above with custom class:

```python
class Car:
def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic
        
>>> car1 = Car('red', 3812.4, True)
>>> car2 = Car('blue', 40231.0, False)

# Get the mileage:
>>> car2.mileage
40231.0

# Classes are mutable:
>>> car2.mileage = 12
>>> car2.windshield = 'broken'

# String representation is not very useful
# (must add a manually written __repr__ method): >>> car1
<Car object at 0x1081e69e8>
```

## `collections.namedtuple` – Convenient Data Objects

Similar to defining a custom class, using `namedtuple` allows you to define reusable “blueprints” for your records that ensure the correct field names are used.

`namedtuple` is an extension of the built-in `tuple`

- Namedtuples are immutable - you can NOT add new fields or modify existing fields after the namedtuple instance was created.
- Each object stored in them can be accessed through a unique identifier.

Namedtuple objects are implemented as regular Python classes internally. When it comes to memory usage, they are also “better” than regular classes and just as memory efficient as regular tuples. :thumbsup:

Moreover, Namedtuples can be an easy way to clean up your code and make it more readable by enforcing a better structure for your data. It can also helps you express the intent of your code more clearly.

Example: Implement the `Car` above with `namedtupule`

```python
>>> from collections import namedtuple
>>> Car = namedtuple('Car' , 'color mileage automatic') 
>>> car1 = Car('red', 3812.4, True)

# Instances have a nice repr:
>>> car1
Car(color='red', mileage=3812.4, automatic=True)

# Accessing fields:
>>> car1.mileage
3812.4

# Fields are immtuable:
>>> car1.mileage = 12
AttributeError: "can't set attribute"
>>> car1.windshield = 'broken' AttributeError:
"'Car' object has no attribute 'windshield'"
```

## `typing.NamedTuple` – Improved Namedtuples

`typing.NamedTuple` is very similar to `collections.namedtuple`, the main difference being an updated syntax for defining new record types and added support for type hints.

Example:

```python
>>> from typing import NamedTuple
class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool
>>> car1 = Car('red', 3812.4, True)

# Instances have a nice repr:
>>> car1
Car(color='red', mileage=3812.4, automatic=True)

# Accessing fields:
>>> car1.mileage
3812.4

# Fields are immutable:
>>> car1.mileage = 12
AttributeError: "can't set attribute"
>>> car1.windshield = 'broken' AttributeError:
"'Car' object has no attribute 'windshield'"

# Type annotations are not enforced without
# a separate type checking tool like mypy:
>>> Car('red', 'NOT_A_FLOAT', 99)
Car(color='red', mileage='NOT_A_FLOAT', automatic=99)
```

## `types.SimpleNamespace` – Fancy Attribute Access

`SimpleNamespace` is basically a glorified dictionary that allows attribute access and prints nicely. Attributes can be added, modified, and deleted freely.

- `SimpleNamespace` instances expose all of their keys as class attributes. 

  $\rightarrow$ You can use obj.key “dotted” attribute access instead of the `obj['key']` square-brackets indexing syntax that’s used by regular dicts.

- All instances also include a meaningful `__repr__` by default.

Example:

```python
>>> from types import SimpleNamespace
>>> car1 = SimpleNamespace(color='red',
...                        mileage=3812.4,
...                        automatic=True)

# The default repr:
>>> car1
namespace(automatic=True, color='red', mileage=3812.4)

# Instances support attribute access and are mutable:
>>> car1.mileage = 12
>>> car1.windshield = 'broken'
>>> del car1.automatic
>>> car1
namespace(color='red', mileage=12, windshield='broken')
```

