---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 320
# ============================================================

# ========== Basic metadata ==========
title: Zustandsschätzung
date: 2022-06-16
draft: false
type: book # page type
authors:
  - admin
tags:
  - SI
  - Lecture Notes
  - Wertkontinuierliche lineare Systeme
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

## Prädiktion

Wir möchte *ein Schritt* Prädiktion für Zustand machen, also am Zeitschritt $k$ ($k > m$, $m:= \text{\#Messungen}$) die Prädiktion für den Zustand {{< math >}}$\underline{x}_{k+1}${{< /math >}} zu machen

Modell:

{{< math >}}
$$
\underline{x}_{k+1}=\mathbf{A}_{k} \cdot \underline{x}_{k}+\mathbf{B}_{k} \cdot\left(\underline{\tilde{u}}_{k}+\underline{w}_{k}\right)
$$
{{< /math >}} 

- Initialer Schätzwert für $k$: 

  {{< math >}}
  $$
  \underline{x}_{k|1:m}
  $$
  {{< /math >}} 

  - basiert auf Messungen {{< math >}}$\underline{y}_{1}, \dots, \underline{y}_{m}${{< /math >}} 
  - Eingabewerte {{< math >}}$\underline{\tilde{u}}_{0}, \dots, \underline{\tilde{u}}_{k-1}${{< /math >}} 
  - mit Erwartungswert {{< math >}}$\underline{\hat{x}}_{k|1:m}${{< /math >}} und Kovarianzmatrix {{< math >}}$C_{k|1:m}^x${{< /math >}} 

- Berechnung des Erwartungswerts für $k+1$

  {{< math >}}
  $$
  \begin{aligned}
  &E\left\{\underline{x}_{k+1}\right\}\\\\
  =&E\left\{\mathbf{A}_{k} \cdot \underline{x}_{k}+\mathbf{B}_{k}\left(\underline{\tilde{u}}_{k}+\underline{w}_{k}\right)\right\}\\\\
  =&E\left\{\mathbf{A}_{k} \cdot x_{k}+\mathbf{B}_{k} \tilde{u}_{k}+\mathbf{B}_{k} \underline{w}_{k}\right\}\\\\
  =&\mathbf{A}_{k} \cdot E\left\{x_{k}\right\}+\mathbf{B}_{k} \cdot \underbrace{E\left\{\tilde{u}_{k}\right\}}_{=\tilde{\underline{u}}_{k} \text{ (da } \tilde{\underline{u}}_{k} \text{ is fix)}}+\mathbf{B}_{k} \cdot\underbrace{E\left\{\underline{w}_{k}\right\}}_{=0 \text{ ("mittelwertfrei")}}\\\\
  =&\mathbf{A}_{k} \cdot \underline{\hat{x}}_{k|1: m}+\mathbf{B}_{k} \tilde{\underline{u}}_{k} \qquad (+)
  \end{aligned}
  $$
  

  {{< /math >}} 

- Berechnung der Kovarianzmatrix {{< math >}}$C_{k+1|1:m}^x${{< /math >}} 

  {{< math >}}
  $$
  \begin{aligned}
  \underline{x}_{k+1} &=\mathbf{A}_{k} \underline{x}_{k}+\mathbf{B}_{k} \underline{u}_{k} \\
  &=\left[\begin{array}{ll}
  \mathbf{A}_{k} & \mathbf{B}_{k}
  \end{array}\right]\left[\begin{array}{c}
  \underline{x}_{k} \\
  \underline{u}_{k}
  \end{array}\right]
  \end{aligned}
  $$
  {{< /math >}} 

  {{< math >}}
  $$
  \begin{aligned}
  \underline{x}_{k+1}-\hat{\underline{x}}_{k+1} &=\left[\begin{array}{ll}
  \mathbf{A}_{k} & \mathbf{B}_{k}
  \end{array}\right]\left[\begin{array}{c}
  \underline{x}_{k}-\hat{\underline{x}}_{k} \\
  u_{k}-\hat{u}_{k}
  \end{array}\right] \\
  &=\left[\begin{array}{ll}
  \mathbf{A}_{k} & \mathbf{B}_{k}
  \end{array}\right]\left[\begin{array}{c}
  \underline{x}_{k}-\hat{x}_{k} \\
  \underline{w}_{k}
  \end{array}\right]
  \end{aligned}
  $$
  {{< /math >}} 

  Annahme: Zustand und Systemrauschen sind unkorreliert

  {{< math >}}
  $$
  \begin{aligned}
  \operatorname{Cov}\left\{\left[\begin{array}{c}
  \underline{x}_{k} \\
  \underline{\tilde{u}}_{k}
  \end{array}\right]\right\} &=E\left\{\left[\begin{array}{c}
  \underline{x}_{k}-\underline{\hat{x}}_{k} \\
  \underline{w}_{k}
  \end{array}\right]\left[\left(\underline{x}_{k}-\underline{\hat{x}}_{k}\right)^{\top} \underline{w}_{k}^{\top}\right]\right\} \\
  &=\left[\begin{array}{cc}
  C_{k \mid 1: m}^{x} & 0 \\
  0 & C_{k}^{w}
  \end{array}\right]
  \end{aligned}
  $$
  {{< /math >}} 
  
  {{< math >}}
  $$
  \begin{aligned}
  C_{k+1 \mid 1 : m}^{x} &=E\left\{\left(\underline{x}_{k+1}-\hat{x}_{k+1}\right)\left(\begin{array}{l}
  x_{k+1} \\
  \hat{\underline{x}}_{k+1}
  \end{array}\right)\right\} \\
  &=\left[\begin{array}{ll}
  \mathbf{A}_{k} & \mathbf{B}_{k}
  \end{array}\right] \cdot E\left\{\left[\begin{array}{c}
  \underline{x}_{k}-\hat{\underline{x}}_{k} \\
  \underline{w}_{k}
  \end{array}\right]\left[\begin{array}{ll}
  \underline{x}_{k}-\hat{\underline{x}}_{k} & \underline{w}_{k}
  \end{array}\right]\right\} \cdot\left[\begin{array}{l}
  \mathbf{A}_{k}^{\top} \\
  \mathbf{B}_{k}^{\top}
  \end{array}\right] \\\\
  &=\left[\begin{array}{ll}
  \mathbf{A}_{k} & \mathbf{B}_{k}
  \end{array}\right] \cdot\left[\begin{array}{cc}
  C_{k \mid 1:m} & 0 \\
  0 & C_{k}^{w}
  \end{array}\right] \cdot\left[\begin{array}{l}
  \mathbf{A}_{k}^{\top} \\
  \mathbf{B}_{k}^{\top}
  \end{array}\right] \\
  &=\mathbf{A}_{k} \cdot C_{k \mid 1: m}^{x} \mathbf{A}_{k}^{\top}+\mathbf{B}_{k} C_{k}^{w} \mathbf{B}_{k}^{\top} \qquad(++)
  \end{aligned}
  $$
  {{< /math >}} 

Rekursive Prädiktion

- Beginn mit Erwartungswert {{< math >}}$\underline{\hat{x}}_{m|1:m}${{< /math >}} und Kovarianzmatrix {{< math >}}$C_{m|1:m}^x${{< /math >}} 

- Rekursion mit $(+)$ und $(++)$ für $k > m$



## Filterung

{{% callout note %}}
**Erinnerung** 

[Struktur des dynamischen Systems]({{< relref "statische_systeme#dynamische-systeme" >}}) 

{{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/wertekontinuierliche_lineare_systeme-Gauß-Markov-Modell.drawio.png" caption="Graphische Darstellung von dynamischer Systeme" numbered="true" >}}

[Messabbildung]({{< relref "statische_systeme#messabbildung" >}})

{{< math >}}
$$
\underline{y}\_{k}=\mathbf{H}\_{k} \cdot \underline{x}\_{k}+\underline{v}\_{k}
$$
{{< /math >}}
{{% /callout %}}

Ansatz: **Linearer Schätzer**

{{< math >}}
$$
\underline{x}_{k \mid 1: k}=\mathbf{K}_{k}^{(1)} \underline{x}_{k \mid 1: k-1}+\mathbf{K}_{k}^{(2)} \underline{y}_{k} \qquad(\ast)
$$
{{< /math >}} 

🎯 Wir suchen den sog. **BLUE-Filter** (Best Linear Unbiased Estimator) 💪

{{% callout note %}}
Ein Schätzer heißt {{< hl >}}**erwartungstreu**{{< /hl >}} , wenn sein Erwartungswert gleich dem wahren Wert des zu schätzenden Parameters ist. 

Ist eine Schätzfunktion nicht erwartungstreu, spricht man davon, dass der Schätzer {{< hl >}}**verzerrt**{{< /hl >}} ist. Das Ausmaß der Abweichung seines Erwartungswerts vom wahren Wert nennt man **Verzerrung** oder **Bias**. Die Verzerrung drückt den systematischen Fehler des Schätzers aus.

Source und Bsp: [Wiki](https://de.wikipedia.org/wiki/Erwartungstreue)

{{% /callout %}}

- Erwartungswerttreue (unbiased)

  {{< math >}}
  $$
  \begin{aligned}
  E\left\{\underline{x}_{k \mid 1: k}\right\}&=E\left\{\mathbf{K}_{k}^{(1)} \underline{x}_{k \mid 1: k-1}+\mathbf{K}_{k}^{(2)} \underline{y}_{k}\right\} \\
  E\left\{\underline{x}_{k \mid 1: k}\right\}&=\mathbf{K}_{k}^{(1)} E\left\{\underline{x}_{k \mid 1: k-1}\right\}+\mathbf{K}_{k}^{(2)} E\left\{\underline{y}_{k}\right\} \\
  E\left\{\underline{x}_{k \mid 1: k}\right\}&=\mathbf{K}_{k}^{(1)} E\left\{\underline{x}_{k \mid 1: k-1}\right\}+\mathbf{K}_{k}^{(2)} E\left\{\mathbf{H}_{k} \cdot x_{k}+\underline{y}_{k}\right\} \\
  E\left\{\underline{x}_{k \mid 1: k}\right\}&=\mathbf{K}_{k}^{(1)} E\left\{\underline{x}_{k \mid 1: k-1}\right\}+\mathbf{K}_{k}^{(2)} \mathbf{H}_{k} E\left\{\underline{x}_{k}\right\} \quad \mid \text { Erwartungstreu } \\
  \underline{\tilde{x}}&=\mathbf{K}_{k}^{(1)} \underline{\tilde{x}}+\mathbf{K}_{k}^{(2)} \mathbf{H}_{k} \cdot \underline{\tilde{x}} \\
  \Rightarrow  &=\mathbf{K}_{k}^{(1)}+\mathbf{K}_{k}^{(2)} \mathbf{H}_{k}
  \end{aligned}
  $$
  {{< /math >}} 

  z.B. 

  {{< math >}}
  $$
  \begin{aligned}
  \mathbf{K}_{k}^{(1)} &= \mathbf{I} - \mathbf{K}_{k}\mathbf{H}_{k} \\
  \mathbf{K}_{k}^{(2)} &= \mathbf{K}_{k}
  \end{aligned}
  $$
  {{< /math >}} 

Setze in $(\ast)$ ein:

{{< math >}}
$$
\underbrace{\underline{x}_{k \mid 1: k}}_{=: \underline{x}_{k}^{e}}=\left(\mathbf{I}-\mathbf{K}_{k}\mathbf{H}_{k} \right) \underbrace{\underline{x}_{k \mid 1: k-1}}_{=: \underline{x}_{k}^{p}}+\mathbf{K}_{k} \underline{y}_{k} \qquad(* *)
$$
{{< /math >}} 

Aber der Schätzert ist noch nicht vollständig festgelegt, da $\mathbf{K}_{k}$ noch nicht festgelegt ist. 

$\Rightarrow$ Wiri suche $\mathbf{K}_{k}$ so, dass der resultierende Schätzer MINIMAL kovarianz aufweist. ("Minimalvarianz Schätzer")

Nehme an, dass Messung unkorreliert mit priorer Schätzung. Aus $(\ast\ast)$ gilt

{{< math >}}
$$
\underbrace{\mathbf{C}_{k \mid 1: k}\left(\mathbf{K}_{k}\right)}_{=: \mathbf{C}_{k}^{e}\left(\mathbf{K}_{k}\right)}=\left(\mathbf{I}-\mathbf{K}_{k} \mathbf{H}_{k}\right) \underbrace{\mathbf{C}_{k \mid 1: k-1}^{x}}_{=: \mathbf{C}_{k}^{p}}\left(\mathbf{I}-\mathbf{K}_{k} \mathbf{H}_{k}\right)^{\top}+\mathbf{K}_{k} C_{k}^{y} \mathbf{K}_{k}^{\top} \qquad(\ast\ast\ast)
$$
{{< /math >}} 

{{% callout note %}}

Trick: Auf **Skalares Gütemaß** zurückzuführen

D.h., um Kovarianzmatrizen generell vergleichen zu können, verwende man die Funktionen, die von einer $n \times n$ Matrix in $\mathbb{R}^1$ abbilden. Anders gesagt, die einer Kovarianzmatrix einen Skalar zuordnen, denn man kann nur Skalare direkt miteinander vergleichen.

Z.B., Projektion mit beliebigen Einheitsvektor $\underline{e}$

{{< math >}}
$$
P(\mathbf{K}) = \underline{e}^\top \cdot \mathbf{C}_c(\mathbf{K}) \cdot \underline{e}
$$

{{< /math >}} 

MINIMAL kovarianz $\Leftrightarrow$ $P(\mathbf{K})$ soll minimal sein für $\underline{e}$.

Andere mögliche skalare Gütemaße für eine diagonale Kovarianzmatrix (z.B. $\mathbf{C}=\left[\begin{array}{cc}\sigma_{x}^{2} & 0 \\ 0 & \sigma_{y}^{2}\end{array}\right]$):

- $\operatorname{Spur}(\cdot)$: Summe der Diagonalelemente

  {{< math >}}
  $$
  \begin{equation}
  \operatorname{Spur}(\mathbf{C})=\sigma\_{x}^{2}+\sigma\_{y}^{2}
  \end{equation}
  $$
  {{< /math >}} 

- $\operatorname{det}(\cdot)$: Determinante, also Produkt der Eigenwerte

  {{< math >}}
  $$
  \operatorname{det}(\mathbf{C})=\sigma\_{x}^{2} \cdot \sigma\_{y}^{2}
  $$
  {{< /math >}} 

{{% /callout %}}

Ableitung mit der [Matrizen Differenzregeln]({{< relref "../math/matrix_differenzieren" >}}):

{{< math >}}
$$
\begin{aligned}
\frac{\partial}{\partial K} P(\mathbf{K}) &=\frac{\partial}{\partial \mathbf{K}}\left\{\underline{e}^{\top}\left[(\mathbf{I}-\mathbf{K} \mathbf{H}) \mathbf{C}_{p}(\mathbf{I}-\mathbf{K} \mathbf{H})^{\top}+\mathbf{K} \mathbf{C}_{y} \mathbf{K}^{\top}\right] \underline{e}^{\top}\right\} \\
&=\frac{\partial}{\partial \mathbf{K}}\left\{\underline{e}^{\top}\left[\mathbf{C}_{p}-\mathbf{C}_{p} \mathbf{H}^{\top} \mathbf{K}^{\top}-\mathbf{K} \mathbf{H} \mathbf{C}_{p}+\mathbf{K} \mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top} \mathbf{K}^{\top}+\mathbf{K} \mathbf{C}_{y} \mathbf{K}^{\top}\right] \underline{e}\right\} \\
&=-\left[\mathbf{H} \mathbf{C}_{p} \underline{e} \underline{e}^{\top}\right]^{\top}-\underline{e} \underline{e}^{\top}\left(\mathbf{H} \mathbf{C}_{p}\right)^{\top}+2 \underline{e} \underline{e}^{\top} \mathbf{K} \mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top}+2 \underline{e} \underline{e}^{\top} \cdot \mathbf{K} \mathbf{C}_{y} \\
&\overset{!}{=} \mathbf{0}
\end{aligned}
$$
{{< /math >}} 

Also

{{< math >}}
$$
\begin{array}{l}
-\mathbf{C}_{p} \cdot \mathbf{\mathbf{H}}^{\top}-\mathbf{C}_{p} \mathbf{H}^{\top}+2 \mathbf{K} \mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top}+2 \mathbf{K} \mathbf{C}_{y} \stackrel{!}{=} \mathbf{0} \\
\mathbf{K}\left(\mathbf{C}_{y}+\mathbf{H} \mathbf{C}_{p} \mathbf{H}\right)^{\top}=\mathbf{C}_{p} \mathbf{H}^{\top} \\
\mathbf{K}=\mathbf{C}_{p} \mathbf{H}^{\top}\left(\mathbf{C}_{y}+\mathbf{H} \mathbf{C}_{p} \mathbf{\mathbf{H}}^{\top}\right)^{-1} \quad \text { (Kalman gain) }
\end{array}
$$
{{< /math >}} 

Setze $\mathbf{K}$ in $(\ast \ast)$ ein

{{< math >}}
$$
\begin{aligned}
\underline{\hat{x}}_{e} &=(\mathbf{I}-\mathbf{K} \mathbf{H}) \underline{\hat{x}}_{p}+\mathbf{K} \cdot \underline{\hat{y}} \qquad \text { (combination form) } \\
&=\underline{x}_{p}+\mathbf{K}\left(\underline{\hat{y}}-\mathbf{H} \cdot \underline{x}_{p}\right) \qquad \text { (feedback form) } \\
&=\underline{\hat{x}}_{p}+\mathbf{C}_{p} \mathbf{H}^{\top}\left(\mathbf{C}_{y}+\mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top}\right)^{-1}\left(\underline{y}-\mathbf{H} \cdot \underline{\hat{x}}_{p}\right)
\end{aligned}
$$
{{< /math >}} 

Das ist das {{< hl >}}**Kalman Filter**{{< /hl >}}.

Nun Setze $\mathbf{K}$ in $(\ast \ast \ast)$ ein, um die Kovarianzmatrix zu berechnen.

{{< math >}}
$$
\begin{aligned}
\mathbf{C}_{e}=& {\left[\mathbf{I}-\mathbf{C}_{p} \mathbf{H}^{\top}\left(\mathbf{C}_{y}+\mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top}\right)^{-1} \mathbf{H}_{k}\right] \cdot \mathbf{C}_{p} } \\
& \cdot\left[\mathbf{I}-\mathbf{C}_{p} \mathbf{H}^{\top}\left(\mathbf{C}_{y}+\mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top}\right)^{-1} \mathbf{H}_{k}\right]^{-1} \\
&+\mathbf{C}_{p} \mathbf{H}^{\top}\left(\mathbf{C}_{y}+\mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top}\right)^{-1} \mathbf{C}_{y}\left(\mathbf{C}_{y}+\mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top}\right)^{-1} \mathbf{H} \mathbf{C}_{p} \\\\
=& \mathbf{C}_{p}-2 \mathbf{C}_{p} \mathbf{H}^{\top}\left(\mathbf{C}_{y}+\mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top}\right)^{-1} \mathbf{H} \mathbf{C}_{p} \\
&+\mathbf{C}_{p} \mathbf{H}^{\top}\left(\mathbf{C}_{y}+\mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top}\right)^{-1} \mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top}\left(\mathbf{C}_{y}+\mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top}\right)^{-1} \mathbf{H} \mathbf{C}_{p} \\
&+\mathbf{C}_{p} \mathbf{H}^{\top}(\underbrace{\mathbf{C}_{y}+\mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top}}_{=:\mathbf{D}})^{-1} \mathbf{C}_{y}\left(\mathbf{C}_{y}+\mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top}\right)^{-1} \mathbf{H} \mathbf{C}_{p}\\\\
=& \mathbf{C}_{p}-2 \mathbf{C}_{p} \mathbf{H}^{\top} \mathbf{D}^{-1} \mathbf{H} \mathbf{C}_{p}+\mathbf{C}_{p} \mathbf{H}^{\top} \mathbf{D}^{-1} \mathbf{D} \mathbf{D}^{-1} \mathbf{H} \mathbf{C}_{p} \\\\
=& \mathbf{C}_{p}-\mathbf{C}_{p} \mathbf{H}^{\top}\left(\mathbf{C}_{y}+\mathbf{H} \mathbf{C}_{p} \mathbf{H}^{\top}\right)^{-1} \mathbf{H} \mathbf{C}_{p}
\end{aligned}
$$
{{< /math >}} 

{{% callout note %}}
Die ausführliche Zusammenfassung für Kalman Filter siehe [hier]({{< relref "../understanding/kalman_filter.md" >}}).
{{% /callout %}}