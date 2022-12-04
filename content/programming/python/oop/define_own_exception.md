---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 523
# ============================================================

# ========== Basic metadata ==========
title: Define Your Own Exception Classes
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

- Defining your own exception types will state your code’s intent more clearly and make it easier to debug.
- Derive your custom exceptions from Python’s built-in Exception class or from more specific exception classes like ValueError or KeyError.
- You can use inheritance to define logically grouped exception hierarchies.

------

Defining your own error types can be of great value:

- You’ll make potential error cases stand out clearly → your functions and modules will become more maintainable.
- You can also use custom error types to provide additional debugging information.

<span style="color:  ForestGreen">→ All of this will improve your Python code and make it easier to under- stand, easier to debug, and more maintainable.</span>

Example: Let’s say you wanted to validate an input string representing a person’s name in your application. 

```python
def validate(name):
    if len(name) < 10:
        raise ValueError
```

However, there’s a downside to using a “high-level” *generic* exception class like `ValueError`. When a name fails to validate, it’ll look like this in the debug stack trace:

```python
>>> validate('joe')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    validate('joe')
  File "<input>", line 3, in validate
    raise ValueError 
ValueError
```

This stack trace isn’t really all that helpful. To be able to fix the problem, your teammate almost certainly has to look up the implementation of `validate()`. This could be time consuming.

An improvement for this is to introduce a custom exception type to represent a failed name validation:

```python
class NameToShortError(ValueError):
    pass

def validate(name):
    if len(name) < 10:
        raise NameToShortError
```

The custom `NameTooShortError` exception is "self-documenting", which results in a much nicer stack track when the validation fails:

```python
>>> validate('jane')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    validate('jane')
  File "<input>", line 3, in validate 
     raise NameTooShortError(name)
NameTooShortError: jane
```


<span style="color:  ForestGreen">Custom exception classes make it much easier to understand what’s going on when things go wrong (and eventually they always do). By spending just 30 seconds on defining a simple exception class, this code snippet became much more communicative already.</span>

## Good Practice

It’s good practice to **create a custom exception base class for the module and then derive all of your other exceptions from it.**

1. Declare a base class that all of our concrete errors will inherit from. E.g.

   ```python
   class BaseValidationError(ValueError):
       pass
   ```

2. All of our “real” error classes can be derived from the base error class. This gives a nice and clean exception hierarchy with little extra effort.

   E.g.

   ```python
   class NameTooShortError(BaseValidationError): 
       pass
   
   class NameTooLongError(BaseValidationError): 
       pass
   
   class NameTooCuteError(BaseValidationError): 
       pass
   ```

Of course you can take this idea further and logically group your exceptions into fine grained sub-hierarchies. <span style="color: Red">But be careful—it’s easy to introduce unnecessary complexity by going overboard with this.</span>

In conclusion, defining custom exception classes makes it easier for your users to adopt an *it’s easier to ask for forgiveness than permission* (EAFP) coding style that’s considered more Pythonic.