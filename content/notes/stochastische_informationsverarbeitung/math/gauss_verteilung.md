---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 108
# ============================================================

# ========== Basic metadata ==========
title: Gaußverteilung
date: 2022-07-03
draft: false
type: book # page type
authors:
  - admin
tags:
  - SI
  - Lecture Notes
  - Math
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

## Skalarer Fall (1D)

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/WP_Normalverteilung_01-1024x576.jpg" alt="Eigenschaften Normalverteilung, Normalverteilung, Wendestellen, Standardabweichung, Varianz, Mittelwert, Sigma, Mü, Maximum, Erwartungswert, Funktion Normalverteilung" style="zoom: 50%;" />

{{< math >}}
$$
f(x)=\frac{1}{\sqrt{2 \pi} \sigma} \exp \left\{-\frac{1}{2} \frac{(x-\hat{x})^{2}}{\sigma^{2}}\right\}
$$
{{< /math >}} 

- Erwartungswert 
  $$
  E_{f}\{x\}=\hat{x}
  $$

- Varianz

  {{< math >}}
  $$
  E_{f}\left\{(x-\hat{x})^{2}\right\}=\sigma^{2}
  $$
  {{< /math >}} 



> Given the parameters $\mu$ and $\sigma$ of a Gaussian density, mean and variance are already given. On the other hand, assume that we wish to approximate a given density $\tilde{f}_x$ with a simpler density of the same mean and standard deviation. Then, given the mean and the standard deviation of the density $\tilde{f}_x$, an appropriate Gaussian density is immediately obtained. This is a property not generally shared by more complicated densities.

## 2D Normalverteilung

{{< math >}}
$$
\begin{aligned}
f_{x y}(x, y)&=\frac{1}{2 \pi \sigma_{x} \sigma_{y} \sqrt{1-r^{2}}} \exp \left\{-\frac{1}{2} Q(x, y)\right\} \\
Q(x, y)&=\frac{1}{1-r}\left\{\frac{(x-\hat{x})^{2}}{\sigma_{x}^{2}}-2 r \frac{x-\hat{x}}{\sigma_{x}} \frac{y-\hat{y}}{\sigma_{y}}+\frac{(y-\hat{y})^{2}}{\sigma_{y}^{2}}\right\}

\end{aligned}
$$
{{< /math >}} 

- $r \in [-1, 1]$: Korrelationskoeffizent (in some literature also written as $\rho$)

Alternativ

{{< math >}}
$$
f_{x y}(x, y)=\mathcal{N} \left(\left[\begin{array}{l}
x \\
y
\end{array}\right],\left[\begin{array}{l}
\hat{x} \\
\hat{y}
\end{array}\right],\left[\begin{array}{ll}
C_{x x} & C_{x y} \\
C_{y x} & C_{y y}
\end{array}\right]\right)
$$
{{< /math >}} 

mit

{{< math >}}
$$
\left[\begin{array}{ll}
c_{x x} & c_{x y} \\
c_{y x} & c_{y y}
\end{array}\right]=\left[\begin{array}{lc}
\sigma_{x}^{2} & r \sigma_{x} \sigma_{y} \\
r \sigma_{x} \sigma_{y} & \sigma_{y}^{2}
\end{array}\right]
$$
{{< /math >}} 

### Correlationskoeffizient

{{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/Figure_1.png" caption="Correlation of bivariate Gaussian distribution ($\rho$ is the correlation coefficient). (Source: [Combination of Multivariate Gaussian Distributions through Error Ellipses](https://geostatisticslessons.com/lessons/errorellipses))" numbered="true" >}}

- unkorreliert ($r = 0$) (Figure 1 right)
  - $\Rightarrow \boldsymbol{x}, \boldsymbol{y}$ unkorreliert
  - $\Rightarrow$ (nur für Gauß) $\boldsymbol{x}, \boldsymbol{y}$ unabhängig ({{< math >}}$f_{\boldsymbol{x}, \boldsymbol{y}} = f_{\boldsymbol{x}}(x) f_{\boldsymbol{y}}(y)${{< /math >}}) 

- positiv korreliert ($r > 0$) (Figure 1 left)
- positiv korreliert ($r < 0$) (Figure 1 middle)





## $N$-dim. Normalverteilung

{{< math >}}
$$
f_{\boldsymbol{x}}(x)=\frac{1}{\sqrt{(2 \pi)^{N} \cdot|\mathbf{C}|}} \exp \left\{-\frac{1}{2}(\underline{x}-\underline{\hat{x}})^{\top} \mathbf{C}^{-1}(\underline{x}-\underline{\hat{x}})\right\}
$$
{{< /math >}} 

- {{< math >}}$\underline{\hat{x}}${{< /math >}}: Mean
- {{< math >}}$\mathbf{C}${{< /math >}}: Kovarianzmatrix