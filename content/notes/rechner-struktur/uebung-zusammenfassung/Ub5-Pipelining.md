---
linktitle: ''
summary: ''
weight: 150
title: Ub5-Pipelining
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

**Befehlspipelining**

Zerlegung der Ausführung einer Maschinenoperation in Teilphasen, die dann von hintereinander geschaltenen Verarbeitungseinheiten taktsynchron bearbeitet werden, wobei *jede Einheit genau eine spezielle Teiloperation ausführt.*

**Pipeline-Stufe**

Stufen, der Pipeline, die jeweils durch Pipeline-Register getrennt sind

**Pipelining**

- Pipeline-Stufen benutzen unterschiedliche Ressourcen
- Ausführung eines Befehls in $k$ Taktzyklen

- erhöht den Durchsatz, reduziert NICHT Ausführungszeit eines Befehls
- **Taktzyklus ist abhängig von der *langsamsten* Stufe**

- Unterscheidung zwischen Integer- und FP-Ausführung



## Bsp

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2020-07-02%2013.13.37.png" alt="截屏2020-07-02 13.13.37" style="zoom:80%;" />

- Zykluszeit

  - OHNE Pipelining

    $$
    \text{Zykluszeit} = \text{Summe aller Stufen}
    $$
    
    $$
    \text{Zykluszeit} = 250 + 100 + 130 + 220 + 50 = 750 \text{ps}
    $$
    
  - Mit Pipelining
    $$
    \text{Zykluszeit} = \text{Längste Stufe} + \text{Latenz des Pipelineregisters}
    $$
  
    $$
    \text{Zykluszeit} = 250 + 20 = 270 \text{ps}
    $$
  
    

- SpeedUp
  $$
  \begin{aligned} \text {SpeedUp} &=\frac{\text { average exec time WITHOUT pipeline }}{\text { average exectime WITH pipeline }} \\ &=\frac{\mathrm{CPI} \cdot \text { CycleTime WITHOUT pipeline}}{\mathrm{CPI} \cdot \text { CycleTime WITH pipeline}} \end{aligned}
  $$