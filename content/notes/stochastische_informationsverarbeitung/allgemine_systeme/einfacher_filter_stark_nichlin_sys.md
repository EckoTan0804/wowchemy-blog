---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 591
# ============================================================

# ========== Basic metadata ==========
title: Einfache Filter für stark nichtlineare Systeme
date: 2022-08-09
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

## Nutzung „einfacher“ Filter für stark nichtlineare Systeme

2 Variante

- Approximation der Zustandsdichten durch [Gaussian Mixture](#gaussian-mixture-filter) $\rightarrow$ Bank von nichtlinearen Kalman Filter für Prädiktion und Filterung
- Approximation aller Dichten durch wertdiskrete Repräsentation $\rightarrow$ [Wertdiskreter Filter](#rasterbasierte-filter)



## Gaussian Mixture Filter

### Motivation

Approximation der Zustandsschätzung durch Gaussian Mixture

{{< math >}}
$$
f(\underline{x})=\sum_{i=1}^{L} w_{i} \mathcal{N}\left(\underline{x}-\underline{\hat{x}}_{i}, C_{i}\right)
$$
{{< /math >}} 

mit

{{< math >}}
$$
\begin{aligned}
&w_{i} \geqslant 0, \quad i \in\{1, \ldots,L\} \\
&\sum_{i=1}^{L} w_{i}=1
\end{aligned}
$$
{{< /math >}} 

(Damit ist Gaussian Mixture für beliebige $L$ eine gültige Dichte)

Parameter

- Gewichtsvektor $\underline{w} = [w_1, \dots, w_L]^T$
- Mittelwerte $\underline{\hat{x}}_1, \dots, \underline{\hat{x}}_L$
- Kovarianzmatrizen $C_1, \dots, C_L$

Gaussian Mixtures sind universelle Approximators. Falls $L$ genügend groß, kann jede Dichte beliebig genau approximiert werden.

### Vorgehen

- **Ziel: Nutzung der Erkenntnisse zum Kalman Filter für schwach nichtlineare Systeme $\rightarrow$ stark nichtlinearer Fall**

- Deshalb: Individuelle Verarbeitung der einzelnen Komponente $i (also Vernachlässigung der Überlappung) 

- Ergibt Bank von nichtlinearen Kalman Filter, die parallel arbeiten.

- Funktioniert besonders gut, wenn
  - Überlappung der Komponenten klein
  - einzelne Komponenten schmal (induzierte Nichtlinearität)

### Prädiktionsschritt

Systemmodell

{{< math >}}
$$
\underline{x}_{k+1} = \underline{a}_k(\underline{x}_k) + \underline{w}_k
$$
{{< /math >}} 

Einfache Schreiweise:

{{< math >}}
$$
\underline{z} = \underline{a}(\underline{x}) + \underline{w} \quad \underline{w} \sim \text{Gauß}
$$
{{< /math >}} 

**💡Kernidee: Aufspaltung der Chapman-Kolmogorov-Gleichung**

{{< math >}}
$$
\begin{aligned}
f^{p}(\underline{z})&=\int_{\mathbb{R}^{N}} f^{w}(\underline{z}-\underline{a}(\underline{x})) \cdot f^{e}(\underline{x}) d \underline{x}\\
&=\int_{\mathbb{R}^{N}} f^{w}(\underline{z}-\underline{a}(\underline{x})) \cdot\left[\sum_{i=1}^{c} w_{i} \mathcal{N} \left(\underline{x}-\underline{\hat{x}}_{i}^{e}, C_{i}^{e}\right)\right] d \underline{x}\\
&=\sum_{i=1}^{L} w_{i} \underbrace{\int_{\mathbb{R}^{N}} f^{w}(\underline{z}-\underline{a}(\underline{x})) \mathcal{N}\left(\underline{x}-\underline{\hat{x}}_{i}^{e}, C_{i}^{e}\right) d \underline{x}}_{\approx \mathcal{N}(\underline{z} - \underline{z}_{i+1}^p, C_{i+1}^p)}
\end{aligned}
$$
{{< /math >}} 

{{< math >}} $\underline{z}_{i+1}^p, C_{i+1}^p${{< /math >}} durch Anwendung nichtlinearer Kalman Filter 

### Filterschritt

Messmodell:

{{< math >}}
$$
\underline{y}_k=\underline{h}_{k}\left(\underline{x}_{k}\right)+\underline{v}_{u}
$$
{{< /math >}} 

Einfache Schreibweise:

{{< math >}}
$$
\underline{y}=\underline{h}_{k}(\underline{x})+\underline{v} \quad \underline{v} \sim \operatorname{Gauß}
$$
{{< /math >}} 

Filterschritt

{{< math >}}
$$
\begin{aligned}
f^{e}(\underline{x}) &=c^{e} f^{v}\left(\underline{\hat{y}}-\underline{h}(\underline{x})\right) \cdot \sum_{i=1}^{L} w_{i} \mathcal{N}\left(\underline{x}-\hat{\underline{x}}_{i}^{p}, C_{i}^{p}\right) \\
&=c^{e} \sum_{i=1}^{L} w_{i} \underbrace{f^{v}(\underline{\hat{y}}-\underline{h}(\underline{x})) \cdot \mathcal{N} \left(\underline{x}-\underline{\hat{x}}_{i}^{p}, C_{i}^{p}\right)}_{\approx k_i \mathcal{N} \left(\underline{x}-\underline{\hat{x}}_{i}^{e}, C_{i}^{e}\right)} \\
&= c^e \sum_{i=1}^{L} w_{i} k_i \mathcal{N} \left(\underline{x}-\underline{\hat{x}}_{i}^{e}, C_{i}^{e}\right)
\end{aligned}
$$
{{< /math >}} 

{{< math >}}$\underline{\hat{x}}_{i}^{e}, C_{i}^{e}${{< /math >}} durch nichtlinearen Kalman Filter bestimmen.

## Rasterbasierte Filter

### Rasterbasierte Repräsentation von Dichten

Zunächst: Skalarer Fall

- Gegeben: Dichte $f(x), x \in \mathbb{R}$ 

- Gescuht: Wertdiskrete Repräsentation 

  {{< math >}}
  $$
  \underline{\eta} \in \mathbb{R}_{+}^{L}, \quad \underline{\mathbf{1}}^{\top} \cdot \underline{\eta}=1 \text{ (Normalisierung)}
  $$
  {{< /math >}} 

### Rasterbasierter Filter- und Prädiktionsschritt

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-rasterbasierte_repr_dichte.drawio.png" alt="allg_sys-rasterbasierte_repr_dichte.drawio" style="zoom:67%;" />

{{< math >}}
$$
\underline{\eta}=\left[\begin{array}{c}
\eta
_{1} \\
\eta
_{2} \\
\vdots \\
\eta
_{L}
\end{array}\right]
$$
{{< /math >}} 

Annahme: Repräsentiere $\eta_i$ in **Mitte** jedes Intervalls durch Dirac'sche Deltafunktion

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-Copy%20of%20rasterbasierte_repr_dichte.drawio.png" alt="allg_sys-Copy of rasterbasierte_repr_dichte.drawio" style="zoom:67%;" />

Kriterium: Integralwerte sollen gleich sein.

{{< math >}}
$$
\begin{aligned}
&\int_{x_{i-1}}^{x_i}f(x)dx \overset{!}{=} \underbrace{\int_{x_{i-1}}^{x_i} \eta_i \cdot \delta(x - \frac{x_i + x_{i-1}}{2}) dx}_{=\eta_i}   \\
&\Rightarrow \eta_i \propto \int_{x_{i-1}}^{x_i}f(x)dx \quad i \in \{1, \dots, L\}
\end{aligned}
$$
{{< /math >}} 

Normalisierung erfordlich:

{{< math >}}
$$
\eta_{i}:=\frac{\eta_{i}}{\sum_{i} \eta_{i}} \quad i \in\left\{1, \dots, L\right\}
$$
{{< /math >}} 

In vielen Fällen, Integral über $f(x)$ nicht analytisch lösbar. $\Rightarrow$ Integration zu aufwändig.

Alternative: Stückweise Konstant Approximation von $f(x)$

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-rasterbasierte_repr_dichte_stueckweise_konstant_approx.drawio.png" alt="allg_sys-rasterbasierte_repr_dichte_stueckweise_konstant_approx.drawio" style="zoom:67%;" />

- Aber: Optimaler Vergleich erfordert auch Integration

- Deshalb: Verwendung des Dichtwerts an Stelle

  {{< math >}}
  $$
  h_i = f(\frac{x_i + x_{i-1}}{2})
  $$
  {{< /math >}} 

  Damit

  {{< math >}}
  $$
  \begin{aligned}
  &\int_{x_{i-1}}^{x_i} f(x) dx \approx \int_{x_{i-1}}^{x_i} h_i dx = h_i(\underbrace{x_i - x_{i-1}}_{=\Delta}) \\
  & \Rightarrow \eta_i \propto \Delta \cdot h_i = \Delta \cdot f(\frac{x_i + x_{i-1}}{2})
  \end{aligned}
  $$
  {{< /math >}} 

  mit Normalisierung

#### **Rasterbasierter Filterschritt**

Generatives Modell

{{< math >}}
$$
y = h(x, v)
$$
{{< /math >}} 

Kovertiere in probabilitisches Modell $f(y \mid x)$

Messung $\hat{y}$ sidn nicht wertdiskret $\rightarrow$ Quantisierung von $f(\hat{y} \mid x) = f^L(x)$

Da $f(\hat{y} \mid x)$ i.d.R. nicht analytisch integrierbar $\rightarrow$

{{< math >}}
$$
\eta_{i}^{L} \propto \Delta f^{L}\left(\frac{x_{i}+x_{i-1}}{2}\right) \quad i \in\{1, \dots,L\}
$$
{{< /math >}} 

und Normalisierung.

Für gegebene Dichte $\underline{\eta}^{p}=\left[\eta_{1}^{p}, \eta_{2}^{p}, \ldots, \eta_{L}^{p}\right]^{\top}$

{{< math >}}
$$
\underline{\eta}^{e} \propto \underline{\eta}^{L} \odot \underline{\eta}^{p}
\tag{posteriore Verteilung}
$$
{{< /math >}} 

#### **Rasterbasierter Prädiktionsschritt**

Generatives Modell

{{< math >}}
$$
x_{k+1} = a_k(x_k, w_k) 
$$
{{< /math >}} 

Einfache Schreibweise

{{< math >}}
$$
z = a(x, w)
$$
{{< /math >}} 

probabilitisches Modell: $f(z \mid x)$

Hier müssen wir für skalare Zustände eine 2D-Dichte quantisieren.

$\Rightarrow$ Es ergibt sich eine Matrix

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-rasterbasiert_prädiktion.drawio.png" alt="allg_sys-rasterbasiert_prädiktion.drawio" style="zoom:67%;" />

{{< math >}}
$$
A_{i j} \propto f\left(\frac{z_{j}+z_{j-1}}{2}, \frac{x_{i}+x_{i-1}}{2}\right)
$$
{{< /math >}} 

Normalisierung

- Es handelt sich um Transitionsmatrix
- Stochastische Matrix, Zeilensumme = 1
- {{< math >}}$A_{i j}:=\displaystyle\frac{A_{i j}}{\sum_{i=1}^{L} A_{i j}}, i \in\{1, \ldots,L\}${{< /math >}} 

Gegeben:

- Transitionsmatrix $A \in \mathbb{R}_{+}^{L \times L}$
- Schätzung aus letzen Filterschritt $\underline{\eta}^e \in \mathbb{R}_{+}^{L}$ 

Ergebnis des Prädiktionsschritts:

{{< math >}}
$$
\underline{\eta}^p = A^\top \underline{\eta}^e
$$
{{< /math >}} 

Aufwändiger als Filterschritt 🤪

### Erweiterung Prädiktionsschritt

Bisher angenommen: Raster für $z$ (also $x_{k+1}$) schon bekannt/fest

Das ist leider nicht praxisgerecht, da sich Wertbereich aus Abbildung ergibt.

Speizialfall: Lineares System mit additives Rauschen (i. Allg. schwieriger)

{{< math >}}
$$
z = \underbrace{x + u}_{z^\prime} + w \quad w \sim f^w(w)
$$
{{< /math >}} 

- Zwischengröße $z^\prime$: Nutze Eingang $\hat{u}$, um Raster zu verschieben (bewegliches Raster)

  {{< math >}}
  $$
  z_i^\prime = x_i + \hat{u} \quad i \in \{1, \dots, L\}
  $$
  {{< /math >}} 

  Wir setzen $z_i = z_i^\prime$

Danach Faltung mit $f_w(w)$:

{{< math >}}
$$
fz\left(z^{\prime}\right)=f^{w}\left(z-z^{\prime}\right)
$$
{{< /math >}} 

Dann Quantisierung von $f(z \mid z^\prime) \Rightarrow$ 

{{< math >}}
$$
\begin{aligned}
A_{i j} &=f^{w}\left(\frac{z_{j}+z_{j - 1}}{2} \mid \frac{z_{i}^{\prime}+z_{i - 1}^\prime}{2}\right) \\
A_{i j}&=f^{\omega}\left(\frac{1}{2}\left[z_{i}+z_{j-1}-\left(z_{i}^{\prime}+z_{i-1}^{\prime}\right)\right]\right)
\end{aligned}
$$
{{< /math >}} 

Wir wissen

{{< math >}}
$$
\begin{aligned}
\frac{z_{i}+z_{j-1}}{2}&=\frac{2 j-1}{2} \Delta+z_{0} \\
\frac{z_{i}^{\prime}+z_{i-1}^{\prime}}{2}&=\frac{z_{i}-1}{2} \Delta+z_{0}^{\prime} \\
\Rightarrow A_{ij} &= f^w(\Delta[j - i]), \text{ falls }  z_0 = z_0^\prime
\Rightarrow j - i \in \{-(L-1), \dots, -1, 0, 1, \dots, L - 1\}
\end{aligned}
$$
{{< /math >}} 

Vorabdiskretisierung von $f^w(\cdot)$

![allg_sys-Vorabdiskretisierung.drawio](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-Vorabdiskretisierung.drawio.png)

Eintragen der Werte in Transitionsmatrix $A$ mit $A_{ij} = f^w(\Delta(j-i))$

Dann Berechnung der Posteriro wie gehabt.

### Rekonstruktion kontinuierlicher Dichten

Ergebnis von Prädiktion und Filterung in *wertdiskreter* Form $\underline{\eta} \in \mathbb{R}_+^L$

Berechnung von Kenngröße einfach, dazu Positionen erforderlich

Erwartungswert

{{< math >}}
$$
\begin{aligned}
\hat{x} &=\int_{\mathbb{R}} x \sum_{i=1}^{2} \eta_{i} \int\left(x-\frac{x_{i}+x_{i-1}}{2}\right) d x \\
&=\sum_{i=1}^{L} \eta_{i} \frac{x_{i}+x_{i-1}}{2} \quad \mid \frac{x_{i}+x_{i-1}}{2}=\frac{2 i-1}{2} \Delta+x_{0} \\
&= \sum_{i=1}^{L} \eta_{i} (\frac{2i-1}{2} \Delta + x_0)
\end{aligned}
$$
{{< /math >}} 

Analog für Varianz.

Gesucht: kontinuierliche Rekonstruktion $f(x)$ aus $\eta$

Als Dirac Mixture

{{< math >}}
$$
f(x) \approx \sum_{i=1}^{L} \eta_{i} \delta\left(x-\frac{x_{i}+x_{i-1}}{2}\right)
$$
{{< /math >}} 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-Rekonstruktion.drawio.png" alt="allg_sys-Rekonstruktion.drawio" style="zoom:67%;" />

Verschiedenen Möglichkeiten der Interpolation

- Stückweise Konstante Interpolation

  {{< math >}}
  $$
  \int_{x_{i-1}}^{x_{i}} h_{i} d x \overset{!}{=} \int_{x_{i=1}}^{x_{i}} u_{i} \delta() d x \Rightarrow h_{i}=\frac{\eta_{i}}{\Delta}
  $$
  {{< /math >}} 

- Stetige, stückweise lineare Interpolation

  {{< math >}}
  $$
  (t_i + t_{i-1}) \frac{\Delta}{2} = \eta_i
  $$
  {{< /math >}} 

  und weitere Bedingung

  {{< math >}}
  $$
  t_0 = t_1
  $$
  

  {{< /math >}} 

### Erweiterungen

Mehrdimensional Fall: $\underline{x} \in \mathbb{R}^N$

- Filterschritt analog
- Prädiktionsschritt: $f(\underline{z} \mid \underline{x})$ nun von $\mathbb{R}^N$aud $\mathbb{R}^N \Rightarrow A \in \mathbb{R}^{2N}$  

Lösung

- Bewegliches Raster für nichtlineare Systemmodelle
- Adaptive Auflösung eines äquidistanten / homogenen Rasters
- Inhomoge Raster $\rightarrow$ variable Auflösung
- Effiziente Implementierung, z.B.  dünn besetzte Matrizen ($0$ nicht explizit dargestellt)