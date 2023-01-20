---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 24
# ============================================================

# ========== Basic metadata ==========
title: Looping and Iterations
date: 2023-01-14
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - Basics
  - Looping
  - Iteration
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

- Iterators provide a sequence interface to Python objects that’s memory efficient and considered Pythonic.
- To support iteration an object needs to implement the iterator protocol by providing the `__iter__` and `__next__` dunder methods.

------

## Writing Pythonic Loops

in Python, for-loops are really “**for-each**” loops that can iterate directly over items from a container or sequence, without having to look them up by index.

Example:

```python
my_items = ['a', 'b', 'c']

for item in my_items:
    print(item)
```

Advantages

- Remains nice and clean and almost reads like pseudo code from a programming textbook
- We don't need to take care of the container's size and looping index
- The container itself now takes care of handing out the elements so they can be processed.
  - If the container is ordered, the resulting sequence of elements will be too. 
  - If the container isn’t ordered, it will return its elements in arbitrary order but the loop will still cover all of them.

If we need to keep track of the running index, we can use the **`enumerate()`** built-in.

Example:

```python
for i, item in enumerate(my_items):
    print(f"{i}: {item}")
```

If we inevitablely need to write a Java- or C-style loop (e.g., we must contrl the step size for the index),:

```java
for (int i = a; i < n; i += s) { 
    // ...
}
```

We can make use of the `range()` function: it accepts optional parameters to control the start value for the loop (`a`), the stop value (`n`), and the step size (`s`).

```python
for i in range(a, n, s):
    # ...
```

## Comprehensions

Comprehensions are a key feature in Python. Under the hood, comprehension are for`-loops over a collection but expressed in a more terse and compact syntax.

```python
# list comprehension
values = [expression for item in collection]
```

It is equivalent to

```python
# plain for-loop
values = []
for item in collection:
    values.append(expression)
```

List comprehensions can filter values based on some arbitrary condi- tion that decides whether or not the resulting value becomes a part of the output list.

```python
values = [expression
          for item in collection
          if condition]
```

Example:

```python
>>> even_squares = [x * x for x in range(10) if x % 2 == 0]
>>> even_squares
[0, 4, 16, 36, 64]
```

Python also supports comprehensions for *sets* and *dictionaries*.

Set comprehension:

```python
>>> { x * x for x in range(-9, 10) }
set([64, 1, 36, 0, 49, 9, 16, 81, 25, 4])
```

{{% callout note %}}
Unlike lists, which retain the order of the elements in them, Python sets are an unordered collection type.
{{% /callout %}}

Dictionary comprehension:

```python
>>> { x: x * x for x in range(5) } 
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

{{% callout  warning %}}
As you get more proficient at using them, it becomes easier and easier to write code that’s difficult to read. If you’re not careful, you might have to deal with monstrous list, set, and dict comprehensions soon.

Remember, too much of a good thing is usually a bad thing. And readabilty always has the first priority!

{{% /callout %}}

## List Slicing Tricks

List slicing

- We can view it as an extension of the square-brackets indexing syntax
- Commonly used to access ranges of elements within an ordered col- lection.

List slicing pattern

```python
list[start:stop:step]
```

**Note: To avoid off-by-one errors, the upper bound `stop` is always *exclusive***.

Example

```python
>>> lst = [1, 2, 3, 4, 5]
>>> lst
[1, 2, 3, 4, 5]

# lst[start:end:step]
>>> lst[1:3:1]
[2, 3]
```

Tricks with step parameter (a.k.a. stride)

- If you leave out the step size, it defaults to one.

  ```python
  >>> lst[1:3]
  [2, 3]
  ```

- You can also control the step size to skip element.

  ```python
  >>> lst[::2]
  [1, 3, 5]
  ```

- If you ask for a [::-1] slice, you’ll get a copy of the original list, but in the reverse order:

  ```python
  >>> numbers[::-1]
  [5, 4, 3, 2, 1]
  ```

  This is pretty neat, but in most cases we should still stick with `list.reverse()` and the built-in `reversed()` function to reverse a list.

You can use the `:`-operator to clear all elements from a list without destroying the list object itself.

```python
>>> lst = [1, 2, 3, 4, 5]
>>> del lst[:]
>>> lst
[]
```

