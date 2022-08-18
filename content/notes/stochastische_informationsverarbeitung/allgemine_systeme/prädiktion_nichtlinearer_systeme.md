---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 560
# ============================================================

# ========== Basic metadata ==========
title: Prädiktion nichtlinearer Systeme
date: 2022-07-27
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
Skript 10.2, 10.3
{{% /callout %}}

## Chapman-Kolmogorov-Gleichung

{{% callout note %}}
Übungsblatt Aufg. 10.1
{{% /callout %}}

Verbunddichte

{{< math >}}
$$
f\left(\underline{x}_{k+1}, \underline{x}_{k}\right)=f\left(\underline{x}_{k+1} \mid \underline{x}_{k}\right) \cdot f\left(\underline{x}_{k}\right)
$$
{{< /math >}} 

Marginalisierung

{{< math >}}
$$
f\left(x_{k+1}\right)=\int_{\mathbb{R}^{N}} f\left(\underline{x}_{k+1} \mid \underline{x}_{k}\right) \cdot f\left(\underline{x}_{k}\right) d \underline{x}_{k}
$$
{{< /math >}} 

Definition

- geschätzte Dichte im Zeitschritt $k$ einschließlich der letzten Messung

  {{< math >}}
  $$
  f_{k}^{e}\left(\underline{x}_{k}\right)=f\left(\underline{x}_{k} \mid \underline{\hat{y}}_{k}, \underline{\hat{y}}_{k-1}, \ldots, \underline{\hat{y}}_{1}, \underline{\hat{u}}_{k-1}, \underline{\hat{\hat{u}}}_{k-2}, \ldots, \underline{\hat{u}}_{0}\right)
  $$
  {{< /math >}} 

- Prädiktion der Dichte im Zeitschritt $k+1$ (Messung nicht inklusive)

  {{< math >}}
  $$
  f_{k+1}^{p}\left(\underline{x}_{k+1}\right)=f\left(\underline{x}_{k+1} \mid \underline{\hat{y}}_{k}, \underline{\hat{y}}_{k-1}, \ldots, \underline{\hat{y}}_{1}, \underline{\hat{u}}_{k}, \underline{\hat{u}}_{k-1}, \ldots, \underline{\hat{u}}_{0}\right)
  $$
  {{< /math >}} 

Prädiktion für dynamische Systeme ( {{< hl >}}**Chapman-Kolmogorov-Gleichung**{{< /hl >}})

{{< math >}}
$$
f_{k+1}^{p}\left(\underline{x}_{k+1}\right)=\int_{\mathbb{R}^{N}} \underbrace{f\left(\underline{x}_{k+1} \mid \underline{x}_{k}\right)}_{\text{Prädiktionsdichte}} f_{k}^{e}\left(\underline{x}_{k}\right) \mathrm{d} \underline{x}_{k}
$$
{{< /math >}} 

‼️ <span style="color: Red">Problem: Es handelt sich um ein Parameterintegral!</span>

- <span style="color: Red">Integrand hängt von $\underline{x}_{k+1}$ ab (lässt sich i.Allg nicht herausziehen)</span>
- <span style="color: Red">Erfordert Lösung des Integrals für alle $\underline{x}_{k+1}$</span>
- <span style="color: Red">Nur möglich für analytische Lösung</span>

Weiter nützliche Form der CK-Gleichung

{{< math >}}
$$
\begin{aligned}
f(\underline{x}_{k + 2}, \underline{x}_{k}) &= \int_{\mathbb{R}^N} f(\underline{x}_{k+2}, \underline{x}_{k+1}, \underline{x}_{k}) d\underline{x}_{k+1} \\\\
f(\underline{x}_{k + 2} \mid \underline{x}_{k}) f(\underline{x}_{k}) &= \int_{\mathbb{R}^N} f(\underline{x}_{k+2} \mid \underline{x}_{k+1}, \underline{x}_{k}) f(\underline{x}_{k+1}, \underline{x}_{k}) d\underline{x}_{k+1} \quad | \quad \text{Markov} \\\\
f(\underline{x}_{k + 2} \mid \underline{x}_{k}) f(\underline{x}_{k}) &= \int_{\mathbb{R}^N} f(\underline{x}_{k+2} \mid \underline{x}_{k+1}) f(\underline{x}_{k+1}, \underline{x}_{k}) d\underline{x}_{k+1} \\\\
f(\underline{x}_{k + 2} \mid \underline{x}_{k}) f(\underline{x}_{k}) &= \int_{\mathbb{R}^N} f(\underline{x}_{k+2} \mid \underline{x}_{k+1}) f(\underline{x}_{k+1} \mid \underline{x}_{k}) f(\underline{x}_{k})d\underline{x}_{k+1} \\\\
f(\underline{x}_{k + 2} \mid \underline{x}_{k})  &= \int_{\mathbb{R}^N} f(\underline{x}_{k+2} \mid \underline{x}_{k+1}) f(\underline{x}_{k+1} \mid \underline{x}_{k}) d\underline{x}_{k+1}
\end{aligned}
$$
{{< /math >}} 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-CK_Gleichung.drawio.png" alt="allg_sys-CK_Gleichung.drawio" style="zoom:67%;" />



