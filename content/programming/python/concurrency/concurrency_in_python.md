---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 1710
# ============================================================

# ========== Basic metadata ==========
title: Concurrency 101
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

## What is Concurrency?

The dictionary definition of concurrency is **simultaneous occurrence.** In Python, the things that are occurring *simultaneously* are called by different names (thread, task, process) but at a high level, they all refer to **a sequence of instructions that run in order**.

> Think of them as different **trains of thought.** Each one can be stopped at certain points, and the CPU or brain that is processing them can switch to a different one. The state of each one is saved so it can be restarted right where it was interrupted.

But threads, tasks, and processes are different in detail:

- only `multiprocessing` actually runs these trains of thought at literally the same time.

- [`Threading`](https://realpython.com/intro-to-python-threading/) and `asyncio` both run on a *single* processor and therefore only run one at a time. They just cleverly find ways to take turns to speed up the overall process.

  But there is a big difference between `threading` and `asyncio` in the way threads or tasks take turns

  - In `threading`, the operating system actually knows about each thread and can interrupt it at any time to start running a different thread. This is called **[pre-emptive multitasking](https://en.wikipedia.org/wiki/Preemption_(computing)#Preemptive_multitasking)** since the operating system can pre-empt your thread to make the switch.
    - Pre-emptive multitasking is handy in that the code in the thread does *not* need to do anything to make the switch. 
    - It can also be difficult because of that “at any time” phrase. This switch can happen in the middle of a single Python statement, even a trivial one like `x = x + 1`!
  - `Asyncio` uses [cooperative multitasking](https://en.wikipedia.org/wiki/Cooperative_multitasking). The tasks must cooperate by announcing when they are ready to be switched out. That means that the code in the task has to change slightly to make this happen.
    - The benefit of doing this extra work up front is that you always know where your task will be swapped out. It will not be swapped out in the middle of a Python statement unless that statement is marked.

## What is Parallelism?

`multiprocessing` allows us to use all CPU cores we have. With `multiprocessing`, Python creates new processes. 

- A **process** here can be thought of as almost a completely different program, though technically they’re usually defined as a collection of resources where the resources include memory, file handles and things like that. *One way to think about it is that each process runs in its own Python interpreter.*

- Because they are different processes, each of your trains of thought in a multiprocessing program can run on a different core. Running on a different core means that they *actually can run at the same time*, which is fabulous 👏. There are some complications that arise from doing this, but Python does a pretty good job of smoothing them over most of the time.

Comparison between concurrency and parallelism:

| Concurrency Type                       | Switching Decision                                           | Number of Processors |
| -------------------------------------- | ------------------------------------------------------------ | -------------------- |
| Pre-emptive multitasking (`threading`) | The operating system decides when to switch tasks external to Python. | 1                    |
| Cooperative multitasking (`asyncio`)   | The tasks decide when to give up control.                    | 1                    |
| Multiprocessing (`multiprocessing`)    | The processes all run at the same time on different processors. | Many                 |



## When is Concurrency Useful?

Concurrency can make a big difference for two types of problems: **I/O-bound** and **CPU-bound**.

I/O-bound problems cause your program to slow down because *it frequently must wait for [input/output](https://realpython.com/python-input-output/) (I/O) from some external resource*. They arise frequently when your program is working with things that are much slower than your CPU.

![Timing Diagram of an I/O Bound Program](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/IOBound.4810a888b457.png)

**CPU-bound** programs: classes of programs that do significant computation without talking to the network or accessing a file. In this case, he resource limiting the speed of your program is the CPU, not the network or the file system.

![CPUBound.d2d32cb2626c](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/CPUBound.d2d32cb2626c.png)

| I/O-Bound Process                                            | CPU-Bound Process                                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Your program spends most of its time talking to a slow device, like a network connection, a hard drive, or a printer. | You program spends most of its time doing CPU operations.    |
| Speeding it up involves overlapping the times spent waiting for these devices. | Speeding it up involves finding ways to do more computations in the same amount of time. |





## How to Speed Up an I/O-Bound Program?







## How to Speed Up a CPU-Bound Program?

 A CPU-bound problem does few I/O operations, and its overall execution time is a factor of how fast it can process the required data.

We’ll use a somewhat silly function to create something that takes a long time to run on the CPU

```python
def cpu_bound(number):
    # computes the sum of the squares of each number from 0 to the passed-in value
    return sum(i * i for i in range(number))
```

### Synchronous Version

```python
import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    for number in numbers:
        cpu_bound(number)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
```

This code calls `cpu_bound()` 20 times with a different large number each time. It does all of this on a single thread in a single process on a single CPU. The execution timing diagram looks like this:

![CPUBound.d2d32cb2626c](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/CPUBound.d2d32cb2626c-20240213160924535.png)

This program takes about 7.1 seconds on my machine:

```
Duration 7.118567943572998 seconds
```

### CPU-Bound `multiprocessing` Version

`multiprocessing` is explicitly designed to share heavy CPU workloads across multiple CPUs. Here’s what its execution timing diagram looks like:

![CPUMP.69c1a7fad9c4](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/CPUMP.69c1a7fad9c4.png)

Let's apply `multiprocessing` to accelerate our code above:

```python
import multiprocessing
import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
```

- In `find_sums()`, we change from looping through the numbers to creating a `multiprocessing.Pool` object and using its `.map()` method to send individual numbers to worker-processes as they become free
- The `multiprocessing.Pool()` constructor has the `processes` optional parameter.
  -  You can specify how many `Process` objects you want created and managed in the `Pool`. By default, it will determine how many CPUs are in your machine and create a process for each one.
  - In a production environment, you might want to have a little more control.

In my machine, the running time is reduced to about 2.3 seconds.

```
Duration 2.3258490562438965 seconds
```







## When to Use Concurrency?







## Reference

- [Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency/#what-is-concurrency)