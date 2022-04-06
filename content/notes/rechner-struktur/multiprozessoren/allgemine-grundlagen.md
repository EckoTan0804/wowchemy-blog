---
linktitle: ''
summary: ''
weight: 30
title: Parallele Architekturmodelle
date: 2020-07-08
draft: false
type: book
authors:
- admin
tags:
- Vorlesung
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

## Multiprozessor mit gemeinsamem Speicher

- **Globaler Speicher** $\Leftrightarrow$ **Gemeinsamer Adressraum**

- **UMA**: **U**niform **M**emory **A**ccess

- Bsp: **symmetrischer Multiprozessor (SMP), Multicore-Prozessor**

  - **Gleichberechtigter** Zugriff der Prozessoren auf die Betriebsmittel

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2020-07-10%2022.10.42.png" alt="截屏2020-07-10 22.10.42" style="zoom: 67%;" />

> **Uniform memory access** (**UMA**) is a [shared memory](https://en.wikipedia.org/wiki/Shared_memory_architecture) architecture used in [parallel computers](https://en.wikipedia.org/wiki/Parallel_computer). All the processors in the UMA model share the physical memory uniformly. In an UMA architecture, access time to a memory location is independent of which processor makes the request or which memory chip contains the transferred data.
>
> More see: [Uniform memory access](https://en.wikipedia.org/wiki/Uniform_memory_access)

## Multiprozessor mit verteiltem Speicher

- **Verteilter Speicher** ⇔ **Verteilter Adressraum**

- **NORMA**: **No** **R**emote **M**emory **A**ccess
- Bsp: Cluster

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2020-07-10%2022.11.55.png" alt="截屏2020-07-10 22.11.55" style="zoom: 67%;" />

## Multiprozessor mit verteiltem gemeinsamen Speicher

- **Verteilter Speicher** ⇔ **Gemeinsamer Adressraum**
- **NUMA**: **N**on-**U**niform **M**emory **A**ccess
- **CC-NUMA**: **C**ache-**C**oherent **N**on-**U**niform **M**emory **A**ccess
  - Globaler Adressraum: Zugriff auf *entfernten* Speicher über load / store Operationen

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2020-07-10%2022.13.31.png" alt="截屏2020-07-10 22.13.31" style="zoom: 67%;" />



## Konfigurationen von Multiprozessoren

![截屏2020-07-21 17.46.16](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2020-07-21%2017.46.16.png)