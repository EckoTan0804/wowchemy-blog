---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 640
# ============================================================

# ========== Basic metadata ==========
title: Progressive Filterung
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

## Systematisches Resampling

- Gegeben: Priore Dirac Mixture

  {{< math >}}
  $$
  f_{p}(\underline{x})=\sum_{i=1}^{L} w_{i}^{p} \delta(\underline{x}-\underline{\hat{x}}_i^p)
  $$
  {{< /math >}} 

- Filterschritt (Bayes)

  {{< math >}}
  $$
  \tilde{f}_e(\underline{x}) \propto f_{p}(\underline{x}) \cdot f_{L}(\underline{x})=\sum_{i=1}^{L} \underbrace{w_{i}^{p} \cdot f_{L}\left(\hat{\underline{x}}_{i}^{p}\right)}_{w_{i}^{e}} \cdot \delta(\underline{x} - \underbrace{\underline{\hat{x}}_{i}^{p}}_{\underline{x}_{i}^{e}})
  $$
  {{< /math >}} 

- Probleme
  - Falls Support / Träger von $f_L(\cdot)$ kleiner als Support von $f_p(\cdot)$, sterben viele Partikel aus!
  - Positionen {{< math >}}$\underline{\hat{x}}_i^e${{< /math >}} sterben aus!
- Lösung
  - Progressive Verarbeitung
  - Reapproximation durch Optimierung

## Progressive Filterung

Progressiv = Der Filterschritt wird nicht in einen Schlag verwendet, sondern wir verwenden mehrere Likelihood, um die Filterung durchzuführen.

Effektives Support:

{{< math >}}
$$
\alpha_{\varepsilon}(f(\cdot))=\{x: f(x) \geqslant \varepsilon\} \qquad (\alpha-\text{Schritt bei } \epsilon)
$$
{{< /math >}} 

Gegeben: Likelihood $f_L(\underline{x})$ mit {{< math >}}$\alpha_{\varepsilon}(f_L(\cdot)) \ll \alpha_{\varepsilon}(f_p(\cdot))${{< /math >}} 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-15%2022.21.19.png" alt="截屏2022-08-15 22.21.19" style="zoom:50%;" />

Dekomposition von {{< math >}}$f_L(\underline{x}) ${{< /math >}} 

{{< math >}}
$$
f_L(\underline{x}) = f_L^1(\underline{x}) \cdot f_L^2(\underline{x}) \cdots f_L^k(\underline{x})
$$
{{< /math >}} 

Der Produkt von Dichten: $f_L^i(\underline{x})$ "breiter" als $f_L(\underline{x})$ $\rightarrow$ Effektives Support ist größer ({{< math >}}$\alpha_{\varepsilon}(f_L^i(\cdot)) > \alpha_{\varepsilon}(f_L(\cdot))${{< /math >}} )

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-15%2022.33.16.png" alt="截屏2022-08-15 22.33.16" style="zoom:67%;" />

Note: Dekomposition ist NICHT eindeutig.

Damit kann Filterschritt dekomponiert werden:

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-15%2022.43.30.png" alt="截屏2022-08-15 22.43.30" style="zoom: 33%;" />

- In jedem Schritt Gewichtung der prioren Dirac Mixture
- Reapproximation nach jedem Teil-Filterschritt

Algorithms:

- {{< math >}}$f_e^0 (\underline{x}) = f_p(\underline{x})${{< /math >}} 

- For $i \in \{1, \dots, k\}$

  {{< math >}}
  $$
  \begin{aligned}
  \tilde{f}_e^i(\underline{x}) &= f_e^{i-1}(\underline{x}) \cdot f_L^i((\underline{x})) \text{ (gewicht)} \quad \to f_e(\underline{x}) \\
  f_e^{i}(\underline{x}) &= \operatorname{Reapproximate}(\tilde{f}_e^i(\underline{x})) \text{ (ungewicht)} \quad \to  = f_e^k(\underline{x}) 
  \end{aligned}
  $$
  {{< /math >}} 



## Reapproximation

#### Ziel

- Gegeben: Gewichtete Dirac Mixture

  {{< math >}}
  $$
  \tilde{f}(\underline{x}) = \sum_{i=1}^L \tilde{w}_i \cdot \delta(\underline{x} - \underline{\hat{x}}_i)
  $$
  {{< /math >}} 

