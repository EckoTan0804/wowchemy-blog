---
# Title, summary, and position in the list
linktitle: "📖 DL with PyTorch"
summary: Summary of the book 'Deep Learning with PyTorch' officially released by PyTorch.
weight: 200

# Basic metadata
title: "Deep Learning with PyTorch"
date: 2020-10-18
draft: false
type: book # page type
authors: ["admin"]
tags: ["Deep Learning", "PyTorch", "DL-with-PyTorch"]
categories: ["Deep Learning"]
toc: true # Show table of contents?

# Advanced metadata
profile: false  # Show author profile?

reading_time: true # Show estimated reading time?
share: true  # Show social sharing links?
featured: true

comments: true  # Show comments?
disable_comment: false
commentable: false  # Allow visitors to comment? Supported by the Page, Post, and Docs content types.

editable: false  # Allow visitors to edit the page? Supported by the Page, Post, and Docs content types.

# Optional header image (relative to `static/img/` folder).
header:
  caption: ""
  image: ""
---

## Book

[Deep Learning with PyTorch](https://pytorch.org/deep-learning-with-pytorch)

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/deep-learning-thumbnail.png" alt="img" style="zoom:50%;" />

## Code

- [Github repo](https://github.com/deep-learning-with-pytorch/dlwpt-code)

- Almost all of our example notebooks contain the following boilerplate in the first cell (some lines may be missing in early chapters)

  ```python
  %matplotlib inline
  from matplotlib import pyplot as plt
  import numpy as np
  import torch
  import torch.nn as nn
  import torch.nn.functional as F 
  import torch.optim as optim
  
  torch.set_printoptions(edgeitems=2) 
  torch.manual_seed(123)
  ```

- Convention
  - Variables named with a `_t` suffix are tensors stored in CPU memory, 
  - Variables named with a `_g` suffix are tensors in GPU memory
  - Variables named with a `_a` suffix  are NumPy arrays.