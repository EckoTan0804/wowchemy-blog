---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 101
# ============================================================

# ========== Basic metadata ==========
title: Ereignis und Wahrscheinlichkeit
date: 2022-06-04
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

# Ereignisse

Ein **endlicher Ergebnisraum** eines **Zufallsexperimentes** ist eine nichtleere Menge

{{< math >}} 
$$
\Omega=\left\{\omega_{1}, \omega_{2}, \ldots, \omega_{N}\right\}.
$$
{{< /math >}} *I.e.,* $\Omega$ enthält alle mögliche Ergebnisse.

Die Elemente {{< math >}} $\omega_{n} \in \Omega$ {{< /math >}} heißen {{< hl >}}**Ergebnisse**{{< /hl >}}, die möglichen Ausgänge eines Zufallsexperiments.

Jede Teilmenge $A \subset \Omega$ heißt {{< hl >}}**Ereignis**{{< /hl >}}.

- Jede einelementige Teilmenge {{< math >}} $\left\{\omega_{n}\right\} \subset \Omega$ {{< /math >}} heißt {{< hl >}}**Elementarereignis**{{< /hl >}} (ZUsammenfassung von einem oder mehreren Ergebnissen).

  $\rightarrow$ Der Ergebnisraum $\Omega$ (das **sichere Ereignis**) und die leere Menge $\emptyset$ (das **unmögliche Ereignis**) sind stets Ereignisse.

Für zwei Ereignisse $A$ und $B$

- Gilt $A \subset B$, so ist $A$ ein {{< hl >}}**Teilereignis**{{< /hl >}} von $B$.

- Der **Durchschnitt** $(A \cap B)$, die Vereinigung $(A \cup B)$, und die **Differenz** $(A-B)$ sind auch Ereignisse.
  - Durchschnitt und Vereinigung sind *kommutativ*, *assoziativ* und *distributiv*.

- Das **entgegengesetzte Ereignis** $\bar{A}$ von $A$ ist auch ein Ereignis und wird als {{< hl >}}**Negation**{{< /hl >}} oder {{< hl >}}**Komplement**{{< /hl >}} bezeichnet.

- Gilt $A \cap B=\varnothing$, so heißen $A$ und $B$ {{< hl >}}**disjunkt**{{< /hl >}} ode {{< hl >}}**unvereinbar**{{< /hl >}} .

- **de MORGANschen Formeln**

  {{< math >}}  
  $$
  \begin{array}{l}
  \overline{A \cup B}=\bar{A} \cap \bar{B} \\
  \overline{A \cap B}=\bar{A} \cup \bar{B}
  \end{array}
  $$
  {{< /math >}} 

{{< spoiler text="Beispiel" >}}

Würfel werfen.

- Ergebnisraum {{< math >}}$\Omega = \\{1, 2, 3, 4, 5, 6\\}${{< /math >}} (Also $\|\Omega\| = 6$)
- Beispiel Ereignise
  - "Der Würfel zeight eine ungerade Zahl."
  - "Der Würfel zeigt eine 3."
  - "Der Würfel zeigt eine 3." (das unmögliche Ereignis)
- Ereignis $A$ = "Der Würfel zeight eine ungerade Zahl." = $\\{1, 3, 5\\}$. Ereignis $B$ = "Der Würfel zeight eine gerade Zahl" = $\\{2, 4, 6\\}$. $A \cap B = \emptyset$ $\Rightarrow$ $A$ und $B$ sind disjunkt oder unvereinbar.

