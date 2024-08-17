---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 102 # Position in the left sidebar
# ============================================================

# ========== Basic metadata ==========
title: Information, Navigation, and Management Commands
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

## Overview

### What is a shell?

- User interface for running commands

- Interactive language

- Scripting language, can be used to automate tasks

- Default shell: **Bash**. Other shells: sh, ksh, tcsh, zsh, and fish. Check shell with

  ```bash
  printenv SHELL 
  ```

  This returns the path to the default shell program

### Shell command applications

{{< spoiler text="Getting information" >}}
  - `whoam`: User name
  - `id`: User ID and group ID
  - `uname`: OS name
  - `ps`: Running processes
  - `top`: Resource usage
  - `df`: Mounted file systems
  - `man`: Reference manual
  - `date`: Today's date
{{< /spoiler >}}

{{< spoiler text="Navigating and working with files and directories" >}}Files 

- Files
  - `cp`: Copy fiile
  - `mv`: Change file name or path
  - `rm`: Remove file
  - `touch`: Create empty file, update file timestamp
  - `chmod`: Change/modify file permissions
  - `ws`: Get count of lines, words, characters in file
  - `grep`: Return lines in file matching pattern 
- Directory
  - `ls`: List files and directories
  - `find`: Fined files in directory tree
  - `pwd`: Get present working directory
  - `mkdir`: Make directory
  - `cd`: Change directory
  - `rmdir`: Remove directory

{{< /spoiler >}}

{{< spoiler text="Printing file and string contents" >}}

- `cat`: Print file contents
- `more`: Print file contents page-by-page
- `head`: Print first N lines of file
- `tail`: print last N lines of file
- `echo`: Print string or variable value

{{< /spoiler >}}

{{< spoiler text="File compression and archiving" >}}

- `tar`: Archive a set of files
- `zip`: Compress a set of files
- `unzip`: Extract files from a compressed zip archive

{{< /spoiler >}}

{{< spoiler text="Performing network operations" >}}

- `hostname`: Print hostname
- `ping`: Send packts to URL and print response
- `ifconfig`: Display or configure system network interfaces
- `curl`: Display contents of file at a URL
- `wget`: Download file from URL

{{< /spoiler >}}

{{< spoiler text="Monitoring performance and status of the system, its components and applications" >}}

{{< /spoiler >}}

{{< spoiler text="Running batch jobs, such as ETL operations." >}}

{{< /spoiler >}}

## Informational Command

- Display user information
- Verify identity or identify user account

| Command                    | Usage                                                        |
| -------------------------- | ------------------------------------------------------------ |
| `whoami`                   | Return user name                                             |
| `id`                       | User or Group ID<br /><li> `id -u` returns the numerical ID of the user<br /><li>  `id -u -n` returns the name corresponding to the numerical user ID |
| `uname` (Unix name)        | Returns OS information<br /><li> Identify system or diagnose issues |
| `df` (disk free)           | Show disk usage to monitor disk usage or check space         |
| `ps` (process status)      | Monitor or manage processes                                  |
| `top` (table of processes) | Task manger: Monitor system performance and reosurce usage   |
| `echo`                     | Print string or variable value                               |
| `date`                     | Display system date and time                                 |
| `man <command>` (manual)   | Show manual for any command                                  |



