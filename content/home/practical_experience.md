---
# An instance of the Experience widget.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: experience

# Activate this widget? true/false
active: true

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 60

title: Practical Experience
subtitle:

# Date format for experience
#   Refer to https://wowchemy.com/docs/customization/#date-format
date_format: Jan 2006

# Experiences.
#   Add/remove as many `experience` items below as you like.
#   Required fields are `title`, `company`, and `date_start`.
#   Leave `date_end` empty if it's your current employer.
#   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
experience:
  - title: Walkable Path Discovery Utilizing Drones
    company: KIT, Computer Vision for Human-Computer Interaction (CV:HCI) Lab
    company_url: 'https://cvhci.anthropomatik.kit.edu/587.php'
    company_logo: kit-cvhci
    location: Karlsruhe, Germany
    date_start: '2021-04-12'
    date_end: '2021-07-31'
    description: |2-
        * Development of "flying guide dog" prototype for the visually impaired using drone and semantic segmentation
        * Train SegFormer model on large-scale Mapillay Vistas dataset using PyTorch
        * Design of drone self-control algorithm
        * Build Pedestrian and Vehicle Traffic Lights (PVTL) dataset for traffic light recognition
        * Design and train traffic light recognition model using PyTorch
        
  - title: Hand Gesture Recognition
    company: KIT, Interactive Systems Lab (ISL)
    company_url: 'http://isl.anthropomatik.kit.edu/english/8903.php'
    company_logo: kit
    location: Karlsruhe, Germany
    date_start: '2020-11-01'
    date_end: '2021-02-18'
    description: |2-
        * Development of hand gesture recognition application with Python
        * Building and training of neural networks using PyTorch
        * Dataset preprocessing and data augmentation using albumentations
        * Hyperparameter tuning using Ray-Tune

  - title: Real World Person Detection on Jetson GPU
    company: KIT, High Performance Humanoid Technologies (H²T)
    company_url: 'https://h2t.anthropomatik.kit.edu/english/index.php'
    company_logo: kit-ies
    location: Karlsruhe, Germany
    date_start: '2017-10-01'
    date_end: '2018-02-28'
    description: |2-
        * Training of Single-Stage Detectors (YOLO, RetinaNet, SSD)
        * Deployment of end-to-end person detection pipeline on Nvidia Jetson devices
        * Performance optimization using Nvidia Nsight

  - title: Lego Mindstorms
    company: KIT, Vision and Fusion Laboratory
    company_url: 'https://ies.anthropomatik.kit.edu/english/index.php'
    company_logo: kit
    location: Karlsruhe, Germany
    date_start: '2020-11-01'
    date_end: '2021-03-20'
    description: |2-
        * Design and development of LEGO robot based on leJos Ev3 framework using Java
        * Methodology: Scrum
        * 2nd place in the final race

  - title: Development of an interactive feedback system based on RStudio Shiny for data from ESM applications for Android
    company: KIT, the Telecooperation Office (TECO)
    company_url: 'https://ies.anthropomatik.kit.edu/english/index.php'
    company_logo: kit-teco
    location: Karlsruhe, Germany
    date_start: '2016-10-01'
    date_end: '2017-04-30'
    description: |2-
        * Development of Android application for survey based on experience sampling method (ESM)
        * Methodology: Waterfall model
        * Open source Frameworks: okhttp3, gson

design:
  columns: '2'
---