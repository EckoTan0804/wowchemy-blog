---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 730
# ============================================================

# ========== Basic metadata ==========
title: Wertekontinuierliche lineare Systeme
date: 2022-08-22
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

## Kalman Filter 

**Prädiktion**

{{< math >}}
$$
\underline{\hat{x}}_k^p = \mathbf{A}_{k-1}\underline{\hat{x}}_{k-1}^e + \mathbf{B}_{k-1} \underline{\hat{u}}_{k-1}
$$
{{< /math >}}  

{{< math >}}
$$
\mathbf{C}_k^p = \mathbf{A}_{k-1} \mathbf{C}_{k-1}^e A_{k-1}^\top + \mathbf{B}_{k-1} \mathbf{C}_{k-1}^w \mathbf{B}_{k-1}^\top
$$
{{< /math >}} 

**Filterung**

{{< math >}}
$$
\mathbf{K}_k = \mathbf{C}_k^p \mathbf{H}_k^\top (\mathbf{C}_k^v + \mathbf{H}_k \mathbf{C}_k^p \mathbf{H}_k ^\top)^{-1}
\tag{Kalman Gain}
$$
{{< /math >}}  

{{< math >}}
$$
\underline{\hat{x}}_k^e = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k) \underline{\hat{x}}_k^p + \mathbf{K}_k \underline{\hat{y}}_k = \underline{\hat{x}}_k^p + \mathbf{K}_k(\underline{\hat{y}}_k - \mathbf{H}_k \underline{\hat{x}}_k^p)
$$
{{< /math >}} 

{{< math >}}
$$
\mathbf{C}_k^e = (\mathbf{I} - \mathbf{K}_k\mathbf{H}_k)\mathbf{C}_k^p = \mathbf{C}_k^p - \mathbf{C}_k^p \mathbf{H}_k^\top (\mathbf{C}_k^v + \mathbf{H}_k \mathbf{C}_k^p \mathbf{H}_k ^\top)^{-1}\mathbf{H}_k \mathbf{C}_k^p
$$
{{< /math >}} 

## Kalman Filter (vektoriell) herleiten

### Prädiktion

Systemabbildung

{{< math >}}
$$
\underline{x}_{k+1}=\mathbf{A}_{k} \cdot \underline{x}_{k}+\mathbf{B}_{k} \cdot \underbrace{\left(\underline{\tilde{u}}_{k}+\underline{w}_{k}\right)}_{\underline{u_k}}
$$
{{< /math >}} 

Schritte

1. Berechnung des Erwartungswerts für $k+1$

   {{< math >}}
   $$
    E\left\{\underline{x}_{k+1}\right\}=\mathbf{A}_{k} \cdot \underline{\hat{x}}_{k|1: m}+\mathbf{B}_{k} \tilde{\underline{u}}_{k} \qquad (+)
   $$
   {{< /math >}} 

