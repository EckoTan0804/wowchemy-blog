---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 440
# ============================================================

# ========== Basic metadata ==========
title: Ensemble Kalmanfilter (EnKF)
date: 2022-07-15
draft: false
type: book # page type
authors:
  - admin
tags:
  - SI
  - Lecture Notes
  - Nichtlineares Kalmanfilter
  - EnKF
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

## Motivation

Prädiktionsschritt von Nichtlineares Kalmanfilter (NLKF) $\rightarrow$ speziell Variante sample-basiert

![EnKF.drawio](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/EnKF.drawio.png)

Durch Re-approximation mit Gaußdichte $\rightarrow$ Zusatzinformation verloren

Wenn keine Messungen vorliegen und mehrere Prädiktionsschritte nacheinander $\rightarrow$ Man kann temporär Approximation fortlassen

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/EnKF-EnKF_Motivation.drawio.png" alt="EnKF-EnKF_Motivation.drawio" style="zoom:67%;" />

Filterschritt von NLKF

{{< math >}}
$$
\begin{array}{l}
\underline{\hat{x}}_{e}=\underline{\hat{x}}_{p}+\mathbf{C}_{x y} \mathbf{C}_{y y}^{-1}(\underline{\hat{y}}-E\{\underline{h}(\underline{x})\}) \\
\mathbf{C}_{e}=\mathbf{C}_{p}-\mathbf{C}_{x y} \mathbf{C}_{y y}^{-1} \mathbf{C}_{y x}
\end{array}
$$
{{< /math >}} 

wobei

{{< math >}}
$$
\begin{array}{ll}
\mathbf{C}_{x x}=\mathbf{C}_{p} \in \mathbb{R}^{N \times N}\quad &\mathbf{C}_{x y} \in \mathbb{R}^{N \times M} \\
\mathbf{C}_{y x} \in \mathbb{R}^{M \times N}\quad  &\mathbf{C}_{yy} \in \mathbb{R}^{M \times M}
\end{array}
$$
{{< /math >}} 

Unabhängig von gewähltes Form der Momenteberechnung $\rightarrow$ Hoher Aufwand für Berechnung und Speichern der Kovairanzmatrizen 🤪

## Idee

- Beibehaltung der Samples nach Prädiktionsschritt $\rightarrow$ Keine Re-approximation  durch Gauß
- Damit bleibt Forminformation erhalten und Unsicherheit wird in samples gespeichert.

- Speicherkomplexität

  - Kalmanfilter (KF)

    - Erwartungswert; $N$
    - Kovarianzmatrix $\frac{N(N+1)}{2}$

    $\Rightarrow$ Insgesamt $\frac{N^2 + 3N}{2}$

  - EnKF

    - Ein sample: $N$
    - $L$ samples: $L \cdot N$ (z.B mit sampling auf der Hauptachse gilt $L = 2N \rightarrow 2N^2$)

- Aber: spart Aufwand bei Berechnung der Kovarianzmatrix

- 🎯 Ziel: Rekursive Berechnung des Prädiktionsschritts

## Herausforderungen

Gegeben

- $L$ Samples {{< math >}}$\underline{x}_{k, i}, i = 1, \dots, L${{< /math >}} 

- Systemabbildung 

  {{< math >}}
  $$
  \underline{x}_{k+1} = \underline{a}_k(\underline{x}_k, \underline{w}_k)
  $$
  {{< /math >}} 

Gesucht: $L^\prime$ Samples {{< math >}}$\underline{x}_{k, i+1}, i = 1, \dots, L^\prime${{< /math >}} 

Wir benötigen Samples für $\underline{w}_k$: {{< math >}}$\underline{w}_{k, j}, j = 1, \dots, Q${{< /math >}}  

‼️ Problem: Abbildung der Kombination aller Samples $\Rightarrow$ <span style="color: Red">Kartesisches Produkt!!! $\Rightarrow$ Anzahl der Samples steigt bei rekursiver Prädiktion *exponentiell* !!!</span>

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/EnKF-EnKF_Herausforderung.drawio.png" alt="EnKF-EnKF_Herausforderung.drawio" style="zoom:67%;" /> 

**Lösungsidee: Begrenzung der Abtastwerte**

- Ziel: Einstellbare Anzahl an Samples $\rightarrow$ um Komplexität zu folgen
- Einfacher Fall: Konstante Anzahl Samples über Zeit

**Anzatz 1: Über Reduktion**

- Prior

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/EnKF-Reduktion.drawio.png" alt="EnKF-Reduktion.drawio" style="zoom: 67%;" />

- Posterior (also Reduktion von {{< math >}}$\underline{x}_{k+1, i}${{< /math >}} )

  - braucht $L \cdot Q$ Abbildungen
  - Ergebnis aber oft besser

