---
linktitle: ''
summary: ''
weight: 304
title: Numpy Tile
date: 2020-11-22
draft: false
type: book
authors:
- admin
tags:
- Python
- Numpy
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

```python
x = np.array([[1, 2],
              [3, 4]])
print(x)
print(x.shape)
```

```
[[1 2]
 [3 4]]
(2, 2)
```

```python
x1 = np.tile(x, (1, 2))
print(x1)
print(x1.shape)
```

```
[[1 2 1 2]
 [3 4 3 4]]
(2, 4)
```

{{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/np-tile.png" title="Numpy tile" numbered="true" >}}

## Reference

- [numpy tile documentation](https://numpy.org/doc/stable/reference/generated/numpy.tile.html)

- {{< youtube 9BjmmK61pjI >}}