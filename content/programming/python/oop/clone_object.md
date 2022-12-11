---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 524
# ============================================================

# ========== Basic metadata ==========
title: Object Cloning
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

- Making a shallow copy of an object won’t clone child objects. → The copy is not fully independent of the original.
- A deep copy of an object will recursively clone child objects.The clone is fully independent of the original, but creating a deep copy is slower.
- You can deep or shallow copy arbitrary objects with the standard `copy` module.

------

## Shallow vs. Deep Copy

For compound objects, there’s an important difference between ***shallow*** and ***deep* copying**:

- Shallow copy
  - Constructing a new collection object and then **populating it with references to the child objects** found in the original → only ***one level*** deep
  - The copying process does NOT recurse and therefore won’t create copies of the child objects themselves.

- Deep copy

  - Makes the copying process recursive

    - first constructing a new collection object
    - then recursively populating it with copies of the child objects found in the original

    → Copying an object this way walks the whole object tree to create a **fully independent clone** of the original object and all of its children.

## Shallow Copy

Python’s built-in mutable collections like lists, dicts, and sets can be *shallowly* copied by calling their **factory functions** on an existing collection:

```python
new_list = list(original_list) 
new_dict = dict(original_dict) 
new_set = set(original_set)
```

#### Example

we’ll create a new nested list and then *shallowly* copy it with the `list()` factory function:

```python
>>> xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
>>> ys = list(xs) # Make a shallow copy
```

Now `ys` will be a new and independent object with the same contents as `xs`:

```python
>>> xs
[[1, 2, 3], [4, 5, 6], [7, 8, 9]] 

>>> ys
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

To further verify that `ys` is really independent from the original, we add a new sublist ot the original `xs` and check to make sure this modification didn’t affect the copy `ys`:

```python
>>> xs.append(['new'])
>>> xs
[[1, 2, 3], [4, 5, 6], [7, 8, 9], ['new']] 

>>> ys
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

**However, because we only created a *shallow* copy of the original list `xs`, `ys `still contains references to the original child objects stored in `xs`. These children were *NOT* copied. They were merely referenced again in the copied list.**

```python
>>> xs[1][0] = 'X'
>>> xs
[[1, 2, 3], ['X', 5, 6], [7, 8, 9], ['new']] 

>>> ys
[[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
```

The diagram below shows how this works:

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/python_shallow_copy.png" alt="python_shallow_copy" style="zoom:67%;" />

## Use The`copy` Module

The `copy` module in the Python standard library provides a simple interface for creating shallow and deep copies of arbitrary Python objects.

- `copy.deepcopy()` creates deep copy
- `copy.copy()` creates shallow copy

{{% callout note %}}
For built-in collections it’s considered more Pythonic to simply use the list, dict, and set factory functions to create shallow copies.
{{% /callout %}}