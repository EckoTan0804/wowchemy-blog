---
# ===== Title, summary, and position in the left sidebar =====
linktitle: "Function: Lambda Function" # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 22
# ============================================================

# ========== Basic metadata ==========
title: Lambda Function
date: 2022-12-03
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - Basics
  - Function
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



The `lambda` keyword in Python provides a shortcut for declaring small anonymous functions. Lambda functions behave just like regular functions declared with the def keyword.

Example:

```python
>>> add = lambda x, y: x + y 
>>> add(5, 3)
8
```

It is equivalent to declaring the same `add` function with the `def` keyword (which would be slightly moer verbose):

```python
>>> def add(x, y): 
... 	return x + y 
>>> add(5, 3)
8
```

We can also define a lambda function and then immediately evaluated it inline, without binding the function object to a name:

```python
>>> (lambda x, y: x + y)(5, 3) 
8
```

The syntactic difference between lambdas and regular function definitions is: Lambda functions are restricted to a *single* expression. This means a lambda function can’t use statements or annotations—not even a `return` statement.

Executing a lambda function evaluates its expression and then automatically returns the expression’s result, so there’s always an *implicit* return statement.

## When to use `lambda`?

Lambdas provide a handy and “unbureaucratic” shortcut to defining a function in Python. A typical use case for lambdas is writing short and concise *key funcs* for sorting iterables by an alternate key:

```python
>>> tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')] 
>>> sorted(tuples, key=lambda x: x[1])
[(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]
```

Just like regular nested functions, lambdas also work as *lexical closures*. 

Example:

```python
>>> def make_adder(n):
... 	return lambda x: x + n

>>> plus_3 = make_adder(3)

>>> plus_3(4) 
7
```

The `x + n` lambda can still access the value of `n` even though it was defined in the make_adder function (the enclosing scope).

## When NOT to use `lambda`?

**Lambda functions should be used sparingly and with extraordinary care!!!**

If you’re tempted to use a lambda, spend a few seconds (or minutes) to think if it is really the cleanest and most maintainable way to achieve the desired result.

For example:

```python
# Bad readablility with lambda:
>>> list(filter(lambda x: x % 2 == 0, range(16))) [0, 2, 4, 6, 8, 10, 12, 14]

# Better readablility with list comprehension
>>> [x for x in range(16) if x % 2 == 0] [0, 2, 4, 6, 8, 10, 12, 14]
```

Do not use lambda just for show-off purpose. 

- If you find yourself doing anything remotely complex with lambda expressions, consider defining a standalone function with a proper name instead.
- Saving a few keystrokes won’t matter in the long run, but your col- leagues (and your future self) will appreciate clean and readable code more than terse wizardry.