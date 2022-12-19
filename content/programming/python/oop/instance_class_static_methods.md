---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 527
# ============================================================

# ========== Basic metadata ==========
title: Instance, Class, and Static Methods
date: 2022-12-16
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

**TL:DR**

- Instance methods need a class instance and can access the instance through `self`.
- Class methods don’t need a class instance. They can’t accessthe instance (`self`) but they have access to the class itself via `cls`.
- Static methods don’t have access to `cls` or `self`. They work like regular functions but belong to the class’ namespace.
- Static and class methods communicate and (to a certain degree) enforce developer intent about class design. This can have definite maintenance benefits.

------

## Instance vs. Class vs. Static Methods

```python
class MyClass:

    # instance method
    def method(self):
        return "Instance method called", self

    # class method
    @classmethod
    def classmethod(cls):
        return "Class method called", cls

    # static method
    @staticmethod
    def staticmethod():
        return "Static method called"
```

- **Instance method** (`method(self)`)
  - Takes one parameter, `self`, which points to an instance of `MyClass` when the method is called
    - Through the `self` parameter, instance methods can freely access attributes and other methods on the same object. 
  - instance methods can also access the class itself through the `self.__class__` attribute. I.e., instance methods can also modify class state.
- **Class method** (`classmethod(cls)`)
  - Marked with a `@classmethod` decorator
  - Takes a `cls` that points to the class when the method is called
  - Since the class method only has access to this cls argument, it can’t modify object instance state. But it can still modify class state that applies across all instances of the class.
- **Static method** (`staticmethod`)
  - Does not take a `self` or `cls` parameter
  - Can NOT modify object state or class state

**Example**

Instance method:

```python
>>> obj = MyClass()
>>> obj.method()
('Instance method called', <__main__.MyClass at 0x7f7fd8365eb0>)
```

> When the method is called, Python replaces the `self` argument with the instance object, `obj`.

Instance methods can also access the *class itself* through the `self.__class__` attribute. $\rightarrow$ Instance methods can freely modify state on the object instance *and* on the class itself.

Class method: 

```python
>>> obj.classmethod()
('Class method called', __main__.MyClass)
```

The result shows us that it doesn’t have access to the `<MyClass instance>` object,but only to the `<class MyClass>` object, representing the class itself (everything in Python is an object, even classes themselves).

Static method:

```python
>>> obj.staticmethod() 
'static method called'
```

Static methods can neither access the object instance state nor the class state. They work like regular functions but belong to the class’ (and every instance’s) namespace.

Now let's call these method on the class itself:

```python
>>> MyClass.classmethod()
('Class method called', __main__.MyClass)
```

```python
>>> MyClass.staticmethod()
'Static method called'
```

```python
>>> MyClass.method()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In [8], line 1
----> 1 MyClass.method()

TypeError: method() missing 1 required positional argument: 'self'
```

Attempting to call the instance method `method()` failed with a `TypeError`.

This is to be expected. As this time we didn’t create an object instance and tried calling an instance function directly on the class blueprint itself. This means there is no way for Python to populate the `self` argument and therefore the call fails with a `TypeError` exception.

## When to Use `@classmethod`

Let's say we have a `Pizza` class:

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f"pizza ({self.ingredients!r})"

```

and want to creat various pizza objects:

```python
Pizza(['mozzarella', 'tomatoes']) 
Pizza(['mozzarella', 'tomatoes', 'ham', 'mushrooms']) 
Pizza(['mozzarella'] * 4)
```

A nice and clean way to do that is by using class methods as **[*factory functions*](https://en.wikipedia.org/wiki/Factory_(object-oriented_programming))** for the different kinds of pizzas we can create:

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f"pizza ({self.ingredients!r})"
    
    # Use classmethod as factory function to create different kinds of pizza

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
```

Now we use the `cls` argument in the `margherita` and `prosciutto` factory methods instead of calling the `Pizza` constructor directly. Under the hood, these factory methods all use the same `__init__` constructor internally and simply provide a shortcut for remembering all of the various ingredients.

This is a trick called **[*Don’t Repeat Yourself (DRY)*](https://en.wikipedia.org/wiki/Don't_repeat_yourself)** principle. The advantage is that <span style="color:  ForestGreen">if we decide to rename this class at some point, we won’t have to remember to update the constructor name in all of the factory functions</span>.

Another way to look at this use of class methods is to realize that they **allow you to define *alternative* constructors for your classes**.

- Python only allows one `__init__` method per class.
- Using class methods makes it possible to add as many alternative constructors as necessary. $\rightarrow$ <span style="color:  ForestGreen">This can make the interface for your classes self-documenting (to a certain degree) and simplify their usage</span>.

## When To Use `@staticmethod`

- Static methods can’t access class or instance state because they don’t take a `cls` or `self` argument

  - Using static methods is a great signal to show that particular methods are **independent** from everything else around them

  -  This restriction is also enforced by the Python runtime. It allows you to communicate clearly about parts of your class architecture so that new development work is naturally guided to happen within these boundaries. <span style="color:  ForestGreen">In practice, they often help avoid accidental modifications that go against the original design</span>.

- using static methods and class methods are ways to communicate developer intent while enforcing that intent enough to avoid most “slip of the mind” mistakes and bugs that would break the design.
- Static methods also have benefits when it comes to writing test code.
  - As static methods are completely independent from the rest of the class, we do NOT have to worry about setting up a complete class instance before we can test the method in a unit test. We can just fire away like we would if we were testing a regular function. $\rightarrow$ <span style="color:  ForestGreen">this makes future maintenance easier and provides a link between object-oriented and procedural programming styles.</span>