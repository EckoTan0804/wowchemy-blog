---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 540
# ============================================================

# ========== Basic metadata ==========
title: Probabilistische Systemmodelle
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

## Mit Additivem Rauschen

Allgemein:

{{< math >}}
$$
\underline{z} = \underline{a}(\underline{x}) + \underline{v}
$$
{{< /math >}} 

$\Rightarrow$

{{< math >}}
$$
f(\underline{z} \mid \underline{x})=f_v(\underline{z}-\underline{a}(\underline{x}))
$$
{{< /math >}} 

Beispiel:

{{< math >}}
$$
z = x^2 + v \qquad v \sim f_v(v)
$$
{{< /math >}} 

Gesucht: $f(z|x)$

{{< math >}}
$$
f(z \mid x, v)=\delta\left(z-x^{2}-v\right), \quad f(z, v \mid x)=f(z \mid x, v) \cdot f_v(v)
$$
{{< /math >}} 

{{< math >}}
$$
\begin{aligned}
f(z \mid x) &\overset{\text{Marginalisierung}}{=}\int_{\mathbb{R}} f(z, v \mid x) d v\\ 
&=\int_{\mathbb{R}} f(z \mid x, v) \cdot f_v(v) d v \\
&=\int_{\mathbb{R}} \delta\left(z-x^{2}-v\right) \cdot f_v(v) d v \\
&=f_{v}\left(z-x^{2}\right)
\end{aligned}
$$
{{< /math >}} 

In dem Fall

{{< math >}}
$$
z = x_{k + 1} \quad x = x_{k},
$$
{{< /math >}} 

heißt

{{< math >}}
$$
f_v(z \mid x) = f_v(x_{k+1} \mid x_k) = f_v(x_{k+1} - a(x_k)) 
\tag{additive}
$$
{{< /math >}} 

**Transitionsdichte** (Engl. transition density). 

## Mit Multiplikativem Rauschen

Abbildung

{{< math >}}
$$
z = x \cdot v \quad v \sim \mathcal{N}(v, 0, \sigma_v)
$$
{{< /math >}} 

Annahme: $z, x, v$ sind positiv.

Gesucht: $f(z \mid x)$

Rückführung auf additiven Fall mit $\log(\cdot)$:

{{< math >}}
$$
\underbrace{\log (z)}_{\bar{z}}=\log (x \cdot v)=\underbrace{\log (x)}_{\bar{x}}+\underbrace{\log (v)}_{\bar{v}} \Leftrightarrow \bar{z}=\bar{x}+\bar{v}
$$
{{< /math >}} 

Dichte von {{< math >}}$\bar{v} = \log(v)${{< /math >}}:

{{< math >}}
$$
f(\bar{v} \mid v) = \delta(\bar{v} - \log(v)) = \exp(\bar{v})\delta(v - \exp(\bar{v}))
$$
{{< /math >}} 

{{< math >}}
$$
\begin{aligned}
f_\bar{v}(\bar{v}) &= \int_{\mathbb{R}} f(\bar{v} \mid v) f_v(v) dv \\\\
&= \int_{\mathbb{R}} \exp(\bar{v})\delta(v - \exp(\bar{v})) f_v(v) dv  \\\\
&= \exp(\bar{v}) f_v(\exp(\bar{v})) \\\\
&= \frac{1}{\sqrt{2 \pi} \sigma_{v}} \exp (\bar{v}) \exp\left\{-\frac{1}{2} \frac{[\exp(\bar{v})]^{2}}{\sigma_{v}^{2}}\right\}
\end{aligned}
$$
{{< /math >}} 

Dann

{{< math >}}
$$
\begin{aligned}
f(\bar{z} \mid \bar{x}) &= f_\bar{v}(\bar{z} - \bar{x}) \\
&= \frac{1}{\sqrt{2 \pi} \sigma_{v}} \exp \{\bar{z} - \bar{x}\} \exp\left\{-\frac{1}{2} \frac{[\exp(\bar{z} - \bar{x})]^{2}}{\sigma_{v}^{2}}\right\}
\end{aligned}
$$
{{< /math >}} 

{{< math >}}
$$
\begin{aligned}
z = \exp\{\bar{z}\} &\Rightarrow g(\bar{z}) = z - \exp(\bar{z}) \\
&\Rightarrow g^{\prime}(\bar{z})  = -\exp(\bar{z}) \quad \text{Nullstelle}: \bar{z} = \log(z)
\end{aligned}
$$
{{< /math >}} 