**Ansatz 2: Anzahl von Parren mit Latin Hypercube Sampleing (LHS)**

- Jede Zeile und Spalte darf NUR *ein* Element erhalten

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/EnKF-LHS.drawio.png" alt="EnKF-LHS.drawio" style="zoom:80%;" />

- Optimale Wahl schwierig 

  - Diskretes Gütemaß ist i.d.R. zimliche kompliziert

- Triviale praktische Umsetzung: Ziehe (Konstante) Samples aus {{< math >}}$\underline{w}_k${{< /math >}} für jedes {{< math >}}$\underline{x}_{k, i}${{< /math >}} (aber schlecht für wenige Samples)

  Anordnung

  {{< math >}}
  $$
  \mathcal{X}_{k}=[\underbrace{\underline{x}_{k, 1}}_{\mathbb{R}^N}, \underline{x}_{k, 2}, \ldots, \underline{x}_{k, L}] \in \mathbb{R}^{N \times L}, \quad \mathcal{W}_{k}=\left[\underline{w}_{k, 1}, \underline{w}_{k, 2}, \ldots, \underline{w}_{k, L}\right] \in \mathbb{R}^{N \times L}
  $$
  {{< /math >}} 

  > Jede {{< math >}}$\underline{x}_{k, i}${{< /math >}} und {{< math >}}$\underline{w}_{k, j}${{< /math >}} ist ein Vektor.

  {{< math >}}$\underline{a}_k${{< /math >}} überladen:

  {{< math >}}
  $$
  \mathcal{X}_{k+1} = \underline{a}_k(\mathcal{X}_{k}, \mathcal{W}_{k})
  $$
  {{< /math >}} 

## Filterschritt

🎯 Ziel

- Durchführung der Filterschritt NUR mit Samples
  - Direkte Überführung der prioren Samples in posteriore Samples
- Vermeidung der Verwendung der Update-Formeln für Kovarianzmatrix
  - Reine Representation der Unsicherheiten durch Samples

Lineare Messungabbildung

{{< math >}}
$$
\underline{y}=\mathbf{H} \cdot \underline{x}+\underline{v}
$$
{{< /math >}} 

Für gegebene Messung $\hat{y}$:

{{< math >}}
$$
\underbrace{\underline{\hat{y}}-\underline{v}}_{=:\hat{\mathcal{Y}}}=\mathbf{H} \cdot \underline{x}
$$
{{< /math >}} 

Mess-sampleset:

{{< math >}}
$$
\hat{\mathcal{Y}}=\underline{\hat{y}} \cdot \underline{\mathbb{1}}^{\top}-\mathcal{V} \qquad \mathcal{V}=\left[\underline{v}_{1}, \underline{v}_{2}, \ldots, \underline{v}_{L}\right]
$$
{{< /math >}} 

![EnKF-Mess-sampleset.drawio](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/EnKF-Mess-sampleset.drawio.png)

Damit ist Update des Zustands in "combination form"

{{< math >}}
$$
\mathcal{X}_{e}=(\mathbf{I}-\mathbf{K} \mathbf{H}) \mathcal{X}_{p}+\mathbf{K} \mathcal{\hat{Y}}
$$
{{< /math >}} 

> $\mathcal{X}$ und $\mathcal{Y}$ sind Matrizen

wäre begrenzt auf additives Rauschen, aber funktioniert direkt für nichtlineare Messabbildung $\underline{y}=\underline{h}(\underline{x}, \underline{v})$.

Alternative Herleitung

- Prädizierte Mess-samples basierend auf prioren Samples und Rauschen-samples:

  {{< math >}}
  $$
  \mathcal{Y} = \mathbb{H} \cdot \mathcal{X}_p + \mathcal{V}
  $$
  {{< /math >}} 

- Update des Zustands in "feedback form"

  {{< math >}}
  $$
  \begin{aligned}
  \mathcal{X}_e &= \mathcal{X}_p + \mathbf{K}(\underbrace{\underline{\hat{y}} \cdot \underline{\mathbb{1}}^\top}_{\text{gemessen}} - \underbrace{\mathcal{Y}}_{\text{Prädiktion}}) \\\\
  &= \mathcal{X}_e + \mathbf{K}(\underline{\hat{y}} \cdot \underline{\mathbb{1}}^\top - \mathbb{H} \mathcal{X}_p - \mathcal{V})\\\\
  &= (\mathbb{I} - \mathbf{K}\mathbf{H})\mathcal{X}_p + \mathbf{K}(\underbrace{\underline{\hat{y}} \cdot \underline{\mathbb{1}}^\top - \mathcal{V}}_{=\hat{\mathcal{Y}}})
  
  \end{aligned}
  $$
  {{< /math >}} 