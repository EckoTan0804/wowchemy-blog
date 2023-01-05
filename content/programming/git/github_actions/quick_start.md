---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 301
# ============================================================

# ========== Basic metadata ==========
title: Getting Started
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

## What is GitHub Actions?

GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that **allows you to automate your build, test, and deployment pipeline**. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.



GitHub Actions use **yaml** files to define event, jobs, and steps.

These yaml files are stored in `.github/workflows` directory.  

An **event** automatically triggers the workflow, which contains a **job**. The job then uses the **step**s to control the order, in which the **action**s are run. These actions are the commands that automate the software testing.

## GitHub Actions Components

{{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/1*8mUtip6z_oydfLi4P86KUw.png" caption="Source: [Getting started with GitHub Actions](https://itnext.io/getting-started-with-github-actions-fe94167dbc6d)" numbered="true" >}}

You can configure a GitHub Actions ***workflow*** to be triggered when an ***event*** occurs in your repository, such as a pull request being opened or an issue being created. Your workflow contains one or more ***jobs*** which can run in sequential order or in parallel. Each job will run inside its own virtual machine ***runner***, or inside a container, and has one or more ***steps*** that either run a script that you define or run an ***action***, which is a reusable extension that can simplify your workflow.

### Workflow

A workflow is a configurable automated process that will run one or more jobs. 

- Defined by YAML files in the `.github/workflows` directory in a repository. A repository can have multiple workflows, each of which can perform a different set of tasks. 
- Runs when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule.
- You can reference a workflow within another workflow, see "[Reusing workflows](https://docs.github.com/en/actions/learn-github-actions/reusing-workflows)."

(For more information about workflows, see "[Using workflows](https://docs.github.com/en/actions/using-workflows).")

### Events

An event is a specific activity in a repository that triggers a workflow run. 

- For example, activity can originate from GitHub when someone creates a pull request, opens an issue, or pushes a commit to a repository. 

For a complete list of events that can be used to trigger workflows, see [Events that trigger workflows](https://docs.github.com/en/actions/reference/events-that-trigger-workflows).

### Jobs

A job is a set of **steps** in a workflow that execute on the same runner.

- Each step is either a shell script that will be executed, or an *action* that will be run.
- Steps are executed *in order* and are dependent on each other.
- Each step is executed on the same runner. (you can share data from one step to another. )

By default, jobs have no dependencies and run in *parallel* with each other.

When a job takes a dependency on another job, it will wait for the dependent job to complete before it can run. 

### Actions

- An *action* is a custom application for the GitHub Actions platform that performs a complex but frequently repeated task.

- Use an action to help reduce the amount of repetitive code that you write in your workflow files.
- You can write your own actions (see "[Creating actions](https://docs.github.com/en/actions/creating-actions)"), or you can find actions to use in your workflows in the GitHub Marketplace.

### Runners

A runner is a server that runs your workflows when they're triggered. 

- A runner is a server that runs your workflows when they're triggered. 
- GitHub provides Ubuntu Linux, Microsoft Windows, and macOS runners to run your workflows. Each workflow run executes in a fresh, newly-provisioned virtual machine. 

## Understanding the Workflow File

Let's say we have created a `learn-github-actions.yml` in the `.github/workflows/` directory in the repository:

```yaml
# Optional
# The name of the workflow 
# as it will appear in the "Actions" tab of the GitHub repository. 
name: learn-github-actions

# Optional
# The name for workflow runs generated from the workflow, 
# which will appear in the list of workflow runs on your repository's "Actions" tab.
run-name: ${{ github.actor }} is learning GitHub Actions

# Trigger for this workflow.
# Here we use the `push` event, so a workflow run is triggered every time
# someone pushes a change to the repository or merges a pull request.
on: [push]

jobs: # Group together all the jobs that run in this workflow
  check-bats-version: # Define a job named `check-bats-version`
    runs-on: ubuntu-latest # specify the runner on which this job runs
    steps: # Group together all the steps that run in this job
      # The `uses` keyword specifies that this step will run `v3` of the `actions/checkout` action. 
      # This is an action that checks out your repository onto the runner,`
      # allowing you to run scripts or other actions against your code.
      # You should use the checkout action any time your workflow will run against the repository's code.
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '14'
      
      # The `run` keyword tells the job to execute a command on the runner.
      - run: npm install -g bats
      - run: bats -v
```

Visualize the workflow we created in a hierarchy:

![Workflow overview](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/overview-actions-event.png)

As we can see, each step executes a single action or shell script. Steps 1 and 2 run actions, while steps 3 and 4 run shell scripts.

## View the Activity for a Workflow Run

When your workflow is triggered, a *workflow run* is created that executes the workflow. After a workflow run has started, you can see a visualization graph of the run's progress and view each step's activity on GitHub.

A step by step guide see: [Viewing the activity for a workflow run](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#viewing-the-activity-for-a-workflow-run)

## Quick Start Demo

See [Quickstart for GitHub Actions](https://docs.github.com/en/actions/quickstart)

## Reference

- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
- [Getting started with GitHub Actions](https://itnext.io/getting-started-with-github-actions-fe94167dbc6d)