2. Berechnung der Kovarianzmatrix {{< math >}}$C_{k+1|1:m}^x${{< /math >}} mit der Annahme, dass Zustand und Systemrauschen unkorreliert sind

   {{< math >}}
   $$
   \begin{aligned}
     \underline{x}_{k+1} &=\mathbf{A}_{k} \underline{x}_{k}+\mathbf{B}_{k} \underline{u}_{k} \\
     &=\left[\begin{array}{ll}
     \mathbf{A}_{k} & \mathbf{B}_{k}
     \end{array}\right]\left[\begin{array}{c}
     \underline{x}_{k} \\
     \underline{u}_{k}
     \end{array}\right]
     \end{aligned}
   $$
   {{< /math >}} 

   1. Berechne {{< math >}}$\operatorname{Cov}\left\{\left[\begin{array}{c}
        \underline{x}_{k} \\
        \underline{\tilde{u}}_{k}
        \end{array}\right]\right\}${{< /math >}} 

      {{< math >}}
      $$
      \begin{aligned}
        \underline{x}_{k+1}-\hat{\underline{x}}_{k+1} &=\left[\begin{array}{ll}
        \mathbf{A}_{k} & \mathbf{B}_{k}
        \end{array}\right]\left[\begin{array}{c}
        \underline{x}_{k}-\hat{\underline{x}}_{k} \\
        \underline{u}_{k}-\underline{\hat{u}}_{k}
        \end{array}\right] \\
        &=\left[\begin{array}{ll}
        \mathbf{A}_{k} & \mathbf{B}_{k}
        \end{array}\right]\left[\begin{array}{c}
        \underline{x}_{k}-\underline{\hat{x}}_{k} \\
        \underline{w}_{k}
        \end{array}\right]
        \end{aligned}
      $$
      {{< /math >}} 

      {{< math >}}
      $$
      \begin{aligned}
        \operatorname{Cov}\left\{\left[\begin{array}{c}
        \underline{x}_{k} \\
        \underline{\tilde{u}}_{k}
        \end{array}\right]\right\} &=E\left\{\left[\begin{array}{c}
        \underline{x}_{k}-\underline{\hat{x}}_{k} \\
        \underline{w}_{k}
        \end{array}\right]\left[\left(\underline{x}_{k}-\underline{\hat{x}}_{k}\right)^{\top} \underline{w}_{k}^{\top}\right]\right\} \\
        &=\left[\begin{array}{cc}
        C_{k \mid 1: m}^{x} & 0 \\
        0 & C_{k}^{w}
        \end{array}\right]
        \end{aligned}
      $$
      {{< /math >}} 

   2. {{< math >}}$\operatorname{Cov}\left\{\left[\begin{array}{c}
        \underline{x}_{k} \\
        \underline{\tilde{u}}_{k}
        \end{array}\right]\right\}${{< /math >}} in Berechnung von {{< math >}}$C_{k+1|1:m}^x${{< /math >}} einsetzen

      {{< math >}}
      $$
      \begin{aligned}
        \mathbf{C}_{k+1 \mid 1 : m}^{x} &=E\left\{\left(\underline{x}_{k+1}-\hat{x}_{k+1}\right)\left(x_{k+1} - \hat{\underline{x}}_{k+1}\right)^\top\right\} \\
        &=\left[\begin{array}{ll}
        \mathbf{A}_{k} & \mathbf{B}_{k}
        \end{array}\right] \cdot E\left\{\left[\begin{array}{c}
        \underline{x}_{k}-\hat{\underline{x}}_{k} \\
        \underline{w}_{k}
        \end{array}\right]\left[\begin{array}{ll}
        \underline{x}_{k}-\hat{\underline{x}}_{k} & \underline{w}_{k}
        \end{array}\right]\right\} \cdot\left[\begin{array}{l}
        \mathbf{A}_{k}^{\top} \\
        \mathbf{B}_{k}^{\top}
        \end{array}\right] \\\\
        &=\left[\begin{array}{ll}
        \mathbf{A}_{k} & \mathbf{B}_{k}
        \end{array}\right] \cdot\left[\begin{array}{cc}
        \mathbf{C}_{k \mid 1:m} & 0 \\
        0 & \mathbf{C}_{k}^{w}
        \end{array}\right] \cdot\left[\begin{array}{l}
        \mathbf{A}_{k}^{\top} \\
        \mathbf{B}_{k}^{\top}
        \end{array}\right] \\
        &=\mathbf{A}_{k} \cdot \mathbf{C}_{k \mid 1: m}^{x} \mathbf{A}_{k}^{\top}+\mathbf{B}_{k} \mathbf{C}_{k}^{w} \mathbf{B}_{k}^{\top} \qquad(++)
        \end{aligned}
      $$
      {{< /math >}} 

### Filterung

Messabbildung

{{< math >}}
$$
\underline{y}_{k}=\mathbf{H}_{k} \cdot \underline{x}_{k}+\underline{v}_{k}
$$
{{< /math >}} 

Schritte

