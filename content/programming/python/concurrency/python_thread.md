---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 1720
# ============================================================

# ========== Basic metadata ==========
title: Thread and Thread Pool
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





## Python Threads

A [thread](https://en.wikipedia.org/wiki/Thread_(computing)) refers to a thread of execution by a computer program.

Every Python program is a process with one thread called the ***main thread*** used to execute your program instructions.

- Each process is in fact one instance of the Python interpreter that executes Python instructions (Python bytecode)

Each thread that is created requires the application of resources (e.g. memory for the thread’s stack space). The computational costs for setting up threads can become expensive if we are creating and destroying many threads over and over for ad hoc tasks.

Instead, we would prefer to keep worker threads around for reuse if we expect to run many ad hoc tasks throughout our program. -> This can be achieved using a **thread pool**.

## Thread Pools

A [thread pool](https://en.wikipedia.org/wiki/Thread_pool) is a **programming pattern for automatically managing a pool of worker threads**. The pool is responsible for a fixed number of threads.

- It controls when the threads are created, such as just-in-time when they are needed.

- It also controls what threads should do when they are not being used, such as making them wait without consuming computational resources.

Each thread in the pool is called a **worker** or a **worker thread**. 

- Each worker is *agnostic* to the type of tasks that are executed, along with the user of the thread pool to execute a suite of similar (homogeneous) or dissimilar tasks (heterogeneous) in terms of the function called, function arguments, task duration, and more.

- Worker threads are designed to be re-used once the task is completed and provide protection against the unexpected failure of the task, such as raising an exception, without impacting the worker thread itself.

The pool may provide some facility to configure the worker threads, such as running an initialization function and naming each worker thread using a specific naming convention.

- Thread pools can provide a generic interface for executing ad hoc tasks with a variable number of arguments, but do not require that we choose a thread to run the task, start the thread, or wait for the task to complete.

- It can be significantly more efficient to use a thread pool instead of manually starting, managing, and closing threads, especially with a large number of tasks.

Python provides a thread pool via the **`ThreadPoolExecutor`** class.


## Reference
- [Python Threads and the Need for Thread Pools](https://superfastpython.com/threadpoolexecutor-in-python/#Python_Threads_and_the_Need_for_Thread_Pools)