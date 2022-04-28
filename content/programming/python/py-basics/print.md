---
# ===== Title, summary, and position in the left sidebar =====
linktitle: # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 27 # Order in the chapter
# =========================================================

# ========== Basic metadata ==========
title: Print
date: 2022-04-28
draft: false
type: book # page type
authors: 
  - admin
tags: 
  - Python
  - Basics
categories: 
  - Coding
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

`print()` is capable of taking the following arguments:

{{< figure src="https://stackabuse.s3.amazonaws.com/media/python-how-to-print-without-a-newline-space-1.jpg" caption="`print()` function" numbered="true" >}}

- The values (`value1`, `value2`) mentioned above can be any string or any of the data types like list, float, string, etc.
- `sep`: Divides the values given as arguments
- `end`: String appended to the end (`\n` by default)

## Example

```python
arr = [1, 2, 3, 4 ,5]

_ = [print("num", el, sep=": ", end="; ") for el in arr]
```

```txt
num: 1; num: 2; num: 3; num: 4; num: 5; 
```

## Reference

- [Python: How to Print without Newline or Space](https://stackabuse.com/python-how-to-print-without-newline-or-space/)