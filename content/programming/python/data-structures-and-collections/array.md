---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 211
# ============================================================

# ========== Basic metadata ==========
title: Array Data Structure
date: 2023-01-04
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

- You need to store arbitrary objects, potentially with mixed data types? $\rightarrow$ Use `list` (mutable) or `tuple` (immutable)
- You have numeric (integer or floating point) data and tight packing and performance is important? $\rightarrow$ Try `array.array`. Also consider going beyond the standard library and try out packages like `NumPy` or `Pandas`.
- You have textual data represented as Unicode characters?  $\rightarrow$ Use Python’s built-in `str`. If you need a “mutable string,” use a list of characters.
- You want to store a contiguous block of bytes? $\rightarrow$ Use `byte` (immutable) or `bytearray` (mutable).

In most cases, start out with a simple list. Only specialize later on if performance or storage space becomes an issue. (Most of the time, using a general-purpose array data structure like `list` gives you the fastest development speed and the most programming conve- nience.)



------

Arrays consist of *fixed-size* →records that allow each element to be efficiently located based on its *index*. Arrays store information in adjoining blocks of memory, therefore they’re considered *contiguous* data structures (as opposed to *linked* datas structure like linked lists, for example.)

Performance-wise, it’s very fast to look up an element contained in an array given the element’s index. A proper array implementation guarantees a constant *O(1)* access time for this case.

## `list` – Mutable Dynamic Arrays

Python’s lists are implemented as *dynamic arrays*. $\rightarrow$ A list allows elements to be added or removed, and the list will *automatically* adjust the backing store that holds these elements by allocating or releasing memory.

Python lists can hold *arbitrary* elements. Therefore, you can mix and match different kinds of data types and store them all in a single list. However, <span style="color: Red">the downside is that supporting multiple data types at the same time means that data is generally less tightly packed</span>.

Example:

```python
>>> arr = ['one', 'two', 'three'] 
>>> arr[0]
'one'

# Lists have a nice repr:
>>> arr
['one', 'two', 'three']

# Lists are mutable:
>>> arr[1] = 'hello'
>>> arr
['one', 'hello', 'three']

>>> del arr[1] 
>>> arr
['one', 'three']

# Lists can hold arbitrary data types:
>>> arr.append(23) 
>>> arr
['one', 'three', 23]
```

## `tuple` - Immutable Containers

Python’s tuple objects are ***immutable***. 

- Elements can NOT be added or removed dynamicall.
- All elements in a tuple must be defined at creation time.

Just like lists, tuples can hold elements of arbitrary data types.

Example:

```python
>>> t = ("one", "two", "three")
>>> t
('one', 'two', 'three')

>>> t[0]
"one"

# Tuples are immutable:
>>> t[1] = "Hello"
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In [3], line 1
----> 1 t[1] = "Hello"

TypeError: 'tuple' object does not support item assignment

>>> del t[1]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In [4], line 1
----> 1 del t[1]

TypeError: 'tuple' object doesn't support item deletion

# Tuples can hold arbitrary data types:
# (Adding elements creates a copy of the tuple)
>>> t + (23, )
('one', 'two', 'three', 23)
```

## `array.array` - Basic Typed Arrays

Python’s array module provides space-efficient storage of basic C- style data types like bytes, 32-bit integers, floating point numbers, etc.

Arrays created with the `array.array` class

- mutable
- behave similarly to lists
- “typed arrays” constrained to a **single** data type $\rightarrow$ more space-efficient than lists and tuples. This can be useful if you need to store many elements of the same type.

Example:

```python
>>> import array
>>> arr = array.array('f', (1.0, 1.5, 2.0, 2.5))
>>> arr[1]
1.5


# Arrays are mutable:
>>> arr[1] = 23.0
>>> arr
array('f', [1.0, 23.0, 2.0, 2.5])

>>> del arr[1]
>>> arr
array('f', [1.0, 2.0, 2.5])

>>> arr.append(42.0)
>>> arr
array('f', [1.0, 2.0, 2.5, 42.0])


# Arrays are "typed":
>>> arr[1] = 'hello'
TypeError: "must be real number, not str"
```

## `str` - Immutable Arrays of Unicode Characters

A str is an ***	immutable*** array of characters.

- It’s also a recursive data structure—each character in a string is a `str` object of length 1 itself.

String objects are **space-efficient** because they’re tightly packed and they specialize in a single data type.

Example:

```python
>>> arr = 'abcd'
>>> arr[1]
'b'

>>> arr
'abcd'


# Strings are immutable:
>>> arr[1] = 'e'
TypeError:
"'str' object does not support item assignment"

>>> del arr[1]
TypeError:
"'str' object doesn't support item deletion"


# Strings can be unpacked into a list to
# get a mutable representation:
>>> list('abcd')
['a', 'b', 'c', 'd']
>>> ''.join(list('abcd'))
'abcd'


# Strings are recursive data structures:
>>> type('abc')
"<class 'str'>"
>>> type('abc'[0])
"<class 'str'>"
```

## `bytes` – Immutable Arrays of Single Bytes

Bytes objects are ***immutable*** sequences of single bytes (integers in the range of `0<=x<=255`).

They are similar to `str` objects and they are also space-efficient. But unlike strings, there’s a dedicated “mutable byte array” data type called `bytearray` that they can be unpacked into.

Example:

```python
>>> arr = bytes((0, 1, 2, 3))
>>> arr[1]
1


# Bytes literals have their own syntax:
>>> arr
b'x00x01x02x03'
>>> arr = b'x00x01x02x03'


# Only valid "bytes" are allowed:
>>> bytes((0, 300))
ValueError: "bytes must be in range(0, 256)"


# Bytes are immutable:
>>> arr[1] = 23
TypeError:
"'bytes' object does not support item assignment"
>>> del arr[1]
TypeError:
"'bytes' object doesn't support item deletion"
```

## `bytearray` – Mutable Arrays of Single Bytes

- The `bytearray` type is a ***mutable*** sequence of integers in the range `0 <= x <= 255`.
- They’re closely related to bytes objects. But they can be modified freely — you can overwrite elements, remove existing elements, or add new ones. The `bytearray` object will grow and shrink accordingly.
- Bytearrays can be converted back into immutable bytes objects. But this involves copying the stored data in full—a slow operation taking $O(n)$ time.

Example:

```python
>>> arr = bytearray((0, 1, 2, 3))
>>> arr[1]
1


# The bytearray repr:
>>> arr
bytearray(b'x00x01x02x03')


# Bytearrays are mutable:
>>> arr[1] = 23
>>> arr
bytearray(b'x00x17x02x03')
>>> arr[1] 
23


# Bytearrays can grow and shrink in size:
>>> del arr[1]
>>> arr
bytearray(b'x00x02x03')
>>> arr.append(42)
>>> arr
bytearray(b'x00x02x03*')


# Bytearrays can only hold "bytes"
# (integers in the range 0 <= x <= 255) 
>>> arr[1] = 'hello'
TypeError: "an integer is required"
>>> arr[1] = 300
ValueError: "byte must be in range(0, 256)"


# Bytearrays can be converted back into bytes objects: # (This will copy the data)
>>> bytes(arr)
b'x00x02x03*'
```

