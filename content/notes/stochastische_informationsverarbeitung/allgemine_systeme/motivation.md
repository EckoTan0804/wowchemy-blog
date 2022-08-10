---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 501
# ============================================================

# ========== Basic metadata ==========
title: Motivation
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

Bisher: Systeme immer durch Gaußdichte repräsentiert.

Systemgleichung

{{< math >}}
$$
\underline{x}_{k+1} = \underline{a}_k (\underline{x}_k, \underline{w}_k)
$$
{{< /math >}} 

kann durch Transitionsdichte {{< math >}}$f(\underline{x}_{x+1} | \underline{x}_k)${{< /math >}} beschrieben werden.

Messgleichung

{{< math >}}
$$
\underline{y}_k = \underline{h}_k (\underline{x}_k, \underline{v}_k)
$$
{{< /math >}} 

kann durch Likelihhod {{< math >}}$f(\underline{y}_k | \underline{x}_k)${{< /math >}} beschrieben werden.

Allgemein für beide Gleichung:

{{< math >}}
$$
\underline{z} = \underline{h}(\underline{x}, \underline{v})
$$
{{< /math >}} 

Für lienare Systeme: Repräsentation durch Gaußdichte {{< math >}}$\mathcal{N}(x, \mu, \sigma)${{< /math >}} ist in Ordnung

{{< math >}}
$$
z = Hx + v
$$
{{< /math >}} 

Erwartungswert

{{< math >}}
$$
E(z | x) = Hx
$$
{{< /math >}} 

Kovarianz

{{< math >}}
$$
\operatorname{Cov}(z \mid x)=E\left(\left[z-E(z|x)\right]^{2} \mid x\right)=\sigma_{v}^{2}
$$
{{< /math >}} 

Daher

{{< math >}}
$$
\begin{aligned}
f(z \mid x) &=\mathcal{N}\left(z, H \cdot x, \sigma_{v}\right) \\\\
& \propto \exp \left(-\frac{1}{2} \frac{(z-H \cdot x)^{2}}{\sigma_{v}^{2}}\right)  \quad | \text { Gauß in } z \\\\
& \propto \exp \left\{-\frac{1}{2} \frac{\left(x-\frac{z}{H}\right)^{2}}{\left(\sigma_{v} / H\right)^{2}}\right\} \quad | \text { Gauß in } x \\\\
& = \mathcal{N}(x, \frac{z}{H}, \frac{\sigma_v}{H})
\end{aligned}
$$
{{< /math >}} 

Aber im Allgemein für 

{{< math >}}
$$
z = h(x) + v 
\tag{additives Rauschen}
$$
{{< /math >}} 

ist $f(z|x)$ NICHT Gauß in $x$!!! 

Wir benötigen eine Methode zur Berechnung von $f(z|x)$ im allgemeinen Fall. 💪