---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 104
# ============================================================

# ========== Basic metadata ==========
title: Zweidimensionale Zufallsvariable
date: 2022-06-05
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

## Verteilungsfunktion und Dichte

Eine vektorwertige Funktion

{{< math >}}
$$
\underline{X}=\underline{X}(\omega): \Omega \rightarrow \mathbb{R}^{2}
$$
{{< /math >}} 

die jedem Ergebnis $\omega \in \Omega$ einen Vektor $\underline{x}=\left[\begin{array}{l}x_{1} \\ x_{2}\end{array}\right]$ zuordnet, heißt {{< hl >}}**mehrdimensionale Zufallsvariable**{{< /hl >}}, wenn das Urbild eines jeden Intervalls $I_{\underline{a}}=\left(-\infty, a_{1}\right] \times\left(-\infty, a_{2}\right] \subset \mathbb{R}^{2}$ ein Ereignis ist

{{< math >}}
$$
X^{-1}\left(I_{a}\right) \in \mathfrak{B}, \quad \forall \underline{a} \in \mathbb{R}^{2}.
$$
{{< /math >}} 

### Verteilungsfunktion

Die Funktion

{{< math >}}
$$
\begin{aligned}
F_{\underline{X}}(\underline{x}) &=F_{X_{1}, X_{2}}\left(x_{1}, x_{2}\right) \\
&=\mathrm{P}\left(X_{1} \leq x_{1}, X_{2} \leq x_{2}\right)
\end{aligned}
$$
{{< /math >}} 

der zweidimensionalen Zufallsvariablen $\underline{X}$ heißt {{< hl >}}**Verteilungsfunktion**{{< /hl >}} von $\underline{X}$.

### Dichte

Die {{< hl >}}**Dichte**{{< /hl >}} der zweidimensionalen Zufallsvariablen $\underline{X}$: partielle Ableitungen der Verteilungsfunktion $F_{\underline{X}}(\underline{x})$

{{< math >}}
$$
f_{\underline{X}}(\underline{x})=f_{X_{1}, X_{2}}\left(x_{1}, x_{2}\right)=\frac{\partial^{2}}{\partial x_{1} \partial x_{2}} F_{X_{1}, X_{2}}\left(x_{1}, x_{2}\right)
$$
{{< /math >}} 

Sind beide Komponenten diskret verteilt, schreibt man für deren „Dichte“

{{< math >}}
$$
f_{\underline{X}}(\underline{x})=\sum_{n=1}^{\infty} \sum_{k=1}^{\infty} \mathrm{P}\left(X_{1}=x_{1, n}, X_{2}=x_{2, k}\right) \cdot \delta\left(x_{1}-x_{1, n}, x_{2}-x_{2, k}\right)
$$
{{< /math >}} 

mit der zweidimensionalen $\delta$- Distribution $\delta(x_1, x_2)$ und den Einzelwahrscheinlichkeiten $\mathrm{P}\left(X_{1}=x_{1, n}, X_{2}=x_{2, k}\right)$.

## Randdichten und bedingte Dichten

$\underline{X}$ sei eine zweidimensionale Zufallsvariable mit der Dichte $f(\underline{X})=f_{\underline{X}}\left(x_{1}, x_{2}\right)$. Dann heißen

{{< math >}}
$$
\begin{array}{l}
f_{X_{1}}\left(x_{1}\right)=\int_{-\infty}^{\infty} f_{\underline{X}}\left(x_{1}, x_{2}\right) \mathrm{d} x_{2} \\
f_{X_{2}}\left(x_{2}\right)=\int_{-\infty}^{\infty} f_{\underline{X}}\left(x_{1}, x_{2}\right) \mathrm{d} x_{1}
\end{array}
$$
{{< /math >}} 

{{< hl >}}**Randdichten**{{< /hl >}} von $X$.

$X$ sei eine zweidimensionale Zufallsvariable mit der Dichte $f_X(x_1, x_2)$ und es gelte $f_{X_1}(x_1) > 0$ und $f_{X_2}(x_2) > 0$ . Dann heißt

