---
# ===== Title, summary, and position in the left sidebar =====
linktitle: ""
summary: Classification models.
weight: 410
# =========================================================

# Basic info
title: "K Nearest Neighbors"
date: 2020-07-13
draft: false
type: book # page type
authors: ["admin"]
tags: ["ML", "Classification", "K-Nearest-Neighbors"]
categories: ["Machine Learning"]
toc: true # Show table of contents?

# Advanced settings
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

## Non-parametric Methods

- Store all the training data
- Use the training data for doing predictions
- Do **NOT** adapt parameters
- Often referred to as ***instance-based methods***

👍 **Advantages** 

+ Complexity adapts to training data
+ Very fast at training

👎 **Disadvantages**

- Slow for prediction
- Hard to use for high-dimensional input



## $k$-Nearest Neighbour Classifiers

To classify a new input vector $x,$ 

1. Examine the $k$-closest training data points to $x$ (comman values for $k$: $k=3$, $k=5$)
2. Assign the object to the **most frequently** occurring class

![image-20200128213429949](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/image-20200128213429949.png)

🤔 **When to consider?**

- Can measure distances between data-points
- Less than 20 attributes per instance
- Lots of training data

👍 **Advantages** 

- Training is very fast
- Learn complex target functions
- Similar algorithm can be used for regression
- High accuracy
- Insensitive to outliers
- No assumptions about data

👎 **Disadvantages**

- Computationally expensive
- requires a lot of memory

### Decision Boundaries

- The nearest neighbour algorithm does **NOT** explicitly compute decision boundaries.
- The decision boundaries form a subset of the Voronoi diagram for the training data.
- The *more data* points we have, the *more complex the decision boundary* can become

### Distance Metrics

Most common distance metric:  **Euclidean distance (ED)**

{{< math >}}
$$
d(\boldsymbol{x}, \boldsymbol{y})=\|\boldsymbol{x}-\boldsymbol{y}\|=\sqrt{\left(\sum_{k=1}^{d}\left(\boldsymbol{x}_{k}-\boldsymbol{y}_{k}\right)^{2}\right)}
$$
{{< /math >}}

- makes sense when different features are **commensurate**; each is variable measured in the **same units.**

- If the units are different (e.g.. length and weight), data needs to be **normalised** (resulting input dimensions are zero mean, unit variance)
  $$
  \tilde{\boldsymbol{x}}=(\boldsymbol{x}-\boldsymbol{\mu}) \oslash \boldsymbol{\sigma}
  $$

  - $\mu$: Mean
  - $\sigma$: Standard deviation
  - $\oslash$: **element-wise** division

Another distance metrics:

- **Cosine Distance:** Good for documents, images
  {{< math >}}
  $$
  d(\boldsymbol{x}, \boldsymbol{y})=1-\frac{\boldsymbol{x}^{T} \boldsymbol{y}}{\|\boldsymbol{x}\|\|\boldsymbol{y}\|}
  $$
  {{< /math >}}

- **Hamming Distance:** For string data / categorical features
  {{< math >}}
  $$
  d(\boldsymbol{x}, \boldsymbol{y})=\sum_{k=1}^{d}\left(\boldsymbol{x}_{k} \neq \boldsymbol{y}_{k}\right)
  $$
  {{< /math >}}

- **Manhattan Distance:** Coordinate-wise distance
  {{< math >}}
  $$
  d(\boldsymbol{x}, \boldsymbol{y})=\sum_{k=1}^{d}\left|\boldsymbol{x}_{k}-\boldsymbol{y}_{k}\right|
  $$
  {{< /math >}}

- **Mahalanobis Distance:** Normalized by the sample covariance matrix – unaffected by coordinate transformations
  {{< math >}}
  $$
  d(\boldsymbol{x}, \boldsymbol{y})=\|\boldsymbol{x}-\boldsymbol{y}\|_{\Sigma^{-1}}=\sqrt{(\boldsymbol{x}-\boldsymbol{y})^{T} \boldsymbol{\Sigma}^{-1}(\boldsymbol{x}-\boldsymbol{y})}
  $$
  {{< /math >}}