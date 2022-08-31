---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 630
# ============================================================

# ========== Basic metadata ==========
title: Partikel Filter
date: 2022-08-14
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

## Naives Partikelfilter

### Prädiktions- und Filterschritt

{{% callout note %}}
Übungsblatt Aufg. 13.2
{{% /callout %}}

#### Prädiktionsschritt 

Zum Startzeitpunkt (z.B. $k=0$): Initiale Samples gegeben

{{< math >}}
$$
f_{k}^{e}\left(\underline{x}_{k}\right)=\sum_{i=1}^{L} w_{k}^{e, i} \cdot \delta\left(\underline{x}_{k}-\underline{\hat{x}}_{k}^{e, i}\right) \qquad w_{k}^{e, i}=\frac{1}{L}, i \in\left\{1, \ldots, L\right\}
$$
{{< /math >}} 

Prädiktion mithilfe des probabilistischen Systemmodells $f(\underline{x}_{k+1} \mid \underline{x}_k)$

- Ziehe Samples zum Zeitpunkt $k+1$

  {{< math >}}
  $$
  \underline{\hat{x}}_{k+1}^{p, i} \sim f\left(\underline{x}_{k+1} \mid \hat{x}_{k}^{e, i}\right)
  $$
  {{< /math >}} 

- Gewichte bleiben gleich

  {{< math >}}
  $$
  w_{k+1}^{p, i} = w_{k}^{e, i}
  $$
  {{< /math >}} 

$\Rightarrow$

{{< math >}}
$$
f_{k+1}^{p}\left(\underline{x}_{k+1}\right)=\sum_{i=1}^{L} w_{k+1}^{p, i} \delta\left(\underline{x}_{k+1}-\underline{\hat{x}}_{k+1}^{p, i}\right)
$$
{{< /math >}} 

Bei gegebenen geschriebenen Systemmodell

{{< math >}}
$$
\underline{x}_{k+1} = \underline{a}_k(\underline{x}_k, \underline{w}_k)
$$
{{< /math >}} 

- Ziehe {{< math >}}$\underline{w}_k^i \sim f_k^w(\cdot)${{< /math >}} 
- {{< math >}}$\underline{\hat{x}}_{k+1}^{p, i}=\underline{a}_{k}\left(\underline{\hat{x}}_{k}^{e, i}, \underline{w}_{k}^{i}\right), i \in\left\{1, \ldots,L\right\}${{< /math >}} 



#### Filterschritt

Filterung mithilfe des probabilistischen Messmodells $f(\underline{y}_k \mid \underline{x}_k)$, falls Messung verfügbar.

Messupdate 

{{< math >}}
$$
\begin{aligned}
f_{k}^{e}\left(\underline{x}_{k}\right) &\propto f\left(\underline{y}_{k} \mid \underline{x}_{k}\right) \cdot f_{k}^{p}\left(\underline{x}_{k}\right)\\
&=f\left(\underline{y}_{k} \mid \underline{x}_{k}\right) \cdot \sum_{i=1}^{L} w_{k}^{p, i} \cdot \delta\left(\underline{x}_{k}-\underline{\hat{x}}_{k}^{p, i}\right)\\
&=\sum_{i=1}^{L} \underbrace{w_{k}^{p, i} \cdot f\left(\underline{y}_{k} \mid \hat{\underline{x}}_{k}^{p, i}\right)}_{\propto w_{k}^{e, i}} \cdot \delta(\underline{x}_{k}-\underbrace{\underline{\hat{x}}_{k}^{p, i}}_{\underline{\hat{x}}_{k}^{e, i}})
\end{aligned}
$$
{{< /math >}} 

- Positionen bleiben gleich

   {{< math >}}
  $$
  \underline{\hat{x}}_{k}^{e, i} = \underline{\hat{x}}_{k}^{p, i}
  $$
  {{< /math >}} 

- Gewichte werden adaptiert

  {{< math >}}
  $$
  w_{k}^{e, i} \propto w_{k}^{p, i} \cdot f\left(\underline{y}_{k} \mid \hat{\underline{x}}_{k}^{p, i}\right)
  $$
  {{< /math >}} 

  - Normalisierung erforderlich

    {{< math >}}
    $$
    w_{k}^{e, i}:=\frac{w_{k}^{e, i}}{\displaystyle \sum_{i} w_{k}^{e,i}}
    $$
    {{< /math >}} 

