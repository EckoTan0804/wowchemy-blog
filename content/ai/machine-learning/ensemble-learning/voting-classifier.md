---
# Title, summary, and position in the list
# linktitle: ""
summary: ""
weight: 620

# Basic metadata
title: "Voting Classifier"
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

Suppose we have trained a few classifiers, each one achieving about 80% accuracy.

A very simple way to create an even better classifier is to aggregate the predictions of each classifier and predict the class that gets the **most** votes. 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/Voting_Classifier.png" alt="Voting_Classifier" style="zoom:67%;" />

This majority-vote classifier is called a **hard voting classifier**

> Surprisingly, this voting classifier often achieves a higher accuracy than the best classifier in the ensemble. In fact, even if each classifier is a weak learner (meaning it does only slightly better than random guessing), the ensemble can still be a strong learner (achieving high accuracy), provided there are a sufficient number of weak learners and they are sufficiently diverse. (Reason behind: the law of large numbers)

 

**Ensemble methods work best when the predictors are as independent from one another as possible.** 

- One way to get diverse classifiers is to **train them using very different algorithms.** This     increases the chance that they will make very different types of errors, improving the ensemble’s accuracy.
- Another approach is to use the **same** training algorithm for every predictor, but to train them on different random subsets of the training set. (See [Bagging and Pasting]({{< relref "bagging-and-pasting.md" >}}))

