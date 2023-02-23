---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 503
# ============================================================

# ========== Basic metadata ==========
title: "Hydra: Advanced"
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

## Extend Configs

A common pattern is to extend an existing config, overriding and/or adding new config values to it. The extension is done by 

- including the base configuration, and then 

- overriding the chosen values in the current config.

Example:  Extending a config from the same config group

`config.yaml`

```yaml
defaults:
  - db: mysql 
```

`db/mysql.yaml`

```yaml
defaults:
  - base_mysql  # We extend mysql on the base of base_mysql

user: omry
password: secret
port: 3307
encoding: utf8
```

`db/base_mysql.yaml`

```yaml
host: localhost
port: 3306
user: ???
password: ???
```

```bash
$ python my_app.py
db:
  host: localhost   # from db/base_mysql
  port: 3307        # overridden by db/mysql.yaml 
  user: omry        # populated by db/mysql.yaml
  password: secret  # populated by db/mysql.yaml
  encoding: utf8    # added by db/mysql.yaml
```

## Configuring Experiments

To clearly support multiple configurations, each configuration file **only specifies the changes to the master (default) configuration**.

Example:

The default configuration is:

![截屏2023-02-23 23.22.29](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2023-02-23%2023.22.29.png)

The benchmark config files **specify the deltas from the default configuration**:

![截屏2023-02-23 23.22.50](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2023-02-23%2023.22.50.png)

Key concepts:

- **`# @package _global_`**  
  Changes specified in this config should be interpreted as relative to the `_global_` package.  
  We could instead place *nglite.yaml* and *aplite.yaml* next to *config.yaml* and omit this line.
- **The overrides of `/db` and `/server` are absolute paths.**  
  This is necessary because they are outside of the experiment directory.

Running the experiments from the command line requires prefixing the experiment choice with a `+`.

```bash
$ python .\train.py +experiment=aplite
```

### Sweeping over experiments

This approach also enables sweeping over those experiments:

```bash
$ python my_app.py --multirun +experiment=aplite,nglite
```

To run all the experiments, use the [glob](https://hydra.cc/docs/advanced/override_grammar/extended/#glob-choice-sweep) syntax:

```bash
$ python my_app.py --multirun '+experiment=glob(*)'
```

## Specializing Configuration

In some cases the desired configuration should depend on other configuration choices.

Example:

You may want to use only 5 layers in your Alexnet model if the dataset of choice is cifar10, and the default 7 otherwise.

We can start with a config that looks like this:

```yaml
# config.yaml
defaults:
  - dataset: imagenet
  - model: alexnet
```

We want to specialize the config based on the choice of the selected dataset and model.

`OmegaConf` supports value interpolation, we can construct a value that would - at runtime - be a function of other values. The idea is that **we can add another element to the defaults list that would load a file name that depends on those two values**.

Modify `config.yaml`:

```yaml
defaults:
  - dataset: imagenet
  - model: alexnet
  - optional dataset_model: ${dataset}_${model}
```

- The key `dataset_model` is an arbitrary directory, it can be anything unique that makes sense, including nested directory like `dataset/model`.

- `${dataset}_${model}` is using OmegaConf's [variable interpolation](https://omegaconf.readthedocs.io/en/latest/usage.html#variable-interpolation) syntax. At runtime, that value would resolve to *imagenet_alexnet*, or *cifar_resnet* - depending on the values of `defaults.dataset` and `defaults.model`.

- `optional`: By default, Hydra fails with an error if a config specified in the defaults does not exist. In this case we only want to specialize cifar10 + alexnet, not all 4 combinations. the keyword `optional` tells Hydra to just continue if it can't find this file.

Code example see: [hydra/examples/patterns/specializing_config at main · facebookresearch/hydra · GitHub](https://github.com/facebookresearch/hydra/blob/main/examples/patterns/specializing_config)

## Configuring Hydra

Hydra is highly configurable. Many of its aspects and subsystems can be configured, including:

- The Launcher
- The Sweeper
- Logging
- Output directory patterns
- Application help (--help and --hydra-help)

You can include some Hydra config snippet in your own config to override it directly, or compose in different configurations provided by plugins or by your own code. You can also override everything in Hydra from the command line just like with your own configuration.

### Accessing the Hydra config

Hydra is passing to the function annotated by `@hydra.main()`. Two ways to access the Hydra config:

- In your config, using the `hydra` resolver:

  ```yaml
  config_name: ${hydra:job.name}
  ```

  The resolver name is `hydra`, and the `key` is passed after the colon.

- In code, using the `HydraConfig` singleton

  ```python
  from hydra.core.hydra_config import HydraConfig
  
  @hydra.main()
  def my_app(cfg: DictConfig) -> None:
      print(HydraConfig.get().job.name)
  ```

The following variables are populated at runtime:

- [`hydra.job`](https://hydra.cc/docs/configure_hydra/intro/#hydrajob): used for configuring some aspects of your job (more information see: [Job Configuration](https://hydra.cc/docs/configure_hydra/job/))

- [`hydra.run`](https://hydra.cc/docs/configure_hydra/intro/#hydrarun): Used in single-run mode (i.e. when the `--multirun` command-line flag is omitted). See [configuration for run](https://hydra.cc/docs/configure_hydra/workdir/#configuration-for-run).

- [`hydra.sweep`](https://hydra.cc/docs/configure_hydra/intro/#hydrasweep): Used in multi-run mode (i.e. when the `--multirun` command-line flag is given) See [configuration for multirun](https://hydra.cc/docs/configure_hydra/workdir/#configuration-for-multirun).

- [`hydra.runtime`](https://hydra.cc/docs/configure_hydra/intro/#hydraruntime): Fields under **`hydra.runtime`** are populated automatically and should NOT be overridden.

- [`hydra.overrides`](https://hydra.cc/docs/configure_hydra/intro/#hydraoverrides): Fields under **`hydra.overrides`** are populated automatically and should not be overridden.

- [`hydra.mode`](https://hydra.cc/docs/configure_hydra/intro/#hydramode)

For other fields that are present also at the top level of the Hydra Config see: [Other Hydra settings](https://hydra.cc/docs/configure_hydra/intro/#other-hydra-settings).

**Resolvers provided by Hydra**

- **hydra**: Interpolates into the `hydra` config node. e.g. Use `${hydra:job.name}` to get the Hydra job name.

- **now**: Creates a string representing the current time using [strftime](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior). e.g. for formatting the time you can use something like`${now:%H-%M-%S}`.

- **python_version**: Return a string representing the runtime python version by calling `sys.version_info`. Takes an optional argument of a string with the values major, minor or macro. e.g:

## Hydra + wandb

See: [Configuring W&B Projects with Hydra](https://wandb.ai/adrishd/hydra-example/reports/Configuring-W-B-Projects-with-Hydra--VmlldzoxNTA2MzQw)

## Reference

- [Hydra official tutorial](https://hydra.cc/docs/patterns/extending_configs/)