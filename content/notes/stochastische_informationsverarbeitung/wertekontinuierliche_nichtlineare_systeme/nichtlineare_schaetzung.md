---
# ===== Title, summary, and position in the left sidebar =====
linktitle: "NLKF: Nichtlineare Schätzung" # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 420
# ============================================================

# ========== Basic metadata ==========
title: Nichtlineare Schätzung
date: 2022-06-30
draft: false
type: book # page type
authors:
  - admin
tags:
  - SI
  - Lecture Notes
  - Wertekontinuierliche Nichtlineare Systeme
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

## Approximation durch Linearisierung

Idea

1. Linearisierung der nichtlinear Funktion

   <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-03%2021.42.26.png" alt="截屏2022-07-03 21.42.26" style="zoom: 25%;" />

2. (Normal/Linear) Kalman Filter anwenden

### Systemmodell

{{< math >}}
$$
\underline{x}_{k+1}=\underline{a}_{k}\left(\underline{x}_{k}, \underline{u}_{k}\right)
\tag{Systemmodell}
$$
{{< /math >}} 

Linearisierung der rechten Seite von $\text{(Systemmodell)}$ mit Taylor-Entwicklung von {{< math >}}$\underline{\overline{x}}_k, \underline{\overline{u}}_k${{< /math >}}:

{{< math >}}
$$
\begin{array}{ll}
&\underline{a}_{k}\left(\underline{x}_{k}, \underline{u}_{k}\right) = \underline{a}_{k}\left(\underline{\overline{x}}_k, \underline{\overline{u}}_k\right) &+ \overbrace{\left.\frac{\partial \underline{a}_{k}\left(\underline{x}_{k}, \underline{u}_{k}\right)}{\partial \underline{x}_{k}^{\top}}\right|_{\underline{x}_{k}=\underline{\bar{x}}_{k}, \underline{u}_{k}=\underline{\bar{u}}_{k}}}^{=\mathbf{A}} \cdot \overbrace{(\underline{x}_{k} - \underline{\overline{x}}_k)}^{=\Delta \underline{x}_{k}} + \text{THO} \\\\
& & + \underbrace{\left.\frac{\partial \underline{a}_{k}\left(\underline{x}_{k}, \underline{u}_{k}\right)}{\partial \underline{u}_{k}^{\top}}\right|_{\underline{x}_{k}=\underline{\bar{x}}_{k}, \underline{u}_{k}=\overline{\underline{\bar{u}}}_{k}}}_{=\mathbf{B}} \cdot (\underline{u}_{k} - \underline{\overline{u}}_k) + \text{THO}

\end{array}
$$
{{< /math >}} 

- $\text{THO}$: Terme höherer Ordnung

- Jacobi-Matrizen

  {{< math >}}
  $$
  \begin{array}{l}
  \mathbf{A}_{k}=\left[\begin{array}{ccc}
  \frac{\partial a_{k, 1}}{\partial x_{k, 1}} & \cdots & \frac{\partial a_{k, 1}}{\partial x_{k, N}} \\
  \vdots & & \vdots \\
  \frac{\partial a_{k, N}}{\partial x_{k, 1}} & \cdots & \frac{\partial a_{k, N}}{\partial x_{k, N}}
  \end{array}\right]_{\underline{x}_{k}=\overline{\underline{x}}_{k}, \underline{u}_{k}= \bar{\underline{u}}_{k}} \\\\
  \mathbf{B}_{k}=\left[\begin{array}{ccc}
  \frac{\partial a_{k, 1}}{\partial u_{k, 1}} & \cdots & \frac{\partial a_{k, 1}}{\partial u_{k, N}} \\
  \vdots & & \vdots \\
  \frac{\partial a_{k, N}}{\partial u_{k, 1}} & \cdots & \frac{\partial a_{k, N}}{\partial u_{k, N}}
  \end{array}\right]_{\underline{x}_{k}=\overline{\underline{x}}_{k}, \underline{u}_{k}= \bar{\underline{u}}_{k}}
  \end{array}
  $$
  {{< /math >}} 

Annahme

- Ableitung existiert
- {{< math >}}$\underline{a}_k(\cdot, \cdot)${{< /math >}} ausreichend linear um {{< math >}}$\underline{\overline{x}}_k, \underline{\overline{u}}_k${{< /math >}}

Vernachlässigen von $\text{THO} \Rightarrow$

