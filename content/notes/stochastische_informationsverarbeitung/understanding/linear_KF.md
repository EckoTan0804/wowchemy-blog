---
# ===== Title, summary, and position in the left sidebar =====
linktitle: "KF Family: LKF" # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 2011
# ============================================================

# ========== Basic metadata ==========
title: Linear Kalman Filter
date: 2022-07-19
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

## Intuition Example

![截屏2022-07-19 15.40.40](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-19%2015.40.40.png)

Estimation of the 1D position of the vehicle.

Starting from an initial probabilistic estimate at time $k-1$

> Note: The initial estimate, the predicted state, and the final corrected state are all random variabless that we will specify their means and covariances.

1. Use a motion model to **predict** our new state
2. Use observation model (e.g. derived from GPS) to **correct** that prediction of vehicle position at time $k$

In this way, we can think of the Kalman filter as a technique to fuse information from different sensors to produce a final estimate of some unknown state, taking the uncertainty in motion and measurements into account.



## The Linear Dynamical System

Motion model:

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-19%2016.07.45.png" alt="截屏2022-07-19 16.07.45" style="zoom:50%;" />

{{< math >}}
$$
\mathbf{x}_{k}=\mathbf{F}_{k-1} \mathbf{x}_{k-1}+\mathbf{G}_{k-1} \mathbf{u}_{k-1}+\mathbf{w}_{k-1}
$$
{{< /math >}} 

where

- $\mathbf{u}_k$: control input
- $\mathbf{w}_k$: process/motion noise. {{< math >}}$\mathbf{w}_{k} \sim \mathcal{N}\left(\mathbf{0}, \mathbf{Q}_{k}\right)${{< /math >}} 

Measurement model

{{< math >}}
$$
\mathbf{y}_{k}=\mathbf{H}_{k} \mathbf{x}_{k}+\mathbf{v}_{k}
$$
{{< /math >}} 

where

- $\mathbf{v}_{k}$: measurement noise. {{< math >}}$\mathbf{v}_{k} \sim \mathcal{N}\left(\mathbf{0}, \mathbf{R}_{k}\right)${{< /math >}} 

## Kalman Filter Steps

### Prediction

We use the process model to predict how our state evolves since the last time step, and will propagate our uncertainty.

{{< math >}}
$$
\begin{array}{l}
\check{\mathbf{x}}_{k}=\mathbf{F}_{k-1} \mathbf{x}_{k-1}+\mathbf{G}_{k-1} \mathbf{u}_{k-1} \\
\check{\mathbf{P}}_{k}=\mathbf{F}_{k-1} \hat{\mathbf{P}}_{k-1} \mathbf{F}_{k-1}^{T}+\mathbf{Q}_{k-1}
\end{array}
$$
{{< /math >}} 

### Correction

We use measurement to correct that prediction

> Notation:
>
> - $\check{x}_k$: a prediction before the measurement is incorporated
>
> - $\hat{x}_k$: corrected prediction at time step $k$

- Optimal Gain

  {{< math >}}
  $$
  \mathbf{K}_{k}=\check{\mathbf{P}}_{k} \mathbf{H}_{k}^{T}\left(\mathbf{H}_{k} \check{\mathbf{P}}_{k} \mathbf{H}_{k}^{T}+\mathbf{R}_{k}\right)^{-1}
  $$
  {{< /math >}} 

- Correction

  {{< math >}}
  $$
  \begin{aligned}
  \hat{\mathbf{x}}_{k} &=\check{\mathbf{x}}_{k}+\mathbf{K}_{k}\underbrace{\left(\mathbf{y}_{k}-\mathbf{H}_{k} \check{\mathbf{x}}_{k}\right)}_{\text{innovation}} \\
  \hat{\mathbf{P}}_{k}&=\left(\mathbf{I}-\mathbf{K}_{k} \mathbf{H}_{k}\right) \check{\mathbf{P}}_{k}
  \end{aligned}
  $$
  {{< /math >}} 

