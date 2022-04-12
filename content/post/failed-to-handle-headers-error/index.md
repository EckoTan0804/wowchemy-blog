---
title: "Solution of \"Error: failed to resolve output format\""
subtitle: 

# Summary for listings and search engines
summary: " "

# Link this post with a project
projects: []

# Date published
date: 2022-04-12

# Date updated
lastmod: 

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

share: true 

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
# image:
#   caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/CpkOjOcXdUY)'
#   focal_point: ""
#   placement: 2
#   preview_only: false

authors:
- admin

tags:
- Troubleshooting

categories:
- Blog

---

Sometimes when I try to build my website locally, I come across an error:

```bash
Error: from config: failed to resolve output format "headers" from site config
```

To resolve this issue, simply follow the steps from [Wowchemy website](https://wowchemy.com/docs/hugo-tutorials/troubleshooting/?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=fr&_x_tr_pto=nui#error-failed-to-resolve-output-format):

1. Manually **delete Hugo’s default cache folder** (Hugo’s cache folder defaults to `$TMPDIR/hugo_cache/` on Mac/Linux and `%TMP%\hugo_cache\` on Windows.)

2. Re-run Hugo

   ```bash
   hugo server
   ```

   



## Reference

- [Troubleshooting: Error: failed to resolve output format](https://wowchemy.com/docs/hugo-tutorials/troubleshooting/?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=fr&_x_tr_pto=nui#error-failed-to-resolve-output-format)
- [Error: failed to resolve output format #2532](https://github.com/wowchemy/wowchemy-hugo-themes/discussions/2532)