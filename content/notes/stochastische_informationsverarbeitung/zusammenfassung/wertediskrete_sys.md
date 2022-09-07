---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 720
# ============================================================

# ========== Basic metadata ==========
title: Wertediskrete Systeme
date: 2022-08-20
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

## Wonham Filter

Zustandschätzung für wertediskrete Systeme: **Wonham Filter**

- Prädiktion

  {{< math >}}
  $$
  \underline{\xi}_{k}^{p}=\mathbf{A}^{\top} \underline{\xi}_{k-1}^{e}
  $$
  {{< /math >}} 

- Filterung

  {{< math >}}
  $$
  \underline{\xi}_{k}^{e} \overset{y_k = m}{=} \frac{\mathbf{B}(:, m) \odot \underline{\xi}_{k}^{p}}{\mathbf{B}(:, m)^\top \cdot \underline{\xi}_{k}^{p}}
  $$
  {{< /math >}} 

{{% callout note %}}

Üb 4, A2

{{% /callout %}}

Herleitung

- Prädiktion {{< math >}}$P(x_k \mid y_{0:m}, u_{0:k-1})${{< /math >}} für $k > m$

  1. nach $x_{k-1}$ marginalisieren

  2. Bayes einsetzen

     {{< math >}}
     $$
     P(a, b \mid c) = P(a \mid b, c) \cdot P(b \mid c) \qquad (\ast)
     $$
     {{< /math >}} 

  3. Markov Eigenschaft verwenden

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-22%2010.14.29.png" alt="截屏2022-08-22 10.14.29" style="zoom:67%;" />

- Filterung: {{< math >}}$P\left(x_{k} \mid y_{1: k}, u_{0: k-1}\right)${{< /math >}} 

  1. {{< math >}}$P\left(x_{k} \mid y_{1: k}, u_{0: k-1}\right) = P(x_{k} \mid y_k, y_{1: k-1},  u_{0: k-1})${{< /math >}} 

  2. Bayes einsetzen

     {{< math >}}
     $$
     P(b \mid a, c) \cdot P(a \mid c)=P(a \mid b, c) \cdot P(b \mid c) \quad (\triangle)
     $$
     {{< /math >}} 

  3. Schreibe in Form {{< math >}}$\frac{\text{Likelihood} \cdot \text{Prädiktion}}{\text{Normalisierungskonstant}}${{< /math >}} 

     {{< math >}}
     $$
     P\left(x_{k} \mid y_{1: k}, u_{0: k-1}\right) = \frac{\overbrace{P\left(y_{k} \mid x_{k}\right)}^{\text{Likelihood}} \cdot \overbrace{P\left(x_{k} \mid y_{1: k-1}, u_{0: k-1}\right)}^{\text{Einschritt-Prädiktion}}}{\underbrace{P\left(y_{k} \mid y_{1: k-1}, u_{0: k-1}\right)}_{\text{Normalisierungskonstant}}}
     $$
     {{< /math >}} 

     - Likelihood: $P\left(y_{k} \mid x_{k}\right) = \mathbf{B}(x_k, y_k)$

     - Prädiktion erhalten wir in Prädiktionsschritt

     - Normalisierungskonstant

       1. Marginalisierung nach $x_k$

       2. Bayes einsetzen

          {{< math >}}
          $$
          P(a, b \mid c) = P(a \mid b, c) \cdot P(b \mid c) \qquad (\ast)
          $$
          {{< /math >}} 

## Komplexitätsproblem bei der Diskretisierung eines allgemeinen Systems

Riesiger Speicherbedarf von Wahrscheinlichkeitsvektor und Transitionsmatrix