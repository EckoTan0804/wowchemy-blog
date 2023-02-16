---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 2002
# ============================================================

# ========== Basic metadata ==========
title: Logging
date: 2023-01-11
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

Logging is a very useful tool in a programmer’s toolbox.

- It helps you develop a better understanding of the flow of a program

- It helps you discover scenarios that you might not even have thought of while developing

Logs

- provide developers with an extra set of eyes that are constantly looking at the flow that an application is going through

- can store information

- If an error occurs, can provide more insights than a stack trace by telling you what the state of the program was before it arrived at the line of code where the error occurred.

## The Logging Module

```python
import logging
```

5 standard levels indicating the severity of events (in the increasing order)

| Logging level | Value | Usage                                                        | Possible message output                                      |
| :------------ | ----- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **Debug**     | 10    | Problem diagnosis, very detailed                             | Unexpected indentation in line XY                            |
| **Info**      | 20    | Gives feedback stating that the system is running properly   | Function 1*1 is executed                                     |
| **Warning**   | 30    | The application is working properly to the greatest possible extent, but an unexpected situation has occurred or a warning has been issued about a future problem | Storage space becomes scarce                                 |
| **Error**     | 40    | A function could not be executed because a problem occurred  | An error occurred and the action was canceled                |
| **Critical**  | 50    | A serious problem has occurred and the entire application may need to be stopped | Serious error: The program cannot access this service and must be terminated |

![](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/1*aHKt_H9yzoU_gcSlfQgDpQ.png)

Logging with default logger:

```python
import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

Output:

```shell
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
```

- Default output format: evel, name, and message separated by a colon (`:`)

- The `debug()` and `info()` messages didn’t get logged.

  - By default, the logging module logs the messages with a severity level of `WARNING` or above.

  - You can change that by configuring the logging module to log events of all levels if you want.

## Basic Configurations

 You can use the `basicConfig(**kwargs)` method to configure the logging. Some of the commonly used parameters for `basicConfig()` are:

- `level`: The root logger will be set to the specified severity level.

  ```python
  import logging
  
  logging.basicConfig(level=logging.DEBUG)
  logging.debug('This will get logged')
  ```

  ```shell
  DEBUG:root:This will get logged
  ```

- `filename`: file where the log information will be output to

- `filemode`: If `filename` is given, the file is opened in this mode. The default mode is `a` (append).

- `format`: format of the log message.

  ```python
  import logging
  
  logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
  
  # The log message will be ouput to `app.log`
  logging.warning('This will get logged to a file') 
  ```

More parameters can be found [here](https://docs.python.org/3/library/logging.html#logging.basicConfig).

Note: calling `basicConfig()` to configure the root logger works only if the root logger has not been configured before. **Basically, this function can only be called once.**

## Formatting the Output

There are some basic elements that are already a part of the `LogRecord` and can be easily added to the output format, e.g.,

- asctime `%(asctime)s`

  - The format can be changed using the `datefmt` attribute, which uses the same formatting language as the formatting functions in the datetime module

- message `%(message)s`

- name`%(name)s`

The entire list of available attributes can be found [here](https://docs.python.org/3/library/logging.html#logrecord-attributes).

Example:

```python
logging.basicConfig(
    level=logging.DEBUG,
    format=f"[%(asctime)s] - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logging.info("User log in")
```

```shell
[2023-01-11 13:50:25] - INFO - User log in
```

### Logging Variable Data

Logging methods take a string as an argument $\rightarrow$ We can format a string with variable data using f-string.

Example:

```python
user_name = "John"

logging.basicConfig(
    level=logging.DEBUG,
    # filename="test.log",
    # filemode="w",
    format=f"[%(asctime)s] - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logging.info(f"{user_name} log in")
```

```shell
[2023-01-11 13:55:23] - INFO - John log in
```

### Capturing Stack Traces

The logging module also allows you to capture the full stack traces in an application. [Exception information](https://realpython.com/python-exceptions/) can be captured if the `exc_info` parameter is passed as `True`.

Example:

```python
import logging

a = 5
b = 0

try:
    c = a / b
except Exception as e:
    logging.error("Exception occurred", exc_info=True)    
```

```shell
ERROR:root:Exception occurred
Traceback (most recent call last):
  File "exceptions.py", line 6, in <module>
    c = a / b
ZeroDivisionError: division by zero
```

If `exc_info` is not set to `True`, the output of the above program would not tell us anything about the exception. 

If you’re logging from an exception handler, use the `logging.exception()` method, which logs a message with level `ERROR` and adds exception information to the message. Calling `logging.exception()` is like calling `logging.error(exc_info=True)`, which always dumps exception information.

## Classes and Functions

You can (and should) define your own logger by [creating an object](https://realpython.com/python3-object-oriented-programming/) of the `Logger` class, especially if your application has multiple modules.

The most commonly used classes defined in the logging module are:

- **`Logger`:** the class whose objects will be used in the application code directly to call the functions.

- **`LogRecord`**: Loggers automatically create `LogRecord` objects that have all the information related to the event being logged, like the name of the logger, the function, the line number, the message, and more.

- **`Handler`:**

  - Send the `LogRecord` to the required output destination, like the console or a file.

  - `Handler` is a base for subclasses like `StreamHandler`, `FileHandler`, `SMTPHandler`, `HTTPHandler`, and more. These subclasses send the logging outputs to corresponding destinations.

- **`Formatter`:**  specify the format of the output by specifying a string format that lists out the attributes that the output should contain.

- **`Filters`**: provide a finer grained facility for determining which log records to output.

We mostly deal with the objects of the `Logger` class, which are instantiated using the module-level function `logging.getLogger(name)`. Multiple calls to `getLogger()` with the same `name` will return a reference to the same `Logger` object, which saves us from passing the logger objects to every part where it’s needed.

Example:

```python
import logging

logger = logging.getLogger('example_logger')
```

This creates a custom logger named `example_logger`. 

- Unlike the root logger, the name of a custom logger is not part of the default output format and has to be added to the configuration.

- a custom logger can’t be configured using `basicConfig()`. You have to configure it using Handlers and Formatters.

## Using Handlers

Handlers are useful when you want to configure your own loggers and send the logs to multiple places when they are generated.

- A logger that you create can have more than one handler $\rightarrow$ you can set it up to be output to a standard output stream and saved to a log file as well.

- You can also set the severity level in handlers

  - This is useful if you want to set multiple handlers for the same logger but want different severity levels for each of them. E.g., logs with level `WARNING` and above to be logged to the console, but everything with level `ERROR` and above should also be saved to a file

#### Example

```python
import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
file_handler = logging.FileHandler("file.log")
file_handler.setLevel(logging.ERROR)

# Create formatters and add to handlers
date_format="%Y-%m-%d %H:%M:%S"
console_format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt=date_format,
)
console_handler.setFormatter(console_format)
file_format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt=date_format,
)
file_handler.setFormatter(file_format)


# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.warning('This is a warning')
logger.error('This is an error')
```

```shell
2023-01-11 14:55:01 - __main__ - WARNING - This is a warning
2023-01-11 14:55:01 - __main__ - ERROR - This is an error
```

`file.log`

```
2023-01-11 14:55:01 - __main__ - ERROR - This is an error
```

Here, `logger.warning()` is creating a `LogRecord` that holds all the information of the event and passing it to all the Handlers: `console_handler` and `file_handler`.

- `console_handler` is a `StreamHandler` with level `WARNING` and takes the info from the `LogRecord` to generate an output in the format specified and prints it to the console.

- `file_handler` is a `FileHandler` with level `ERROR`, and it ignores this `LogRecord` as its level is `WARNING`.

When `logger.error()` is called, 

- `console_handler`  behaves exactly as before

- `file_handler` gets a `LogRecord` at the level of `ERROR`, so it proceeds to generate an output and writes it to the specified file

Note: The name of the logger corresponding to the `__name__` variable is logged as `__main__`, which is the name Python assigns to the module where execution starts. If this file is imported by some other module, then the `__name__` variable would correspond to its name *logging_example*.

## Other Configuration Methods

Except using the module and class functions to configure logging (as above), you can also configure logging by create a **config file** or a **dictionary **and loading it using `fileConfig()` or `dictConfig()`, respectively.

### File configuration

`logging.conf`

```toml
[loggers]
keys=root,sampleLogger

[handlers]
keys=consoleHandler

[formatters]
keys=sampleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_sampleLogger]
level=DEBUG
handlers=consoleHandler
qualname=sampleLogger
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=sampleFormatter
args=(sys.stdout,)

[formatter_sampleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

- There are two loggers, one handler, and one formatter

- After their names are defined, they are configured by adding the words logger, handler, and formatter before their names separated by an underscore.

Use `fileConfig()` to load this config file

```python
import logging
import logging.config
from pathlib import Path

logging_conf_path = Path(__file__).parent.joinpath("logging.conf")
assert logging_conf_path.exists()

logging.config.fileConfig(fname=logging_conf_path, disable_existing_loggers=False)

logger = logging.getLogger(__name__)
logger.debug("This is a debug message.")
```

### Dictionary configuration

Same configuration in a [YAML](https://realpython.com/python-yaml/) format for the dictionary approach:

To configure loggers or handlers, specify attributes as key-values pairs in yaml. 

Example:

```yaml
handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
```

is equivalent to

```python
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
```

#### Example: `logging_config.yaml`

```yaml
version: 1
formatters:
  simple:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: simple
    stream: ext://sys.stdout
loggers:
  sampleLogger:
    level: DEBUG
    handlers: [console]
    propagate: no
root:
  level: DEBUG
  handlers: [console]
```

```python
import logging
import logging.config
import yaml
from pathlib import Path

config_file_path = Path(__file__).parent.joinpath("logging_config.yaml")
assert config_file_path.exists()

with open(config_file_path) as f:
    config = yaml.safe_load(f)
    logging.config.dictConfig(config)
    
logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
```

## Gotchas

### `setLevel()` is being ignored

In Python `logging` package, there are two `setLevel()` methods:

- The [`setLevel()` of `Logger`](https://docs.python.org/3/library/logging.html) determines which severity *level* of messages it will pass to its handlers. Logging messages which are less severe than *level* will be ignored.
- The `setLevel()` of `Logger` determines which level of messages that handler will send on.

Reference: [Logging level is info, but only warnings are shown. Python logging - Stack Overflow](https://stackoverflow.com/questions/64783221/logging-level-is-info-but-only-warnings-are-shown-python-logging)

## Reference

- [Logging in Python – Real Python](https://realpython.com/python-logging/#the-logging-module)