---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 103
# ============================================================

# ========== Basic metadata ==========
title: Zufallsvariable
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

## Zufallsvariablen

{{% callout warning %}}

Zufallsvariablen werden auf den SI-Übungsblättern durch kleine, fettgedruckte Buchstaben gekennzeichnet, z.B. $X$. 

Diese Notation wird nicht auf den handschriftlichen Mitschrieben umgesetzt, sodass Zufallsvariablen und „normale“ Variablen meistens aus dem Kontext heraus unterschieden werden müssen. 🤪

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

> Man schreibt für die „Dichte“ einer diskreten Zufallsvariablen, deren Einzelwahrscheinlichkeiten $p_n = P(X = x_n)$ gegeben sind, auch
> $$
> f_{X}(x)=\sum_{n=1}^{\infty} \mathrm{P}\left(X=x_{n}\right) \delta\left(x-x_{n}\right)=\sum_{n=1}^{\infty} p_{n} \delta\left(x-x_{n}\right)
> $$
>
> - $\delta(\cdot)$: [Delta-Distribution]({{< relref "dirac_funktion" >}})

#### Verteilungsfunktion

Die {{< hl >}}**Verteilungsfunktion (aka. Kumulative Wahrscheinlichkeitsdichte, Engl,. Cumulative Distribution Function (CDF))**{{< /hl >}} gibt an, mit welcher Wahrscheinlichkeit das Ergebnis des Zufallsexperiments *kleiner oder gleich* eines bestimmten Wertes ist.

- Dafür werden alle Ergebnisse bis zu diesem Wert aggregiert, also „aufaddiert“. Deshalb spricht man auch oft von einer **kumulativen Verteilungsfunktion**.

Um die diskrete Verteilungsfunktion zu erhalten, werden schrittweise alle Wahrscheinlichkeitswerte kumuliert. Das heißt, man bildet das Integral unter der Wahrscheinlichkeitsfunktion.

{{< math >}}
$$
F(x): \boldsymbol{\Omega} \rightarrow[\mathbf{0}, \mathbf{1}], X \in \mathbb{N}_{\mathbf{0}}
$$
{{< /math >}} 

{{< math >}}
$$
F(x)= P(X \leq x) = \sum_{x_{i} \leq x} f\left(x_{i}\right)
$$
{{< /math >}} 

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-05-31%2022.20.17.png" alt="截屏2022-05-31 22.20.17" style="zoom: 40%; float: left" />

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-05-31%2022.43.01.png" alt="截屏2022-05-31 22.43.01" style="zoom:40%; float:right" />



Eigenschaften

- {{< math >}}$\lim _{x \rightarrow-\infty} F_{X}(x)=0 ; \lim _{x \rightarrow \infty} F_{X}(x)=1${{< /math >}} 
- $F(X)$ ist monoton steigend und rechtseitig stetig

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

In der SI Vorlesung sowie Übung wird die Verteilungsfunktion der Zufallsvariable $X$ als $F_{X}(x)$ schreiben.

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

In der SI Vorlesung sowie Übung wird die Dichtefunktion der Zufallsvariable $X$ als $f_{X}(x)$ schreiben.

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
    <td class="tg-c3ow">$F(x): \boldsymbol{\Omega} \rightarrow[\mathbf{0}, \mathbf{1}], X \in \mathbb{N}_{\mathbf{0}}$<br>$F(x)= P(X \leq x) = \sum_{x_{i} \leq x} f\left(x_{i}\right)$</td>
    <td class="tg-c3ow">$F(x): \Omega \rightarrow[0,1], x \in \mathbb{R}$<br>$F(x)=\int f(x) \mathrm{d} x, \quad f(x)=\frac{F(x)}{\mathrm{d} x}$</td>
  </tr>
</tbody>
</table>



## Kenntwerte von Zufallsvariablen

### Erwartungswert

{{< hl >}}**Erwartungswert**{{< /hl >}} (auch **Mittelwert**) : der Durchschnitt, wenn ein Versuch unendlich oft durchgeführt wird

{{< math >}}
$$
E_{f_X}\{X\} = \hat{X} = \mu_{X} = \int_{-\infty}^{\infty} x f_{X}(x) d x
$$


{{< /math >}} 

- Notation: $\mu$, $E(X)$, $E\[X\]$, $E\\{X\\}$

#### Rechenregeln

{{< math >}}$\mathrm{E}_{f_{X}}\{aX + b\}=a \mathrm{E}_{f_{X}}\{X\}+b${{< /math >}} 

