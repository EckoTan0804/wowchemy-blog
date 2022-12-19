---
# ===== Title, summary, and position in the left sidebar =====
linktitle: 
summary: 
weight: 291
# =========================================================

# ========== Basic metadata ==========
title: "[Issues] List"
date: 2020-07-08
draft: false
type: book # page type
authors: ["admin"]
tags: ["Python", "Basics", "Data Structure"]
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

#### E.g. 1

```python
>>> a = ["a", "b", "c", "d", "e"]
>>> b = ["a", "c", "e"]
```

We want a list vector with the same length as `a`. If the element also occurs in `b`, value in the corresponding position is `1`, else `0`.

I.e., target output should be `[1, 0, 1, 0, 1]`

Solution:

```python
>>> l = [1 if el in b else 0 for el in a]
>>> l
```

```
[1, 0, 1, 0, 1]
```

(See also: [https://stackoverflow.com/questions/40769428/how-to-replace-elements-in-list-when-condition-is-met](https://stackoverflow.com/questions/40769428/how-to-replace-elements-in-list-when-condition-is-met)) 

#### E.g. 2

```python
>>> a = np.arange(5)
>>> a
```

```
array([0, 1, 2, 3, 4])
```

```python
>>> a[a > 2] = 5
>>> a
```

```
array([0, 1, 2, 5, 5])
```

## List Comprehension

Define the list and its contents at the same time by following this format:

```python
new_list = [expression for member in iterable]
```

- **expression**: the member itself, a call to a method, or any other valid expression that returns a value.
- **member**: the object or value in the list or iterable
- **iterable**: a list, [set](https://realpython.com/python-sets/), sequence, [generator](https://realpython.com/introduction-to-python-generators/), or any other object that can return its elements one at a time

#### Example

Get the even numbers in 0 to 10 (10 is not inlcuded):

```python
>>> even_nums = [el for el in range(10) if el % 2 == 0]
>>> even_nums
```

```txt
[0, 2, 4, 6, 8]
```

#### Advantages

- More pythonic
- More declarative than loops: list comprehensions are easier to read and understand

#### Combined with conditional logic

- **Simple filtering**: Place the conditional to the *end*

  ```python
  new_list = [expression for member in iterable (if conditional)]
  ```

  Here, the conditionals allow list comprehensions to filter out unwanted values.

- **Change a member value**: Place the conditional *near the beginning*

  ```python
  new_list = [expression (if conditional) for member in iterable]
  ```

  - Example: Change all odd numbers in 0 - 10 to 0

    ```python
    >>> arr = [el if el % 2 == 0 else 0 for el in range(10)]
    >>> arr
    [0, 0, 2, 0, 4, 0, 6, 0, 8, 0]
    ```

#### Nested list comprehension

Nested List Comprehensions are nothing but a list comprehension within another list comprehension which is quite similar to nested for loops.

{{< spoiler text="Example" >}} 

Let's say we want to obtain all possible combination of two lists: `a = [1, 2, 3]` and `b = [4, 5]`.

Use list comprehension:

```python
>>> combinations = [[i, j] for j in b for i in a]
>>> combinations
[[1, 4], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5]]
```

This is equvalent to nested loops:

```python
combinations = []

for i in a:
    for j in b:
        combinations.append([i, j])

```

Apparently, using list comprehension is more succinct and more pythonic.

{{< /spoiler >}}

#### Reference

- [When to Use a List Comprehension in Python](https://realpython.com/list-comprehension-python/)

## Print Lists

#### Using `for`-loop

```python
a = [1, 2, 3, 4, 5]
for x in a:
    print(x)
```

Output:

```txt
1
2
3
4
5
```

#### Using `* ` symbol

```python
>>> a = [1, 2, 3, 4, 5]
>>> print(*a)
1 2 3 4 5
```

Using this way, we can also easily control the separator and ending.

```python
>>> print(*a, sep=", ") # print list separted by comma
1, 2, 3, 4, 5
```

```python
print(*a, sep="\n") # print list in new line
```

Output:

```txt
1
2
3
4
5
```

#### Convert list to string for display

If it is a list of strings we can simply join them using [join()](https://www.geeksforgeeks.org/python-string-methods-set-2-len-count-center-ljust-rjust-isalpha-isalnum-isspace-join/) function.

```python
>>> a = ["Hello", "World"]
>>> print(" ".join(a))
Hello World
```

#### Reference

- [Print lists in Python (4 Different Ways)](https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/)

## List Comprehension Vs. `*`-operator

List comprehension and using the `*`-operator are two common methods to create list containing repeating elements. However, there is a minor difference between them, which is often overlooked and may cause unexpected bug.

- The `*`-operator can NOT make independent objects 
  - Reason:  the multiplication operator `*` operates on objects, without seeing expressions.
  - *E.g.*: `[x] * 3` creates a list `[x, x, x]`, which is essentially a list with 3 references to the **same** `x`. *I.e.,* when you modify one single `x`, all references will be modified.
- List comprehension can make independent objects
  - It re-evaluates the element expression on every iteration. Every evaluation generates a new **independent** object. *I.e.*, Modifying one of them will not affect the others.
  - *E.g.*: `[x for _ in range(3)]` creates a like `[x, copy.copy(x), copy.copy(x)]`

Using the `*`-operator may be inconsistent. In contrast, list comprehension would be a safer option.

#### Example 1: List containing objects

```python
class Student:

    def __init__(self, age):
        self.age = age
```

Create list with `*`:

```python
>>> students = [Student(12)] * 3
>>> _ = [print(student.age) for student in students]
12
12
12
```

As is essentially a list with 3 references to the **same** `Student`, modifying one of them will affect others.

```python
>>> students[0].age = 15
>>> _ = [print(student.age) for student in students]
15
15
15
```

In contrast, using list comprehension will create a list containing three independent `Student`s.

```python
>>> students = [Student(12) for _ in range(3)]
>>> _ = [print(student.age) for student in students]
12
12
12
```

Modifying one of them will NOT affect others:

```python
>>> students[0].age = 15
>>> _ = [print(student.age) for student in students]
15
12
12
```

#### Example 2: Multidimensional Array/List

Using `*`-operator:

```python
>>> matrix = [[0, 0]] * 2
>>> matrix
[[0, 0], [0, 0]] # Two reference to the same [0, 0]
>>> matrix[0][1] = 1
>>> matrix
[[0, 1], [0, 1]]
```

Using list comprehension:

```python
>>> matrix = [[0] * 2 for _ in range(2)]
>>> matrix
[[0, 0], [0, 0]] # Two independent [0, 0]
>>> matrix[0][1] = 1
>>> matrix
[[0, 1], [0, 0]]
```



#### Reference

- [List of lists changes reflected across sublists unexpectedly](https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly)