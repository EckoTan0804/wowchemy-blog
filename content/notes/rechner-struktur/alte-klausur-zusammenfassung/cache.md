---
linktitle: ''
summary: ''
weight: 240
title: Cache Aufgaben
date: 2020-08-06
draft: false
type: book
authors:
- admin
tags:
- Alte Klausur

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

## Cache Miss

- **Compulsory/Cold Miss**
- **Capacity Miss**
- **Conflict Miss**
- **Coherency Miss**
  - Nur bei Multiprozessor-Systemen mit Kohärenzprotokoll
  - Unterscheidung zwischen False- und True-Sharing
  - False-Sharing, falls nicht eigentliches Wort sondern anderes Wort in Cache-Block geändert wurde (See also: [What’s false sharing and how to solve it](https://medium.com/@genchilu/whats-false-sharing-and-how-to-solve-it-using-golang-as-example-ef978a305e10))

### Bsp: Klausur SS17, Aufg. 3, (e)

- Multiprozessor mit gemeinsamen Speicher, der aus drei Prozessoreinheiten sowie Caches besteht.
- Jeder Cache bietet Platz für eine Cache-Zeile. 
- Cache-Protokoll: MESI Protokoll
- Zugriff auf vier Variablen (A, B, C, D), wobei
  - Variablen A,B und C dem selben Speicherblock angehören, also zusammen geladen werden
  - D einem anderen Speicherblock angehör
  - Beide Speicherblöcke werden auf die selbe Cache-Zeile abgebildet.

Klassifizieren Sie die auftretenden Cache Misses. Unterscheiden Sie dabei zwis- 4P chen True- und False-Sharing Misses.

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2020-08-06%2023.40.02.png" alt="截屏2020-08-06 23.40.02" style="zoom:80%;" />

> - False-Sharing Miss in Zeile 6:
>
>   Variablen A, B, C angehören dem selben Speicherblock. Prozessor 1 hat in Zeile 4 Variable A verändert.
>
>   Laut MESI Protokoll muss der selbe Speicherblock in andere Cache des anderen Prozessors invalidiert werden. $\Rightarrow$ Cache Miss
>
>   Da NICHT eigentliches Wort B, sondern Variable A, also das andere Wort, in Cache-Block geändert wird, ist dieses Cache Miss daher ein False-Sharing Miss.
>
> - True-Sharing Miss in Zeile 9:
>
>   Variable B ist in Zeile 7 geändert. D.h. das eigentliche (dasselbe) Wort wird geändert
>
>   $\Rightarrow$ True-Sharing



## Mehrstufiger Cache-Architektur

{{% callout warning %}} 

Achtung:

Wie der Zugriff auf die nächste Ebene stattfindet (sequentiell oder parallel)?

{{% /callout %}}

- Beim **sequntiellen** Zugriffe auf die nächste Ebene
  $$
  t\_{a}=\underbrace{r\_{H 1} * t\_{L 1}}\_{\text{Hit L1}} + \underbrace{r\_{M1} *(\underbrace{r\_{H2} *\left(t\_{L1}+t\_{L2}\right)}\_{\text{Hit L2}}+\underbrace{r\_{M2} *(t\_{L1}+t\_{L2}+t\_{Mem})}\_{\text{Miss L2}})}\_{\text{Miss L1}}
  $$

  - Bsp: SS18, Aufg.3, (b)

- Beim **parallelen** Zugriffe auf die nächste Ebene

  - Die Zugriffszeit höherer Ebene beim Miss kann in Zugriffszeit niedrigerer Ebene verstecken.

  $$
  t\_{a}=\underbrace{r\_{H 1} * t\_{L 1}}\_{\text{Hit L1}} + \underbrace{r\_{M1} *(\underbrace{r\_{H2} *t\_{L2}}\_{\text{Hit L2}}+\underbrace{r\_{M2} *t\_{Mem}}\_{\text{Miss L2}})}\_{\text{Miss L1}}
  $$

  - Bsp: WS1819,  Aufg.3, (c)



## Cache Kohärenzprotokolle

- Verzeichnis-/Tabellen-basierte Protokolle (directory-based protocols)
- Snooping-Protokolle (Bus-Schnüffeln)
  - Write-Invalid Protokoll
    - MSI
    - MESI
    - MOESI
  - Write-Update Protokoll