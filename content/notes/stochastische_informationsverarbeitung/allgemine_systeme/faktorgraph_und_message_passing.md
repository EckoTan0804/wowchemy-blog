---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 580
# ============================================================

# ========== Basic metadata ==========
title: Faktorgraphen und Message Passing
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

## Faktorgraphen

### Regeln

![allg_sys-Faktorgraph.drawio (1)](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-Faktorgraph.drawio%20%281%29.png)

### Beispiel 

![allg_sys-Faktorgraph_Bsp.drawio](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-Faktorgraph_Bsp.drawio.png)



## Message Passing

Definiere Nachricht an einer Kante

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-Nachricht.drawio%20%281%29.png" alt="allg_sys-Nachricht.drawio (1)" style="zoom:67%;" />

Schnitt zur Aufteilung eines Systems in 2 Teile

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-System_Schnitt.drawio%20%281%29.png" alt="allg_sys-System_Schnitt.drawio (1)" style="zoom:67%;" />

Betrachtung von Block mit einem Eingang und einem Ausgang

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-Block.drawio%20%282%29.png" alt="allg_sys-Block.drawio (2)" style="zoom:67%;" />

Gegeben: $R_x$ und $L_y$

{{< math >}}
$$
\begin{aligned}
&R_{y}(y)=\int f(y \mid x) \cdot R_{x}(x) d x \\
&L_{x}(x)=\int f(y \mid x) \cdot L_{y}(y) d y
\end{aligned}
$$
{{< /math >}} 

Speizialfall: Lineares System

{{< math >}}
$$
\begin{aligned}
y &= Hx\\
\Rightarrow f(y \mid x) &= \delta(y - Hx)
\end{aligned}
$$
{{< /math >}} 



{{< math >}}
$$
\begin{aligned}
R_y(y) &= \int \delta(y-Hx) R_x(x) dx  \quad \mid g(x):=y-Hx, g^\prime(x) = -H, x_1 = \frac{y}{H}\\
&= \int \frac{1}{|H|} \delta(x - \frac{y}{H}) R_x(x) dx \\
&= \frac{1}{|H|} R_x(\frac{y}{H})
\end{aligned}
$$
{{< /math >}} 

{{< math >}}
$$
\begin{aligned}
L_{x}(x) &=\int f(y \mid x) L_{y}(y) d y \\
&=\int \delta(y-H x) \cdot L_{y}(y) d y \\
&=L_{y}(H \cdot x)
\end{aligned}
$$
{{< /math >}} 

### Beispiel

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-Message_Passing_Bsp.drawio.png" alt="allg_sys-Message_Passing_Bsp.drawio" style="zoom: 67%;" />

- Gegeben: $\underline{\hat{x}}_4$
- Gesucht: $f(\underline{x}_2 \mid \underline{\hat{x}}_4)$
- Ziel: Rekursive Berechnung der Nachrichten

- Direkt gegeben:

  {{< math >}}
  $$
  R_{1}\left(\underline{x}_{1}\right)=f_{1}\left(\underline{x}_{1}\right) \quad L_{3}\left(\underline{x}_{3}\right)=f\left(\underline{\hat{x}}_{4} \mid \underline{x}_{3}\right)
  $$
  {{< /math >}} 

- Benötigt: $L_2(\underline{x}_2)$ und $R_2(\underline{x}_2)$

  {{< math >}}
  $$
  \begin{aligned}
  &R_{2}\left(\underline{x}_{2}\right)=\int f\left(\underline{x}_{2} \mid \underline{x}_{1}\right) R_{1}\left(\underline{x}_{1}\right) d \underline{x}_{1} \\
  &L_{2}\left(\underline{x}_{2}\right)=\int f\left(\underline{x}_{3} \mid \underline{x}_{2}\right) L_{3}\left(\underline{x}_{3}\right) d \underline{x}_{3}
  \end{aligned}
  $$
  {{< /math >}} 

$\Rightarrow$ Fusionsergebnis:

{{< math >}}
$$
f\left(\underline{x}_{2} \mid \underline{\hat{x}}_{4}\right) \propto L_{2}\left(\underline{x}_{2}\right) \cdot R_{2}\left(\underline{x}_{2}\right)
$$
{{< /math >}} 