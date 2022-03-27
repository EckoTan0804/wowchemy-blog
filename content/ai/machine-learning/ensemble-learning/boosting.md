---
# Title, summary, and position in the list
# linktitle: ""
summary: ""
weight: 650

# Basic metadata
title: "Boosting"
date: 2020-11-07
draft: false
type: book # page type
authors: ["admin"]
tags: ["Machine Learning", "Ensemble Learning"]
categories: ["Machine Learning"]
toc: true # Show table of contents?

# Advanced metadata
profile: false  # Show author profile?

reading_time: true # Show estimated reading time?
share: false  # Show social sharing links?
featured: true

comments: true  # Show comments?
disable_comment: false
commentable: true  # Allow visitors to comment?  

editable: false  # Allow visitors to edit the page?  

# Optional header image (relative to `assets/media/` folder).
header:
  caption: ""
  image: ""
---


# Boosting

Refers to any Ensemble method that can **combine serval weak learners into a strong learner**

💡 **General idea: train predictors sequentially, each trying to correct its predecessor.**

Popular boosting methods:
- [AdaBoost]({{< relref "adaboost.md" >}})
- Gradient Boost