### Summary 

![截屏2022-07-19 16.46.13](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-19%2016.46.13.png)

## Example

Consider a self-driving vehicle estimating its own position.

The state vector includes the position and its first derivative, velocity.

{{< math >}}
$$
\mathbf{x}=\left[\begin{array}{c}
p \\
\frac{d p}{d t}=\dot{p}
\end{array}\right]
$$
{{< /math >}} 

Input is the scalar acceleration

{{< math >}}
$$
\mathbf{u}=a=\frac{d^{2} p}{d t^{2}}
$$
{{< /math >}} 

THe linear dynamical system is 

- Motion/Process model

  {{< math >}}
  $$
  \mathbf{x}_{k}=\left[\begin{array}{cc}
  1 & \Delta t \\
  0 & 1
  \end{array}\right] \mathbf{x}_{k-1}+\left[\begin{array}{c}
  0 \\
  \Delta t
  \end{array}\right] \mathbf{u}_{k-1}+\mathbf{w}_{k-1}
  $$
  {{< /math >}} 

- Position observation

  {{< math >}}
  $$
  y_{k}=\left[\begin{array}{ll}
  1 & 0
  \end{array}\right] \mathbf{x}_{k}+v_{k}
  $$
  {{< /math >}} 

- Nose densities

  {{< math >}}
  $$
  v_{k} \sim \mathcal{N}(0,0.05) \quad \mathbf{w}_{k} \sim \mathcal{N}\left(\mathbf{0},(0.1) \mathbf{1}_{2 \times 2}\right)
  $$
  {{< /math >}} 

Given the data at time step $k=0$

{{< math >}}
$$
\begin{array}{l}
\hat{\mathbf{x}}_{0} \sim \mathcal{N}\left(\left[\begin{array}{l}
0 \\
5
\end{array}\right],\left[\begin{array}{cc}
0.01 & 0 \\
0 & 1
\end{array}\right]\right) \\
\Delta t=0.5 \mathrm{~s} \\
u_{0}=-2\left[\mathrm{~m} / \mathrm{s}^{2}\right] \quad y_{1}=2.2[\mathrm{~m}]
\end{array}
$$
{{< /math >}} 

We want to estimate the state at time step $k=1$.

Prediction step

{{< math >}}
$$
\begin{aligned}
\check{\mathbf{x}}_{k} &=\mathbf{F}_{k-1} \mathbf{x}_{k-1}+\mathbf{G}_{k-1} \mathbf{u}_{k-1} \\\\
{\left[\begin{array}{c}
\check{p}_{1} \\
\check{p}_{1}
\end{array}\right] } &=\left[\begin{array}{cc}
1 & 0.5 \\
0 & 1
\end{array}\right]\left[\begin{array}{l}
0 \\
5
\end{array}\right]+\left[\begin{array}{c}
0 \\
0.5
\end{array}\right](-2)=\left[\begin{array}{c}
2.5 \\
4
\end{array}\right]
\end{aligned}
$$
{{< /math >}} 

{{< math >}}
$$
\begin{aligned}
\check{\mathbf{P}}_{k} &=\mathbf{F}_{k-1} \hat{\mathbf{P}}_{k-1} \mathbf{F}_{k-1}^{T}+\mathbf{Q}_{k-1} \\\\
\check{\mathbf{P}}_{1} &=\left[\begin{array}{cc}
1 & 0.5 \\
0 & 1
\end{array}\right]\left[\begin{array}{cc}
0.01 & 0 \\
0 & 1
\end{array}\right]\left[\begin{array}{cc}
1 & 0.5 \\
0 & 1
\end{array}\right]^{T}+\left[\begin{array}{cc}
0.1 & 0 \\
0 & 0.1
\end{array}\right]=\left[\begin{array}{cc}
0.36 & 0.5 \\
0.5 & 1.1
\end{array}\right]
\end{aligned}
$$
{{< /math >}} 

Correction step

