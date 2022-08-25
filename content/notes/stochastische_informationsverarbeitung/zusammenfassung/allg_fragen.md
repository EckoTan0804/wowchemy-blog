---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 710
# ============================================================

# ========== Basic metadata ==========
title: Allgemeine Fragen
date: 2022-08-18
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

## Vorlesung in eigenen Worten zusammenfassen

Die SI Vorlesung vermittelt die fundamentalen und formalen Grundlagen der Zustandsschätzung rund um Prädiktion und Filterung.



## Vier behandelten Typen von Systemen

erläutern

- Nennen
- Zusammenhänge
- Unterschiede
- Limitierungen
- Komplexität einer Implementierung der zugehörigen Schätzer



4 Type von Systeme

- Wertediskrete Systeme
- Wertekontinuierliche lineare Systeme
- Wertekontinuierliche und schwach nichtlineare Systeme
- Allgemeine Systeme



## Wann kann man mit 1D-Messungen auch auf einen 3D-Zustand schließen? Wie sehen dann die Unsicherheits-Ellipsen über der Zeit aus?





## Definition

### Induzierte Nichtlinearität

### Bedingte Unabhängigkeit

Zwei Variable $A, B$ sind bedingt unabhängig, gegeben $C$ $\Leftrightarrow$

{{< math >}}
$$
P(A, B | C) = P(A | C) P(B | C)
$$
{{< /math >}} 

Damit äquivalent sind die Formulierungen:
{{< math >}}
$$
P(A | B,C) = P(A | C) \qquad P(B | A,C) = P(B | C)
$$
{{< /math >}} 

### Zustand

(Script P19)

The state of a dynamic system is defined as the smallest set of variables, the so called **state variables**, that completely determine the behavior of the system for $t \geq t_0$ given their values at $t_0$ together with the input function for $t \geq t_0$.

- When modeling a system, the choice of state variables is not unique. 
- State variables do not need be physically existent. They also do not need to be measurable.

> Der Zustand eines dynamischen Systems ist definiert als die kleinste Menge von Variablen, den so genannten **Zustandsvariablen**, die das Verhalten des Systems für $t \geq t_0$ vollständig bestimmen/beschreiben, wenn man ihre Werte bei $t_0$ zusammen mit der Eingangsfunktion für $t \geq t_0$ betrachtet.

### Zustandsschätzung

Rekonstruktion des internen Zustands aus Messungen und Eingängen

### Komplexität einer Rekursion

### Dichtefunktion, Likelihood

**Verteilungsfunktion** oder **kumulative Wahrscheinlichkeitsdichte** $F_{\boldsymbol{x}}(x)$ der Zufallsvariablen $\boldsymbol{x}$

{{< math >}}
$$
F_{\boldsymbol{x}}: \mathbb{R} \rightarrow[0,1] \qquad F_{\boldsymbol{x}}(x):=\mathrm{P}(\boldsymbol{x} \leq x)
$$
{{< /math >}} 

Eigenschaften von $F_{\boldsymbol{x}}(x)$

- {{< math >}}$\lim _{x \rightarrow-\infty} F_{\boldsymbol{x}}(x)=0${{< /math >}} 
- {{< math >}}$\lim _{x \rightarrow\infty} F_{\boldsymbol{x}}(x)=1${{< /math >}} 
- monoton steigend und rechtsseitig stetig.

Bei stetiger Zufallsvariable:

{{< math >}}
$$
F_{\boldsymbol{x}}(x)=\int_{-\infty}^{x} f_{\boldsymbol{x}}(u) \mathrm{d} u
$$
{{< /math >}} 

$f_{\boldsymbol{x}}(x)$ heißt **Dichte** von $x$.

"Dichte" einer diskreten Zufallsvariable:

{{< math >}}
$$
f_{\boldsymbol{x}}(x)=\sum_{n=1}^{\infty} \mathrm{P}\left(\boldsymbol{x}=x_{n}\right) \delta\left(x-x_{n}\right)=\sum_{n=1}^{\infty} p_{n} \delta\left(x-x_{n}\right)
$$
{{< /math >}} 

