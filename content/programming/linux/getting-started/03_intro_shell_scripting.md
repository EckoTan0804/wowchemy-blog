---
# ===== Title, summary, and position in the left sidebar =====
linktitle:   # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 104 # Position in the left sidebar
# ============================================================

# ========== Basic metadata ==========
title: Shell Scripting
date: 2024-08-15
draft: false
type: book # page type
authors:
  - admin
tags:
  - Linux
  - OS
  - Shell scripting
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

## Shell Scripting Basics

A **script** is a list of commands that can be interpreted and run by a program called **scripting  language**, which is usually not compiled but interpreted at runtime instead.

- Generally slower to run than compiled languages, but they are also much easier and faster to develop
- Widely used to automate processes, such as
  - ETL jobs
  - File backups and archiving
  - System administration tasks

Shell script is an executable text file with an interpreter directive, a.k.a. "shebang" (``#!``) directive, which has the form "pound, bang, interpreter" plus an optional argument

```bash
#!interpreter [optional-arg]
```

- `interpreter`: An absolute path to an executable program
- `optional-arg`: A string representing a single argument

Example:

- `#!/bin/sh` invokes the Bourne shell or other compatible shell program, from the bin directory.
- `#!/bin/bash` invokes the BAsh shell
- `#!/usr/bin/env python3`

## Shell Variables

**Shell variables** offer a powerful way to store and later access or modify information such as numbers, character strings, and other data structures by name.

Example

```bash
$ firstname=Jeff
$ echo $firstname
Jeff
```

The first line assigns the value `Jeff` to a new variable called `firstname`. The next line accesses and displays the value of the variable, using the `echo` command along with the special character `$` in front of the variable name to extract its value, which is the string `Jeff`. Thus, we have created a new shell variable called `firstname` for which the value is `Jeff`.

Another way to create a shell variable is to use the `read` command, which reads user input into a shell variable. 

Example:

```bash
$ read lastname  
Grossman  
$ echo $lastname  
Grossman  
```

The `read` command is particularly useful in shell scripting. You can use it within a shell script to prompt users to input information, which is then stored in a shell variable and available for use by the shell script while it is running.

## Filters, Pipes, and Variables

#### Filters

**Filters** are shell commands, which

- Take input from standard input
- Send output to standard output
- Transform input data into output data
- Examples: `wc`. `cat`. `more`, `head`, `sort`, `grep`
- Filters can be chain together!

#### Pipe (Pipeline)

**Pipe command (`|`)** : for chaining filter commands

- Use pattern

  ```bash
  [command 1] | [command 2] | [command 3] ... | [command n]
  ```

  E.g.,

  ```bash
  command 1 | command 2
  ```

  Output of  `command 1` is input of `command 2`

  ![截屏2024-08-18 14.46.10](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-08-18%2014.46.10.png)

- Example

  ![截屏2024-08-18 14.01.00](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-08-18%2014.01.00.png)

#### Variables

- Scope limited to shell

- `set`: List all variables and their definitions that are visible to the current shell

- Define shell variables

  ```bash
  var_name=value  # Note: NO space around "="!
  ```

  Clear/Delete a variable\

  ```bash
  unset var_name
  ```

  Example

  ![截屏2024-08-18 14.09.56](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-08-18%2014.09.56.png)

- **Environment variables**: Just like shell variables, except they have extended scope. They persist in any child processes spawned by the shell in which they originate.

  - Extend shell variable to environment variable:

    ```bash
    export var_name
    ```

    Example

    ```bash
    export GREETINGS
    ```

    makes the `GREETINGS` variable defined in the example above an environment variable

  - `env`: List all environment variables

## Useful Features of the Bash Shell

### Metacharacters

**Metacharacters** are special characters that have meaning to the shell.

- `#`: Precedes a comment that the shell ignores

- `;`: Seprate commands typed on the same line, e.g., 

  ```bash
  $ echo "Hello" ; whoami
  ```

- `*`: Filename expansion wildcard, represents any number of consecutive characters within a filename pattern

- `?`: Single character wildcard in filename expansion (a single-character version of `*` ), e.g.,

  ![截屏2024-08-18 14.59.31](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-08-18%2014.59.31.png)

- `\`: Escape unique character interpretation
- `" "`: Interpret literally, interpret metacharacters within string
- `' '`: Interpret literally, escape all metacharacters within string

Example:

![截屏2024-08-18 15.36.03](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-08-18%2015.36.03.png)

### I/O redirection

**Input/Output**, or **I/O redirection**, refers to a set of features used for redirecting either the standard input, the keyboard, or the standard output, the terminal. 

- `>`: Redirect output to the file. It also creates the file if it doesn’t exist and overwrites its contents if it already exists.
- `>>`: Append output to the file
- `2>`: Ridirect standard error to file
- `2>>`: Append standard error to file
- `<`: Redirect file contents to standard input

Example

![截屏2024-08-18 15.40.10](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-08-18%2015.40.10.png)

### Command substitution

- Replace the command with its output: `$(command)$` or `command`. Example:

  ![截屏2024-08-18 15.42.02](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-08-18%2015.42.02.png)

### Command line arguments

- Program arguments specified on the command line
- A way to pass arguments to a shell script

Example

```bash
$ ./MyBashScript.sh arg1 arg2
```

### Batch vs. concurrent modes

**Batch mode**: Commands run *sequentially*

```bash
command 1; command 2  
```

Command 2 only runs after command 1 is completed.

**Concurrent mode**: Commands run in *parallel*

```bash
command 1 & command 2
```

The ampersand operator, after command 1, directs command 1 to operate in the background and passes control to command 2 in the foreground. 

## Advanced Bash Scripting

### Conditionals

Bash script conditionals use the following `if`-`then`-`else` syntax:

```bash
if [ condition ]
then
    statement_block_1  
else
    statement_block_2  
fi
```

{{% callout info %}}

- You must always put spaces around your condition within the square brackets `[` `]`.
- Every `if` condition block must be paired with a `fi` to tell Bash where the condition block ends.
- The `else` block is optional but recommended. If the condition evaluates to `false` without an `else` block, then nothing happens within the `if` condition block. Consider options such as echoing a comment in `statement_block_2` to indicate that the condition was evaluated as `false`.


{{% /callout %}}

Example: the condition is checking whether the number of command-line arguments read by some Bash script, `$#`, is equal to 2.

```bash
if [[ $# == 2 ]]
then
  echo "number of arguments is equal to 2"
else
  echo "number of arguments is not equal to 2"
fi
```

Notice: the use of the double square brackets, which is the syntax required for making integer comparisons in the condition `[[ $# == 2 ]]`.

{{% callout  info %}}

`$` can be used to access command-line arguments passed to the script.

Examples:

- `$0`: The name of the script.
- `$1`, `$2`, `$3`, ...: The first, second, third, etc., arguments passed to the script.
- `$#`: The number of arguments passed.
- `$@` or `$*`: All arguments as a list.
- `$?`: The exit status of the last command.
- `$$`: The process ID (PID) of the current script.

{{% /callout %}}

You can also make string comparisons. For example, assume you have a variable called `string_var` that has the value `"Yes"` assigned to it. Then the following statement evaluates to `true`:

```bash
`[ $string_var == "Yes" ]`  # Only need single square brackets for string comparison
```

You can also include multiple conditions to be satified by using the **"and" operator `&&`** or the "or" operator `||`. Example

```bash
if [ condition1 ] && [ condition2 ]
then
    echo "conditions 1 and 2 are both true"
else
    echo "one or both conditions are false"
fi


if [ condition1 ] || [ condition2 ]
then
    echo "conditions 1 or 2 are true"
else
    echo "both conditions are false"
fi
```

`if`-`then`-`elif`-`else` Syntax:

```bash
if [ condition ]
then
    statement_block_1  
elif
    statement_block_2  
else
	statement_block_3
fi
```

### Logical Operators

- `==`: is equal to

  ```bash
  # If a variable a has a value of 2, the following condition evaluates to true; otherwise it evalutes to false.
  $a = 2
  ```

- `!=`: is not equal to

- `<=` or `-le`: is less than or equal to

More see: [Advanced Bash-Scripting Guide](https://tldp.org/LDP/abs/html/comparison-ops.html) 

### Arithmetic calculations

You can perform integer addition, subtraction, multiplication, and division using the notation `$(())`.

Example

```bash
echo $((3+2))
```

```bash
a=3
b=2
c=$(($a+$b))
echo $c
```

{{% callout  warning %}}
Bash natively handles integer arithmetic but does not handle floating-point arithmetic. As a result, it will always truncate the decimal portion of a calculation result.
{{% /callout %}}

Basic arithmetic operators:

| Symbol | Operation      |
| ------ | -------------- |
| `+`    | addition       |
| `-`    | subtraction    |
| `*`    | multiplication |
| `/`    | division       |

### Arrays

An array is a space-delimited list contained in parentheses. To create an array, declare its name and contents:

```bash
my_array=(1 2 "three" "four" 5)
```

If you want to add items to your array after creating it, you can add to your array by appending one element at a time:

```bash
my_array+=("six")
my_array+=(7)
```

This adds elements `"six"` and `7` to the array `my_array`.

By using indexing, you can access individual or multiple elements of an array:

```bash
# print the first item of the array:
echo ${my_array[0]}

# print the third item of the array:
echo ${my_array[2]}

# print all array elements:
echo ${my_array[@]}
```

Get the array length:

```bash
arr_len=${#arr[@]}  
```

or

```bash
arr_len=${#arr[*]} 
```

Here `#` gives the lenght of the array (or string).

### `for` loops

You can use a `for` loop along with indexing to iterate over all elements of an array.

Syntax

- The `for` loop requires a `; do` component in order to cycle through the loop. 
- You need to terminate the `for` loop block with a `done` statement.

```bash
for item in ${arr[@]}; do
	# Handle $item
done
```

```bash
for i in ${!arr[@]}; do
  # Handle ${arr[$i]}
done
```

Another way to implement a `for` loop when you know how many iterations you want is as follows. For example, the following code prints the number 0 through 6.

```bash
N=6
for (( i=0; i<=$N; i++ )) ; do
  echo $i
done
```

## Scheduling Jobs Using Cron

Job scheduling: Schedule jobs to run automatically at certain times. E.g., "Backup script to run every Sunday at 2AM".

**Cron** is the general name of the tool that runs scheduled jobs consisting of shell commands or shell scripts. 

**Crond** is the daemon or service that interprets “crontab files” every minute and submits the corresponding jobs to cron at scheduled 

times. 

A **crontab**, short for “cron table,” is a simple text file containing jobs and schedule data. Crontab is also a command that invokes a text editor to allow you to edit a crontab file.

#### Adding jobs in Crontab

Enter `crontab -e` opens the default text editor and allows you to specify a new schedule and a new command.

Syntax:

```bash
m h dom mon dow command
```

Five time-and-date fields `m h dom mon dow` stand for: minute, hour, day of month, month, and day of week. All five positions must have either a numeric entry or an asterisk (`*`), which is a wildcard symbol that means “any.”

The five time-and-date fields cannot contain spaces and their allowed values are as follows:

| Field   | Allowed values     |
| ------- | ------------------ |
| minute  | 0-59               |
| hour    | 0-23, 0 = midnight |
| day     | 1-31               |
| month   | 1-12               |
| weekday | 0-6, 0 = Sunday    |

Example: Append the current date to the file ‘sundays.txt’ at 15:30 every Sunday. 

```bash
30 15 * * 0 date >> sundays.txt
```

Then save and exit the editor.

#### Viewing and removing Cron jobs

Viewing: `crontab -l`

Removing

- Use `crontab -e` to open the editor and remove specific line(s)
- `crontabl r`: Remove all cron jobs 







