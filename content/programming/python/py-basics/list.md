---
# ===== Title, summary, and position in the left sidebar =====
linktitle: 
summary: 
weight: 13
# =========================================================

# ========== Basic metadata ==========
title: List
date: 2020-07-08
draft: false
type: book # page type
authors: ["admin"]
tags: ["Python", "Basics"]
categories: ["Coding"]
toc: true # Show table of contents
# ====================================

# ========== Advanced metadata ========== 
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
  caption: ""
  image: ""
---

## Change Value in List Based on Conditions

### E.g. 1

```python
a = ["a", "b", "c", "d", "e"]
b = ["a", "c", "e"]
```

We want a list vector with the same length as `a`. If the element also occurs in `b`, value in the corresponding position is `1`, else `0`.

I.e., target output should be `[1, 0, 1, 0, 1]`

Solution:

```python
l = [1 if el in b else 0 for el in a]
l
```

```
[1, 0, 1, 0, 1]

```

(See also: [https://stackoverflow.com/questions/40769428/how-to-replace-elements-in-list-when-condition-is-met](https://stackoverflow.com/questions/40769428/how-to-replace-elements-in-list-when-condition-is-met)) 

### E.g. 2

```python
a = np.arange(5)
a
```

```
array([0, 1, 2, 3, 4])

```

```python
a[a > 2] = 5
a
```

```
array([0, 1, 2, 5, 5])

```