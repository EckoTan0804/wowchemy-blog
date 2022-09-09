---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 740
# ============================================================

# ========== Basic metadata ==========
title: Schwach nichtlineare wertekontinuierliche Systeme
date: 2022-08-24
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

## Lineare Vs. Nichtlineare Systeme

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-7btt{border-color:inherit;font-weight:bold;text-align:center;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow"></th>
    <th class="tg-7btt">Linear</th>
    <th class="tg-7btt">Nichtlinear</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-7btt">Systemabbildung</td>
    <td class="tg-c3ow">$\underline{x}_{k+1} = \mathbf{A}_k \underline{x}_k + \mathbf{B}_k (\underline{u}_k + \underline{w}_k)$</td>
    <td class="tg-c3ow">$\underline{x}_{k+1} = \underline{a}_k(\underline{x}_k, \underline{u}_k, \underline{w}_k)$</td>
  </tr>
  <tr>
    <td class="tg-7btt">Messabbildung</td>
    <td class="tg-c3ow">$\underline{y}_{k} = \mathbf{H}_k \underline{x}_k + \underline{v}_k$</td>
    <td class="tg-c3ow">$\underline{y}_k = \underline{h}_k (\underline{x}_k, \underline{v}_k)$</td>
  </tr>
</tbody>
</table>

## Extended Kalman Filter (EKF)

💡 Idee: Linearisierung mit Tylorentwicklung 1. Ordnung um die beste verfügbare Schätzung, um den (linear) Kalman-Filter zu vewenden.

- Systemabbildung

  {{< math >}}
  $$
  \underline{a}_{k}\left(\underline{x}_{k}, \underline{u}_{k}\right) \approx \underbrace{\underline{a}_{k}\left(\underline{\overline{x}}_k, \underline{\overline{u}}_k\right)}_{\text{Nomialteil}}+\underbrace{\mathbf{A}_{k}\left(\underline{x}_k-\underline{\overline{x}}_k\right)+\mathbf{B}_{k}\left(\underline{u}_{k}-\underline{\overline{u}}_k\right)}_{\text{Differentialteil}}
  $$
  {{< /math >}} 

- Messabbildung

  {{< math >}}
  $$
  \underline{h}_{k}\left(\underline{x}_{k}, \underline{v}_{k}\right) \approx \underbrace{\underline{h}_{k}\left(\underline{\bar{x}}_{k}, \underline{\bar{v}}_{k}\right)}_{\text{Nomialteil}}+ \underbrace{\mathbf{H}_{k} \cdot \left(\underline{x}_{k}-\underline{\bar{x}}_{k}\right)+\mathbf{L}_{k} \cdot\left(\underline{v}_{k}-\underline{\bar{v}}_{k}\right)}_{\text{Differentialteil}}
  $$
  {{< /math >}} 

{{% callout note %}}

Üb 7, A2

{{% /callout %}}

Prädiktion

- Berechnung Erwartungswert über nichtlineare Funktion

  {{< math >}}
  $$
  \underline{\hat{x}}_{k+1}^{p}=\underline{a}_{k}\left(\underline{\hat{x}}_{k}^{e}, \hat{\underline{u}}_{k}\right)
  $$
  {{< /math >}} 

- Berechnung Kovarianzmatrix über die Linearisierung

  {{< math >}}
  $$
  \mathbf{C}_{k+1}^{p} \approx \mathbf{A}_{k} \mathbf{C}_{k}^{e} \mathbf{A}_{k}^{\top}+\mathbf{C}_{k}^{w^{\prime}}=\mathbf{A}_{k} \mathbf{C}_{k}^{e} \mathbf{A}_{k}^{\top}+\mathbf{B}_{k}  \mathbf{C}_{k}^{w} \mathbf{B}_{k}^{\top}
  $$
  {{< /math >}} 

  mit 

  {{< math >}}
  $$
  \mathbf{A}_k = \left.\frac{\partial \underline{a}_{k}\left(\underline{x}_{k}, \underline{u}_{k}\right)}{\partial \underline{x}_{k}^{\top}}\right|_{\underline{x}_{k}=\underline{\hat{x}}_{k-1}^{e}, \underline{u}_{k}=\hat{\underline{u}}_{k}} \qquad
  \mathbf{B}_k = \left.\frac{\partial \underline{a}_{k}\left(\underline{x}_{k}, \underline{u}_{k}\right)}{\partial \underline{u}_{k}^{\top}}\right|_{\underline{x}_{k}=\underline{\hat{x}}_{k-1}^{e}, \underline{u}_{k}=\hat{\underline{u}}_{k}}
  $$
  {{< /math >}} 

Filterung

- Linearisierung um $\underline{x}_k$ und $\underline{v}_k$ 

  {{< math >}}
  $$
  \mathbf{H}_{k}=\left.\frac{\partial \underline{h}_{k}\left(\underline{x}_{k}, \underline{v}_{k}\right)}{\partial \underline{x}_{k}^{\top}}\right|_{\underline{x}_{k}=\underline{\hat{x}}_{k}^{p}, \underline{v}_{k}=\underline{\hat{v}}_{k}} \qquad
  \mathbf{L}_{k}=\left.\frac{\partial \underline{h}_{k}\left(\underline{x}_{k}, \underline{v}_{k}\right)}{\partial \underline{v}_{k}^{\top}}\right|_{\underline{x}_{k}=\underline{\hat{x}}_{k}^{p}, \underline{v}_{k}=\underline{\hat{v}}_{k}}
  $$
  {{< /math >}} 

- KF Filterung schriit mit Linearisierung

  {{< math >}}
  $$
  \begin{aligned}
  \mathbf{K}_{k}&=\mathbf{C}_{k}^{p} \mathbf{H}_{k}^{\top}\left(\mathbf{L}_{k} \mathbf{C}_{k}^{v} \mathbf{L}_{k}^{\top}+\mathbf{H}_{k} \mathbf{C}_{k}^{p} \mathbf{H}_{k}^{T}\right)^{-1} \\\\
  \hat{\underline{x}}_{k}^{e}&=\hat{\underline{x}}_{k}^{p}+\mathbf{K}_{k}\left[\hat{\underline{y}}_{k}-\underline{h}_{k}\left(\hat{\underline{x}}_{k}^{p}, \hat{\underline{v}}_{k}\right)\right]  \overset{\underline{v} \text{ mittelwertfrei}}{=} \hat{\underline{x}}_{k}^{p}+\mathbf{K}_{k}\left[\hat{\underline{y}}_{k}-\underline{h}_{k}\left(\hat{\underline{x}}_{k}^{p}, 0\right)\right]\\\\
  \mathbf{C}_{k}^{e}&=\mathbf{C}_{k}^{p}-\mathbf{K}_{k} \mathbf{H}_{k} \mathbf{C}_{k}^{p} = (\mathbf{I} - \mathbf{K}_{k} \mathbf{H}_{k})\mathbf{C}_{k}^{p}
  \end{aligned}
  $$
  {{< /math >}} 

## (Linear) KF vs. EKF

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-1wig{font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-fymr{border-color:inherit;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-fymr">(Linear) KF</th>
    <th class="tg-fymr">EKF</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fymr">Prädiktion</td>
    <td class="tg-0pky">$\underline{\hat{x}}_k^p = \mathbf{A}_{k-1}\underline{\hat{x}}_{k-1}^e + \mathbf{B}_{k-1} \underline{\hat{u}}_{k-1}$<br>$\mathbf{C}_k^p = \mathbf{A}_{k-1} \mathbf{C}_{k-1}^e A_{k-1}^\top + \mathbf{B}_{k-1} \mathbf{C}_{k-1}^w \mathbf{B}_{k-1}^\top$</td>
    <td class="tg-0pky">$\underline{\hat{x}}_{k+1}^{p}=\underline{a}_{k}\left(\underline{\hat{x}}_{k}^{e}, \hat{\underline{u}}_{k}\right)$<br>$\mathbf{C}_{k+1}^{p} \approx \mathbf{A}_{k} \mathbf{C}_{k}^{e} \mathbf{A}_{k}^{\top}+\mathbf{C}_{k}^{w^{\prime}}=\mathbf{A}_{k} \mathbf{C}_{k}^{e} \mathbf{A}_{k}^{\top}+\mathbf{B}_{k}  \mathbf{C}_{k}^{w} \mathbf{B}_{k}^{\top}$</td>
  </tr>
  <tr>
    <td class="tg-fymr">Filterung</td>
    <td class="tg-0pky">$\mathbf{K}_k = \mathbf{C}_k^p \mathbf{H}_k^\top (\mathbf{C}_k^v + \mathbf{H}_k \mathbf{C}_k^p \mathbf{H}_k ^\top)^{-1}$<br>$\underline{\hat{x}}_k^e = \underline{\hat{x}}_k^p + \mathbf{K}_k(\underline{\hat{y}}_k - \mathbf{H}_k \underline{\hat{x}}_k^p)$<br>$\mathbf{C}_k^e = (\mathbf{I} - \mathbf{K}_k\mathbf{H}_k)\mathbf{C}_k^p$</td>
    <td class="tg-0pky">$\begin{aligned}<br>  \mathbf{K}_{k}&amp;=\mathbf{C}_{k}^{p} \mathbf{H}_{k}^{\top}\left(\mathbf{L}_{k} \mathbf{C}_{k}^{v} \mathbf{L}_{k}^{\top}+\mathbf{H}_{k} \mathbf{C}_{k}^{p} \mathbf{H}_{k}^{T}\right)^{-1} \\<br>  \hat{\underline{x}}_{k}^{e}&amp;=\hat{\underline{x}}_{k}^{p}+\mathbf{K}_{k}\left[\hat{\underline{y}}_{k}-\underline{h}_{k}\left(\hat{\underline{x}}_{k}^{p}, \hat{\underline{v}}_{k}\right)\right] \\<br>  \mathbf{C}_{k}^{e}&amp;=\mathbf{C}_{k}^{p}-\mathbf{K}_{k} \mathbf{H}_{k} \mathbf{C}_{k}^{p} = (\mathbf{I} - \mathbf{K}_{k} \mathbf{H}_{k})\mathbf{C}_{k}^{p}<br>  \end{aligned}$</td>
  </tr>
  <tr>
    <td class="tg-1wig">Auxiliary</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">$\mathbf{A}_k = \left.\frac{\partial \underline{a}_{k}\left(\underline{x}_{k}, \underline{u}_{k}\right)}{\partial \underline{x}_{k}^{\top}}\right|_{\underline{x}_{k}=\underline{\hat{x}}_{k-1}^{e}, \underline{u}_{k}=\hat{\underline{u}}_{k}}$<br>$\mathbf{B}_k = \left.\frac{\partial \underline{a}_{k}\left(\underline{x}_{k}, \underline{u}_{k}\right)}{\partial \underline{u}_{k}^{\top}}\right|_{\underline{x}_{k}=\underline{\hat{x}}_{k-1}^{e}, \underline{u}_{k}=\hat{\underline{u}}_{k}}$<br>$\mathbf{H}_{k}=\left.\frac{\partial \underline{h}_{k}\left(\underline{x}_{k}, \underline{v}_{k}\right)}{\partial \underline{x}_{k}^{\top}}\right|_{\underline{x}_{k}=\underline{\hat{x}}_{k}^{p}, \underline{v}_{k}=\underline{\hat{v}}_{k}}$<br>$\mathbf{L}_{k}=\left.\frac{\partial \underline{h}_{k}\left(\underline{x}_{k}, \underline{v}_{k}\right)}{\partial \underline{v}_{k}^{\top}}\right|_{\underline{x}_{k}=\underline{\hat{x}}_{k}^{p}, \underline{v}_{k}=\underline{\hat{v}}_{k}}$</td>
  </tr>
</tbody>
</table>

### Probleme

- Berechnung der posteriore Verteilung nur gut für “schwache” Nichtlinearität
- Linearisierung nur um einen Punkt

- Linearisiertes System ist i.A. zeitvariant, auch wenn originalsytstem zeitinvariant ist, da Linearisierung vom Schätzwert abhängt.

## Kalman Filter in probabilistischer Form



**Filterung**

(Annahme: {{< math >}}$\underline{x}_k${{< /math >}} und {{< math >}}$\underline{y}_k${{< /math >}} sind gemeinsam Gaußverteilt)

1. Define {{< math >}}$\underline{z}:=\left[\begin{array}{l}
   \underline{x} \\
   \underline{y}
   \end{array}\right]${{< /math >}}

2. Mittelwert und Varianz von $\underline{z}$ berechnen.

   {{< math >}}


$$
   \underline{\mu}_z=\left[\begin{array}{l}
   \underline{\mu}_x \\
   \underline{\mu}_y
   \end{array}\right]=\frac{1}{L}\sum_{i=1}^L\left[\begin{array}{l}
   \underline{x}_i \\
   \underline{y}_i
   \end{array}\right],  \quad \mathbf{C}_{z} = \frac{1}{L}\sum_{i=1}^L(\underline{z}_i - \underline{\mu}_z)(\underline{z}_i - \underline{\mu}_z)^\top = \left[\begin{array}{ll}
   \mathbf{C}_{x x} & \mathbf{C}_{x y} \\
   \mathbf{C}_{y x} & \mathbf{C}_{y y}
   \end{array}\right]
$$
   {{< /math >}} 

3. Filterung in probabilistischer Form mit Messung {{< math >}}$\hat{\underline{y}}${{< /math >}}

   {{< math >}}
   $$
   \begin{aligned}
   \underline{\hat{x}}_k^e &= \underline{x}_k^p + \mathbf{C}_{xy} \mathbf{C}_{yy}^{-1} (\underline{\hat{y}} - \underline{\mu}_y) \\
   \mathbf{C}_k^e &= \mathbf{C}_k^p - \mathbf{C}_{xy} \mathbf{C}_{yy}^{-1} \mathbf{C}_{yx}
   \end{aligned}
   $$
   {{< /math >}} 

### Unscented Kalman Filter (UKF)

{{% callout note %}}

Üb 7, A3

{{% /callout %}}

Unscented Prinzipien

- Nichtlineare Transformation eines einzelnen Punktes ist einfach
- Es ist einfach, eine Punktwolke zu finden, deren Stichprobenmittelwert und -varianz mit den Momenten der gegebene Dichte übereinstimmen.
- Es ist einfach, Mittelwert und Varianz einer Punktwolke zu bestimmen

Bsp: additives Rauschen

{{< math >}}
$$
\begin{aligned}
\underline{x}_{k+1} &= \underline{a}_{k}(\underline{x}_{k}) + \underline{w}_{k} \\
\underline{y}_{k} &= \underline{h}_{k}(\underline{x}_{k}) + \underline{v}_{k}
\end{aligned}
$$
{{< /math >}} 

**Prädiktion**

1. Samples/Particles/Punkte propagieren

   {{< math >}}
   $$
   \underline{x}_{k}^{p, i} = \underline{a}_{k-1}(\underline{x}_{k-1}^{e, i})
   $$
   {{< /math >}} 

2. Mittelwert und Varianz basierend auf Samples berechnen 

   {{< math >}}
   $$
   \begin{aligned}
   \underline{\hat{x}}_{k}^p &= \frac{1}{L} \sum_{i=1}^L \underline{x}_{k}^{p, i} \\
   \mathbf{C}_k^p &= \frac{1}{L} \sum_{i=1}^L (\underline{x}_{k}^{p, i} - \underline{\hat{x}}_{k}^p) (\underline{x}_{k}^{p, i} - \underline{\hat{x}}_{k}^p)^\top + \mathbf{C}_k^w
   \end{aligned}
   $$
   {{< /math >}} 

**Fitlerung**

0. Sampling: 

   - Für prioren Schätzwert: $2N$ btw. $2N+1$ Samples auf Hauptachsen für Dimension $N$

     > Bsp: Im skalaren Fall ($N=1$), 2 Samples:
     >
     > $$
     > x_1 = \mu_p + \sigma_p \quad x_2 = \mu_p - \sigma_p
     > $$

   - Ähnlich für Samples vom Mess-Rauschen

     > Bsp: Im skalaren Fall ($N=1$), 2 Samples:
     >
     > $$
     > v_1 = \mu_v + \sigma_v \quad v_2 = \mu_v - \sigma_v
     > $$

1. Punkte Propagation

   {{< math >}}
   $$
   \underline{y}_{k}^{p, i} = \underline{h}_{k}(\underline{x}_{k}^{p, i})
   $$
   {{< /math >}} 

   bzw.

   {{< math >}}
   $$
   \underline{y}_{k}^{i, j} = \underline{h}_{k}(\underline{x}_{k}^{p, i}, \underline{v}_k^j)
   $$
   {{< /math >}} 

2. Verbundraum {{< math >}}$\underline{z}=\left[\begin{array}{l}
   \underline{x} \\
   \underline{y}
   \end{array}\right]${{< /math >}} erstellen (Annahme: {{< math >}}$\underline{x}_k${{< /math >}} und {{< math >}}$\underline{y}_k${{< /math >}} sind gemeinsam Gaußverteilt). 
   Mittelwert und Varianz von $\underline{z}$ berechnen.

   {{< math >}}

   
   $$
   \underline{\mu}_z=\left[\begin{array}{l}
   \underline{\mu}_x \\
   \underline{\mu}_y
   \end{array}\right]=\frac{1}{L}\sum_{i=1}^L\left[\begin{array}{l}
   \underline{x}_i \\
   \underline{y}_i
   \end{array}\right],  \quad \mathbf{C}_{z} = \frac{1}{L}\sum_{i=1}^L(\underline{z}_i - \underline{\mu}_z)(\underline{z}_i - \underline{\mu}_z)^\top = \left[\begin{array}{ll}
   \mathbf{C}_{x x} & \mathbf{C}_{x y} \\
   \mathbf{C}_{y x} & \mathbf{C}_{y y}
   \end{array}\right]
   $$
   {{< /math >}} 

3. Filterung in probabilistischer Form mit Messung {{< math >}}$\hat{\underline{y}}${{< /math >}}

   {{< math >}}
   $$
   \begin{aligned}
   \underline{\hat{x}}_k^e &= \underline{x}_k^p + \mathbf{C}_{xy} \mathbf{C}_{yy}^{-1} (\underline{\hat{y}} - \underline{\mu}_y) \\
   \mathbf{C}_k^e &= \mathbf{C}_k^p - \mathbf{C}_{xy} \mathbf{C}_{yy}^{-1} \mathbf{C}_{yx}
   \end{aligned}
   $$
   {{< /math >}} 

#### Sampling

Samples nur auf Hauptachsen: Insgesamt $2N$ btw. $2N+1$ ($N$: \#Dimensionen)

#### Vorteil von UKF gegen EKF

- UKF reduziert möglicherweise den Linearisierungsfehler des EKF
- Man braucht die Jacobi-Matrizen nicht zu berechnen 👏



### Analytische Momente

{{% callout note %}}

Üb 7, A4

{{% /callout %}}

1. Verbundraum $\underline{z}$ erstellen

   {{< math >}}
   $$
   z := \left[\begin{array}{l}
   x \\
   y
   \end{array}\right]
   $$
   {{< /math >}} 

2. Mittelwert von $\underline{z}$ berechnen (mithilfe von höheren Momente der Gaußdichte)

   {{< math >}}
   $$
   E\{\underline{z}\}=\left[\begin{array}{c}
   \hat{x}_{p} \\
   E\{h(x)\}
   \end{array}\right]
   $$
   {{< /math >}} 

3. Differenz zwichen $h(x)$ und $E\{h(x)\}$ berechnen

   {{< math >}}
   $$
   \bar{h}(x)=h(x)-E\{h(x)\}
   $$
   {{< /math >}} 

4. $\operatorname{Cov}\{\underline{z}\}$ berechnen

   {{< math >}}
   $$
   \operatorname{Cov}\{\underline{z}\}=\left[\begin{array}{ll}
   \mathbf{C}_{x x} & \mathbf{C}_{x y} \\
   \mathbf{C}_{y x} & \mathbf{C}_{y y}
   \end{array}\right]=\left[\begin{array}{cc}
   \sigma_{p}^{2} & E\left\{\left(x-\hat{x}_{p}\right) \bar{h}(x)\right\} \\
   E\left\{\left(x-\hat{x}_{p}\right) \bar{h}(x)\right\} & E\left\{\overline{h}^{2}(x)\right\}+\sigma_{v}^{2}
   \end{array}\right]
   $$
   {{< /math >}} 

5. Filterung in probabilistischer Form.

   {{< math >}}
   $$
   \begin{aligned}
   \underline{\hat{x}}_k^e &= \underline{x}_k^p + \mathbf{C}_{xy} \mathbf{C}_{yy}^{-1} (\underline{\hat{y}} - \underline{\mu}_y) \\
   \mathbf{C}_k^e &= \mathbf{C}_k^p - \mathbf{C}_{xy} \mathbf{C}_{yy}^{-1} \mathbf{C}_{yx}
   \end{aligned}
   $$
   {{< /math >}} 

## Ensemble Kalman Filter (EnKF)

{{% callout note %}}

Üb 6, A4 (f)

{{% /callout %}}

💡 Repräsentiere den unsicheren Schätzwert nun per „Streuungsbreite“ einer Punktwolke.

Als „unsicheren Zustand“ verwende $L$ $N$-dim. Vektoren als **Samples**

{{< math >}}
$$
\mathcal{X}_{k}=[\underbrace{\underline{x}_{k, 1}}_{\mathbb{R}^N}, \underline{x}_{k, 2}, \ldots, \underline{x}_{k, L}] \in \mathbb{R}^{N \times L}, \quad \mathcal{W}_{k}=\left[\underline{w}_{k, 1}, \underline{w}_{k, 2}, \ldots, \underline{w}_{k, L}\right] \in \mathbb{R}^{N \times L}
$$
{{< /math >}} 

wobei die Samples als Spalten einer Matrix kompakt aufgefasst werden können.

**Prädiktion**

- Nichtlinear

  {{< math >}}
  $$
  \mathcal{X}_{k}^p = \underline{a}_{k-1}(\mathcal{X}_{k-1}^e, \underline{u}_{k-1}, \mathcal{W}_{k-1})
  $$
  {{< /math >}} 

- Linear

  {{< math >}}
  $$
  \mathcal{X}_{k}^p = \mathbf{A}_{k-1}\mathcal{X}_{k-1}^e + \mathbf{B}_{k-1}(\underline{u}_{k-1} + \mathcal{W}_{k-1})
  $$
  {{< /math >}} 

**Filterung**

- Durchführung der Filterschritt NUR mit Samples
- Vermeidung der Verwendung der Update-Formeln für Kovarianzmatrix (Reine Representation der Unsicherheiten durch Samples)

Schritte

1. „Prädizierte“ Mess-Samples berechnen

   - linear

     {{< math >}}
     $$
     \mathcal{Y}_k = \mathbf{H}_k \mathcal{X}_{k}^p + \mathcal{V}_{k}
     $$
     {{< /math >}} 

   - nichtlinear

     {{< math >}}
     $$
     \mathcal{Y}_k = \underline{h}_k (\mathcal{X}_{k}^p, \mathcal{V}_{k})
     $$
     {{< /math >}} 

2. Kalman Gain berechnen

   {{< math >}}
   $$
   \begin{aligned}
   \mathbf{C}_{x y} &=\frac{1}{L} \sum_{i=1}^{L} \underline{x}_{k, i}^{\mathrm{p}} \cdot \underline{y}_{k, i}^{\top} \\
   &=\frac{1}{L} \mathcal{X}_{k}^{\mathrm{p}} \cdot \mathcal{Y}_{k}^{\top} \\\\
   \mathbf{C}_{y y} &=\frac{1}{L} \sum_{i=1}^{L} \underline{y}_{k, i} \cdot \underline{y}_{k, i}^{\top} \\
   &=\frac{1}{L} \mathcal{Y}_{k} \cdot \mathcal{Y}_{k}^{\top} \\\\
   \mathbf{K} &=\mathbf{C}_{x y} \cdot \mathbf{C}_{y y}^{-1}
   \end{aligned}
   $$
   {{< /math >}} 

3. Filterschritt mit der tatsächlichen Messung $\underline{\hat{y}}_k$

   {{< math >}}
   $$
   \mathcal{X}_{k}^e = \mathcal{X}_{k}^p + \mathbf{K} (\underline{\hat{y}}_k \cdot \underline{\mathbb{1}}^\top - \mathcal{Y}_k)
   $$
   {{< /math >}} 