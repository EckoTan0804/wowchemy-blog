---
# ===== Title, summary, and position in the left sidebar =====
linktitle: Math # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 2
# ============================================================

# ========== Basic metadata ==========
title: Math Vorkenntnisse
date: 2022-05-27
draft: false
type: book # page type
authors:
  - admin
tags:
  - SI
  - Lecture Notes
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

## Ereignisse

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



## Zufallsvariablen

{{% callout warning %}}

Zufallsvariablen werden auf den SI-Übungsblättern durch kleine, fettgedruckte Buchstaben gekennzeichnet, z.B. $\boldsymbol{x}$. 

Diese Notation wird nicht auf den handschriftlichen Mitschrieben umgesetzt, sodass Zufallsvariablen und „normale“ Variablen meistens aus dem Kontext heraus unterschieden werden müssen. 🤪👎

{{% /callout %}}

Eine {{< hl >}}**Zufallsvariable**{{< /hl >}} ist eine Art Funktion, die jedem Ergebnis $\omega$ deines Zufallsexperiments genau eine Zahl $x$ zuordnet.

- ordnet also den Ergebnissen eines Zufallsexperiments reelle Zahlen zu
- beschreibt sozusagen das Ergebnis eines Zufallsexperiments, das noch nicht durchgeführt wurde

> Man sagt Variable, weil deine Zahl, die du am Ende erhältst, eben variabel ist.

‼️**Wichtig: zwischen $X$ und $x$ zu unterscheiden.**

- $X$: die tatsächliche Zufallsvariable, welche keinen festen Wert hat. Sie bildet das derzeit unbekannte Ergebnis eines Zufallsexperiments ab
- $x$: das Ergebnis nach dem Experiment und steht ist somit eine konkrete Zahl.

Bsp: 2 Würfeln werfen

- Zufallsvariable $X$ = Augensumme
- $P(X = 6)$: "Die Wahrscheinlichkeit, dass die Summe von zwei Würfeln sechs ergibt" (Hier $x=6$)

### Diskrete Zufallsvariable

Eine Zufallsvariable wird als {{< hl >}}**diskret**{{< /hl >}} bezeichnet, wenn sie nur **endlich viele** oder **abzählbar** unendlich viele Werte annimmt.

- Sklaenarten: Nominal- oder Ordinalskala

{{% callout note %}}
„Abzählbar unendlich“ bedeutet, dass die Menge der Ausprägungen durchnummeriert werden kann.
{{% /callout %}}

Bsp: Das Ergebnis beim Würfelwurf ist $x \in \Omega = \\{1, 2, 3, 4, 5, 6\\}$, also $|\Omega| = 6$.

#### Wahrscheinlichkeitsfunktion

Bei diskreten Zufallsvariablen ermittelt man die {{< hl >}}**Wahrscheinlichkeitsfunktion** (Engl. Probability mass function (PMF)){{< /hl >}}, die Wahrscheinlichkeit für ein ganz konkretes Ergebnis angibt.

{{< math >}}
$$
f(x): \Omega \rightarrow[0,1], x \in \mathbb{N}_{0}
$$
{{< /math >}} 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-05-31%2022.20.17.png" alt="截屏2022-05-31 22.20.17" style="zoom: 50%;" />

Die Funktionswert 

{{< math >}}
$$
f(x) = P(X=x)
$$
{{< /math >}} 

entspricht der Wahrscheinlichkeit, dass $X$ den Wert $x$ annimmt. Daher gilt 

{{< math >}}
$$
\sum_{x \in \Omega} f(x)=1
$$
{{< /math >}} 

#### Verteilungsfunktion

Die {{< hl >}}**Verteilungsfunktion (Engl,. Cumulative Distribution Function (CDF))**{{< /hl >}} gibt an, mit welcher Wahrscheinlichkeit das Ergebnis des Zufallsexperiments *kleiner oder gleich* eines bestimmten Wertes ist.

- Dafür werden alle Ergebnisse bis zu diesem Wert aggregiert, also „aufaddiert“. Deshalb spricht man auch oft von einer **kumulativen Verteilungsfunktion**.

Um die diskrete Verteilungsfunktion zu erhalten, werden schrittweise alle Wahrscheinlichkeitswerte kumuliert. Das heißt, man bildet das Integral unter der Wahrscheinlichkeitsfunktion.

