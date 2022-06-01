---
# ===== Title, summary, and position in the left sidebar =====
linktitle: Overview # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 1
# ============================================================

# ========== Basic metadata ==========
title: Stochastische Informationsverarbeitung
date: 2022-05-26
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

## Meta Information

Lecture website: [**Stochastische Informationsverarbeitung**](https://isas.iar.kit.edu/de/LehreWS2122_SI.php)

Semester: WS21/22

Language: German

Lecturer:

- [Prof. Dr.-Ing. Uwe Hanebeck](https://isas.iar.kit.edu/de/Mitarbeiter_Hanebeck.php) 
- [Daniel Frisch](https://isas.iar.kit.edu/de/Mitarbeiter_Frisch.php)

Exam type: Oral

## Beschreibung

### Inhalt

Die SI vermittelt die fundamentalen und formalen Grundlagen der Zustandsschätzung rund um Prädiktion und Filterung.

Modelle und Zustandsschätzer für **wertediskrete und -kontinuierliche** lineare sowie **allgemeine** Systeme werden behandelt

- Für wertediskrete und -kontinuierliche lineare Systeme
  -  Prädiktion und Filterung (HMM, Kalman Filter)
  - Glättung für wertediskrete Systeme (zusätzlich)
- Modellierung von allgemeinen statischen und dynamischen Systemen
  - Entwickeln ausgehend von einer generativen eine probabilistische Systembeschreibung
  - Unterschiedliche Arten des Rauscheinflusses (additiv, multiplikativ) sowie verschiedene Dichterepräsentationen werden untersucht.
  - Grundlegenden Methoden der Zustandsschätzung für allgemeine Systeme
  - Herausforderungen bei der Implementierung generischer Schätzer



### Ziel

- Wiederholung von Grundlagen Wahrscheinlichkeitstheorie
- Gefühl für Systemtheorie und Behandlung von Unsicherheiten
- Verständnis für
  - Systemmodellierung und Systemidentifikation
  - grundlegende Schätz-, Fusion-, Filterungs- und Prädiktionsverfahren
- Bewusstsein für Schwierigkeiten und Herausforderungen
- Herleitung und Anwendung von exakten Schätzern für
  - wertediskrete Systeme
  -  lineare wertekontinuierliche Systeme
- Herleitung und Anwendung von approximativen Schätzern für
  - schwach nichtlineare Systeme

## Struktur

- **Wertediskrete Systeme**
  - Statische Systeme
  - Dynamische Systeme: Markov-Kette, Messmodell
  - Zustandsschätzung im Hidden Markov Model
- **Wertekontinuierliche lineare Systeme**
  - Statische Systeme
  - Dynamische Systeme: Systemmodell mit Markov-Eigenschaft, Messmodell 
  - Zustandsschätzung: Kalman Filter
- **Wertekontinuierliche und schwach nichtlineare Systeme**
  - Statische Systeme
  - Dynamische Systeme
  - Nichtlineare Schätzung durch Linearisierung (EKF)
  - Nichtlineare Schätzung durch Kalmanfilter in probabilistischer Form
  - Berechnung der Momente: analytisch, numerisch, basierend auf Abtastwerten (UKF) 
  - Ensemble Kalmanfilter (EnKF)
- **Allgemeine Systeme**
  - Dirac'sche Deltafunktion
  - Funktionen von Zufallsvariablen
  - Probabilistische Systemmodelle, Abstraktion
  - Prädiktion nichtlinearer Systeme
  - Filterschritt für nichtlineare Systeme
  - Faktorgraphen und Message Passing
  - Einfache Filter für stark nichtlineare Systeme
- **Sample-basierte Filter**
  - Reapproximation von kontinuierlichen Dichten mit Samples
  - Partikelfilter
  - Progressive Filterung