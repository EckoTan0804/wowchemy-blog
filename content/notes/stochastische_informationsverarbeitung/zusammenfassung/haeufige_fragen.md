---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 770
# ============================================================

# ========== Basic metadata ==========
title: Häufige Prüfungsfragen
date: 2022-09-13
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

## Allgemeine Fragen

### Was haben wir in der Vorlesung gemacht/gelernt/behandelt?





### Was ist Zustandsschätzung?



### Was ist Zustand?





### Welche Arten von Systemen sind einfach? Warum?

Wertdiskret und wertkontinuierlich linear.

Grund: konstanter Rechen- und Speicherbedarf



## Wertdiskrete Systeme

### Wonham Filter herleiten



## Wertkontinuierliche lineare Systeme

### Linear Kalman Filter herleiten



### Eigeenschaften des KFs





## Wertkontinuierliche schwache nichtlineare Systeme

### Wie kann man erkennen, ob ein System stark oder schwach nichtlinear?

- Vergleich mit Taylor Entwicklung 1. Ordnung
- Induzierte Nichtlinearität

### Was kann man machen, wenn das System schwach nichtlinear ist?



### Wie funktioniert die Zustandsschätzung bei schwach nichtlinearen Systemen?



### Wie funktioniert das EKF? EKF herleiten



### UKF erklären und herleiten

- Wie funktioniert die Filterung mit Samples?

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-09-12 22.29.08.png" alt="截屏2022-09-12 22.29.08" style="zoom: 33%;" />



- Wie können wir Samples von der Priore erzeugen?



### Unterschied zwischen UKF und EnKF?



### NLKF (KF in probabilistischer Form)





## Allgemine Systeme



###Chapman-Komolgorov Gleichung herleiten



### Problem von allgemeinen Systeme?

- Prädiktion: Parameterintergral bei Chapman-Komolgorov Gleichung
  - <span style="color: Red">Integrand hängt von $\underline{x}_{k+1}$ ab (lässt sich i.Allg nicht herausziehen)</span>
  - <span style="color: Red">Nur möglich für analytische Lösung</span>
  - <span style="color: Red">Sonst erfordert (numerische) Lösung des Integrals für alle $\underline{x}_{k+1}$</span>

- Filterung
  - Type der Dichte zur Beschreibung der Schätzung ändert sich
  2. Dichte wrid mit jedem Schritt komplexer



### Wie kann man gegen Parameterintergral bei Prädiktion tun?

Transitionsdichte {{< math >}}$f\left(\underline{x}_{k+1} \mid \underline{x}_k\right)${{< /math >}} durch entkoppelte Mixture approximieren

{{< math >}}
$$
f\left(\underline{x}_{k+1} \mid \underline{x}_k\right)=\sum_{i=1}^L w_k^{(i)} f_{k+1}^{(i)}\left(\underline{x}_{k+1}\right) f_k^{(i)}\left(\underline{x}_k\right)
$$
{{< /math >}} 

Vorteil: die Integrande von CK-Gleichung, die von {{< math >}}$\underline{x}_{k+1}${{< /math >}}, lässt sich rausziehen. Das Integral ist eine Konstante und wird als Faktor fürs neue Gewicht verwendet.

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2022-09-13 20.55.22.png" alt="截屏2022-09-13 20.55.22" style="zoom: 33%;" />



### Generatives System (mit additivem oder multiplikativem Rauschen) in probabilistische überführen und herleiten









## Sampling 

### Wie funktioniert Partikel Filter? 