{{< math >}}
$$
F(x): \boldsymbol{\Omega} \rightarrow[\mathbf{0}, \mathbf{1}], \boldsymbol{x} \in \mathbb{N}_{\mathbf{0}}
$$
{{< /math >}} 

{{< math >}}
$$
F(x)= P(X \leq x) = \sum_{x_{i} \leq x} f\left(x_{i}\right)
$$
{{< /math >}} 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-05-31%2022.20.17.png" alt="截屏2022-05-31 22.20.17" style="zoom: 40%; float: left" />

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-05-31%2022.43.01.png" alt="截屏2022-05-31 22.43.01" style="zoom:40%; float:right" />



{{< spoiler text="Beispiel" >}}
Würfelwurf:

Wahrscheinlichkeitsfunktion:

{{< math >}}
$$
f(X=k) = \frac{1}{6} \quad k \in \\{1, 2, 3, 4, 5, 6\\}
$$


{{< /math >}} 

Verteilungsfunktion:

{{< math >}}
$$
F(3) = P(X \leq 3) = \sum_{i\leq 3}f(X=i) = \frac{1}{3} + \frac{1}{3} + \frac{1}{3}
$$

{{< /math >}} 
{{< /spoiler >}}

{{% callout note %}}

In der SI Vorlesung sowie Übung wird die Verteilungsfunktion der Zufallsvariable $\boldsymbol{x}$ als $F_{\boldsymbol{x}}(x)$ schreiben.

{{% /callout %}}

Differenz zwischen kumulativer Wahrscheinlichkeiten:

{{< math >}}
$$
F(b) - F(a) = P(a < x \leq b) = P(x\leq b) - P(x \leq a)
$$
{{< /math >}} 



### Stetige Zufallsvariable

Eine {{< hl >}}**stetige**{{< /hl >}} Zufallsvariable 

- ist **überabzählbar**, also nimmt *unendlich viele, nicht abzählbare* Werte an.
- meistens bei Messvorgängen der Fall (z.B. Zeit, Längen oder Temperatur)
- Skalenarten: Intervall- oder Rationalskala

Für stetige Zufallsvariable können wir die Wahrscheinlichkeit nur für **Intervalle** und NICHT für genaue Werte bestimmen.

- Es gibt doch unendlich viele Werte, also ist es unmöglich, ein exaktes Ergebnis festzulegen.
- z.B.
  - "Mit welcher Wahrscheinlichkeit ist eine zufällig gewählte Studentin zwischen 165cm und 170cm groß?"
- Man benutzt im stetigen Fall die **Verteilungsfunktion** zur Berechnung von Wahrscheinlichkeiten.

#### Dichtefunktion

Die {{< hl >}}**Dichtefunktion (Engl. Probability Density Function (PDF))**{{< /hl >}} oder **Dichte** beschreibt, "Wie dicht liegen die betrachteten Werte um einen beliebigen Punkt?"

{{< math >}}
$$
f(x): \mathbf{\Omega} \rightarrow \mathbb{R}^{+}
$$
{{< /math >}} 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-05-31%2022.24.46.png" alt="截屏2022-05-31 22.24.46" style="zoom:50%;" />



- Eigenschaften von $f$:

{{< math >}}


$$
\begin{array}{l}
f \text{ ist integrierbar}\\
f(x) \geq 0 \quad \forall x \in \mathbb{R} \\
\displaystyle \int_{-\infty}^{+\infty} f(x) \mathrm{d} x=1
\end{array}
$$
{{< /math >}} 

- Unterschied zu Wahrscheinlichkeitsfunktion

  - Die Dichtefunktion liefert nicht die Wahrscheinlichkeit, sondern NUR die "Wahrscheinlichkeitsdichte"

  - Bei der stetigen Zufallsvariable, überabzählbar und unendlich viele Ausprägung hat, ist die Wahrscheinlichkeit für jede konkrete Ausprägung gleich 0
    $$
    P(X=x) = 0 \quad \forall x \in \mathbb{R}
    $$

Die Wahrscheinlichkeit, dass $X$ einen Wert $x \in [a, b]$ annimmt , entspricht der Fläsche $S$

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-05-31%2022.37.24.png" alt="截屏2022-05-31 22.37.24" style="zoom:50%;" />

{{< math >}}
$$
P(a \leq x \leq b)=\int_{a}^{b} f(x) \mathrm{d} x=S
$$
{{< /math >}} 

{{% callout note %}}

