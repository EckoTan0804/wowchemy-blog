---
# ===== Title, summary, and position in the left sidebar =====
linktitle: 
summary:
weight: 220
# =========================================================

# Basic info
title: "Bias Variance Tradeoff"
date: 2020-07-06
draft: false
type: book # page type
authors: ["admin"]
tags: ["ML", "Model Selection"]
categories: ["Machine Learning"]
toc: true # Show table of contents?

# Advanced settings
profile: false  # Show author profile?

reading_time: true # Show estimated reading time?
# summary: "Objective function overview"
share: true  # Show social sharing links?
featured: true

comments: true  # Show comments?
disable_comment: false
commentable: true  # Allow visitors to comment?  

editable: false  # Allow visitors to edit the page?  

# Optional header image (relative to `assets/media/` folder).
header:
  caption: ""
  image: ""

# Menu
menu: 
    machine-learning:
        parent: model-selection
        weight: 2
---

## TL;DR

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-fymr{border-color:inherit;font-weight:bold;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-fymr">Resaon</th>
    <th class="tg-fymr">Example</th>
    <th class="tg-fymr">affect</th>
    <th class="tg-fymr">Model's complexity ⬆️</th>
    <th class="tg-fymr">Model's complexity ⬇️</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">Bias</td>
    <td class="tg-0pky">wrong  assumption</td>
    <td class="tg-0pky">assume a  quadratic model to be linear</td>
    <td class="tg-0pky">underfitting</td>
    <td class="tg-0pky">⬇️</td>
    <td class="tg-0pky">⬆️</td>
  </tr>
  <tr>
    <td class="tg-0pky">Variance</td>
    <td class="tg-0pky">excessive  sensitivity to small variations</td>
    <td class="tg-0pky">high-degree  polynomial model</td>
    <td class="tg-0pky">overfitting</td>
    <td class="tg-0pky">⬆️</td>
    <td class="tg-0pky">⬇️</td>
  </tr>
  <tr>
    <td class="tg-0pky">Inreducible  error</td>
    <td class="tg-0pky">noisy  data</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
</tbody>
</table>

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/image-20200120105846503.png" alt="image-20200120105846503" style="zoom:50%;" />

## Explaination

A model’s generalization error can be expressed as the sum of three very different errors:

### Bias
This part of the generalization error is due to **wrong assumptions**, such as assuming that the data is linear when it is actually quadratic. 
A high-bias model is most likely to **underfit** the training data.

### Variance
This part is due to the model’s **excessive sensitivity to small variations** in the training data. \
A model with many degrees of freedom (such as a high-degree polynomial model) is likely to have **high variance**, and thus to **overfit** the training data.

### Irreducible Error
This part is due to the **noisiness of the data** itself. 
The only way to reduce this part of the error is to **clean up the data** (e.g., fix the data sources, such as broken sensors, or detect and remove outliers). 

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">High bias</th>
    <th class="tg-0pky">Low bias</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">High variance</td>
    <td class="tg-0pky">something is terribly wrong! 😭</td>
    <td class="tg-0pky">Overfitting</td>
  </tr>
  <tr>
    <td class="tg-0pky">Low variance</td>
    <td class="tg-0pky">Underfitting</td>
    <td class="tg-0pky">too good to be true! 🤪</td>
  </tr>
</tbody>
</table>