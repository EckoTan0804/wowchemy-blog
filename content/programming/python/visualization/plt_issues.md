---
linktitle: ''
summary: ''
weight: 503
title: Matplotlib Issues
date: 2022-01-23
draft: false
type: book
authors:
- admin
tags:
- Python
- Visualization
- Matploblib
categories:
- coding
toc: true
profile: false
reading_time: true
share: true
featured: true
comments: true
disable_comment: false
commentable: true
editable: false
header:
  caption: ''
  image: ''
---

Just to mark down some issues I have met when using `matplotlib.pyplot` for plotting. 

## Change global font to Times New Roman

```python
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'DeJavu Serif'
plt.rcParams['font.serif'] = ['Times New Roman']
```

Source: [Matplotlib cannot find basic fonts](https://stackoverflow.com/a/66462451/4891826)