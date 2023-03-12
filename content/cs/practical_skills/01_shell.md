---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 01
# ============================================================

# ========== Basic metadata ==========
title: Shell
date: 2023-03-11
draft: false
type: book # page type
authors:
  - admin
tags:
  - Practical Skills
  - CS
  - Programming
categories:
  - CS
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

TL;DR

- Shell is a programming environement. It has variables, conditionals, loops, and functions.
  - When shell is askedt o execute a command, it search the required program in `$PATH`

- There are two types of paths: absolute and relative.
- Default input and output of program executed in shell are both terminal (i.e., keyboard as input and screen as output).
  - We can redirect the input and output streams using with `< file` (input from file), `> file` (output to file and rewrite it), and `>> file` (output to file and append at the end).

- Roo user is a powerful tool. 
  - Use the `sudo` command.
  - But double check that you really wanted to use it!


------

## Using the shell

When you launch your terminal, you will see a ***prompt*** that often looks a little like this:

```bash
missing:~$ 
```

- You are on the machine called `missing`

- Your “current working directory”, or where you currently are, is `~` (short for “home”)

- The `$` tells you that you are not the root user

At this prompt you can type a *command*, which will then be interpreted by the shell. 

### Example

```bash
missing:~$ date
Fri 10 Jan 2020 11:49:31 AM EST
```

Here, we executed the `date` program, which (perhaps unsurprisingly) prints the current date and time. The shell then asks us for another command to execute.

```bash
missing:~$ echo hello
hello
```

We told the shell to execute the program `echo` with the argument `hello`. 

- The `echo` program simply prints out its arguments.

- The shell parses the command by splitting it by whitespace, and then runs the program indicated by the first word, supplying each subsequent word as an argument that the program can access.

  - If you want to provide an argument that contains spaces or other special characters (e.g. "Hello world"), you can either quote the argument with `'` or `"` (`"Hello world"`), or escape just the relevant characters with `\` (`Hello\ world`)

### Under the hood

**The shell is a programming environment**, just like Python or Ruby. 

- It has variables, conditionals, loops, and functions. 

- When you run commands in your shell, you are really writing a small bit of code that your shell interprets.

- If the shell is asked to execute a command that doesn’t match one of its programming keywords, it consults an *environment variable* called `$PATH` that lists which directories the shell should search for programs when it is given a command

  ```bash
  missing:~$ echo $PATH
  /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
  
  missing:~$ which echo
  /bin/echo
  
  missing:~$ /bin/echo $PATH
  /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
  ```

   - When we run the `echo` command,

     - The shell sees that it should execute the program `echo`, and then searches **through the `:`-separated list of directories in `$PATH`** for a file by that name.

     - When it finds it, it runs it (assuming the file is *executable*)

   - We can find out which file is executed for a given program name using the `which` program. 

   - We can also bypass `$PATH` entirely by giving the *path* to the file we want to execute.

## Navigating in the shell

A path on the shell is a delimited list of directories; separated by `/` on Linux and macOS and `\` on Windows.

- On Linux and macOS, the path `/` is the “root” of the file system, under which all directories and files lie.

- on Windows there is one root for each disk partition (e.g., `C:\`).

In the following, it is assumed that a Linux filesystem is being used.

- **Absolute path**: A path that starts with `/`.

- **Relative path**: Relative to the current working directory

  - We can see with the `pwd` command and

  - change with the `cd` command

In a path, 

- `.` : the current directory
-  `..`:  its parent directory
- `~`: the `$HOME` directory
- `cd -`  : `cd` to the directory you're previously in

Example

```bash
missing:~$ pwd  # print working directory
/home/missing

missing:~$ cd /home

missing:/home$ pwd
/home

missing:/home$ cd ..

missing:/$ pwd
/

missing:/$ cd ./home

missing:/home$ pwd
/home

missing:/home$ cd missing

missing:~$ pwd
/home/missing

