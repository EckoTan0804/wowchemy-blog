---
# ===== Title, summary, and position in the left sidebar =====
linktitle: Terminal Input & Output # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 16 # Order in the chapter
# =========================================================

# ========== Basic metadata ==========
title: Basic Input and Output
date: 2022-04-28
draft: false
type: book # page type
authors: 
  - admin
tags: 
  - Python
  - Basics
categories: 
  - Coding
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

{{< figure src="https://files.realpython.com/media/Basic-Input-Output-and-String-Formatting-in-Python_Watermarked.59ecd279c01b.jpg" caption="Source: RealPython" numbered="true" >}}

## Reading Input From the Keyboard

`input([<prompt>])`: Reads a line from the keyboard. ([Documentation](https://docs.python.org/3/library/functions.html#input))

- pauses program execution to allow the user to type in a line of input from the keyboard

- Once the user presses the Enter key, all characters typed are read and returned as a [string](https://realpython.com/python-strings/)

  - Note: the return string doesn’t include the newline generated when the user presses the Enter key.

  - Example

    ```python
    >>> user_input = input()
    foo bar baz
    >>> user_input
    'foo bar baz'
    ```

- If you include the optional `<prompt>` argument, then `input()` displays it as a prompt so that your user knows what to input

  - Example

    ```python
    >>> name = input("What is your name? ")
    What is your name? Winston Smith
    >>> name
    'Winston Smith'
    ```

- `input()` always returns a **string**. If you want a numeric type, convert the string with the appropriate built-in fuctions (`int()`, `float()`, `complex()`)



## Writing Output to the Console

You can display program data to the console in Python with [`print()`](https://docs.python.org/3/library/functions.html#print).

`print()` is capable of taking the following arguments:

{{< figure src="https://stackabuse.s3.amazonaws.com/media/python-how-to-print-without-a-newline-space-1.jpg" caption="`print()` function" numbered="true" >}}

- The values (`value1`, `value2`) mentioned above can be any string or any of the data types like list, float, string, etc.
- `sep`: Divides the values given as arguments
- `end`: String appended to the end (`\n` by default)

### Example

```python
>>> arr = [1, 2, 3, 4 ,5]
>>> _ = [print("num", el, sep=": ", end="; ") for el in arr]
num: 1; num: 2; num: 3; num: 4; num: 5; 
```

```python
>>> d = {"foo": 1, "bar": 2, "baz": 3}
>>> for k, v in d.items():
...     print(k, v, sep=" -> ")
...
foo -> 1
bar -> 2
baz -> 3
```

## Reference

- [Basic Input, Output, and String Formatting in Python](https://realpython.com/python-input-output/#reading-input-from-the-keyboard)

- [Python: How to Print without Newline or Space](https://stackabuse.com/python-how-to-print-without-newline-or-space/)