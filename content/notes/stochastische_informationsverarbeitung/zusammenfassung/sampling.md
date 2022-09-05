---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 760
# ============================================================

# ========== Basic metadata ==========
title: Sampling
date: 2022-08-28
draft: false
type: book # page type
authors:
  - admin
tags:
  - SI
  - Lecture Notes
  - Zusammenfassung
  - Summary
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

## Reapproximation von Dichten

Approximate original continuous density with discrete Dirac Mixture

{{< math >}}
$$
f(\underline{x})=\sum_{i=1}^{L} w_{i} \cdot \delta\left(\underline{x}-\underline{\hat{x}}_{i}\right)
$$
{{< /math >}} 

- Weights $w_{i}>0, \displaystyle \sum_{i=1}^{L} w_{i}=1$
- $\underline{x}_i$: locations / samples

In univariate case (1D), compare **cumulative distribution functions (CDFs)** $\tilde{F}(x), F(x)$ using **Cramér–von Mises distance**:

{{< math >}}
$$
D(\underline{\hat{x}})=\int_{\mathbb{R}}(\tilde{F}(x)-F\left(x, \underline{\hat{x}})\right)^{2} \mathrm{~d} x
$$
{{< /math >}} 

{{< math >}}$F(x, \underline{\hat{x}})${{< /math >}}: Dirac mixture cumulative distribution

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

We minimize the Cramér–von Mises distance {{< math >}}$D(\underline{\hat{x}})${{< /math >}} with Newton's method.

### Generalization of concept of CDF

#### Localized Cumulative Distribution (LCD)

{{< math >}}
$$
F(\underline{m}, b)=\int_{\mathbb{R}^{N}} f(\underline{x}) K(\underline{x}-\underline{m}, b) \mathrm{d} \underline{x}
$$
{{< /math >}} 

- $K(\cdot, \cdot)$: Kernel

  {{< math >}}
  $$
  K(\underline{x}-\underline{m}, b)=\prod_{k=1}^{N} \exp \left(-\frac{1}{2} \frac{\left(x_{k}-m_{k}\right)^{2}}{b^{2}}\right)
  $$
  {{< /math >}} 

- $\underline{m}$: Kernel location

- $\underline{b}$: Kernel width

Properties of LCD:

- Symmetric
- Unique
- Multivariate 

Generalized Cramér–von Mises Distance (GCvD)

{{< math >}}
$$
D=\int_{\mathbb{R}_{+}} w(b) \int_{\mathbb{R}^{N}}(\tilde{F}(\underline{m}, b)-F(\underline{m}, b))^{2} \mathrm{~d} \underline{m} \mathrm{~d} b
$$
{{< /math >}} 

- $\tilde{F}(\underline{m}, b)$: LCD of continuous density
- $F(\underline{m}, b)$: LCD of Dirac mixture

Minimization of GCvD: Quasi-Newton method (L-BFGS)

#### Projected Cumulative Distribution (PCD)

Use reapproximation methods for univariate case in multivariate case.

**Radon Transform**

Represent general $N$-dimensional probability density functions via the set of all one-dimensional projections

- Linear projection of random vector $\underline{\boldsymbol{x}} \in \mathbb{R}^{N}$ to to scalar random variable $\boldsymbol{r} \in \mathbb{R}$ onto line described by unit vector $\underline{u} \in \mathbb{S}^{N-1}$

  {{< math >}}
  $$
  \boldsymbol{r} = \underline{u}^\top \underline{\boldsymbol{x}}
  $$


  {{< /math >}} 

- Given probability density function $f(\underline{x})$ of random vector $\underline{\boldsymbol{x}}$, density $f_r(r \mid \underline{u})$ is Radon transfrom of $f(\underline{x})$ for all $\underline{u} \in \mathbb{S}^{N-1}$

  {{< math >}}
  $$
  f_{r}(r \mid \underline{u})=\int_{\mathbb{R}^{N}} f(\underline{t}) \delta\left(r-\underline{u}^{\top} \underline{t}\right) \mathrm{d} \underline{t}
  $$
  {{< /math >}} 

**Representing PDFs by *all* one-dimensional projections**

1. Represent the two densities $\tilde{f}(\underline{x})$ and $f(\underline{x})$ by their Radon transforms $\tilde{f}(r \mid \underline{u})$ and $f(r \mid u)$

2. Compare the sets of projections $\tilde{f}(r \mid \underline{u})$ and $f(r \mid u)$ for every $\underline{u} \in \mathbb{S}^{N-1}. Resulting distance is

   {{< math >}}
   $$
   D_{1}(\underline{u})=D(\tilde{f}(r \mid \underline{u}), f(r \mid \underline{u}))
   $$
   {{< /math >}} 