{{< math >}}
$$
\underline{a}_{k}\left(\underline{x}_{k}, \underline{u}_{k}\right) \approx \underline{a}_{k}\left(\underline{\overline{x}}_k, \underline{\overline{u}}_k\right)+\mathbf{A}_{k}\left(\underline{x}_k-\underline{\overline{x}}_k\right)+\mathbf{B}_{k}\left(\underline{u}_{k}-\underline{\overline{u}}_k\right)
$$
{{< /math >}} 

Für die linke Seite von $(\text{Systemmodell})$:

{{< math >}}
$$
\underline{x}_{k+1}= \underline{\overline{x}}_{k+1} + \Delta \underline{x}_{k+1}
$$
{{< /math >}} 

Für {{< math >}}$\underline{u}_{k}${{< /math >}} definiere man

{{< math >}}
$$
\underline{u}_{k}:=\underline{\hat{u}}_{k}+\underline{w}_{k}
$$
{{< /math >}} 

mit {{< math >}}$E\left\{\underline{w}_{k}\right\}=0, \operatorname{Cov}\left\{\underline{w}_{k}\right\}=\mathbf{C}_{k}^{w}${{< /math >}} 

- Lineariesierung: {{< math >}}$\overline{\underline{u}}_{k} \overset{!}{=} \hat{\underline{u}}_{k} \Rightarrow \Delta \underline{u}_{k}= \underline{u}_{k} -\overline{\underline{u}}_{k} = \underline{w}_{k}${{< /math >}} (d.h. die Abweichung {{< math >}}$\underline{w}_k${{< /math >}} ist ein Rauschen)

- Äquivalentes Rauschen

  {{< math >}}
  $$
  w_{k}^{\prime}=\mathbf{B}_{k} \cdot w_{k} \Rightarrow E\left\{w_{k}^{\prime}\right\}=0, \operatorname{Cov}\left\{w_{k}^{\prime}\right\}=\mathbf{B}_{k} \cdot \mathbf{C}_{k}^{w} \cdot \mathbf{B}_{k}^{\top}
  $$
  {{< /math >}} 

Durch obige Linearisierung der beiden Seiten kann man das Systemmodell so schreiben:

{{< math >}}
$$
\underline{\overline{x}}_{k+1} + \Delta \underline{x}_{k+1} \approx \underline{a}_{k}\left(\underline{\overline{x}}_k, \underline{\overline{u}}_k\right)+\mathbf{A}_{k}\Delta \underline{x}_k+\underline{w}_k^\prime
$$
{{< /math >}} 

- Nominalteil

  {{< math >}}
  $$
  \underline{\overline{x}}_{k+1} = \underline{a}_{k}\left(\underline{\overline{x}}_k, \underline{\overline{u}}_k\right)
  $$
  {{< /math >}} 

- Differentialteil

  {{< math >}}
  $$
  \Delta \underline{x}_{k+1} \approx \mathbf{A}_{k}\Delta \underline{x}_k+\underline{w}_k^\prime
  $$
  {{< /math >}} 

### Messgleichung

{{< math >}}
$$
\underline{y}_{k}=\underline{h}_{k}\left(\underline{x}_{k}, \underline{v}_{k}\right)
\tag{Messgleichung}
$$
{{< /math >}} 

Linearisierung der rechten Seite um {{< math >}}$\underline{\bar{x}}_{k}, \underline{\bar{v}}_{k}${{< /math >}}:

{{< math >}}
$$
\underline{h}_{k}\left(\underline{x}_{k}, \underline{v}_{k}\right) \approx \underline{h}_{k}\left(\underline{\bar{x}}_{k}, \underline{\bar{v}}_{k}\right)+\mathbf{H}_{k} \cdot \underbrace{\left(\underline{x}_{k}-\underline{\bar{x}}_{k}\right)}_{=\Delta \underline{x}_k}+\mathbf{L}_{k} \cdot\left(\underline{v}_{k}-\underline{\bar{v}}_{k}\right)
$$
{{< /math >}} 

mit Jacobi-Matrizen

{{< math >}}
$$
\mathbf{H}_{k}=\left.\frac{\partial \underline{h}_{k}\left(\underline{x}_{k}, \underline{v}_{k}\right)}{\partial \underline{x}_{k}^{\top}}\right|_{\underline{x}_{k}=\underline{x}_{k}, \underline{v}_{k}=\underline{\bar{v}}_{k}} \qquad
\mathbf{L}_{k}=\left.\frac{\partial \underline{h}_{k}\left(\underline{x}_{k}, \underline{v}_{k}\right)}{\partial \underline{v}_{k}^{\top}}\right|_{\underline{x}_{k}=\underline{x}_{k}, \underline{v}_{k}=\underline{\bar{v}}_{k}}
$$
{{< /math >}} 

