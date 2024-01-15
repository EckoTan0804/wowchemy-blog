---
title: "Homebrew"
subtitle: 

# Summary for listings and search engines
summary: " "

# Link this post with a project
projects: []

# Date published
date: 2023-05-19

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
- Mac
- Homebrew

categories:
- Tech

---

![Homebrew — The Missing Package Manager for macOS (or Linux)](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/homebrew-social-card.png)

## Installation

Paste that in a macOS Terminal or Linux shell prompt.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Test whether the installation is successful by typing

```bash
brew help
```

## Basic Usages

### Search for package

```bash
brew search <package>
```

*E.g.*:

```bash
brew search postgres
```

![截屏2023-05-20 00.10.23](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2023-05-20%2000.10.23.png)

There are two types of results

- **Foumlae**: Command-line software
- **Casks**: An extension of `Homebrew` that allows us to install MacOS native applications (*e.g.*, Google Chrome)

{{% callout note %}}
We can also search in browser: [Homebrew Formular](https://formulae.brew.sh/).
{{% /callout %}}

### Install packages

```bash
brew install <package>
```

*E.g.*:

```bash
brew install tree
```

Homebrew will install `tree` in `/usr/local/bin/` (we can verify that by typing `which tree`).

If we want to get more information about an (installed) package, we can use 

```bash
brew info <package>
```

### Install packages

```bash
brew uninstall <package>
```

### List installed packages

```bash
brew list
```

### Updating packages

Fetch the newest version of all the packages:

```bash
brew update 
```

View the outdated packages:

```bash
brew outdated 
```

Update/Upgrade outdated packages:

```bash
brew upgrade 
```

Remove older versions of packages:

```bash
brew cleanup
```

### Self-diagnosis

```bash
brew doctor
```

### Install Mac applications

```bash
brew install --cask <package>
```

To see more information about the package (if you are unsure):

```bash
brew info --cask <package>
```

To visit the homepage of the package:

```bash
brew home --cask <package>
```

## Reference

- [Homebrew homepage](https://brew.sh/)
  - [Command documentation](https://docs.brew.sh/Manpage)
  - [Documentation](https://docs.brew.sh/)
- Tutorials
  - {{< youtube SELYgZvAZbU >}}