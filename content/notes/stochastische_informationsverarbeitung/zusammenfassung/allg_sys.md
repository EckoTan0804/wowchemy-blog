---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 750
# ============================================================

# ========== Basic metadata ==========
title: Allgemeine Systeme
date: 2022-08-25
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

## Generatives und probabilistisches Modell

Für Herleitung ist es super wichtig, die Eigenschaft der Dirac'schen Funktion anzuwenden:

{{< math >}}
$$
\delta (g(x)) = \sum_{i=1}^N \frac{1}{|g^\prime(x_i)|}\delta (x - x_i)
$$
{{< /math >}} 

- $g(x_i) = 0$
- $g^\prime(x_i) \neq 0$

### Mit Additivem Rauschen

Generatives Modell:

{{< math >}}
$$
z = a(x) + v \quad v \sim f_v(v)
$$
{{< /math >}} 

Probabilistisches Modell:

{{< math >}}
$$
f(z \mid x) = f_v(z - a(x))
$$
{{< /math >}} 

### Mit Multiplikativem Rauschen

Generatives Modell:

{{< math >}}
$$
z = x \cdot v \quad v \sim f_v(v)
$$
{{< /math >}} 

Probabilistisches Modell:

{{< math >}}
$$
f(z \mid x) = \frac{1}{|x|}f_v(\frac{z}{x})
$$
{{< /math >}} 

### Warum lässt sich das nur bei bestimmten Modellen exakt lösen?

"For the general generative model, where the noise enters the system in an arbitrary fashion." (Script P149)

## Abstraktion

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-27%2010.48.03.png" alt="截屏2022-08-27 10.48.03" style="zoom: 33%;" />

## Prädiktion (Vorwärtsinferenz)

{{% callout note %}}
Üb9 A2, A3
{{% /callout %}}

- Gegeben
  - $f_a(a)$
  - $g(a)$
- Gesucht: $f_b(b)$

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-Vorwaertsinferenz.drawio.png" alt="allg_sys-Vorwaertsinferenz.drawio" style="zoom: 67%;" />

### Chapman-Kolmogorov-Gleichung

{{% callout note %}}
Üb A10.1
{{% /callout %}}

{{< math >}}
$$
f_{k+1}^{p}\left(\underline{x}_{k+1}\right)=\int_{\mathbb{R}^{N}} \underbrace{f\left(\underline{x}_{k+1} \mid \underline{x}_{k}\right)}_{\text{Prädiktionsdichte}} f_{k}^{e}\left(\underline{x}_{k}\right) \mathrm{d} \underline{x}_{k}
$$
{{< /math >}} 

Herleitung ist ganz simple: Verbunddichte + Marginalisierung

{{< math >}}
$$
f\left(x_{k+1}\right)= \int_{\mathbb{R}^{N}} f\left(\underline{x}_{k+1}, \underline{x}_{k}\right) d \underline{x}_{k}= \int_{\mathbb{R}^{N}} f\left(\underline{x}_{k+1} \mid \underline{x}_{k}\right) \cdot f\left(\underline{x}_{k}\right) d \underline{x}_{k}
$$
{{< /math >}} 

‼️ <span style="color: Red">Problem: **Parameterintegral**</span>

- <span style="color: Red">Integrand hängt von $\underline{x}_{k+1}$ ab (lässt sich i.Allg nicht herausziehen)</span>
- <span style="color: Red">Erfordert Lösung des Integrals für alle $\underline{x}_{k+1}$</span>
- <span style="color: Red">Nur möglich für analytische Lösung</span>

### Prädiktionsschritte

1. Umforme $f(b \mid a) = \delta(b - g(a))$ mit

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



### Vereinfachte Prädiktion

Für 

{{< math >}}


$$
\underline{z} = \underline{a}(\underline{x}, \underline{w})
$$
{{< /math >}} 

ist die Transitionsdichte $f(\underline{z} | \underline{x})$ durch Mixture approximierbar

{{< math >}}
$$
f(\underline{z} | \underline{x}) = \sum_{i \in \mathbb{Z}} f_i^z(\underline{z}) \cdot f_i^x(\underline{x})
$$
{{< /math >}} 

## Filterung

### Rückwartsinferenz

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-Rueckwaertsinferenz.drawio.png" alt="allg_sys-Rueckwaertsinferenz.drawio" style="zoom:67%;" />

Bei Rückwartsinferenz ist es wichtig, Formel von Bayes anwuwenden.

{{< math >}}
$$
f(a \mid b) = \frac{f(a, b)}{f(b)} = \frac{f(b \mid a) f(a)}{f(b)} = \underbrace{\frac{1}{f(b)}}_{\text{Normalizationskonstant}} \cdot \underbrace{f(b \mid a)}_{\text{Likelihood}} \cdot \underbrace{f(a)}_{\text{Vorwissen}}
$$
{{< /math >}} 

### Konkrete Messung

{{% callout note %}}
Üb9 A2, A3
{{% /callout %}}

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
   f_a(a \mid b) = \frac{f_a(b \mid a) f_a(a)}{f_b(b)} = \frac{\overbrace{\delta(b - g(a))}^{\text{Schritt 1}} f_a(a)}{\underbrace{f_b(b)}_{\text{Schritt 2}}}
   $$
   {{< /math >}} 

### Unsichere Messung

{{% callout note %}}
Üb A9.4
{{% /callout %}}

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-Rueckwaertsinferenz_dichte.drawio.png" alt="allg_sys-Rueckwaertsinferenz_dichte.drawio" style="zoom:67%;" />

**Schritte**:

0. Erweitere das System um eine zusätzliche stochastische Abbildung und einen festen Ausgang $\hat{z}$

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-08 16.51.24.png" alt="截屏2022-08-08 16.51.24" style="zoom: 50%;" />

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
   f(x \mid \hat{z}) &=\frac{1}{f\left(\hat{z}\right)} \cdot f(x, z) \quad \mid \text{Marginalisierung nach } y\\
   &=\frac{1}{f(\hat{z})} \int f(x, y, z) d y \\
   &=\frac{1}{f(\hat{z})} \int f(\hat{z} \mid y, x) \cdot f(y , x) d y  \quad \mid \hat{z}, x \text{ sind unabhängig}\\
   &=\frac{1}{f(\hat{z})} \int f(\hat{z} \mid y) \cdot f(y \mid x) \cdot f(x) d y \\
   &=\frac{1}{f(\hat{z})} \int \underbrace{f(\hat{z} \mid y)}_{\text{Berechnet in Schritt 1}} \cdot \underbrace{f(y \mid x)}_{\text{Systemmodell}} \cdot f(x) d y 
   \end{aligned}
   $$
   {{< /math >}} 