### Ablauf

Gewichte sind repräsentiert mit Kreise.

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-14%2017.37.55.png" alt="截屏2022-08-14 17.37.55" style="zoom: 33%;" />

### Vor- und Nachteile

👍 <span style="color:  ForestGreen">Vorteile</span>

- <span style="color:  ForestGreen">Problemlose Behandlung vom nichtlinearen System- und Messmodellen</span>
- <span style="color:  ForestGreen">Einstellbare Genauigkeit und Rechenaufwand nach Anzahl der Partikel balancieren</span>
- <span style="color:  ForestGreen">Extreme einfache Implementierung</span>

👎 <span style="color: Red">Nachteile</span>

- <span style="color: Red">Varianz der Samples erhöht sich mit Filterschritten</span>
- <span style="color: Red">Partikel sterben aus $\rightarrow$ Degenerierung des Filters</span>
- <span style="color: Red">Aussterben schneller, je genauer die Messung, da Likelihood schmaler ($\rightarrow$ Paradox!)</span>

## Verbesserungen

### Resampling

- Maßnahme zur Veringerung der Varianz der Samples

- Approximation der gewichteter Samples durch ungewichtete

  {{< math >}}
  $$
  f_{k}^{e}\left(\underline{x}_{k}\right)=\sum_{i=1}^{L} w_{k}^{e, i} \cdot \delta\left(\underline{x}_{k}-\underline{\hat{x}}_{k}^{e, i}\right) \approx \sum_{i=1}^{L} \frac{1}{L} \delta\left(\underline{x}_{k}-\underline{\hat{x}}_{k}^{e, i}\right)
  $$
  {{< /math >}} 

- Sehr einfaches Verfahren
  - Verwerfen von Samples mit kleinen Gewichten
  - Duplizieren von Samples mit hohen Gewichten proportional zu $w_i$ (importance resampling)
- Positionen der Samples nicht verändert
  - Veränderung der Position erst im nachfolgenden Prädiktionsschritt

### Partikelfilter mit Resampling

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-14%2018.04.26.png" alt="截屏2022-08-14 18.04.26" style="zoom:50%;" />

### Verschiedene Techniken für Resampling 

- Gegeben: $L$ Partikel mit Gewichten $w_i$
- Gesucht: $L$ Partikel mit Geweichte $\frac{1}{L}$ (gleichgewichtet)
- Achtung
  - Hier nur Vervielfältigung
  - Positionen der Partikel *unverändert*

- Kann als Kategoriale Verteilung gesehen werden

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-15%2009.43.53.png" alt="截屏2022-08-15 09.43.53" style="zoom:50%;" />

#### Rouletterad

- Resampling proportional zu der Gewichten $w_i$

- Betrachtung der kumulative Verteilung $F(i)$

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-15%2009.46.51.png" alt="截屏2022-08-15 09.46.51" style="zoom:50%;" />

- Ziehe $L$-mal Zufallszahl $u$ und wähle größte $i$ mit $F(i) \leq u$

- Entspricht Auswahl mit Rouletterad (z.B. hier $L=5$)

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-15%2009.49.11.png" alt="截屏2022-08-15 09.49.11" style="zoom:67%;" />

- Problem
  - Sehr kleine Gewichte nicht ausreichend proportional gezogen werden. 
  - Man bevorzugt ganz große Gewichte.

#### Stochastic Universal Sampling

{{% callout note %}}
Üb A13.1 (a)
{{% /callout %}}

- Bisher

  - starkes Rauschen $\rightarrow$ Auswahl variiert stark
  - Bevorzugung großer Gewichte

- Daher: Determistisches Auswahl

  - Randomisierung durch einmaliges Ziehen von $\epsilon \in [0, \frac{1}{2}]$

    {{< math >}}
    $$
    u_i = \frac{i}{L} - \epsilon \qquad i \in \{1, \dots, L\}
    $$
    {{< /math >}} 

    Für $\epsilon = \frac{1}{2L}$:

    {{< math >}}
    $$
    u_i = \frac{2i - 1}{2L}
    $$
    {{< /math >}} 

