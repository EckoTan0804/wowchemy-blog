---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 19
# ============================================================

# ========== Basic metadata ==========
title: Sorting
date: 2022-05-02
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - Basics
  - Sorting
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

Python provides two built-in functions for sorting:

- `list.sort()`: modifies the list in-place
- `sorted()`: builds a new sorted list from an iterable

Difference between these methods:

- [`list.sort()`](https://docs.python.org/3/library/stdtypes.html#list.sort) method is only defined for lists. In contrast, the [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) function accepts any iterable.
- `list.sort()` modifies the list *in-place* and returns `None`. `sorted()` returns a new sorted list. Usually `sort()` is less convenient than `sorted()`.

## Sorting Basics

A simple ascending sort is very easy: just call the [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) function. It returns a new sorted list.

Example

```python
>>> a = [5, 2, 1, 3, 4]
>>> b = sorted(a)

>>> a # the original list is not affected
[5, 2, 1, 3, 4]

>>> b
[1, 2, 3, 4, 5]

```

## Key

Both [`list.sort()`](https://docs.python.org/3/library/stdtypes.html#list.sort) and [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) have a `key` parameter.

The value of the `key` parameter should be a function (or other callable) that serves as a key for the sort comparison. In other word, `key` decides the comparison criteria for sorting.

One way to specify `key` is to use the lambda function.

Example:

```python
students_dict = [
    {"name": "John", "age": 12, "grade": "A"},
    {"name": "Mary", "age": 14, "grade": "B"},
    {"name": "Ben", "age": 13, "grade": "A"}
]

sorted(students_dict, key=lambda student: student.get("age")) # sort by age
```

Output:

```txt
[{'age': 12, 'grade': 'A', 'name': 'John'},
 {'age': 13, 'grade': 'A', 'name': 'Ben'},
 {'age': 14, 'grade': 'B', 'name': 'Mary'}]
```

This also works for objects with named attributes.

Example:

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def __repr__(self):
        return repr((self.name, self.age, self.grade))

students = [
    Student("John", 12, "A"),
    Student("Mary", 14, "B"),
    Student("Ben", 13, "A")
]
```

```python
sorted(students, key=lambda student: student.age)
```

Output:

```txt
[('John', 12, 'A'), ('Ben', 13, 'A'), ('Mary', 14, 'B')]
```

### Operator Module Functions

Python `operator` module provides convenience functions to make accessor functions easier and faster: 

- `itemgetter()`
- `attrgetter()`
- `methodcaller()`

#### `itemgetter()`

Example:

```python
students_tuple = [
    ("John", 12, "A"),
    ("Mary", 14, "B"),
    ("Ben", 13, "A")            
]

sorted(students_tuple, key=itemgetter(1))
```

Output:

```txt
[('John', 12, 'A'), ('Ben', 13, 'A'), ('Mary', 14, 'B')]
```

```python
students_dict = [
    {"name": "John", "age": 12, "grade": "A"},
    {"name": "Mary", "age": 14, "grade": "B"},
    {"name": "Ben", "age": 13, "grade": "A"}
]

sorted(students_dict, key=itemgetter("age"))
```

Output:

```txt
[{'age': 12, 'grade': 'A', 'name': 'John'},
 {'age': 13, 'grade': 'A', 'name': 'Ben'},
 {'age': 14, 'grade': 'B', 'name': 'Mary'}]
```

#### `attrgetter()`

Example:

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def __repr__(self):
        return repr((self.name, self.age, self.grade))

students = [
    Student("John", 12, "A"),
    Student("Mary", 14, "B"),
    Student("Ben", 13, "A")
]
```

```txt
[('John', 12, 'A'), ('Ben', 13, 'A'), ('Mary', 14, 'B')]
```


## order

Both [`list.sort()`](https://docs.python.org/3/library/stdtypes.html#list.sort) and [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) accept a *reverse* parameter with a boolean value. This is used to flag descending sorts" `reverse=False` and `reverse=True` represent ascending and descening order, respectively.

## Advance

### Multiple levels of sorting

Multiple level of sorting can be easily achieved with [operator module functions](#operator-module-functions).

For example, to sort by `grade` then by `age`:

```python
>>> sorted(students_tuple, key=itemgetter(2, 1))
[('John', 12, 'A'), ('Ben', 13, 'A'), ('Mary', 14, 'B')]
```

```python
>>> sorted(students, key=attrgetter("grade", "age"))
[('John', 12, 'A'), ('Ben', 13, 'A'), ('Mary', 14, 'B')]
```

```python
>>> sorted(students_dict, key=itemgetter("grade", "age"))
[{'age': 12, 'grade': 'A', 'name': 'John'},
 {'age': 13, 'grade': 'A', 'name': 'Ben'},
 {'age': 14, 'grade': 'B', 'name': 'Mary'}]
```

## Reference

- [Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)