missing:~$ ../../bin/echo hello
hello
```

> Notice that our shell prompt kept us informed about what our current working directory was. You can configure your prompt to show you all sorts of useful information

In general, when we run a program, it will operate **in the current directory unless we tell it otherwise**.

To see what lives in a given directory, we use the `ls` command.

- Unless a directory is given as its first argument, `ls` will print the contents of the current directory.

- Example

  ```bash
  missing:~$ ls -l /home
  drwxr-xr-x 1 missing  users  4096 Jun 15  2019 missing
  ```

   - The `d` at the beginning of the line tells us that `missing` is a directory.

   - The following three groups of characters (`rwx`) indicate permissions (`r`-read, `w`-write, `x`-execute) of

     - the owner of the file (`missing`)

     - the owning group (`users`)

     - everyone else

   - Permissions

     - A `-` indicates that the given principal does not have the given permission

       - Above, only the owner (with permission `rwx`) is allowed to modify (`w`) the `missing` directory (i.e., add/remove files in it).

     - To enter a directory, a user must have “search” (represented by “execute”: `x`) permissions on that directory (and its parents).

     - To list its contents, a user must have read (`r`) permissions on that directory.

{{% callout note %}}
If you ever want *more* information about a program’s arguments, inputs, outputs, or how it works in general, give the `man` program a try. 

- It takes as an argument the name of a program, and shows you its *manual page*. 

- Press `q` to exit.
{{% /callout %}}

## Connecting programs

In the shell, programs have two primary “streams” associated with them: their **input stream** and their **output stream**. 

- When the program tries to read input, it reads from the input stream.

- When it prints something, it prints to its output stream.

**Normally, a program’s input and output are both your terminal. That is, your keyboard as input and your screen as output.**

We can also rewire those streams. The simplest form of redirection is

- `< file`: rewire the input of this program to be the content of `file` 
-  `> file`: rewire the output of the preceding programi into this file

(more see [How to do input/output redirection in Linux](https://www.educative.io/answers/how-to-do-input-output-redirection-in-linux)). These let you rewire the input and output streams of a program to a file respectively. 

Example:

```bash
missing:~$ echo hello > hello.txt

missing:~$ cat hello.txt
hello

missing:~$ cat < hello.txt
hello

# Read content from hello.txt and output to hello2.txt
missing:~$ cat < hello.txt > hello2.txt  

missing:~$ cat hello2.txt
hello
```

`cat` is a program that con`cat`enates files. 

- When given file names as arguments, it prints the contents of each of the files in sequence to its output stream

- But when `cat` is not given any arguments, it prints contents from its input stream to its output stream (like in the third example above).

Note that `>` will overwrite the target file. If you want to append instead, use `>>`.

Where this kind of input/output redirection really shines is in the use of ***pipes***: **The `|` operator lets you “chain” programs such that the output of one is the input of another**. The `|` operator takes the output of the program to the left and make it the input of the program to the right.

E.g.: When you use `cat` command to view a file which spans multiple pages, the prompt quickly jumps to the last page of the file, and you do not see the content in the middle. To avoid this, you can pipe the output of the `cat` command to `less` which will show you only one scroll length of content at a time ([Pipe, Grep and Sort Command in Linux/Unix with Examples](https://www.guru99.com/linux-pipe-grep.html#:~:text=is%20a%20Filter%3F-,What%20is%20a%20Pipe%20in%20Linux%3F,'%7C'%20denotes%20a%20pipe.)).

```bash
missing:~$ cat hello2.txt | less
```

## A versatile and powerful tool

On most Unix-like systems, one user is special: **the “root” user**.

- The root user is above (almost) all access restrictions, and can create, read, update, and delete any file in the system.

- You will not usually log into your system as the root user though, since it’s too easy to accidentally break something.

  - Instead, you will be using the `sudo` command. As its name implies, it lets you “do” something “as su” (short for “super user”, or “root”).

- When you get permission denied errors, it is usually because you need to do something as root. Though make sure you first double-check that you really wanted to do it that way!!!

## Reference

- [Course overview + the shell](https://missing.csail.mit.edu/2020/course-shell/)

  {{< youtube Z56Jmr9Z34Q>}}