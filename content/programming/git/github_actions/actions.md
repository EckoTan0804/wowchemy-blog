---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 302
# ============================================================

# ========== Basic metadata ==========
title: Actions Usage
date: 2023-01-05
draft: false
type: book # page type
authors:
  - admin
tags:
  - Coding
  - Git
  - GitHub
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

## Overview

Actions are the building blocks that power your workflow. 

A workflow can contain actions created by the [community](https://github.com/marketplace?category=&query=&type=actions&verification=) or customized directly within your repository.

## Adding an Action to Workflow

### Adding an action from GitHub Marketplace

You can find a number of useful actions in [GitHub Marketplace](https://github.com/marketplace?category=&query=&type=actions&verification=).

An action's listing page includes the action's version and the workflow syntax required to use the action. To keep your workflow stable even when updates are made to an action, you can reference the version of the action to use by specifying the Git or Docker tag number in your workflow file.

Steps:

1. Navigate to the action you want to use in your workflow.

2. Choose the version you want to use and copy the workflow syntax

   ![截屏2023-01-06 14.12.07](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2023-01-06%2014.12.07-20230106145904658.png)

3. Paste the syntax as a new step in your workflow. (For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/automating-your-workflow-with-github-actions/workflow-syntax-for-github-actions#jobsjob_idsteps).")
4. If the action requires you to provide inputs, set them in your workflow. (For information on inputs an action might require, see "[Using inputs and outputs with an action](https://docs.github.com/en/actions/learn-github-actions/finding-and-customizing-actions#using-inputs-and-outputs-with-an-action).")

### Adding an action from the same repository

If an action is defined in the same repository where your workflow file uses the action, you can reference the action with either the ‌`{owner}/{repo}@{ref}` or `./path/to/dir` syntax in your workflow file.

Example:

Repository file structure:

```txt
|-- hello-world (repository)
|   |__ .github
|       └── workflows
|           └── my-first-workflow.yml
|       └── actions
|           |__ hello-world-action
|               └── action.yml
```

Workflow file:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # This step checks out a copy of your repository.
      - uses: actions/checkout@v3
      # This step references the directory that contains the action.
      - uses: ./.github/actions/hello-world-action
```

### Adding an action from a different repository

If an action is defined in a different repository than your workflow file, you can reference the action with the `{owner}/{repo}@{ref}` syntax in your workflow file. The action must be stored in a public repository.

Example:

```yaml
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: actions/setup-node@v3
```

### Referencing a container on Docker Hub

If an action is defined in a published Docker container image on Docker Hub, you must reference the action with the `docker://{image}:{tag}` syntax in your workflow file. 

To protect your code and data, it is strongly recommend you verify the integrity of the Docker container image from Docker Hub before using it in your workflow.

Example:

```yaml
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: docker://alpine:3.8
```

## Using Release Management for Your Custom Actions

Similar to any dependency, you should indicate the version of the action you'd like to use based on your comfort with automatically accepting updates to the action.

You will designate the version of the action in your workflow file. Check the action's documentation for information on their approach to release management, and to see which tag, branch, or SHA value to use.

### Using tags

Tags are useful for letting you decide when to switch between major and minor versions, but these are more ephemeral and can be moved or deleted by the maintainer.

Example:

```yaml
steps:
  - uses: actions/javascript-action@v1.0.1
```

### Using SHAs

- If you need more reliable versioning, you should use the SHA value associated with the version of the action, as SHAs are immutable and therefore more reliable than tags or branches.

- However this approach means you will not automatically receive updates for an action, including important bug fixes and security updates. 
- You must use a commit's full SHA value, and not an abbreviated value. This example targets an action's SHA.

Example:

```yaml
steps:
  - uses: actions/javascript-action@172239021f7ba04fe7327647b213799853a9eb89
```

### Using branches

Specifying a target branch for the action means it will always run the version currently on that branch. However, this approach can create problems if an update to the branch includes breaking changes.

Example:

```yaml
steps:
  - uses: actions/javascript-action@main # targets a branch name `main`
```

## Using Inputs and Outputs with an Action

- An action often accepts or requires inputs and generates outputs that you can use. 
  - E.g., an action might require you to specify a path to a file, the name of a label, or other data it will use as part of the action processing.
- To see the inputs and outputs of an action, check the `action.yml` or `action.yaml` in the root directory of the repository.

Example:

```yaml
name: "Example"
description: "Receives file and generates output"
inputs:
  file-path: # id of input
    description: "Path to test script"
    required: true
    default: "test-file.js"
outputs:
  results-file: # id of output
    description: "Path to results file"
```

- The `inputs` keyword defines a required input called `file-path`, and includes a default value that will be used if none is specified.
- The `outputs` keyword defines an output called `results-file`, which tells you where to locate the results.

## Reference

- [Finding and customizing actions](https://docs.github.com/en/actions/learn-github-actions/finding-and-customizing-actions)