{{< spoiler text="Beweis" >}}
$$
\begin{array}{ll}
&\mathrm{E}\_{f\_{X}}\\{a X+b\\} \\\\
=&\int\_{-\infty}^{\infty}(a x+b) f\_{X}(x) \mathrm{d} x \\\\
=&a \int\_{-\infty}^{\infty} x f\_{X}(x) \mathrm{d} x+b \int\_{-\infty}^{\infty} f\_{X}(x) \mathrm{d} x \\\\
=&a \cdot \mathrm{E}\_{f_{X}}\\{X\\}+b \cdot 1
\end{array}
$$
{{< /spoiler >}}

Mehr Regeln:

{{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-04%2010.52.26.png" caption="Basic expectation rules. (Source: [kalmanfilter.net](https://www.kalmanfilter.net/background2.html))" numbered="true" >}}

### $k$-te Moment

Der Erwartungswert 

{{< math >}}
$$
\mathrm{E}_{f_X}\left\{X^{k}\right\}=\int_{-\infty}^{\infty} x^{k} f_{X}(x) \mathrm{d} x
$$
{{< /math >}} 

das {{< hl >}}**$k$-te Moment**{{< /hl >}} der Zufallsvariable $X$.

Der Erwartungswert 

{{< math >}}
$$
\mathrm{E}_{f_X}\left\{\left(X-\mathrm{E}\{X\}\right)^{k}\right\}=\int_{-\infty}^{\infty}\left(x-\mu_{X}\right)^{k} f_{X}(x) \mathrm{d} x
$$
{{< /math >}} 

ist das {{< hl >}}**$k$-te zentrale Moment**{{< /hl >}} der Zufallsvariable $X$.

### Varianz 

**Varianz** := die erwartete *quadratische* Abweichung vom Erwartungswert

{{< math >}}
$$
E_{f_X}\{(X - \mu_X)^2\} = \operatorname{Var}(X) = \sigma_X^2
$$


{{< /math >}} 

- das zweite zentrale Moment

- Je größer die Varianz, desto weiter streuen die Werte um $E(X)$
- Notationen: $\sigma^2$, $\operatorname{Var}(X)$, $\operatorname{Var}\[X\]$

#### Rechenregeln

{{< math >}}$\operatorname{Var}_{f_X}\{aX+b\} = a^2 \operatorname{Var}_{f_X}\{X\}${{< /math >}} 

{{< spoiler text="Beweis" >}}
$$
\begin{array}{l}
&\operatorname{Var}\_{f\_{X}}\\{a X+b\\} \\\\
=&\mathrm{E}\_{f\_{X}}\left\\{\left(a X+b-\mathrm{E}\_{f\_{X}}\\{a X+b\\}\right)^{2}\right\\} \\\\
=&\mathrm{E}\_{f\_{X}}\left\\{\left(a X+b-\left(a \mu\_{X}+b\right)\right)^{2}\right\\}\\\\
=&\mathrm{E}\_{f\_{X}}\left\\{\left(a\left(X-\mu\_{X}\right)\right)^{2}\right\\} \\\\
=&\int\_{-\infty}^{\infty}\left(a\left(X-\mu\_{X}\right)\right)^{2} f\_{X}(x) \mathrm{d} x \\\\
=&a^{2} \int\_{-\infty}^{\infty}\left(X-\mu\_{X}\right)^{2} f\_{X}(x) \mathrm{d} x \\\\
=&a^{2} \mathrm{E}\_{f\_{X}}\left\\{\left(X-\mu\_{X}\right)^{2}\right\\} \\\\
=&a^{2} \operatorname{Var}\_{f\_{X}}\\{X\\}
\end{array}
$$
{{< /spoiler >}}

</br>

{{< math >}}$\operatorname{Var}_{f_{X}}\{X\}=\mathrm{E}_{f_{X}}\left\{X^{2}\right\}-\left(\mathrm{E}_{f_{X}}\{X\}\right)^{2}${{< /math >}} 

{{< spoiler text="Beweis" >}}
$$
\begin{aligned}
    \operatorname{Var}\_{f\_{X}}\\\{X\\}=& \int\_{-\infty}^{\infty}\left(x-\mathrm{E}\_{f\_{X}}\\{X\\}\right)^{2} f\_{X}(x) \mathrm{d} x \\\\
    =& \int\_{-\infty}^{\infty}\left(x-\mu\_{X}\right)^{2} f\_{X}(x) \mathrm{d} x \\\\
    =& \int\_{-\infty}^{\infty}\left(x^{2}-2 x \mu\_{X}+\mu\_{X}^{2}\right) f\_{X}(x) \mathrm{d} x \\\\
    =& \int\_{-\infty}^{\infty} x^{2} f\_{X}(x) \mathrm{d} x-2 \mu\_{X} \int\_{-\infty}^{\infty} x f\_{X}(x) \mathrm{d} x+\mu\_{X}^{2} \int\_{-\infty}^{\infty} f\_{X}(x) \mathrm{d} x \\\\
    =& \mathrm{E}\_{f\_{X}}\left\\{X^{2}\right\\}-2 \mu\_{X} \mathrm{E}\_{f\_{X}}\\{X\\}+\mu\_{X}^{2} \cdot 1 \\\\
    =& \mathrm{E}\_{f\_{X}}\left\\{X^{2}\right\\}-2 \mu\_{X} \mu\_{X}+\mu\_{X}^{2} \cdot 1 \\\\
    =& \mathrm{E}\_{f\_{X}}\left\\{X^{2}\right\\}-\mu\_{X}^{2}
    \end{aligned}
$$
{{< /spoiler >}}

Mehr Regeln:

{{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-04%2010.55.30.png" caption="Basic variance and covariance rules. (Source: [kalmanfilter.net](https://www.kalmanfilter.net/background2.html))" numbered="true" >}}

{{< spoiler text="Beweis für Regel 10" >}}
![截屏2022-07-04 10.57.26](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-04%2010.57.26.png)
{{< /spoiler >}}

{{< spoiler text="Beweis für Regel 11" >}}
![截屏2022-07-04 10.57.54](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-04%2010.57.54.png)
{{< /spoiler >}}

{{< spoiler text="Beweis für Regel 13" >}}
![截屏2022-07-04 10.59.10](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-04%2010.59.10.png)
{{< /spoiler >}}

{{< spoiler text="Beweis für Regel 14" >}}
![截屏2022-07-04 10.59.30](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-07-04%2010.59.30.png)
{{< /spoiler >}}


### Standardabweichung

**Standardabweichung**: Streumaß, das die selbe Einheit wie $X$ hat

{{< math >}}
$$
\sigma=\sqrt{\operatorname{Var}(X)}
$$
{{< /math >}} 

Groß $\sigma$ $\rightarrow$ große Streuung

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/Section2Module7HighLowStandardDeviation.jpg" alt="Standard Deviation" style="zoom:75%;" />



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
    <td class="tg-c3ow">$\int_{-\infty}^{+\infty} x \cdot f(x) \mathrm{d} x$</td>
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

### Normalverteilte Zufallsvariable

Ein {{< hl >}}**normalverteilte Zufallsvariable**{{< /hl >}} $X$ hat die Dichte

{{< math >}}
$$
f_{X}(x)=\mathcal{N}\left(x-\mu, \sigma^{2}\right)=\frac{1}{\sqrt{2 \pi} \sigma} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^{2}}
$$
{{< /math >}} 

Ihr $k$-tes zentrales Moment ist allgemein

{{< math >}}
$$
\mathrm{E}_{f_{X}}\left\{(X-\mu)^{k}\right\}=\left\{\begin{array}{ll}
1 \cdot 3 \cdot 5 \cdots(k-1) \sigma^{k} & \text { falls } k \text { gerade } \\
0 & \text { falls } k \text { ungerade }
\end{array}\right.
$$
{{< /math >}}

Die Normalverteilung ist also vollständig durch $\mu$ und $\sigma$ charakterisiert. 

### Standardisierte Zufallsvariable

Eine Zufallsvariable $X$ mit dem Erwartungswert $\mu_X = E_{f_X}\{X\}$ und der Varianz $\sigma_X^2$ wird durch

{{< math >}}
$$
Y = \frac{X - \mu_X}{\sigma_X}
$$
{{< /math >}} 

in eine {{< hl >}}**standardisierte Zufallsvariable**{{< /hl >}} $Y$, die den Erwartungswert 0 und die Varianz 1 besitzt, transformiert.

### Modalwert, Quantil, Median

Ein Wert, für den die Dichtefunktion $f_X(x)$ ein lokales Maximum annimmt, heißt {{< hl >}}**Modalwert**{{< /hl >}} der stetigen Zufallsvariablen $X$.

Ein Wert $x_p$, der den Ungleichungen

{{< math >}}
$$
P(X < x_p) \leq p, \quad P(X > x_p) \leq 1 - p \quad (0 < p < 1)
$$
{{< /math >}} 

genügt, heißt {{< hl >}}**$p$-tes Quantil**{{< /hl >}}. 

- Für eine stetige Zufallsvariable X ist ein $p$-tes Quantil $x_p$ gegeben durch $F_X(x_p) = p$
- Ein Quantil der Ordnung $p=\frac{1}{2}$ heißt {{< hl >}}**Median**{{< /hl >}} der Zufallsvariable $X$
- Für normalverteilte Zufallsvariablen fallen Erwartungswert, Modalwert und Median zusammen.

## Reference

- Wahrscheinlichkeits-, Dichte- und Verteilungsfunktion diskreter und stetiger Zufallsvariablen
  
    {{< youtube _lq7zfecSpw>}}

- Erwartungswert

  - Kenngrößen (Momente) von Zufallsvariablen I: Erwartungswert, Varianz, Standardabweichung

    {{< youtube KKr-aLFrSVA>}}