{{% callout note %}}
In Python 3 you can also use `lst.clear()` for the same job, which might be the more readable patter.
{{% /callout %}}

Besides clearing lists, you can also use slicing to replace all elements of a list without creating a new list object.

```python
>>> original_lst = lst
>>> lst[:] = [7, 8, 9]
>>> lst
[7, 8, 9]
>>> original_lst
[7, 8, 9]
```

Another use case for hte `:`-operator creating (shallow) copies of existing lists:

```python
>>> copied_lst = lst[:]
>>> copied_lst
[7, 8, 9]
>>> copied_lst is lst
False
```

## Beautiful Iterators

According to Python's *iterator protocol*: Objects that support the `__iter__` and `__next__` dunder methods automatically work with for-in loops.

To understand how iterators work under the hood, let's take a look at an example.

```python
class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value
```

The two dunder method, `__iter__` and `__next__`, are the keys to making a Python object iterable.

```python
repeater = Repeater("Hello")

for item in repeater:
    print(item)
```

You will see lots of `"Hello"` printed to the screen, and this loop will never complete. But in other words, this iterator works!

To dispel some of that “magic,” we can expand this loop into a slightly longer code snippet that gives the same result:

```python
repeater = Repeater('Hello')
iterator = repeater.__iter__()
while True:
    item = iterator.__next__()
    print(item)
```

As we can see, the `for-in` was just syntactic sugar for a simple while loop:

- It first prepared the `repeater` object for iteration by calling its `__iter__` method → This returns the *actual iterator object*.
- Then the loop repeatedly called the iterator object's `__next__` method to retrieve values from it.

<span style="color:  ForestGreen">(Because there’s never more than one element “in flight,” this approach is highly memory-efficient.)</span>

On more abstract terms, iterators provide a common interface that allows you to process every element of a container while being *completely isolated* from the container’s internal structure. 

→ In other words, whether you’re dealing with a list of elements, a dictionary, or an infinite sequence, it does not matter, because every single one of these objects can be traversed in the same way with the power iterators.

We can also manually "emulate" how the loop uses the iterator protocol:

```python
>>> repeater = Repeater('Hello')
>>> iterator = iter(repeater)
>>> next(iterator)
'Hello'
>>> next(iterator)
'Hello'
>>> next(iterator)
'Hello'
```

> Notice that here we replace the `__iter__` and `__next__` with Python's built-in functions, `iter()` and `next()`.
>
> - Internally, these built-ins invoke the same dunder methods, but they make this code a little prettier and easier to read by providing a clean “facade” to the iterator protocol.
> - Python offers these facades for other functionality as well. E.g.
>   - `len(x)` is a shortcut for calling `x.__len__`.
> - Generally, it’s a good idea to use the built-in facade functions rather than directly accessing the dunder methods implementing a protocol. It just makes the code a little easier to read.

### A simple iterator

In the previous example, `Repeater` and `RepeaterIterator` correpsonded directly to the two phases used by Python's iterator protocol:

1. `Repeater` : setting up and retrieving the iterator object with an `iter()` call,
2. `RepeaterIterator`: repeatedly fetching values from it via `next()`.

Both of these responsibilities can be shouldered by a single class. it doesn’t really matter where `__next__` is defined. **In the iterator protocol, all that matters is that `__iter__` returns any object with a `__next__` method on it.**

→ We can add the `__next__` method directly to the `Repeater` class!

```python
class SimpleRepeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value
```

### Iterators that can stop

**Iterators use exceptions to structure control flow. To signal the end of iteration, a Python iterator simply raises the built-in `StopIteration` exception.**

Python iterators normally can NOT be “reset”—once they’re exhausted they’re supposed to raise `StopIteration` every time next() is called on them. To iterate anew you’ll need to request a fresh iterator object with the `iter()` function.

Having this idea in mind, we can implement a `BoundedRepeater` that will stop after a predefined number of repetitions:

```python
class BoundedRepeater:
    def __init__(self, value, max_reps):
        self.value = value
        self.max_reps = max_reps
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_reps:
            raise StopIteration
        self.count += 1
        return self.value
```

```python
>>> repeater = BoundedRepeater('Hello', 3)
>>> for item in repeater:
        print(item)
Hello
Hello 
Hello
```