Sei {{< math >}}$\underline{\bar{v}}_{k} = \underline{\hat{v}}_{k}${{< /math >}} für [mittelwertfreies](https://de.wikipedia.org/wiki/Mittelwertfreiheit) {{< math >}}$\underline{v}_{k} \Rightarrow \underline{\hat{v}}_{k} = \underline{0}${{< /math >}} 

Das Effektive Rauschen ist dann

{{< math >}}
$$
\underline{v}_{k}^\prime = \mathbf{L}_{k} \cdot \underline{v}_{k}
$$
{{< /math >}} 

mit 

{{< math >}}
$$
E\left\{\underline{v}_{k}^{\prime}\right\}=\underline{0}, \quad \operatorname{Cov}\left\{\underline{v}_{k}^{\prime}\right\}=\mathbf{L}_{k} \cdot \mathbf{C}_{k}^{v} \cdot \mathbf{L}_{k}^{\top}
$$
{{< /math >}} 

Damit kann man die Messgliechung so umschreiben:

{{< math >}}
$$
\underline{y}_{k}=\underline{\bar{y}}_{k}+\Delta \underline{y}_{k} \approx \underline{h}_{k}\left(\underline{\bar{x}}_{k}, \underline{\bar{v}}_{k}\right)+\mathbf{H}_{k} \Delta \underline{x}_{k}+\underline{v}_{k}^{\prime}
$$
{{< /math >}} 

- Nominalteil

  {{< math >}}
  $$
  \underline{\bar{y}}_{k} = \underline{h}_{k}\left(\underline{\bar{x}}_{k}, \underline{\bar{v}}_{k}\right)
  $$
  {{< /math >}} 

- Differentialteil

  {{< math >}}
  $$
  \Delta \underline{y}_{k} \approx \mathbf{H}_{k} \Delta \underline{x}_{k}+\underline{v}_{k}^{\prime}
  $$
  {{< /math >}} 

### Erweitertes Kalmanfilter (EKF)

💡Linearisierung um jeweils beste Schätzung

- Prädiktion

  - Berechnung Erwartungswert über nichtlineare Funktion

    {{< math >}}
    $$
    \underline{\hat{x}}_{k}^{p}=\underline{a}_{k}\left(\underline{\hat{x}}_{k-1}^{e}, \hat{\underline{u}}_{k}\right)
    $$
    {{< /math >}} 

  - Berechnung Kovarianzmatrix über die Linearisierung

    {{< math >}}
    $$
    \mathbf{C}_{k}^{p} \approx \mathbf{A}_{k} \mathbf{C}_{k}^{e} \mathbf{A}_{k}^{\top}+\mathbf{C}_{k}^{w^{\prime}}=\mathbf{A}_{k} \mathbf{C}_{k}^{e} \mathbf{A}_{k}^{\top}+\mathbf{B}_{k}  \mathbf{C}_{k}^{w} \mathbf{B}_{k}^{\top}
    $$
    {{< /math >}} 
    
    mit 
    
    {{< math >}}
    $$
    \mathbf{A}_k = \left.\frac{\partial \underline{a}_{k}\left(\underline{x}_{k}, \underline{u}_{k}\right)}{\partial \underline{x}_{k}^{\top}}\right|_{\underline{x}_{k}=\underline{\hat{x}}_{k-1}^{e}, \underline{u}_{k}=\hat{\underline{u}}_{k}} \qquad
    \mathbf{B}_k = \left.\frac{\partial \underline{a}_{k}\left(\underline{x}_{k}, \underline{u}_{k}\right)}{\partial \underline{u}_{k}^{\top}}\right|_{\underline{x}_{k}=\underline{\hat{x}}_{k-1}^{e}, \underline{u}_{k}=\hat{\underline{u}}_{k}}
    $$
    {{< /math >}} 

- Filterung

  - Berechnung von {{< math >}}$\underline{\bar{y}}_k${{< /math >}} (Messung, die aus dem prioren Schätzwert (also die Prädiktion) bekomme, als Nominalwert zum jetztigen Zeitpunkt)

    {{< math >}}
    $$
    \underline{\bar{y}}_k = \underline{h}_k(\underline{\bar{x}}_k^p, \underline{\hat{v}}_k)
    $$
    {{< /math >}} 

  - Berechnung von {{< math >}}$\Delta \underline{y}_k${{< /math >}} 

    {{< math >}}
    $$
    \Delta \underline{y}_{k}=\underline{\hat{y}}_{k}-\underline{\bar{y}}_{k}
    $$
    {{< /math >}} 

    - {{< math >}}$\underline{\hat{y}}_{k}${{< /math >}}: wahre Messung

    und 

    {{< math >}}
    $$
    \Delta \underline{y}_{k} \approx \mathbf{H}_{k} \cdot\left(\underline{x}_{k}^{e}-\hat{x}_{k}^{p}\right)+\underline{v}_{k}^{\prime}
    $$
    {{< /math >}} 
    
    mit 
    
    {{< math >}}
    $$
    \mathbf{H}_{k}=\left.\frac{\partial \underline{h}_{k}\left(\underline{x}_{k}, \underline{v}_{k}\right)}{\partial \underline{x}_{k}^{\top}}\right|_{\underline{x}_{k}=\underline{\hat{x}}_{k}^{p}, \underline{v}_{k}=\underline{\hat{v}}_{k}} \qquad
    \mathbf{L}_{k}=\left.\frac{\partial \underline{h}_{k}\left(\underline{x}_{k}, \underline{v}_{k}\right)}{\partial \underline{v}_{k}^{\top}}\right|_{\underline{x}_{k}=\underline{\hat{x}}_{k}^{p}, \underline{v}_{k}=\underline{\hat{v}}_{k}}
    $$
    {{< /math >}}  
  
  Filterung Schritt
  
  {{< math >}}
  $$
  \begin{aligned}
  \mathbf{K}_{k}&=\mathbf{C}_{k}^{p} \mathbf{H}_{k}^{\top}\left(\mathbf{L}_{k} \mathbf{C}_{k}^{v} \mathbf{L}_{k}^{\top}+\mathbf{H}_{k} \mathbf{C}_{k}^{p} \mathbf{H}_{k}^{T}\right)^{-1} \\\\
  
  \hat{\underline{x}}_{k}^{e}&=\hat{\underline{x}}_{k}^{p}-\mathbf{K}_{k}\left[\hat{\underline{y}}_{k}-\underline{h}_{k}\left(\hat{\underline{x}}_{k}^{p}, \hat{\underline{v}}_{k}\right)\right] \\\\
  
  \mathbf{C}_{k}^{e}&=\mathbf{C}_{k}^{p}-\mathbf{K}_{k} \mathbf{H}_{k} \mathbf{C}_{k}^{p} = (\mathbf{I} - \mathbf{K}_{k} \mathbf{H}_{k})\mathbf{C}_{k}^{p}
  \end{aligned}
  $$
  {{< /math >}} 

### Probleme bei Linearisierung

- Berechnung der posterirre Verteilung nur gut für "schwache" Nichtlinearität

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-03%2021.42.26.png" alt="截屏2022-07-03 21.42.26" style="zoom: 25%;" />

- Linearisierung nur um einen Punkt

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-03%2021.43.45.png" alt="截屏2022-07-03 21.43.45" style="zoom: 20%;" />

- Linearisiertes System ist i.A. zeitvariant, auch wenn originalsytstem zeitinvariant ist, da Linearisierung vom Schätzwert abhängt.



## Schätzung in probabilistischer Form: Nichtlineares Kalmanfilter 

### Erwartungswertbildung

Gegeben:

- Funktion {{< math >}}$\underline{y}=\underline{g}(\underline{x})${{< /math >}} 
- {{< math >}}$\underline{x} \sim f_x(x)${{< /math >}} 

Gesucht: Bestimmte Momente von {{< math >}}$\underline{y}${{< /math >}} 

Z.B. für skalares Fall 

{{< math >}}
$$
y = g(x)
$$
{{< /math >}} 

suchen wir {{< math >}}$E\left\{y^{j}\right\}, j \in \mathbb{N}${{< /math >}}.

Wir wissen

{{< math >}}
$$
E\left\{y^{i}\right\}=\int_{\mathbb{R}} y^{j} f_{y}(y) d y
$$
{{< /math >}} 

Aber

- {{< math >}}$f_y(y)${{< /math >}}, posteriore Dichte, ist oft nicht einfach berechbar
- Falls berechbar, die Berechnung von {{< math >}}$f_y(y)${{< /math >}} is viel zu aufwändig, wenn nur Momente benötigt werden

{{% callout note %}}

Theorem (Dualität bei Erwartungswertbildung)

{{< math >}}
$$
E\_{f\_y}\left\\{y^{j}\right\\}=E\_{f\_{x}}\left\\{[g(x)]^{j}\right\\}=\int\_{\mathbb{R}}[g(x)]^{j} f\_{x}(x) d x
$$
{{< /math >}} 
{{% /callout %}}

- {{< math >}}$f_y(y)${{< /math >}} muss also nicht berechnet werden.
- Nützlich, wenn
  - {{< math >}}$f_y(y)${{< /math >}} schwer zu berechnen
  - 1-order nichtlineare Momente von {{< math >}}$f_x(\cdot)${{< /math >}} einfach berechenbar

Für sample-basierte Approximation der prioren Dichte {{< math >}}$f_x(x)${{< /math >}}

{{< math >}}
$$
f_{x}(x)=\sum_{i=1}^{L} w_{i} \delta\left(x-x_{i}\right)
$$
{{< /math >}} 

ist berechnung der posterioren Dichte {{< math >}}$f_y(y)${{< /math >}} trivial.

{{< math >}}
$$
f_y(y)=\sum_{i=1}^{L} w_{i} \delta\left(y-y_{i}\right), \quad y_{i}=g\left(x_{i}\right)
$$
{{< /math >}} 

Damit

{{< math >}}
$$
E\left\{y^{j}\right\}=\int_{\mathbb{R}} y^{j} f_{y}(y) d y=\sum_{i=1}^{L} w_{i} y_{i}^{j}=\sum_{i=1}^{L} w_{i}\left[g\left(x_{i}\right)\right]^{j}
$$
{{< /math >}} 

und 

{{< math >}}
$$
E\left\{[g(x)]^{j}\right\}=\int_{\mathbb{R}}[g(x)]^{j} f_{x}(x) d x=\sum_{i=1}^{L} w_{i}\left[g\left(x_{i}\right)\right]^{j}
$$
{{< /math >}} 

Die Berechnungen sind in diesem Fall identisch, aber im allgemeinem Fall gilt dies NICHT! 🤪

### Prädiktion in probabilistischer Form

Systemmodell

{{< math >}}
$$
x_{k+1}=\underline{a}_{k}\left(\underline{x}_{k}, \underline{u}_{k}\right)
$$
{{< /math >}} 

- {{< math >}}$\underline{x}${{< /math >}}: Zustand
- {{< math >}}$\underline{u}${{< /math >}}: Störgröße

Für einen Kalman Filter, wir möchte in nächsten Schritt die Erwartungswert und die Kovarianzmatrix haben.

Erwartungswert 

{{< math >}}
$$
\hat{x}_{k+1}^{p}=E\left\{\underline{a}_{n}\left(\underline{x}_{k}, \underline{u}_{k}\right)\right\}=\int_{\mathbb{R}^{N}} \int_{\mathbb{R}^{p}} \underline{a}_{k}\left(\underline{x}_{k}, \underline{u}_{k}\right) f_{k}^{x u}\left(\underline{x}_{k}, \underline{u}_{k}\right) d\underline{x}_{k} d\underline{u}_{k}
$$
{{< /math >}} 

In der Regel sind {{< math >}}$\underline{x}_{k}, \underline{u}_{k}${{< /math >}} unabhängig. Also

{{< math >}}
$$
f_{k}^{x u}\left(\underline{x}_{k}, \underline{u}_{k}\right) = f_{k}^{e}\left(\underline{x}_{k}\right) \cdot f_{k}^{u}\left(\underline{u}_{k}\right).
$$
{{< /math >}} 

Und nehme an, dass {{< math >}}$\underline{x}_{k}, \underline{u}_{k}${{< /math >}} normalverteilt sind, also

{{< math >}}
$$
\begin{aligned}
f_{k}^{e}\left(\underline{x}_{u}\right) &= \mathcal{N}(\underline{x}_{k}, \hat{x}_{k}^{e}, \mathbf{C}_{k}^{e}) \\\\
f_{k}^{u}\left(\underline{u}_{k}\right) &= \mathcal{N}\left(\underline{u}_{k}, \hat{\underline{u}}_{k}, \mathbf{C}_{k}^{w}\right)
\end{aligned}
$$
{{< /math >}} 

Für additives Rauschen 

{{< math >}}
$$
\underline{x}_{k+1}=\underline{a}_{k}\left(\underline{x}_{k}\right)+\underline{u}_{k} \left(= \underline{a}_{k}\left(\underline{x}_{k}\right)+(\underline{\hat{u}}_{k} + \underline{w}_k)\right)
$$
{{< /math >}} 

gilt

{{< math >}}
$$
\underline{\hat{x}}_{k+1}^{p}=\int_{\mathbb{R}^{n}} \underline{a}_{k}\left(\underline{x}_{k}\right) \cdot f_{k}^{e}\left(\underline{x}_{k}\right) d \underline{x}_{k}+\underline{\hat{u}}_{k}
$$
{{< /math >}} 

Dann ist 

{{< math >}}
$$
\begin{aligned}
\underline{x}_{k+1} - \underline{\hat{x}}_{k+1}^{p} &= (\underline{a}_{k}(\underline{x}_{k})+(\underline{\hat{u}}_{k} + \underline{w}_k)) - \left(\int_{\mathbb{R}^{n}} \underline{a}_{k}\left(\underline{x}_{k}\right) \cdot f_{k}^{e}\left(\underline{x}_{k}\right) d \underline{x}_{k}+\underline{\hat{u}}_{k}\right) \\\\
&= \underbrace{\underline{a}_{k}(\underline{x}_{k}) - \int_{\mathbb{R}^{n}} \underline{a}_{k}\left(\underline{x}_{k}\right) \cdot f_{k}^{e}\left(\underline{x}_{k}\right) d \underline{x}_{k}}_{:= \underline{\bar{a}}_{k}(\underline{x}_{k})} + \underline{w}_k
\end{aligned}
$$
{{< /math >}} 

Die Kovarianzmatrix ist

{{< math >}}
$$
\begin{aligned}
\mathbf{C}_{k+1}^{p} &= E\left\{\left(\underline{x}_{k+1}-\underline{\hat{x}}_{k+1}^{p}\right)(\underline{x}_{k+1}-\underline{\hat{x}}_{k+1}^{p})^{\top}\right\} \\\\
&= E\left\{(\underline{\bar{a}}_{k}(\underline{x}_{k}) + \underline{w}_k) (\underline{\bar{a}}_{k}(\underline{x}_{k}) + \underline{w}_k) ^ \top\right\} \\\\
&= E\left\{\underline{\bar{a}}_{k}(\underline{x}_k) \underline{\bar{a}}_{k}^\top(\underline{x}_k) + \underline{w}_k\underline{\bar{a}}_{k}(\underline{x}_k) + \underline{\bar{a}}_{k}(\underline{x}_k)\underline{w}_k^\top + \underline{w}_k\underline{w}_k^\top\right\} \\\\
&= E\left\{\underline{\bar{a}}_{k}(\underline{x}_k) \underline{\bar{a}}_{k}^\top(\underline{x}_k)\right\} + \underbrace{E\left\{\underline{w}_k\underline{\bar{a}}_{k}(\underline{x}_k)\right\}}_{=0} + \underbrace{E\left\{\underline{\bar{a}}_{k}(\underline{x}_k)\underline{w}_k^\top\right\}}_{=0} + E\left\{\underline{w}_k\underline{w}_k^\top\right\} \\\\
&= E\left\{\underline{\bar{a}}_{k}(\underline{x}_k) \underline{\bar{a}}_{k}^\top(\underline{x}_k)\right\} +  E\left\{\underline{w}_k\underline{w}_k^\top\right\} \\\\
&= \int_{\mathbb{R}^{N}} \overline{\underline{a}}_{k}\left(\underline{x}_{k}\right) \overline{\underline{a}}_{k}^{\top}\left(x_{k}\right) f_{k}^{e}\left(\underline{x}_{k}\right) d \underline{x}_{k}+\mathbf{C}_{k}^{w}
\end{aligned}
$$
{{< /math >}} 

### Filterung in probabilistischer Form

#### Einschub: Konditionierung einer Gaußschen Verbunddichte

Zufallsvektor {{< math >}}$\underline{z}=\left[\begin{array}{l}\underline{x} \\ \underline{y}\end{array}\right]${{< /math >}} mit Gaußcher Verbundverteilung:

{{< math >}}
$$
f(\underline{z})=\mathcal{N}\left(\underline{z}_{1}, \underline{\hat{z}}, \mathbf{C}_{z}\right), \quad \underline{\hat{z}}=\left[\begin{array}{l}
\underline{\hat{x}} \\
\underline{\hat{y}}
\end{array}\right], \quad \mathbf{C}_{z}=\left[\begin{array}{ll}
C_{x x} & C_{x y} \\
C_{y x} & C_{y y}
\end{array}\right]
$$
{{< /math >}} 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/wertkontinuierliche_nichtlineare_system-Konditionierung_gauss_verbunddichte.drawio.png" alt="wertkontinuierliche_nichtlineare_system-Konditionierung_gauss_verbunddichte.drawio" style="zoom:67%;" />

Gegeben: Messung {{< math >}}$y^\ast${{< /math >}}

Konditionale Verteilung:

{{< math >}}
$$
\begin{equation}
f\left(\underline{x} \mid \underline{y}^{\ast}\right)= \mathcal{N}\left(\underline{x}, \underline{\hat{x}}^{*}, \mathbf{C}_{x}^{\ast}\right)
\end{equation}
$$
{{< /math >}} 

Dann ist

{{< math >}}
$$
\begin{array}{l}
\underline{\hat{x}}^{\ast}=\underline{\hat{x}}+C_{x y} C_{y y}^{-1}\left(\underline{y}^{*}-\underline{\hat{y}}\right) \\
\mathbf{C}_{x}^{\ast}=C_{x x}-C_{x y} C_{y y}^{-1} C_{y x}
\end{array}
\tag{*}
$$
{{< /math >}} 

#### Alternative Herleitung Kalmanfilter

Messmodell

{{< math >}}
$$
\underline{y}=\mathbf{H} \cdot \underline{x}+\underline{v}
$$
{{< /math >}} 

Gegeben:

{{< math >}}
$$
\underline{x}_{p} \sim \mathcal{N}\left(\hat{\underline{x}}_{p}, \mathbf{C}_{p}\right), \quad \underline{v}\sim \mathcal{N}\left(\underline{0}, \mathbf{C}_{v}\right)
$$
{{< /math >}} 

Wir definiere {{< math >}}$\underline{z}${{< /math >}} als Verbund von {{< math >}}$\underline{x}_{p}${{< /math >}} und {{< math >}}$\underline{y}${{< /math >}}

{{< math >}}
$$
\underline{z}:=\left[\begin{array}{l}
\underline{x}_{p} \\
\underline{y}
\end{array}\right]=\left[\begin{array}{l}
\underline{x}_{p} \\
\mathbf{H} \cdot \underline{x}_{p}+\underline{v}
\end{array}\right]=\left[\begin{array}{ll}
\mathbf{I} & 0 \\
\mathbf{H} & \mathbf{I}
\end{array}\right]\left[\begin{array}{c}
\underline{x}_{p} \\
\underline{v}
\end{array}\right]
$$
{{< /math >}} 

Die Erwartungswert ist dann

{{< math >}}
$$
\underline{\hat{z}}=\left[\begin{array}{c}
\hat{x}_{p} \\
\mathbf{H} \cdot \hat{x}_{p}
\end{array}\right]
$$
{{< /math >}} 

Die Kovairanzmatrix von {{< math >}}$\underline{z}${{< /math >}} :

{{< math >}}
$$
\begin{array}{l}
\operatorname{Cov}\{\underline{z}\}&=E\left\{\left[\begin{array}{ll}
\mathbf{I} & 0 \\
\mathbf{H} & \mathbf{I}
\end{array}\right]\left[\begin{array}{c}
\underline{x}_{p}-\hat{\underline{x}}_{p} \\
\underline{v}
\end{array}\right]\left[\begin{array}{c}
\underline{x}_{p}-\underline{\hat{x}}_{p} \\
\underline{v}
\end{array}\right]^{\top}\left[\begin{array}{cc}
\mathbf{I} & \mathbf{H}^{\top} \\
0 & \mathbf{I}
\end{array}\right]\right\}\\\\
&=\left[\begin{array}{ll}
\mathbf{I} & 0 \\
\mathbf{H} & \mathbf{I}
\end{array}\right] E\left\{\left[\begin{array}{cc}
\underbrace{\left(\underline{x}_{p}-\underline{\hat{x}}_{p}\right)(\underline{x}_{p}-\underline{\hat{x}}_{p})^{\top}}_{=\mathbf{C}_p} & \underbrace{\left(\underline{x}_{p}-\underline{\hat{x}}_{p}\right) \underline{v}^{\top}}_{=0} \\
\underbrace{\underline{v}\left(\underline{x}_{p}-\underline{\hat{x}}_{p}\right)}_{=0} & \underbrace{\underline{v} \underline{v}^{\top}}_{=\mathbf{C}_v} 
\end{array}\right]\right\}\left[\begin{array}{cc}
\mathbf{I} & 0 \\
\mathbf{H} & \mathbf{I}
\end{array}\right]\\\\
&=\left[\begin{array}{ll}
\mathbf{I} & 0 \\
\mathbf{H} & \mathbf{I}
\end{array}\right]\left[\begin{array}{cc}
\mathbf{C}_p & 0 \\
0 & \mathbf{C}_v
\end{array}\right]\left[\begin{array}{cc}
\mathbf{I} & 0 \\
\mathbf{H} & \mathbf{I}
\end{array}\right]=\left[\begin{array}{cc}
\mathbf{C}_{p} & \mathbf{C}_{p} \mathbf{H}^{\top} \\
\mathbf{H}  \mathbf{C}_{p} & \mathbf{C}_{v}+\mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top}
\end{array}\right]
\end{array}
$$
{{< /math >}} 

