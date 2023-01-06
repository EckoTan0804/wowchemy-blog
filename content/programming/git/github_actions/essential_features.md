---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 303
# ============================================================

# ========== Basic metadata ==========
title: Customization Techniques
date: 2023-01-06
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

GitHub Actions allow you to customize your workflows to meet the unique needs of your application and team.

## Using Variables in Workflow

GitHub Actions include default environment variables for each workflow run. If you need to use custom environment variables, you can set these in your YAML workflow file.

Example:

```yaml
jobs:
  example-job:
      steps:
        - name: Connect to PostgreSQL
          run: node client.js
          env:
            POSTGRES_HOST: postgres
            POSTGRES_PORT: 5432
```

In this example, we create custom variables named `POSTGRES_HOST` and `POSTGRES_PORT`. These variables are then available to the `node client.js` script.

## Add Scripts to Workflow

You can use actions to run scripts and shell commands, which are then executed on the assigned runner. 

Example: use the `run` keyword to execute `npm install -g bats` on the runner.

```yaml
jobs:
  example-job:
    steps:
      - run: npm install -g bats
```

To run a script as an action, you can store the script in your repository and supply the path and shell type. Example:

```yaml
jobs:
  example-job:
    steps:
      - name: Run build script
        run: ./.github/scripts/build.sh
        shell: bash
```

## Sharing Data between Jobs

If your job generates files that you want to share with another job in the same workflow, or if you want to save the files for later reference, you can store them in GitHub as ***artifacts***.

Artifacts are the files created when you build and test your code.

- Might include binary or package files, test results, screenshots, or log files. 
- Are associated with the workflow run where they were created and can be used by another job.

All actions and workflows called within a run have write access to that run's artifacts.

Example: create a file and then upload it as an artifact

```yaml
jobs:
  example-job:
    name: Save output
    steps:
      - shell: bash
        run: | expr 1 + 1 > output.log
      - name: Upload output file
        uses: actions/upload-artifact@v3
        with:
          name: output-log-file
          path: output.log
```

To download an artifact from a separate workflow run, you can use the `actions/download-artifact` action. To download an artifact from the same workflow run, your download job should specify `needs: upload-job-name` so it doesn't start until the upload job finishes.

Example: download the artifact named `output-log-file`.

```yaml
jobs:
  example-job:
    steps:
      - name: Download a single artifact
        uses: actions/download-artifact@v3
        with:
          name: output-log-file
```

## Reference

- [Essential features of GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/essential-features-of-github-actions)