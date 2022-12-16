---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 526
# ============================================================

# ========== Basic metadata ==========
title: Class vs Instance Variable
date: 2022-12-16
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

TL;DR

- **Class variables** are for data shared by all instances of a class. They belong to a class, not a specific instance and are shared among all instances of a class.
- **Instance variables** are for data that is unique to each instance. They belong to individual object instances and are not shared among the other instances of a class. Each instance variable gets a unique backing store specific to the instance.
- Class variables can be incautiously "shadowed" by instance variables of the same name, which could introduceds bugs and odd behaviour.
- Be careful and double-check your scoping when dealing with shared state on a class. Automated tests and peer reviews help greatly with that.

------

## Class Variable vs. Instance Variable

Two kinds of data attributes on Python objects

- **Class variables**

  - Declared inside the class definition (but outside of any instance methods)
  - Not tied to any particular instance of a class
  - Class variables store their contents on the class itself, and all objects created from a particular class share access to the same set of class variables.
    - I.e.modifying a class variable affects all object instances at the same time.

- **Instance variables**

  - Always tied to a particular object instance

  - Contents of an instance vari- able are completely independent from one object instance to the next. 

    - I.e. modifying an instance variable only affects one object instance at a time.

#### Example

```python
class Dog:
    num_legs = 4 # class variabel

    def __init__(self, name):
        self.name = name # instance variable
```

```python
>>> jack = Dog('Jack') 
>>> jill = Dog('Jill') 
>>> jack.name, jill.name 
('Jack', 'Jill')
```

We can access the `num_legs` class variable either directly on each `Dog` instance or *on the class itself* :

```python
>>> jack.num_legs, jill.num_legs 
(4, 4)

>>> Dog.num_legs
4
```

If we try to access an *instance* variable through the class, it’ll fail with an `AttributeError`. 

```python
>>> Dog.name
AttributeError:
"type object 'Dog' has no attribute 'name'"
```

The reason is that instance variables are specific to each object instance and are created when the `__init__` constructor runs—they do NOT even exist on the class itself.

Now let's say we want `jack` to have 6 legs. If we directly modify the `num_legs` class variable on the `Dog`class:

```python
>>> Dog.num_legs = 6

>>> jack.num_legs, jill.num_legs 
(6, 6)
```

As we can see, modifying a class variable *on the class namespace* affects all instances of the class.

Let’s roll back the change to the class variable and instead try to give an extra pair o’ legs specifically to `jack`only:

```python
>>> Dog.num_legs = 4 
>>> jack.num_legs = 6
```

```python
>>> jack.num_legs, jill.num_legs, Dog.num_legs 
(6, 4, 4)
```

It seems ok, and we got the result we wanted. But a pitfalls occurs: <span style="color: Red">we introduced a `num_legs` instance variable to the `jack` instance. And now the new `num_legs` instance variable “**shadows**” the class variable of the same name, overriding and hiding it when we access the object instance scope.</span>

```python
>>> jack.num_legs, jack.__class__.num_legs 
(6, 4)
```

