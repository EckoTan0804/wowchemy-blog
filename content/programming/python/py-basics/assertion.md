---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 20
# ============================================================

# ========== Basic metadata ==========
title: Assertion
date: 2022-12-03
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - Basics
  - Assertion
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


- The proper use of assertions is to **inform developers about *unrecoverable* errors in a program.**
- Assertions are *not* intended to signal expected error conditions.
- Assertions are meant to be *internal self-checks* for your program.

keep in mind that Python’s assert statement is a debugging aid, not a mechanism for handling run-time errors.

The goal of using assertions is to let developers find the likely root cause of a bug more quickly. An assertion error should *NEVER* be raised unless there’s a bug in your program.

## Syntax

```python
assert_stmt ::= "assert" expression1 ["," expression2]
```

- `expression1` is the condition we test
- the optional `expression2` is an error message that’s displayed if the assertion fails.

At execution time, the Python interpreter transforms each assert state- ment into roughly the following sequence of statements:

```python
if __debug__:
    if not expression1:
        raise AssertionError(expression2)
```

Before the assert condition is checked, there’s an additional check for the `__debug__` global variable. It’s a built-in boolean flag that’s true under normal circumstances and false if optimizations are requested.

## Two caveats when using asserts

### Don’t Use Asserts for Data Validation

Assertions can be globally disabled3 with the `-0` and `-00` command line switches, as well as the `PYTHONOPTIMIZE` environment variable in CPython!

$\rightarrow$ This turns any assert statement into a null-operation: the assertions simply get compiled away and won’t be evaluated 🤪, which means that none of the conditional expressions will be executed. As a side-effect, it becomes extremely dan- gerous to use assert statements as a quick and easy way to validate input data.

The solution to avoid this problem is: **NEVER use assertions to do data validation.** Instead, we could do our validation with regular `if`-statements and raise validation exceptions if necessary

#### Example

❌ Don't do

```python
def delete_product(prod_id, user):
    assert user.is_admin(), 'Must be admin'
    assert store.has_product(prod_id), 'Unknown product' 	
    store.get_product(prod_id).delete()
```

✅ Do 

```python
def delete_product(product_id, user): 
    if not user.is_admin():
        raise AuthError('Must be admin to delete') 
    if not store.has_product(product_id):
        raise ValueError('Unknown product id') 			  
    store.get_product(product_id).delete()
```

### Asserts That Never Fail

When you **pass a tuple as the first argument** in an `assert` statement, the assertion always evaluates as `true` and therefore never fails.

For example, the following assertion will never fail:

```python
assert(1 == 2, 'This should fail')
```

Reason is that non-empty tuples is always `true` in Python.

A good countermeasure you can apply to prevent this syntax quirk from causing trouble is to use a code linter.  Newer versions of Python 3 will also show a syntax warning for these dubious asserts.