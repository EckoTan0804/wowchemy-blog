---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 620
# ============================================================

# ========== Basic metadata ==========
title: Reapproximation von Dichten
date: 2022-08-10
draft: false
type: book # page type
authors:
  - admin
tags:
  - SI
  - Lecture Notes
  - Sample-basierte Filter
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

4 cases

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-10%2021.58.40.png" alt="截屏2022-08-10 21.58.40" style="zoom: 33%;" />

Examples for reapproximation

- Continuous → continuous: Gaussian mixture reduction

- Continuous → discrete: deterministic sampling, i.e., replacing a continuous density with Dirac mixture

- Discrete → continuous: density estimation, i.e., finding a continuous density representing a set of given samples

- Discrete → discrete: Dirac mixture reduction

**Challenge:** Three cases involving discrete densities

- Continuous → continuous case: Use standard distance measures, e.g. integral squared distance (ISD)

- Discrete densities prohibit use of standard distance measures

Here we focus on **continuous** → **discrete Reapproximation**

- Given: Continuous density $\tilde{f}(\underline{x})$

- Deterministic sampling, i.e., approximation with Dirac mixture

- Definition of Dirac mixture with $L$ components

  {{< math >}}
  $$
  f(\underline{x})=\sum_{i=1}^{L} w_{i} \cdot \delta\left(\underline{x}-\underline{\hat{x}}_{i}\right)
  $$
  {{< /math >}} 

  - Weights $w_{i}>0, \displaystyle \sum_{i=1}^{L} w_{i}=1$
  - $\underline{x}_i$: locations / samples

- **🎯 Goal: Systematic approximation of given continuous density**



- Application examples
  - Mapping of random variables through nonlinear functions

  - Sample-based fusion and estimation (UKF)


## Univariate Case (1D)

### Synthesis

Instead of comparing densities $\tilde{f}(x), f(x)$, we compare **cumulative distribution functions (CDFs)** $\tilde{F}(x), F(x)$

CDF of $f(x)$:

{{< math >}}

$$
F(x)=P(\boldsymbol{x} \leq x)=\int_{-\infty}^{x} f(u) \mathrm{d} u
$$
{{< /math >}} 

- This definition is *unique*, as other definition $\bar{F}(x)=P(\boldsymbol{x}>x)$ is dependent

  {{< math >}}
  $$
  \begin{aligned}
  \bar{F}(x)=&P(\boldsymbol{x}>x) \\
  &=\int_{x}^{\infty} f(u) d u \\
  &=1-\int_{-\infty}^{x} f(u) d u \\
  &=1-P(\boldsymbol{x} \leq x) \\
  &=1-F(x)
  
  \end{aligned}
  $$
  {{< /math >}} 

- Example

  Dirac mixture density

  {{< math >}}
  $$
  f(x, \underline{\hat{x}})=\sum_{i=1}^{L} w_{i} \delta\left(x-\hat{x}_{i}\right)
  $$
  {{< /math >}} 

  Dirac mixture cumulative distribution

  {{< math >}}

  
  $$
  F(x, \underline{\hat{x}})=\sum_{i=1}^{L} w_{i} \mathrm{H}\left(x-\hat{x}_{i}\right) \text { with } \mathrm{H}(x)=\int_{-\infty}^{x} \delta(t) \mathrm{d} t= \begin{cases}0 & x<0 \\ \frac{1}{2} & x=0 \\ 1 & x>0\end{cases}
  $$
  {{< /math >}} 
  
  with the Dirac position
  
  {{< math >}}
  $$
  \underline{\hat{x}}=\left[\hat{x}_{1}, \hat{x}_{2}, \ldots, \hat{x}_{L}\right]^{\top}
  $$
  {{< /math >}} 

CDF of $\tilde{f}(x)$ follows analogously:

{{< math >}}
$$
\tilde{F}(x)=\int_{-\infty}^{x} \tilde{f}(u) \mathrm{d} u
$$
{{< /math >}} 