- Bsp: $L=5$

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-15%2010.01.04.png" alt="截屏2022-08-15 10.01.04" style="zoom:50%;" />

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-08-15%2010.01.22.png" alt="截屏2022-08-15 10.01.22" style="zoom: 67%;" />



## Importance Sampling

**🎯 Ziel: Berechung des Integrals**

{{< math >}}
$$
E = \int_{\mathbb{R}^N} g(\underline{x}) f(\underline{x}) d\underline{x}
$$
{{< /math >}} 

- $E$: Erwartungswert

- {{< math >}}$g(\underline{x})${{< /math >}}: nichtlineare Funktion
- {{< math >}}$f(\underline{x})${{< /math >}} : Verteilungsdichte

Falls Samples von $f(\underline{x})$ verfügbar:

{{< math >}}
$$
E=\int_{\mathbb{R}^{N}} g(\underline{x}) \sum_{i=1}^{L} w_{i} \cdot \delta\left(\underline{x}-\underline{\hat{x}}_{i}\right) d \underline{x}=\sum_{i=1}^{L} w_{i} g(\underline{x}_i)
$$
{{< /math >}} 

Aber: Oft Sampling von $f(\underline{x})$ nicht möglich 🤪

Abhilfe: **Proposal distribution** (a.k.a instrumental distribution, importance distribution) $p(\underline{x})$ mit 

{{< math >}}
$$
\operatorname{supp}\{f(\cdot)\} \subset \operatorname{supp}\{p(\cdot)\}
$$
{{< /math >}} 

($\operatorname{supp}$ stehts für support)

d.h. $p(\underline{x}) > 0$ falls $f(\underline{x}) > 0$.

$\rightarrow$ Sampling von $p(\underline{x})$ ist einfach 👏

Einsetzen:

{{< math >}}
$$
E=\int_{\mathbb{R}^{N}} g(\underline{x}) \cdot \frac{p(\underline{x})}{p(\underline{x})} \cdot f(\underline{x}) d \underline{x}=\int_{\mathbb{R}^{N}} g(\underline{x}) \cdot \frac{f(\underline{x})}{p(\underline{x})} \cdot p(\underline{x}) d \underline{x}
$$
{{< /math >}} 

{{< math >}}
$$
\begin{aligned}
p(\underline{x}) &\approx \sum_{i=1}^{L} w_{i} \cdot \delta\left(\underline{x}-\underline{\hat{x}}_{i}\right) \\\\
\Rightarrow E &\approx \int_{\mathbb{R}^{N}} g(\underline{x}) \cdot \frac{f(\underline{x})}{p(\underline{x})} \cdot \sum_{i=1}^{L} w_{i} \delta\left(\underline{x}-\underline{\hat{x}}_{i}\right) d \underline{x} \\\\
&= \sum_{i=1}^{L} g(\underline{\hat{x}}_{i}) \cdot \underbrace{\frac{f(\underline{\hat{x}}_i)}{p(\underline{\hat{x}}_{i})} \cdot w_i}_{=: w_{i}^\prime} \\\\
&= \sum_{i=1}^{L} w_{i}^\prime \cdot g(\underline{\hat{x}}_{i})
\end{aligned}
$$
{{< /math >}} 

Konvergenz gegen $E$ für $L \to \infty$

### Sequential Importance Sampling

{{% callout note %}}
Übungsblatt Aufg. 13.3
{{% /callout %}}

**🎯 Ziel: Systematische und korrekte Positionierung der Samples an Stellen hoher Likelihood vor Filterschritt**

- Verwendung von Proposal statt Systemmodell {{< math >}}$f(\underline{x}_{k+1} \mid \underline{x}_k)${{< /math >}} 

**💡Idee: Importance Sampling für {{< math >}}$f(\underline{x}_k, \underline{x}_{k-1} \mid \underline{y}_{1:k})${{< /math >}}** 

{{< math >}}
$$
f_{k}^{e}\left(\underline{x}_{k}\right)=f\left(\underline{x}_{k} \mid \underline{y}_{1: k}\right)=\int_{\mathbb{R}^{N}} \cdots \int_{\mathbb{R}^{N}} f\left(\underline{x}_{1: k} \mid \underline{y}_{1 : k}\right) d \underline{x}_{1: k-1}
$$
{{< /math >}} 

