---
# Title, summary, and position in the list
# linktitle: ""
summary: ""
weight: 530

# Basic metadata
title: "Learning in Logistic Regression"
date: 2020-08-03
draft: false
type: book # page type
authors: ["admin"]
tags: ["NLP", "Logistic Regression"]
categories: ["Natural Language Processing"]
toc: true # Show table of contents?

# Advanced metadata
profile: false  # Show author profile?

reading_time: true # Show estimated reading time?
share: true  # Show social sharing links?
featured: true

comments: true # Show comments?
disable_comment: false
commentable: true # Allow visitors to comment? Supported by the Page, Post, and Docs content types.

editable: false  # Allow visitors to edit the page? Supported by the Page, Post, and Docs content types.

# Optional header image (relative to `static/img/` folder).
header:
  caption: ""
  image: ""
---

Logistic regression is an instance of supervised classification in which we know the correct label $y$ (either 0 or 1) for each observation $x$.

The system produces/predicts $\hat{y}$, the estimate for the true $y$. We want to learn parameters ($w$ and $b$) that make $\hat{y}$ for each training observation **as close as possible** to the true $y$. 💪

This requires two components:

- **loss function**: also called **cost function**, a metric measures the distance between the system output and the gold output
  - The loss function that is commonly used for logistic regression and also for neural networks is **[cross-entropy loss]({{< relref "cross-entropy.md" >}})**
- **Optimization algorithm** for iteratively updating the weights so as to minimize this loss function
  - Standard algorithm: [**gradient descent**]({{< relref "gradient-descent.md" >}})

