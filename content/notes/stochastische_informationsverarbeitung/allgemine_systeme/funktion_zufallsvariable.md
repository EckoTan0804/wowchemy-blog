---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 530
# ============================================================

# ========== Basic metadata ==========
title: Funktionen von Zufallsvariablen
date: 2022-07-24
draft: false
type: book # page type
authors:
  - admin
tags:
  - SI
  - Lecture Notes
  - Allgemeine Systeme
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

Abbildung

{{< math >}}
$$
y = h(x)
$$
{{< /math >}} 

- Gegeben: $x \sim f_x(x)$

- Gesucht: $y \sim f_y(y)$

Verbunddichte

{{< math >}}
$$
f_{xy}(x, y) = f(y | x) \cdot f_x(x)
$$
{{< /math >}} 

$f(y|x)$ kann als probabilistische Beschreibung der Abbildung anfassen.

Dichte von $y$

{{< math >}}
$$
f_{y}(y)=\int_{\mathbb{R}} f_{x y}(x, y) d x=\int_{\mathbb{R}} f(y \mid x) \cdot f_{x}(x) d x
$$
{{< /math >}} 

Probabilistische Abbildung:

{{< math >}}
$$
f(y|x) = \delta(y - h(x))
$$
{{< /math >}} 

Damit folgt

{{< math >}}
$$
f_y(y)=\int_{\mathbb{R}} \delta(\underbrace{y-h(x)}_{g(x)}) f_x(x) d x
$$
{{< /math >}} 

## Beispiel

### Beispiel 1

Gegeben

{{< math >}}
$$
y = \frac{1}{x} \qquad x \sim f_x(x)
$$
{{< /math >}} 

Probabilistische Abbildung:

{{< math >}}

$$
f(y|x) = \delta(\underbrace{y - \frac{1}{x}}_{=g(x)})
$$
{{< /math >}} 

{{< math >}}
$$
g(x_1) = 0 \Rightarrow x_1 = \frac{1}{y} \qquad g^\prime(x) = \frac{1}{x^2}
$$
{{< /math >}} 

Laut 

{{< math >}}
$$
\delta (g(x)) = \sum_{i=1}^N \frac{1}{|g^\prime(x_i)|}\delta (x - x_i)
$$
{{< /math >}} 

gilt

{{< math >}}
$$
f(y|x) = \delta(y - \frac{1}{x}) = x_1^2 \delta(x - \frac{1}{y}) = \frac{1}{y^2} \delta(x - \frac{1}{y})
$$
{{< /math >}} 

{{< math >}}
$$
\begin{aligned}
f_y(y) &= \int_{\mathbb{R}} f(y | x) \cdot f_{x}(x) d x \\
&= \int_{\mathbb{R}} \frac{1}{y^2} \delta(x - \frac{1}{y}) f_{x}(x) d x \\
&= \frac{1}{y^2} f_{x}(\frac{1}{y})
\end{aligned}
$$
{{< /math >}} 

Z.B., wenn $x$ gaußverteilt, also {{< math >}}$f_x(x) = e^{-x^2}${{< /math >}}, dann kann man die Dichte von $y$ sofort berechnen:

{{< math >}}
$$
f_y(y) = \frac{1}{y^2} e^{-\frac{1}{y^2}}
$$
{{< /math >}} 

### Beispiel 2: Quadratic Function

{{< math >}}
$$
\begin{aligned}
&\delta(g(x))=\delta\left(y-a x^{2}\right), \quad a>0 \\
&\Rightarrow g(x)=y-a x^{2} \\
&\Rightarrow g^{\prime}(x)=-2 a x
\end{aligned}
$$
{{< /math >}} 

Fallunterscheidung

{{< math >}}
$$
\begin{aligned}
&g\left(x_{i}\right)=0 \\
&y \geq 0: N=2, \quad x_{1}=\sqrt{\frac{y}{a}}, \quad x_{2}=-\sqrt{\frac{y}{a}} \\
&y<0: N=0, \quad \text { no roots. }
\end{aligned}
$$
{{< /math >}} 

{{< math >}}
$$
\begin{aligned}
f(y|x) &= \delta\left(y-a x^{2}\right) \\\\
&= \begin{cases}\frac{1}{\left|g^{\prime}\left(x_{1}\right)\right|} \delta\left(x-x_{1}\right)+\frac{1}{\left|g^{\prime}\left(x_{2}\right)\right|} \delta\left(x-x_{2}\right) & , y \geq 0 \\
0 & , y<0\end{cases} \\\\
&= \begin{cases}\frac{1}{2 \cdot \sqrt{a y}}\left(\delta\left(x-\sqrt{\frac{y}{a}}\right)+\delta\left(x+\sqrt{\frac{y}{a}}\right)\right) & , y \geq 0 \\
0 & , y<0\end{cases} \\\\
\end{aligned}
$$
{{< /math >}} 

{{< math >}}
$$
\begin{aligned}
f_y(y) &= \int_{\mathbb{R}} f(y | x) \cdot f_{x}(x) d x \\
&= \frac{1}{2 \sqrt{a y}}\left\{f_{x}\left(-\sqrt{\frac{y}{a}}\right)+f_x\left(\sqrt{\frac{y}{a}}\right)\right\} \cdot u(y) \qquad u(y)= \begin{cases}1, & y \geqslant 0 \\ 0, & \text { sonst }\end{cases}
\end{aligned}
$$
{{< /math >}} 

Für {{< math >}}$f_x(x) = \mathcal{N}(x, 0, \sigma)${{< /math >}}:

{{< math >}}
$$
f_{y}(y)=\frac{1}{\sqrt{2 \pi a y}} \exp \left\{-\frac{1}{2} \frac{y}{a \sigma^{2}}\right\} u(y)
$$
{{< /math >}} 