3. Integrate these one-dimensional distance measures $D_1(\underline{u})$ over all unit vectors $\underline{u} \in \mathbb{S}^{N-1}$ to get the multivariate distance measure $D(\tilde{f}(\underline{x}), f(\underline{x}))$. Minimize via univariate Newton updates.

















## Navies Partikel Filter

{{% callout note %}}
Üb A13.2
{{% /callout %}}

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-14%2017.37.55.png" alt="截屏2022-08-14 17.37.55" style="zoom: 33%;" />

### Prädiktion

💡Update Sample Positionen. Gewichte bleiben gleich.

1. {{< math >}}$f_{k}^{e}\left(\underline{x}_{k}\right)${{< /math >}} durch Dirac Mixture darstellen

   {{< math >}}
   $$
   f_{k}^{e}\left(\underline{x}_{k}\right)=\sum_{i=1}^{L} w_{k}^{e, i} \cdot \delta\left(\underline{x}_{k}-\underline{\hat{x}}_{k}^{e, i}\right) \qquad w_{k}^{e, i}=\frac{1}{L}, i \in\left\{1, \ldots, L\right\}
   $$
   {{< /math >}} 

2. Ziehe Samples zum Zeitpunkt $k+1$

   {{< math >}}
   $$
   \underline{\hat{x}}_{k+1}^{p, i} \sim f\left(\underline{x}_{k+1} \mid \hat{x}_{k}^{e, i}\right)
   $$
   {{< /math >}} 

   Gewichte bleiben gleich

   {{< math >}}
   $$
   w_{k+1}^{p, i} = w_{k}^{e, i}
   $$
   {{< /math >}} 

3. {{< math >}}$f_{k+1}^{p}\left(\underline{x}_{k}\right)${{< /math >}} durch Dirac Mixture darstellen

   {{< math >}}
   $$
   f_{k+1}^{p}\left(\underline{x}_{k+1}\right)=\sum_{i=1}^{L} w_{k+1}^{p, i} \delta\left(\underline{x}_{k+1}-\underline{\hat{x}}_{k+1}^{p, i}\right)
   $$
   {{< /math >}} 

### Filterung

💡Update Gewichte. Sample Positionen bleiben gleich.

{{< math >}}
$$
\begin{aligned}
f_{k}^{e}\left(\underline{x}_{k}\right) &\propto f\left(\underline{y}_{k} \mid \underline{x}_{k}\right) \cdot f_{k}^{p}\left(\underline{x}_{k}\right)\\
&=f\left(\underline{y}_{k} \mid \underline{x}_{k}\right) \cdot \sum_{i=1}^{L} w_{k}^{p, i} \cdot \delta\left(\underline{x}_{k}-\underline{\hat{x}}_{k}^{p, i}\right)\\
&=\sum_{i=1}^{L} \underbrace{w_{k}^{p, i} \cdot f\left(\underline{y}_{k} \mid \hat{\underline{x}}_{k}^{p, i}\right)}_{\propto w_{k}^{e, i}} \cdot \delta(\underline{x}_{k}-\underbrace{\underline{\hat{x}}_{k}^{p, i}}_{\underline{\hat{x}}_{k}^{e, i}})
\end{aligned}
$$
{{< /math >}} 

1. Positionen bleiben gleich

   {{< math >}}
   $$
   \underline{\hat{x}}_{k}^{e, i} = \underline{\hat{x}}_{k}^{p, i}
   $$
   {{< /math >}} 

2. Gewichte adaptieren

   {{< math >}}
   $$
   w_{k}^{e, i} \propto w_{k}^{p, i} \cdot f\left(\underline{y}_{k} \mid \hat{\underline{x}}_{k}^{p, i}\right)
   $$
   {{< /math >}} 

   und Normalisieren

   {{< math >}}
   $$
   w_{k}^{e, i}:=\frac{w_{k}^{e, i}}{\displaystyle \sum_{i} w_{k}^{e,i}}
   $$
   {{< /math >}} 

### Problem

- Varianz der Samples erhöht sich mit Filterschritten

- Partikel sterben aus $\rightarrow$ Degenerierung des Filters
- Aussterben schneller, je genauer die Messung (Paradox!)

## Resampling

- Approximation der gewichteter Samples durch ungewichtete

  {{< math >}}
  $$
  f_{k}^{e}\left(\underline{x}_{k}\right)=\sum_{i=1}^{L} w_{k}^{e, i} \cdot \delta\left(\underline{x}_{k}-\underline{\hat{x}}_{k}^{e, i}\right) \approx \sum_{i=1}^{L} \frac{1}{L} \delta\left(\underline{x}_{k}-\underline{\hat{x}}_{k}^{e, i}\right)
  $$
  {{< /math >}} 

- Gegeben: $L$ Partikel mit Gewichten $w_i$
- Gesucht: $L$ Partikel mit Geweichte $\frac{1}{L}$ (gleichgewichtet)



