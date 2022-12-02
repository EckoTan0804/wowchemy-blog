---
# ===== Title, summary, and position in the left sidebar =====
linktitle: Getting Started # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 1211
# ============================================================

# ========== Basic metadata ==========
title: Getting Started with Python Testing
date: 2022-12-02
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - Testing
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

## Testing Your Code

### Automated vs. Manual Testing

**Exploratory testing** 

- A form of testing that is done without a plan. You’re just exploring the application.
- To have a complete set of manual tests, all you need to do is make a list of all the features your application has, the different types of input it can accept, and the expected results.
- Every time you make a change to your code, you need to go through every single item on that list and check it. 🤯

 **Automated testing** 

- Execution of your test plan (the parts of your application you want to test, the order in which you want to test them, and the expected responses) by a script instead of a human

### Unit Tests vs. Integration Tests

**Integration testing**: testing *multiple* components

- Major challenge: When an integration test doesn’t give the right result, it’s very hard to diagnose the issue without being able to isolate which part of the system is failing.

**Unit test**: checks that a *single* component operates in the right way → helps you to isolate what is broken in your application and fix it faster.

### Choosing a Test Runner

The three most popular test runners are:

- `unittest`
- `nose` or `nose2`
- `pytest`

#### `unittest`

- Contains both a testing framework and a test runner
- Important requirements for writing and executing tests
  - You put your tests into classes as methods
  - You use a series of special assertion methods in the `unittest.TestCase` class instead of the built-in `assert` statement

`nose`

- Compatible with any tests written using the `unittest` framework and can be used as a drop-in replacement for the `unittest` test runner

- If you’re starting from scratch, it is recommended that you use `nose2` instead of `nose`.

`pytest`

- Supports execution of `unittest` test cases
- The real advantage of `pytest` comes by writing `pytest` test cases. ( `pytest` test cases are a series of functions in a Python file starting with the name `test_`.)
- Other great features
  - Support for the built-in `assert` statement instead of using special `self.assert*()` methods
  - Support for filtering for test cases
  - Ability to rerun from the last failing test
  - An ecosystem of hundreds of plugins to extend the functionality

Choosing the best test runner for your requirements and level of experience is important.

Here we will use `unittest`, the Python built-in standard library. 



## Writing Your First Test

### Where to Write the Test

- You can create a folder called `tests/` and split the tests into multiple files
  - It is convention to ensure each file starts with `test_` so all test runners will assume that Python file contains tests to be executed.
  - Some very large projects split tests into more subdirectories based on their purpose or usage.

### How to Structure a Simple Test

Before you dive into writing tests, you’ll want to first make a couple of decisions:

1. What do you want to test?
2. Are you writing a unit test or an integration test?

Then the structure of a test should loosely follow this workflow:

1. Create your inputs
2. Execute the code being tested, capturing the output
3. Compare the output with an expected result

#### Example

Our project folder looks like this:

```
project/
│
├── my_sum/
│   └── __init__.py
|
└── test.py
```

In `my_sum/__init__.py` there is a function called `sum()`:

```python
def sum(arg):
    """takes an iterable (a list, tuple, or set) and adds the values together"""
    total = 0
    for val in arg:
        total += val
    return total
```

The most simple test would be a list of integers. So, in `test.py` with the following Python code:

```python
import unittest

from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    # Execute the test runner by discovering all classes in this file that inherit from `unittest.TestCase`.
    unittest.main()
```

### How to Write Assertions

**Assertion**: validate the output against a known response. 

Some general best practices around how to write assertions:

- Make sure tests are repeatable and run your test multiple times to make sure it gives the same result every time
- Try and assert results that relate to your input data, such as checking that the result is the actual sum of values in the `sum()` example

Some of the most commonly used methods in `unittest`:

| Method                    | Equivalent to      |
| ------------------------- | ------------------ |
| `.assertEqual(a, b)`      | `a == b`           |
| `.assertTrue(x)`          | `bool(x) is True`  |
| `.assertFalse(x)`         | `bool(x) is False` |
| `.assertIs(a, b)`         | `a is b`           |
| `.assertIsNone(x)`        | `x is None`        |
| `.assertIn(a, b)`         | `a in b`           |
| `.assertIsInstance(a, b)` | `isinstance(a, b)` |

`.assertIs()`, `.assertIsNone()`, `.assertIn()`, and `.assertIsInstance()` all have opposite methods, named `.assertIsNot()`, and so forth.

### Side Effects

