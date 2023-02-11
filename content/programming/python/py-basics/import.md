---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 26
# ============================================================

# ========== Basic metadata ==========
title: Import
date: 2023-02-11
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - Basics
  - Import
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

In Python, we use the **`import`** keyword to make code in one **module** available in another. 

<span style="color:  ForestGreen">Imports in Python are important for **structuring your code** effectively. Using imports properly will make you more productive, allowing you to reuse code while keeping your projects maintainable.</span>

## Basic Python Import

### Modules and packages

#### Module

- Definition (according to [Python.org glossary](https://docs.python.org/glossary.html))

  > An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing. ([Source](https://docs.python.org/glossary.html#term-module))

- Usually corresponds to one `.py` file containing Python code

- Example

  ```python
  >>> import math # import the code in the `math` module
  >>> math.pi # access the `pi` variable within the math module
  3.141592653589793
  ```

- Acts as a [**namespace**](https://realpython.com/python-namespaces-scope/) that keeps all the attributes of the module together.

  - List the content of a namespace with `dir()`:

    ```python
    >>> import math
    >>> dir() # shows what’s in the global namespace
    ['__annotations__', '__builtins__', ..., 'math']
    
    >>> dir(math) # shows what's in the `math` namespace
    ['__doc__', ..., 'nan', 'pi', 'pow', ...]
    ```

- Ways to import

  - Direct import

    ```python
    import math
    ```

  - Import specific parts of a module

    ```python
    >>> from math import pi 
    >>> pi
    3.141592653589793
    
    >>> math.pi
    NameError: name 'math' is not defined
    ```

    In this case `pi` is placed in the global namespace and NOT within `math` namespace.

  - Rename modules and attributes as they’re imported

    ```python
    >>> import math as m
    >>> m.pi
    3.141592653589793
    
    >>> from math import pi as PI
    >>> PI
    3.141592653589793
    ```

- Importing a module both loads the contents and creates a namespace containing the contents. 

#### Package

- Definition

  >A Python module which can contain submodules or recursively, subpackages. Technically, a package is a Python module with an `__path__` attribute. ([Source](https://docs.python.org/glossary.html#term-package))

  (A package is still a module. As a user, you usually don’t need to worry about whether you’re importing a module or a package.)

-  package typically corresponds to a file directory containing Python files and other directories. 

- To create a Python package yourself, you create 

  - a directory and 
  - a [file named `__init__.py`](https://docs.python.org/reference/import.html#regular-packages) inside it
    - contains the contents of the package when it’s treated as a module
    - can be left empty.

- In general, submodules and subpackages ar NOT imported when you import a package. 

  - You can use `__init__.py` to include any or all submodules and subpackages if you want. It’s fairly common to import subpackages and submodules in an `__init__.py` file to make them more readily available to your users. 
  - Submodules and subpackages included in `__init__.py` will be then imported along with the package
  - Good Example: [`__init__.py` of the `request` package](https://github.com/psf/requests/blob/v2.23.0/requests/__init__.py#L112)

### Absolute and relative imports

Let's say we have a package called `world` and it includes a subpackage called `africa`.

In `world/__init__.py`:

```python
from . import africa
```

The dot (`.`) refers to the current package, and the statement is an example of a **relative import**. You can read it as *“From the current package, import the subpackage `africa`.”*

There’s an equivalent **absolute import** statement in which you explicitly name the current package:

```python
from world import africa
```

**The [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/#imports) recommends using absolute imports in general. However, relative imports are an alternative for organizing package hierarchies.** (For more information, see [Absolute vs Relative Imports in Python](https://realpython.com/absolute-vs-relative-python-imports/).)

### Python’s import path

Python looks for modules and packages in its [**import path**](https://docs.python.org/glossary.html#term-import-path), which is a list of locations that are searched for modules to import.

{{% callout note %}}
When you type `import `something, Python will look for something a few different places before searching the import path.

In particular, it’ll look in a module cache to see if something has already been imported, and it’ll search among the built-in modules.
{{% /callout %}}

You can inspect Python’s import path by printing `sys.path`. This list will contain three different kinds of locations:

- The directory of the current script (or the current directory if there’s no script, such as when Python is running interactively). This location is always the **first** in the searching list.
- The contents of the `PYTHONPATH` environment variable
- Other, installation-dependent directories

Python will start at the beginning of the list of locations and look for a given module in each location until the first match. 

You should always be careful that you don’t create modules that **shadow**, or hide, other important modules. 

For example, we define our custom `math` module:

```python
# math.py

def double(number):
    return 2 * number
```

```python
>>> import math
>>> math.double(3.14)
6.28
```

But this module also shadows the standard `math` module that’s included in the standard library! That means our earlier example of looking up the value of $\pi$ no longer works:

```python
>>> import math
>>> math.pi
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'pi'

>>> math
<module 'math' from 'math.py'>
```

In other words, Python now searches your new `math` module for `pi` instead of searching the `math` module in the standard library.

To avoid these kinds of issues, **you should be careful with the names of your modules and packages. In particular, your top-level module and package names should be unique.** 

### Namespace packages

**Namespace packages**

- less dependent on the underlying file hierarchy
- can be split across multiple directories
- A namespace package is created automatically if you have a directory containing a `.py` file but no `__init__.py`.

### Import style guide

[PEP 8](https://www.python.org/dev/peps/pep-0008/), the Python style guide, has a couple of [recommendations about imports](https://www.python.org/dev/peps/pep-0008/#imports). 

To keep your code both readable and maintainable, here are a few general rules of thumb for how to style your imports:

- Keep imports at the top of the file.
- Write imports on separate lines.
- Organize imports into groups: first standard library imports, then third-party imports, and finally local application or library imports.
- Order imports alphabetically within each group.
- Prefer absolute imports over relative imports.
- Avoid wildcard imports like `from module import *`.

[`isort`](https://pypi.org/project/isort/) and [`reorder-python-imports`](https://pypi.org/project/reorder-python-imports/) are great tools for enforcing a consistent style on your imports.

## Resource Imports

Sometimes you’ll have code that depends on data files or other resources. If the resource file is important for your package and you want to distribute your package to other users, then a few challenges will arise:

1. You won’t have control over the path to the resource since that will depend on your user’s setup as well as on how the package is distributed and installed. You can try to figure out the resource path based on your package’s `__file__` or `__path__` attributes, but this may not always work as expected.
2. Your package may [reside inside a ZIP file](https://realpython.com/python-import/#run-python-scripts-from-zip-files) or an old [`.egg` file](https://packaging.python.org/discussions/wheel-vs-egg/), in which case the resource won’t even be a physical file on the user’s system.

With the introduction of **`importlib.resources`** into the standard library in [Python 3.7](https://realpython.com/python37-new-features/#importing-data-files-with-importlibresources), there’s now one standard way of dealing with resource files.

### `importlib.resources`

- Gives access to resources within packages

  - A **resource** is any file located within an importable package. The file may or may not correspond to a physical file on the file system.

- Advantages

  - More consistent way to deal with the files inside your packages
  - Gives you easier access to resource files in other packages

- Requirement when using `importlib.resources`: 

  - Your resource files must be available inside a regular package. Namespace packages aren’t supported. 

    → In practice, this means that the file must be in a directory containing an `__init__.py` file.

#### Example

Assume you have [resources](https://www.gutenberg.org/ebooks/11) inside a package like this:

```
books/
│
├── __init__.py
├── alice_in_wonderland.png
└── alice_in_wonderland.txt
```

`__init__.py` is just an empty file necessary to designate `books` as a regular package.

You can then use `open_text()` and `open_binary()` to open text and binary files, respectively:

```python
>>> from importlib import resources
>>> with resources.open_text("books", "alice_in_wonderland.txt") as fid:
...     alice = fid.readlines()
```

```python
>>> with resources.open_binary("books", "alice_in_wonderland.png") as fid:
...     cover = fid.read()
```

`open_text()` and `open_binary()` are equivalent to the built-in `open()` with the `mode` parameter set to `rt` and `rb`, respectively.

{{% callout note %}}
`importlib.resources` became part of the standard library in Python 3.7. However, on older versions of Python, a [backport is available as `importlib_resources`](https://importlib-resources.readthedocs.io/). This backport is compatible with Python 2.7 as well as Python 3.4 and later versions. To use the backport, install it from [PyPI](https://pypi.org/project/importlib_resources/):

```bash
$ python -m pip install importlib_resources
```

To seamlessly fall back to using the backport on older Python versions, you can import `importlib.resources` as follows:

```python
try:
    from importlib import resources
except ImportError:
    import importlib_resources as resources
```

See the [tips and tricks section](https://realpython.com/python-import/#handle-packages-across-python-versions) of this tutorial for more information.
{{% /callout %}}

## Dynamic imports

### Using `importlib`

The whole import machinery is available in the `importlib` package, and this allows you to do your imports more dynamically. 

## Python Import Systems

### Import Internals

{{% callout note %}}
The details of the Python import system are described in the official documentation. 
{{% /callout %}}

At a high level, three things happen when you import a module (or package). The module is:

1. Searched for
2. Loaded
3. Bound to a namespace

For the usual imports—those done with the `import` statement—all three steps happen automatically. When you use `importlib`, however, **ONLY the first two steps** are automatic. You need to bind the module to a variable or namespace yourself.

{{% callout note %}}
Even when you import only one attribute from a module, the whole module is loaded and executed. The rest of the contents of the module just aren’t bound to the current namespace. 
{{% /callout %}}

The module cache plays a very important role in the Python import system. The first place Python looks for modules when doing an import is in `sys.modules`. If Python finds a module in the module cache, then it won’t bother searching the import path for the module. If a module is already available, then it isn’t loaded again.

### Reloading modules

Use **[`importlib.reload()`](https://docs.python.org/library/importlib.html#importlib.reload)** to reload a module.

Example:

```python
>>> import number
>>> number.answer
24

>>> # Update number.py in your editor. Now `number.answer` is changed to 42.

>>> import importlib
>>> importlib.reload(number)
<module 'number' from 'number.py'>

>>> number.answer
42
```

## Import Tips and Tricks

### Handle packages across Python versions

Sometimes you need to deal with packages that have different names depending on the Python version. As long as the different versions of the package are compatible, you can handle this by renaming the package with `as`.

Example:

```python
try:
    from importlib import resources
except ImportError:
    import importlib_resources as resources
```

In the rest of the code, you can refer to `resources` and not worry about whether you’re using `importlib.resources` or `importlib_resources`. 👏

### Handle missing packages: Use an alternative

This case is similar to the one above. Also use `try...except` to handle.

```python
try:
    # import the desired package
except ImportError:
    # import an alternative
```

## Reference

- [Python import: Advanced Techniques and Tips](https://realpython.com/python-import/)