Proposal: {{< math >}}$p\left(\underline{x}_{1: k} \mid \underline{y}_{1 : k}\right)${{< /math >}} hängt auch von {{< math >}}$\underline{y}_k${{< /math >}} ab.

Damit:

{{< math >}}
$$
f_{k}^{e}\left(\underline{x}_{k}\right) = \int_{\mathbb{R}^{N}} \cdots \int_{\mathbb{R}^{N}} \underbrace{\frac{f\left(\underline{x}_{1: k} \mid \underline{y}_{1 : k}\right)}{p\left(\underline{x}_{1: k} \mid \underline{y}_{1 : k}\right)}}_{=: w_k^{e, i}} p\left(\underline{x}_{1: k} \mid \underline{y}_{1 : k}\right) d \underline{x}_{1: k-1}
$$
{{< /math >}} 

Annahme: Proposal ist faktorisierbar

{{< math >}}
$$
p\left(\underline{x}_{1: k} \mid \underline{y}_{1: k}\right)=p\left(\underline{x}_{k} \mid \underline{x}_{1: k - 1}, \underline{y}_{1: k}\right) \cdot p\left(\underline{x}_{1: k -1} \mid \underline{y}_{1: k - 1}\right)
$$
{{< /math >}} 

Für gegebenes Sample {{< math >}}$\underline{\hat{x}}_{k-1}^{e, i}${{< /math >}} aus letzten Zeitpunkt, ziehe

{{< math >}}
$$
\underline{x}_{k}^{e, i} \sim P\left(\underline{x}_{k} \mid \hat{\underline{x}}_{k-1}^{e, i}, \underline{y}_{k}\right)
$$
{{< /math >}} 

Jetzt umschreiben von {{< math >}}$\frac{f\left(\underline{x}_{1: k} \mid \underline{y}_{1 : k}\right)}{p\left(\underline{x}_{1: k} \mid \underline{y}_{1 : k}\right)}${{< /math >}} 

- Zähler

  {{< math >}}
  $$
  \begin{aligned}
  f\left(\underline{x}_{1: k} \mid \underline{y}_{1: k}\right) &\propto f\left(\underline{y}_{k} \mid \underline{x}_{1: k}, \underline{y}_{1: k - 1}\right) \cdot f\left(\underline{x}_{1: k} \mid \underline{y}_{1: k-1}\right)\\
  &=f\left(\underline{y}_{k} \mid \underline{x}_{k}\right) \cdot f\left(\underline{x}_{k} \mid \underline{x}_{1:k-1}, \underline{y}_{1:k-1}\right) \cdot f\left(\underline{x}_{1:k-1} \mid \underline{y}_{1: k-1}\right)\\
  &=f\left(\underline{y}_{k} \mid \underline{x}_{k}\right) \cdot f\left(\underline{x}_{k} \mid \underline{x}_{k-1}\right) \cdot f\left(\underline{x}_{1: k-1} \mid \underline{y}_{1: k \cdot 1}\right)
  \end{aligned}
  $$
  {{< /math >}} 

- Nenner

  {{< math >}}
  $$
  p\left(\underline{x}_{1: k} \mid \underline{y}_{1: k}\right)=p\left(\underline{x}_{k} \mid \underline{x}_{1: k - 1}, \underline{y}_{1: k}\right) \cdot p\left(\underline{x}_{1: k -1} \mid \underline{y}_{1: k - 1}\right)
  $$
  {{< /math >}} 

$\Rightarrow$ Gewicht für Position $i$:

{{< math >}}
$$
w_k^{e, i} = \frac{f\left(\underline{\hat{x}}_{1: k} \mid \underline{y}_{1 : k}\right)}{p\left(\underline{\hat{x}}_{1: k} \mid \underline{y}_{1 : k}\right)} \propto \frac{f\left(\underline{y}_{k} \mid \underline{x}_{k}^i\right) \cdot f\left(\underline{x}_{k}^i\mid \underline{x}_{k-1}^i\right)}{p\left(\underline{x}_{k}^i \mid \underline{x}_{1: k - 1}^i, \underline{y}_{1: k}\right)} \cdot \underbrace{\frac{f\left(\underline{x}_{1: k-1}^i \mid \underline{y}_{1: k \cdot 1}\right)}{p\left(\underline{x}_{1: k -1}^i \mid \underline{y}_{1: k - 1}\right)}}_{=w_{k-1}^{e, i}}
$$
{{< /math >}} 

