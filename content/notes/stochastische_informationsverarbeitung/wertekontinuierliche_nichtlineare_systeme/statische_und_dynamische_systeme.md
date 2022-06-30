---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 410
# ============================================================

# ========== Basic metadata ==========
title: Statische und Dynamische Systeme
date: 2022-06-30
draft: false
type: book # page type
authors:
  - admin
tags:
  - SI
  - Lecture Notes
  - Wertekontinuierliche Nichtlineare Systeme
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

## Statische Systeme

- Ein-/Ausgang: Zufallsvektoren $\underline{u}_k$ und $\underline{y}_k$ ($k \in \mathbb{N}_0$ ist der Zeitschritt)

  - $\underline{u}_k \in \mathbb{R}^P$ und $\underline{y}_k \in \mathbb{R}^M$ sind wertekontinuierlich

- Abbildung von $\underline{u}_k$ und $\underline{y}_k$ durch **nichtlineare** Abbildung

  {{< math >}}
  $$
  \underline{y}_{k}=\underline{a}_{k}\left(\underline{u}_{k}\right)
  \tag{Generatives Modell}
  $$
  {{< /math >}} 

- Beschreibung der Unsicherheit in $\underline{u}_k$ und $\underline{y}_k$ durch Dichten
  - {{< math >}}$\underline{u}_k${{< /math >}}: {{< math >}}$f_{k}^{u}\left(\underline{u}_{k}\right)${{< /math >}} 
  - {{< math >}}$\underline{y}_k${{< /math >}}: {{< math >}}$f_k^y(\underline{y}_k)${{< /math >}}
- Gesucht: {{< math >}}$f_k^y(\underline{y}_k)${{< /math >}} zu gegeben {{< math >}}$f_{k}^{u}\left(\underline{u}_{k}\right)${{< /math >}} 

## Dynamische Systeme

### Systemabbildung

- Zustand {{< math >}}$\underline{x}_k, k \in \mathbb{N}_0${{< /math >}} mit {{< math >}}$\underline{x}_k \in \mathbb{R}^N${{< /math >}} 

- Nichtlineare System

  {{< math >}}
  $$
  \underline{x}_{k+1}=\underline{a}_{k}\left(\underline{x}_{k}, \underline{\hat{u}}_{k}, \underline{w}_{k}\right)
  $$
  {{< /math >}} 

- Beschreibung von {{< math >}}$\underline{x}_k${{< /math >}} durch Dichte {{< math >}}$f_k^x(\underline{x}_k)${{< /math >}} 

- Spezielle Rauschstruktur: **Additives Rauschen**

  {{< math >}}
  $$
  \underline{x}_{k+1}=\underline{a}\left(\underline{x}_{k}, \underline{\hat{u}}_{k}\right)+\underline{w}_{k}
  $$
  {{< /math >}} 

  - Systemrauschen {{< math >}}$\underline{w}_k${{< /math >}} wird beschrieben durch Dichte {{< math >}}$f_k^w(\underline{w}_k)${{< /math >}} 
  - Typische Annahme
    -  {{< math >}}$\underline{w}_k${{< /math >}} ist Gauß verteilt mit bekannten Parametern
    -  {{< math >}}$\underline{w}_k${{< /math >}} ist weißes Rauschen

### Messabbildung

- Nichtlineare Abbildung

  {{< math >}}
  $$
  \underline{y}_{k}=\underline{h}_{k}\left(\underline{x}_{u}, \underline{v}_{k}\right)
  $$
  {{< /math >}} 

  - Spezialfall: **Additives Rauschen**

    {{< math >}}
    $$
    \underline{y}_{k}=\underline{h}_{k}\left(\underline{x}_{u}\right) + \underline{v}_{k}
    $$
    {{< /math >}} 

    Rauschen {{< math >}}$\underline{v}_{k}${{< /math >}} beschrieben durch {{< math >}}$f_k^v(\underline{v}_k)${{< /math >}} 

### Gesammtsystem

![wertkontinuierliche_nichtlineare_system.drawio](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/wertkontinuierliche_nichtlineare_system.drawio.png)

{{% callout note %}}
Note: Das System ist gekapselt. Von außen können wir nur {{< math >}}$\underline{\hat{u}}_{k}${{< /math >}} und {{< math >}}$\underline{y}_k${{< /math >}} sehen.
{{% /callout %}}