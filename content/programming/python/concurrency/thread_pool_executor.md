---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 1721
# ============================================================

# ========== Basic metadata ==========
title: ThreadPoolExecutor
date: 2024-02-13
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - Concurrency
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

## Executors and Features

The **ThreadPoolExecutor** Python class is used to create and manage thread pools and is provided in the [concurrent.futures module](https://docs.python.org/3/library/concurrent.futures.html). The **ThreadPoolExecutor** extends the **`Executor`** class and will return **`Future`** objects when it is called.

- **Executor**: Parent class for the ThreadPoolExecutor that defines basic lifecycle operations for the pool.
- **Future**: Object returned when submitting tasks to the thread pool that may complete later.

### Executors

The **ThreadPoolExecutor** class extends the abstract **Executor** class.

The **Executor** class defines three methods used to control our thread pool

- **`submit()`**: Dispatch a function to be executed and return a future object.
- **`map()`**: Apply a function to an iterable of elements.
- **`shutdown()`**: Shut down the executor.

The **Executor** is started when the class is created and must be shut down explicitly by calling **shutdown()**, which will release any resources held by the **Executor**.

 **submit()** and **map()** functions are used to submit tasks to the Executor for asynchronous execution.

- The **map()** function operates just like the **built-in map()** function and is used to apply a function to each element in an iterable object (e.g., list). Unlike the built-in **map()** function, each application of the function to an element will happen *asynchronously* instead of sequentially.
- The **submit()** function takes a function, as well as any arguments, and will execute it asynchronously, although the call returns immediately and provides a **Future** object.

### Features

A future is **an object that represents a [delayed result for an asynchronous task](https://en.wikipedia.org/wiki/Futures_and_promises).**

- It is also sometimes called a **{{< hl >}}promise{{< /hl >}}** or a **{{< hl >}}delay{{< /hl >}}**. 
- It provides a context for the result of a task that may or may not be executing and a way of getting a result once it is available.
- In Python, the `Future` object is returned from an `Executor`, such as a `ThreadPoolExecutor` when calling the **submit()** function to dispatch a task to be executed asynchronously.
- In general, we do *not* create Future objects; we only receive them and we may need to call functions on them. There is always one `Future` object for each task sent into the `ThreadPoolExecutor` via a call to `submit()`.

The `Future` object provides a number of helpful functions for inspecting the status of the task

- **`cancelled()`**: Returns **`True`** if the task was cancelled before being executed.
- **`running()`**: Returns **`True`** if the task is currently running.
- **`done()`**: Returns **`True`** if the task has completed or was cancelled.

A running task cannot be cancelled and a done task could have been cancelled.

A `Future` object also provides access to the result of the task via the **`result()`** function. If an exception was raised while executing the task, it will be re-raised when calling the `result()` function or can be accessed via the **`exception()`** function.

- `result()`: Access the result from running the task.
- `exception(): Access any exception raised while running the task.

Both the `result()` and `exception()` functions allow a timeout to be specified as an argument, which is the number of seconds to wait for a return value if the task is not yet complete. If the timeout expires, then a **`TimeoutError`** will be raised.

If we want to have the thread pool automatically call a function once the task is completed, we can attach  a callback to the `Future` object for the task via the **`add_done_callback()`** function.

- **`add_done_callback()`**: Add a callback function to the task to be executed by the thread pool once the task is completed.
  - We can add more than one callback to each task and they will be executed in the order they were added. If the task has already completed before we add the callback, then the callback is executed immediately.
  - Any exceptions raised in the callback function will not impact the task or thread pool.

## ThreadPoolExecutor Lifecycle

There are four main steps in the [lifecycle of using the ThreadPoolExecutor class](https://superfastpython.com/threadpoolexecutor-quick-start-guide/);

- Create: Create the thread pool by calling the constructor **T`hreadPoolExecutor()`**.
- Submit: Submit tasks and get futures by calling **`submit()`** or **`map()`**.
- Wait: Wait and get results as tasks complete (optional).
- Shut down: Shut down the thread pool by calling **`shutdown()`**.

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-02-18%2018.44.08.png" alt="截屏2024-02-18 18.44.08" style="zoom:50%;" />



### 1. Create the Thread Pool

When an instance of a **`ThreadPoolExecutor`** is created, it must be configured with 

- the fixed number of threads in the pool

  - Default Total Threads = (Total CPUs) + 4

    > if you have 4 CPUs, each with hyperthreading (most modern CPUs have this), then Python will see 8 CPUs and will allocate (8 + 4) or 12 threads to the pool by default.

  - It is typically not a good idea to have thousands of threads as it may start to impact the amount of available RAM and results in a large amount of switching between threads, which may result in worse performance.

- a prefix used when naming each thread in the pool, and

- the name of a function to call when initializing each thread along with any arguments for the function

```python
# create a thread pool with the default number of worker threads
executor = ThreadPoolExecutor()

# create a thread pool with 10 worker threads
executor = ThreadPoolExecutor(max_workers=10)
```

### 2. Submit tasks to the thread pool

Once the thread pool has been created, you can submit tasks for asynchronous execution. There are two main approaches for submitting tasks defined on the Executor parent class: `map()` and `submit()`.

#### Submit tasks with `map`

The **`map()`** function is an *asynchronous* version of the [built-in map() function](https://docs.python.org/3/library/functions.html#map) for applying a function to each element in an iterable, like a list. You can call the [map() function](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.map) on the pool and pass it the name of your function and the iterable. One common use case to use `map()` is to convert a `for`-loop to run using one thread per loop iteration:

```python
# perform all tasks in parallel
results = pool.map(my_task, my_items) # does not block
```

- `my_task` : the name of the function you want to execute
- `my_items`: iterable of objects, each to be executed by the `my_task` function 

The tasks will be queued up in the thread pool and executed by worker threads in the pool as they become available. The `map()` function will return an iterable immediately. This iterable can be used to access the results from the target task function as they are available **in the order that the tasks were submitted (e.g. order of the iterable you provided)**. 

{{% callout note %}}

Even though the tasks are executed concurrently, the `executor.map()` method ensures that the results are returned in the original order of the input iterable.

{{% /callout %}}3

Example:

```python
from time import sleep
from random import random
from concurrent.futures import ThreadPoolExecutor

def task(num):
    sleep(random())
    return num * 2


with ThreadPoolExecutor(10) as executor:
    # execute tasks concurrently and process results in order
    for result in executor.map(task, range(5)):
        # retrieve the result
        print(result)
```

Output:

```0
0
2
4
6
8
```

You can also set a timeout when calling **map()** via the “**timeout**” argument in seconds if you wish to impose a limit on how long you’re willing to wait for each task to complete as you’re iterating, after which a **TimeOut** error will be raised.

```python
# perform all tasks in parallel
# iterate over results as they become available
for result in executor.map(my_task, my_items, timeout=5):
	# wait for task to complete or timeout expires
	print(result)
```

#### Submit tasks with `submit()`

The **`submit()`** function submits one task to the thread pool for execution.

The function takes the name of the function to call and all arguments to the function, then returns a **`Future`** object immediately.

- The `Future` object is a promise to return the results from the task (if any) and provides a way to determine if a specific task has been completed or not.

```python
with ThreadPoolExecutor(10) as executor:
	# submit a task with arguments and get a future object
	future = executor.submit(my_task, arg1, arg2) # does not block
```

- `my_task` : the name of the function you want to execute
- `arg1`, `arg2`: the first and second arguments to pass to the `my_task` function

You can access the result of the task via the **result()** function on the returned **Future** object. This call will block until the task is completed.

```python
# get the result from a future
result = future.result() # blocks
```

You can also set a timeout when calling `result()` via the**`timeout`** argument in seconds if you wish to impose a limit on how long you’re willing to wait for each task to complete, after which a `TimeOut` error will be raised.

```python
# wait for task to complete or timeout expires
result = future.result(timeout=5) # blocks
```







## ThreadPoolExecutor Example



## Reference

- [ThreadPoolExecutor for Thread Pools in Python](https://superfastpython.com/threadpoolexecutor-in-python/#ThreadPoolExecutor_for_Thread_Pools_in_Python)

- [LifeCycle of the ThreadPoolExecutor](https://superfastpython.com/threadpoolexecutor-in-python/#LifeCycle_of_the_ThreadPoolExecutor)