1. Schreibe $\underline{x}_k^e$ als lineare Kombination von $\underline{x}_k^p$ und $\underline{y}_k$

   {{< math >}}
   $$
   \underline{x}_{k}^e=\mathbf{K}_{k}^{(1)} \underline{x}_{k}^p+\mathbf{K}_{k}^{(2)} \underline{y}_{k}
   $$
   {{< /math >}} 

2. Aus BLUE Filter ergibt sich

   {{< math >}}
   $$
   E\{\underline{x}_{k}^e\}=E\{\mathbf{K}_{k}^{(1)} \underline{x}_{k}^p+\mathbf{K}_{k}^{(2)} \underline{y}_{k}\}
   $$
   {{< /math >}} 

   $\Rightarrow$

   {{< math >}}
   $$
   \begin{aligned}
     \mathbf{K}_{k}^{(1)} &= \mathbf{I} - \mathbf{K}_{k}\mathbf{H}_{k} \\
     \mathbf{K}_{k}^{(2)} &= \mathbf{K}_{k}
   \end{aligned}
   $$
   {{< /math >}} 

   und

   {{< math >}}
   $$
   \underline{x}_{k}^e=(\mathbf{I} - \mathbf{K}_{k}\mathbf{H}_{k}) \underline{x}_{k}^p+\mathbf{K}_{k} \underline{y}_{k}
   $$
   {{< /math >}} 

3. Berechne Kovarianzmatrix $\mathbf{C}_k^e$

   {{< math >}}
   $$
   \mathbf{C}_{k}^{e}\left(\mathbf{K}_{k}\right)=E\{\underline{x} - \underline{x}_k^e\} = \left(\mathbf{I}-\mathbf{K}_{k} \mathbf{H}_{k}\right) \mathbf{C}_{k}^{p}\left(\mathbf{I}-\mathbf{K}_{k} \mathbf{H}_{k}\right)^{\top}+\mathbf{K}_{k} C_{k}^{v} \mathbf{K}_{k}^{\top}
   $$
   {{< /math >}} 

   Wir suche $\mathbf{K}_{k}$ so, dass der resultierende Schätzer MINIMAL kovarianz aufweist.

   1. Auf skalares Gütemaß zurückzuführen

      {{< math >}}
      $$
      P(\mathbf{K}_{k}) = \underline{e}^\top \left( \left(\mathbf{I}-\mathbf{K}_{k} \mathbf{H}_{k}\right) \mathbf{C}_{k}^{p}\left(\mathbf{I}-\mathbf{K}_{k} \mathbf{H}_{k}\right)^{\top}+\mathbf{K}_{k} C_{k}^{v} \mathbf{K}_{k}^{\top}\right) \underline{e}
      $$
      {{< /math >}} 

   2. {{< math >}}$\frac{\partial}{\partial \mathbf{K}_{k}} P(\mathbf{K}_{k})\overset{!}{=} 0 \Rightarrow${{< /math >}} 

      {{< math >}}
      $$
      \mathbf{K}_k = \mathbf{C}_k^p \mathbf{H}_k^\top (\mathbf{C}_k^v + \mathbf{H}_k \mathbf{C}_k^p \mathbf{H}_k^\top)^{-1}
      $$
      {{< /math >}} 

4. {{< math >}}$\mathbf{K}_k${{< /math >}} in {{< math >}}$\underline{x}_{k}^e${{< /math >}} und {{< math >}}$\mathbf{C}_{k}^{e}${{< /math >}} einsetzen



## Ergebnis von "Gauß mal Gauß"





## Drei Gütemaße für die „Größe“ einer Kovarianzmatrix

Mögliche Gütemaße für generelles Vergleichen von Kovarianzmatrizen:

{{< math >}}
$$
f: \mathbb{R}^{n \times n} \to \mathbb{R}^1
$$
{{< /math >}} 

Funktion, die einer Kovarianzmatrix einen Skalar zuordnen kann, denn man kann nur Skalare direkt miteinander vergleichen.

Drei Gütemaße 

- Projektion mit Einheitsvektor
- Spur
- Determinante

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-22%2012.31.16.png" alt="截屏2022-08-22 12.31.16" style="zoom:67%;" />