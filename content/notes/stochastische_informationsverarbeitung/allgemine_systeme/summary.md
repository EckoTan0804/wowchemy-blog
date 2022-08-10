---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 599
# ============================================================

# ========== Basic metadata ==========
title: Zusammenfassung
date: 2022-08-07
draft: false
type: book # page type
authors:
  - admin
tags:
  - SI
  - Lecture Notes
  - Allgemeine Systeme
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

## Vorwärtsinferenz

- Gegeben
  - $f_a(a)$
  - $g(a)$
- Gesucht: $f_b(b)$

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-Vorwärtsinferenz.drawio.png" alt="allg_sys-Vorwärtsinferenz.drawio" style="zoom:67%;" />

**Schritte**: 

1. Umforme $f(b \mid a) = \delta(b - g(a))$ () mit

   {{< math >}}
   $$
   \delta (g(x)) = \sum_{i=1}^N \frac{1}{|g^\prime(x_i)|}\delta (x - x_i)
   $$
   {{< /math >}} 

   wobei

   - $g(x_i) = 0$ (also $x_i$ sind Nullstellen, $i = 1, 2, \dots, N$)
   - $g^\prime(x_i) \neq 0$

2. Berechne $f_b(b)$ mithilfe von **Chapman-Kolmogorov-Gleichung**

   {{< math >}}
   $$
   f(b) = \int f(b \mid a) f(a) da
   $$
   {{< /math >}} 

   und setze die Unformung von $f(b \mid a)$ von Schritt 1 ein. Dann kriege die gesuchte Dichtefunktion $f_b(b)$ in Abhängigkeit von $f_a(a)$.

{{% callout note %}}
Bsp: Aufgabe 10.1
{{% /callout %}}

## Rückwartsinferenz

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-Rückwärtsinferenz.drawio%20%281%29.png" alt="allg_sys-Rückwärtsinferenz.drawio (1)" style="zoom:67%;" />

### Konkrete Messung

1. Umforme $f_b(b \mid a) = \delta(b - g(a))$ mit

   {{< math >}}
   $$
   \delta (g(x)) = \sum_{i=1}^N \frac{1}{|g^\prime(x_i)|}\delta (x - x_i)
   $$
   {{< /math >}} 

   wobei

   - $g(x_i) = 0$ (also $x_i$ sind Nullstellen, $i = 1, 2, \dots, N$)
   - $g^\prime(x_i) \neq 0$

2. Berechne $f_b(b)$

   {{< math >}}
   $$
   f_b(b) = \int f_{a, b}(a, b) da = \int f_{b}(b \mid a) f_a(a) da
   $$
   {{< /math >}} 

   mit Einsetzen der Unformung von $f(b \mid a)$ von Schritt 1 ein

3. Berechne $f_a(a \mid b)$ mithilfe von Bayes Regeln

   {{< math >}}
   $$
   f_a(a \mid b) = \frac{f_a(b \mid a) f_a(a)}{f_b(b)} = \frac{\delta(b - g(a)) f_a(a)}{f_b(b)}
   $$
   {{< /math >}} 

{{% callout note %}}
Bsp: Aufgabe 10.2, 10.3
{{% /callout %}}

### Unsichere Messung

![allg_sys-Rückwärtsinferenz_dichte.drawio](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-Rückwärtsinferenz_dichte.drawio.png)

**Schritte**:

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-08%2016.51.24.png" alt="截屏2022-08-08 16.51.24" style="zoom: 50%;" />

1. Bestimme $f(\hat{z} \mid y)$

   {{< math >}}
   $$
   \begin{aligned}
   f(\hat{z} \mid y) &= \frac{f(y \mid \hat{z})f(\hat{z})}{f(y)} \\\\
   &= \frac{f(y \mid \hat{z})f(\hat{z})}{\int f(y, x) dx} \\\\
   &= \frac{f(y \mid \hat{z})f(\hat{z})}{\int f(y|x)f(x) dx} \\\\
   &= \frac{f(y \mid \hat{z})f(\hat{z})}{\int \delta(y - g(x)) f(x) dx} \\\\
   \end{aligned}
   $$
   {{< /math >}} 

   Und setze die Umformung von $\delta(y - g(x))$ 

   {{< math >}}
   $$
   \delta (g(x)) = \sum_{i=1}^N \frac{1}{|g^\prime(x_i)|}\delta (x - x_i)
   $$
   {{< /math >}} 

   - $g(x_i) = 0$ (also $x_i$ sind Nullstellen, $i = 1, 2, \dots, N$)
   - $g^\prime(x_i) \neq 0$

   ein.

2. Berechung der Rückwärtsinferenz $f(x \mid \hat{z})$

   {{< math >}}
   $$
   \begin{aligned}
   f(x \mid \hat{z}) &=\frac{1}{f\left(\hat{z}\right)} \cdot f(x, z) \\
   &=\frac{1}{f(\hat{z})} \int f(x, y, z) d y \\
   &=\frac{1}{f(\hat{z})} \int f(\hat{z} \mid y, x) \cdot f(y , x) d y  \quad \mid \hat{z}, x \text{ sind unabhängig}\\
   &=\frac{1}{f(\hat{z})} \int f(\hat{z} \mid y) \cdot f(y \mid x) \cdot f(x) d y \\
   &=\frac{1}{f(\hat{z})} \int \underbrace{f(\hat{z} \mid y)}_{\text{Berechnet in Schritt 1}} \cdot \underbrace{f(y \mid x)}_{\text{Systemmodell}} \cdot f(x) d y 
   \end{aligned}
   $$
   {{< /math >}} 













{{% callout note %}}
Bsp: Aufgabe 10.4
{{% /callout %}}