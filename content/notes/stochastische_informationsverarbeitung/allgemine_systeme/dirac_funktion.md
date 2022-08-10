---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 510
# ============================================================

# ========== Basic metadata ==========
title: Dirac’sche Deltafunktion
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

{{% callout note %}}
Mehr zu Dirac'sche Deltafunktion siehe: [Delta-Distribution]({{< relref "../math/dirac_funktion.md" >}})
{{% /callout %}}

## Eigenschaften

### Symmetrie

{{< math >}}
$$
\delta (x) = \delta (-x)
$$
{{< /math >}} 

### Skalierung

{{< math >}}
$$
\delta (ax) = \frac{1}{|a|}\delta (x)
$$
{{< /math >}} 

### Kompizierte Argumente

{{< math >}}
$$
\delta (g(x)) = \sum_{i=1}^N \frac{1}{|g^\prime(x_i)|}\delta (x - x_i)
$$
{{< /math >}} 

wobei

- $g(x_i) = 0$ (also $x_i$ sind Nullstellen, $i = 1, 2, \dots, N$)
- $g^\prime(x_i) \neq 0$

### Ableitung der Heaviside Step Funktion

{{< math >}}
$$
\delta(x) = \frac{d}{dx} H(x)
$$
{{< /math >}} 

wobei $H(x)$ ist die Heaviside Step Funktion

{{< math >}}
$$
H(x):= \begin{cases}1, & x>0 \\ 0, & x \leq 0\end{cases}
$$
{{< /math >}} 

![Dirac distribution CDF.svg](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/325px-Dirac_distribution_CDF.svg.png)