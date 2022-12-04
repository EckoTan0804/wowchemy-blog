---
# ===== Title, summary, and position in the left sidebar =====
linktitle: Object Comparison # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 521
# ============================================================

# ========== Basic metadata ==========
title: "Object Comparison: == vs is"
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

- The `==` operator compares by checking for *equality* (the objects referred to by the variables are equal, i.e. have the same contents)
- The `is` operator comparies *identities* (whether two variables are in fact pointing to the same identical object)

Example

```python
>>> a = [1, 2, 3] 
>>> b = a
```

```python
>>> a
[1, 2, 3] 
>>> b
[1, 2, 3]
```

```python
>>> a == b 
True
```

```python
>>> a is b 
True
```

`a` and `b` point to the same list object, as we assigned them earlier.

```python
>>> c = list(a) # create an identical copy of the list a
```

```python
>>> c
[1, 2, 3]
```

```python
>>> a == c # should be true, as a and c have the same content
True
```

```python
>>> a is c 
False
```

