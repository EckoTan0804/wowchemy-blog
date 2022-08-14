---
# ===== Title, summary, and position in the left sidebar =====
linktitle: Empirische Momente  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 610
# ============================================================

# ========== Basic metadata ==========
title: Empirische Momente von zufälligen und deterministischen Samples
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

Erzeugung von Samples

{{< math >}}
$$
y_i = m + \sigma \cdot w_i \quad w_i \in \mathcal{N}(0, 1) \quad i = 1, \dots , L
$$
{{< /math >}} 

- $w_i$: Grundsamples
- $m$: Mittelwert

Check:

{{< math >}}
$$
\begin{aligned}
&E\left\{y_{i}\right\}=E\left\{m+\sigma \cdot w_{i}\right\}=E\{m\}+\sigma \cdot E\left\{w_{i}\right\}=m \\
&E\left\{\left(y_{i}-m\right)^{2}\right\}=E\left\{\left(\sigma \cdot w_{i}\right)^{2}\right\}=\sigma^{2} E\left\{w_{i}^{2}\right\}=\sigma^{2}
\end{aligned}
$$
{{< /math >}} 

Empirische Schätzer

{{< math >}}
$$
\hat{m}=\frac{1}{L} \sum_{i=1}^{L} y_{i}
$$
{{< /math >}} 

{{< math >}}
$$
\begin{aligned}
\hat{c}=\hat{\sigma}^{2} &=\frac{1}{L} \sum_{i=1}^{L}\left(y_{i}-\hat{m}\right)^{2} \\
&=\frac{1}{L} \sum_{i=1}^{L}\left(y_{i}^{2}-2 \hat{m} y_{i}+\hat{m}^{2}\right) \\
&=\frac{1}{L} \sum_{i=1}^{L} y_{i}^{2}-\left(\frac{1}{L} \sum_{i=1}^{L} y_{i}\right)^{2} \\
&=\frac{1}{L} \sum_{i=1}^{L} y_{i}^{2}-\frac{1}{L^{2}} \sum_{i=1}^{L} \sum_{j=1}^{L} y_{i} y_{j}
\end{aligned}
$$
{{< /math >}} 

Überprüfung

- Mittelwert

  {{< math >}}
  $$
  \begin{aligned}
  E\{\hat{m}\} &=E\left\{\frac{1}{L} \sum_{i=1}^{L}\left(m+2 w_{i}\right)\right\} \\
  &=\frac{1}{L} \sum_{i=1}^{L} E\left\{m_{i}+w_{i}\right\} \\
  &=m \quad ✅
  \end{aligned}
  $$
  {{< /math >}} 

- Varianz

  {{< math >}}
  $$
  \begin{aligned}
  E\{\hat{C}\}&=E\left\{\frac{1}{L} \sum_{i=1}^{L}\left(m+\sigma w_{i}\right)^{2}-\frac{1}{L^{2}} \sum_{i=1}^{l} \sum_{j=1}^{c}\left(m_{1}+\sigma w_{i}\right)\left(m+\sigma w_{i}\right)\right\}\\
  &=\frac{1}{L} \sum_{i=1}^{L} E\left\{m^{2}+2\sigma w_{i}+\sigma^{2} w_{i}^{2}\right\}- \\
  & \qquad\frac{1}{L^{2}} \sum_{i=1}^{L} \sum_{j=1}^{L} E\left\{m^{2}+m \sigma w_{i}+m \sigma w_{j}+\sigma^{2} w_{i} w_{j}\right\}\\
  &=\frac{1}{L} \sum_{i=1}^{L}\left(m^{2}+\sigma^{2}\right)-\frac{1}{L^{2}} \sum_{i=1}^{L} \sum_{j=1}^{L}\left(m^{2}+\sigma^{2} E\left\{\omega_{i} \omega_{j}\right\}\right)\\
  &=m^{2}+\sigma^{2}-m^{2}-\frac{1}{L^{2}} \cdot L \cdot{\sigma^{2}}^{2}\\
  &=\sigma^{2}-\frac{1}{L} \sigma^{2}\\
  &=\frac{L-1}{L} \cdot \sigma^{2}
  \end{aligned}
  $$
  {{< /math >}} 





Für deterministische Samples (z.B.)

{{< math >}}
$$
\begin{aligned}
&y_{1}=m-\sigma \\
&y_{2}=m+\sigma
\end{aligned}
$$
{{< /math >}} 

{{< math >}}
$$
\begin{aligned}
\hat{m} &=\frac{1}{2}(m-\sigma+m+\sigma)=m \quad ✅ \\
\hat{z}^{2} &=\frac{1}{2}\left[(m-\sigma)^{2}+(m+\sigma)^{2}\right]-\frac{1}{4}(m-\sigma+m+\sigma)^{2} \\
&=\frac{1}{2}\left[m^{2}-2 m \sigma+\sigma^{2}+m^{2}+2 m \sigma+\sigma^{2}\right]-m^{2} \\
&=\frac{1}{2}\left[2 m^{2}+2\sigma^{2}\right]-m^{2} \\
&=\sigma^{2}
\end{aligned}
$$
{{< /math >}} 