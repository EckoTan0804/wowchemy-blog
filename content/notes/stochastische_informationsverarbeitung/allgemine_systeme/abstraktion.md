---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 550
# ============================================================

# ========== Basic metadata ==========
title: Abstraktion
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
Skript 10.1, 10.2
{{% /callout %}}

## Abstrahierte Systembeschreibung & Eigenschaften

Alle Komponenten eines Systems können durch 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-27%2022.02.34.png" alt="截屏2022-07-27 22.02.34" style="zoom:50%;" />

beschrieben werden ({{< math >}}$\underline{a} \in \mathbb{R}^A, \underline{b}\in \mathbb{R}^b${{< /math >}}) .

Kauselität: $a$ (Grund) bewrikt $b$ (Wirkung).

Für $\underline{a}$ gegeben, $f(\underline{b} \mid \cdot)$ heißt {{< hl >}}**Transitionsdichte**{{< /hl >}}.

Für $\underline{b}$ gegeben, $f(\cdot \mid \underline{a})$ heißt {{< hl >}}**Likelihood**{{< /hl >}}.

### Eigenschaften von probabilistischer Systembeschreibung

In Allg. gilt

{{< math >}}
$$
\int_{\mathbb{R}^{B}} f(\underline{b} \mid \underline{a}) d \underline{b}=1 \quad \forall \underline{a}
$$
{{< /math >}} 

Es gilt aber i.A. 

{{< math >}}
$$
\int_{\mathbb{R}^{A}} f(\underline{b} \mid \underline{a}) d \underline{a} \neq 1,
$$
{{< /math >}} 

sogar nicht definiert.

## Vorwärts-/Rückwärtsinferenz

**Vorwärtsinferenz**

*"Given information about $\underline{a}$, we desire information about $\underline{b}$."*

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-27%2022.18.55.png" alt="截屏2022-07-27 22.18.55" style="zoom:50%;" />

- Gegeben: Werte für $\underline{\hat{a}}$ oder Dichte $f(\underline{a})$
- Gesucht: $f(\underline{b})$

**Rückwärtsinferenz**

*"Information about the output $\underline{b}$ is given and we desire to reconstruct an appropriate description of $\underline{a}$."*

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-27%2022.19.17.png" alt="截屏2022-07-27 22.19.17" style="zoom:50%;" />

- Gegeben: Werte für $\underline{\hat{b}}$ oder Dichte $f(\underline{b})$
- Gesucht: $f(\underline{a})$

 ## Vorwärtsinferenz

{{% callout note %}}
Übungsblatt Aufg. 9.1
{{% /callout %}}

**Annahme: KEIN Vorwissen über $f(\underline{b})$**

Betrachte eine einfache generative Systemabbildung:

{{< math >}}
$$
\underline{b} = \underline{g}(\underline{a}) \quad \underline{a} \in \mathbb{R}^A, \underline{b} \in \mathbb{R}^B
$$
{{< /math >}} 

Probablistische Systemabbildung:

{{< math >}}
$$
f(\underline{b} \mid \underline{a}) = \delta(\underline{b} - \underline{g}(\underline{a}))
$$
{{< /math >}} 

Marginalisierung ergibt:

{{< math >}}
$$
\begin{aligned}
f(\underline{b}) &= \int_{\mathbb{R}^A} f(\underline{a}, \underline{b}) d\underline{a} \\\\
&= \int_{\mathbb{R}^A} f(\underline{a} \mid \underline{b}) f(\underline{a}) d\underline{a} \\\\
&= \int_{\mathbb{R}^A} \delta(\underline{b} - \underline{g}(\underline{a})) f(\underline{a}) d\underline{a}
\end{aligned}
$$
{{< /math >}} 

Weitere Vereinfachung NUR für konkrete $\underline{g}(\cdot)$ möglich.

Für Speizialfall der Vorgabe eines Wertes $\underline{\hat{a}}$ ergibt sich

{{< math >}}
$$
f(\underline{a}) = \delta(\underline{a} - \underline{\hat{a}})
$$
{{< /math >}} 

Damit

{{< math >}}
$$
\begin{aligned}
f(\underline{b}) &= \int_{\mathbb{R}^A} \delta(\underline{b} - \underline{g}(\underline{a})) f(\underline{a}) d\underline{a} \\\\
&= \int_{\mathbb{R}^A} \delta(\underline{b} - \underline{g}(\underline{a})) \delta(\underline{a} - \underline{\hat{a}}) d\underline{a} \\\\
&= \delta(\underbrace{\underline{b} - g(\underline{\hat{a}})}_{\underline{\hat{b}}})
\end{aligned}
$$
{{< /math >}} 

Das erwartete Ergebnis ist dann

{{< math >}}
$$
f(\underline{b}) = \delta(\underline{b} - \underline{\hat{b}})
$$
{{< /math >}} 

mit $\underline{\hat{b}} = \underline{g}(\underline{\hat{a}})$.

## Probabilistisches nichtlineares Systemmodell

Allgemeines Systemmodell

{{< math >}}
$$
\underline{x}_{k+1} = \underline{a}_k(\underline{x}_k, \underline{w}_k)
$$
{{< /math >}} 

in Form $f(\underline{b} \mid \underline{a})$ bringen:

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-prob_nichtlin_sys.drawio.png" alt="allg_sys-prob_nichtlin_sys.drawio" style="zoom:67%;" />

{{< math >}}
$$
\underline{a}=\left[\begin{array}{c}
\underline{x}_{k} \\
\underline{w}_{k}
\end{array}\right], \quad \underline{b}=\underline{x}_{k+1}
$$
{{< /math >}} 

{{< math >}}
$$
f(\underline{b} \mid \underline{a}) = \delta \left(\underline{x}_{k+1} - \underline{a}_k(\underline{x}_k, \underline{w}_k)\right)
$$
{{< /math >}} 

Mit anderen Systemgrenzen:

![allg_sys-Copy of prob_nichtlin_sys.drawio](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/allg_sys-Copy%20of%20prob_nichtlin_sys.drawio.png)

{{< math >}}
$$
\begin{aligned}
f(\underline{b} \mid \underline{a}^\prime) &= f(\underline{x}_{k+1} \mid \underline{x}_k) \\\\
&= \int_{\mathbb{R}^N} \underbrace{f(\underline{x}_{k+1} \mid \underline{x}_k, \underline{w}_k)}_{f(\underline{b} \mid \underline{a})} \cdot f(\underline{w}_k) d\underline{w}_k
\end{aligned}
$$
{{< /math >}} 

In diesem Fall enthält $f(\underline{b} \mid \underline{a})$ Systemrauschen $\rightarrow$ ist nicht mehr durch $\delta$-funktion beschreibbar.