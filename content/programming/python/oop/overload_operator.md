---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 520
# ============================================================

# ========== Basic metadata ==========
title: Operator Overloading
date: 2022-05-04
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - basics
  - OOP
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

In Python, methods with `__` (double underscore) prefix and suffix (*e.g.*, `__init__()`) are special methods.They are called **magic methods** or **dunder methods** (dunder for "**d**ouble **under**score"). They can help override functionality for built-in functions for custom classes.

Essentially, each built-in function or operator has a special method corresponding to it. For example, there’s `__len__(),` corresponding to `len()`, and `__add__()`, corresponding to the `+` operator.

By default, most of the built-ins and operators will not work with objects of your classes. You must add the corresponding special methods in your class definition to make your object compatible with built-ins and operators. When you do this, the behavior of the function or operator associated with it changes according to that defined in the method.

## The Internals of Operations

Every class in Python defines its own behavior for built-in functions and methods. Under the hood, when you pass an instance of some class to a built-in function or use an operator on the instance, it is actually equivalent to calling a special method with relevant arguments.

- If there is a **built-in function**, `func()`, and the corresponding special method for the function is `__func__()`, Python interprets a call to the function as `obj.__func__()`, where `obj` is the object.
- In the case of **operators**, if you have an operator `opr` and the corresponding special method for it is `__opr__()`, Python interprets something like `obj1 <opr> obj2` as `obj1.__opr__(obj2)`.

For example

- When you’re calling `len()` on an object, Python handles the call as `obj.__len__()`.

  ```python
  >>> a = 'Real Python'
  >>> len(a)
  11
  >>> a.__len__()
  11
  ```

- When you use the `[]` operator on an iterable to obtain the value at an index, Python handles it as `itr.__getitem__(index)`, where `itr` is the iterable object and `index` is the index you want to obtain.

  ```python
  b = ['Real', 'Python']
  >>> b[0]
  'Real'
  >>> b.__getitem__(0)
  'Real'
  ```

You can see these special methods using the built-in `dir()` function.

## Overloading Built-in Functions

To overload the built-in functions, you only need to define the corresponding special method in your class.

In the following, we'll demonstrate the overloading with some common built-in functions.

###  `len()`: Gives a Length to Your Objects

To change the behavior of `len()`, you need to define the `__len__()` special method in your class. Whenever you pass an object of your class to `len()`, your custom definition of `__len__()` will be used to obtain the result.

Example

```python
class Order:

    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return len(self.cart)
```

```python
>>> order = Order(["apple", "banana"], "Ben")
>>> len(order)
2
```

Use `len()` to directly obtain the length of the cart is more pythonic and more intuitive than calling something like `order.get_cart_len()`. 

### `str()`: Prints Your Objects Prettily 

- The `str()` built-in is used to obtain a user-friendly string representation of the object which can be read by a normal user rather than the programmer. 