Lasse

{{< math >}}
$$
\mathbf{C}_{x x}=\mathbf{C}_{p} \quad \mathbf{C}_{x y}=\mathbf{C}_{p} \mathbf{H}^{\top} \quad \mathbf{C}_{y x}=\mathbf{H} \mathbf{C}_{p} \quad \mathbf{C}_{y y}=\mathbf{C}_{v}+\mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top}
$$
{{< /math >}} 

und in $(*)$ einsetzen, ergibt sich der Kalman Filter.

#### Filterung in probabilistischer Form

Messgleichung

{{< math >}}
$$
\underline{y}=\underline{h}(\underline{x}, \underline{v})
$$
{{< /math >}} 

Definiere

{{< math >}}
$$
\underline{z}=\left[\begin{array}{l}
\underline{x} \\
\underline{y}
\end{array}\right]=\left[\begin{array}{c}
\underline{x} \\
\underline{h}(\underline{x}, \underline{v})
\end{array}\right] \Rightarrow E\{\underline{z}\}=\left[\begin{array}{c}
\underline{\hat{x}}_{p} \\
E\{\underline{h}(\underline{x}, \underline{v})\}
\end{array}\right]
$$
{{< /math >}} 

Bei additivem Rauschen 

{{< math >}}
$$
y=\underline{h}(\underline{x})+\underline{v}
$$
{{< /math >}} 