### Zufallsvariable

{{% callout note %}}

Üb 1, A4, A5

{{% /callout %}}

Eine **Zufallsvariable** ist eine numerische Beschreibung des Ergebnisses eines Zufallsexperiments. Es handelt sich um eine Funktion, die ein Ergebnis $\omega$ aus einem Ergebnisraum $\Omega$ in den Raum $\mathbb{R}$ der reellen Zahlen abbildet

{{< math >}}
$$
\boldsymbol{x}=\boldsymbol{x}(\omega): \Omega \rightarrow \mathbb{R}
$$
{{< /math >}} 

Zwei Typen

- **Diskret**: Ergebnisse sind endlich oder höchstens abzählbar unendlich
- **Kontinuierlich**: Ereignis- und Wertemenge ist überabzählbaren.

#### Momente

{{% callout note %}}

Üb 2, A1.1

{{% /callout %}}

**Erwartungswert** (Mittelwert, 1-te Moment) der Zufallsvariablen $\boldsymbol{x}$:

{{< math >}}
$$
\mathrm{E}_{f_{\boldsymbol{x}}}\{\boldsymbol{x}\}=\hat{\boldsymbol{x}}=\mu_{\boldsymbol{x}}=\int_{-\infty}^{\infty} x f_{\boldsymbol{x}}(x) \mathrm{d} x
$$
{{< /math >}} 

**$k$-te Moment** der Zufallsvariablen $\boldsymbol{x}$:
{{< math >}}
$$
\mathrm{E}_{f_{\boldsymbol{x}}}\left\{\boldsymbol{x}^{k}\right\}=\int_{-\infty}^{\infty} x^{k} f_{\boldsymbol{x}}(x) \mathrm{d} x
$$
{{< /math >}} 

**$k$-te zentrale Moment** der Zufallsvariablen $\boldsymbol{x}$:

{{< math >}}
$$
\mathrm{E}_{f_{\boldsymbol{x}}}\left\{\left(\boldsymbol{x}-\mathrm{E}_{f_{\boldsymbol{x}}}\{\boldsymbol{x}\}\right)^{k}\right\}=\int_{-\infty}^{\infty}\left(x-\mu_{\boldsymbol{x}}\right)^{k} f_{\boldsymbol{x}}(x) \mathrm{d} x
$$
{{< /math >}} 

Varianz (2-te zentral Moment) der Zufallsvariablen $\boldsymbol{x}$:

{{< math >}}
$$
\mathrm{E}_{f_{\boldsymbol{x}}}\left\{\left(\boldsymbol{x}-\mathrm{E}_{f_{\boldsymbol{x}}}\{\boldsymbol{x}\}\right)^{2}\right\}=\int_{-\infty}^{\infty}\left(x-\mu_{\boldsymbol{x}}\right)^{2} f_{\boldsymbol{x}}(x) \mathrm{d} x
$$
{{< /math >}} 

- $\sigma_{\boldsymbol{x}}$: Standardabweichung der Zufallsvariablen $\boldsymbol{x}$

### 2-dim. Zufallsvariable

{{% callout note %}}

Üb 2, A2.2

{{% /callout %}}

$\underline{X}$ sei eine zweidimensionale Zufallsvariable mit der Dichte $f(\underline{X})=f_{\underline{X}}\left(x_{1}, x_{2}\right)$.

**Randdichte**

{{< math >}}
$$
\begin{array}{l}
f_{X_{1}}\left(x_{1}\right)=\int_{-\infty}^{\infty} f_{\underline{X}}\left(x_{1}, x_{2}\right) \mathrm{d} x_{2} \\
f_{X_{2}}\left(x_{2}\right)=\int_{-\infty}^{\infty} f_{\underline{X}}\left(x_{1}, x_{2}\right) \mathrm{d} x_{1}
\end{array}
$$
{{< /math >}} 

