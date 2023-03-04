---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 25
# ============================================================

# ========== Basic metadata ==========
title: Generator
date: 2023-01-20
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - Basics
  - Generator
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

In Python, a generator is a [function](https://www.programiz.com/python-programming/function) that returns an [iterator](https://www.programiz.com/python-programming/iterator) that produces a sequence of values when iterated over.

Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.

## Understanding Generators

Generator functions look and act just like regular functions, but with one defining characteristic. Generator functions use the Python [`yield` keyword](https://realpython.com/python-keywords/#returning-keywords-return-yield) instead of `return`. 

For example: generating infinite sequence:

```python
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
```

This looks like a typical [function definition](https://realpython.com/defining-your-own-python-function/), except for the Python `yield `statement and the code that follows it. 

- **`yield` indicates where a value is sent back to the caller, but unlike `return`, you don’t exit the function afterward.**
- Instead, **the state of the function is remembered.** That way, when `next()` is called on a generator object (either explicitly or implicitly within a `for` loop), the previously yielded variable `num` is incremented, and then yielded again.

### Building generators

#### Define as function

 Similar to defining a [normal function](https://www.programiz.com/python-programming/function), we can define a generator function using the `def` keyword, but instead of the `return` statement we use the `yield` statement.

```python
def generator_name(arg):
    # statements
    yield something
```

When the generator function is called, it does not execute the function body immediately. Instead, it returns a generator object that can be iterated over to produce the values.

#### Define using comprehension

Like list comprehensions, generator expressions allow you to quickly create a generator object in just a few lines of code. 

```python
(expression for item in iterable)
```

The generator expression creates a generator object that produces the values of `expression` for each item in the `iterable`, one at a time, when iterated over.

Generator comprehensions are also useful in the same cases where list comprehensions are used, with an added benefit: **<span style="color:  ForestGreen">you can create them without building and holding the entire object in memory before iteration</span>.**

Example: squaring numbers

```python
num_squared_list = [num ** 2 for num in range(5)] # list comprehension
num_squared_generator = (num ** 2 for num in range(5)) # generator comprehension
```

```python
>>> num_squared_list
[0, 1, 4, 9, 16]

>>> num_squared_generator
<generator object <genexpr> at 0x7f9c604c8430>
```

### Profiling generator performance

Memory:

```python
>>> import sys
>>> nums_squared_lc = [i ** 2 for i in range(10000)]
>>> sys.getsizeof(nums_squared_lc) # in bytes
87624
>>> nums_squared_gc = (i ** 2 for i in range(10000))
>>> print(sys.getsizeof(nums_squared_gc)) # in bytes
120
```

The list is over 700 times larger than the generator object!

Speed:

```python
>>> import cProfile
>>> cProfile.run('sum([i * 2 for i in range(10000)])')
         5 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.001    0.001 <string>:1(<listcomp>)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


>>> cProfile.run('sum((i * 2 for i in range(10000)))')
         10005 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    10001    0.002    0.000    0.002    0.000 <string>:1(<genexpr>)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.001    0.001    0.003    0.003 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

Summing across all values in the list comprehension took about *a third* of the time as summing across the generator.

If the list is smaller than the running machine’s available memory, then list comprehensions can be [faster to evaluate](https://stackoverflow.com/questions/11964130/list-comprehension-vs-generator-expressions-weird-timeit-results/11964478#11964478) than the equivalent generator expression.

{{% callout note %}}

Memory matters → Use generator comprehension.

Runtime matters → Use list comprehension.

{{% /callout %}}

## Understanding the `yield` Statement

On the whole, `yield` is a fairly simple statement. Its primary job is to control the flow of a generator function in a way that’s similar to `return` statements.

- When the `yield `statement is hit/arrived, the program **suspends function execution and returns the yielded value to the caller**. (In contrast, `return` stops function execution completely.) When a function is suspended, the state of that function is saved (including variables binding local to the generator, the instruction point, the internal stack, and any exception handling).
- This allows you to resume function execution whenever you call one of the generator’s methods. In this way, all function evaluation picks back up **right after** `yield`.

Example:

```python
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
        yield f"Next number to yield: {num}"
```

```python
>>> inf_seq_generator = infinite_sequence()
>>> inf_seq_generator
<generator object infinite_sequence at 0x7f9c604c8b30>

# The `inifinite_sequence` runs and arrives line 4,
# the execution is suspended by yield statement. 
# The `num` (0 in this case) is yielded.
>>> next(inf_seq_generator)
0

# The funtion execution picks back up right after `yield num`.
# I.e., the program continues from line 5, `num += 1`. `num` is incremented to 1.
# Then the `yield` statement at line 6 is arrived
# --> It suspends the program and yield "Next number to yield: 1"
>>> next(inf_seq_generator)
'Next number to yield: 1'

>>> next(inf_seq_generator)
1

>>> next(inf_seq_generator)
'Next number to yield: 2'

>>> next(inf_seq_generator)
2

```

## Use of Python Generators

There are several reasons that make generators a powerful implementation.

### Easy to Implement

Generators can be implemented in a clear and concise way as compared to their iterator class counterpart.

### Memory Efficient

A normal function to return a sequence will create the entire sequence in memory before returning the result. This is an overkill, if the number of items in the sequence is very large.

In contrast, Generator implementation of such sequences is memory friendly and is preferred since it only produces one item at a time.

### Represent Infinite Stream

Generators are excellent mediums to represent an infinite stream of data. Infinite streams cannot be stored in memory, and since generators produce only one item at a time, they can represent an infinite stream of data.

E.g., the following generator function can generate all the even numbers (at least in theory).

```python
def all_even():
    n = 0
    while True:
        yield n
        n += 2
```

### Pipelining Generators

Multiple generators can be used to pipeline a series of operations. 

E.g., suppose we have a generator that produces the numbers in the Fibonacci series. And we have another generator for squaring numbers. If we want to find out the sum of squares of numbers in the Fibonacci series, we can do it in the following way by pipelining the output of generator functions together.

```python
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))

# Output: 4895
```



## Reference

- [Python Generators](https://www.programiz.com/python-programming/generator)

- [How to Use Generators and yield in Python](https://realpython.com/introduction-to-python-generators/#understanding-generators)

