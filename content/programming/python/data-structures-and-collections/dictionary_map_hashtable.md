---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 210
# ============================================================

# ========== Basic metadata ==========
title: Dictionaries, Maps, and Hashtables
date: 2022-12-19
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

- Dictionaries are the central data structure in Python
- THe built-in `dict` type is "good enough" most of the time
- Specialized implementations, like read-only or ordered dicts, are also available in the Python standard library.

------

In Python, **dictionaries** (or “dicts” for short) 

- store an arbitrary number of objects, each identified by a unique dictionary *key*.
- also called ***maps*, *hashmaps*, *lookup tables*, or *associative arrays***.
- allow for the efficient lookup, insertion, and deletion of any object associated with a given key.

## `dict`

Python features a robust dictionary implementation that’s built directly into the core language: the `dict` data type.

"Suyntactic sugar" for working with dicts:

- curly-braces dict expression syntax

  ```python
  phonebook = {
      "bob": 7387,
      "alice": 3719,
      "jack": 7052,
  }
  
  >>> phonebook['alice']
  3719
  ```

- dictionary comprehensions

  ```python
  squares = {x: x * x for x in range(6)}
  
  >>> squares
  {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
  ```

Python’s dictionaries are indexed by keys that can be of any **hashable** type.

- A hashable object has a hash value which never changes during its lifetime (see `__hash__`), and it can be compared to other objects (see `__eq__`). 
- Hashable objects which compare as equal must have the same hash value.

For most use cases, Python’s built-in dictionary implementation will do everything you need.

- Are highly optimized and underlie many parts of the language (*e.g.* class attributes and variables in a stack frame are both stored internally in dictionaries)
- Are  based on a well-tested and finely tuned hash table implementation that provides $O(1)$  time complexity for lookup, insert, update, and delete operations in the average case.

## `collections.OrderedDict`

- Remembers the insertion order of keys added to it
- Must be imported from the `collections` module

Example

```python
>>> from collections import OrderedDict
>>> d = OrderedDict(one=1, two=2, three=3)
>>> d
OrderedDict([('one', 1), ('two', 2), ('three', 3)])

>>> d["four"] = 4
>>> d
OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])

>>> d.keys()
odict_keys(['one', 'two', 'three'])
```

## `collections.defaultdict`

- Accepts a callable in its constructor whose return value will be used if a requested key cannot be found

Example: Use `list` as the [`default_factory`](https://docs.python.org/3/library/collections.html#collections.defaultdict.default_factory)

```python
>>> from collections import defaultdict
>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...    d[k].append(v)
...
>>> sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```

> - When each key is encountered for the *first* time, it is not already in the mapping; so an entry is automatically created using the [`default_factory`](https://docs.python.org/3/library/collections.html#collections.defaultdict.default_factory) function which returns an empty [`list`](https://docs.python.org/3/library/stdtypes.html#list). The `list.append()` operation then attaches the value to the new list.
> - When keys are encountered again, the look-up proceeds normally (returning the list for that key) and the `list.append()` operation adds another value to the list.

Example: Setting the [`default_factory`](https://docs.python.org/3/library/collections.html#collections.defaultdict.default_factory) to [`int`](https://docs.python.org/3/library/functions.html#int) makes the [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict) useful for counting

```python
from collections import defaultdict

s = "mississippi"
d = defaultdict(int)

for k in s:
    d[k] += 1
```

```python
>>> d.items()
dict_items([('m', 1), ('i', 4), ('s', 4), ('p', 2)])
```

> - When a letter is first encountered, it is missing from the mapping, so the [`default_factory`](https://docs.python.org/3/library/collections.html#collections.defaultdict.default_factory) function calls [`int()`](https://docs.python.org/3/library/functions.html#int) to supply a default count of zero.
> - The increment operation then builds up the count for each letter.

## `collections.ChainMap`

- Quickly links a number of mappings so they can be treated as a single unit. It is often much faster than creating a new dictionary and running multiple [`update()`](https://docs.python.org/3/library/stdtypes.html#dict.update) calls.

- Is **an updatable view over multiple dicts, and it behaves just like a normal dict** (All of the usual dictionary methods are supported).

- Can be used to simulate nested scopes and is useful in templating.

- Use cases

  - Searching through multiple dictionaries

    Example:

    ```python
    >>> toys = {'Blocks': 30, 'Monopoly': 20}
    >>> computers = {'iMac': 1000, 'Chromebook': 800, 'PC': 400}
    >>> clothing = {'Jeans': 40, 'T-Shirt': 10}
    ```

    ```python
    >>> from collections import ChainMap
    >>> inventory = ChainMap(toys, computers, clothing)
    ```

    Test some normal dict operations:

    ```python
    >>> inventory['Monopoly']
    20
    
    >>> inventory.get('Mario Bros.')
    None
    
    >>> inventory.pop('Blocks')
    200
    
    >>> inventory['Blocks']  
    # KeyError: 'Blocks'
    ```

    If we now add a toy to the `toys` dictionary, it will also be made available in the inventory. This is the **updatable** aspect of a ChainMap.

    ```python
    >>> toys['Nintendo'] = 200
    >>> inventory['Nintendo']
    200
    ```

    A nice feature is that while in our example `toys`, `computers` and `clothing` are all in the same context (the interpreter), they could come from totally *different* modules or packages. This is because ChainMap stores the underlying dictionaries **by reference**.

  - Providing a chain of default values

  - Performance-critical applications that frequently compute subsets of a dictionary

More see:

- [A practical usage of ChainMap in Python](https://florimond.dev/en/posts/2018/07/a-practical-usage-of-chainmap-in-python/)

- [`ChainMap`](https://docs.python.org/3/library/collections.html#collections.ChainMap) objects

## `types.MappingProxyType`

- A wrapper around a standard dictionary that provides a **read-only** view into the wrapped dictionary’s data. It can be used to create **immutable** proxy versions of dictionaries.
- Using `MappingProxyType` allows you to put these read-only restrictions in place without first having to create a full copy of the dictionary

Example

```python
from types import MappingProxyType

writable = {"one": 1, "two": 2}
read_only = MappingProxyType(writable)
```

```python
>>> read_only["one"]
1
```

The proxy is read-only. Trying to modify the proxy will cause an error:

```python
>>> read_only["one"] = 23
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In [19], line 1
----> 1 read_only["one"] = 23

TypeError: 'mappingproxy' object does not support item assignment
```

Updates to the original are reflected in the proxy:

```python
>>> writable["one"] = 42
>>> read_only["one"]
42
```

## Conclusion

If you’re looking for a general recommendation on which mapping type to use in your programs, it is recommended to use the built-in `dict` data type. It’s a versatile and optimized hash table implementation that’s built directly into the core language.

It is ONLY recommended that you use one of the other data types listed here if you have special requirements that go beyond what’s provided by dict.