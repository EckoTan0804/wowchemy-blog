---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 213
# ============================================================

# ========== Basic metadata ==========
title: Sets
date: 2023-01-07
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - Basics
  - Data structures
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

- Use the built-in `set` type when looking for a mutable set.
- `frozenset` objects are hashable and can be used as dictionary or set keys.
- `collections.Counter` implements multiset or “bag” data structures.

------

## Overview

A **set** is an *unordered* collection of objects that does *NOT* allow duplicate elements.

Typically, sets are used 

- to quickly test a value for membership in the set
- to insert or delete new values from a set
- to compute the union or intersection of two sets

In a “proper” set implementation, membership tests are expected to run in fast `O(1)` time. Union, intersection, difference, and subset operations should take `O(n)` time on average. 

### Sets in Python

In Python, the curly-braces set expression syntax and set comprehensions allow you to conveniently define new set instances:

```python
vowels = {'a', 'e', 'i', 'o', 'u'}
squares = {x * x for x in range(10)}
```

{{% callout note %}}
To create an empty set you’ll need to call the `set()` constructor. Using empty curly-braces `{}` is ambiguous and will create an empty dictionary instead.
{{% /callout %}}

## `set` – Your Go-To Set

This is the built-in set implementation in Python. The `set` type is *mutable* and allows for the dynamic insertion and deletion of elements.

#### Example

```python
>>> vowels = {'a', 'e', 'i', 'o', 'u'}
>>> 'e' in vowels
True

>>> letters = set('alice')
>>> letters.intersection(vowels)
{'a', 'e', 'i'}

>>> vowels.add('x')
>>> vowels
{'i', 'a', 'u', 'o', 'x', 'e'}

>>> len(vowels)
6
```

## `frozenset` – Immutable Sets

- An *immutable* version of set that cannot be changed after it has been constructed.
- Frozensets are static and only allow query operations on their elements (no inserts or deletions.)
- As frozensets are static and hashable, they can be used as dictionary keys or as elements of another set.

#### Example

```python
>>> vowels = frozenset({'a', 'e', 'i', 'o', 'u'}) 
>>> vowels.add('p')
AttributeError:
"'frozenset' object has no attribute 'add'"

# Frozensets are hashable and can
# be used as dictionary keys:
>>> d = { frozenset({1, 2, 3}): 'hello' }
>>> d[frozenset({1, 2, 3})]
'hello'
```

## `collections.Counter` – Multisets

The `collections.Counter` class implements a multiset (or bag) type that allows elements in the set to *have more than one* occurrence.

$\rightarrow$ This is useful if you need to keep track of not only if an element is part of a set, but also how many times it is included in the set

#### Example

```python
>>> from collections import Counter
>>> inventory = Counter()

>>> loot = {'sword': 1, 'bread': 3}
>>> inventory.update(loot)
>>> inventory
Counter({'bread': 3, 'sword': 1})

>>> more_loot = {'sword': 1, 'apple': 1}
>>> inventory.update(more_loot)
>>> inventory
Counter({'bread': 3, 'sword': 2, 'apple': 1})
```

You’ll want to be careful when counting the number of elements in a `Counter` object.

- Calling `len()` returns the number of unique elements in the multiset
- Calling `sum()` returns the total number of elements 

```python
>>> len(inventory)
3  # Number of unique elements

>>> sum(inventory.values())
6  # Total number of elements
```

