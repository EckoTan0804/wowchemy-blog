---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 2003
# ============================================================

# ========== Basic metadata ==========
title: loguru
date: 2023-02-16
draft: false
type: book # page type
authors:
  - admin
tags:
  - Python
  - Packages
  - logging
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

![GitHub - Delgan/loguru: Python logging made (stupidly) simple](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/logo.png)

**Loguru** is a library which aims to bring enjoyable logging in Python. It is intended to make Python logging less painful by adding a bunch of useful functionalities that solve caveats of the standard loggers.



## Tutorial

See: [A Complete Guide to Logging in Python with Loguru](https://betterstack.com/community/guides/logging/loguru/)

## `loguru` vs. Built-in `logging`

See

- [Python logging HOWTO: logging vs loguru. Python Practice.](https://alimbekov.com/en/python-logging-vs-loguru/)

Switch from standard `logging` to `loguru`:

- [Switching from standard logging to loguru &mdash; loguru documentation](https://loguru.readthedocs.io/en/stable/resources/migration.html)

- [Replace Python standard logging mechanism with Loguru](https://qxf2.com/blog/replace-python-standard-logging-with-loguru/)

## Issues and Solutions

### Apply default level color in custom format

Use the special tag `<level>` in custom format.

> The special tag `<level>` (abbreviated with `<lvl>`) is transformed according to the configured color of the logged message level.

Reference

- [python - How to use Loguru defaults + and extra information? - Stack Overflow](https://stackoverflow.com/questions/70977165/how-to-use-loguru-defaults-and-extra-information)

- [default message color · Issue #122 · Delgan/loguru · GitHub](https://github.com/Delgan/loguru/issues/122)

### Integrate `rich.logging.RichHandler`

Use[ `configure()` method](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.configure) of `loguru.logger`.

Example:

```python
from rich.logging import RichHandler
from loguru import logger

rich_handler = RichHandler()

logger.configure(
    handlers=[
        {"sink": rich_handler, "format": "{message}"},
    ],
)
```

## Reference

- [loguru documentation](https://loguru.readthedocs.io/en/stable/index.html)

- [A Complete Guide to Logging in Python with Loguru](https://betterstack.com/community/guides/logging/loguru/)

- [Replace Python standard logging mechanism with Loguru](https://qxf2.com/blog/replace-python-standard-logging-with-loguru/)

- [Python logging HOWTO: logging vs loguru. Python Practice.](https://alimbekov.com/en/python-logging-vs-loguru/)