**Bedingte Dichte**

Bedingte Dichte von $x_1$

{{< math >}}
$$
f_{X_{1}}\left(x_{1} \mid X_{2}=x_{2}\right)=\frac{f_{\underline{X}}\left(x_{1}, x_{2}\right)}{f_{X_{2}}\left(x_{2}\right)}
$$
{{< /math >}} 

Bedingte Dichte von $x_2$

{{< math >}}
$$
f_{X_{2}}\left(x_{2} \mid X_{1}=x_{1}\right)=\frac{f_{\underline{X}}\left(x_{1}, x_{2}\right)}{f_{X_{1}}\left(x_{1}\right)}
$$
{{< /math >}} 

### Unabhängigkeit und Unkorreliertheit von Zufallsvariablen

{{% callout note %}}

Üb 2, A2.3

{{% /callout %}}

$X, Y$ sind unabhängig $\Leftrightarrow$

{{< math >}}
$$
f_{X, Y}(x, y)=f_{X}(x) \cdot f_{Y}(y)
$$
{{< /math >}} 

Damit gilt auch

{{< math >}}
$$
f_{X}(x \mid Y=y)=f_{X}(x)
$$
{{< /math >}} 

Die **Kovarianz** {{< math >}}$\sigma_{X, Y}=\operatorname{Cov}_{\boldsymbol{f}_{X, Y}}\{X, Y\}${{< /math >}}  von $X$ und $Y$:

{{< math >}}
$$
\sigma_{X, Y}=\operatorname{Cov}_{f_{X, Y}}\{X, Y\}=\mathrm{E}\{(X-\mathrm{E}\{X\}) \cdot(Y-\mathrm{E}\{Y\})\}=\mathrm{E}\left\{\left(X-\mu_{x}\right) \cdot\left(Y-\mu_{y}\right)\right\}
$$
{{< /math >}} 

Der **Korrelationskoeffizient** von $X$ und $Y$:

{{< math >}}
$$
\rho_{X, Y}=\frac{\sigma_{X, Y}}{\sigma_{X} \cdot \sigma_{Y}} \in [-1, 1]
$$
{{< /math >}} 

- $\left|\rho_{X, Y}\right|=1$: $X$ und $Y$ sind maximal ähnlich
- $\left|\rho_{X, Y}\right|=0$: $X$ und $Y$ sind komplett unähnlich (*i.e.*, $X$ und $Y$ sind **unkorreliert**)

Unabhängigkeit und Unkorreliertheit:

{{< math >}}
$$
\text{Unabhängigkeit} \underset{\text{+ Normalverteilung}}{\rightleftharpoons} \text{Unkorreliertheit}
$$
{{< /math >}} 

### Erwartungswert

{{% callout note %}}

- Üb 1, A7
- Üb 2, A3.4

{{% /callout %}}

Der **Erwartungswert** kann interpretiert werden als Mittelwert aller möglichen Werte $x_n$, die eine (diskrete) Zufallsvariable $\boldsymbol{x}$ annehmen kann. Dabei werden die Werte entsprechend ihrer Auftretenswahrscheinlichkeit $p_n$ gewichtet.

{{< math >}}
$$
\mathrm{E}\{\boldsymbol{x}\}=\sum_{n=1}^{N} x_{n} p_{n}
$$
{{< /math >}} 

Kontinuierlicher Fall:

{{< math >}}
$$
\mathrm{E}_{f_\boldsymbol{x}}\{\boldsymbol{x}\} = \int_{-\infty}^{\infty}x f_\boldsymbol{x}(x) dx
$$
{{< /math >}} 

Erwartungswert für Funktionen einer Zufallsvariable:

{{< math >}}
$$
\mathrm{E}_{f_{\boldsymbol{x}}}\{g(\boldsymbol{x})\}=\int_{-\infty}^{\infty} g(x) f_{\boldsymbol{x}}(x) \mathrm{d} x
$$
{{< /math >}} 