{{< math >}}
$$
f(z \mid \bar{x}) = \frac{1}{|z|} f(\log(z) \mid \bar{x})
$$
{{< /math >}} 

$x = \exp(\bar{x}) \Rightarrow$

{{< math >}}
$$
f(z \mid x)=\frac{1}{\sqrt{2 \pi} \sigma_{v}} \frac{1}{|x|} \exp \left\{-\frac{1}{2} \frac{z^{2}}{\sigma_{v}^{2} x^{2}}\right\}
$$
{{< /math >}} 

**Direkte Lösung:**

{{< math >}}
$$
f(z \mid x, v) = \delta(z - x \cdot v)
$$
{{< /math >}} 

{{< math >}}
$$
f(z, v \mid x) = f(z \mid x, v) \cdot f_v(v) = \delta(z - x \cdot v) f_v(v)
$$
{{< /math >}} 

{{< math >}}
$$
f(z \mid x) = \int_{\mathbb{R}} f(z, v \mid x) dv = \int_{\mathbb{R}}\delta(z - x \cdot v) f_v(v) dv
$$
{{< /math >}} 

Setze

{{< math >}}
$$
\begin{aligned}
g(v) := z - xv &\Rightarrow g^\prime(v) = -x, \quad \text{Nullstelle } v = \frac{z}{x}
\end{aligned}
$$
{{< /math >}} 

Daher

{{< math >}}
$$
\begin{aligned}
f(z \mid x)&=\int_{\mathbb{R}} \frac{1}{|x|} \delta\left(v-\frac{z}{x}\right) \cdot f_v(v) d v \\
&=\frac{1}{|x|} \cdot f_v\left(\frac{z}{x}\right) \qquad \qquad (\text{multiplicative})
\end{aligned}
$$
{{< /math >}} 

### Mixed Additive and Multiplicative Noise (Script Chp. 9.2.2)

System equation 

{{< math >}}
$$
x_{k+1} = x_k v_k + w_k
$$
{{< /math >}} 

with additive noise $w_k$ and multiplicative noise $v_k$. The noise termsare jointly distributed according to $f_{k}^{vw}(v_k, w_k)$.

The joint density of the state at time step $k+1$ is

{{< math >}}
$$
f\left(x_{k+1}, v_{k}, w_{k} \mid x_{k}\right)=f\left(x_{k+1} \mid x_{k}, v_{k}, w_{k}\right) f_{k}^{v w}\left(v_{k}, w_{k}\right),
$$
{{< /math >}} 

where according to the system equation the density of the state at time step $k + 1$ conditioned on the state at time step $k$ and the noise terms $v_k$ and $w_k$ is

{{< math >}}
$$
f(x_{k+1} \mid x_{k}, v_{k}, w_{k}) = \delta(x_{k+1} - x_{k}v_{k} - w_{k}).
$$
{{< /math >}} 

The desired transition density is now given by

{{< math >}}
$$
\begin{aligned}
f\left(x_{k+1} \mid x_{k}\right) &=\int_{\mathbb{R}} \int_{\mathbb{R}} f\left(x_{k+1}, v_{k}, w_{k} \mid x_{k}\right) d w_{k} d v_{k} \\
&=\int_{\mathbb{R}} \int_{\mathbb{R}} \delta\left(x_{k+1}-x_{k} v_{k}-w_{k}\right) f_{k}^{v w}\left(v_{k}, w_{k}\right) \mathrm{d} w_{k} \mathrm{~d} v_{k}\\
&\overset{\text{additive}}{=} f_{k}\left(x_{k+1} \mid x_{k}\right)=\int_{\mathbb{R}} f_{k}^{v w}\left(v_{k}, x_{k+1}-x_{k} v_{k}\right) \mathrm{d} v_{k} \mid v_k, w_k \text{ independent}\\
&=\int_{\mathbb{R}} f_{k}^{v}\left(v_{k}\right) f_{k}^{w}\left(x_{k+1}-x_{k} v_{k}\right) \mathrm{d} v_{k}
\end{aligned}
$$
{{< /math >}} 

These expressions cannot in general be solved analytically.