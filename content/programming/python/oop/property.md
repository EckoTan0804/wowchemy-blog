---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 528
# ============================================================

# ========== Basic metadata ==========
title: Property
date: 2023-02-12
draft: false
type: book # page type
authors:
  - admin
tags:
  - admin
tags:
  - Python
  - Basics
  - OOP
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

- Use `@property` decorator for getters and setter in OOP in a more pythonic way.

------

Python programming provides us with a built-in `@property` decorator which makes usage of getter and setters much easier in Object-Oriented Programming. We will learn it step by step with an example.

## The Temperature Example

Let us assume that we decide to make a [class](https://www.programiz.com/python-programming/class) that stores the temperature in degrees Celsius. And, it would also implement a method to convert the temperature into degrees Fahrenheit.

The first naive solution is as follows:

```python
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
```

```python
>>> human = Celsius()
>>> human.temperature = 37

>>> human.temperature
37

>>> human.to_fahrenheit()
98.60000000000001
```

whenever we assign or retrieve any object attribute like `temperature` as shown above, Python searches it in the object's built-in `__dict__` dictionary attribute as

```python
print(human.__dict__) 
# Output: {'temperature': 37}
```

Therefore, `human.temperature` internally becomes `human.__dict__['temperature']`.

**Suppose we want to extend the usability of the Celsius class defined above. We know that the temperature of any object cannot reach below -273.15 degrees Celsius.** An obvious solution to the above restriction will be to hide the attribute `temperature` (make it private) and define new **getter and setter methods** to manipulate it: 

```python
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value
```

```python
>>> human = Celsius()
>>> print(human.get_temperature())
37

>>> print(human.to_fahrenheit())
98.60000000000001

>>> human.set_temperature(-300)
Traceback (most recent call last):
  File "<string>", line 30, in <module>
  File "<string>", line 16, in set_temperature
ValueError: Temperature below -273.15 is not possible.
```

<span style="color: Red">However, the bigger problem with the above update is that all the programs that implemented our previous class have to modify their code from `obj.temperature` to `obj.get_temperature()` and all expressions like `obj.temperature = val` to `obj.set_temperature(val)`. This refactoring can cause problems while dealing with hundreds of thousands of lines of codes!!! </span>

<span style="color: Red"> → All in all, our new update was not backwards compatible.</span>

## The `Property` class

A pythonic way to deal with the above problem is to use the `property` class.

We can update our code:

```python
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)
```

The last line of the code makes a property object `temperature`. Property attaches some code (`get_temperature` and `set_temperature`) to the member attribute accesses (`temperature`).

```python
>>> human = Celsius(37)
Setting value...

>>> print(human.temperature)
Getting value...
37

>>> print(human.to_fahrenheit())
Getting value...
98.60000000000001

>>> human.temperature = -300
Setting value...
Traceback (most recent call last):
  File "<string>", line 31, in <module>
  File "<string>", line 18, in set_temperature
ValueError: Temperature below -273 is not possible
```

Any code that retrieves the value of `temperature` (including `self.temperature`) will automatically call `get_temperature()` instead of a dictionary (__dict__) look-up. Similarly, any code that assigns a value to `temperature` will automatically call `set_temperature()`.

By using `property`, we can see that NO modification is required in the implementation of the value constraint. Thus, our implementation is backward compatible. 👏

{{% callout note %}}
The actual temperature value is stored in the private `_temperature` variable. The `temperature` attribute is a property object which provides an interface to this private variable.
{{% /callout %}}

### More details

In Python, `property()` is a built-in function that creates and returns a `property` object. The syntax of this function is:

```
property(fget=None, fset=None, fdel=None, doc=None)
```

Here,

- `fget` is function to get value of the attribute
- `fset` is function to set value of the attribute
- `fdel` is function to delete the attribute
- `doc` is a string (like a comment)

A property object has three methods, `getter()`, `setter()`, and `deleter()` to specify `fget`, `fset` and `fdel` at a later point. This means, the line:

```python
temperature = property(get_temperature,set_temperature)
```

can be broken down as:

```python
# make empty property
temperature = property()

# assign fget
temperature = temperature.getter(get_temperature)

# assign fset
temperature = temperature.setter(set_temperature)
```

## The `@property` Decorator

A more python (and also the more recommended) way is to use the `@property` decorator. We can even not define the names `get_temperature` and `set_temperature` as they are unnecessary and pollute the class namespace. For this, we reuse the `temperature` name while defining our getter and setter functions.

```python
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
```

## Reference

- [Python @property decorator](https://www.programiz.com/python-programming/property)