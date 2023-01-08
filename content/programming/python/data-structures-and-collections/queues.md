---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 215
# ============================================================

# ========== Basic metadata ==========
title: Queues
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

- `collections.deque` is an excellent default choice for implementing a FIFO queue data structure in Python

- `list` objects can be used as queues, but this is generally NOT recommended due to slow performance.

------

A **queue** is a collection of objects that supports fast ***first-in, first-out (FIFO)*** semantics for inserts and deletes. 

The insert and delete operations are sometimes called **enqueue** and **dequeue**. Unlike lists or arrays, queues typically do NOT allow for random access to the objects they contain.

Performance-wise, a proper queue implementation is expected to take $O(1)$ time for insert and delete operations.

## `list` — Terribly Sloooow Queues

It’s possible to use a regular `list` as a queue but this is NOT ideal from a performance perspective. Because inserting or deleting an element at the beginning requires shifting all of the other elements by one, requiring `O(n)` time.

Therefore, it is NOT recommend using a list as a makeshift queue in Python (unless you’re only dealing with a small number of elements). 

## `collections.deque` – Fast & Robust Queues

- A double-ended queue that supports adding and removing elements from either end in $O(1)$ time (non-amortized).
- Implemented as doubly-linked lists
  - Excellent and consistent performance for inserting and deleting elements, 
  - but poor $O(n)$ performance for randomly accessing elements in the middle of the stack.

- Is a great default choice if you’re look- ing for a queue data structure in Python’s standard library.

## `queue.Queue` – Locking Semantics for Parallel Computing

- Synchronized and provides locking semantics to support multiple concurrent producers and consumers.

#### Example

```python
>>> from queue import Queue
>>> q = Queue()
>>> q.put('eat')
>>> q.put('sleep')
>>> q.put('code')

>>> q
<queue.Queue object at 0x1070f5b38>

>>> q.get()
'eat'
>>> q.get()
'sleep'
>>> q.get()
'code'
>>> q.get_nowait()
queue.Empty
>>> q.get()
# Blocks / waits forever...
```

## `multiprocessing.Queue` – Shared Job Queues

- A shared job queue implementation that allows queued items to be processed in parallel by multiple concurrent workers.
- Makes it easy to distribute work across multiple processes in order to work around the GIL limitations.
- Can store and transfer any pickle-able object across process boundaries.

#### Example

```python
>>> from multiprocessing import Queue
>>> q = Queue()
>>> q.put('eat')
>>> q.put('sleep')
>>> q.put('code')

>>> q
<multiprocessing.queues.Queue object at 0x1081c12b0>

>>> q.get()
'eat'
>>> q.get()
'sleep'
>>> q.get()
'code'
>>> q.get()
# Blocks / waits forever...
```