{{< math >}}
$$
f_{X_{1}}\left(x_{1} \mid X_{2}=x_{2}\right)=\frac{f_{\underline{X}}\left(x_{1}, x_{2}\right)}{f_{X_{2}}\left(x_{2}\right)}
$$
{{< /math >}} 

die {{< hl >}}**bedingte Dichte**{{< /hl >}} von $X_1$ unter der Bedingung $X_2 = x_2$.

{{< math >}}
$$
f_{X_{2}}\left(x_{2} \mid X_{1}=x_{1}\right)=\frac{f_{\underline{X}}\left(x_{1}, x_{2}\right)}{f_{X_{1}}\left(x_{1}\right)}
$$
{{< /math >}} 

ist die bedingte Dichte von $X_2$ unter der Bedingung $X_1 = x_1$.

{{% callout note %}}
**Formel von der totalen Wahrscheinlichkeit für Dichten**

{{< math >}}
$$
f\_{X\_{1}}\left(x\_{1}\right)=\int\_{-\infty}^{\infty} f\_{X\_{1}}\left(x\_{1} \mid X\_{2}=x_{2}\right) f\_{X\_{2}}\left(x\_{2}\right) \mathrm{d} x\_{2}
$$


{{< /math >}} 

{{% /callout %}}

{{% callout note %}}
**Satz von Bayes für Dichten**

{{< math >}}
$$
f\_{X\_{2}}\left(x\_{2} \mid X\_{1}=x\_{1}\right)=\frac{f\_{X\_{1}}\left(x\_{1} \mid X\_{2}=x\_{2}\right) f\_{X\_{2}}\left(x\_{2}\right)}{\int\_{-\infty}^{\infty} f\_{X\_{1}}\left(x\_{1} \mid X\_{2}=x\_{2}\right) f\_{X\_{2}}\left(x\_{2}\right) \mathrm{d} x\_{2}}
$$
{{< /math >}} 

{{% /callout %}}

Der {{< hl >}}**bedingte Erwartungswert**{{< /hl >}}  einer Zufallsvariablen $X_1$ unter der Bedingung $X_2 = x_2$ ist

{{< math >}}
$$
\mathrm{E}_{f_{\underline{\underline{x}}}}\left\{X_{1} \mid X_{2}=x_{2}\right\}=\int_{-\infty}^{\infty} x_{1} f_{X_{1}}\left(x_{1} \mid X_{2}=x_{2}\right) \mathrm{d} x_{1}
$$
{{< /math >}} 

## Unabhängigkeit von Zufallsvariablen

Zwei Zufallsvariablen $X, Y$ heißen {{< hl >}}**unabhängig**{{< /hl >}} , wenn gilt

{{< math >}}
$$
f_{X, Y}(x, y)=f_{X}(x) \cdot f_{Y}(y)
$$
{{< /math >}} 

Damit gilt auch

{{< math >}}
$$
f_{X}(x \mid Y=y)=f_{X}(x)
$$
{{< /math >}} 

**Erwartungswert** für zweidimensionale Zufallsvariablen:

{{< math >}}
$$
\mathrm{E}_{f_{X, Y}}\{g(X, Y)\}=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) f_{X, Y}(x, y) \mathrm{d} x \mathrm{~d} y
$$
{{< /math >}} 

Die **Kovarianz** {{< math >}}$\sigma_{X, Y}=\operatorname{Cov}_{\boldsymbol{f}_{X, Y}}\{X, Y\}${{< /math >}}  von zwei Zufallsvariablen $X$ und $Y$ ist

{{< math >}}
$$
\sigma_{X, Y}=\operatorname{Cov}_{f_{X, Y}}\{X, Y\}=\mathrm{E}\{(X-\mathrm{E}\{X\}) \cdot(Y-\mathrm{E}\{Y\})\}=\mathrm{E}\left\{\left(X-\mu_{x}\right) \cdot\left(Y-\mu_{y}\right)\right\}
$$
{{< /math >}} 

Der **Korrelationskoeffizient** von $X$ und $Y$:

{{< math >}}
$$
\rho_{X, Y}=\frac{\operatorname{Cov}_{f_{X, Y}}\{X, Y\}}{\sqrt{\operatorname{Var}_{f_{X}}\{X\} \operatorname{Var}_{f_{Y}}\{Y\}}}=\frac{\sigma_{X, Y}}{\sigma_{X} \cdot \sigma_{Y}} \in [-1, 1]
$$
{{< /math >}} 

- stellt ein *Ähnlichkeitsmaß* der Zufallsvariablen $X$ und $Y$ dar
  - $\left|\rho_{X, Y}\right|=1$: $X$ und $Y$ sind maximal ähnlich
  - $\left|\rho_{X, Y}\right|=0$: $X$ und $Y$ sind komplett unähnlich (*i.e.*, $X$ und $Y$ sind **unkorreliert**)
    - Unabhängige Zufallsvariablen sind unkorreliert. (Die Umkehrung dieser Aussage gilt im allgemeinen NICHT!)
    - Haben $X$ und $Y$ eine Normalevwrteilung und hat $[X, Y]^\top$ eine zweidimensionale Normalverteilung, folgt aus Unkorreliertheit $\rho_{X, Y} = 0$ auch die Unabhängigkeit von $X$ und $Y$

Ist {{< math >}}$\underline{X}=\left\{X_{1}, X_{2}, \ldots, X_{N}\right\}^{\top}${{< /math >}}  ein $N$-dimensional Zufallsvektor, seine **Kovarianzmatrix** ist

{{< math >}}
$$
\begin{array}{l}
\operatorname{Cov}_{f_{\underline{x}}}\{\underline{X}\}=\mathrm{E}_{f_{\underline{\underline{x}}}}\left\{(\underline{X}-\underline{\mu})(\underline{X}-\underline{\mu})^{\top}\right\}\\ 
\newline
=\left[\begin{array}{cccc}
\operatorname{Var}_{X_{1}}\left\{X_{1}\right\} & \operatorname{Cov}_{X_{1}, X_{2}}\left\{X_{1}, X_{2}\right\} & \cdots & \operatorname{Cov}_{X_{1}, X_{N}}\left\{X_{1}, X_{N}\right\} \\
\operatorname{Cov}_{X_{2}, X_{1}}\left\{X_{2}, X_{1}\right\} & \operatorname{Var}_{X_{2}}\left\{X_{2}\right\} & \cdots & \mathrm{Cov}_{X_{2}, X_{N}}\left\{X_{2}, X_{N}\right\} \\
\vdots & \vdots & \ddots & \vdots \\
\operatorname{Cov}_{X_{N}, X_{1}}\left\{X_{N}, X_{1}\right\} & \operatorname{Cov}_{X_{N}, X_{2}}\left\{X_{N}, X_{2}\right\} & \cdots & \operatorname{Var}_{X_{N}}\left\{X_{N}\right\}
\end{array}\right]\\
\newline
=\left[\begin{array}{cccc}
\sigma_{X_{1}}^{2} & \rho_{X_{1}, X_{2}} \sigma_{X_{1}} \sigma_{X_{2}} & \cdots & \rho_{X_{1}, X_{N}} \sigma_{X_{1}} \sigma_{X_{N}} \\
\rho_{X_{2}, X_{1}} \sigma_{X_{2}} \sigma_{X_{1}} & \sigma_{X_{2}}^{2} & \cdots & \rho_{X_{2}, X_{N}} \sigma_{X_{2}} \sigma_{X_{N}} \\
\vdots & \vdots & \ddots & \vdots \\
\rho_{X_{N}, X_{1}} \sigma_{X_{N}} \sigma_{X_{1}} & \rho_{X_{N}, X_{2}} \sigma_{X_{N}} \sigma_{X_{2}} & \cdots & \sigma_{X_{N}}^{2}
\end{array}\right] 
\end{array}
$$
{{< /math >}} 

{{< spoiler text="Detail" >}}
![截屏2022-06-05 18.47.05](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-06-05%2018.47.05.png)
{{< /spoiler >}}

Eine Kovarianzmatrix ist stets **symmetrisch** und **positiv [definit](https://de.wikipedia.org/wiki/Definitheit)** (oder positiv semidefinit).
