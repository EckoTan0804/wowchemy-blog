---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 2014
# ============================================================

# ========== Basic metadata ==========
title: EKF Limitations
date: 2022-07-21
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

## Linearization Error

Recap: The EKF works by linearizing the nonlinear motion and measurement models to update the mean and covariance of the state.

The difference between the linear approximation and the nonlinear function is called {{< hl >}}**linearization error**{{< /hl >}}

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-21%2015.51.52.png" alt="截屏2022-07-21 15.51.52" style="zoom: 33%;" />

In general, linearization error depends on

- How nonlinear the function is
- How far away from the operating poitn the linear approximation is being used

## Example: Polar Coordinates $\rightarrow$ Cartesian Coordinates

![截屏2022-07-21 15.55.56](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-21%2015.55.56.png)

Now we perform linearized transformation:

![截屏2022-07-21 15.57.09](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-21%2015.57.09.png)

Compare the linearized and nonlinearized output distributions:

![截屏2022-07-21 15.56.53](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-21%2015.56.53.png)

- The mean of the linearized distribution is a very different place than the true mean
- The linearized covariance seriously underestimates the spread of the true output distribution along the $y$-dimension

$\rightarrow$ In this case, the linearization error can cause our belief of the output distribution to completely miss the mark, and this can cause big problem in our estimator!

## Limitations of the EKF

### Linearization errors

The EKF is prone to linearization error when

- The system dynamics are highly nonlinear
- The sensor sampling is slow relative how fast the system is evolving

This has two important consequences

- The estimated mean state can become very different from the true state
- The estimated state covariance can fail to capture the true uncertainty in the state

<span style="color: Red">$\Rightarrow$ Linearization error can cause the estimator to be overconfident in a wrong answer!</span>

### Computing Jacobians

Computing Jacobian matrices for complicated nonlinear functions is also a common source of error in EKF implementations!

- Analytical differentiation is prone to human error
- Numerical differentiation can be slow and unstable
- Automatic differentiation (e.g., at compile time) can also behave unpredictably

And what if one or more of our models is non-differentiable (*e.g.* the step function)?

## Summary

- The EKF uses analytical local linearization and, as a result, is sensitive to linearization errors
- For highly nonlinear systems, the EKF estimate can diverge and become unreliable
- Computing complex Jacobin matrices is an error-prone process and must be done with substantial care

## Reference

- [Limitations of the EKF](https://www.coursera.org/lecture/state-estimation-localization-self-driving-cars/lesson-5-limitations-of-the-ekf-OCrZc)