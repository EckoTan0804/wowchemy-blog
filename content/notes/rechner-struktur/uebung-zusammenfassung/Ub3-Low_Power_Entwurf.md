---
linktitle: ''
summary: ''
weight: 131
title: Ub3-Low Power Entwurf
date: 2020-07-08
draft: false
type: book
authors:
- admin
tags:
- Übung

- Rechnerstruktur
categories:
- Computer Structure
toc: true
profile: false
reading_time: true
share: true
featured: true
comments: true
disable_comment: false
commentable: true
editable: false
---

## Leistungsaufnahme

$$
P_{\text {total}}=P_{\text {switching}}+P_{\text {shortcircuit}}+P_{\text {static}}+P_{\text {leakage}}
$$

- $P_{\text {switching}}$: Leistungsaufnahme durch Umladen der kapazitiven Last
  - Schaltleistung: $P_{\text {switching }}=C_{\text {eff }} * U^{2} * f$

- $P_{\text {shortcircuit}}$: Leistungsaufnahme aufgrund von Kurzschluss im CMOS-Gatter bei Zustandsänderung
- $P_{\text {static}}$: Statische Leistungsaufnahme der Schaltung
- $P_{\text {leakage}}$: Leckströme
  - Integrationsdichte ⬆️, Leckstrom ⬆️
  - Temperatur ⬆️, Leckstrom ⬆️
  - früher vernachlässigbar, spielt heute jedoch eine überaus zentrale Rolle



## Relationen zwischen Leistungaufnahme, Taktfrequenz, und Versorgungsspannung

- $P \sim f * U^{2}$

- $f \sim U$ 

  (Je geringer die Versorgungsspannung, desto geringer die maximal mögliche Taktfrequenz)

- **Kubus-Regel**
  - $P \sim U^3$
  - $P \sim f^3$



## Schaltwahrscheinlichkeit

Wahrscheinlichkeit, dass Gatter schaltet:
$$
\mathbb{P}_{\text {Schalt }}=2 * \mathbb{P}(1) *(1-\mathbb{P}(1))
$$

> $\begin{aligned}
> \mathbb{P}\_{\text {Schalt }} &=\mathbb{P}(0 \rightarrow 1 \vee 1 \rightarrow 0) \\\\
> &=\mathbb{P}(0 \rightarrow 1)+\mathbb{P}(1 \rightarrow 0) \\\\
> &=\mathbb{P}(0) * \mathbb{P}\_{\text {neu }}(1)+\mathbb{P}(1) * \mathbb{P}\_{\text {neu }}(0) \\\\
> &=\mathbb{P}(0) * \mathbb{P}(1)+\mathbb{P}(0) * \mathbb{P}(1) \\\\
> &=2 * \mathbb{P}(1) * \mathbb{P}(0) \\\\
> &=2 * \mathbb{P}(1) *(1-\mathbb{P}(1))
> \end{aligned}$

### Bsp (Aufg. 4)

ODER-Gatter mit $\mathbb{P}_{\text {Eingang a} =1}=\frac{1}{4}$ und $\mathbb{P}_{\text {Eingang b} =1}=\frac{1}{4}$

ODER: 

| $a$  | $b$  | $a \vee b$ |
| ---- | ---- | ---------- |
| 0    | 0    | 0          |
| 0    | 1    | 1          |
| 1    | 0    | 1          |
| 1    | 1    | 1          |

$$
\begin{aligned}
\mathbb{P}(1) &= 1 - \mathbb{P}(0) \\\\
&= 1 - \mathbb{P}(a=0 \wedge b=0) \\\\
&= 1 - \mathbb{P}(a=0) \mathbb{P}(b=0) \\\\
&= 1 - (1-\mathbb{P}(a=1)) (1-\mathbb{P}(b=1)) \\\\
&= 1 - (1 - \frac{1}{4})(1 - \frac{3}{4}) \\\\
&= 1 - \frac{3}{4} \cdot \frac{1}{4} \\\\
&= \frac{13}{16}
\end{aligned}
$$