- Example

  Gaussian density:

  {{< math >}}
  $$
  \tilde{f}(x)=\frac{1}{\sqrt{2 \pi}} \exp \left(-\frac{1}{2} x^{2}\right)
  $$
  {{< /math >}} 

  $\Rightarrow$ Gaussian cumulative distribution:

  {{< math >}}
  $$
  \tilde{F}(x)=\frac{1}{2}\left(1+\operatorname{erf}\left(\frac{x}{\sqrt{2}}\right)\right)
  $$
  {{< /math >}} 

We compare $\tilde{F}(x), F(x)$ use **Cramér–von Mises distance**:

{{< math >}}
$$
D(\underline{\hat{x}})=\int_{\mathbb{R}}(\tilde{F}(x)-F\left(x, \underline{\hat{x}})\right)^{2} \mathrm{~d} x
$$
{{< /math >}} 

### Minimization of Cramér–von Mises distance

Gradient of the distance measure $D(\underline{\hat{x}})$:

{{< math >}}
$$
\underline{G}(\underline{\hat{x}})=\nabla D(\underline{\hat{\hat{x}}})=\frac{\partial D(\underline{\hat{x}})}{\partial \underline{\hat{x}}}=\left[\frac{\partial D(\underline{\hat{x}})}{\partial \hat{x}_{1}}, \frac{\partial D(\underline{\hat{x}})}{\partial \hat{x}_{2}}, \ldots, \frac{\partial D(\underline{\hat{x}})}{\partial \hat{x}_{L}}\right]^{\top}
$$
{{< /math >}} 

with 

{{< math >}}
$$
\frac{\partial D(\underline{\hat{x}})}{\partial \hat{x}_{i}}=2 w_{i} \int_{-\infty}^{\infty}[\tilde{F}(t)-F(t, \underline{\hat{x}})] \delta\left(t-\hat{x}_{i}\right) \mathrm{d} t
$$
{{< /math >}} 

or

{{< math >}}
$$
\frac{\partial D(\underline{\hat{x}})}{\partial \hat{x}_{i}}=2 w_{i}\left[\tilde{F}\left(\hat{x}_{i}\right)-F\left(\hat{x}_{i}, \underline{\hat{x}}\right)\right] \text { with } F\left(\hat{x}_{i}, \underline{\hat{x}}\right)=\sum_{j=1}^{L} w_{j} \mathrm{H}\left(\hat{x}_{i}-\hat{x}_{j}\right)
$$
{{< /math >}} 

The Hesse matrix is

{{< math >}}
$$
\mathbf{H}(\underline{x})=\operatorname{diag}\left(\left[\frac{\partial^{2} D(\underline{\hat{x}})}{\partial \hat{x}_{1}^{2}}, \frac{\partial^{2} D(\underline{\hat{x}})}{\partial \hat{x}_{2}^{2}}, \ldots, \frac{\partial^{2} D(\underline{\hat{x}})}{\partial \hat{x}_{L}^{2}}\right]\right)
$$
{{< /math >}} 

with

{{< math >}}
$$
\frac{\partial^{2} D(\underline{\hat{x}})}{\partial \hat{x}_{i}^{2}}=2 w_{i} \tilde{f}\left(\hat{x}_{i}\right)
$$
{{< /math >}} 

### Sorted Locations & Equal Weights

When location vector $\underline{\hat{x}}$ is sorted, i.e., {{< math >}}$\hat{x}_{1}<\hat{x}_{2}<\ldots<\hat{x}_{L}${{< /math >}} , we obtain

{{< math >}}
$$
H\left(\hat{x}_{i}-\hat{x}_{j}\right)= 
\begin{cases}
0 & i < j \\
\frac{1}{2} & i=j \\
1 & i > j
\end{cases}
$$
{{< /math >}} 

Cumulative distribution can be simplified

{{< math >}}
$$
F\left(\hat{x}_{i}, \underline{\hat{x}}\right)=\frac{w_{i}}{2}+\sum_{j=1}^{i-1} w_{j}
$$
{{< /math >}} 

When samples are *equally* weighted (i.e. $w_i = \frac{1}{L}$), we get

