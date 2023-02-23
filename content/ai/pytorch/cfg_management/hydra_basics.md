---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 502
# ============================================================

# ========== Basic metadata ==========
title: "Hydra: Basics"
date: 2023-02-23
draft: false
type: book # page type
authors:
  - admin
tags:
  - Deep Learning
  - PyTorch
  - Config Management
  - Hydra
categories:
  - Deep Learning
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

![GitHub - facebookresearch/hydra: Hydra is a framework for elegantly  configuring complex applications](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/Hydra-Readme-logo2.svg)

**Hydra is an open-source Python framework that simplifies the development of research and other complex applications.** The name Hydra comes from its ability to run multiple similar jobs - much like a Hydra with multiple heads.

Key features

- Hierarchical configuration composable from multiple sources
- Configuration can be specified or overridden from the command line
- Dynamic command line tab completion
- Run your application locally or launch it to run remotely
- Run multiple jobs with different arguments with a single command

Installation:

```bash
$ pip install hydra-core --upgrade
```



## Specifying a Config File

- Hydra configuration files are yaml files and should have the `.yaml` file extension.

- Specify the config name by passing a `config_name` parameter to the **@hydra.main()** decorator. Note that you should omit the **.yaml** extension.

- Specify the directory containing it relative to the application by passing `config_path`.

- When running the script, use `++` to override a config value if it's already in the config, or add it otherwise.

#### Example

```
|- config.yaml
|- my_app.py
```

```yaml
# config.yaml
db: 
  driver: mysql
  user: omry
  password: secret
```

```python
from omegaconf import DictConfig, OmegaConf
import hydra

@hydra.main(version_base=None, config_path=".", config_name="config")
def my_app(cfg):
    print(OmegaConf.to_yaml(cfg))

if __name__ == "__main__":
    my_app()
```

Hydra creates an empty `cfg` object and passes it to the function annotate with `@hydra.main`

`config.yaml` is loaded automatically when you run your application.

```bash
$ python my_app.py
db:
  driver: mysql
  user: omry
  password: secret
```

> Note: `config_path` and `config_name` can also be specified in command line instead of in code.
>
> ```bash
> $ python my_app.py --config-path=. --config-name="config"
> ```

We can use `++` to override a config value if it's already in the config, or add it otherwise:

```bash
# Override an existing item
$ python my_app.py ++db.password=1234
db:
  driver: mysql
  user: omry
  password: 1234


# Add a new item
$ python my_app.py ++db.timeout=5
db:
  driver: mysql   
  user: omry      
  password: secret
  timeout: 5 
```

## Using the Config Object

Hydra's configuration object is an instance of `OmegaConf`'s DictConfig. More about `OmegaConf` see [here](https://omegaconf.readthedocs.io/en/latest/usage.html#access-and-manipulation).

#### Example

```yaml
# config.yaml
node:                         # Config is hierarchical
  loompa: 10                  # Simple value
  zippity: ${node.loompa}     # Value interpolation
  do: "oompa ${node.loompa}"  # String interpolation
  waldo: ???                  # Missing value, must be populated prior to access
```

```python
# main.py


from omegaconf import DictConfig, OmegaConf
import hydra

@hydra.main(version_base=None, config_path=".", config_name="config")
def my_app(cfg: DictConfig):
    assert cfg.node.loompa == 10          # attribute style access
    assert cfg["node"]["loompa"] == 10    # dictionary style access

    assert cfg.node.zippity == 10         # Value interpolation
    assert isinstance(cfg.node.zippity, int)  # Value interpolation type
    assert cfg.node.do == "oompa 10"      # string interpolation

    cfg.node.waldo                        # raises an exception

if __name__ == "__main__":
    my_app()
```

## Grouping Config Files

A ***Config Group*** is a named group with a set of valid options. Selecting a non-existent config option generates an error message with the valid options.

### Creating config groups

To create a config group, create a directory to hold a file for each configuration option.

For example, suppose we want to benchmark your application on each of PostgreSQL and MySQL. We create a directory, e.g. `db`,  to hold a file for each database config option.

Directory layout

```
├─ conf
│  └─ db
│      ├─ mysql.yaml
│      └─ postgresql.yaml
└── my_app.py
```

`db/mysql.yaml`

```yaml
driver: mysql
user: omry
password: secret
```

`db/postgresql.yaml`

```yaml
driver: postgresql
user: postgres_user
password: drowssap
timeout: 10
```

### Using config groups

Since we moved all the configs into the `conf` directory, we need to tell Hydra where to find them using the `config_path` parameter. **`config_path` is a directory relative to `my_app.py`**.

```python
# my_app.py

from omegaconf import DictConfig, OmegaConf
import hydra

@hydra.main(version_base=None, config_path="conf")
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))

if __name__ == "__main__":
    my_app()
```

Running `my_app.py` without requesting a configuration will print an empty config.

```bash
$ python my_app.py
{}
```

Select an item from a config group with `+GROUP=OPTION`:

```bash
$ python my_app.py +db=postgresql
db:
  driver: postgresql
  pass: drowssap
  timeout: 10
  user: postgres_user
```

You can still override individual values in the resulting config:

```bash
$ python my_app.py +db=postgresql db.timeout=20
db:
  driver: postgresql
  pass: drowssap
  timeout: 20
  user: postgres_user
```

## Selecting default configs

You can add a **Default List** to your config file. A **Defaults List** is a list telling Hydra how to compose the final config object. By convention, it is the *first* item in the config.

The defaults are ordered:

- If multiple configs define the same value, the last one wins.
- If multiple configs contribute to the same dictionary, the result is the combined dictionary.

Example:

We extend the example above by adding a default config file named `default.yaml` in the `conf` directory:

```
├─ conf
│  └─ db
│      ├─ mysql.yaml
│      └─ postgresql.yaml
|  └─ default.yaml
└── my_app.py
```

`default.yaml`:

```yaml
defaults:
  - db: mysql
```

```python
from omegaconf import DictConfig, OmegaConf
import hydra

@hydra.main(version_base=None, config_path="conf", config_name="default")
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))

if __name__ == "__main__":
    my_app()
```

When you run the updated application, MySQL is loaded by default.

```bash
$ python my_app.py
db:
  driver: mysql
  pass: secret
  user: omry
```

#### Overriding a config group default

We can still load PostgreSQL, and override individual values.

```bash
$ python my_app.py db=postgresql db.timeout=20
db:
  driver: postgresql
  pass: drowssap
  timeout: 20
  user: postgres_user
```

We can remove a default entry from the defaults list by prefixing it with ~:

```bash
$ python my_app.py ~db
{}
```

### Composition order of primary config

Your primary config can contain both config values and a Defaults List. In such cases, you should add the `_self_` keyword to your defaults list to specify the composition order of the config file relative to the items in the defaults list.

- If you want your primary config to override the values of configs from the Defaults List, append `_self_` to the **end** of the Defaults List.

  ```yaml
  # config.yaml
  defaults:
    - db: mysql
    - _self_  # primary overrides default 
  
  db:
    user: root
  ```

  ```bash
    # Result config: db.user from config.yaml
  db:
    driver: mysql  # db/mysql.yaml
    pass: secret   # db/mysql.yaml 
    user: root     # config.yaml (the value is overriden by primary confi)
  ```

- If you want the configs from the Defaults List to override the values in your primary config, insert `_self_` as the **first **item in your Defaults List.

  ```yaml
  # config.yaml
  defaults:
    - _self_  # default overrides primary
    - db: mysql
  
  db:
    user: root
  ```

  ```bash
    # Result config: db.user from config.yaml
  db:
    driver: mysql  # db/mysql.yaml
    pass: secret   # db/mysql.yaml 
    user: omry     # db/mysql.yaml 
  ```

## Leveraging Modularity and Composition

Resorting to modularity and composition, we can keep the configs manageable. Instead of creating a numerb of different config files that fully specify each config, **create a single config that specifies the different configuration dimensions, and the default for each.**

#### Example

Directory layout:

```
├── conf
│   ├── config.yaml
│   ├── db
│   │   ├── mysql.yaml
│   │   └── postgresql.yaml
│   ├── schema
│   │   ├── school.yaml
│   │   ├── support.yaml
│   │   └── warehouse.yaml
│   └── ui
│       ├── full.yaml
│       └── view.yaml
└── my_app.py
```

`configy.yaml`

```yaml
defaults:
  - db: mysql
  - ui: full
  - schema: school
```

The resulting default configuration is a composition of the *mysql* database, the *full* ui, and the *school* schema

## Running Hydra

### Multirun from the command-line

You can configure `hydra.mode` in any supported way. The legal values are `RUN` and `MULTIRUN`.

Setting `hydra.mode=MULTIRUN` in your input config would make your application multi-run by default. For example, the following shows how to override from the command-line and sweep over **all** 6 combinations of the dbs and schemas.

```bash
$ python my_app.py hydra.mode=MULTIRUN db=mysql,postgresql schema=warehouse,support,school
[2021-01-20 17:25:03,317][HYDRA] Launching 6 jobs locally
[2021-01-20 17:25:03,318][HYDRA]        #0 : db=mysql schema=warehouse
[2021-01-20 17:25:03,458][HYDRA]        #1 : db=mysql schema=support
[2021-01-20 17:25:03,602][HYDRA]        #2 : db=mysql schema=school
[2021-01-20 17:25:03,755][HYDRA]        #3 : db=postgresql schema=warehouse
[2021-01-20 17:25:03,895][HYDRA]        #4 : db=postgresql schema=support
[2021-01-20 17:25:04,040][HYDRA]        #5 : db=postgresql schema=school
```

You can also specify the multirun mode by using `--multirum` (`-m`) argument:

```bash
$ python my_app.py --multirun db=mysql,postgresql schema=warehouse,support,school
```

```bash
python my_app.py -m db=mysql,postgresql schema=warehouse,support,school
```

### Sweeping via `hydra.sweeper.params`

You can also define sweeping in the input configs by overriding `hydra.sweeper.params`.

The multirun example above can be achieved via the following config:

```yaml
hydra:
  sweeper:
    params:
      db: mysql,postgresql
      schema: warehouse,support,school
```

If a sweep is specified in both an input config and at the command line, then the commandline sweep will **take precedence over** the sweep defined in the input config.

### Additional sweep types

See the [Extended Override syntax](https://hydra.cc/docs/advanced/override_grammar/extended/) for details.

## Output/Working directory

Hydra creates a directory for each run and executes your code within that working directory.

The working directory is used to:

- Store the output for the application (For example, a database dump file)
- Store the Hydra output for the run (Configuration, Logs etc)

Every time you run the app, a new working directory is created.

```python
# my_app.py


import hydra
from omegaconf import DictConfig
from pathlib import Path

@hydra.main(version_base=None)
def my_app(cfg: DictConfig) -> None:
    print(f"Current working directory : {Path.cwd()}")
```

```bash
$  python my_app.py hydra.job.chdir=True 
Current working directory : outputs\2023-02-20\10-00-36
```

> Note: By default `hydra.job.chdir=False`, which means `Path.cwd()` will output the directory where the python script locates. To get the log directory, you need to explicitly set `hydra.job.chdir` to `True`.

Structure of the working directory:

```
outputs/2023-02-20/10-00-36
├── .hydra
│   ├── config.yaml
│   ├── hydra.yaml
│   └── overrides.yaml
└── my_app.log
```

- Hydra output directory (`.hydra` by default)

  - `config.yaml`: A dump of the user specified configuration

  - `hydra.yaml`: A dump of the Hydra configuration

  - `overrides.yaml`: The command line overrides used

- `main_app.log`: Application log file created for this run

### Changing or disabling Hydra's output subdir

- You can change the `.hydra` subdirectory name by overriding `hydra.output_subdir`. 

- You can disable its creation by overriding `hydra.output_subdir` to `null`.

#### Accessing the original working directory in your application

With `hydra.job.chdir=True`, you can still access the original working directory by importing `get_original_cwd()` and `to_absolute_path()` in `hydra.utils`.

### Customizing working directory pattern

The output directory can be configured by

- setting `hydra.run.dir` (for single hydra runs) or

- `hydra.sweep.dir`/`hydra.sweep.subdir` (for multirun sweeps).

#### Configuration for single run

Run output directory grouped by date:

```yaml
hydra:
  run:
    dir: ./outputs/${now:%Y-%m-%d}/${now:%H-%M-%S}
```

Run output directory grouped by job name:

```yaml
hydra:
  run:
    dir: outputs/${hydra.job.name}/${now:%Y-%m-%d_%H-%M-%S}
```

Run output directory can contain user configuration variables:

```yaml
hydra:
  run:
    dir: outputs/${now:%Y-%m-%d_%H-%M-%S}/opt:${optimizer.type}
```

More see: [Customizing working directory pattern](https://hydra.cc/docs/configure_hydra/workdir/)

## Logging

By default, Hydra logs at the `INFO` level to both the console and a log file in the automatic working directory.

Example

```python
import logging
from omegaconf import DictConfig
import hydra

# A logger for this file
logger = logging.getLogger(__name__)

@hydra.main()
def my_app(_cfg: DictConfig) -> None:
    logger.info("Info level message")
    logger.debug("Debug level message")

if __name__ == "__main__":
    my_app()
```

We can easily integrate `loguru.logger` for customized logging.

You can enable DEBUG level logging from the command line by overriding `hydra.verbose`.

`hydra.verbose` can be a Boolean, a String or a List:

Examples:

- `hydra.verbose=true` : Sets the log level of **all** loggers to `DEBUG`
- `hydra.verbose=NAME` : Sets the log level of the logger `NAME` to `DEBUG`. Equivalent to `import logging; logging.getLogger(NAME).setLevel(logging.DEBUG)`.
- `hydra.verbose=[NAME1,NAME2]`: Sets the log level of the loggers `NAME1` and `NAME2` to `DEBUG`

## Debug

### Printing the configuration

Print the config for your app *without* running your function by adding `--cfg` or `-c` to the command line.

The `--cfg` option takes one argument indicating which part of the config to print:

- `job`: Your config
- `hydra`: Hydra's config
- `all`: The full config, which is a union of `job` and `hydra`.

You can use --package or -p to display a subset of the configuration:

```bash
$ python my_app.py --cfg hydra --package hydra.job
```

## Reference

- [Hydra official tutorial](https://hydra.cc/docs/tutorials/intro/)