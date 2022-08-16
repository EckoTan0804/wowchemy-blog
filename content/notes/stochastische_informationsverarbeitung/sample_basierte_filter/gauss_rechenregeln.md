---
# ===== Title, summary, and position in the left sidebar =====
linktitle: "Einschub: Gauß Rechenregeln" # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 635
# ============================================================

# ========== Basic metadata ==========
title: Gauß Rechenregeln
date: 2022-08-15
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

## Produkt zweier Gaußdichten

Gegeben

{{< math >}}
$$
\begin{aligned}
f_1(x) &= \frac{1}{\sqrt{2\pi} \sigma_1} \exp\left\{-\frac{1}{2} \frac{(x - m_1)^2}{\sigma_1^2}\right\} \\
f_2(x) &= \frac{1}{\sqrt{2\pi} \sigma_2} \exp\left\{-\frac{1}{2} \frac{(x - m_2)^2}{\sigma_2^2}\right\}
\end{aligned}
$$
{{< /math >}} 

Gesucht: 

{{< math >}}
$$
\begin{aligned}
f(x) &= \frac{1}{\sqrt{2\pi} \sigma} \exp\left\{-\frac{1}{2} \frac{(x - m)^2}{\sigma_1^2}\right\} \\\\
&\propto f_1(x) \cdot f_2(x) = \frac{1}{\sqrt{2\pi} \sigma_1}\frac{1}{\sqrt{2\pi} \sigma_2} \cdot e^{-\frac{1}{2} \frac{(x - m_1)^2}{\sigma_1^2}} e^{-\frac{1}{2} \frac{(x - m_2)^2}{\sigma_2^2}}
\end{aligned}
$$
{{< /math >}} 

Exponent:

{{< math >}}
$$
\begin{aligned}
&\frac{\left(x-m_{1}\right)^{2}}{\sigma_{1}^{2}}+\frac{\left(x-m_{2}\right)^{2}}{\sigma_{2}^{2}} \overset{!}{=} \frac{(x-m)^{2}}{\sigma^{2}}+2C \\\\
&\frac{x^{2}-2 m_{1} x+m_{1}^{2}}{\sigma_{1}^{2}}+\frac{x-2 m_{2} x+m_{2}^{2}}{\sigma_{2}{ }^{2}} \stackrel{!}{=} \frac{x^{2}-2 mx+m^{2}}{\sigma^{2}}+2 C \\\\
&x^{2}\left(\frac{1}{\sigma_{1}^{2}}+\frac{1}{\sigma_{2}^{2}}-\frac{1}{\sigma^{2}}\right)-2\left(\frac{m_{1}}{\sigma_{1}^{2}}+\frac{m_{2}}{\sigma_{2}^{2}}-\frac{m}{\sigma^{2}}\right) \cdot x +\frac{m_{1}^{2}}{\sigma_{1}^{2}}+\frac{m_{2}^{2}}{\sigma_{2}^{2}}-\frac{m^{2}}{\sigma^{2}}-2 C \stackrel{!}{=} 0
\end{aligned}
$$
{{< /math >}} 

Ergebnis:

{{< math >}}
$$
\begin{aligned}
\sigma^{2}&=\frac{1}{\frac{1}{\sigma_{1}^{2}}+\frac{1}{\sigma_{2}^{2}}}=\frac{\sigma_{1}^{2} \sigma_{2}^{2}}{\sigma_{1}^{2}+\sigma_{2}^{2}} \\\\
m &= \sigma^2 \left(\frac{m_1}{\sigma_1^2} + \frac{m_2}{\sigma_2^2} \right)\\\\
2C &= \frac{m_1^2}{\sigma_1^2} + \frac{m_2^2}{\sigma_2^2} - \frac{m^2}{\sigma^2} = \frac{(m_1 - m_2)^2}{\sigma_1^2 + \sigma_2^2}

\end{aligned}
$$
{{< /math >}} 

(See also: [Product of Two Gaussian PDFs](https://ccrma.stanford.edu/~jos/sasp/Product_Two_Gaussian_PDFs.html))

Andere Darstellung:

{{< math >}}
$$
\begin{aligned}
f(x) &\propto \frac{1}{\sqrt{2\pi} \sigma_1}\frac{1}{\sqrt{2\pi} \sigma_2} \cdot e^{-\frac{1}{2} \frac{(m_1 - m_2)^2}{\sigma_1^2 + \sigma_2^2}} e^{-\frac{1}{2} \frac{(x - m)^2}{\sigma^2}} \\\\
&= \underbrace{\frac{1}{\sqrt{2\pi} \sqrt{\sigma_1^2 + \sigma_2^2}} e^{-\frac{1}{2} \frac{(m_1 - m_2)^2}{\sigma_1^2 + \sigma_2^2}}}_{\text{Gewicht (norm.)}} \cdot \underbrace{\frac{1}{\sqrt{2\pi} \sigma} e^{-\frac{1}{2} \frac{(x - m)^2}{\sigma^2}}}_{\text{Ergebnisdichte (n orm.)}}
\end{aligned}
$$
{{< /math >}} 

## Dekomposition einer Gaußdichten

Gegeben: Gaußdichte mit $m, \sigma$

Gesucht: Dekomposition, d.h. mögliche Werte für $m_1, m_2, \sigma_1, \sigma_2$

{{< math >}}
$$
\begin{aligned}
\frac{1}{\sigma^2} &= \frac{1}{\sigma_1^2} + \frac{1}{\sigma_2^2} \\\\
\Rightarrow \kappa^2 &= \kappa_1^2 + \kappa_2^2 \\\\
\Rightarrow \kappa_1^2 &= (1 - \gamma)\kappa^2, \kappa_2^2 = \gamma \cdot \kappa^2 \qquad \gamma \in [0, 1]
\end{aligned}
$$
{{< /math >}} 

{{< math >}}
$$
m=\frac{1}{\kappa^{2}}\left((1-\gamma) \kappa^{2} \cdot m_{1}+\gamma \kappa^{2} \cdot m_{2}\right)=(1-\gamma) \cdot m_{1}+\gamma \cdot m_{2}
\tag{*}
$$
{{< /math >}} 

Gilt offennsichtlich für {{< math >}}$m_1 = m_2 = m${{< /math >}}, aber auch Wahl von $m_1, m_2$ nach $(*)$ möglich