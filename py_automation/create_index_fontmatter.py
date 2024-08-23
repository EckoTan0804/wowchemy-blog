def create_top_level_index_fontmatter(title):
    return f"""---
linktitle: 
title: {title}
layout: docs

# View.
#   1 = List
#   2 = Compact
#   3 = Card
view: 2
draft: false

# Optional header image (relative to `assets/media/` folder).
header:
    caption: ""
    image: ""
---
"""


def create_sub_level_index_fontmatter(title, date, weight, tag, category):
    return f"""---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: {weight}
# ============================================================

# ========== Basic metadata ==========
title: {title}
date: {date}
draft: false
type: book # page type
authors:
    - admin
tags:
    - {tag}
categories:
    - {category}
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
"""