{{< math >}}
$$
F(\hat{x}_{i}, \underline{\hat{x}}) = \frac{1}{2L} + \frac{i-1}{L} = \frac{2i - 1}{2L} \qquad i = 1, \dots, L
$$
{{< /math >}} 

Analytic solutions (possible in some special cases)

{{< math >}}
$$
\tilde{F}\left(\hat{x}_{i}\right)-F\left(\hat{x}_{i}, \underline{\hat{x}}\right)=0 \Rightarrow \hat{x}_{i}=\tilde{F}^{-1}(\frac{2 i-1}{2 L}) \qquad i=1, \ldots, L
$$
{{< /math >}} 

- E.g. Gaussian distribution:

  {{< math >}}
  $$
  \tilde{F}^{-1}(x)=\sqrt{2} \operatorname{erfinv}((2 i-1) /(2 L))
  $$
  {{< /math >}} 

#### Example: DMA of standard Normal Distribution


{{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/Kapture%202022-08-11%20at%2009.59.37.gif" caption="With increasing number of Dirac functions, the CDF can be well approximated." numbered="true" >}}

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-11%2009.57.08.png" alt="截屏2022-08-11 09.57.08" style="zoom: 50%;" />

### General Optimization

In general: Minimum of $D(\underline{\hat{x}})$ is obtained iteratively using **Newton’s method**

{{< math >}}
$$
\Delta \underline{\hat{x}}=-\mathbf{H}^{-1}(\underline{\hat{x}}) \underline{G}(\underline{\hat{x}})
$$
{{< /math >}} 

with

{{< math >}}
$$
\underline{G}(\underline{\hat{\hat{x}}})=\left[\frac{\partial D(\underline{\hat{x}})}{\partial \hat{x}_{1}}, \frac{\partial D(\underline{\hat{x}})}{\partial \hat{x}_{2}}, \ldots, \frac{\partial D(\underline{\hat{x}})}{\partial \hat{x}_{L}}\right]^{\top}
$$
{{< /math >}} 

and 

{{< math >}}
$$
\frac{\partial D(\underline{\hat{x}})}{\partial \hat{x}_{i}}=2 w_{i}\left[\tilde{F}\left(\hat{x}_{i}\right)-F\left(\hat{x}_{i}, \underline{\hat{x}}\right)\right]
$$
{{< /math >}} 

The Hessian $\mathbf{H}(\underline{x})$ is given by

{{< math >}}
$$
\mathbf{H}(\underline{\hat{x}})=2 \operatorname{diag}\left(\left[w_{1} \tilde{f}\left(\hat{x}_{1}\right), w_{2} \tilde{f}\left(\hat{x}_{2}\right), \ldots, w_{L} \tilde{f}\left(\hat{x}_{L}\right)\right]\right)
$$
{{< /math >}} 

The resulting Newton step:

{{< math >}}
$$
\Delta \underline{\hat{x}}=-\left[\frac{\tilde{F}\left(\hat{x}_{1}\right)-F\left(\hat{x}_{1}, \hat{\hat{x}}\right)}{\tilde{f}\left(\hat{x}_{1}\right)}, \frac{\tilde{F}\left(\hat{x}_{2}\right)-F\left(\hat{x}_{2}, \underline{\hat{x}}\right)}{\tilde{f}\left(\hat{x}_{2}\right)}, \ldots, \frac{\tilde{F}\left(\hat{x}_{L}\right)-F\left(\hat{x}_{L}, \underline{\hat{x}}\right)}{\tilde{f}\left(\hat{x}_{L}\right)}\right]^{\top}
$$
{{< /math >}} 

## Extension to Multivariate Distributions

- Extension to multivariate case is not trivial
  - Less nice properties of multivariate cumulative distributions 🤪

- Distinguish several classes of multivariate methods
  - Methods that generalize concept of CDF
  - Methods that perform reduction to univariate case
  - Kernel-based methods
  - Continuous flow between density approximations

### Challenge of Multivariate Cumulative Distributions

Definition for 2D:

{{< math >}}
$$
F(u, v)=\int_{-\infty}^{u} \int_{-\infty}^{v} f(x, y) d x d y
$$
{{< /math >}} 

However, $F(u, v)$ is *asymmetric* and definition is not unique. 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-11%2011.44.30.png" alt="截屏2022-08-11 11.44.30" style="zoom:50%;" />

Alternative definitions:

{{< math >}}
$$
\begin{aligned}
&F(u, v)=\int_{-\infty}^{u} \int_{v}^{\infty} f(x, y) d x d y \\
&F(u, v)=\int_{u}^{\infty} \int_{v}^{\infty} f(x, y) d x d y \\
&F(u, v)=\int_{u}^{\infty} \int_{-\infty}^{v} f(x, y) d x d y
\end{aligned}
$$
{{< /math >}} 

- Three CDFs are independent, forth is dependent.

For general $N$–dimensional random vectors: $2^N$ different variants,, $2^N - 1$ are independent

$\rightarrow$ exponentially complex!

- Use in statistical tests difficult
- Results differ depending on variant

Thus, we require generalization of concept of CDF. 💪

### Localized Cumulative Distributions (LCDs)

**Univariate case (1D)**

💡 Key idea

- Compare local probability masses of $\tilde{f}(x)$ and $f(x)$
- Integrate over intervals at all positions and all widths

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-11%2012.04.07.png" alt="截屏2022-08-11 12.04.07" style="zoom: 67%;" />

Compare $\tilde{A}(m, b)$ and $A(m,b), \forall m, b$

Symmetric, unique, but redundant...

**Multivariate case (2D)**

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-11%2012.13.09.png" alt="截屏2022-08-11 12.13.09" style="zoom: 67%;" />

Different kernels possible

- Rectangular kernels
- Gaussian kernels
- Anisotropic vs. isotropic kernels
- Separable vs. inseparable kernels

#### **Cumulative Transformation of Densities**

Given

- Random vector $\underline{x} \in \mathbb{R}^N$
- Probability density function $f(\underline{x}): \mathbb{R}^N \to \mathbb{R}_+$

{{< hl >}}**Localized Cumulative Distribution (LCD)**{{< /hl >}}:

{{< math >}}
$$
F(\underline{m}, b)=\int_{\mathbb{R}^{N}} f(\underline{x}) K(\underline{x}-\underline{m}, b) \mathrm{d} \underline{x}
$$
{{< /math >}} 

- $K(\cdot, \cdot)$: Kernel
- $\underline{m}$: Kernel location
- $\underline{b}$: Kernel width

 Specific kernel employed: 

{{< math >}}
$$
K(\underline{x}-\underline{m}, b)=\prod_{k=1}^{N} \exp \left(-\frac{1}{2} \frac{\left(x_{k}-m_{k}\right)^{2}}{b^{2}}\right)
$$
{{< /math >}} 

- Separable (i.e. in form of product)
- isotropic (i.e. same in each direction)
- Gaussian

Properties of LCD: 

- Symmetric
- Unique
- Multivariate

Examples

- **LCD** **(Rectangular Kernel)**

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-13%2010.44.51.png" alt="截屏2022-08-13 10.44.51" style="zoom:67%;" />

- **LCD (Gaussian Kernel)**

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-13%2010.47.53.png" alt="截屏2022-08-13 10.47.53" style="zoom: 33%;" />

#### **Generalized Cramér–von Mises Distance (GCvD)**

Given:

- LCD of given continuous density $\tilde{F}(\underline{m}, b)$
- LCD of Dirac mixture $F(\underline{m}, b)$

Definition:

{{< math >}}
$$
D=\int_{\mathbb{R}_{+}} w(b) \int_{\mathbb{R}^{N}}(\tilde{F}(\underline{m}, b)-F(\underline{m}, b))^{2} \mathrm{~d} \underline{m} \mathrm{~d} b
$$
{{< /math >}} 

Minimization of GCvD:

- For many Dirac components → high-dimensional optimization problem
- Gradient available, Hessian more difficult 
- Use Quasi-Newton method: L-BFGS


### Projected Cumulative Distributions (PCD)

#### Options for Reduction to Univariate Case

Reapproximation methods for univariate case readily available. How can we use univariate methods in multivariate case?

Solution

- Approximation on principal axis of PDF

  - Limited to densities where principal axis can be defined
  - Examples: Gaussian PDF, Bingham PDF on sphere
  - Does not cover the entire density 🤪

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-13%2010.57.53.png" alt="截屏2022-08-13 10.57.53" style="zoom: 33%;" />

- Cartesian product of 1D approximation 👎

  - Curse of dimensionality (as very similar to grid) 
  - Only for product densities (or rotations thereof)  
  - Inefficient coverage

- **Representing PDFs by *all* one-dimensional projections (a.k.a Radon transform)** 👍

  1. Represent the two densities $\tilde{f}(\underline{x})$ and $f(\underline{x})$ by infinite set of one-dimensional projections

     - Projections onto all unit vectors $\underline{u} \in \mathbb{S}^{N-1}$

     - We obtain sets of projections $\tilde{f}(r \mid \underline{u})$ and $f(r \mid u)$

     - These are the Radon transforms of $\tilde{f}(\underline{x})$ and $f(\underline{x})$ 

  2. We compare the sets of projections $\tilde{f}(r \mid \underline{u})$ and $f(r \mid u)$ for every $\underline{u} \in \mathbb{S}^{N-1}$

     - For comparison, we use the univariate cumulative distribution functions $\tilde{F}(r \mid \underline{u})$ and $F(r \mid u)$

     - These are unique, well defined, and easy to calculate

     - Resulting distance measures

       {{< math >}}
       $$
       D_{1}(\underline{u})=D(\tilde{f}(r \mid \underline{u}), f(r \mid \underline{u}))
       $$
       {{< /math >}} 

       depend on the projection vector $\underline{u}$

  3. We integrate these one-dimensional distance measures $D_1(\underline{u})$ over all all unit vectors $\underline{u} \in \mathbb{S}^{N-1}$

     - This gives multivariate distance measure $D(\tilde{f}(\underline{x}), f(\underline{x}))$
     - Typically a discretized subset of $\underline{u} \in \mathbb{S}^{N-1}$ is used
     - Distance measure minimized via univariate Newton updates

####  Radon Transform

- Represent general $N$-dimensional probability density functions via the set of all one-dimensional projections

- Linear projection of random vector $\underline{\boldsymbol{x}} \in \mathbb{R}^{N}$ to to scalar random variable $\boldsymbol{r} \in \mathbb{R}$ onto line described by unit vector $\underline{u} \in \mathbb{S}^{N-1}$

  {{< math >}}
  $$
  \boldsymbol{r} = \underline{u}^\top \underline{\boldsymbol{x}}
  $$
  

  {{< /math >}} 

- Given probability density function $f(\underline{x})$ of random vector $\underline{\boldsymbol{x}}$, density $f_r(r \mid \underline{u})$ of $\boldsymbol{r}$ is given by

  {{< math >}}
  $$
  f_{r}(r \mid \underline{u})=\int_{\mathbb{R}^{N}} f(\underline{t}) \delta\left(r-\underline{u}^{\top} \underline{t}\right) \mathrm{d} \underline{t}
  $$
  {{< /math >}} 

- $f_r(r \mid \underline{u})$ is Radon transform of $f(\underline{x})$ for all $\underline{u} \in \mathbb{S}^{N-1}$

Visualization:

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-13%2012.11.44.png" alt="截屏2022-08-13 12.11.44" style="zoom: 33%;" />

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-13%2012.12.06.png" alt="截屏2022-08-13 12.12.06" style="zoom:33%;" />

**Dirac Mixture Densities**

{{< math >}}
$$
f(\underline{x} \mid \hat{\mathbf{X}})=\sum_{i=1}^{L} w_{i} \delta\left(\underline{x}-\underline{\hat{x}}_{i}\right)
$$
{{< /math >}} 

with

{{< math >}}
$$
\hat{\mathbf{X}}=\left[\underline{\hat{x}}_{1}, \underline{\hat{x}}_{2}, \ldots, \underline{\hat{x}}_{L}\right]
$$
{{< /math >}} 

Radon transform is given by

{{< math >}}
$$
f_{r}(r \mid \underline{\hat{r}}, \underline{u})=\sum_{i=1}^{L} w_{i} \delta\left(\underline{u}^{\top} \underline{x} - \underline{u}^{\top} \underline{\hat{x}}_{i}\right)=\sum_{i=1}^{L} w_{i} \delta\left(r-\hat{r}_{i}(\underline{u})\right)
$$
{{< /math >}} 

- {{< math >}}$\hat{r}_{i}(\underline{u})=\underline{u}^{\top} \underline{x}_{i}, i=1, \ldots, L${{< /math >}} are the projected Dirac locations

Collect projected Dirac locations $\hat{r}_{i}(\underline{u})$ in vector

{{< math >}}
$$
\underline{\hat{r}}=\left[\hat{r}_{1}(\underline{u}), \hat{r}_{2}(\underline{u}), \ldots, \hat{r}_{L}(\underline{u})\right]^{\top}
$$
{{< /math >}} 

**Gaussian Densities**

- For Gaussian Density $f (\underline{x}) $with mean vector $\underline{\hat{x}}$ and covariance matrix $\mathbf{C}_x$, density $f_r(r \mid \underline{u})$ resulting from the projection is also Gaussian

- Its mean $\hat{r}(\underline{u})$ can simply be calculated by taking the expected value

  {{< math >}}
  $$
  \hat{r}(\underline{u})=\mathrm{E}\{\boldsymbol{r}(\underline{u})\}=\mathrm{E}\left\{\underline{u}^{\top} \underline{\boldsymbol{x}}\right\}=\underline{u}^{\top} \underline{\hat{x}}
  $$
  {{< /math >}} 

- Its standard deviation $\sigma_r(\underline{u})$ is given by

  {{< math >}}
  $$
  \sigma_{r}^{2}(\underline{u})=\mathrm{E}\left\{(\boldsymbol{r}(\underline{u})-\hat{r}(\underline{u}))^{2}\right\}=\mathrm{E}\left\{\left(\underline{u}^{\top} \boldsymbol{x}-\underline{u}^{\top} \underline{\hat{x}}\right)^{2}\right\}=\mathrm{E}\left\{\underline{u}^{\top}(\boldsymbol{x}-\underline{\hat{x}})(\boldsymbol{x}-\underline{\hat{x}})^{\top} \underline{u}\right\}=\underline{u}^{\top} \mathbf{C}_{x} \underline{u}
  $$
  {{< /math >}} 

**Gaussian Mixture Densities**

- For $N$-dimensional Gaussian mixture densities $f(\underline{x})$ of the form

  {{< math >}}
  $$
  f(\underline{x})=\sum_{i=1}^{M} w_{i} \frac{1}{\sqrt{(2 \pi)^{N}\left|\mathbf{C}_{x, i}\right|}} \exp \left(-\frac{1}{2}\left(\underline{x}-\underline{\hat{x}}_{i}\right)^{\top} \mathbf{C}_{x, i}^{-1}\left(\underline{x}-\underline{\hat{x}}_{i}\right)\right)
  $$
  {{< /math >}} 

  the density $f_r(r, \underline{u})$ is also a Gaussian mixture

- Due to the linearity of the projection operator, it is given by

  {{< math >}}
  $$
  f_{r}(r \mid \underline{u})=\sum_{i=1}^{M} w_{i} \frac{1}{\sqrt{2 \pi} \sigma_{r, i}(\underline{u})} \exp \left(-\frac{1}{2} \frac{\left(r-\hat{r}_{i}(\underline{u})\right)^{2}}{\sigma_{r, i}^{2}(\underline{u})}\right)
  $$
  {{< /math >}} 

  with 

  {{< math >}}
  $$
  \hat{r}_{i}(\underline{u})=\underline{u}^{\top} \underline{\hat{x}}_{i}
  $$
  {{< /math >}} 

  and

  {{< math >}}
  $$
  \sigma_{r, i}(\underline{u})=\sqrt{\underline{u}^{\top} \mathbf{C}_{x, i} \underline{u}}
  $$
  {{< /math >}} 

### Multivariate Cramér-von Mises Distance

Multivariate distance measure between two continuous and/or discrete probability density functions

1. **One-dimensional Projections via Radon Transform**

   Given density $\tilde{f}(\underline{x})$ and its approximation $f(\underline{x})$, represented by their Radon transforms $\tilde{f}(r \mid \underline{u})$ (i.e. by their 1D projections onto unit vectors $\underline{u} \in \mathbb{S}^{N-1}$)

2. **One-dimensional Cumulative Distributions**

   Based on Radon transform $\tilde{f}(r \mid \underline{u})$, calculate one-dimensional cumulative distributions of the projected densities as

   {{< math >}}
   $$
   \tilde{F}(r \mid \underline{u})=\int_{\infty}^{r} \tilde{f}(t, \underline{u}) \mathrm{d} t
   $$
   {{< /math >}} 

   and similarly for $F(r \mid \underline{u})$

   - Example: For Dirac mixture approximation, cumulative distribution function of its Radon transform is given by

     {{< math >}}
     $$
     F(r \mid \underline{\hat{r}}, \underline{u})=\sum_{i=1}^{L} w_{i} \mathrm{H}\left(r-\hat{r}_{i}(\underline{u})\right)
     $$
     {{< /math >}} 

3. **One-dimensional Distance**

   - For comparing the one-dimensional projections, we compare their cumulative distributions $\tilde{F}(r \mid \underline{u})$ and $F(r \mid \underline{\hat{r}}, \underline{u})$ for all $\underline{u} \in \mathbb{S}^{N-1}$

   - As distance measure use integral squared distance

     {{< math >}}
     $$
     D_{1}(\underline{\hat{r}}, \underline{u})=\int_{\mathbb{R}}[\tilde{F}(r \mid \underline{u})-F(r \mid \underline{\hat{r}}, \underline{u})]^{2} \mathrm{~d} r
     $$
     {{< /math >}} 

   - Gives distance between the projected densities in the direction of the unit vector $\underline{u}$ for all $\underline{u}$

4. **One-dimensional Newton Step**

   -  Newton step can now be written as

     {{< math >}}
     $$
     \Delta \underline{\hat{r}}(\underline{\hat{r}}, \underline{u})=-\mathbf{H}^{-1}(\underline{\hat{r}}, \underline{u}) \underline{G}(\underline{\hat{r}}, \underline{u})
     $$
     {{< /math >}} 

     with

     {{< math >}}
     $$
     \begin{aligned}
     \underline{G}(\underline{\hat{r}}, \underline{u})&=\left[\frac{\partial D_{1}(\underline{\hat{r}}, \underline{u})}{\partial \hat{r}_{1}}, \frac{\partial D_{1}(\underline{\hat{r}}, \underline{u})}{\partial \hat{r}_{2}}, \ldots, \frac{\partial D_{1}(\underline{\hat{r}}, \underline{u})}{\partial \hat{r}_{L}}\right]^{\top} \\
     \frac{\partial D_{1}(\underline{\hat{r}}, \underline{u})}{\partial \hat{r}_{i}}&=2 w_{i}\left[\tilde{F}\left(\hat{r}_{i} \mid \underline{u}\right)-F\left(\hat{r}_{i} \mid \underline{u}\right)\right]
     
     \end{aligned}
     $$
     {{< /math >}} 

   - Hessian $\mathbf{H}(\underline{r}, \underline{u})$ is given by

     {{< math >}}
     $$
     \mathbf{H}(\underline{\hat{r}}, \underline{u})=2 \operatorname{diag}\left(\left[w_{1} \tilde{f}\left(\hat{r}_{1} \mid \underline{u}\right), w_{2} \tilde{f}\left(\hat{r}_{2} \mid \underline{u}\right), \ldots, w_{L} \tilde{f}\left(\hat{r}_{L} \mid \underline{u}\right)\right]\right)
     $$
     {{< /math >}} 

   - $\Rightarrow$ Resulting Newton step

     {{< math >}}
     $$
     \Delta \underline{\hat{r}}(\underline{\hat{r}}, \underline{u})=-\left[\frac{\tilde{F}\left(\hat{r}_{1} \mid \underline{u}\right)-F\left(\hat{r}_{1} \mid \underline{\hat{r}}, \underline{u}\right)}{\tilde{f}\left(\hat{r}_{1} \mid \underline{u}\right)},  \ldots, \frac{\tilde{F}\left(\hat{r}_{L} \mid \underline{u}\right)-F\left(\hat{r}_{L} \mid \underline{\hat{r}}, \underline{u}\right)}{\tilde{f}\left(\hat{r}_{L} \mid \underline{u}\right)}\right]^{\top}
     $$
     {{< /math >}} 

5. **Backprojection to $N$-dimensional space**

   - For specific projection vector $\underline{u}$: Newton update $\Delta \underline{\hat{r}}(\underline{\hat{r}}, \underline{u})$

   - Backprojection into original $N$-dimensional space: Update can be used to modify original Dirac locations in direction along the vector $\underline{u}$

   - For every location vector $\underline{\hat{x}}_i$ we obtain

     {{< math >}}
     $$
     \Delta \underline{\hat{x}}_{i}(\underline{u})=\Delta \underline{\hat{r}}(\underline{\hat{r}}, \underline{u}) \cdot \underline{u}
     $$
     {{< /math >}} 

6. **Step 6 Assemble Multivariate Distance**

   - Individual 1D distances $D_1(\underline{r}, \underline{u})$ can be assembled to form multivariate distance measure

   - Performed by integrating over all 1D distances depending on unit vector $\underline{u}$ 

     {{< math >}}
     $$
     D_{N}(\hat{\mathbf{X}})=\int_{\mathbb{S}^{N-1}} D_{1}(\underline{\hat{r}}, \underline{u}) \mathrm{d} \underline{u}
     $$
     {{< /math >}} 

   - Plugging in $D_1(\underline{r}, \underline{u})$:

     {{< math >}}
     $$
     D_{N}(\hat{\mathbf{X}})=\int_{\mathbb{S}^{N-1}} \int_{\mathbb{R}}[\tilde{F}(r \mid \underline{u})-F(r \mid \underline{\hat{r}}, \underline{u})]^{2} \mathrm{~d} r \mathrm{~d} \underline{u} \quad \text { with } r=\underline{u}^{\top} \cdot \underline{x}
     $$
     {{< /math >}} 

7. **Perform Full Newton Update**

   Full Newton update by integrating over all partial updates along projection vectors $\underline{u}$

   {{< math >}}
   $$
   \Delta \underline{\hat{x}}_{i}=\int_{\mathbb{S}^{N-1}} \Delta \underline{\hat{x}}_{i}(\underline{u}) \mathrm{d} \underline{u}
   $$
   {{< /math >}} 

#### **Discretization of Space of Unit Vectors**

- In practice, Space $\mathbb{S}^{N-1}$ containing unit vectors $\underline{u}$ has to be discretized

- Two options are available for performing the discretization:

  - Deterministic discretization, e.g., by calculating a grid
  - Random discretization by drawing uniform samples from the hypersphere

- For both cases: Consider $K$ samples $\underline{u}_k$

- Integration reduces to summation

  {{< math >}}
  $$
  \Delta \underline{\hat{x}}_{i} \approx \frac{1}{K} \sum_{k=1}^{K} \Delta \underline{\hat{x}}_{i}\left(\underline{\hat{u}}_{k}\right) \quad \text { for } i=1,2, \ldots, L
  $$
  {{< /math >}} 

- Stopping criterion

  - Given initial locations for the location of the Dirac components

  - Full Newton updates are performed until the maximum change over all location vectors

    {{< math >}}
    $$
    \max _{i}\left|\Delta \underline{\hat{x}}_{i}\right|
    $$
    {{< /math >}} 

    falls below a given threshold

**Complete Algorithm (Randomized Variant)**

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-14%2011.44.09.png" alt="截屏2022-08-14 11.44.09" style="zoom: 50%;" />