Reference: [Wahrscheinlichkeit](https://studyflix.de/statistik/wahrscheinlichkeit-1932)

{{< /spoiler >}}



## Wahrscheinlichkeit (von Kolmogoroff)

Ein nichtleeres System $\mathfrak{B}$ von Teilmengen eines Ergebnisraums $\Omega$ heißt {{< hl >}}**$\sigma$-Algebra**{{< /hl >}}  (über $\Omega$), wenn gilt

{{< math >}}
$$
\begin{array}{c}
A \in \mathfrak{B} \quad \Rightarrow \quad \bar{A} \in \mathfrak{B}, \\
A_{n} \in \mathfrak{B} ; n=1,2, \ldots \quad \Rightarrow \quad \bigcup_{n=1}^{\infty} A_{n} \in \mathfrak{B}.
\end{array}
$$
{{< /math >}}

Ein höchstens abzählbares System 

{{< math >}}

$$\left\{A_{n} \in \mathfrak{B}: A_{k} \cap A_{n}=\varnothing, k \neq n\right\}$$

{{< /math >}} 

heißt {{< hl >}}**vollständige Ereignisdisjunktion**{{< /hl >}}, wenn gilt {{< math >}}$\bigcup_{n=1}^{\infty} A_{n}=\Omega${{< /math >}} .

### Kolmogoroffsche Axiome

Gegeben seien ein Ergebnisraum $\Omega$ und eine geeignete $\sigma$-Algebra $\mathfrak{B}$ über $\Omega$. Die Elemente von $\mathfrak{B}$ sind also die Ereignisse eines Zufallsexperiments.

Eine Funktion $P$, die jedem Ereignis $A \in \mathfrak{B}$ eine relle Zahl zuordnet, erfülle

{{< math >}}
$$
\begin{aligned}
\mathrm{P}(\Omega) &=1 \quad &(\text{Normiertheit})\\
\mathrm{P}(A) & \geq 0 \quad \forall A \in \mathfrak{B} \quad &(\text{Nicht-negativität}) \\
\mathrm{P}\left(\bigcup_{n=1}^{\infty} A_{n}\right) &=\sum_{n=1}^{\infty} \mathrm{P}\left(A_{n}\right) \quad A_i \cap A_j = \emptyset, \forall i,j \quad &(\text{Additivität})
\end{aligned}
$$
{{< /math >}} 

dann heißt $P(A)$ die {{< hl >}}**Wahrscheinlichkeit**{{< /hl >}} des Ereignisses $A$.

{{< spoiler text="Beispiel" >}}

Würfelwurf 

Ergebnisraum $\Omega = \\{1, 2, 3, 4, 5, 6\\}$ 

Ereignis $E = \text{Zahlen von 1 bis 6}$, also {{< math >}} $E_i$ {{< /math >}} ist die Zahl $i$ (z.B {{< math >}} $E_1$ {{< /math >}} ist die Zahl 1).

Dann haben wir:

{{< math >}}
$$
\begin{aligned}
P(E_1) &= \frac{1}{6} \\
P(E_2) &= \frac{1}{6} \\
P(\Omega) &= \frac{6}{6} = 1 \\
P(E_1 \cup E_2) &= \frac{1}{6} + \frac{1}{6} = \frac{2}{6} \quad (E_1 \cap E_2 = \emptyset)
\end{aligned}
$$
  {{< /math >}} 

Reference: {{< youtube GtpN4SRESaA>}}
{{< /spoiler >}}

Hieraus folgt

{{< math >}}
$$
\begin{aligned}
\mathrm{P}(\varnothing) &=0, \\
\mathrm{P}(\bar{A}) &=1-\mathrm{P}(A), \\
0 \leq \mathrm{P}(A) & \leq 1, \\
\mathrm{P}(A \cup B) &=\mathrm{P}(A)+\mathrm{P}(B)-\mathrm{P}(A \cap B), \\
\mathrm{P}\left(\bigcup_{n=1}^{\infty} A_{n}\right) &=1 \quad \text { für jede vollständige Ereignisdisjunktion } A_{n} .
\end{aligned}
$$
{{< /math >}} 



## Bedingte Wahrscheinlichkeiten

Sei $B \subset \Omega$ als **vorausgesetztes Ereignis**, $A, B \in \mathfrak{B}$ und $\mathrm{P}(B)>0$. Dann heißt 

{{< math >}}
$$
\mathrm{P}(A \mid B)=\frac{\mathrm{P}(A \cap B)}{\mathrm{P}(B)}
$$
{{< /math >}} 

{{< hl >}}**bedingte Wahrscheinlichkeit**{{< /hl >}} von $A$ unter der Bedingung $B$.

### Multiplikationsregel für Wahrscheinlichkeiten

{{< math >}}  
$$
\mathrm{P}(A \cap B)=\mathrm{P}(A \mid B) \mathrm{P}(B)
$$
{{< /math >}} 

Im allgemein ist $\mathrm{P}(A \mid B) \neq \mathrm{P}(B \mid A)$. Es gilt die Beziehung

{{< math >}}
$$
\mathrm{P}(A \mid B) \mathrm{P}(B)=\mathrm{P}(A \cap B) = \mathrm{P}(B \mid A) \mathrm{P}(A)
$$
{{< /math >}} 

Verallgemeinierung: Die wiederholte Anwendung der Multiplikationsregel auf den Durchschnitt $N$ zufälliger Ereignisse liefert

{{< math >}}
$$
\begin{aligned}
&\mathrm{P}\left(\bigcap_{n=1}^{N} A_{n}\right) \\
=&\mathrm{P}\left(\bigcap_{n=2}^{N} A_{n} \mid A_{1}\right) \mathrm{P}\left(A_{1}\right) \\
=&\mathrm{P}\left(\bigcap_{n=3}^{N} A_{n} \mid A_{2} \cap A_{1}\right) \mathrm{P}\left(A_{2} \mid A_{1}\right) \mathrm{P}\left(A_{1}\right) \\
=&\mathrm{P}\left(\bigcap_{n=4}^{N} A_{n} \mid A_{3} \cap A_{2} \cap A_{1}\right) \mathrm{P}\left(A_{3} \mid A_{2} \cap A_{1}\right) \mathrm{P}\left(A_{2} \mid A_{1}\right) \mathrm{P}\left(A_{1}\right) \\
=&\mathrm{P}\left(A_{N} \mid \bigcap_{n=1}^{N-1} A_{n}\right) \cdots \mathrm{P}\left(A_{4} \mid A_{3} \cap A_{2} \cap A_{1}\right) \mathrm{P}\left(A_{3} \mid A_{2} \cap A_{1}\right) \mathrm{P}\left(A_{2} \mid A_{1}\right) \mathrm{P}\left(A_{1}\right)
\end{aligned}
$$
{{< /math >}} 

{{< spoiler text="Beispiel" >}}
Vereinfachung mit 3 Ereignisse

{{< math >}}
$$
\begin{array}{ll}
&P(A) \cdot P(B \mid A) \cdot P(C \mid A \cap B) \\\\
=&P(A) \cdot \frac{P(A \cap B)}{P(A)} \cdot \frac{P(C \mid A \cap B)}{P(A \cap B)} \\\\
=&P(A \cap B \cap C)
\end{array}
$$
{{< /math >}} 

Ref: [Multiplikationssatz](https://www.sofatutor.com/mathematik/wahrscheinlichkeitsrechnung-und-stochastik/bedingte-wahrscheinlichkeit-und-abhaengigkeit/multiplikationssatz)

{{< /spoiler >}}

### Formel von der totalen Wahrscheinlichkeit

Die Ereignisse {{< math >}}$A_{n}(1 \leq n \leq N)${{< /math >}}  seien eine vollständige *Ereignisdisjunktion* (also {{< math >}}$A_i \cap A_j = \emptyset, \forall i, j${{< /math >}} ) und es gelte {{< math >}}$\mathrm{P}\left(A_{n}\right)>0, \forall n${{< /math >}} . Dann folgt für $\forall B \in \mathfrak{B}$ die **Formel von der totalen Wahrscheinlichkeit**

{{< math >}}
$$
\mathrm{P}(B)=\sum_{n=1}^{N} \mathrm{P}\left(B \mid A_{n}\right) \mathrm{P}\left(A_{n}\right)
$$
{{< /math >}} 

{{< spoiler text="Beispiel" >}}
$A \cap \bar{A} = \emptyset$
{{< math >}}
$$
\begin{array}{l}
P(B)&=P(B \cap A)+P(B \cap \bar{A}) \\\\
&=P(A)P(B \mid A)+P(\bar{A})P(B \mid \bar{A})
\end{array}
$$
{{< /math >}} 
{{< /spoiler >}}

{{< spoiler text="Beispiel" >}}
[Satz der totalen Wahrscheinlichkeit](https://studyflix.de/statistik/satz-der-totalen-wahrscheinlichkeit-1111)
{{< /spoiler >}}


Und wenn $P(B) > 0$ ist, folgt die **Formel von Bayes**:

{{< math >}}
$$
\mathrm{P}\left(A_{n} \mid B\right)=\frac{\mathrm{P}\left(B \mid A_{n}\right) \mathrm{P}\left(A_{n}\right)}{\sum_{k=1}^{N} \mathrm{P}\left(B \mid A_{k}\right) \mathrm{P}\left(A_{k}\right)}
$$
{{< /math >}} 

Im allgemeinen ist $\mathrm{P}(A) \neq \mathrm{P}(A \mid B)$. Gilt aber für $A, B \in \mathfrak{B}$

{{< math >}}
$$
\mathrm{P}(A \mid B)=\mathrm{P}(A),
$$
{{< /math >}} 

so heißt $A$ {{< hl >}}**unabhängig**{{< /hl >}} von $B$.

Für unabhängige Ereignisse folgt hieraus

{{< math >}}
$$
\begin{array}{c}
\mathrm{P}(A \cap B)=\mathrm{P}(A \mid B) \mathrm{P}(B)=\mathrm{P}(A) \mathrm{P}(B) \\
\mathrm{P}(B \mid A)=\frac{\mathrm{P}(A \cap B)}{\mathrm{P}(A)}=\mathrm{P}(B)
\end{array}
$$
{{< /math >}} 
