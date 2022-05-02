---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary: In-depth look at the Python built-in handling for strings. # Summary of this post
weight: 17
# ============================================================

# ========== Basic metadata ==========
title: String
date: 2022-05-01
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - Basics
  - String
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

{{< figure src="https://files.realpython.com/media/Strings-and-Character-Data-in-Python_Watermarked.296b2b518ae5.jpg" caption="Source: Real Python" numbered="true" width="80%">}}

**String = object that contains a sequence of character data.**

Python provides a rich set of operators, functions, and methods for working with strings.

## String Operators

### The `+` Operator

The `+` operator concatenates strings. It returns a string consisting of the operands joined together


{{< spoiler text="Example" >}}

```python
>>> str_1 = "Hello"
>>> str_2 = "World"
>>> str_1 + str_2
HelloWorld
```

{{< /spoiler >}}

### The `*` Operator

The `*` operator creates multiple copies of a string. If `s` is a string and `n` is an integer, either of the following expressions returns a string consisting of `n` concatenated copies of `s`:

- `s * n`
- `n * s`

If `n` <= 0, then the result is an empty string.

{{< spoiler text="Example" >}}

```python
>>> s = 'foo.' 

>>> s * 4 # n > 0
'foo.foo.foo.foo.'
>>> 4 * s
'foo.foo.foo.foo.'
```

n <= 0:
```python
>>> 'foo' * -8 # n <= 0
''
```

{{< /spoiler >}}

### The `in` Operator

As string is essentially a *list* of characters, the membership operator `in` can also be used with string.

{{< spoiler text="Example" >}}

```python
>>> s = 'foo'

>>> s in 'That\'s food for thought.'
True
>>> s in 'That\'s good for now.'
False
```

```python
>>> 'z' not in 'abc'
True
>>> 'z' not in 'xyz'
False
```

{{< /spoiler >}}

## Build-in String Functions

| Function | Description                                  |
| -------- | :------------------------------------------- |
| `chr()`  | Converts an integer to a character           |
| `ord()`  | Converts a character to an integer           |
| `len()`  | Returns the length of a string               |
| `str()`  | Returns a string representation of an object |

### `ord(c)`

