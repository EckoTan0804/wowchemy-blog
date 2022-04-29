---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 101
# ============================================================

# ========== Basic metadata ==========
title: Git Squashing
date: 2022-04-29
draft: false
type: book # page type
authors:
  - admin
tags:
  - Git ops
categories:
  - Git
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

## What is Git Squashing?

**Git squashing = combine multiple continuous commits into one**

{{< figure src="https://i.ytimg.com/vi/V5KrD7CmO4o/maxresdefault.jpg" caption="Git squash" numbered="true" >}}

## When to use Git Squashing?

Purpose of Git squashing: to keep the branch graph clean :muscle:

Scenarios:

{{< spoiler text="Implementing features" >}}

Usually, we'll commit multiple times before we reach a satisfactory result, such as some fixes and tests. When we've implemented the feature, those intermediate commits look redundant. So, in this case, we may want to squash our commits into one.

{{< /spoiler >}} 

{{< spoiler text="Merging branches" >}}

When we start working on a new feature, we'll start a feature branch. Let's say we've done our work with 20 commits in our feature branch.</br>So, when we merge the feature branch to the master branch, we want to do a squashing to combine the 20 commits into one. In this way, we keep the master branch clean.

{{< /spoiler >}} 

## How to Git Squashing?

We can perform Git squashing via interactive rebase:

```bash
git rebase -i HEAD~{X}
```

`X`  is the number of commits to be squashed.

If `X` is large and not easy to count, we can find the hash of the commit that we want to rebase "onto" (by calling `git log`) and directly rebase on it:

```bash
git rebase -i {hash_onto}
```

### Example

A nich and clear video tutorial:

{{< youtube V5KrD7CmO4o >}}

and its detailed description: [Combining Git commits with squash](https://www.themoderncoder.com/combining-git-commits-with-squash/)

## Reference

- [Squash the Last X Commits Using Git](https://www.baeldung.com/ops/git-squash-commits)

- [How to Squash Commits in Git](https://www.git-tower.com/learn/git/faq/git-squash)

- [【狀況題】把多個 Commit 合併成一個 Commit](https://gitbook.tw/chapters/rewrite-history/merge-multiple-commits-to-one-commit)
