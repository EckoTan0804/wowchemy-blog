---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 525
# ============================================================

# ========== Basic metadata ==========
title: Abstract Base Class (ABC)
date: 2022-12-11
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

- **Abstract Base Classes (ABCs)** ensure that derived classes implement particular methods from the base class at instantiation time
- Using Python's`abc` module help avoid bugs and make class hierarchies easier to maintain.

------

In OOP, inheritance is very common. To make the code of inheritance relationship as maintainable and programmer-friendly as possible, we want to make sure that

- instantiating the base class is impossible
- forgetting to implement interface methods in one of the sub-classes raises an error as early as possible.

To enforce that a derived class implements a number of meth- ods from the base class, something like this Python idiom is typically used:

```python
class Base:
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()


class Concrete(Base):
    def foo(self):
        return "foo() called"

    # We forgot to override bar()...
```

Calling methods on an instance of `Base `correctly raises `NotImplementedError `exceptions:

```python
>>> b = Base()
>>> b.foo() 
NotImplementedError
```

Furthermore, instantiating and using `Concrete `works as expected. If we call an unimplemented method like `bar()` on it, this also raises an exception:

```python
>>> c = Concrete() 

>>> c.foo()
'foo() called'

>>> c.bar() 
NotImplementedError
```

This implementation is decent. However, it has two downsides

- <span style="color: Red">instantiate `Base` just fine without getting an error (which is not expected, as the base class should be uninstantiatable)</span>
- <span style="color: Red">provide incomplete subclasses—instantiating `Concrete `will not raise an error until we call the missing method `bar()`</span>

We can solve these issues with Python's **`abc`** module. Here’s an updated implemen- tation using an Abstract Base Class defined with the `abc `module:

```python
from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass
```

```python
class Concrete(Base):
    def foo(self):
        pass

    # We forget to declare bar()
```

This still behaves as expected and creates the correct class hierarchy:

```python
>>> issubclass(Concrete, Base)
True
```

Benefit of applying the `abc` module:

- Instantiating base class will raise an exception

  ```python
  >>> b = Base()
  ---------------------------------------------------------------------------
  TypeError                                 Traceback (most recent call last)
  Cell In [19], line 1
  ----> 1 b = Base()
  
  TypeError: Can't instantiate abstract class Base with abstract methods bar, foo
  ```

- Subclasses of Base raise a TypeError *at instantiation time* whenever we forget to im- plement any abstract methods. The raised exception also tells us which method or methods we’re missing, makes it more difficult to write invalid subclasses.

  ```python
  >>> c = Concrete()
  ---------------------------------------------------------------------------
  TypeError                                 Traceback (most recent call last)
  Cell In [10], line 1
  ----> 1 c = Concrete()
  
  TypeError: Can't instantiate abstract class Concrete with abstract method bar
  ```

  

These advantages often make the class hierarchies more robust and more readily maintainable. Using ABCs states the programmer’s intent clearly and thus makes the code more communicative. 👍