---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 214
# ============================================================

# ========== Basic metadata ==========
title: Stacks
date: 2023-01-08
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

- `collections.deque` provides a safe and fast general-purpose stack implementation. First choice!
- The built-in `list` type can be used as a stack, but be careful to only append and remove items with `append()` and `pop()` in order to avoid slow performance.
- Use `queue` module for parallel processing cases

------

A **stack** is a collection of objects that supports fast ***last-in, first-out (LIFO***) semantics for inserts and deletes. 

The insert and delete operations are also often called *push* and *pop*. Performance-wise, a proper stack implementation is expected to take *O(1)* time for insert and delete operations.

## `list` – Simple, Built-In Stacks

Python’s built-in `list` type makes a decent stack data structure as it supports push and pop operations in amortized $O(1)$ time. To get the amortized $O(1)$ performance for inserts and deletes, new items must be added to the end of the list with the `append()` method and removed again from the end using `pop()`.

For optimum performance, stacks based on Python lists should grow towards *higher* indexes and shrink towards *lower* ones. Adding and removing from the front is much slower and takes O(n) time, as the existing elements must be shifted around to make room for the new element. This is a performance antipattern that you should avoid as much as possible!

#### Example

```python
>>> s = []
>>> s.append('eat')
>>> s.append('sleep')
>>> s.append('code')

>>> s
['eat', 'sleep', 'code']

>>> s.pop()
'code'
>>> s.pop()
'sleep'
>>> s.pop()
'eat'
>>> s.pop()
IndexError:
"pop from empty list"
```

## `collections.deque` – Fast & Robust Stacks

The `deque` class implements a *double-ended* queue that supports adding and removing elements from either end in $O(1)$ time (non-amortized). $\rightarrow$ `deque` can serve both as queues and as stacks.

Python’s `deque` objects have excellent and consistent performance for inserting and deleting elements, but poor $O(n)$ performance for randomly accessing elements in the middle of a stack.

Overall, collections.deque is a great choice if you’re looking for a stack data structure in Python’s standard library :clap:.

#### Example

```python
>>> from collections import deque
>>> s = deque()
>>> s.append('eat')
>>> s.append('sleep')
>>> s.append('code')

>>> s
deque(['eat', 'sleep', 'code'])

>>> s.pop()
'code'
>>> s.pop()
'sleep'
>>> s.pop()
'eat'
>>> s.pop()
IndexError:
"pop from an empty deque"
```

## `queue.LifoQueue` – Locking Semantics for Parallel Computing

This stack implementation in the Python standard library is *synchronized* and provides *locking* semantics to support multiple concurrent producers and consumers.

{{% callout note %}}
Besides LifoQueue, the queue module contains several other classes that implement multi-producer/multi-consumer queues that are use- ful for parallel computing.
{{% /callout %}}

Depending on your use case, the locking semantics might be helpful, or they might just incur unneeded overhead. In this case you’d be better off with using a list or a deque as a general-purpose stack.

#### Example

```python
>>> from queue import LifoQueue
>>> s = LifoQueue()
>>> s.put('eat')
>>> s.put('sleep')
>>> s.put('code')

>>> s
<queue.LifoQueue object at 0x108298dd8>
>>> s.get()
'code'
>>> s.get()
'sleep'
>>> s.get()
'eat'

>>> s.get_nowait()
queue.Empty
>>> s.get()
# Blocks / waits forever...
```

## Stack Implementations Comparison

If you’re not looking for parallel processing support (or don’t want to handle locking and unlocking manually), your choice comes down to the built-in `list` type or `collections.deque`.

Difference between `list` and `collections.deque`:

- `list` is backed by a dynamic array which makes it great for fast random access, but requires occasional resizing when elements are added or removed. 
  - You get an amortized $O(1)$ time complexity for push and pop operations.
  -  But you do need to be careful to only insert and remove items “from the right side” using `append()` and `pop()`. Otherwise, perfor- mance slows down to $O(n)$.
- `collections.deque` is backed by a doubly-linked list which optimizes appends and deletes at both ends and provides consistent $O(1)$ performance for these operations.
  - More stable performance and also easier to use (you don’t have to worry about adding or removing items from “the wrong end.”)

In summary: `collections.deque` is an excellent choice for implementing a stack (LIFO queue) in Python.