Recehenregeln:

- {{< math >}}$\mathrm{E}_{f_{X}}\{a X+b\}=a \mathrm{E}_{f_{X}}\{X\}+b${{< /math >}} 
- $a$ ist eine Konstante: {{< math >}}$E(a)=a${{< /math >}} 
- {{< math >}}$E(X \pm Y)=E(X) \pm E(Y)${{< /math >}} 
- {{< math >}}$E(XY) = E(x) E(Y)${{< /math >}}, falls $x, Y$ unabhängig



### Varianz

{{< math >}}
$$
E_{f_X}\{(X - \mu_X)^2\} = \operatorname{Var}(X) = \sigma_X^2
$$


{{< /math >}} 

Rechenregeln:

- {{< math >}}$\operatorname{Var}_{f_X}\{aX+b\} = a^2 \operatorname{Var}_{f_X}\{X\}${{< /math >}} 
- {{< math >}}$\operatorname{Var}_{f_{X}}\{X\}=\mathrm{E}_{f_{X}}\left\{X^{2}\right\}-\left(\mathrm{E}_{f_{X}}\{X\}\right)^{2}${{< /math >}} 
- $a$ is eine Konstante
  - $\operatorname{Var}_{f_X}\{a\} = 0$
  - {{< math >}}$\operatorname{Var}_{f_X}\{a \pm X\} = \operatorname{Var}_{f_X}\{X\}${{< /math >}} 
- {{< math >}}$\operatorname{Var}\{X, Y\} = E\{XY\} - \mu_X \mu_Y ${{< /math >}} 

### Kovarianzmatrix

{{% callout note %}}

- Üb 2, A2.3
- Üb 4, A5

{{% /callout %}}

{{< math >}}
$$
\begin{array}{l}
\operatorname{Cov}_{f_{\underline{x}}}\{\underline{X}\}=\mathrm{E}_{f_{\underline{\underline{x}}}}\left\{(\underline{X}-\underline{\mu})(\underline{X}-\underline{\mu})^{\top}\right\}\\ 
\newline
=\left[\begin{array}{cccc}
\sigma_{X_{1}}^{2} & \sigma_{X_1 X_2} & \cdots & \sigma_{X_1 X_N} \\
\sigma_{X_2 X_1} & \sigma_{X_{2}}^{2} & \cdots & \sigma_{X_2 X_N} \\
\vdots & \vdots & \ddots & \vdots \\
\sigma_{X_N X_1} & \sigma_{X_N X_2} & \cdots & \sigma_{X_{N}}^{2}
\end{array}\right] 
\newline
=\left[\begin{array}{cccc}
\sigma_{X_{1}}^{2} & \rho_{X_{1}, X_{2}} \sigma_{X_{1}} \sigma_{X_{2}} & \cdots & \rho_{X_{1}, X_{N}} \sigma_{X_{1}} \sigma_{X_{N}} \\
\rho_{X_{2}, X_{1}} \sigma_{X_{2}} \sigma_{X_{1}} & \sigma_{X_{2}}^{2} & \cdots & \rho_{X_{2}, X_{N}} \sigma_{X_{2}} \sigma_{X_{N}} \\
\vdots & \vdots & \ddots & \vdots \\
\rho_{X_{N}, X_{1}} \sigma_{X_{N}} \sigma_{X_{1}} & \rho_{X_{N}, X_{2}} \sigma_{X_{N}} \sigma_{X_{2}} & \cdots & \sigma_{X_{N}}^{2}
\end{array}\right] 
\end{array}
$$
{{< /math >}} 







### Positiv definit, positiv semidefinit

Eine beliebige (ggf. symmetrische bzw. hermitesche) $n \times n$-Matrix $A$ ist

- positiv definit, falls

  {{< math >}}
  $$
  x^T A x > 0
  $$
  {{< /math >}} 