Returns an integer value ([ASCII](https://en.wikipedia.org/wiki/ASCII) or [Unicode](https://realpython.com/courses/python-unicode/)) for the given character.

{{< spoiler text="Example" >}}

```python
>>> ord('a')
97
>>> ord('#')
35
```

```python
>>> ord('€')
8364
>>> ord('∑')
8721
```

{{< /spoiler >}}

### `chr(n)`

`chr()` does the reverse of `ord()`. Given a numeric value `n`, `chr(n)` returns a string representing the character that corresponds to `n`.

{{< spoiler text="Example" >}}

```python
>>> chr(97)
'a'
>>> chr(35)
'#'
```

```python
>>> chr(97)
'a'
>>> chr(35)
'#'
```

{{< /spoiler >}}

### `len(s)`

Returns the length (number of characters) of a string.

{{< spoiler text="Example" >}}

```python
>>> s = 'I am a string.'
>>> len(s)
14
```

{{< /spoiler >}}

### `str(obj)`

Returns a string representation of an object.

{{< spoiler text="Example" >}}

```python
>>> str(49.2)
'49.2'
>>> str(3+4j)
'(3+4j)'
>>> str(3 + 29)
'32'
>>> str('foo')
'foo'
```

{{< /spoiler >}}

## List Operations for String

In Python, strings are ordered sequences of character data. Therefore, list operations (indexing, slicing, negative indexing) also work with string.

## Interpolating Variables into a String

Since Python 3.6, a new powerful formatting mechanism was introduced. 

This feature is formally named the **Formatted String Literal**, but is more usually referred to by its nickname **f-string**.

More about f-string see: [f-string]({{< relref "format-string" >}})

## Modify Strings

In a nutshell, you can’t. Strings are one of the data types Python considers **immutable**, meaning not able to be changed.

You can usually easily accomplish what you want by generating a copy of the original string that has the desired change in place. Two possibilities:

- Assign a new string to the variable

  ```python
  >>> s = 'foobar'
  >>> s = s[:3] + 'x' + s[4:]
  >>> s
  'fooxar'
  ```

- Use built-in string method

  ```python
  >>> s = 'foobar'
  >>> s = s.replace('b', 'x')
  >>> s
  'fooxar'
  ```

  

## Built-in String Methods

Python provides a lot of useful built-in methods for string objects.

> - **Function**: a callable procedure that you can invoke to perform specific tasks.
> - **Method**: a specialized type of callable procedure that is tightly associated with an object. Like a function, a method is called to perform a distinct task, but it is invoked on a specific object and has knowledge of its target object during execution.

{{% callout note %}}

In the following method definitions, arguments specified in square brackets (`[]`) are optional.

{{% /callout %}}

### Case Conversion

Methods in this group perform case conversion on the target string.

#### `s.capitalize()`

Returns a copy of `s` with the first character converted to uppercase and all other characters converted to lowercase. Non-alphabetic characters are unchanged.

{{< spoiler text="Example" >}}

```python
>>> s = 'foo123#BAR#.'
>>> s.capitalize()
'Foo123#bar#.'
```

{{< /spoiler >}}

#### `s.lower()`

Returns a copy of `s` with all alphabetic characters converted to lowercase.

#### `s.swapcase()`

Returns a copy of `s` with uppercase alphabetic characters converted to lowercase and vice versa.

{{< spoiler text="Example" >}}

```python
>>> 'FOO Bar 123 baz qUX'.swapcase()
'foo bAR 123 BAZ Qux'
```

{{< /spoiler >}}

#### `s.title()`

Returns a copy of `s` in which the first letter of each word is converted to uppercase and remaining letters are lowercase.

{{% callout warning %}}

This method uses a fairly simple algorithm. It does NOT attempt to distinguish between important and unimportant words, and it does NOT handle apostrophes, possessives, or acronyms gracefully.

{{% /callout %}}

{{< spoiler text="Example" >}}

```python
>>> "what's happened to ted's IBM stock?".title()
"What'S Happened To Ted'S Ibm Stock?"
```

{{< /spoiler >}}

#### `s.upper()`

Returns a copy of `s` with all alphabetic characters converted to uppercase.

### Find and Replace

- These methods provide various means of searching the target string for a specified substring.
- Each method in this group supports optional `<start>` and `<end>` arguments.
  - The action of the method is restricted to the portion of the target string starting at character position `<start>` and proceeding up to but *NOT* including character position `<end>`
  - If `<start>` is specified but `<end>` is not, the method applies to the portion of the target string from `<start>` through the end of the string.

#### `s.count(<sub>[, <start>[, <end>]])`

- Counts occurrences of a substring in the target string.
- returns the number of non-overlapping occurrences of substring `<sub>` in `s`:

{{< spoiler text="Example" >}}

```python
>>> 'foo goo moo'.count('oo')
3
```

```python
>>> 'foo goo moo'.count('oo', 0, 8)
2
```

{{< /spoiler >}}

#### `s.endswith(<suffix>[, <start>[, <end>]])`

- Determines whether the target string ends with a given substring
- returns `True` if `s` ends with the specified `<suffix>` and `False` otherwise

{{< spoiler text="Example" >}}

```python
>>> 'foobar'.endswith('bar')
True
>>> 'foobar'.endswith('baz')
False
```

```python
>>> 'foobar'.endswith('oob', 0, 4)
True
>>> 'foobar'.endswith('oob', 2, 4)
False
```

{{< /spoiler >}}

#### `s.find(<sub>[, <start>[, <end>]])`

- Searches the target string for a given substring. You can use `.find()` to see if a Python string contains a particular substring.
- Returns the *lowest* index in `s` where substring `<sub>` is found
- Returns `-1` if the specified substring is not found

{{< spoiler text="Example" >}}

```python
>>> 'foo bar foo baz foo qux'.find('foo')
0
```

```python
>>> 'foo bar foo baz foo qux'.find('grault')
-1
```

```python
>>> 'foo bar foo baz foo qux'.find('foo', 4)
8
>>> 'foo bar foo baz foo qux'.find('foo', 4, 7)
-1
```

{{< /spoiler >}}

#### `s.index(<sub>[, <start>[, <end>]])`

Identical to `.find()`, except that it raises an exception if `<sub>` is not found rather than returning `-1`

#### `s.rfind(<sub>[, <start>[, <end>]])`

- Searches the target string for a given substring starting at the end.

- Returns the *highest* index in `s` where substring `<sub>` is found
- Returns `-1` if the substring is not found

{{< spoiler text="Example" >}}

```python
>>> 'foo bar foo baz foo qux'.rfind('foo')
16
```

```python
>>> 'foo bar foo baz foo qux'.rfind('grault')
-1
```

```python
>>> 'foo bar foo baz foo qux'.rfind('foo', 0, 14)
8
>>> 'foo bar foo baz foo qux'.rfind('foo', 10, 14)
-1
```

{{< /spoiler >}}

#### `s.rindex(<sub>[, <start>[, <end>]])`

Identical to `.rfind()`, except that it raises an exception if `<sub>` is not found rather than returning `-1`

#### `s.startswith(<prefix>[, <start>[, <end>]])`

- Determines whether the target string starts with a given substring.
- Returns `True` if `s` starts with the specified `<prefix>` and `False` otherwise

{{< spoiler text="Example" >}}

```python
>>> 'foobar'.startswith('foo')
True
>>> 'foobar'.startswith('bar')
False
```

```python
>>> 'foobar'.startswith('bar', 3)
True
>>> 'foobar'.startswith('bar', 3, 2)
False
```

{{< /spoiler >}}

### Character Classification

Classify a string based on the characters it contains.

#### `s.isalnum()`

- Determines whether the target string consists of alphanumeric characters
- Returns `True` if `s` is nonempty and all its characters are alphanumeric (either a letter or a number), and `False` otherwise

{{< spoiler text="Example" >}}

```python
>>> 'abc123'.isalnum()
True
>>> 'abc$123'.isalnum()
False
>>> ''.isalnum()
False
```

{{< /spoiler >}}

#### `s.isalpha()`

- Determines whether the target string consists of alphabetic characters.
- `s.isalpha()` returns `True` if `s` is nonempty and all its characters are alphabetic, and `False` otherwise

{{< spoiler text="Example" >}}

```python
>>> 'ABCabc'.isalpha()
True
>>> 'abc123'.isalpha()
False
```

{{< /spoiler >}}

#### `s.isdigit()`

- Determines whether the target string consists of digit characters. You can use the `.isdigit()` Python method to check if your string is made of only digits.

- Returns `True` if `s` is nonempty and all its characters are numeric digits, and `False` otherwise

{{< spoiler text="Example" >}}

```python
>>> '123'.isdigit()
True
>>> '123abc'.isdigit()
False
```

{{< /spoiler >}}

#### `s.isidentifier()`

- Determines whether the target string is a valid Python identifier.
- Returns `True` if `s` is a valid Python identifier according to the language definition, and `False` otherwise

{{< spoiler text="Example" >}}

```python
>>> 'foo32'.isidentifier()
True
>>> '32foo'.isidentifier()
False
>>> 'foo$32'.isidentifier()
False
```

{{< /spoiler >}}

{{% callout warning %}}

`.isidentifier()` will return `True` for a string that matches a [Python keyword](https://realpython.com/python-keywords/) even though that would not actually be a valid identifier, e.g.,

```python
>>> 'and'.isidentifier() # and is a keyword in python
True
```

To test whether a string matches a Python keyword, use `keyword.iskeyword():`

```python
>>> from keyword import iskeyword
>>> iskeyword('and')
True
```

If you really want to ensure that a string would serve as a valid Python identifier, you should check that `.isidentifier()` is `True` and that `iskeyword()` is `False`

{{% /callout %}}

#### `s.islower()`

- Determines whether the target string’s alphabetic characters are lowercase.
- returns `True` if `s` is nonempty and all the alphabetic characters it contains are lowercase, and `False` otherwise. Non-alphabetic characters are ignore.

{{< spoiler text="Example" >}}

```python
>>> 'abc'.islower()
True
>>> 'abc1$d'.islower()
True
>>> 'Abc1$D'.islower()
False
```

{{< /spoiler >}}

#### `s.isprintable()`

- Returns `True` if `s` is empty or all the alphabetic characters it contains are printable.
- Returns `False` if `s` contains at least one non-printable character.
- Non-alphabetic characters are ignored

{{< spoiler text="Example" >}}

```python
>>> 'a\tb'.isprintable()
False
>>> 'a b'.isprintable()
True
>>> ''.isprintable()
True
>>> 'a\nb'.isprintable()
False
```

{{< /spoiler >}}

{{% callout note %}}

This is the only `.isxxxx()` method that returns `True` if `s` is an empty string. All the others return `False` for an empty string.

{{% /callout %}}

#### `s.isspace()`

- Determines whether the target string consists of whitespace characters.
- Returns `True` if `s` is nonempty and all characters are whitespace characters, and `False` otherwise.
- The most commonly encountered whitespace characters are 
  - space `' '`
  - tab `'\t'`
  - newline `'\n'`

{{< spoiler text="Example" >}}

```python
>>> ' \t \n '.isspace()
True
>>> '   a   '.isspace()
False
```

{{< /spoiler >}}

#### `s.istitle()`

- Determines whether the target string is title cased.
- Returns
  -  `True` if `s` is nonempty, the first alphabetic character of each word is uppercase, and all other alphabetic characters in each word are lowercase. (more intuitive: “Uppercase characters may only follow uncased characters and lowercase characters only cased ones.”)
  - `False`, otherwise 

{{< spoiler text="Example" >}}

```python
>>> 'This Is A Title'.istitle()
True
>>> 'This is a title'.istitle()
False
>>> 'Give Me The #$#@ Ball!'.istitle()
True
```

{{< /spoiler >}}

#### `s.isupper()`

- Determines whether the target string’s alphabetic characters are uppercase.
- Returns `True` if `s` is nonempty and all the alphabetic characters it contains are uppercase, and `False` otherwise. 
- Non-alphabetic characters are ignored

{{< spoiler text="Example" >}}

```python
>>> 'ABC'.isupper()
True
>>> 'ABC1$D'.isupper()
True
>>> 'Abc1$D'.isupper()
False
```

{{< /spoiler >}}

### String Formatting

Modify or enhance the format of a string

#### `s.center(<width>[, <fill>])`

- Centers a string in a field.

- Returns a string consisting of `s` centered in a field of width `<width>`. By default, padding consists of the ASCII space character

  ```python
  >>> 'foo'.center(10)
  '   foo    '
  ```

- If the optional `<fill>` argument is specified, it is used as the padding character

  ```python
  >>> 'bar'.center(10, '-')
  '---bar----'
  ```

- If `s` is already at least as long as `<width>`, it is returned unchanged

  ```python
  >>> 'foo'.center(2)
  'foo'
  ```

#### `s.expandtabs(tabsize=8)`

- Replaces each tab character (`'\t'`) with spaces. 
- `tabsize` is an optional keyword parameter specifying alternate tab stop columns. By default, spaces are filled in assuming a tab stop at every eighth column

{{< spoiler text="Example" >}}

```python
>>> 'a\tb\tc'.expandtabs()
'a       b       c'
>>> 'aaa\tbbb\tc'.expandtabs()
'aaa     bbb     c'
```

```python
>>> 'a\tb\tc'.expandtabs(4)
'a   b   c'
>>> 'aaa\tbbb\tc'.expandtabs(tabsize=4)
'aaa bbb c'
```

{{< /spoiler >}}

#### `s.ljust(<width>[, <fill>])`

- Left-justifies a string in field.

- Returns a string consisting of `s` left-justified in a field of width `<width>`

  ```python
  >>> 'foo'.ljust(10)
  'foo       '
  ```

- If the optional `<fill>` argument is specified, it is used as the padding character

  ```python
  >>> 'foo'.ljust(10, '-')
  'foo-------'
  ```

- If `s` is already at least as long as `<width>`, it is returned unchanged

  ```python
  >>> 'foo'.ljust(2)
  'foo'
  ```

##### `s.lstrip([<chars>])`

- Trims leading characters from a string.

- returns a copy of `s` with any whitespace characters removed from the left end

  ```python
  >>> '   foo bar baz   '.lstrip()
  'foo bar baz   '
  >>> '\t\nfoo\t\nbar\t\nbaz'.lstrip()
  'foo\t\nbar\t\nbaz'
  ```

- If the optional `<chars>` argument is specified, it is a string that specifies the set of characters to be removed

  ```python
  >>> 'http://www.realpython.com'.lstrip('/:pth')
  'www.realpython.com'
  ```

#### `s.replace(<old>, <new>[, <count>])`

- Replaces occurrences of a substring within a string.

- Returns a copy of `s` with all occurrences of substring `<old>` replaced by `<new>`

  ```python
  >>> 'foo bar foo baz foo qux'.replace('foo', 'grault')
  'grault bar grault baz grault qux'
  ```

- If the optional `<count>` argument is specified, a maximum of `<count>` replacements are performed, starting at the left end of `s`

  ```python
  >>> 'foo bar foo baz foo qux'.replace('foo', 'grault', 2)
  'grault bar grault baz foo qux'
  ```

#### `s.rjust(<width>[, <fill>])`

- Right-justifies a string in a field.
- Works similarly to [`s.ljust()`](#sljustwidth-fill)

#### `s.rstrip([<chars>])`

- Trims trailing characters from a string.
- Works similarly to [`s.lstrip()`](#slstripchars)

#### `s.strip([<chars>])`

- Strips characters from the left and right ends of a string.
- Equivalent to `s.lstrip().rstrip()`

- As with `.lstrip()` and `.rstrip()`, the optional `<chars>` argument specifies the set of characters to be removed

#### `s.zfill(<width>)`

- Pads a string on the left with zeros.

- Returns a copy of `s` left-padded with `'0'` characters to the specified `<width>`

  ```python
  >>> '42'.zfill(5)
  '00042'
  ```

- If `s` contains a leading sign, it remains at the left edge of the result string after zeros are inserted

  ```python
  >>> '+42'.zfill(8)
  '+0000042'
  >>> '-42'.zfill(8)
  '-0000042'
  ```

- If `s` is already at least as long as `<width>`, it is returned unchanged

### Converting Between Strings and Lists

Convert between a string and some composite data type by either pasting objects together to make a string, or by breaking a string up into pieces.

#### `s.join(<iterable>)`

Concatenates strings from an iterable.

{{< spoiler text="Example" >}}

```python
>>> ', '.join(['foo', 'bar', 'baz', 'qux'])
'foo, bar, baz, qux'
```
In the following example, `<iterable>` is specified as a single string value. When a string value is used as an iterable, it is interpreted as a list of the string’s individual characters.

```python
>>> list('corge')
['c', 'o', 'r', 'g', 'e']

>>> ':'.join('corge')
'c:o:r:g:e'
```

{{< /spoiler >}}

#### `s.partition(<sep>)`

- Splits `s` at the first occurrence of string `<sep>`. 
- The return value is a three-part tuple consisting of:
  - The portion of `s` preceding `<sep>`
  - `<sep>` itself
  - The portion of `s` following `<sep>`

{{< spoiler text="Example" >}}

```python
>>> 'foo.bar'.partition('.')
('foo', '.', 'bar')
>>> 'foo@@bar@@baz'.partition('@@')
('foo', '@@', 'bar@@baz')
```

If `<sep>` is not found in `s`, the returned tuple contains `s` followed by two empty strings:

```python
>>> 'foo.bar'.partition('@@')
('foo.bar', '', '')
```

{{< /spoiler >}}

#### s.rpartition(<sep>)

Works exactly like `s.partition(<sep>)`, except that `s` is split at the *last* occurrence of `<sep>` instead of the first occurrence

#### `s.rsplit(sep=None, maxsplit=-1)`

- Splits a string into a list, starting from the right

- Without arguments, `s.rsplit()` splits `s` into substrings delimited by any sequence of whitespace and returns the substrings as a list

  ```python
  >>> 'foo bar baz qux'.rsplit()
  ['foo', 'bar', 'baz', 'qux']
  >>> 'foo\n\tbar   baz\r\fqux'.rsplit()
  ['foo', 'bar', 'baz', 'qux']
  ```

- If `<sep>` is specified, it is used as the delimiter for splitting

  ```python
  >>> 'foo.bar.baz.qux'.rsplit(sep='.')
  ['foo', 'bar', 'baz', 'qux']
  ```

  - When `<sep>` is explicitly given as a delimiter, consecutive delimiters in `s` are assumed to delimit empty strings, which will be returned

    ```python
    >>> 'foo...bar'.rsplit(sep='.')
    ['foo', '', '', 'bar']
    ```

- If the optional keyword parameter `<maxsplit>` is specified, a maximum of that many splits are performed, starting from the right end of `s`

  ```python
  >>> 'www.realpython.com'.rsplit(sep='.', maxsplit=1)
  ['www.realpython', 'com']
  ```

#### `s.split(sep=None, maxsplit=-1)`

Behaves exactly like `s.rsplit()`, except that if `<maxsplit>` is specified, splits are counted from the *left* end of `s` rather than the right end

#### `s.splitlines([<keepends>])`

- Splits `s` at line boundaries up into lines and returns them in a list. 

- Any of the following characters or character sequences is considered to constitute a line boundary:

  | Escape Sequence |          Character          |
  | :-------------: | :-------------------------: |
  |      `\n`       |           Newline           |
  |      `\r`       |       Carriage Return       |
  |     `\r\n`      | Carriage Return + Line Feed |
  | `\v` or `\x0b`  |       Line Tabulation       |
  | `\f` or `\x0c`  |          Form Feed          |
  |     `\x1c`      |       File Separator        |
  |     `\x1d`      |       Group Separator       |
  |     `\x1e`      |      Record Separator       |
  |     `\x85`      | Next Line (C1 Control Code) |
  |    `\u2028`     |   Unicode Line Separator    |
  |    `\u2029`     | Unicode Paragraph Separator |



## Reference

- [Strings and Character Data in Python](https://realpython.com/python-strings/#built-in-string-methods)