- Kalman Gain

  {{< math >}}
  $$
  \begin{aligned}
  \mathbf{K}_{1} &=\check{\mathbf{P}}_{1} \mathbf{H}_{1}^{T}\left(\mathbf{H}_{1} \check{\mathbf{P}}_{1} \mathbf{H}_{1}^{T}+\mathbf{R}_{1}\right)^{-1} \\
  &\left.=\left[\begin{array}{cc}
  0.36 & 0.5 \\
  0.5 & 1.1
  \end{array}\right]\left[\begin{array}{l}
  1 \\
  0
  \end{array}\right]\left(\begin{array}{ll}
  1 & 0
  \end{array}\right]\left[\begin{array}{cc}
  0.36 & 0.5 \\
  0.5 & 1.1
  \end{array}\right]\left[\begin{array}{l}
  1 \\
  0
  \end{array}\right]+0.05\right)^{-1} \\
  &=\left[\begin{array}{l}
  0.88 \\
  1.22
  \end{array}\right]
  \end{aligned}
  $$
  {{< /math >}} 

- Correction of the state prediction

  {{< math >}}
  $$
  \begin{aligned}
  \hat{\mathbf{x}}_{1} &=\check{\mathbf{x}}_{1}+\mathbf{K}_{1}\left(\mathbf{y}_{1}-\mathbf{H}_{1} \check{\mathbf{x}}_{1}\right) \\\\
  {\left[\begin{array}{c}
  \hat{p}_{1} \\
  \hat{\dot{p}}_{1}
  \end{array}\right] } &=\left[\begin{array}{c}
  2.5 \\
  4
  \end{array}\right]+\left[\begin{array}{c}
  0.88 \\
  1.22
  \end{array}\right]\left(2.2-\left[\begin{array}{ll}
  1 & 0
  \end{array}\right]\left[\begin{array}{c}
  2.5 \\
  4
  \end{array}\right]\right)=\left[\begin{array}{l}
  2.24 \\
  3.63
  \end{array}\right]
  \end{aligned}
  $$
  {{< /math >}} 

- Correction of covariance

  {{< math >}}
  $$
  \begin{aligned}
  \hat{\mathbf{P}}_{1} &=\left(\mathbf{1}-\mathbf{K}_{1} \mathbf{H}_{1}\right) \check{\mathbf{P}}_{1} \\\\
  &=\left[\begin{array}{ll}
  0.04 & 0.06 \\
  0.06 & 0.49
  \end{array}\right]
  \end{aligned}
  $$
  {{< /math >}} 

  > Note that the final covariance (*i.e.* the covariance after correction) is smaller. That is, we are more certain about the car position after we incoporate the position measurement. This uncertainty reduction occurs because our measurement model is fairly accurate (the measurement noise variance is quite small).



## Best Linear Unbiased Estimator (BLUE)

If we have white, uncorrelated zero-mean noise, the Kalman Fitler is the best (*i.e.*, lowest variance) unbiased estimator that uses only a linear combination of measurements.

### Bias

We repeat the above Kalman filter for $K$ times.

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-19%2022.29.32.png" alt="截屏2022-07-19 22.29.32" style="zoom:67%;" />

The {{< hl >}}**bias**{{< /hl >}} is defined as the difference between true position and the mean of estimated position values.

![截屏2022-07-19 22.32.03](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-19%2022.32.03.png)

An estimator of filter is {{< hl >}}**unbiased**{{< /hl >}} if it produces an "average" error of zero at a particular time step $k$, over many trials.

{{< math >}}
$$
E\left[\hat{e}_{k}\right]=E\left[\hat{p}_{k}-p_{k}\right]=E\left[\hat{p}_{k}\right]-p_{k}=0 \qquad \forall k \in  \mathbb{N}
$$
{{< /math >}} 

#### Bias in Kalman filter state estimation

Consider the error dynamics

- Predicted state error

  {{< math >}}
  $$
  \check{\mathbf{e}}_{k}=\check{\mathbf{x}}_{k}-\mathbf{x}_{k}
  $$
  {{< /math >}} 