### Prädiktion mit CK-Glg.: Lösungsansätze

Im allgemeinen Fall ist CK-Gleichung NICHT exakt lösbar 🤪

Ausnahme (Bsp.)

- System ist linear und $f_{k}^{e}(\cdot)$ kann durch erste zwei Momente beschrieben werden

- $f_{k}^{e}(\underline{x}_k)$ ist durch Abstastwerte repräsentiert.

  {{< math >}}
  $$
  \begin{aligned}
  & f_{k}^{e}\left(\underline{x}_{k}\right)=\sum_{i=1}^{L} w_{i} \delta\left(\underline{x}_{k}-\hat{\underline{x}}_{k, i}\right)  \qquad w_i \geq 0, \sum_i w_i = 1\\
  \Rightarrow \qquad & f_{k=1}^{p}\left(\underline{x}_{k+1}\right)=\sum_{i=1}^{L} w_{i} f\left(\underline{x}_{k+1} \mid \hat{\underline{x}}_{k, i}\right)
  \end{aligned}
  $$
  

  {{< /math >}} 

## Vereinfachte Prädiktion

### Systemmodell mit additivem Rauschen

Wir beginnen mit additivem Rauschen.

Generatives Modell

{{< math >}}
$$
\underline{x}_{k+1} = \underline{a}_{k}(\underline{x}_{k}) + \underline{w}_{k} \qquad \underline{x}_{k+1}, \underline{x}_{k}, \underline{w}_{k} \in \mathbb{R}^N
$$
{{< /math >}} 

Vereinfachte Schreibweise

{{< math >}}
$$
\underline{z} = \underline{a}(\underline{x}) + \underline{w}
$$


{{< /math >}} 

Probablistisches Modell (inkl. Rauschen)

{{< math >}}
$$
f(\underline{z} \mid \underline{x}) = f_w(\underline{z} - \underline{a}(\underline{x}))
$$
{{< /math >}} 

Vereinfachung: Aufteilung in diskrete "Streifen":

{{< math >}}
$$
f\left(\underline{z} \mid \underline{\hat{x}}_{i}\right)=f_w\left(\underline{z}-\underline{a}\left(\underline{\hat{x}}_{i}\right)\right) \qquad i \in \mathbb{Z}
$$
{{< /math >}} 

In den "Zwischenräumen" gilt nun aber {{< math >}}$\int f(\underline{z} \mid \underline{x}) = 1${{< /math >}}  NICHT. Wir definiere eine "Füllfunktion" $f_i(\underline{x})$:

{{< math >}}
$$
f_i(\underline{x}) = \mathcal{N}(\underline{x}, \underline{\hat{x}}_i, C_i) \qquad i \in \mathbb{Z}
$$
{{< /math >}} 

mit 

{{< math >}}
$$
f(\underline{x}) = \sum_{i \in \mathbb{Z}} w_if_i(\underline{x}) \approx 1
$$
{{< /math >}} 

> Z.B. Skalarer Fall
>
> {{< math >}}
> $$
> f(x)=\sum_{i \in \mathbb{Z}} w_{i} f_i(x), \quad f_i(x)=\exp \left(-\frac{1}{2} \frac{\left(x-\hat{x}_{i}\right)^{2}}{\sigma^{2}}\right)
> $$
> {{< /math >}} 
>
> mit geeigneten $\sigma$.

Betrachtung für jeweils ein Komponente $i$

{{< math >}}
$$
f_i(\underline{z} \mid \underline{x}) = f(\underline{z} \mid \underline{\hat{x}}_i) \cdot f_i(\underline{x})
$$
{{< /math >}} 

Gesamtdichte ist

{{< math >}}
$$
f(\underline{z} \mid \underline{x}) \approx \sum_{i \in \mathbb{Z}} w_i f(\underline{z} \mid \underline{\hat{x}}_i) \cdot f_i(\underline{x})
$$
{{< /math >}} 

Es gilt

