---
linktitle: ''
summary: ''
weight: 601
title: IPython and Shell Commands
date: 2020-11-07
draft: false
type: book
authors:
- admin
tags:
- Python
- IPython
categories:
- coding
toc: true
profile: false
reading_time: true
share: true
featured: true
comments: true
disable_comment: false
commentable: true
editable: false
header:
  caption: ''
  image: ''
---

## Shell Commands in IPython

Any command that works at the command-line can be used in IPython by prefixing it with the `!` character.

Example

```python
! echo 'hello world!' # echo is like Python's print function
```

```txt
hello world!
```

```python
! pwd # = print working dir
```

```txt
/tmp
```

{{% callout note %}} 

For Unix shell, more see: [The Unix Shell](http://swcarpentry.github.io/shell-novice/)

{{% /callout %}}

## Passing Values to and from the Shell

Shell commands can not only be called from IPython, but can also be made to interact with the IPython namespace. For example, we can save the output of any shell command to a Python list using the assignment operator.

For example

```python
contents = !ls
contents
```

```txt
['my-project']
```

```python
directory = !pwd
```

```txt
directory
```

Note that these results are not returned as lists, but as a special shell return type defined in IPython:

```python
type(directory)
```

```txt
IPython.utils.text.SList
```

This looks and acts a lot like a Python list, but has additional functionality, such as the `grep` and `fields` methods and the `s`, `n`, and `p` properties that allow us to search, filter, and display the results in convenient ways.

Communication in the other direction–passing Python variables into the shell–is possible using the `{varname} `syntax:

```python
name = 'Ben'
! echo "hello {name}"
```

```txt
hello Ben
```

## Shell-Related ,agic Commands

Shell commands in the notebook are executed in a **temporary subshell**. If we'd like to execute the shell commands in a more enduring way, we can use the `%` magic command.

With `%automagic` magic function, we can enable `automagic` function. Then available shell-like magic functions, such as `%cd `, `%cat`, `%cp`, `%env`, `%ls`, `%man`, `%mkdir`, `%more`, `%mv`, `%pwd`, `%rm`, and `%rmdir`, can be used without the `%` sign.

## Magic Commands

There are two types of magic commands

- Line magics: start with `%`
- Cell magics: start with `%%`

Useful magic commands:

- `%matplotlib`: activates matplotlib interactive support during an IPython session
- `%run`: runs a Python script from within IPython shell
- `%time`: displays time required by IPython environment to execute a Python expression.
- `%timeit`: uses the Python [timeit module](https://docs.python.org/3.5/library/timeit.html) which runs a statement 100,000 times (by default) and then provides the mean of the fastest three times.
- `%%writefile`: Write the contents of the cell to a file. The file will be overwritten unless the `-a` (–append) flag is specified.

## Reference

- [IPython and Shell Commands](https://jakevdp.github.io/PythonDataScienceHandbook/01.05-ipython-and-shell-commands.html)

- [IPython - Magic Commands](https://www.tutorialspoint.com/jupyter/ipython_magic_commands.htm)

- [28 Jupyter Notebook Tips, Tricks, and Shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)