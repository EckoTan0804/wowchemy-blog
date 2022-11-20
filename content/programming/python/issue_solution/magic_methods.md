---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 3001
# ============================================================

# ========== Basic metadata ==========
title: Magic Method
date: 2022-11-20
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - Issues & Solution
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

I came across an error with incaution when using the `round()` function:

```python
def get_discount_price(ori_price, discount):
    discount_price = ori_price * (1 - discount)
    # forget to return `discount_price`
```

```python
>>> round(get_discount_price(50, 0.2))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-abb2b34126d0> in <module>
----> 1 round(get_discount_price(50, 0.2))

TypeError: type NoneType doesn't define __round__ method
```

## Reason

The Python built-in `round()` function is implemented by the `__round()__` magic method (a.k.a. dunder methods). If weattempt to call `round(x)` or `round(x, ndigits)`, Python will run the `x.__round__()` or `x.__round__(ndigits)` method, respectively.

Here I forgot to return `discount_price` in `get_discount_price()`. In other words, when I call `get_discount_price()`, it returns nothing, which is of `NoneType`. A `NoneType` object does NOT have or implement the `__round()__` magic methods, which causes the `TypeErroe`.

## Solution

When `TypeError` is raised during calling `round()` function:

1. Check whether the object is of `NoneType`
2. Check whether the `__round()__` magic method is defined or implemented in the class of the object

## Reference

-  [Python __round__() Magic Method](https://blog.finxter.com/python-__round__-magic-method/)