In der SI Vorlesung sowie Übung wird die Dichtefunktion der Zufallsvariable $\boldsymbol{x}$ als $f_{\boldsymbol{x}}(x)$ schreiben.

{{% /callout %}}

#### Verteilungsfunktion

{{< math >}}
$$
F(x): \Omega \rightarrow[0,1], x \in \mathbb{R}
$$
{{< /math >}} 

{{< math >}}
$$
F(x)=\int f(x) \mathrm{d} x, \quad f(x)=\frac{F(x)}{\mathrm{d} x}
$$
{{< /math >}} 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-05-31%2022.24.46.png" alt="截屏2022-05-31 22.24.46" style="zoom:40%; float:left" />

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-05-31%2023.01.08.png" alt="截屏2022-05-31 23.01.08" style="zoom:40%; float:right" />



Die Verteilungsfunktion ist eigentlich die Fläche unter der Dichtfunktion:

{{< math >}}
$$
F(x)=P(X \leq x=c)=\int_{-\infty}^{c} f(x) \mathrm{d} x
$$
{{< /math >}} 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-05-31%2023.05.33.png" alt="截屏2022-05-31 23.05.33" style="zoom:50%;" />



Die Differenz zwischen zwei Verteilungsfunktion ist also:

{{< math >}}
$$
F(b)-F(a)=P(a \leq x \leq b)=\int_{a}^{b} f(x) \mathrm{d} x
$$
{{< /math >}} 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-05-31%2023.07.26.png" alt="截屏2022-05-31 23.07.26" style="zoom:50%;" />

#### Dichtefunktion vs. Verteilungsfunktion

- Dichtfunktion beschreibt, wie sind die Wahrscheinlichkeiten konkret verteilt?

- Verteilungsfunktion
  - Summieren der Wahrscheinlichkeiten $\rightarrow$ Bestimmung der Wahrscheinlichkeit für Intervall
  - liefert die Wahrscheinlichkeit dafür, dass ien Ereignis $\leq$ eines bestimmten Werted eintritt

### Diskrete Vs. Stetige Zufallsvariable

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
    <th class="tg-c3ow">Zufalls-<br>variable</th>
    <th class="tg-7btt"><span style="font-style:normal">Diskret</span></th>
    <th class="tg-7btt"><span style="font-style:normal">Stetig</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow"><span style="font-style:normal">Beispiel</span></td>
    <td class="tg-7btt"><span style="font-weight:400;font-style:normal">Würfelwurf</span></td>
    <td class="tg-c3ow">Zeit<br>Temperatur</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Wahrscheinlichkeit <br>für</td>
    <td class="tg-c3ow">bestimmter/konkreter Punkt<br>$P(X=x) \in [0, 1]$</td>
    <td class="tg-c3ow">NUR für Intervall<br>($P(X=x) = 0$)</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Wahrscheinlichkeitsfunktion/<br>Dichtefunktion</td>
    <td class="tg-c3ow"><span style="font-style:normal">Wahrscheinlichkeitsfunktion</span><br>$f(x): \Omega \rightarrow[0,1], x \in \mathbb{N}_{0}$<br>$f(x) = P(X=x)$<br>$\sum_{x \in \Omega} f(x)=1$</td>
    <td class="tg-c3ow">Dichtefunktion<br>$f(x): \mathbf{\Omega} \rightarrow \mathbb{R}^{+}$<br>$f$ ist integrierbar<br>$f(x) \geq 0 \quad \forall x \in \mathbb{R}$<br>$\displaystyle \int_{-\infty}^{+\infty} f(x) \mathrm{d} x=1$</td>
  </tr>
  <tr>
    <td class="tg-c3ow"><span style="font-style:normal">Verteilungsfunktion</span></td>
    <td class="tg-c3ow">$F(x): \boldsymbol{\Omega} \rightarrow[\mathbf{0}, \mathbf{1}], \boldsymbol{x} \in \mathbb{N}_{\mathbf{0}}$<br>$F(x)= P(X \leq x) = \sum_{x_{i} \leq x} f\left(x_{i}\right)$</td>
    <td class="tg-c3ow">$F(x): \Omega \rightarrow[0,1], x \in \mathbb{R}$<br>$F(x)=\int f(x) \mathrm{d} x, \quad f(x)=\frac{F(x)}{\mathrm{d} x}$</td>
  </tr>
</tbody>
</table>



## Erwartungswert, Varianz und Standardabweichung

### Erwartungswert

