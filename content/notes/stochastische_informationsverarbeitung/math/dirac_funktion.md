---
# ===== Title, summary, and position in the left sidebar =====
linktitle: Delta-Distribution # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 102
# ============================================================

# ========== Basic metadata ==========
title: (Diracsche) Delta-Distribution / Delta-Funktion
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


## Definition

Die {{< hl >}}**Delta-Distribution**{{< /hl >}} (aka. **Dirac-Funktion**, **Dirac-Maß**, **Impulsfunktion**) ist eine spezielle irreguläre [Distribution](https://de.wikipedia.org/wiki/Distribution_(Mathematik)) mit [kompaktem](https://de.wikipedia.org/wiki/Kompakter_Raum) [Träger](https://de.wikipedia.org/wiki/Träger_(Mathematik)). 

$$
\begin{array}{c}
\delta(x)=0, \quad x \neq 0 \\\\
\displaystyle \int_{a}^{b} \delta(x) \mathrm{d} x=1, \quad a<0<b
\end{array}
$$



Illustration: Delta-Funktion im Ursprung wird als Pfeil bei $x=0$ dargestellt und repräsentiert eine Punktladung (Source: [Dirac'sche Delta-Funktion und ihre Eigenschaften](https://de.universaldenker.org/lektionen/235)).

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/dirac-delta-graph.svg" alt="Darstellung einer Delta-Funktion im Ursprung als Pfeil" style="width: 50%;" />



## Delta-Funktion im Koordinatenursprung

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

## Eigenschaften

{{% callout note %}}
Bei Berechnen/Verweden/Überprüfen der Eigenschaften von Dirac-Funktion ist es wichtig, die [Substitutionsregel](https://de.wikipedia.org/wiki/Integration_durch_Substitution) zu verwenden.
{{% /callout %}}


### Verschobene Delta-Funktion

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

### Delta-Funktion ist symmetrisch (gerade)

{{< math >}}
$$
\delta(x) = \delta(-x)
$$

{{< spoiler text="Beweis" >}}
![截屏2022-06-02 12.47.40](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-06-02%2012.47.40.png)
{{< /spoiler >}}


{{< /math >}} 

### Skaliertes Argument der Delta-Funktion

{{< math >}}
$$
\int_{a}^{b} f(x) \delta(|k| x) \mathrm{d} x=\frac{1}{|k|} f(0)
$$
{{< /math >}} 

{{< spoiler text="Beweis" >}}
![截屏2022-06-02 16.27.14](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-06-02%2016.27.14.png)
{{< /spoiler >}}

### Hintereinanderausführung

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

Daher❤️

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

# Reference

-  [Dirac'sche Delta-Funktion und ihre Eigenschaften](https://de.universaldenker.org/lektionen/235)