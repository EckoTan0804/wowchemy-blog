---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 105
# ============================================================

# ========== Basic metadata ==========
title: Differenzierensregeln für Matrizen
date: 2022-06-17
draft: false
type: book # page type
authors:
  - admin
tags:
  - SI
  - Lecture Notes
  - Math
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

{{% callout note %}}
Für eine Matrix $\mathbf{C}$ gilt

{{< math >}}
$$
\frac{\partial}{\partial \mathbf{C}}\left(\underline{a}^{\top} \cdot \mathbf{C} \cdot \underline{b}\right)=\underline{a} \cdot \underline{b}^{\top}
$$
{{< /math >}} 
{{% /callout %}}

Beispiel

{{< math >}}
$$
Q=\underbrace{\left[\begin{array}{ll}
a_{1} & a_{2}
\end{array}\right]}_{\boldsymbol{a}^\top}\left[\begin{array}{ll}
c_{11} & c_{12} \\
c_{21} & c_{22}
\end{array}\right]\underbrace{\left[\begin{array}{l}
b_{1} \\
b_{2}
\end{array}\right]}_{\boldsymbol{b}}=a_{1} b_{1} \cdot c_{11}+a_{2} b_{1} c_{21}+a_{1} b_{2} c_{12}+a_{2} b_{2} c_{22} = \boldsymbol{a} \cdot \boldsymbol{b}^\top
$$
{{< /math >}} 

{{< math >}}
$$
\frac{\partial Q}{\partial \mathbf{C}}=\left[\begin{array}{ll}
\frac{\partial Q}{\partial C_{12}} & \frac{\partial Q}{\partial C_{12}} \\
\frac{\partial Q}{\partial C_{21}} & \frac{\partial Q}{\partial C_{22}}
\end{array}\right]=\left[\begin{array}{ll}
a_{1} b_{1} & a_{1} b_{2} \\
a_{2} b_{1} & a_{2} b_{2}
\end{array}\right]=\left[\begin{array}{l}
a_{1} \\
a_{2}
\end{array}\right]\left[\begin{array}{ll}
b_{1} & b_{2}
\end{array}\right]
$$
{{< /math >}} 

Für eine symmetrische Matrix $\mathbf{C}$:

- Mit $\underline{a}=\underline{e}$ und $\underline{b} = D \cdot \underline{e}$:

  {{< math >}}
  $$
  \frac{\partial}{\partial \mathbf{C}} (\underline{e}^\top \mathbf{C} D \underline{e}) = \underline{e} \cdot \underline{e}^\top \cdot D^\top
  $$
  {{< /math >}} 

- Mit $\underline{a}=D \cdot \underline{e}$ und $\underline{b} = \underline{e}$:

  {{< math >}}
  $$
  \frac{\partial}{\partial \mathbf{C}} (\underline{e}^\top D^\top \mathbf{C} \underline{e}) = D\cdot \underline{e}\cdot \underline{e}^\top 
  $$
  {{< /math >}} 



{{% callout note %}}
{{< math >}}
$$
\frac{\partial}{\partial \mathbf{K}}\left(\boldsymbol{a}^{\top} \cdot \mathbf{K} \cdot \mathbf{C} \cdot \mathbf{K}^{\top} \boldsymbol{b} \right)=\boldsymbol{a} \boldsymbol{b}^{\top} \mathbf{K} \mathbf{C}^{\top}+\boldsymbol{b} \boldsymbol{a}^{\top} \mathbf{K} \mathbf{C}
$$
{{< /math >}} 
{{% /callout %}}

Seien $\boldsymbol{a} = \boldsymbol{e}, \boldsymbol{b} = \boldsymbol{e}$, $\mathbf{C}$ symmetrisch, dann gilt

{{< math >}}
$$
\frac{\partial}{\partial \mathbf{K}}\left(\boldsymbol{e}^{\top} \cdot \mathbf{K} \cdot \mathbf{C} \cdot \mathbf{K}^{\top} \boldsymbol{e} \right)=\boldsymbol{e} \boldsymbol{e}^{\top} \mathbf{K} \mathbf{C}^{\top}+\boldsymbol{e} \boldsymbol{e}^{\top} \mathbf{K} \mathbf{C} = 2\boldsymbol{e} \boldsymbol{e}^{\top} \mathbf{K} \mathbf{C}
$$


{{< /math >}} 