**Erwartungswert**: der Durchschnitt, wenn ein Versuch unendlich oft durchgeführt wird

- Notation: $\mu$, $E(x)$, $E\[x\]$, $E\\{x\\}$

### Varianz 

**Varianz** := die erwartete *quadratische* Abweichung vom Erwartungswert

- Je größer die Varianz, desto weiter streuen die Werte um $E(X)$
- Notationen: $\sigma^2$, $\operatorname{Var}(X)$, $\operatorname{Var}\[X\]$

### Standardabweichung

**Standardabweichung**: Streumaß, das die selbe Einheit wie $X$ hat

{{< math >}}
$$
\sigma=\sqrt{\operatorname{Var}(X)}
$$
{{< /math >}} 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/Section2Module7HighLowStandardDeviation.jpg" alt="Standard Deviation" style="zoom:75%;" />



### Summary

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
    <th class="tg-c3ow">Zufalls-<br>variable</th>
    <th class="tg-7btt"><span style="font-style:normal">Diskret</span></th>
    <th class="tg-7btt"><span style="font-style:normal">Stetig</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-7btt">Erwartungswert<br>($\mu$, $E(x)$)</td>
    <td class="tg-c3ow">$\sum_{i \in \Omega} x_{i} \cdot p_{i}$</td>
    <td class="tg-c3ow">$\int_{-\infty}^{+\infty} x^{1} \cdot f(x) \mathrm{d} x$</td>
  </tr>
  <tr>
    <td class="tg-7btt">Varianz<br>($\sigma^2$, $Var(x)$)</td>
    <td class="tg-c3ow">$\sum_{i \in \Omega}\left(x_{i}-\mu\right)^{2} \cdot p_{i}$</td>
    <td class="tg-c3ow">$\int_{-\infty}^{+\infty}(x-\mu)^{2} \cdot f(x) \mathrm{d} x$</td>
  </tr>
  <tr>
    <td class="tg-7btt">Standardabweichung<br>($\sigma$)</td>
    <td class="tg-c3ow">$\sqrt{Var(x)}$</td>
    <td class="tg-c3ow"><span style="font-weight:400;font-style:normal">$\sqrt{Var(x)}$</span></td>
  </tr>
</tbody>
</table>


## (Diracsche) Delta-Distribution / Delta-Funktion

### Definition

