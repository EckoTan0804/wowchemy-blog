---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 107
# ============================================================

# ========== Basic metadata ==========
title: HMM und Wonham Filter
date: 2022-06-29
draft: false
type: book # page type
authors:
  - admin
tags:
  - SI
  - Lecture Notes
  - Math
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

Das **Hidden Markov Model (HMM)** ist ein [stochastisches](https://de.wikipedia.org/wiki/Stochastik) [Modell](https://de.wikipedia.org/wiki/Mathematisches_Modell), in dem ein System durch eine [Markowkette](https://de.wikipedia.org/wiki/Markowkette) mit unbeobachteten Zuständen modelliert wird. 

> Die Modellierung als Markowkette bedeutet, dass das System auf zufällige Weise von einem Zustand in einen anderen übergeht, wobei die [Übergangswahrscheinlichkeiten](https://de.wikipedia.org/wiki/Übergangswahrscheinlichkeit) nur jeweils vom aktuellen Zustand abhängen, aber nicht von den davor eingenommenen Zuständen.

Ein HMM besteht aus

- Systemmodell / Übergangswahrscheinlichkeiten / Transitionsmatrix $\mathbf{A}$
- Messmodell / Emissionswahrscheinlichkeiten / Messmatrix $\mathbf{B}$

- Zustandsraum; Zustandswahrscheinlichkeiten $\xi_{k}^{\boldsymbol{x}}$
- Messungen; Emissionswahrscheinlichkeiten $\xi_{k}^{\boldsymbol{y}}$
- Initialer Zustand $x_0$ oder initiale Zustandswahrscheinlichkeit $\xi_{0}^{\boldsymbol{x}}$

**Beispiel (Übungsblatt 4.2)**

![截屏2022-06-29 15.45.15](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-06-29%2015.45.15.png)

- Zustandsraum

  {{< math >}}
  $$
  \begin{aligned}
  S &=\{\text { Sonniger Tag }\} \\
  R &=\{\text { Regnerischer Tag }\} \\
  N &=\{\text { Nebliger Tag }\}
  \end{aligned}
  $$
  {{< /math >}} 

- Zustandsvektor

  {{< math >}}
  $$
  \xi_{k}^{\boldsymbol{x}}=\left[\begin{array}{l}
  \mathrm{P}\left(\boldsymbol{x}_{k}=S\right) \\
  \mathrm{P}\left(\boldsymbol{x}_{k}=R\right) \\
  \mathrm{P}\left(\boldsymbol{x}_{k}=N\right)
  \end{array}\right]
  $$
  {{< /math >}} 

- Transiitonsmatrix

  {{< math >}}
  $$
  \mathbf{A}=\left[\begin{array}{lll}
  0.7 & 0.2 & 0.1 \\
  0.2 & 0.6 & 0.2 \\
  0.4 & 0.3 & 0.3
  \end{array}\right]
  $$
  {{< /math >}} 

- Messwerte

  {{< math >}}
  $$
  \begin{array}{l}
  d=\{\text { dreckige Schuhe }\} \\
  s=\{\text { saubere Schuhe }\}
  \end{array}
  $$
  {{< /math >}} 

- Messvektor

  {{< math >}}
  $$
  \underline{\xi}_{k}^{\boldsymbol{y}}=\left[\begin{array}{l}
  \mathrm{P}\left(\boldsymbol{z}_{k}=d\right) \\
  \mathrm{P}\left(\boldsymbol{z}_{k}=s\right)
  \end{array}\right]
  $$
  {{< /math >}} 

- Messmatrix

  {{< math >}}
  $$
  \mathbf{B}=\left[\begin{array}{ll}
  0.1 & 0.9 \\
  0.8 & 0.2 \\
  0.4 & 0.6
  \end{array}\right]
  $$
  {{< /math >}} 

- Initiale Zustandswahrscheinlichkeit $\xi_{0}^{\boldsymbol{x}}$ und initialer Zustand $x_0$

  {{< math >}}
  $$
  \underline{\xi}_{0}^{\boldsymbol{x}}=\left[\begin{array}{l}
  1 \\
  0 \\
  0
  \end{array}\right] ; \quad x_{0}=S
  $$
  {{< /math >}} 

Modell als Zustandsdiagramm mit Übergangswahrscheinlichkeiten

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/wertdiskrete_systeme-HMM.drawio.png" alt="wertdiskrete_systeme-HMM.drawio" style="zoom:80%;" />

## Wonham-Filter

Das Wonham Filter ist ein rekursives Filter für Zustandschätzung für wertdiskrete Systeme.

Das Wonham Filter besteht aus zwei Phasen

1. Prädiktion

   {{< math >}}
   $$
   \underline{\xi}_{k \mid 1: k-1}^{x}=\mathbf{A}_{k}^{\top} \underline{\xi}_{k-1\mid1: k-1}^{x}
   $$
   {{< /math >}} 

   - {{< math >}}$\mathbf{A}_k${{< /math >}}: Transitionsmatrix
   - {{< math >}}$\underline{\xi}_{k-1\mid1: k-1}^{x}${{< /math >}}: letzte Zustandsschätzung

2. Filterung

   Für Messung $y_k = m$:

   {{< math >}}
   $$
   \underline{\xi}_{k \mid 1: k}^{x} =\frac{\mathbf{B}(:, m) \odot \eta_{k \mid 1: k-1}^{x}}{\mathbb{1}_{N}^{T} \operatorname{diag}(\mathbf{B}(:, m)) \cdot \eta_{k \mid 1: k-1}^{x}} =\frac{\mathbf{B}(:, m) \odot \eta_{k \mid 1: k-1}^{x}}{\mathbf{B}(:, m)^\top \cdot \eta_{k \mid 1: k-1}^{x}}
   $$
   {{< /math >}} 

(Mehr über Wonham filter siehe [hier]({{< relref "../wertdiskrete_systeme/zustandsschaetzung#zustandsschätzung" >}}))

**Beispiel (weiter)**

![截屏2022-06-29 16.05.37](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-06-29%2016.05.37.png)

Zeitpunkt $k=1$: 

{{< math >}}
$$
\begin{array}{l}
\underline{\xi}_{1}^{p}=\mathbf{A}^{\top} \underline{\xi}_{0}^{\boldsymbol{x}}=\left[\begin{array}{l}
0.7 \\
0.2 \\
0.1
\end{array}\right] \\\\
\underline{\xi}_{1}^{e}=\frac{\mathbf{B}(:, 1) \odot \underline{\xi}_{1}^{p}}{\mathbf{B}(:, 1)^{\top} \underline{\xi}_{1}^{p}}=\frac{\left[\begin{array}{l}
0.1 \\
0.8 \\
0.4
\end{array}\right] \odot\left[\begin{array}{l}
0.7 \\
0.2 \\
0.1
\end{array}\right]}{\left[\begin{array}{lll}
0.1 & 0.8 & 0.4
\end{array}\right]\left[\begin{array}{l}
0.7 \\
0.2 \\
0.1
\end{array}\right]}=\frac{\left[\begin{array}{l}
0.07 \\
0.16 \\
0.04
\end{array}\right]}{0.27}=\left[\begin{array}{l}
0.25926 \\
0.59259 \\
0.14815
\end{array}\right]
\end{array}
$$
{{< /math >}} 

$P(\boldsymbol{x}_1 = R) = 0.59259$ ist die größst in $\underline{\xi}_{1}^{e}$. $\Rightarrow$ Die Schätzung deutet auf einen regnerischen Tag.

Zeitpunkt $k=2$: 

{{< math >}}
$$
\begin{aligned}
\underline{\xi}_{2}^{p} &=\mathbf{A}^{\top} \underline{\xi}_{1}^{e}=\left[\begin{array}{l}
0.35926 \\
0.45185 \\
0.18889
\end{array}\right] \\
\underline{\xi}_{2}^{e} &=\frac{\mathbf{B}(:, 1) \odot \xi_{2}^{p}}{\mathbf{B}(:, 1)^{\top} \xi_{2}^{p}}=\left[\begin{array}{l}
0.07596 \\
0.76429 \\
0.15975
\end{array}\right]
\end{aligned}
$$
{{< /math >}} 

$\Rightarrow$ Die Schätzung deutet auf einen regnerischen Tag.

Zeitpunkt $k=3$: 

{{< math >}}
$$
\underline{\xi}_{3}^{p}=\mathbf{A}^{\top} \underline{\xi}_{2}^{e}=\left[\begin{array}{l}
0.26993 \\
0.52169 \\
0.20838
\end{array}\right]
$$
{{< /math >}} 

{{< math >}}
$$
\xi_{3}^{e}=\frac{\mathbf{B}(:, 2) \odot \xi_{3}^{p}}{\mathbf{B}(:, 2)^{\top} \xi_{3}^{p}}=\left[\begin{array}{l}
0.51437 \\
0.22091 \\
0.26472
\end{array}\right]
$$
{{< /math >}} 

$\Rightarrow$ Die Schätzung deutet auf einen sonnigen Tag.

Zeitpunkt $k=4$: 

{{< math >}}
$$
\begin{array}{l}
\underline{\xi}_{4}^{p}=\mathbf{A}^{\top} \underline{\xi}_{3}^{e}=\left[\begin{array}{ll}
0.510 & 13 \\
0.314 & 84 \\
0.175 & 04
\end{array}\right]\\
\xi_{4}^{e}=\frac{\mathbf{B}(:, 2) \odot \xi_{4}^{p}}{\mathbf{B}(:, 2)^{\top} \xi_{4}^{p}}=\left[\begin{array}{l}
0.73212 \\
0.10041 \\
0.16747
\end{array}\right]
\end{array}
$$
{{< /math >}} 

$\Rightarrow$ Die Schätzung deutet auf einen sonnigen Tag.

**Beispiel (weiter)**

![截屏2022-06-29 18.20.53](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-06-29%2018.20.53.png)

Lösung:

![截屏2022-06-29 18.21.12](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-06-29%2018.21.12.png)
