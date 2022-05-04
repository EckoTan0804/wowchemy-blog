---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 510
# ============================================================

# ========== Basic metadata ==========
title: OOP Basics
date: 2022-05-04
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

The concept of OOP in Python focuses on creating reusable code. This concept is also known as DRY (Don't Repeat Yourself).

## Class

A class is **a blueprint for the object.**

Example

```python
class Parrot:
    
    # class attribute (same for all instances of a class)
    species = "bird"
    
    # instance attribute (different for every instance of a class)
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

## Object

An object (instance) is **an instantiation of a class**.

Example:

```python
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
```

Access class attributes:

```python
>>> blu.species
'bird'
>>> woo.species
'bird'
```

Access instance attributes:

```python
>>> print(f"{blu.name} is {blu.age} years old.")
Blu is 10 years old.
>>> print(f"{woo.name} is {woo.age} years old.")
Woo is 15 years old.
```



## Methods

- Functions defined inside the body of a class
- Define the behaviors of an object

Example

```python
class Parrot:
    
    # class attribute
    species = "bird"
    
    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        print(f"{self.name} is singing {song}.")

    def dance(self):
        print(f"{self.name} is dancing.")
```

```python
>>> blu = Parrot("Blu", 10)
>>> blu.sing("'Happy'")
Blu is singing 'Happy'.
```

## Inheritance

Inheritance enables us to define a class that takes all the functionality from a parent class and allows us to add more.

```python
class SuperClass:
    
    def __init__(self):
        pass
    
    def super_method(self):
        pass
    
 
class SubClass(SuperClass):
    
    def __init__(self):
        super().__init__()
        pass
    
    def super_method(self):
        """Override method of SuperClass"""
        pass
    
    def sub_method(self):
        """Method that only belongs to SubClass"""
        pass
```

Example

```python
# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def who_is_this(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        # run the __init__() method of the parent class inside the child class.
        super().__init__() 
        print("Penguin is ready")

    # overrides method
    def who_is_this(self):
        print("Penguin")

    def run(self):
        print("Run faster")
```

```python
>>> peggy = Penguin()
Bird is ready
Penguin is ready
>>> peggy.who_is_this()
Penguin
>>> peggy.run()
Run faster
```

## Encapsulation

**Encapsulation: Restrict access to methods and variables to prevent data from direct modification**.

In python, private attributes is denoted using underscore(s) as the prefix, *i.e.*, `_` or `__`. The main difference between them is:

- Prefix `_` is just a naming convention indicating a name is meant for internal use. It is NOT enforced by the Python interpreter (except in wildcard imports) and meant as a hint to the programmer only.
- Prefix `__` triggers name mangling when used in a class context (*i.e.*, can be not directly accessed) and is enforced by the Python interpreter.

More about underscores see: [Underscores in Python]({{< relref "../py-basics/py-underscore" >}}).

Example:

```python
class Computer:

    def __init__(self):
        self._min_price = 800
        self.__max_price = 900

    def sell(self):
        print(f"Price: {self._min_price} ~ {self.__max_price}")

    def set_max_price(self, max_price):
        self.__max_price = max_price
```

```python
>>> computer.sell()
Price: 800 ~ 900
```

Variable with `__` prefix can not be directly accessed or modified:

```python
>>> computer.__max_price
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-20-2eb906d81ddf> in <module>()
----> 1 computer.__max_price

AttributeError: 'Computer' object has no attribute '__max_price'
```

```python
>>> computer.__max_price = 1000
>>> computer.sell()
Price: 800 ~ 900
```

We have to use setters and getters:

```python
>>> computer.get_max_price()
900
```

```python
>>> computer.set_max_price(1000)
computer.sell()
```

In contrast, variable with `_` can be directly accessed or modified:

```python
>>> computer._min_price
800
>>> computer._min_price = 950
>>> computer._min_price
950
```

## Polymorphism

Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

Example:

```python
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
```

Output

```txt
Parrot can fly
Penguin can't fly
```

## Reference

- [Python Object Oriented Programming](https://www.programiz.com/python-programming/object-oriented-programming)

- [Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/#what-is-object-oriented-programming-in-python)