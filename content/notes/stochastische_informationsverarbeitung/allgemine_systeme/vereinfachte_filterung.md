---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 590
# ============================================================

# ========== Basic metadata ==========
title: Vereinfachte Filterung
date: 2022-08-03
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

## Approximation der Likelihood

- Vereinfachung der Likelihood $f(\underline{y} \mid \underline{x})$

- Analog zu vereinfachter Prädiktion

  - Approximierte Repräsentation durch Gaussian Mixture
  - Wichtig: Entkoppelte Komponenten

  {{< math >}}
  $$
  f(\underline{y} \mid \underline{x}) = \sum_{i \in \mathbb{Z}} f_i^y(\underline{y}) f_i^x(\underline{x})
  $$
  {{< /math >}} 

## Resultierender vereinfachter Filterschritt

Likelihood für konkreten Messwert $\underline{\hat{y}}$:

{{< math >}}
$$
f^{L}(\underline{x})=f(\underline{\hat{y}} \mid \underline{x})=\sum_{i \in \mathbb{Z}} f_{i}^{y}(\underline{\hat{y}}) \cdot f_{i}^{x}(\underline{x})
$$
{{< /math >}} 

Priore Gaussian Mixture:

{{< math >}}
$$
f^{p}(\underline{x})=\sum_{j=1}^{L} f_{j}^{p}(\underline{x})
$$
{{< /math >}} 

$\Rightarrow$ Posterior:

{{< math >}}
$$
\begin{aligned}
f^{e}(\underline{x}) & \propto f^{p}(\underline{x}) \cdot f^{L}(\underline{x}) \\
&= \left(\sum_{i \in \mathbb{z}} f_{i}^{y}(\underline{\hat{y}})\right) \cdot \left(\sum_{j=1}^{L} f_{i}^{p}(\underline{x}) \cdot f_{i}^{k}(\underline{x})\right)
\end{aligned}
$$
{{< /math >}} 

Aber Anzahl der Komponenten nimmt zu! 🤪