{{< math >}}
$$
\begin{aligned}
\int_{\mathbb{R}^{N}} f(\underline{z}(\underline{x}) d \underline{z}&=\sum_{i \in \mathbb{Z}} w_{i} f_{i}(\underline{x}) \underbrace{\int_{\mathbb{R}^N}f(\underline{z} \mid \underline{x}) d\underline{z}}_{=1}\\
&=\sum_{i \in \mathbb{Z}} w_{i} f_{i}(\underline{x}) \approx 1
\end{aligned}
$$
{{< /math >}} 

Fall Rauschen $\underline{w}_k$ Gaußverteilt, ist $f(\underline{z} \mid \underline{x} )$ Gaussian Mixture

{{< math >}}
$$
f(\underline{z} \mid \underline{x}) = \sum_{i \in \mathbb{Z}} \underbrace{f_i^z(\underline{z})}_{f_w(\underline{z} - \underline{a}(\underline{\hat{x}}_i))} \cdot f_i^x(\underline{x})
$$
{{< /math >}} 

### Allgemeine Systemmodelle

{{< math >}}
$$
\underline{x}_{k+1} = \underline{a}_k (\underline{x}_k, \underline{w}_k)
$$
{{< /math >}} 

Vereinfachte Schreibweise:

{{< math >}}
$$
\underline{z} = \underline{a}(\underline{x}, \underline{w})
$$


{{< /math >}} 

Ergibt allgemeine Transitionsdichte $f(\underline{z} | \underline{x})$, auch durch Mixture approximierbar

{{< math >}}
$$
f(\underline{z} | \underline{x}) = \sum_{i \in \mathbb{Z}} f_i^z(\underline{z}) \cdot f_i^x(\underline{x})
$$
{{< /math >}} 

Wichtig ist, dass die einzelnen Komponenten entkoppelt sind. 👏

### Bsp 1

Annahme: $f(\underline{x})$ ist eine Gaußdichte.

Einsetzen in CK-Gleichung:

{{< math >}}
$$
\begin{aligned}
f(\underline{z})&=\int_{\mathbb{R}^{N}}\left(\sum_{i \in \mathbb{Z}} w_{i} f_{i}^{z}(\underline{z}) \cdot f_{i}^{x}(\underline{x})\right) f(\underline{x}) d \underline{x}\\
&=\sum_{i \in \mathbb{Z}} w_{i} f_{i}^{z}(\underline{z}) \underbrace{\int_{\mathbb{R}^{N}} f_{i}^{x}(\underline{x}) \cdot f(\underline{x}) d \underline{x}}_{\text{Konstante } c_{i}}\\
&= \sum_{i \in \mathbb{Z}} \underbrace{w_{i} c_i}_{=: \bar{w}_i} f_{i}^{z}(\underline{z})\\
&=\sum_{i \in \pi} \bar{w}_{i} f_{i}^{z}(\underline{z})
\end{aligned}
$$
{{< /math >}} 

Speizialfall: $f(\underline{x}) = \delta(\underline{x} - \underline{\hat{x}}) \Rightarrow$

{{< math >}}
$$
c_i = \int_{\mathbb{R}^{N}} f_{i}(\underline{x}) \delta \left(\underline{x}-\underline{\hat{x}}\right) d \underline{x}=f_i(\underline{\hat{x}})
$$
{{< /math >}} 

### Bsp 2

Annahme: Gaussian Mixture

{{< math >}}
$$
f(\underline{x}) = \sum_{j=1}^L v_j f_j^*(\underline{x})
$$
{{< /math >}}  

Einsetzen in CK-Gleichung:

{{< math >}}
$$
\begin{aligned}
f(\underline{z})&=\int_{\mathbb{R}^{N}}\left\{\sum_{i \in \mathbb{Z}} w_{i} f_{i}^{z}(\underline{z}) f_{i}^{x}(\underline{x})\right\} \cdot \left\{\sum_{i=1}^{L} v_{j} f_{j}^{*}(\underline{x})\right\} d x\\
&=\sum_{i \in \mathbb{Z}} w_{i} f_{i}^{z}(\underline{z}) \underbrace{\sum_{i=1}^{L} v_{j} \underbrace{\int_{\mathbb{R}^N} f_{i}^{x}(\underline{x}) \cdot f_{j}^{*}(\underline{x}) d \underline{x}}_{\text{Konstante}}}_{\text {Kondante } C_{i}} \\
&=\sum_{i \in \pi} \underbrace{w_{i}C_i}_{=: \bar{w}_i} f_{i}^{z}(\underline{z}) \\
&=\sum_{i \in \pi} \bar{w}_{i} f_{i}^{z}(\underline{z}) 
\end{aligned}
$$
{{< /math >}} 