gilt

{{< math >}}
$$
E\{\underline{z}\}=\left[\begin{array}{c}
\underline{\hat{x}}_{p} \\
E\{\underline{h}(x)\}
\end{array}\right], \quad E\{\underline{h}(x)\}=\int_{\mathbb{R}^{N}} \underline{h}(x) \underbrace{f_{p}(x)}_{= \mathcal{N}(\underline{x}, \underline{\hat{x}}_{p}, \mathbf{C}_p)} d \underline{x} \in \mathbb{R}^{M}
$$
{{< /math >}} 

Kovarianzmatrix:

![image-20220711122807030](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/image-20220711122807030.png)

{{< math >}}
$$
E\left\{\left(\underline{x}-\underline{\hat{x}}_{p}\right)\right\} \underline{\bar{h}}^{\top}(\underline{x}) = \int_{\mathbb{R}^N} (\underline{x}-\underline{\hat{x}}_{p}) \underline{\bar{h}}^{\top} f_p(\underline{x}) d\underline{x} \in \mathbb{R}^{N \times M}
$$
{{< /math >}} 

{{< math >}}
$$
E\left\{\underline{\bar{h}}(x) \underline{\bar{h}}^{\top}(\underline{x})\right\} = \int_{\mathbb{R}^N} \underline{\bar{h}}(x) \underline{\bar{h}}^{\top}(\underline{x}) f_p(\underline{x}) d\underline{x} \in \mathbb{R}^{M \times M}
$$
{{< /math >}} 

{{< math >}}
$$
\operatorname{Cov}\{\underline{z}\}=\left[\begin{array}{ll}
\overbrace{C_{x x}}^{\mathbb{R}^{N \times N}} & \overbrace{C_{x y}}^{\mathbb{R}^{N \times M}}\\
\underbrace{C_{y x}}_{\mathbb{R}^{M \times N}} & \underbrace{C_{y y}}_{\mathbb{R}^{M \times M}}
\end{array}\right] \in R^{(N+M) \times (N+M)}
$$
{{< /math >}} 

Einsetzen in $(\ast)$ ergibt sich der **Nichtlineare Kalman Filter**:

{{< math >}}
$$
\begin{array}{l}
\underline{\hat{x}}_{e}=\underline{\hat{x}}_{p}+\mathbf{C}_{x y} \mathbf{C}_{y y}^{-1}(\underline{\hat{y}}-E\{\underline{h}(\underline{x})\}) \\
\mathbf{C}_{e}=\mathbf{C}_{p}-\mathbf{C}_{x y} \mathbf{C}_{y y}^{-1} \mathbf{C}_{y x}
\end{array}
$$
{{< /math >}} 