- positiv semidefinit, falls

  {{< math >}}
  $$
  x^T A x \geq 0
  $$
  {{< /math >}} 

### Weißes Rauschen

Uncertainties taken at different time steps are also independent

### System-Eigenschaften: dynamisch, statisch, linear, zeitinvariant 

**Statisch**: Der aktuellen Ausgang $y_k$ ist abhängig von dem aktuellen Eingang $u_k$.

**Dynamisch**: Der aktuellen Ausgang $y_k$ ist abhängig von 

- dem aktuellen Eingang $u_k$
- dem aktuellen Zustand $x_k$

Bei wertkontinuierlicher linearer Systeme:

{{% callout note %}}

Üb 5, A1

{{% /callout %}}

- **Linear**

  {{< math >}}
  $$
  \mathcal{S}\left\{\sum_{i=1}^{N} c_{i} y_{\mathrm{e} i, n}\right\}=\sum_{i=1}^{N} c_{i} \mathcal{S}\left\{y_{\mathrm{e} i, n}\right\}
  $$
  {{< /math >}} 

  (also höhste Exponent $\leq 1$)



- **Zeitinvariant**

  Das System antwortet auf ein zeitlich verschobenes Eingangssignal {{< math >}}$y_{\mathrm{e}, n-n_{0}}${{< /math >}} mit dem entsprechend zeitlichverschobenen Ausgangssignal {{< math >}}$y_{\mathrm{a}, n-n_{0}}${{< /math >}} 

  {{< math >}}
  $$
  y_{\mathrm{a}, n}=\mathcal{S}\left\{y_{\mathrm{e}, n}\right\} \quad \Longrightarrow \quad y_{\mathrm{a}, n-n_{0}}=\mathcal{S}\left\{y_{\mathrm{e}, n-n_{0}}\right\}.
  $$
  {{< /math >}} 

  (also unabhängig von dem Zeitindex $k$)

- **Kausalität**

  Ein zeitdiskretes System S heißt **kausal**, wenn die Antwort NUR von *gegenwärtigen* oder *vergangenen*, NICHT jedoch von zukünftigen Werten des Eingangssignals abhängt.





### Dirac Funktion

Definition:

{{< math >}}
$$
\begin{aligned}
\delta(x)&=0, \quad x \neq 0 \\
\int_{a}^b \delta(x) dx &= 1 \quad a < x < b
\end{aligned}
$$
{{< /math >}} 

**Rechenregeln**

- Verschiebung

  {{< math >}}
  $$
  \int_{a}^{b} f(x) \delta\left(x-x_{0}\right) \mathrm{d} x=f\left(x_{0}\right)
  $$
  {{< /math >}} 

- Symmetrie

  {{< math >}}
  $$
  \delta(x) = \delta(-x)
  $$

  {{< /math >}} 

- Skalierung

  {{< math >}}
  $$
  \int_{a}^{b} f(x) \delta(|k| x) \mathrm{d} x=\frac{1}{|k|} f(0)
  $$
  {{< /math >}} 

- Hintereinanderausführung

  {{< math >}}
  $$
  \int_{-\infty}^{\infty} f(x) \delta(g(x)) \mathrm{d} x=\sum_{i=1}^{n} \frac{f\left(x_{i}\right)}{\left|g^{\prime}\left(x_{i}\right)\right|}
  $$
  {{< /math >}} 

  wobei $g(x_i) = 0$ und $g^\prime(x_i) \neq 0$.
  
- Verkettung auflösen (super wichtig!!!)

  {{< math >}}
  $$
  \delta(g(x)) = \sum_i \frac{1}{g^\prime(x_i)} \delta(x - x_i)
  $$
  {{< /math >}} 

  wobei $g(x_i) = 0$ und $g^\prime(x_i) \neq 0$.

### Dirac Mixture

{{< math >}}
$$
f(x)=\sum_{i=1}^{L} w_{i} \delta(\underline{x}-\underline{\hat{x}}_i)
$$
{{< /math >}} 