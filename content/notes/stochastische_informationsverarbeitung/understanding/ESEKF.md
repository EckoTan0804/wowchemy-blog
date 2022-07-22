---
# ===== Title, summary, and position in the left sidebar =====
linktitle: "KF Family: ES-EKF" # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 2013
# ============================================================

# ========== Basic metadata ==========
title: Error State Extended Kalman Filter (ES-EKF)
date: 2022-07-20
draft: false
type: book # page type
authors:
  - admin
tags:
  - SI
  - Understanding
  - Kalman Filter
categories:
  - Lecture
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

## What's in a State?

We can think of the vehicle state as composed of two parts

{{< math >}}
$$
\underbrace{\mathbf{x}}_{\text{True state|}}=\underbrace{\hat{\mathbf{x}}}_{\text{Nominal state ("Large")}}+\underbrace{\delta \mathbf{x}}_{\text{Error state ("small")}}
$$
{{< /math >}} 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-20%2022.29.28.png" alt="截屏2022-07-20 22.29.28" style="zoom: 33%;" />



## 💡 Idea

Instead of doing Kalman Filter in the full state (which might have lots of complicated nonlinear behaviours). we use the EKF to directly estimate the error state instead, and then use the estimate of the error state as a correction for nominal state.

![截屏2022-07-20 22.33.53](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-20%2022.33.53.png)

## ES-EKF Steps

Loop 

1. Update nominal state with motion model (for a bunch of times until getting the measurement)

   <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-20%2022.36.51.png" alt="截屏2022-07-20 22.36.51" style="zoom: 33%;" />

2. Propagate uncertainty (for a bunch of times until getting the measurement)

   <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-20%2022.37.38.png" alt="截屏2022-07-20 22.37.38" style="zoom: 33%;" />

3. If a measurement is available

   1. Compute Kalman Gain

   2. Compute error state

      {{< math >}}
      $$
      \delta \hat{\mathbf{x}}_{k}=\mathbf{K}_{k}\left(\mathbf{y}_{k}-\mathbf{h}_{k}\left(\check{\mathbf{x}}_{k}, \mathbf{0}\right)\right)
      $$
      {{< /math >}} 

   3. Correct nominal state

      {{< math >}}
      $$
      \hat{\mathbf{x}}_{k}=\check{\mathbf{x}}_{k}+\delta \hat{\mathbf{x}}_{k}
      $$
      {{< /math >}} 

   4. Correct state covariance

      {{< math >}}
      $$
      \hat{\mathbf{P}}_{k}=\left(\mathbf{1}-\mathbf{K}_{k} \mathbf{H}_{k}\right) \check{\mathbf{P}}_{k}
      $$
      {{< /math >}} 

## Why Use the ES-EKF?

- **Better performance compared to the vanilla EKF**

  The "small" error state is more amenable to linear filtering than the "large" nominal state, which can be integrated nonlinearly

- **Easy to work with constrained quantities (e.g. rotations in 3D)**

  We can also break down the state using a generalized composition operator

  {{< math >}}
  $$
  \underbrace{\mathbf{x}}_{\text{true state}}=\underbrace{\hat{\mathbf{x}}}_{\text{Nominal state (constrained)}} \bigoplus \underbrace{\delta\mathbf{x}}_{\text{Error state (unconstrained)}}
  $$
  {{< /math >}} 

## Summary

- The error-state formulation separates the state into a "large" nominal state and a "small" error state
  - nominal state: keeps track of the motion model, predicts what the state should be
  - error state: captures the modeling errors and the process noise that accumulate over time

- The ES-EKF uses local linearization to estimate the error state and uses it to correct the nominal state
- The ES-EKF can perform better thant the vanilla EKF, and provides a natural way to handle constrained quantities like 3D rotations



## Reference

- [An Improved EKF - The Error State Extended Kalman Filter](https://www.coursera.org/lecture/state-estimation-localization-self-driving-cars/lesson-4-an-improved-ekf-the-error-state-extended-kalman-filter-7Nwfw)