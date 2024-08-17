---
# ===== Title, summary, and position in the left sidebar =====
linktitle:   # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 103 # Position in the left sidebar
# ============================================================

# ========== Basic metadata ==========
title: Text Files, Networking, and Archiving Commands
date: 2024-08-17
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

## Text File Commands

### Viewing file content

`cat` (catenate): Print entire file contents

- Limitation: If the file content is long, the output will take up the entire terminal window

`more`: Print file content page-by-page

`head`: Print first 10 lines of file

- `head -n <N>`: Print first N lines of file

`tail`: Print last 10 lines of file

- `tail -n <N>`: Print last N lines of file

`wc` (word count): Count lines, words, characters

- `-l`/`-w`/`-c`: View only line/word/character count

### Wrangling text files

`sort`: Sort the lines of a file alpha-numerically and prints the sorted result to standard output.

- `-r`: Reverse order

`uniq` (unique): Filter out the repeated lines

- Note: `uniq` only removes duplicated lines if they are consecutive!

`grep` (global regular expression print): Return lines of a file matching a specified pattern

- Example

  ![截屏2024-08-17 13.38.36](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-08-17%2013.38.36.png)

- Some frequently used options for `grep` include:

  | Option | Description                                                |
  | ------ | ---------------------------------------------------------- |
  | `-n`   | Along with the matching lines, also print the line numbers |
  | `-c`   | Get the count of matching lines                            |
  | `-i`   | Ignore the case of the text while matching                 |
  | `-v`   | Print all lines which do not contain the pattern           |
  | `-w`   | Match only if the pattern matches whole words              |

`cut`: Extract a section from each file

- Example

  - Extract the second to ninth characters from every line

  ![ ](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-08-17%2013.41.17.png)

  - Extract the last names

    ![截屏2024-08-17 13.42.29](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-08-17%2013.42.29.png)

    - `-d ' '`: Specify space as the field delimiter
    - `-f2`: Return the second filed from each line

`paste`: Merge lines from different files

## Networking Commands

### Brief introduction to networking

#### Computer networks

A **computer network** is a set of computers that are able to communicate with each other and share **resources** provided by **network nodes**. Examples of computer networks include **Local Area Networks (LANs)**, **Wide Area Networks (WANs)**, and the entire Internet. The Internet, or World Wide Web, is essentially a giant network of computer networks.

A network **resource** is any object, such as a file or document, which can be *identified* by the network.

- An object is ***identifiable*** if it can be assigned a *unique* name and address that the network can use to identify and access it.

A **network node** is any device that participates in a network.

- A network can include any device which is not necessarily a computer but is part of the network’s infrastructure. Examples of network nodes include modems, network switches, hubs, and wifi hotspots.

#### Host, clients, and servers

A **host** is a special type of node in a computer network - it is a computer that can function as a **server** or a **client** on a network.

A **server** is a host computer that is able to accept a connection from a **client** host and fulfill certain resource requests made by the client.

Many hosts can perform either role, acting as both client and server.

#### Packets and pings

A **network packet** is a formatted chunk of data that can be transmitted over a network.

-  Today's computer networks typically use communication protocols that are based on such packets of information. Every packet consists of two types of data: 

  - the **control information**
  -  the **payload**. 

  The control information is data about how and where to deliver the payload, such as the source and destination network addresses, while the payload is the message being sent.

The `ping` command works by sending special 'echo request' packets to a host and waiting for a response from the host.

> `ping` is a utility available on most operating systems that have networking capability. Linux has its own implementation of the `ping` command that's used to test and troubleshoot connectivity to other network hosts.

#### URLs and IP adresses

IP stands for "Internet Protocol" which defines the format of data transmitted over the internet or a local network.

An **IP address** is a code used to uniquely identify any host on a network.

> An IP address can be used to establish a connection to a host and exchange packets with it, for example using the `ping` command. In addition to their payload, IP packets - a type of network packet that conforms to the Internet Protocol - contain the IP addresses of the source and destination hosts.

A **URL**, more commonly known as a web address, stands for *Uniform Resource Locator*.

> A URL uniquely identifies a web resource and enables access to that resource. Typically the resource that a URL points to is a web page, but it can also be used for tasks such as transferring files, sending emails, and accessing databases.

> For example, the URL to the Wikipedia page for URL is `https://en.wikipedia.org/wiki/URL`. Just like for a typical URL, its format indicates a protocol (`https`), a hostname (`en.wikipedia.org`), and a file name (`/wiki/URL`).

### Networking commands

`hostname`: Print host name

- `-s`: Drop the domain suffix

- `-i`: Provide the IP address of the hostname

- Example

  ![截屏2024-08-17 14.57.31](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-08-17%2014.57.31.png)

`ifconfig` (Interface configuration): Display or configure the system network interfaces

- `eth0`: SHow ethernet config information

`ping`: Send ICMP packets to URL and print response

- `c`: Return a set number of ping results

`curl` (Client URL): Transer data to and from URL(s)

`wget` (Web get): Download file(s) from a URL

- More focused than `curl`, supports recursive file downloads

## Archiving and Compression Commands

Archiving and compression are distinct processes, which are usually combined

- **Archiving**: Process of storing information that you don't use regularly but want to preserve
  - An “archive file” is a collection of data files and directories that are stored as a single file. 
  - Archiving makes the collection more portable and serves as a backup in case of loss or corruption.
- Compressing: Reducing the size of a file by taking advantage of redundancy in its information content.
  - Advantages
    - Preserve storage space
    - Speed up data transfer
    - Reduce bandwidth load 

`tar` (tape archiver): Archive and extract files, allows you to pack multiple files and directories into a single archive file.

- `-c`: Create a new archive
- `-f`: Tell tar to interpret its input from the file rather than from the default, which is standard input
- `-z`: Compress the archive file with `gzip`
- `-v`: Verbosely list files processed
- `tar -tf`: List archive contents
- `tar -xf`: Extract ("untag") file and folders
- `tar -xzf`: Decompress and extract

`zip`: Compress files and directories to an archive

{{% callout Different between `zip` and `tar` %}}

`zip` compresses files prior to bundling them, Whereas `tar`, with the `-z` option, achieves compression by applying `gzip` on the entire tarball, but only after bundling it.

![截屏2024-08-17 22.33.23](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-08-17%2022.33.23.png)


{{% /callout %}}

`unzip`: Extract and decompress zipped archive