- Corrected state error

  {{< math >}}
  $$
  \hat{\mathbf{e}}_{k}=\hat{\mathbf{x}}_{k}-\mathbf{x}_{k}
  $$
  {{< /math >}} 

Using the Kalman Fitler equations, we can derive

{{< math >}}
$$
\begin{array}{l}
\check{\mathbf{e}}_{k}=\mathbf{F}_{k-1} \check{\mathbf{e}}_{k-1}-\mathbf{w}_{k} \\
\hat{\mathbf{e}}_{k}=\left(\mathbf{1}-\mathbf{K}_{k} \mathbf{H}_{k}\right) \check{\mathbf{e}}_{k}+\mathbf{K}_{k} \mathbf{v}_{k}
\end{array}
$$
{{< /math >}} 

So long as 

- The initial state estimate is unbiased ({{< math >}}$E\left[\hat{\mathbf{e}}_{0}\right]=\mathbf{0}${{< /math >}} )
- The noise is white, uncorrelated and zero mean ({{< math >}}$E[\mathbf{v}]=\mathbf{0}, E[\mathbf{w}]=\mathbf{0}${{< /math >}} )

Then the state estiamte is unbiased

{{< math >}}
$$
\begin{aligned}
E\left[\check{\mathbf{e}}_{k}\right] &=E\left[\mathbf{F}_{k-1} \check{\mathbf{e}}_{k-1}-\mathbf{w}_{k}\right] \\
&=\mathbf{F}_{k-1} E\left[\check{\mathbf{e}}_{k-1}\right]-E\left[\mathbf{w}_{k}\right] \\
&=\mathbf{0}
\end{aligned}
$$
{{< /math >}} 

{{< math >}}
$$
\begin{aligned}
E\left[\hat{\mathbf{e}}_{k}\right] &=E\left[\left(\mathbf{1}-\mathbf{K}_{k} \mathbf{H}_{k}\right) \check{\mathbf{e}}_{k}+\mathbf{K}_{k} \mathbf{v}_{k}\right] \\
&=\left(\mathbf{1}-\mathbf{K}_{k} \mathbf{H}_{k}\right) E\left[\check{\mathbf{e}}_{k}\right]+\mathbf{K}_{k} E\left[\mathbf{v}_{k}\right] \\
&=\mathbf{0}
\end{aligned}
$$
{{< /math >}} 

### Consistency

A filter is {{< hl >}}**consistent**{{< /hl >}} if for all $k$

{{< math >}}
$$
E\left[\hat{e}_{k}^{2}\right]=E\left[\left(\hat{p}_{k}-p_{k}\right)^{2}\right]=\hat{P}_{k}
$$
{{< /math >}} 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-19%2023.22.43.png" alt="截屏2022-07-19 23.22.43" style="zoom:50%;" />

This means that the filter is neither overconfident nor underconfident in the estimate it has produced.

The Kalman Fitler is consistent in state estimate.

{{< math >}}
$$
E\left[\check{\mathbf{e}}_{k} \check{\mathbf{e}}_{k}^{T}\right]=\check{\mathbf{P}}_{k} \qquad E\left[\hat{\mathbf{e}}_{k} \hat{\mathbf{e}}_{k}^{T}\right]=\hat{\mathbf{P}}_{k}
$$
{{< /math >}} 

so long as

- the initial state estimate is consistent ({{< math >}}$E\left[\hat{\mathbf{e}}_{0} \hat{\mathbf{e}}_{0}^{T}\right]=\check{\mathbf{P}}_{0}${{< /math >}})
- the noise is white and zero-mean ({{< math >}}$E[\mathbf{v}]=\mathbf{0}, E[\mathbf{w}]=\mathbf{0}${{< /math >}})

















## Reference

- [The (Linear) Kalman Filter](https://www.coursera.org/lecture/state-estimation-localization-self-driving-cars/lesson-1-the-linear-kalman-filter-7DFmY)