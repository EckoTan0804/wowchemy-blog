---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 216
# ============================================================

# ========== Basic metadata ==========
title: Priority Queues
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

- `queue.PriorityQueue` stands out from the pack with a nice object-oriented interface and a name that clearly states its in- tent. It should be your preferred choice.
- If you’d like to avoid the locking overhead of `queue.PriorityQueue`, using the `heapq` module directly is also a good option.

------

A **priority queue** is a container data structure that manages a set of records with *totally-ordered* keys (e.g., a numeric weight value) to provide quick access to the record with the smallest or largest key in the set.

> We can think of a priority queue as a modified queue: instead of retrieving the next element by insertion time, it retrieves the highest-priority element. The priority of individual elements is decided by the ordering applied to their keys.

Priority queues are commonly used for dealing with scheduling problems.

## `list` – Maintaining a Manually Sorted Queue

You can use a sorted list to quickly identify and delete the smallest or largest element. 

<span style="color: Red">Downsides</span>

- <span style="color: Red">Inserting new elements into a list is a slow $O(n)$ operation.</span>
- <span style="color: Red">You must *manually* take care of re-sorting the list when new elements are inserted. It’s easy to introduce bugs by missing this step.</span>

## `heapq` – List-Based Binary Heaps

- A binary heap implementation usually backed by a plain `list`, and it supports insertion and extraction of the smallest element in $O(log n)$ time.
- A good choice for implementing priority queues in Python.
- Extra steps must be taken to ensure sort stability and other features typically expected from a “practical” priority queue.

#### Example

```python
import heapq
q = []
heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))

while q:
    next_item = heapq.heappop(q)
    print(next_item)
    
# Result:
# (1, 'eat')
# (2, 'code')
#   (3, 'sleep')
```

## `queue.PriorityQueue` – Beautiful Priority Queues

- Uses `heapq` internally and shares the same time and space complexities
- Is synchronized and provides locking semantics to support multiple concurrent producers and consumers.
- You might prefer the class-based interface provided by `PriorityQueue` over using the function-based interface provided by `heapq`.

#### Example

```python
from queue import PriorityQueue
q = PriorityQueue()
q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

while not q.empty():
    next_item = q.get()
    print(next_item)
    
# Result:
# (1, 'eat')
# (2, 'code')
#   (3, 'sleep')
```