**Side effects** means executing a piece of code will alter other things in the environment, such as the attribute of a class, a file on the filesystem, or a value in a database.

Side effects are quiet often and are an important part of testing. Decide if the side effect is being tested before including it in your list of assertions.

If you find that the unit of code you want to test has lots of side effects, you might be breaking the [Single Responsibility Principle](https://en.wikipedia.org/wiki/Single_responsibility_principle).

- Breaking the Single Responsibility Principle means the piece of code is doing *too many* things and would be better off being refactored. 
- Following the Single Responsibility Principle is a great way to design code that it is easy to write repeatable and simple unit tests for, and ultimately, reliable applications.

### Executing Test Runners

The Python application that executes your test code, checks the assertions, and gives you test results in your console is called the **test runner**. 

There are many ways to execute the `unittest` test runner:

- When you have a single test file named `test.py`, simply run `python test.py`

- Another way is using the `unittest` command line

  ```shell
  $ python -m unittest test
  ```

  - You can provide additional options to change the output. One of those is `-v` for verbose

    ```shell
    $ python -m unittest -v test
    test_list_int (test.TestSum) ... ok
    
    ----------------------------------------------------------------------
    Ran 1 tests in 0.000s
    ```

- Instead of providing the name of a module containing tests, you can request an auto-discovery

  ```shell
  $ python -m unittest discover
  ```

  This will search the current directory for any files named `test*.py` and attempt to test them.

- Once you have multiple test files, as long as you follow the `test*.py` naming pattern, you can provide the name of the directory instead by using the `-s` flag and the name of the directory:

  ```shell
  $ python -m unittest discover -s tests
  ```

  `unittest` will run all tests in a single test plan and give you the results.

- If your source code is not in the directory root and contained in a subdirectory, for example in a folder called `src/`, you can tell `unittest` where to execute the tests so that it can import the modules correctly with the `-t` flag:

  ```shell
  $ python -m unittest discover -s tests -t src
  ```

  `unittest` will change to the `src/` directory, scan for all `test*.py` files inside the the `tests` directory, and execute them.

## More Advanced Testing Scenarios

Remember the three basic steps of every test:

1. Create your inputs
2. Execute the code, capturing the output
3. Compare the output with an expected result

However, it’s not always as easy as creating a static value for the input like a string or a number. Sometimes, your application will require an instance of a class or a context. 

The data that you create as an input is known as a **fixture**. It’s common practice to create fixtures and reuse them.

If you’re running the same test and passing different values each time and expecting the same result, this is known as **parameterization**.

### Handling Expected Failures

To test an expected error without causing the test to fail, use `.assertRaises()` as a context-manager, then inside the `with` block execute the test steps.

E.g. we test the `sum()` method, providing it with a bad value, such as a single integer or a string.

```python
import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_bad_type(self):
        """
        This test case will now only pass if sum(data) raises a TypeError. 
        You can replace TypeError with any exception type you choose.
        """
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)

if __name__ == '__main__':
    unittest.main()
```

### Isolating Behaviors in Your Application

Some simple techniques you can use to test parts of your application that have many side effects:

- Refactoring code to follow the Single Responsibility Principle
- Mocking out any method or function calls to remove side effects
- Using integration testing instead of unit testing for this piece of the application

### Writing Integration Tests

Integration testing is the testing of multiple components of the application to check that they work together. Integration testing might require acting like a consumer or user of the application by:

- Calling an HTTP REST API
- Calling a Python API
- Calling a web service
- Running a command line

Each of these types of integration tests can be written in the same way as a unit test, following the Input, Execute, and Assert pattern.

Significant difference from unit tests: 

- Integration tests are checking more components at once and therefore will have more side effects than a unit test
- Integration tests will require more fixtures to be in place, like a database, a network socket, or a configuration file.

A good practice is to **separate your unit tests and your integration tests**. A simple way to separate unit and integration tests is simply to put them in different folders:

```
project/
│
├── my_app/
│   └── __init__.py
│
└── tests/
    |
    ├── unit/
    |   ├── __init__.py
    |   └── test_sum.py
    |
    └── integration/
        ├── __init__.py
        └── test_integration.py
```

## Automating Test Execution

There are some tools for executing tests *automatically* when you make changes and commit them to a source-control repository like Git. Automated testing tools are often known as **CI/CD** tools, which stands for “Continuous Integration/Continuous Deployment.” They can run your tests, compile and publish any applications, and even deploy them into production.

## Reference

- [Getting Started With Testing in Python](https://realpython.com/python-testing/#automating-the-execution-of-your-tests)