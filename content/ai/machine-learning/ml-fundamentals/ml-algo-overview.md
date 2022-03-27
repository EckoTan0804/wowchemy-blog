---
# Title, summary, and position in the list
linktitle: "ML Algo overview"
summary: ""
weight: 140

# Basic metadata
title: "Overview of Machine Learning Algorithms"
date: 2020-08-17
draft: false
type: book # page type
authors: ["admin"]
tags: ["Machine Learning", "ML Basics"]
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


## Supervised/Unsupervised Learning

### Supervised learning

The training data you feed to the algorithm **includes** the desired solutions, called **labels** 

Typical task:

- Classification
- Regression


Important supervised learning algo:

- k-Nearest Neighbors
- Linear Regression
- Logistic Regression
- Support Vector Machine (SVM)
- Decision Trees and Random     Forests
- Neural Networks

### Unsupervised learning

Training data is **unlabeled**.

Important unsupervised learning algo:

- Clustering

  - K-Means
  - DBSCAN
  - Hierarchical Cluster Analysis (HCA)

- Anomaly detection and novelty detection

  - One-class SVM
  - Isolation Forest

- Visualization and dimensionality reduction

  - Principal Component Analysis  (PCA)
  - Kernel PCA
  - Locally-Linear Embedding (LLE)
  - t-distributed Stochastic Neighbor Embedding (t-SNE)

- Association rule learning

  - Apriori
  - Eclat

### Semisupervised learning (supervised + unsupervised)

Deal with partially labeled training data, usually a lot of unlabeled data and a little bit of labeled data

### Reinforcement Learning

The learning system, called an **agent** in this context, can observe the environment, select and perform actions, and get rewards in return or penalties in the form of negative rewards.

It must then learn by itself what is the best strategy, called a **policy**, to get the most reward over time.

A policy defines what action the agent should choose when it is in a given situation.

## Batch and Online Learning

whether the system can learn incrementally from a stream of incoming data or not

### Batch Learning

The system muss be trained using all the available data (I.e., it is incapable of learning incrementally)

First the system is trained, and then it is launched into production and runs without learning anymore; it just applies what it has learned. This is called **offline learning**.


Want a batch learning system to know about new data? 

 Need to train a new version of the system from scratch on the full dataset (not just the new data, but also the old data). Then stop the old system and replace it with the new one.

### Online Learning 

Train the system **incrementally** by feeding it data instances sequentially, either individually or by small groups called **mini-batches**. 

Each learning step is fast and cheap, so the system can learn about new data on the fly, as it arrives.

👍 Advantages:

- Great for systems that receive data as a continuous flow and need to adapt to chagne rapidly or     autonomously
- Save a huge amount of space (After learning the new data instance, do not need them anymore and can     just discard them)

😠 Challenge: if bad data is fed to the system, the system's performance will gradually decline.

🔧 Solution: 

- monitor the system closely 
- promptly switch learning off if detect a drop in performance
- monitor the input data and react to abnormal data


## Instance-Based Vs. Model-Based Learning


### Instance-based learning

The system learns the examples by heart, then generalizes to new cases by comparing them to the learned examples (or a subset of them), using a similarity measure

### Model-based learning

Build a model of these examples, then use that model to make predictions