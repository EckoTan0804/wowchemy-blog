---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 217
# ============================================================

# ========== Basic metadata ==========
title: Dictionary Tricks
date: 2023-02-04
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

## Sorting Dictionary

Python dictionaries don’t have an inherent order. You can iterate over them just fine but there’s no guarantee that iteration returns the dictionary’s elements in any particular order。

However, it is frequently useful to get a *sorted* representation of a dictionary to put the dictionary’s items into an arbitrary order based on their key, value, or some other derived property.

To sort a dictionary, we can apply the built-in  `sorted()` function on the items. E.g.:

```python
xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
```

```python
>>> sorted(xs.items())
[('a', 4), ('b', 3), ('c', 2), ('d', 1)]
```

The key/value tuples are ordered using Python’s standard lexicographical ordering for comparing sequences.

**To get complete control over how items are ordered, we can specify the `key` argument of the `sorted()` function.** 

E,g,, sort by value:

```python
>>> sorted(xs.items(), key=lambda x: x[1]) 
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
```

Another apporach i to use the Python built-in `operator` module. This module implements some of the most frequently used key funcs as plug-and-play building blocks, such as `operator.itemgetter` and `operator.attrgetter`.

Example: replace the lambda-based index lookup with `operator.itemgetter`:

```python
>>> import operator
>>> sorted(xs.items(), key=operator.itemgetter(1)) 
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
```

Using the operator module might communicate your code’s intent more clearly in some cases. On the other hand, using a simple lambda expression might be just as readable and more explicit. Another benefit of using lambdas as a custom key func is that you get to control the sort order in much finer detail. 

To reverse the sort order, we can use the `reverse=True` keyword argument.

Example:

```python
>>> sorted(xs.items(),
           key=lambda x: x[1],
           reverse=True)
[('a', 4), ('b', 3), ('c', 2), ('d', 1)]
```

## Emulating Switch/Case Statements With Dicts

Python doesn’t have switch/case statements so it’s sometimes neces- sary to write long `if...elif...else` chains as a workaround. Long `if` chains tend to be a code smell that makes programs more difficult to read and maintain.

One way to deal with long `if...elif...else` statements is to **replace them with dictionary lookup tables that emulate the behavior of switch/case statements**. The idea here is to leverage the fact that Python has first-class functions. 

We define a dictionary that maps lookup keys for the input conditions to functions that will carry out the intended operations. And we also make use of the `get()` method of `dict`, which return a default value if the key can't be found, to handle the `else` case.

```python
# long if...elif...else
if cond == "cond_a":
    handle_a()
elif cond == "cond_b":
    handle_b()
else:
    handle_default()
```

```python
# use dict lookup
func_dict = {
    "cond_a": handle_a,
    "cond_b": handle_b,
}

handle = func_dict.get(cond, handle_default)
```

Example:

```python
def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
```

Use dictionary lookup:

```python
>>> def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()
```

{{% callout  warning %}}

this technique won’t apply in every situation and sometimes you’ll be better off with a plain `if`-statement.

{{% /callout %}}

## Merging Dictionaries

Merge two or more dictionaries into one, so that the resulting dictionary contains a combination of the keys and values of the source dicts.

#### Use built-in `update()`

```python
>>> xs = {'a': 1, 'b': 2}
>>> ys = {'b': 3, 'c': 4}

>>> zs = {}
>>> zs.update(xs)
>>> zs.update(ys)
>>> zs
{'a': 1, 'b': 3, 'c': 4}
```

a naive implementation of `update()` is to simply iterate over all of the items of the right-hand side dictionary and add each key/value pair to the left-hand side dictionary, overwriting existing keys as we go along:

```python
def update(dict1, dict2):
   for key, value in dict2.items():
       dict1[key] = value
```

#### Use `dict()` built-in combined with the `**`-operator

```python
>>> zs = dict(xs, **ys)
>>> zs
{'a': 1, 'c': 4, 'b': 3}
```

#### Use the `**`-operator

```python
zs = {**xs, **ys}
```

This expression has the exact same result as a chain of `update()` calls. This is an arguably prettier way to merge an arbitrary number of dictionaries. Using the `**`-operator is also faster than using chained `update()` calls

## Dictionary Pretty-Printing

Example:

```python
>>> mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
>>> str(mapping)
{'b': 42, 'c': 12648430, 'a': 23}
```

### Use `json.dumps()`

```python
>>> import json
>>> json.dumps(mapping, indent=4, sort_keys=True)
{
	"a": 23,
	"b": 42,
    "c": 12648430
}
```

While this looks nice and readable, it isn’t a perfect solution. There are some limitations:

- Printing dictionaries with the `json` module only works with dicts that contain primitive types—you’ll run into trouble trying to print a dictionary that contains a non-primitive data type, like a function.
- Using `json.dumps()` is that it can’t stringify complex data types, like sets.
- In some cases you won’t be able to take the output from json.dumps and copy and paste it into a Python interpreter session to reconstruct the original dictionary object.

#### Use `pprint`

```python
>>> import pprint
>>> pprint.pprint(mapping)
{'a': 23, 'b': 42, 'c': 12648430, 'd': set([1, 2, 3])}
```

However, compared to `json.dumps()`, it doesn’t represent nested structures as well visually. 