mit Normalisierung.

### Spezielle Proposal

#### **Standard Proposal**

Einfache Verwendung der Systemdynamik:

{{< math >}}
$$
p\left(\underline{x}_{k} \mid \underline{x}_{k-1}, \underline{y}_{k}\right) \stackrel{!}{=} f\left(\underline{x}_{k} \mid \underline{x}_{k-1}\right)
$$
{{< /math >}} 

Es ergibt sich

{{< math >}}
$$
w_{k}^{e, i} \propto \frac{f\left(\underline{y}_{k} \mid \hat{\underline{x}}_{k}^{i}\right) \cdot f\left(\hat{\underline{x}}_{k}^{i} \mid \hat{\underline{x}}_{k-1}^{i}\right)}{p\left(\underline{\hat{x}}_{k}^{i} \mid \hat{\underline{x}}_{k-1}^{i}, \underline{y}_k\right)} \cdot w_{k-1}^{e, i}=f\left(\underline{y}_{k} \mid \hat{\underline{x}}_{k}^{i}\right) \cdot w_{k - 1}^{e, i}
$$
{{< /math >}} 

Sehr einfach, aber KEINE verbesserte Performance 🤪

#### **Optimales Proposal**

Verwende

{{< math >}}
$$
\begin{aligned}
p\left(\underline{x}_{k} \mid \underline{x}_{k-1}, \underline{y}_{k}\right) &=f\left(\underline{x}_{k} \mid \underline{x}_{k-1}, \underline{y}_{k}\right) \\
& \propto f\left(\underline{y}_{k} \mid \underline{x}_{k}\right) \cdot f\left(\underline{x}_{k} \mid \underline{x}_{k-1}\right)
\end{aligned}
$$
{{< /math >}} 

Damit wäre

{{< math >}}
$$
w_k^{e, i} = w_{k-1}^{e, i}
$$
{{< /math >}} 

Wird als **optimales Proposal** genannt

- Minimierte Varianz der Gewicht
- Varianz der Gewicht ändert sich nicht

‼️ Aber typischerweise können wir hiervon nicht samplen $\rightarrow$ Nur in Spezialfällen verwendbar.

## Einfaches praktisches Filter: SIR-Partikelfilter

- Standard Proposal

- Resampling nach jedem Filterschritt

- Da Gewichte in Prädiktionsschritt unverändert

  {{< math >}}
  $$
  w_{k-1}^{e, i} = \frac{1}{L}
  $$
  {{< /math >}} 

  und damit

  {{< math >}}
  $$
  w_k^{e, i} \propto f(\underline{y}_k \mid \underline{\hat{x}}_k^i)
  $$
  

  {{< /math >}} 

- Einfachstes praktisches Partikelfilter

- Algorithm

  - Input 

    - {{< math >}}$\underline{\hat{x}}_{k-1}^{e, i}${{< /math >}} 
    
    - {{< math >}}$w_{k-1}^{e, i} = \frac{1}{L},  i \in \{1, \dots, L\}${{< /math >}} 
    
  - For {{< math >}}$i \in \{1, \dots, L\}${{< /math >}} 

    - Ziehe 

      {{< math >}}
      $$
      \underline{\hat{x}}_{k-1}^{e, i} \sim f(\underline{x}_k \mid \underline{\hat{x}}_{k-1}^i)
      $$
      {{< /math >}} 
  
    - Gewichtung 

      {{< math >}}
      $$
      w_k^{e, i} \propto f(\underline{y}_k \mid \underline{\hat{x}}_{k}^{e, i})
      $$
      {{< /math >}} 
  
  - Normalisierung Gewichte $w_k^{e, i}$

  - Resampling 

    {{< math >}}
    $$
    \underline{\hat{x}}_{k}^{e, i}, \quad w_{k}^{e, i} = \frac{1}{L} \qquad  i \in \{1, \dots, L\}
    $$
    {{< /math >}} 