---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 23
# ============================================================

# ========== Basic metadata ==========
title: "Function: Return `None`"
date: 2022-12-04
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

Python adds an implicit return `None `statement to the end of any function. In other words, if a function doesn’t specify a return value, it returns `None `by default.

This means you can replace return None statements with bare return statements or even leave them out completely and still get the same result. E.g.:

```python
def foo1(value):
    if value:
        return value
    else: 
        return None


def foo2(value):
    """Bare return statement implies `return None`"""
    if value:
        return value
    else: 
        return


def foo3(value):
    """Missing return statement implies `return None`"""
    if value:
        return value
```

```python
>>> type(foo1(0)) 
<class 'NoneType'>

>>> type(foo2(0)) 
<class 'NoneType'>

>>> type(foo3(0)) 
<class 'NoneType'>
```

Rule of thumb: 

- If a function does *NOT* have a return value (other languages would call this a *procedure*), then leave out the `return `statement.
- If a function *does* have a return value from a logical point of view, then you need to decide whether to use an im- plicit return or not.