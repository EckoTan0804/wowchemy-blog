---
# Title, summary, and position in the list
# linktitle: ""
summary: ""
weight: 630

# Basic metadata
title: "Random Forest"
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

<img src="https://i.stack.imgur.com/iY55n.jpg" style="zoom:80%; background-color:white">

Train a group of Decision Tree classifiers (generally via the bagging method (or sometimes pasting)), each on a different random subset of the training set


To make predictions, just obtain the preditions of all individual trees, then predict the class that gets the **most** votes.

## Why is Random Forest good?

The Random Forest algorithm **introduces extra randomness** when growing trees; instead of searching for the very best feature when splitting a node, it searches for the best feature among a random subset of features. **This results in a greater tree diversity, which (once again) trades a higher bias for a lower variance, generally yielding an overall better model.** 👏