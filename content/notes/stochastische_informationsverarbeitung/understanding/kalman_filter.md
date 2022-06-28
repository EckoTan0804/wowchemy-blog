---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 2010
# ============================================================

# ========== Basic metadata ==========
title: Kalman Filter
date: 2022-06-24
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

The Kalman filter is an efficient *recursive* filter estimating the internal-state of a [linear dynamic system](https://en.wikipedia.org/wiki/Linear_dynamical_system) from a series of noisy measurements.

Applications include

- Guidance
- Navigation
- Control of vehicles, aircraft, spacecraft, and ships positioned dynamically

## Kalman Filter Summary

Kalman filter in a picture:

![kalman_filter-Kalman_filter_summary.drawio](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/kalman_filter-Kalman_filter_summary.drawio.png)

Summary of equations:

<style type="text/css">
.tg  {border-collapse:collapse;border-color:#ccc;border-spacing:0;}
.tg td{background-color:#fff;border-color:#ccc;border-style:solid;border-width:1px;color:#333;
  font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:1px;color:#333;
  font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-fymr{border-color:inherit;font-weight:bold;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-fymr">Equation</th>
    <th class="tg-fymr">Equation Name</th>
    <th class="tg-fymr">Alternative Names</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fymr" rowspan="2">Predict</td>
    <td class="tg-0pky">$\hat{\boldsymbol{x}}_{n, n-1}=\mathbf{F} \hat{\boldsymbol{x}}_{n-1, n-1} + \mathbf{G} \boldsymbol{u}_{n}$</td>
    <td class="tg-0pky"><span style="font-weight:normal;font-style:normal;text-decoration:none">State Extrapolation</span></td>
    <td class="tg-0pky">Predictor Equation<br>Transition Equation<br>Prediction Equation<br>Dynamic Model<br>State Space Model</td>
  </tr>
  <tr>
    <td class="tg-0pky">$\mathbf{P}_{n, n-1}=\mathbf{F} \mathbf{P}_{n-1, n-1} \mathbf{F}^{T}+\mathbf{Q}$</td>
    <td class="tg-0pky"><span style="font-weight:normal;font-style:normal;text-decoration:none">Covariance Extrapolation</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal">Predictor Covariance Equation</span></td>
  </tr>
  <tr>
    <td class="tg-fymr" rowspan="3">Update</td>
    <td class="tg-0pky">$\mathbf{K}_{n}=\mathbf{P}_{n, n-1} \mathbf{H}^{T}\left(\mathbf{H} \mathbf{P}_{n, n-1} \mathbf{H}^{T}+\mathbf{R}_{n}\right)^{-1}$</td>
    <td class="tg-0pky"><span style="font-weight:normal;font-style:normal;text-decoration:none">Kalman Gain</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;font-style:normal;text-decoration:none">Weight Equation</span></td>
  </tr>
  <tr>
    <td class="tg-0pky">$\hat{\boldsymbol{x}}_{\boldsymbol{n}, \boldsymbol{n}}=\hat{\boldsymbol{x}}_{\boldsymbol{n}, \boldsymbol{n}-1}+\mathbf{K}_{\boldsymbol{n}}\left(\boldsymbol{z}_{n}-\mathbf{H} \hat{\boldsymbol{x}}_{\boldsymbol{n}, \boldsymbol{n}-1}\right)$</td>
    <td class="tg-0pky"><span style="font-weight:normal;font-style:normal;text-decoration:none">State Update</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;font-style:normal;text-decoration:none">Filtering Equation</span></td>
  </tr>
  <tr>
    <td class="tg-0pky">$\mathbf{P}_{n, n}=\left(\mathbf{I}-\mathbf{K}_{n} \mathbf{H}\right) \mathbf{P}_{n, n-1}$</td>
    <td class="tg-0pky">Covariance Update</td>
    <td class="tg-0pky"><span style="font-weight:normal;font-style:normal;text-decoration:none">Corrector Equation</span></td>
  </tr>
  <tr>
    <td class="tg-fymr" rowspan="4"><span style="font-style:italic">Auxilliary</span></td>
    <td class="tg-0pky">$\boldsymbol{z}_{n} = \mathbf{H} \boldsymbol{x}_n + \boldsymbol{v}_n$</td>
    <td class="tg-0pky"><span style="font-weight:normal;font-style:normal;text-decoration:none">Measurement Equation</span></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">$\mathbf{R}_n = E\{\boldsymbol{v}_n \boldsymbol{v}_n^T\}$</td>
    <td class="tg-0pky"><span style="font-weight:normal;font-style:normal;text-decoration:none">Measurement Uncertainty</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;font-style:normal;text-decoration:none">Measurement Error</span></td>
  </tr>
  <tr>
    <td class="tg-0pky">$\mathbf{Q}_n = E\{\boldsymbol{w}_n \boldsymbol{w}_n^T\}$</td>
    <td class="tg-0pky"><span style="font-weight:normal;font-style:normal;text-decoration:none">Process Noise Uncertainty</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;font-style:normal;text-decoration:none">Process Noise Error</span></td>
  </tr>
  <tr>
    <td class="tg-0pky">$\mathbf{P}_{n, n}=E\left\{\boldsymbol{e}_{n} \boldsymbol{e}_{n}^{T}\right\}=E\left\{\left(\boldsymbol{x}_{n}-\hat{\boldsymbol{x}}_{n, n}\right)\left(\boldsymbol{x}_{n}-\hat{\boldsymbol{x}}_{n, n}\right)^{T}\right\}$</td>
    <td class="tg-0pky"><span style="font-weight:normal;font-style:normal;text-decoration:none">Estimation Uncertainty</span></td>
    <td class="tg-0pky"><span style="font-weight:normal;font-style:normal;text-decoration:none">Estimation Error</span></td>
  </tr>
</tbody>
</table>

Summary of notations:

<style type="text/css">
.tg  {border-collapse:collapse;border-color:#ccc;border-spacing:0;}
.tg td{background-color:#fff;border-color:#ccc;border-style:solid;border-width:1px;color:#333;
  font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:1px;color:#333;
  font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-1wig{font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-1wig">Term</th>
    <th class="tg-1wig">Name</th>
    <th class="tg-1wig">Alternative Term</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">$\boldsymbol{x}$</td>
    <td class="tg-0lax">State vector</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal">$\boldsymbol{z}$</span></td>
    <td class="tg-0lax">Output vector</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal">$\boldsymbol{y}$</span></td>
  </tr>
  <tr>
    <td class="tg-0lax">$\mathbf{F}$</td>
    <td class="tg-0lax">State transition matrix</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal">$\mathbf{\Phi}$, $\mathbf{A}$</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal">$\boldsymbol{u}$</span></td>
    <td class="tg-0lax">Input variable</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">$\mathbf{G}$</td>
    <td class="tg-0lax">Control matrix</td>
    <td class="tg-0lax">$\boldsymbol{B}$</td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal">$\mathbf{P}$</td>
    <td class="tg-0lax">Estimate uncertainty</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal">$\boldsymbol{\Sigma}$</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal">$\mathbf{Q}$</td>
    <td class="tg-0lax">Process noise uncertainty</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal">$\mathbf{R}$</span></td>
    <td class="tg-0lax">Measurement uncertainty</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal">$\boldsymbol{w}$</span></td>
    <td class="tg-0lax">Process noise vector</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal">$\boldsymbol{v}$</span></td>
    <td class="tg-0lax">Measurement noise vector</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal">$\mathbf{H}$</span></td>
    <td class="tg-0lax">Observation matrix</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal">$\mathbf{C}$</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal">$\mathbf{K}$</span></td>
    <td class="tg-0lax">Kalman Gain</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">$n$</td>
    <td class="tg-0lax">Discrete time index</td>
    <td class="tg-0lax">$k$</td>
  </tr>
</tbody>
</table>


## Multidimensional Kalman Filter in Detail

A Kalman filter works by a two-phase process, including 5 main equations:

- **Predict** phase: produces prediction of the current state, along with thier uncertainties
  - [State extrapolation equation](#state-extrapolation-equation)
  - [Covariance extrapolation equation](#covariance-extrapolation-equation)
- **Update** phase: refines the prediction using a weighted average given measurements 
  - [Kalman Gain equation](#kalman-gain-equation)
  - [State update equation](#state-update-equation)
  - [Covariance update equation](#covariance-update-equation)

### State extrapolation equation

The Kalman filter assumes that the true state of a system at time step $n$ evolved from the prior state at time step $n-1$ is

{{< math >}}
$$
\boldsymbol{x}_n = \mathbf{F} \boldsymbol{x}_{n-1} +\mathbf{G} \boldsymbol{u}_{n} + \boldsymbol{w}_n
$$
{{< /math >}} 

- {{< math >}}$\boldsymbol{x}_{n}${{< /math >}}: **state vector**

- {{< math >}}$\boldsymbol{u}_{n}${{< /math >}}: **control variable** or **input variable** - a measurable (deterministic) input to the system
- {{< math >}}$\boldsymbol{w}_n${{< /math >}}: **process noise** or disturbance - an unmeasurable input that affects the state
- {{< math >}}$\mathbf{F}${{< /math >}}: **state transition matrix** - applies the effect of each system state parameter at time step $n-1$ on the system state at time step $n$
- {{< math >}}$\mathbf{G}${{< /math >}}: **control matrix** or **input transition matrix** (mapping control to state variables)

The **state extrapolation equation**

- Predicts the next system state, based on the knowledge of the current state
- Extrapolates the state vector from time step $n-1$ to $n$
- Also called
  - Predictor Equation
  - Transition Equation
  - Prediction Equation
  - Dynamic Model
  - State Space Model

- The general form in a matrix notation

  {{< math >}}
  $$
  \hat{\boldsymbol{x}}_{n, n-1}=\mathbf{F} \hat{\boldsymbol{x}}_{n-1, n-1}+\mathbf{G} \boldsymbol{u}_{n}
  $$
  {{< /math >}} 

  - {{< math >}}$\hat{\boldsymbol{x}}_{n, n-1}${{< /math >}}: predicted system state vector at time step $n$

  - {{< math >}}$\hat{\boldsymbol{x}}_{n-1, n-1}${{< /math >}}: estimated system state vector at time step $n-1$
  
  > {{< math >}}$\hat{\boldsymbol{x}}_{n, m}${{< /math >}} represents the estimate of $\boldsymbol{x}$ at time step $n$ given observation/measurements up to and including at time $m \leq n$

#### Example

- [Airplane without control input](https://www.kalmanfilter.net/stateextrap.html#ex1)
- [Airplane with control input](https://www.kalmanfilter.net/stateextrap.html#ex2)
- [Falling object](https://www.kalmanfilter.net/stateextrap.html#ex3)

### Covariance extrapolation equation

The **covariance extrapolation equation** extrapolates the uncertainty in our [state prediction](#state-extrapolation-equation). 

{{< math >}}
$$
\mathbf{P}_{n, n-1}=\mathbf{F} \mathbf{P}_{n-1, n-1} \mathbf{F}^{T}+\mathbf{Q}
$$
{{< /math >}}

- {{< math >}}$\mathbf{P}_{n-1, n-1}${{< /math >}}: uncertainty (covariance matrix) of the estimate at time step $n-1$

  {{< math >}}
  $$
  \begin{aligned}
  \mathbf{P}_{n-1, n-1} &= E\{\underbrace{(\boldsymbol{x}_{n-1, n-1} - \hat{\boldsymbol{x}}_{n-1, n-1})}_{=: \boldsymbol{e}_n} (\boldsymbol{x}_{n-1, n-1} - \hat{\boldsymbol{x}}_{n-1, n-1}) ^T\} \\
  & = E\{\boldsymbol{e}_n \boldsymbol{e}_n^T\}
  \end{aligned}
  $$
  {{< /math >}} 

- {{< math >}}$\mathbf{P}_{n, n-1}${{< /math >}}: uncertainty (covariance matrix) of the prediction at time step $n$

- {{< math >}}$\mathbf{F}${{< /math >}}: state transition matrix

- {{< math >}}$\mathbf{Q}${{< /math >}}: process noise matrix

  {{< math >}}
  $$
  \mathbf{Q}_n = E\{\boldsymbol{w}_n \boldsymbol{w}_n^T\}
  $$
  {{< /math >}} 
  
  - {{< math >}}$\boldsymbol{w}_n${{< /math >}}: process noise vector


{{< spoiler text="Derivation" >}}
At time step $n$, the Kalman filter assumes

{{< math >}}
$$
\boldsymbol{x}\_n = \mathbf{F} \boldsymbol{x}\_{n-1} +\mathbf{G} \boldsymbol{u}\_{n} + \boldsymbol{w}\_n
$$
{{< /math >}} 

The prediction of state is

{{< math >}}
$$
\hat{\boldsymbol{x}}\_{n, n-1}=\mathbf{F} \hat{\boldsymbol{x}}\_{n-1, n-1}+\mathbf{G} \boldsymbol{u}\_{n}
$$
{{< /math >}} 

The difference between $\boldsymbol{x}\_n$ and $\hat{\boldsymbol{x}}\_{n, n-1}$ is

{{< math >}}
$$
\begin{aligned}
\boldsymbol{x}\_{n}-\hat{\boldsymbol{x}}\_{n, n-1} &=\mathbf{F} \boldsymbol{x}\_{n-1}+\mathbf{G} \boldsymbol{u}\_{n}+\boldsymbol{w}\_{n}-\left(\mathbf{F} \hat{\boldsymbol{x}}\_{n-1, n-1}+\mathbf{G}  \boldsymbol{u}\_{n}\right) \\\\
&=\mathbf{F}\left(\boldsymbol{x}\_{n-1}-\hat{\boldsymbol{x}}\_{n-1, n-1}\right)+\boldsymbol{w}\_{n}
\end{aligned}
$$
{{< /math >}} 

The variance associate with the prediction $\hat{\boldsymbol{x}}\_{n, n-1}$ of an unknow true state $\boldsymbol{x}\_n$ is

![image-20220625180624325](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/image-20220625180624325.png)

Noting that the state estimation errors and process noise are uncorrelated:

{{< math >}}
$$
E\left\\{\left(\boldsymbol{x}\_{n-1}-\hat{\boldsymbol{x}}\_{n-1, n-1}\right) \boldsymbol{w}\_{n}^{T}\right\\} = E\left\\{\boldsymbol{w}\_{n}\left(\boldsymbol{x}\_{n-1}-\hat{\boldsymbol{x}}\_{n-1, n-1}\right)^{T}\right\\} = 0
$$
{{< /math >}} 

Therefore

{{< math >}}
$$
\begin{aligned}
\mathbf{P}\_{n, n-1} &=\underbrace{E\left\\{\left(\boldsymbol{x}\_{n-1}-\hat{\boldsymbol{x}}\_{n-1, n-1}\right)\left(\boldsymbol{x}\_{n-1}-\hat{\boldsymbol{x}}\_{n-1, n-1}\right)^{T}\right\\}}\_{=\mathbf{P}\_{n-1, n-1}} \mathbf{F}^{T}+\underbrace{E\left\\{w\_{n} w\_{n}^{T}\right\\}}\_{=\mathbf{Q}} \\\\
&=\mathbf{F} \mathbf{P}\_{n-1, n-1}\mathbf{F}^T+\mathbf{Q}
\end{aligned}
$$
{{< /math >}} 
{{< /spoiler >}}

### Kalman Gain equation

{{< math >}}
$$
\mathbf{K}_{n}=\mathbf{P}_{n, n-1} \mathbf{H}^{T}\left(\mathbf{H} \mathbf{P}_{n, n-1} \mathbf{H}^{T}+\mathbf{R}_{n}\right)^{-1}
$$
{{< /math >}} 

- {{< math >}}$\mathbf{P}_{n, n-1}${{< /math >}}: [uncertainty (covariance) matrix of the current state prediction](#covariance-extrapolation-equation)
- {{< math >}}$\mathbf{H}${{< /math >}}: observation matrix
- {{< math >}}$\mathbf{R}_{n}${{< /math >}}: measurement Uncertainty (measurement noise covariance matrix)

{{< spoiler text="Derivation" >}}

Rearrange the [covariance update equation](#covariance-update-equation)
$$
\begin{array}{l}
\mathbf{P}\_{n, n}=\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right) \mathbf{P}\_{n, n-1}{\color{DodgerBlue} \left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)^{T}}+\mathbf{K}\_{n} \mathbf{R}\_{n} \mathbf{K}\_{n}^{T} \\\\\\\\
\mathbf{P}\_{n, n}=\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right) \mathbf{P}\_{n, n-1}{\color{DodgerBlue}\left(\mathbf{I}-\left(\mathbf{K}\_{n} \mathbf{H}\right)^{T}\right)}+\mathbf{K}\_{n} \mathbf{R}\_{n} \mathbf{K}\_{n}^{T} \qquad | \text{ } \mathbf{I} = \mathbf{I}^T \\\\\\\\
\mathbf{P}\_{n, n}={\color{ForestGreen}\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right) \mathbf{P}\_{n, n-1}}{\color{DodgerBlue}\left(\mathbf{I}-\mathbf{H}^{T} \mathbf{K}\_{n}^{T}\right)}+\mathbf{K}\_{n} \mathbf{R}\_{n} \mathbf{K}\_{n}^{T} \qquad | \text{ } (\mathbf{AB})^T = \mathbf{B}^T \mathbf{A}^T\\\\\\\\
\mathbf{P}\_{n, n}={\color{ForestGreen}\left(\mathbf{P}\_{n, n-1}-\mathbf{K}\_{n} \mathbf{H} \mathbf{P}\_{n, n-1}\right)}\left(\mathbf{I}-\mathbf{H}^{T} \mathbf{K}\_{n}^{T}\right)+\mathbf{K}\_{n} \mathbf{R}\_{n} \mathbf{K}\_{n}^{T} \\\\\\\\
\mathbf{P}\_{n, n}=\mathbf{P}\_{n, n-1}-\mathbf{P}\_{n, n-1} \mathbf{H}^{T} \mathbf{K}\_{n}^{T}-\mathbf{K}\_{n} \mathbf{H} \mathbf{P}\_{n, n-1} \\\\
+{\color{MediumOrchid}\mathbf{K}\_{n} \mathbf{H} \mathbf{P}\_{n, n-1} \mathbf{H}^{T} \mathbf{K}\_{n}^{T}+\mathbf{K}\_{n} \mathbf{R}\_{n} \mathbf{K}\_{n}^{T}} \qquad | \text{ } \mathbf{AB}\mathbf{A}^T + \mathbf{AC}\mathbf{A}^T  = \mathbf{A}(\mathbf{B} + \mathbf{C})\mathbf{A}^T 
\\\\\\\\
\mathbf{P}\_{n, n}=\mathbf{P}\_{n, n-1}-\mathbf{P}\_{n, n-1} \mathbf{H}^{T} \mathbf{K}\_{n}^{T}-\mathbf{K}\_{n} \mathbf{H} \mathbf{P}\_{n, n-1} \\\\
+{\color{MediumOrchid}\mathbf{K}\_{n}\left(\mathbf{H} \mathbf{P}\_{n, n-1} \mathbf{H}^{T}+\boldsymbol{\mathbf{R}}\_{n}\right) \mathbf{K}\_{n}^{T}}
\end{array}
$$

As the Kalman Filter is an **optimal filter**, we will seek a Kalman Gain that minimizes the estimate variance.

In order to minimize the estimate variance, we need to minimize the main diagonal (from the upper left to the lower right) of the covariance matrix {{< math >}}$\mathbf{P}\_{n, n}${{< /math >}}.

The sum of the main diagonal of the square matrix is the **trace** of the matrix. Thus, we need to minimize {{< math >}}$tr(\mathbf{P}\_{n, n})${{< /math >}}. In order to find the conditions required to produce a minimum, we will differentiate {{< math >}}$tr(\mathbf{P}\_{n, n})${{< /math >}} w.r.t. $\mathbf{K}\_n$ and set the result to zero.

{{< math >}}
$$
\begin{array}{l}
tr\left(\mathbf{P}\_{\boldsymbol{n}, \boldsymbol{n}}\right)=tr\left(\mathbf{P}\_{\boldsymbol{n}, \boldsymbol{n}-1}\right)-{\color{DarkOrange}tr\left(\mathbf{P}\_{n, n-1} \mathbf{H}^{T} \mathbf{K}\_{n}^{T}\right)}\\\\
{\color{DarkOrange} -tr\left(\mathbf{K}\_{n} \mathbf{H} \mathbf{P}\_{n, n-1}\right)} + tr\left(\mathbf{K}\_{\boldsymbol{n}}\left(\mathbf{H} \mathbf{P}\_{\boldsymbol{n}, \boldsymbol{n}-\mathbf{1}} \mathbf{H}^{\boldsymbol{T}}+\mathbf{R}\_{\boldsymbol{n}}\right) \mathbf{K}\_{n}^{\boldsymbol{T}}\right) \qquad | \text{} tr(\mathbf{A}) = tr(\mathbf{A}^T)\\\\\\\\
tr\left(\mathbf{P}\_{n, n}\right)=tr\left(\mathbf{P}\_{n, n-1}\right)-{\color{DarkOrange}2 tr\left(\mathbf{K}\_{n} \mathbf{H} \mathbf{P}\_{n, n-1}\right)}\\\\
+tr\left(\mathbf{K}\_{n}\left(\mathbf{H} \mathbf{P}\_{n, n-1} \mathbf{H}^{\boldsymbol{T}}+\mathbf{R}\_{n}\right) \mathbf{K}\_{n}^{T}\right)\\\\\\\\
\frac{d}{d \mathbf{K}\_{n}}t r\left(\mathbf{P}\_{n, n}\right)={\color{DodgerBlue} \frac{d}{d \mathbf{K}\_{n}}t r\left(\mathbf{P}\_{n, n-1}\right)}-{\color{ForestGreen}\frac{d }{d \mathbf{K}\_{n}}2 t r\left(\mathbf{K}\_{n} \mathbf{H} \mathbf{P}\_{n, n-1}\right)} \\\\
+{\color{MediumOrchid}\frac{d}{d\mathbf{K}\_{n}}tr(\mathbf{K}\_{n}(\mathbf{H}\mathbf{P}\_{n, n-1}\mathbf{H}^T + \mathbf{R}\_n)\mathbf{K}\_{n}^T)} \overset{!}{=} 0 \quad | \text{ } {\color{ForestGreen} \frac{d}{d \mathbf{A}}tr(\mathbf{A} \mathbf{B}) = \mathbf{B}^T},{\color{MediumOrchid} \frac{d}{d \mathbf{A}}tr(\mathbf{A} \mathbf{B} \mathbf{A}^T) = 2\mathbf{A} \mathbf{B}}\\\\\\\\
\frac{d\left(t r\left(\mathbf{P}\_{n, n}\right)\right)}{d \mathbf{K}\_{n}}={\color{DodgerBlue}0}-{\color{ForestGreen}2\left(\mathbf{H} \mathbf{P}\_{ n , n - 1 }\right)^{T}}\\\\
+{\color{MediumOrchid}2 \mathbf{K}\_{n}\left(\mathbf{H} \mathbf{P}\_{n, n-1} \mathbf{H}^{T}+\mathbf{R}\_{n}\right)}=0\\\\\\\\
{\color{ForestGreen}\left(\mathbf{H} \mathbf{P}\_{n, n-1}\right)^{T}}={\color{MediumOrchid}\mathbf{K}\_{n}\left(\mathbf{H} \mathbf{P}\_{n, n-1} \mathbf{H}^{T}+\mathbf{R}\_{n}\right)} \\\\\\\\
\mathbf{K}\_{n}=\left(\mathbf{H} \mathbf{P}\_{n, n-1}\right)^{T}\left(\mathbf{H} \mathbf{P}\_{n, n-1} \mathbf{H}^{T}+\mathbf{R}\_{n}\right)^{-1} \quad | \text{ } (\mathbf{AB})^T = \mathbf{B}^T \mathbf{A}^T \\\\\\\\
\mathbf{K}\_{n}=\mathbf{P}\_{n, n-1}^{T} \mathbf{H}^{T}\left(\mathbf{H} \mathbf{P}\_{n, n-1} \mathbf{H}^{T}+\mathbf{R}\_{n}\right)^{-1} \quad | \text{ covariance matrix } \mathbf{P} \text{ symmetric } (\mathbf{P}^T = \mathbf{P})\\\\\\\\
\mathbf{K}\_{n}=\mathbf{P}\_{n, n-1} \mathbf{H}^{T}\left(\mathbf{H} \mathbf{P}\_{n, n-1} \mathbf{H}^{T}+\mathbf{R}\_{n}\right)^{-1}
\end{array}
$$
{{< /math >}} 
{{< /spoiler >}}

#### Kalman Gain intuition

{{% callout note %}}
The Kalman gain tells how much I should refine my prediction (*i.e.*, the *a priori* estimate) by given a measurement.
{{% /callout %}}

We show the intuition of Kalman Gain with a one-dimensional Kalman filter. 

The one-dimensional Kalman Gain is

{{< math >}}
$$
\boldsymbol{K}_{\boldsymbol{n}}=\frac{p_{n, n-1}}{p_{n, n-1}+r_{n}} \in [0, 1]
$$
{{< /math >}} 

- {{< math >}}$p_{n, n-1}${{< /math >}}: variance of the state prediction {{< math >}}$\hat{x}_{n, n-1}${{< /math >}} 
- {{< math >}}$r_n${{< /math >}}: variance of the measurement {{< math >}}$z_n${{< /math >}} 

(Derivation see [here](https://www.kalmanfilter.net/KalmanGainDeriv.html))

Let's rewrite the (one-dimensional) [state update equation](#state-update-equation):

{{< math >}}
$$
\hat{x}_{n, n}=\hat{x}_{n, n-1}+K_{n}\left(z_{n}-\hat{x}_{n, n-1}\right)=\left(1-K_{n}\right) \hat{x}_{n, n-1}+K_{n} z_{n}
$$
{{< /math >}} 

The Kalman Gain $K_n$ is the **weight** that we give to the measurement. And $(1 - K_n)$ is the weight that we give to the state prediction.

- High Kalman Gain

  A low measurement uncertainty (small $r_n$) relative to the prediction uncertainty would result in a high Kalman Gain (close to 1). The new estimate would be close to the measurement.

  > 💡 Intuition
  >
  > small $r_n \rightarrow$ accurate measurements $\rightarrow$ place more weight on the measurements and thus conform to them

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/kalman_filter-high_Kalman_Gain.drawio.png" alt="kalman_filter-high_Kalman_Gain.drawio" style="zoom:60%;" />

- Low Kalman Gain

  A high measurement uncertainty (large $r_n$) relative to the prediction uncertainty would result in a low Kalman Gain (close to 0). The new estimate would be close to the prediction.

  > 💡 Intuition
  >
  > large $r_n \rightarrow$ measurements are not accurate $\rightarrow$ place more weight on the prediction and trust them more
  
  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/kalman_filter-low_Kalman_Gain.drawio.png" alt="kalman_filter-low_Kalman_Gain.drawio" style="zoom: 60%;" />



### State update equation

The **state update equation** updates/refines/corrects the [state prediction](#state-extrapolation-equation) with measurements.

{{< math >}}
$$
\hat{\boldsymbol{x}}_{\boldsymbol{n}, \boldsymbol{n}}=\hat{\boldsymbol{x}}_{\boldsymbol{n}, \boldsymbol{n}-1}+\mathbf{K}_{\boldsymbol{n}}\underbrace{\left(\boldsymbol{z}_{n}-\mathbf{H} \hat{\boldsymbol{x}}_{\boldsymbol{n}, \boldsymbol{n}-1}\right)}_{\text{innovation}}
$$
{{< /math >}} 

- {{< math >}}$\hat{\boldsymbol{x}}_{n, n}${{< /math >}}: estimated system state vector at time step $n$

- {{< math >}}$\hat{\boldsymbol{x}}_{n, n-1}${{< /math >}}: [predicted system state](#state-extrapolation-equation) vector at time step $n$

- {{< math >}}$\mathbf{K}_{\boldsymbol{n}}${{< /math >}}: [Kalman Gain](#kalman-gain-equation)

- {{< math >}}$\mathbf{H}${{< /math >}}: observation matrix

- {{< math >}}$\boldsymbol{z}_{n}${{< /math >}}: measurement at time step $n$

  {{< math >}}
  $$
  \boldsymbol{z}_{n} = \mathbf{H} \boldsymbol{x}_n + \boldsymbol{v}_n
  $$
  {{< /math >}}

  - {{< math >}}$\boldsymbol{x}_n${{< /math >}}: true system state (hidden state)

  - {{< math >}}$\boldsymbol{v}_n${{< /math >}}: measurement noise

    $\rightarrow$ Measurement uncertainty $\mathbf{R}_n$ is given by

    {{< math >}}
    $$
    \mathbf{R}_n = E\{\boldsymbol{v}_n \boldsymbol{v}_n^T\}
    $$
    

    {{< /math >}} 

### Covariance update equation

The **covariance update equation** updates the uncertainty of state estimate on the base of [covariance prediction](#covariance-extrapolation-equation)

{{< math >}}
$$
\mathbf{P}_{n, n}=\left(\mathbf{I}-\mathbf{K}_{n} \mathbf{H}\right) \mathbf{P}_{n, n-1}\left(\mathbf{I}-\mathbf{K}_{n} \mathbf{H}\right)^{T}+\mathbf{K}_{n} \mathbf{R}_{n} \mathbf{K}_{n}^{T}
$$
{{< /math >}} 

- {{< math >}}$\mathbf{P}_{n, n}${{< /math >}}: estimate uncertainty (covariance) matrix of the current state
- {{< math >}}$\mathbf{P}_{n, n-1}${{< /math >}}: [uncertainty (covariance) matrix of the current state prediction](#covariance-extrapolation-equation)
- {{< math >}}$\mathbf{K}_{n}${{< /math >}}: [Kalman Gain](#kalman-gain-equation)
- {{< math >}}$\mathbf{H}${{< /math >}}: observation matrix
- {{< math >}}$\mathbf{R}_{n}${{< /math >}}: measurement Uncertainty (measurement noise covariance matrix)

{{< spoiler text="Derivation" >}}
According to [state update equation](#state-update-equation):

{{< math >}}
$$
\begin{aligned}
\hat{\boldsymbol{x}}\_{n, n} &= \hat{\boldsymbol{x}}\_{n, n-1}+\mathbf{K}\_{n}\left(\boldsymbol{z}\_{n}-\mathbf{H} \hat{\boldsymbol{x}}\_{n, n-1}\right) \\\\\\\\
&= \hat{\boldsymbol{x}}\_{n, n-1}+\mathbf{K}\_{n}\left(\mathbf{H} \boldsymbol{x}\_n + \boldsymbol{v}\_n-\mathbf{H} \hat{\boldsymbol{x}}\_{n, n-1}\right)
\end{aligned}
$$
{{< /math >}} 

The estimation error between the true (hidden) state {{< math >}}$\boldsymbol{x}\_n${{< /math >}} and estimate {{< math >}}$\hat{\boldsymbol{x}}\_{n, n}${{< /math >}} is:

{{< math >}}
$$
\begin{aligned}
\boldsymbol{e}\_n &= \boldsymbol{x}\_n - \hat{\boldsymbol{x}}\_{n, n} \\\\
&= \boldsymbol{x}\_n - \hat{\boldsymbol{x}}\_{n, n-1} - \mathbf{K}\_{n}\mathbf{H}\boldsymbol{x}\_n - \mathbf{K}\_{n}\boldsymbol{v}\_n + \mathbf{K}\_{n}\mathbf{H} \hat{\boldsymbol{x}}\_{n, n-1}\\\\
&= \boldsymbol{x}\_n - \hat{\boldsymbol{x}}\_{n, n-1} - \mathbf{K}\_{n}\mathbf{H}(\boldsymbol{x}\_n - \hat{\boldsymbol{x}}\_{n, n-1}) - \mathbf{K}\_{n}\boldsymbol{v}\_n \\\\
&= (\mathbf{I} - \mathbf{K}\_{n}\mathbf{H})(\boldsymbol{x}\_n - \hat{\boldsymbol{x}}\_{n, n-1}) - \mathbf{K}\_{n}\boldsymbol{v}\_n
\end{aligned}
$$
{{< /math >}} 

Estimate Uncertainty

{{< math >}}
$$
\begin{array}{l}
\boldsymbol{\mathbf{P}}\_{n, n}=E\left(\boldsymbol{e}\_{n} \boldsymbol{e}\_{n}^{T}\right)=E\left(\left(\boldsymbol{x}\_{n}-\hat{\boldsymbol{x}}\_{n, n}\right)\left(\boldsymbol{x}\_{n}-\hat{\boldsymbol{x}}\_{n, n}\right)^{T}\right) \qquad | \text{ Plug in } \boldsymbol{e}\_n\\\\\\\\
\boldsymbol{\mathbf{P}}\_{n, n}=E\left(\left(\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)-\mathbf{K}\_{n} v\_{n}\right) \right.\\\\
\left.\times\left(\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)-\mathbf{K}\_{n} v\_{n}\right)^{T}\right)\\\\\\\\
\mathbf{P}\_{n, n}=E\left(\left(\left(\mathbf{I}-\boldsymbol{\mathbf{K}}\_{n} \mathbf{H}\right)\left(\boldsymbol{x}\_{n}-\hat{\boldsymbol{x}}\_{n, n-1}\right)-\boldsymbol{\mathbf{K}}\_{n} v\_{n}\right) \right.\\\\
\left.\times\left(\left(\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)\right)^{T}-\left(\mathbf{K}\_{n} v\_{n}\right)^{T}\right)\right) \qquad | \text{ }(\mathbf{A} \mathbf{B})^{T}=\mathbf{B}^{T} \mathbf{A}^{T} \\\\\\\\
\mathbf{P}\_{n, n}=E\left(\left(\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)-\mathbf{K}\_{n} v\_{n}\right) \right. \\\\
\left.\times\left(\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)^{T}\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)^{T}-\left(\mathbf{K}\_{n} v\_{n}\right)^{T}\right)\right)\\\\\\\\
\mathbf{P}\_{n, n}=E\left(\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)\left(\boldsymbol{x}\_{n}-\hat{\boldsymbol{x}}\_{n, n-1}\right)^{T}\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)^{T}\right.\\\\
-\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)\left(\mathbf{K}\_{n} v\_{n}\right)^{T}\\\\
-\mathbf{K}\_{n} v\_{n}\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)^{T}\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)^{T}\\\\
\left.+\mathbf{K}\_{n} v\_{n}\left(\mathbf{K}\_{n} v\_{n}\right)^{T}\right) \qquad | \text{ } E(X \pm Y)=E(X) \pm E(Y)\\\\\\\\
\mathbf{P}\_{n, n}=E\left(\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)^{T}\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)^{T}\right)\\\\
-\color{red}{E\left(\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)\left(\mathbf{K}\_{n} v\_{n}\right)^{T}\right)}\\\\
-\color{red}{E\left(\mathbf{K}\_{n} v\_{n}\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)^{T}\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)^{T}\right)}\\\\
+E\left(\mathbf{K}\_{n} v\_{n}\left(\mathbf{K}\_{n} v\_{n}\right)^{T}\right)
\end{array}
$$
{{< /math >}} 

{{< math >}}$\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}${{< /math >}} is the error of the prior estimate in relation to the true value. It is uncorrelated with the current measurement noise $\boldsymbol{v}\_n$. The expectation value of the product of two independent variables is zero. 

{{< math >}}
$$
\begin{aligned}
\color{red}{E\left(\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)\left(\mathbf{K}\_{n} v\_{n}\right)^{T}\right)} = 0 \\\\
\color{red}{E\left(\mathbf{K}\_{n} v\_{n}\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)^{T}\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)^{T}\right)} = 0
\end{aligned}
$$
{{< /math >}} 

Therefore

{{< math >}}
$$
\begin{array}{l}
\mathbf{P}\_{n, n}=E\left(\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)^{T}\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)^{T}\right)\\\\
+{\color{DodgerBlue}{E\left(\mathbf{K}\_{n} v\_{n}\left(\mathbf{K}\_{n} v\_{n}\right)^{T}\right)}} \qquad | \text{ }(\mathbf{A} \mathbf{B})^{T}=\mathbf{B}^{T} \mathbf{A}^{T} \\\\\\\\
\mathbf{P}\_{n, n}=E\left(\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)^{T}\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)^{T}\right)\\\\
+{\color{DodgerBlue}{E\left(\mathbf{K}\_{n} v\_{n} v\_{n}^T \mathbf{K}\_{n}^T\right)}} \qquad | \text{ } E(a X)=a E(X) \\\\\\\\
\mathbf{P}\_{n, n} = \left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right) {\color{ForestGreen}\underbrace{{E\left(\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)\left(\boldsymbol{x}\_{n}-\hat{x}\_{n, n-1}\right)^{T}\right)}}\_{=\mathbf{P}\_{n, n-1}}}\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)^{T}
+\mathbf{K}\_{n}{\color{DodgerBlue}{\underbrace{E\left( v\_{n} v\_{n}^T \right)}\_{=\mathbf{R}\_n}}} \mathbf{K}\_{n}^T \\\\\\\\
\mathbf{P}\_{n, n} = \left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right) {\color{ForestGreen}\mathbf{P}\_{n, n-1}} \left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)^{T} +\mathbf{K}\_{n}{\color{DodgerBlue}\mathbf{R}\_n} \mathbf{K}\_{n}^T
\end{array}
$$
{{< /math >}} 

