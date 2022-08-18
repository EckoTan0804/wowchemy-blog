---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 570
# ============================================================

# ========== Basic metadata ==========
title: Filterschritt für nichtlineare Systeme
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

{{% callout note %}}
Skript 10.4
{{% /callout %}}

**Rückwärtsinferenz**: Inferenz **entgegen** der modellierter Abhängigkeit mit gegebenen Vorwissen

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-27%2022.19.17.png" alt="截屏2022-07-27 22.19.17" style="zoom:50%;" />

Zwei Fälle

- [**Konkrekter Wert** für Ausgang (Messung) gegeben](#rückwärtsinferenz-mit-konkrektem-messwert)
- [**Dichte** für Ausgang gegeben](#rückwärtsinferenz-mit-dichte)

## Rückwärtsinferenz mit Konkrektem Messwert 

{{% callout note %}}
- Skript 10.4.1
- Übungsblatt Aufg. 9.2, 9.3
{{% /callout %}}

Stochastische Abbildung von $a \in \mathbb{R}^N$ auf $b \in \mathbb{R}^M$

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-05%2009.54.23.png" alt="截屏2022-08-05 09.54.23" style="zoom: 67%;" />

Probabilistischer Modell $f(b \mid a)$ (grafisch) 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-05%2009.54.37.png" alt="截屏2022-08-05 09.54.37" style="zoom:67%;" />

Für konkretes $\underline{\hat{b}}$, wir suchen $f(a \mid \underline{\hat{b}})$ 💪

{{< math >}}
$$
\begin{aligned}
&f(\underline{a} \mid \underline{\hat{b}}) f(\underline{\hat{b}})=f(\underline{\hat{b}} \mid \underline{a}) \cdot f(\underline{a}) \\
&\Rightarrow \underbrace{ f(\underline{a} \mid \underline{\hat{b}})}_{\text{Posteriror}}=\underbrace{\frac{1}{f(\underline{\hat{b}})}}_{\text{Normalizationskonstant}} \cdot \underbrace{f(\underline{\hat{b}} \mid \underline{a})}_{\text{Likelihood}} \cdot \underbrace{f(\underline{a})}_{\text{Vorwissen}}
\end{aligned}
$$
{{< /math >}} 

Für Messmodell

- Likelihood: $f(\underline{\hat{y}} \mid \underline{x})$, wobei $\underline{\hat{y}}$ die Messung ist
- $f^p(\underline{x})$: Gegebene priore Verteilung (also die Prädiktion) für Zustand

$\Rightarrow$ Posteriore Verteilung:

{{< math >}}
$$
f^e(\underline{x}) = f(\underline{x} \mid \underline{\hat{y}}) \propto f(\underline{\hat{y}} \mid \underline{x}) \cdot f^p(\underline{x})
$$
{{< /math >}} 

##  Rückwärtsinferenz mit Dichte

{{% callout note %}}
- Skript 10.4.2
- Übungsblatt Aufg. 9.4
{{% /callout %}}

Spezialfall: Additives Rauschen

{{% callout note %}}
Skript 10.4.3
{{% /callout %}}

{{< math >}}
$$
\underline{y} = \underline{g}(\underline{x}) + \underline{v} = \underline{t} + \underline{v}
$$
{{< /math >}} 

Generative Modell

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-backward_inferenz_dichte.drawio.png" alt="allg_sys-backward_inferenz_dichte.drawio" style="zoom:67%;" />

Gegeben

- Vorwissen über Zustand $\underline{x}$ in Form von $f_x(\underline{x})$
- Messung $\underline{\hat{y}}$
- Charakteristik der Messrauschen $\underline{v}$ durch $f_v(\underline{v})$

Gesucht: $f(\underline{x} \mid \underline{\hat{y}})$

Probabilistisches Modell: Faktorisierung Beschreibung der Vebundsdichte
$$
\begin{aligned}
f(\underline{t}, \underline{v}, \underline{x}, \underline{y}) &= f(\underline{y} \mid \underline{t}, \underline{v}, \underline{x}) \cdot f(\underline{t}, \underline{v}, \underline{x}) \quad | \quad \underline{y}, \underline{x} \text{ sind unab.} \\\\
&= f(\underline{y} \mid \underline{t}, \underline{v}) \cdot f(\underline{t} \mid \underline{v}, \underline{x}) \cdot f(\underline{v}, \underline{x}) \quad | \quad \underline{v}, \underline{t} \text{ sind unab.} \\\\
&= f(\underline{y} \mid \underline{t}, \underline{v}) \cdot f(\underline{t} \mid \underline{x}) \cdot f(\underline{v}, \underline{x}) \quad | \quad \underline{v}, \underline{x} \text{ sind unab.}\\\\
&= \delta(\underline{y} - \underline{t} - \underline{v}) \cdot \delta(\underline{t} - \underline{g}(\underline{x})) \cdot f_v(\underline{v}) \cdot f_x(\underline{x})
\end{aligned}
$$
Grafisches Modell

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-backward_inferenz_dichte_grafisch.png" alt="allg_sys-backward_inferenz_dichte_grafisch" style="zoom:67%;" />

**Betrachtung 1: Direkt Marginalisierung**

{{< math >}}
$$
\begin{aligned}
f(\underline{x} \mid \underline{\hat{y}}) &= \frac{f(\underline{x}, \underline{\hat{y}})}{f(\underline{\hat{y}})} \\
&= \frac{1}{f(\underline{\hat{y}})} \int_{\mathbb{R}^M} \int_{\mathbb{R}^M} f(\underline{t}, \underline{v}, \underline{x}, \underline{\hat{y}}) d\underline{v} d\underline{t} \\
&= \frac{1}{f(\underline{\hat{y}})} \int_{\mathbb{R}^M} \int_{\mathbb{R}^M} \delta(\underline{\hat{y}} - \underline{t} - \underline{v}) \cdot \delta(\underline{t} - \underline{g}(\underline{x})) \cdot f_v(\underline{v}) \cdot f_x(\underline{x}) d\underline{v} d\underline{t} \\
&= \frac{1}{f(\underline{\hat{y}})} f_x(\underline{x}) \int_{\mathbb{R}^M} \delta(\underline{t} - \underline{g}(\underline{x})) f_v(\underline{\hat{y}} - \underline{t}) d\underline{t} \\
&= \frac{1}{f(\underline{\hat{y}})} f_x(\underline{x})f_v(\underline{\hat{y}} - \underline{g}(\underline{x}))
\end{aligned}
$$
{{< /math >}} 

**Betrachtung 2: Unsicheres System und deterministische Messung**

![allg_sys-Copy of backward_inferenz_dichte_grafisch.drawio](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-Copy%20of%20backward_inferenz_dichte_grafisch.drawio.png)

Wir betrachte $f(\underline{y} \mid \underline{x})$  als ein Ersatzsystem.

{{< math >}}
$$
\begin{aligned}
f(\underline{y} \mid \underline{x}) &= \frac{1}{f_x(\underline{x})} f(\underline{x}, \underline{y}) \\\\
&= \int_{\mathbb{R}^M} \int_{\mathbb{R}^M} \delta(\underline{t} - \underline{g}(\underline{x})) \delta(\underline{\hat{y}} - \underline{t} - \underline{v}) f_v(\underline{v}) d\underline{v} d\underline{t} \\\\
&= f_v(\underline{\hat{y}} - \underline{g}(\underline{x}))
\end{aligned}
$$
{{< /math >}} 

Damit folgt für das vereinfachte System

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-backward_inferenz_dichte_grafisch_vereinfachte.drawio.png" alt="allg_sys-backward_inferenz_dichte_grafisch_vereinfachte.drawio" style="zoom:67%;" />

Gesuchte posteriore Dichte

{{< math >}}
$$
\begin{aligned}
f(\underline{x} \mid \underline{\hat{y}}) &= \frac{f(\underline{x}, \underline{\hat{y}})}{f(\underline{\hat{y}})} \\\\
&= \frac{1}{f(\underline{\hat{y}})} \cdot f(\underline{\hat{y}} \mid \underline{x}) \cdot f(\underline{x}) \\\\
&= \frac{1}{f(\underline{\hat{y}})} \cdot f_v(\underline{\hat{y}} - \underline{g}(\underline{x})) \cdot f_x(\underline{x})
\end{aligned}
$$
{{< /math >}} 

**Betrachtung 3: Deterministisches System und unsichere Messung**

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-backward_inferenz_dichte_grafisch_Betrachtung3.drawio%20%281%29.png" alt="allg_sys-backward_inferenz_dichte_grafisch_Betrachtung3.drawio (1)" style="zoom:67%;" />

{{< math >}}
$$
\begin{aligned}
f(\underline{\hat{y}} \mid \underline{t}) &= \frac{f(\underline{\hat{y}}, \underline{t})}{f(\underline{t})} \\\\
&= \frac{1}{f(\underline{t})} \int_{\mathbb{R}^M} \underbrace{f(\underline{v}, \underline{t}, \underline{\hat{y}})}_{= f(\underline{\hat{y}} \mid \underline{v}, \underline{t}) f(\underline{v}, \underline{t}) = f(\underline{\hat{y}} \mid \underline{v}, \underline{t}) f(\underline{v}) f(\underline{t})} d\underline{v} \\\\
&= \frac{1}{f(\underline{t})} f(\underline{t}) \int_{\mathbb{R}^M} f_v(\underline{v}) \delta(\underline{\hat{y}} - \underline{t} - \underline{v}) d\underline{v} \\\\
&= f_v(\underline{\hat{y}} - \underline{t})
\end{aligned}
$$
{{< /math >}} 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-backward_inferenz_dichte_grafisch_Betrachtung3_vereinfacht.drawio%20%281%29.png" alt="allg_sys-backward_inferenz_dichte_grafisch_Betrachtung3_vereinfacht.drawio (1)" style="zoom:67%;" />

Gesuchte posteriore Dichte

{{< math >}}
$$
\begin{aligned}
f(\underline{x} \mid \underline{\hat{y}}) &= \frac{f(\underline{x}, \underline{\hat{y}})}{f(\underline{\hat{y}})} \\\\
&= \frac{1}{f(\underline{\hat{y}})} \int_{\mathbb{R}^M} f(\underline{x}, \underline{t}, \underline{\hat{y}}) d\underline{t} \\\\
&= \frac{1}{f(\underline{\hat{y}})} \int_{\mathbb{R}^M} \underbrace{f(\underline{\hat{y}} \mid \underline{x}, \underline{t})}_{=f(\underline{\hat{y}} \mid \underline{t})} f(\underline{x}, \underline{t}) d\underline{t} \quad \mid \underline{x}, \underline{t} \text{ sind unab.} \\\\
&= \frac{1}{f(\underline{\hat{y}})} \int_{\mathbb{R}^M} f(\underline{\hat{y}} \mid \underline{t}) f(\underline{x}) f(\underline{t}) d\underline{t} \\\\
&= \frac{1}{f(\underline{\hat{y}})} \cdot f_v(\underline{\hat{y}} - \underline{g}(\underline{x})) \cdot f(\underline{x})

\end{aligned}
$$
{{< /math >}} 

## Schwierigkeiten Filterschritt

### Problem 1: Type der Dichte zur Beschreibung der Schätzung ändert Sicht.

Beispiel:

- Prior

  {{< math >}}
  $$
  f^p(x) \propto \exp \left[-\frac{1}{2} \frac{(x - x^p)^2}{\sigma_p^2}\right]
  $$
  {{< /math >}} 

- Messabbildung

  {{< math >}}
  $$
  y  = x^2 + v \quad v \sim f^v(v)
  $$
  {{< /math >}} 

  z.B. $f^v(v)$ ist Gauß mit zero-mean und Varianz $=1$

  {{< math >}}
  $$
  f^L(y \mid x) = f^v(y - x^2) \propto \exp \left[-\frac{1}{2} (y - x^2)^2\right]
  $$
  {{< /math >}} 

- Posteriror

  {{< math >}}
  $$
  \begin{aligned}
  f^{e}(x) & \propto f^{p}(x) \cdot f^{L}(\hat{y} \mid x)\\
  & \propto \exp \left[-\frac{1}{2}\left(\frac{x-x^{p}}{\sigma_{p}}\right)^{2}\right] \cdot \exp \left[-\frac{1}{2}\left(y-x^{2}\right)^{2}\right] \\
  & \propto \exp \left[a x^{4}+b x^{3}+c x^{2}+d x+e\right]
  \end{aligned}
  $$
  {{< /math >}} 

  ist nicht mehr Gauß!🤪



### Problem 2: Dichte wrid mit jedem Schritt komplexer

Beispiel

- Priror ist eine Mixture mit 2 Komponente

  {{< math >}}
  $$
  f^p(x) = \sum_{1}^2 f^{p, i}(x)
  $$
  {{< /math >}} 



- Messabbildung

  {{< math >}}
  $$
  y = x + v \quad v \sim f^v(v) = \sum_{j=1}^2 f^{v, j}(v)
  $$
  {{< /math >}} 

- Posterior

  {{< math >}}
  $$
  \begin{aligned}
  f(x) & \propto f^{p}(x) \cdot f^{v}(\hat{y}-x) \\
  &=\left(\sum_{i=1}^{2} f^{p, i}(x)\right) \cdot\left(\sum_{j=1}^{2} f^{v, i}(\hat{y}-x)\right) \\
  &=\sum_{i=1}^{4} f^{e_{i} i}(x)
  \end{aligned}
  $$
  {{< /math >}} 

  $\Rightarrow$ Insgesamt isit Approximation unvermeidbar! 🤪