{{% callout  info %}}
[`tldr`](https://github.com/tldr-pages/tldr) is a free and open-source collaborative documentation effort, which provides documentation that is more accessible than the traditional man pages, along with practical examples.

Example

![Screenshot of the tldr client displaying the tar command.](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/tldr-dark.png)

{{% /callout %}}

```bash
ls
```

## File and Directory Navigation Commands

 `pwd`, `cd`

`ls`

![截屏2024-08-16 17.53.20](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-08-16%2017.53.20.png)

`find`: Find files in directory tress.

- Example:

  ![截屏2024-08-16 17.21.33](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2024-08-16 17.21.33.png)

  - `iname`: case insensitive



## File and Directory Management Commands

`mkdir`

`rm`
{{% callout  info %}}
If you want to remove multiple files, for example by using a wildcard to find all filenames matching a pattern, it's best practice to confirm or deny each deletion by including the `-i` option, which creates a prompt to ask for confirmation before every deletion.
{{% /callout %}}

{{% callout  warning %}}
Be careful when deleting files or directories! There is normally no way to restore a deleted file once it is deleted, as there is no trash folder. This is why you should always back up, or archive, your important files. You will learn more about archiving files soon.
{{% /callout %}}


`rmdir`: Remove empty directory

`touch`: Create empty file, update file date

`cp`: Copy file or directory (`-r`) to destination

`mv`: Move file or directory

- when the source and target directories are the same, you can use `mv` to rename a file. 
  Example: use `mv` to rename `users.txt` to `user-info.txt` by entering the following command:

  ```
  mv users.txt user-info.txt
  ```

{{% callout  warning %}}
You should always use caution when moving a file. If the target file already exists, it will be overwritten, or replaced, by the source file.
{{% /callout %}}

`chmod` (change mode): Change file permissions

- Specify which permissions to change with a combination of the following characters:

  | Option        | Description                                      |
  | ------------- | ------------------------------------------------ |
  | `r`, `w`, `x` | **Permissions**: read, write, and execute        |
  | `u`,`g`, `o ` | **User categories**: user, group, and all others |
  | `+`, `-`      | **Operations**: grant and revoke                 |

- Example

  ![截屏2024-08-16 17.43.31](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-08-16%2017.43.31.png)

### Managing File Permissions and Ownership

Three possible levels of file ownership in Linux: **user**, **group**, and **other**.

- Whoever creates a file, namely the **user** at the time of creation, becomes the owner of that file by default. 
- A **group** of users can also share ownership of a file. 
- The **other** category essentially refers anyone in the universe with access to your Linux machine - careful when assigning ownership permission to this level!

Only an official owner of a file is allowed to change its permissions. This means that only owners can decide who can read the file, write to it, or execute it.

#### Viewing file permissions

Example:

```bash
$ echo "Who can read this file?" > my_new_file
$ more my_new_file
Who can read this file?
$ ls -l my_new_file
-rw-r--r-- 1 theia users 25 Dec 22 17:47 x
```

Here we've echoed the string `"Who can read this file?"` into a new file called `my_new_file`. The next line uses the `more` command to print the contents of the new file. 

Finally, the `ls` command with the `-l` option displays the file's (default) permissions: `rw-r--r--`.

- The first three characters (`rw-`) define the **user** permissions. You, being the user, have the permission `rw-`, which means you have read and write permissions by default, but do not have execution permissions. Otherwise there would be an `x` in place of the last `-`.
- The next three (`r--`) the **group** pemissions. The final three (`r--`) the **other** permissions.

Looking at the entire line, `rw-r--r--`, you can see that anyone can read the file, nobody can execute it, and you are the only user that can write to it.

{{% callout  info %}}

*The* `-` *at the very beginning of the line in the terminal means that the permissions are referring to a file. If you were getting the permissions to a directory, you would see a* `d` *in the front for "directory".*

{{% /callout %}}


#### Directory permissions

The permissions for directories are similar but distinct for files. Though directories use the same `rwx` format, the symbols have slightly different meanings.

The following table illustrates the meanings of each permission for directories:

| Directory Permission | Permissible action(s)                      |
| -------------------- | ------------------------------------------ |
| `r`                  | List directory contents using `ls` command |
| `w`                  | Add or remove files or directories         |
| `x`                  | Enter directory using `cd` command         |

#### Making a file private

You can revoke read permissions from your group and all other users by using the `chmod` command.

Example:

```bash
$ chmod go-r my_new_file
$ ls -l my_new_file
-rw------- 1 theia users 24 Dec 22 18:49 my_new_file
```

In the `chmod` command, `go-r` is the permission change to be applied, which in this case means removing for the group (`g`) and others (`o`) the read (`r`) permission. 

#### Executable file

A Linux file is executable if it contains instructions that can be directly interpreted by the operating system. Basically, an exectuable file is a ready-to-run program. They're also referred to as **binaries** or **executables**.

**Script** is a particular kind of executable. **shell scripting**, or more specifically **Bash scripting**, which is writing scripts in Bash (*born-again shell*), a very popular shell scripting language. A shell script is a plain text file that can be interpreted by a shell.

Formally speaking, for a text file to be considered an executable shell script for a given user, it needs to have two things:

1. Execute permissions set for that user
2. A directive, called a "shebang", in its first line to declare itself to the operating system as a binary