{{< /spoiler >}}


In many textbook you can see a simplified form:

{{< math >}}
$$
\mathbf{P}_{n, n}=\left(\mathbf{I}-\mathbf{K}_{n} \mathbf{H}\right) \mathbf{P}_{n, n-1}
$$
{{< /math >}} 

{{% callout  warning %}}
This equation is elegant and easier to remember and in many cases it performs well. 

However, even the smallest error in computing the Kalman Gain (due to round off) can lead to huge computation errors. The subtraction $\left(\mathbf{I}-\mathbf{K}_{n} \mathbf{H}\right)$ can lead to nonsymmetric matrices due to floating-point errors. Therefore this equation is **numerically unstable**!
{{% /callout %}}


{{< spoiler text="Derivation of a simplified form of the Covariance Update Equation" >}}
{{< math >}}
$$
\begin{array}{l}
\mathbf{P}\_{n, n} = \left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right) \mathbf{P}\_{n, n-1} \left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right)^{T} +\mathbf{K}\_{n}\mathbf{R}\_n \mathbf{K}\_{n}^T \\\\\\\\
\mathbf{P}\_{n, n}=\mathbf{P}\_{n, n-1}-\mathbf{P}\_{n, n-1} \boldsymbol{\mathbf{H}}^{T} \mathbf{K}\_{n}^{T}-\boldsymbol{\mathbf{K}}\_{n} \mathbf{H} \mathbf{P}\_{n, n-1} \\\\
+{\color{MediumOrchid}\mathbf{K}\_{n}}\left(\mathbf{H} \mathbf{P}\_{n, n-1} \mathbf{H}^{T}+\mathbf{R}\_{n}\right) \mathbf{K}\_{n}^{T} \qquad | \text{ Substitute Kalman Gain}\\\\\\\\
\mathbf{P}\_{n, n}=\mathbf{P}\_{n, n-1}-\mathbf{P}\_{n, n-1} \mathbf{H}^{T} \mathbf{K}\_{n}^{T}-\mathbf{K}\_{n} \mathbf{H} \mathbf{P}\_{n, n-1} \\\\
+{\color{MediumOrchid}\mathbf{P}\_{n, n-1}}  \underbrace{{\color{MediumOrchid}{\mathbf{H}^{T}\left(\mathbf{H} \mathbf{P}\_{n, n-1} \mathbf{H}^{T}+\mathbf{R}\_{n}\right)^{-1}}}\left(\mathbf{H} \mathbf{P}\_{n, n-1} \mathbf{H}^{T}+\mathbf{R}\_{n}\right)}\_{=1} \mathbf{K}\_{n}^{T} \\\\\\\\
\mathbf{P}\_{n, n}=\mathbf{P}\_{n, n-1}-\mathbf{P}\_{n, n-1} \mathbf{H}^{T} \mathbf{K}\_{n}^{T}-\mathbf{K}\_{n} \mathbf{H} \mathbf{P}\_{n, n-1} \\\\
+\mathbf{P}\_{n, n-1} \mathbf{H}^{T} \mathbf{K}\_{n}^{T} \\\\\\\\
\mathbf{P}\_{n, n}=\mathbf{P}\_{n, n-1}-\mathbf{K}\_{n} \mathbf{H} \mathbf{P}\_{n, n-1} \\\\\\\\
\mathbf{P}\_{n, n}=\left(\mathbf{I}-\mathbf{K}\_{n} \mathbf{H}\right) \mathbf{P}\_{n, n-1}
\end{array}
$$
{{< /math >}} 
{{< /spoiler >}}


## Reference

- 👍 [kalmnnfilter.net](https://www.kalmanfilter.net/default.aspx): clear and detaied tutorial for Kalman filter
  - [The $\alpha-\beta-\gamma$ filter](https://www.kalmanfilter.net/alphabeta.html): detailed introduction to Kalman filter
  - [One-dimensional Kalman filter](https://www.kalmanfilter.net/kalman1d.html) with serveral elaborated numerical examples
  - [Multidimensional Kalman filter](https://www.kalmanfilter.net/kalmanmulti.html)
  
- 👍 [How a Kalman filter works, in pictures](https://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/#mjx-eqn-kalpredictfull): Kalman filter explained intuitively in pictures

- [Kalman and Bayesian Filters in Python](https://nbviewer.org/github/rlabbe/Kalman-and-Bayesian-Filters-in-Python/blob/master/table_of_contents.ipynb): Kalman filter (in Python) explained using Jupyter Notebook

- [Understanding the Basis of the Kalman Filter Via a Simple and Intuitive Derivation](https://synapticlab.co.kr/attachment/cfile1.uf@2737C54B590907BA0D46CE.pdf)

- [Wikipedia: Kalman Filter](https://en.wikipedia.org/wiki/Kalman_filter#Predict)