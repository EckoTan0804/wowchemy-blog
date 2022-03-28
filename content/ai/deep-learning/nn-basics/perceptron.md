---
# Title, summary, and position in the list
# linktitle: ""
summary: ""
weight: 110

# Basic metadata
title: "Perceptron"
date: 2020-09-01
draft: false
type: book # page type
authors: ["admin"]
tags: ["Deep Learning", "Nerual Network Basics"]
categories: ["Deep Learning"]
toc: true # Show table of contents?

# Advanced metadata
profile: false  # Show author profile?

reading_time: true # Show estimated reading time?

share: false  # Show social sharing links?
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

## Structure

A perceptron is

- a single-layer neural network
- used for supervised learning of binary classifiers

{{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/perceptron.png" caption="Perceptron" numbered="true" >}}


$$
g(x) = \underbrace{\sum\_{i=0}^n w\_i x\_i}\_{\text{linear separator}} + \underbrace{w\_0}\_{\text{offset/bias}}
$$

Decision for classification
$$
\hat{y} = \begin{cases} 1 &\text{if } g(x) > 0 \\\\ -1 &\text{else}\end{cases}
$$

## Update Rule

$w=w+y x$ if prediction is wrong

- If label $y=1$ but predict $\hat{y}=-1$: $w = w + x$

- If label $y=-1$ but predict $\hat{y}=1$: $w = w - x$