- `__str__()` is the method that is used by Python when you call [`print()`](https://realpython.com/python-print/) on your object.
- `__str__()` must return a `str` object

Example

```python
class Order:

    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return len(self.cart)

    def __str__(self):
        return f"{self.customer} has {self.__len__()} products in the cart."
```

```python
>>> order = Order(["apple", "banana"], "Ben")
>>> print(order)
Ben has 2 products in the cart.
```

###  `repr()`: Represents Your Objects

- The `repr()` built-in is used to obtain the *parsable* string representation of an object.
  - An object is parsable means that Python should be able to recreate the object from the representation when `repr` is used in conjunction with functions like [`eval()`](https://realpython.com/python-eval-function/). 
- `repr()` is also the method Python uses to display the object in a REPL session.

Example

```python
class Vector:

    def __init__(self, x_comp, y_comp):
        self.x_comp = x_comp
        self.y_comp = y_comp

    def __repr__(self):
        return f"Vector({self.x_comp}, {self.y_comp})"
```

```python
>>> vector = Vector(3, 4)
>>> repr(vector)
'Vector(3, 4)'

>>> new_vector = eval(repr(vector))
>>> new_vector # Looking at object; __repr__ used
Vector(3, 4)
```

Note:

-  In cases where the `__str__()` method is not defined, Python uses the `__repr__()` method to print the object, as well as to represent the object when `str()` is called on it. 

  ```python
  # In the vector example above, we do not defined __str__() method
  >>> print(new_vector)
  Vector(3, 4) # vector object is printed using __repr__()
  ```

  - If both the methods are missing, it defaults to `<__main__.Vector ...>`.
  - `__repr__()` is the only method that is used to display the object in an interactive session. Absence of it in the class yields `<__main__.Vector ...>`.

- Many of the popular libraries ignore this distinction and use the two methods interchangeably 🤪.

For more about `__repr__()` and `__str__()`, check: [Python String Conversion 101: Why Every Class Needs a “repr”](https://dbader.org/blog/python-repr-vs-str).

### `bool()`: Makes Your Objects Truthy or Falsey

- The `bool()` built-in can be used to obtain the truth value of an object.
- The behavior defined here will determine the truth value of an instance in all contexts that require obtaining a truth value such as in `if` statements.

Example

```python
class Order:

    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return len(self.cart)

    def __str__(self):
        return f"{self.customer} has {self.__len__()} products in the cart."

    def __bool__(self):
        return len(self.cart) > 0
```

```python
>>> order = Order(["apple", "banana"], "Ben")
>>> bool(order)
True
>>> order_2 = Order([], "Amy")
>>> bool(order)
False
```

## Overloading Built-in Operators

Changing the behavior of operators is just as simple as changing the behavior of functions: You define their corresponding special methods in your class, and the operators work according to the behavior defined in these methods.

Usually, these special methods need to accept another argument in the definition other than `self`, generally referred to by the name `other`.

###  `+`: Makes Your Objects Capable of Being Added

- The special method corresponding to the `+` operator is the `__add__()` method.
-  It is recommended that `__add__()` *returns a new instance of the class* instead of modifying the calling instance itself.

Actually this behaviour is quiet often in Python:

```python
>>> a = "Hello"
>>> b = "World"
>>> a + b
`Hello World`
>>> a # remains unchanged
'Hello '
```

```python
>>> list_1 = [1, 2]
>>> list_2 = [3, 4]
>>> list_1 + list_2
[1, 2, 3, 4]
>>> list_1 # remains unchanged
[1, 2]
```

Example (using the `Order` class above):

```python
class Order:

    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return len(self.cart)

    def __str__(self):
        return f"{self.customer} has {self.__len__()} products in the cart."

    def __bool__(self):
        return len(self.cart) > 0

    def __add__(self, other):
        new_cart = self.cart.copy()
        new_cart + other if isinstance(other, list) else new_cart.append(other)
        return Order(new_cart, self.customer)
```

```python
>>> order = Order(["apple", "banana"], "Ben")
>>> (order + "pear").cart # New Order instance
['apple', 'banana', 'pear']
>>> order.cart  # Original instance unchanged
['apple', 'banana']
```

```python
>>> order = order + 'mango'  # Changing the original instance
>>> order.cart
['apple', 'banana', 'mango']
```

Similarly, you have the `__sub__()`, `__mul__()`, and other special methods which define the behavior of `-`, `*`, and so on. These methods should return a new instance of the class as well.

#### Shortcuts: the `+=` operator

- The `+=` operator stands as a shortcut to the expression `obj1 = obj1 + obj2`

- Corresponding special method: `__iadd()__`

- The `__iadd__()` method should make changes *directly* to the `self` argument and return the result, which may or may not be `self`. 

  Roughly, any `+=` use on two objects is equivalent to:

  ```python
  result = obj1 + obj2
  obj1 = resul
  ```

Example:

```python
class Order:

    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return len(self.cart)

    def __str__(self):
        return f"{self.customer} has {self.__len__()} products in the cart."

    def __bool__(self):
        return len(self.cart) > 0

    def __add__(self, other):
        new_cart = self.cart.copy()
        new_cart + other if isinstance(other, list) else new_cart.append(other)
        return Order(new_cart, self.customer)

    def __iadd__(self, other):
        self.cart + other if isinstance(other, list) else self.cart.append(other)
        return self
```

```python
>>> order = Order(["apple", "banana"], "Ben")
>>> order += "mange"
>>> order.cart
['apple', 'banana', 'mange']
```

{{% callout warning %}}

Always make sure that you’re returning something in your implementation of `__iadd__()` and that it is the result of the operation and not anything else.

{{% /callout %}}

Similar to `__iadd__()`, you have `__isub__()`, `__imul__()`, `__idiv__()` and other special methods which define the behavior of `-=`, `*=`, `/=`, and others alike.

### `[]`: Indexes and Slices Your Objects

The `[]` operator is called the indexing operator and is used in various contexts in Python such as g

- etting the value at an index in sequences, 
- getting the value associated with a key in dictionaries, 
- obtaining a part of a sequence through slicing.

You can change its behavior using the `__getitem__()` special method.

Example:

```python
class Order:

    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return len(self.cart)

    def __str__(self):
        return f"{self.customer} has {self.__len__()} products in the cart."

    def __bool__(self):
        return len(self.cart) > 0

    def __add__(self, other):
        new_cart = self.cart.copy()
        new_cart + other if isinstance(other, list) else new_cart.append(other)
        return Order(new_cart, self.customer)

    def __iadd__(self, other):
        self.cart + other if isinstance(other, list) else self.cart.append(other)
        return self

    def __getitem__(self, key):
        return self.cart[key]
```

```python
>>> order = Order(["apple", "banana"], "Ben")
>>> order[1]
'banana'
```

### Reverse Operators: Makes Your Classes Mathematically Correct

While defining the `__add__()`, `__sub__()`, `__mul__()`, and similar special methods allows you to use the operators when your class instance is the *left-hand* side operand, the operator will NOT work if the class instance is the right-hand side operand.

If your class represents a mathematical entity like a vector, a coordinate, or a [complex number](https://realpython.com/python-complex-numbers/), applying the operators should work in *both* the cases since it is a valid mathematical operation. To help you make your classes mathematically correct, Python provides you with **reverse special methods** such as `__radd__()`, `__rsub__()`, `__rmul__()`, and so on.

- These handle calls such as `x + obj`, `x - obj`, and `x * obj`, where `x` is not an instance of the concerned class.
- These reverse special methods should return a *new* instance of class with the changes of the operation rather than modifying the calling instance itself.

## Resource

- [Section 3.3, Special Method Names](https://docs.python.org/3/reference/datamodel.html#special-method-names) of the Data Model section in the Python documentation
- [Fluent Python](https://realpython.com/asins/1491946008/) by Luciano Ramalho
- [Python Tricks: The Book](https://realpython.com/products/python-tricks-book/)

## Reference

- [Operator and Function Overloading in Custom Python Classes](https://realpython.com/operator-function-overloading/)