- Gesucht: Ungewichtete Dirac Mixture

  {{< math >}}
  $$
  \tilde{f}(\underline{x}) \approx f(\underline{x}) = \sum_{i=1}^L \frac{1}{L} \cdot \delta(\underline{x} - \underline{\hat{x}}_i)
  $$
  {{< /math >}} 

- Gütemaß: Distanz $D(\tilde{f}(\underline{x}) , f(\underline{x}))$

- Aber Abstand zwischen Dirac Mixtures in Dichtebereich schwierig 🤪 $\rightarrow$ Wir betrachten die Kumulative Verteilung $\tilde{F}(\underline{x}), F(\underline{x})$

  {{< math >}}
  $$
  \begin{aligned}
  \tilde{F}(\underline{x}) &= \sum_{i=1}^L \tilde{w}_i \cdot H(\underline{x} - \underline{\hat{x}}_i) \\
  F(\underline{x}) &= \sum_{i=1}^L \frac{1}{L} \cdot H(\underline{x} - \underline{\hat{x}}_i) \\
  \end{aligned}
  $$
  {{< /math >}} 

### Herausforderungen

Minimalbeispiel: Approximation von zwei Dirac Komponenten durch eine Komponent

{{< math >}}
$$
\begin{aligned}
\tilde{F}(\underline{x}) &= w_1 \cdot H(x - \tilde{x}_1) +  w_2 \cdot H(x - \tilde{x}_2) \qquad w_1, w_2 > 0, w_1 + w_2 = 1 \\
F(x) &= H(x - \hat{x})
\end{aligned}
$$
{{< /math >}} 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-15%2022.59.28.png" alt="截屏2022-08-15 22.59.28" style="zoom: 50%;" />

Cramér–von Mises Distanz:

{{< math >}}
$$
D=\int_{-\infty}^{\infty}[\tilde{F}(x)-F(x)]^{2} d x=\left(\hat{x}-\tilde{x}_{1}\right) \cdot w_{1}^{2}+\left(\hat{x}-\tilde{x}_{2}\right) \cdot w_{2}^{2} \quad \text{für} \quad \tilde{x}_{1} \leq \hat{x} \leq \tilde{x}_{2}
$$
{{< /math >}} 

{{< math >}}
$$
\frac{\partial D}{\partial \hat{x}} = w_1^2 + w_2^2
$$
{{< /math >}} 

D.h., Für alle $\hat{x}$ mit {{< math >}}$\tilde{x}_{1} \leq \hat{x} \leq \tilde{x}_{2}${{< /math >}},  {{< math >}}$D${{< /math >}} is immer minimiert $\rightarrow$ NICHT eindeutig!

### Wasserstein-Distanz

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-16%2009.40.17.png" alt="截屏2022-08-16 09.40.17" style="zoom:50%;" />

{{< math >}}
$$
D=\int_{0}^{1}\left[\tilde{F}^{-1}(y)-F^{-1}(y)\right]^{2} d y=w_{1}\left(\hat{x}-\tilde{x}_{1}\right)^{2}+w_{2}\left(\hat{x}-\tilde{x}_{2}\right)^{2}
$$
{{< /math >}} 

{{< math >}}
$$
\begin{aligned}
&\frac{\partial D}{\partial{x}}=2 w_{1}\left(\hat{x}-\tilde{x}_{1}\right)+2 w_{2}\left(\hat{x}-\tilde{x}_{2}\right) \\ 
&\Rightarrow \hat{x}=\frac{w_{1} \cdot \tilde{x}_{1}+w_{2} \tilde{x}_{2}}{w_{1}+w_{2}} \quad \text{(Gewichteter Mittelwert)}
\end{aligned}
$$
{{< /math >}} 

#### Allgemeines Verfahren

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-16%2009.50.33.png" alt="截屏2022-08-16 09.50.33" style="zoom:50%;" />

{{< math >}}
$$
\begin{aligned}
&\hat{x}_{1}=\frac{w_{1} \cdot \tilde{x}_{1}+\left(0.5-w_{1}\right) \cdot \tilde{x}_{2}}{0.5} \\
&\hat{x}_{2}=\frac{\left(w_{1}+w_{2}-0.5\right) \tilde{x}_{2}+\left(1-w_{1}-w_{2}\right) \tilde{x}_{3}}{0.5}
\end{aligned}
$$
{{< /math >}} 

## Gesamtverfahren: Progressives Filterverfahren mit laufender Reapproximation

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-16%2010.00.49.png" alt="截屏2022-08-16 10.00.49" style="zoom: 25%;" />