---
# ===== Title, summary, and position in the left sidebar =====
linktitle:   # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 101 # Position in the left sidebar
# ============================================================

# ========== Basic metadata ==========
title: Introduction to Linux
date: 2024-08-15
draft: false
type: book # page type
authors:
  - admin
tags:
  - Linux
  - OS
categories:
  - Coding
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



## Linux and Unix

**Operating System (OS)** is software that

- manages computer hardware and resources

- allows interaction with hardware to perform useful tasks

**Unix** 

- A family of operating systems

- Popular Unix-based OS:

  - HP-UX

  - IBM AIX

  - Apple macOS

**Linux**

- Family of Unix-like OSs (usually specific distribution)

- Originally developed as an effort to create a free, open-source Unix OS

- Key features

  - Free and  open source

  - Secure

  - Multi-user

  - Multitasking

  - Portability

- Use cases

  - Android

  - Supercomputers

  - Data centers and cloud services

  - PCs

## Linux Distributions

Linux distribution

- A specific flavor of Linux OS

- Also referred to as **Distro**

- Core component: Linux kernel

Linux distro differences

- System utilities

- GUI

- Shell commands

- Support types

  - Community vs. enterprise

  - Long-tem support (LTS) vs. rolling release

Common/popular distro

- **Debian**

  - One of the  earliest-rooted distros: first release in 1993 (named version 0.01) and the first official, stable release in 1996 (version 1.1)

  - Features

    - Stable, reliable, and fully open source
    - Supports many computer architectures (or types of hardware)

    -> Highly regarded in the server space

  - Largest community-run distro

- **Ubuntu**

  - Debian-based, used a lot of the same tools as the Debian OS

  - Three official editions

    - Desktop: for personal computers, laptops, and workstations

    - Server:for simple file servers or multinode clouds

    - Core: for the Internet of Things (IoT)

- **Red Hat Linux**

  - A "core" Linux distro (meaning that it is not derived from another Linux distro)

  - Stable, reliable, and fully open source

  - Ships as ***Red Hat Enterprise Linux (or RHEL)***, an edition focused entirely on enterprise customers

- **Fedora**

  - Supports many architectures

  - Very reliable and secure

  - Actively developed, with a large and growing community

- **SUSE Enterprise** (a.k.a SLE)

  - Available in two editions

    - Serve (SLES)

    - Desktop (SLED)

  - Supports many architecture (e.g., ARM for Raspberry Pi)

  - Uses the SUSE Package Hub -> Enable users to install packages that aren't officially part of SLE

- **Arch Linux**

  - Do-it-yourself (DIY) approach

  - Highly configurable -> Requires strong understanding of Linux and system tools

  - Not focus on stability -> easy access to the newest software

## Linux Architecture

![linux_5_layer_arch](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/linux_5_layer_arch.PNG)

| Layer            | Function                                                     | Tasks / Jobs                                                 |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| UI               | Allows users to interact with the system using a keyboard or mouse | Use a web browser to send an Email                           |
| Application      | Includes system daemons, programming languages, shells, user apps, tools |                                                              |
| Operating system | Responsible for jobs that are vital for system stability such as job scheduling and keeping track of time | <li>Assign software to users <br/><li>Help detect errors and prevent failures<br/><li>Perform file management tasks |
| Kernel           | <li>Core component of the OS, responsible for managing memory, processing, and securtiy<br/><li>Lowest-level software, starts on boot<br/><li>Bridge between apps and hardware | <li>Memory management<br/><li>Process management<br/><li>Device drivers<br/><li>Security |
| Hardward         | Includes all the physical or electronic devices in the computer such as processors, memory modules, input devices, and storage |                                                              |

### Linux filesystem

- Collections of files in your machine

- Begins at root directory (`\`)

- Tree-like structure

- Assigns appropriate access rights

![linux_filesystem](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/linux_filesystem.PNG)

-  `/bin`

   - Contains user binary files, which contain the code your machine reads to run programs and execute commands. 

   - It’s called "slash bin" to signify that it exists directly below the root directory.

-  `/usr`: contains user programs

-  `/home`: Your personal working directory where you should store all your personal files

-  `/boot`: Contains your system boot files, the instructions vital for system startup

-  `/media`: Contains files related to temporary media such as CD or USB drives that are connected to the system

## Linux Terminal

**Shell** 

- An OS-level application that interpreets commands.

- You can use shell command to (e.g.)

  - Move and copy files

  - Write to and read from files

  - Extract and filter data

  - Search for data

- Popular shells

  - Bash

  - Zsh

**Terminal**

- An application to interact with the shell

- Enter commands and receive output from them

### Linux system communication

![linux_terminal_communication](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/linux_terminal_communication.PNG)

1. User enters the command in a terminal, which is then relayed to the shell. 

2. The core components of the operating system and kernel translate the command for the hardware to perform. 

3. When the hardware completes the command, the kernel reads any changes or results and sends them back via the shell to the terminal for the user’s information.

### Linux filesystem paths

The filesystem is the human-readable directory or file location.

- `a/b`  indicates that the file or directory named "b" is located inside the directory named "a".

- Special paths

  - `/`: Root directory

  - `~`: Home directory, an important subdirectory of the root directory

  - `..`: Parent of current directory

  - `.`: Current directory

- Filesystem-related commands

  - `cd` : <u>c</u>hange <u>d</u>irectory

  - `pwd`: print path name for <u>p</u>resent <u>w</u>orking <u>d</u>irectory

  - `ls`: list the contents of the directory

## Creating and Editing Text Files

Popular text editors

- Command-line text editors

  - GNU nano: use `nano <filename>` to open a text file in GNU nano from the command prompt

  - vi

  - vim

    - Insert mode

      - Press `i` to enter Insert mode

      - Type some text

      - Press Esc to exist Insert mode and switch to Command mode. Now the text is written to the buffer at the cursor location.

    - Command mode

      - Enter `:sav <filename>` to create a file and write the buffer to the file

      - Enter `:w` to write the buffer to the file without exiting

      - Enter `:q` to quit vim session

      - Enter `:q!` to quit without saving

- GUI-based text editors

  - gedit

- Command-line or GUI: emacs

## Install Software and Updates

**Packages**: Archive files for installing new software or updating existing software

- Deb packages (.deb files): For Debian-based distributions (e.g., Debian, Ubuntu, and Mint)

- RPM packages (.rpm files): For Red Hat-based distributions (e.g., CentOS/RHEL, Fedora, and openSUSE)

  > RPM: Red Hat Package Manager

.deb and .rpm formats are equivalent. You can use `alien` to convert it

- RPM to deb

  ```bash
  alien <package-name>.rpm
  ```

- deb to RPM

  ```bash
  alien -r <package-name>.deb
  ```



**Package managers**

- Manage the download and installation of packages

- Available for different Linux distros

- Can be GUI-based or command-line tools

- Benefits

  - Automatically resolve dependencies

  - Notify you when updates are available

  - Automatic or manual installation

For deb-based

- GUI-based: Update Manager
- Command line-based:  `apt`
  - `sudo apt update`: Find available packages for your distro
    - The output of this command lists each available package, builds a dependency tree, and lets you know how many packages can be upgraded
  - `sudo apt upgrade`: Upgrad all installed packages on a system
  - `sudo apt install <package_name>`: Install a specific package

 

For RPM-based

- GUI-based: PackageKit
- Command line-based: `yum`
  - `sudo yum update`: Update all packages in system
  - `sudo yum install<package_name>`: Install a specific package