Die {{< hl >}}**Delta-Distribution**{{< /hl >}} (aka. **Dirac-Funktion**, **Dirac-Maß**, **Impulsfunktion**) ist eine spezielle irreguläre [Distribution](https://de.wikipedia.org/wiki/Distribution_(Mathematik)) mit [kompaktem](https://de.wikipedia.org/wiki/Kompakter_Raum) [Träger](https://de.wikipedia.org/wiki/Träger_(Mathematik)). 

$$
\begin{array}{c}
\delta(x)=0, \quad x \neq 0 \\\\
\displaystyle \int_{a}^{b} \delta(x) \mathrm{d} x=1, \quad a<0<b
\end{array}
$$



Illustration: Delta-Funktion im Ursprung wird als Pfeil bei $x=0$ dargestellt und repräsentiert eine Punktladung (Source: [Dirac'sche Delta-Funktion und ihre Eigenschaften](https://de.universaldenker.org/lektionen/235)).

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/dirac-delta-graph.svg" alt="Darstellung einer Delta-Funktion im Ursprung als Pfeil" style="width: 50%;" />



### Delta-Funktion im Koordinatenursprung

Betrachte ein Integral der Delta-Funktion zusammen mit einer **Testfunktion** $f(x)$

{{< math >}}
$$
\int_{a}^{b} f(x) \delta(x) \mathrm{d} x
$$
{{< /math >}} 

Denn $\delta(x)$ ist überall $0$, außer an der Stelle $x=0$.

$\Rightarrow$ $f(x)\delta(x)$ ist überall $0$, außer an der Stelle $x=0$. 

$\Rightarrow$ Im Integral bleibt nur der Funktionswert $f(0)$ erhalten, der nicht von $x$ abhängt.

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/dirac-delta-function-picks-function-value-at-origin-with-boundaries.svg" alt="Delta-Funktion pickt den Funktionswert am Ursprung in einem Intervall" style="width:50%;" />

Daher gilt:

{{< math >}}
$$
\int_{a}^{b} f(x) \delta(x) \mathrm{d} x= \int_{a}^{b} f(0)\delta(x) \mathrm{d} x=f(0) \underbrace{\int_{a}^{b} \delta(x)\mathrm{d} x}_{=1}  = f(0)
$$
{{< /math >}} 

### Eigenschaften

{{% callout note %}}
Bei Berechnen/Verweden/Überprüfen der Eigenschaften von Dirac-Funktion ist es wichtig, die [Substitutionsregel](https://de.wikipedia.org/wiki/Integration_durch_Substitution) zu verwenden.
{{% /callout %}}


#### Verschobene Delta-Funktion

Verschiebe die Ladung an eine andere Stelle auf der $x$-Achse (z.B an die Stelle $x=x_0$). Das Argument der Delta-Funktion wird zu $\delta(x-x_0)$.

Die verschobene Delta-Funktion mit einer anderen Funktion $f(x)$ im Integral multipliziert:

{{< math >}}
$$
\int_{a}^{b} f(x) \delta\left(x-x_{0}\right) \mathrm{d} x=f\left(x_{0}\right)
$$
{{< /math >}} 

{{< spoiler text="Beweis" >}}
![verschobene_Dirac_Fkt](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/verschobene_Dirac_Fkt.gif)
{{< /spoiler >}}


<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/shifted-dirac-delta-function.svg" alt="Verschobene Delta-Funktion pickt einen Funktionswert heraus" style="width:50%;" />



Nach rechts verschobene Delta-Funktion pickt den Wert $f(x_0)$ der Funktion an der Stelle $x=x_0$.

{{< spoiler text="Beispiel" >}}
![截屏2022-06-02 12.10.45](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-06-02%2012.10.45.png)
{{< /spoiler >}}

{{< spoiler text="Beispiel" >}}
Eine Delta-Funktion außerhlad der Integrationsgrenzen
![截屏2022-06-02 12.11.43](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-06-02%2012.11.43.png)
{{< /spoiler >}}

#### Delta-Funktion ist symmetrisch (gerade)

{{< math >}}
$$
\delta(x) = \delta(-x)
$$

{{< spoiler text="Beweis" >}}
![截屏2022-06-02 12.47.40](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-06-02%2012.47.40.png)
{{< /spoiler >}}


{{< /math >}} 

#### Skaliertes Argument der Delta-Funktion

{{< math >}}
$$
\int_{a}^{b} f(x) \delta(|k| x) \mathrm{d} x=\frac{1}{|k|} f(0)
$$
{{< /math >}} 

{{< spoiler text="Beweis" >}}
![截屏2022-06-02 16.27.14](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-06-02%2016.27.14.png)
{{< /spoiler >}}

#### Hintereinanderausführung

{{< math >}}
$$
\int_{-\infty}^{\infty} f(x) \delta(g(x)) \mathrm{d} x=\sum_{i=1}^{n} \frac{f\left(x_{i}\right)}{\left|g^{\prime}\left(x_{i}\right)\right|}
$$
{{< /math >}} 

wobei $g(x_i) = 0$ und $g^\prime(x_i) \neq 0$.



{{< spoiler text="Beweis" >}}

Substituiere 
{{< math >}}
$$
u := g(x)
$$
{{< /math >}}
Dann gilt:
{{< math >}}
$$
\begin{aligned}
x &= g^{-1}(u) \\\\
\frac{du}{dx} &= g^\prime(x) = g^\prime(g^{-1}(u))
\end{aligned}
$$
{{< /math >}}
Da $\delta(x) \neq 0$ nur bei $x = 0$, können wir den Bereich des Integrals in kleine Intervalle um jede Nullstelle $x_i$ von $g(x)$ aufteilen, wobei $g(x)$ monoton und somit invertierbar ist.

{{< math >}}
$$
\begin{aligned}
\int f(x) \delta(g(x)) d x &=\sum_{i} \int_{x_{i}-\varepsilon_{i}}^{x_{i}+\varepsilon_{i}} f(x) \delta(g(x)) d x \\\\
&=\sum_{i} \int_{g\left(x_{i}-\varepsilon_{i}\right)}^{g\left(x_{i}+\varepsilon_{i}\right)} f\left(g^{-1}(u)\right) \delta(u) \frac{1}{g^{\prime}\left(g^{-1}(u)\right)} d u \\\\
&=\sum_{i} \int_{g\left(x_{i}-\varepsilon_{i}\right)}^{g\left(x_{i}+\varepsilon_{i}\right)} \frac{f\left(g^{-1}(u)\right)}{g^{\prime}\left(g^{-1}(u)\right)} \delta(u) d u \\\\
&=\sum_{i} \int_{g\left(x_{i}-\varepsilon_{i}\right)}^{g\left(x_{i}+\varepsilon_{i}\right)} \frac{f\left(x_{i}\right)}{g^{\prime}\left(x_{i}\right)} \delta(u) d u \quad(\ast)
\end{aligned}
$$
{{< /math >}} 

{{< math >}}$g^\prime (x_i) > 0${{< /math >}}:

{{< math >}}
$$
\begin{aligned}
(\ast) &=\sum\_{i} \frac{f\left(x\_{i}\right)}{g^{\prime}\left(x\_{i}\right)} \underbrace{\int\_{g\left(x\_{i}-\varepsilon\_{i}\right)}^{g\left(x\_{i}+\varepsilon\_{i}\right)} \delta(u) d u}\_{=1} \\\\
&=\sum\_{i} \frac{f\left(x\_{i}\right)}{g^{\prime}\left(x\_{i}\right)} \\\\
&=\sum\_{i} \frac{f\left(x\_{i}\right)}{|g^{\prime}\left(x\_{i}\right)|}
\end{aligned}
$$
{{< /math >}} 



{{< math >}}$g^\prime (x_i) < 0${{< /math >}}:

Dann ist 

{{< math >}}
$$
g(x_i + \varepsilon_i) < g(x_i - \varepsilon_i)
$$
{{< /math >}} 

Daher

{{< math >}}
$$
\begin{aligned}
(\ast) &=\sum_{i} \int\_{g\left(x\_{i}+\varepsilon\_{i}\right)}^{g\left(x\_{i}-\varepsilon\_{i}\right)} \frac{f\left(x\_{i}\right)}{g^{\prime}\left(x\_{i}\right)} \delta(u) d u \\\\
&=\sum\_{i} \int\_{g\left(x\_{i}-\varepsilon\_{i}\right)}^{g\left(x\_{i}+\varepsilon_{i}\right)}-\frac{f\left(x_{i}\right)}{g^{\prime}\left(x\_{i}\right)} \delta(u) d u \\\\
&=\sum\_{i} \int_{g\left(x\_{i}-\varepsilon\_{i}\right)}^{g\left(x\_{i}+\varepsilon\_{i}\right)} \frac{f\left(x\_{i}\right)}{\left|g^{\prime}\left(x_{i}\right)\right|} \delta(u) d u \\\\
&=\sum\_{i} \frac{f\left(x\_{i}\right)}{\left|g^{\prime}\left(x\_{i}\right)\right|} \underbrace{\int\_{g\left(x\_{i}-\varepsilon\_{i}\right)}^{g\left(x\_{i}+\varepsilon\_{i}\right)} \delta(u) d u}\_{=1} \\\\
&=\sum_{i} \frac{f\left(x\_{i}\right)}{\left|g^{\prime}\left(x\_{i}\right)\right|}
\end{aligned}
$$
{{< /math >}} 

Also

{{< math >}}
$$
\int_{-\infty}^{\infty} f(x) \delta(g(x)) \mathrm{d} x=\sum_{i=1}^{n} \frac{f\left(x_{i}\right)}{\left|g^{\prime}\left(x_{i}\right)\right|} \quad (\square)
$$
{{< /math >}} 

{{< /spoiler >}}

Ref: [Dirac Delta Function of a Function](https://math.stackexchange.com/questions/276583/dirac-delta-function-of-a-function)









## Reference

- Tutorials

  - [Statistik](https://welt-der-bwl.de/Statistik): Zusammenfassung von Statistik

  - [Statistik Tutorials von Studyflix](https://studyflix.de/statistik) 👍

  - Youtube channel "[Math by Daniel Jung](https://www.youtube.com/c/MathebyDanielJung)" (klar erklärt mit Beispiele) 👍


- Zufallsvariable
  - Wahrscheinlichkeits-, Dichte- und Verteilungsfunktion diskreter und stetiger Zufallsvariablen
  
    {{< youtube _lq7zfecSpw>}}

- Erwartungswert

  - Kenngrößen (Momente) von Zufallsvariablen I: Erwartungswert, Varianz, Standardabweichung

    {{< youtube KKr-aLFrSVA>}}

- Dirac-Distribution
  -  [Dirac'sche Delta-Funktion und ihre Eigenschaften](https://de.universaldenker.org/lektionen/235)
