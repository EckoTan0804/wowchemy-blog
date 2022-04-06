---
linktitle: ''
summary: ''
weight: 37
title: MOESI Protocol
date: 2020-07-29
draft: false
type: book
authors:
- admin
tags:
- Vorlesung
- Rechnerstruktur
categories:
- Computer Structure
toc: true
profile: false
reading_time: true
share: true
featured: true
comments: true
disable_comment: false
commentable: true
editable: false
---

## Overview

In computing, MOESI is a full [cache coherency](https://en.wikipedia.org/wiki/Cache_coherency) protocol that encompasses all of the possible states commonly used in other protocols. In addition to the four common [MESI protocol](https://en.wikipedia.org/wiki/MESI_protocol) states, there is a fifth "**Owned**" state representing data that is both modified and shared. This avoids the need to write modified data back to main memory before sharing it. While the data must still be written back eventually, the write-back may be deferred.

This protocol, a more elaborate version of the simpler [MESI protocol](https://en.wikipedia.org/wiki/MESI_protocol) (but not in extended MESI - see [Cache coherency](https://en.wikipedia.org/wiki/Cache_coherency)), **avoids the need to write a dirty cache line back to [main memory](https://en.wikipedia.org/wiki/Main_memory) when another processor tries to read it. Instead, the Owned state allows a processor to supply the modified data directly to the other processor.** <span style="color:green">This is beneficial when the communication latency and bandwidth between two CPUs is significantly better than to main memory. </span> An example would be multi-core CPUs with per-core L2 caches.

## States

- Modified
  - This cache has the **ONLY** valid copy of the cache line, and has made changes to that copy.

- Owned
  - This cache is one of several with a valid copy of the cache line, but has the **exclusive right to make changes to it**—other caches may read but not write the cache line. - - 
  - When this cache changes data on the cache line, it must broadcast those changes to all other caches sharing the line. The introduction of the Owned state allows dirty sharing of data, i.e., *a modified cache block can be moved around various caches WITHOUT updating main memory.* 
  - The cache line may be changed to the Modified state after invalidating all shared copies, or changed to the Shared state by [writing the modifications back](https://en.wikipedia.org/wiki/Write-back) to main memory. 
  - Owned cache lines must respond to a [snoop](https://en.wikipedia.org/wiki/Snoopy_cache) request with data.

- Exclusive
  - This cache has the **ONLY** copy of the line, but the line is clean (unmodified).

- Shared
  - This line is one of several copies in the system. 
  - This cache does NOT have permission to modify the copy (another cache can be in the "owned" state). Other processors in the system may hold copies of the data in the Shared state, as well. 
  - Unlike the MESI protocol, a shared cache line *may* be dirty with respect to memory; 
    - if it is, some cache has a copy in the Owned state, and that cache is responsible for eventually updating main memory. 
    - If no cache hold the line in the Owned state, the memory copy is up to date. The cache line may not be written, but may be changed to the Exclusive or Modified state after invalidating all shared copies. (If the cache line was Owned before, the invalidate response will indicate this, and the state will become Modified, so the obligation to eventually write the data back to memory is not forgotten.) It may also be discarded (changed to the Invalid state) at any time. 
    - Shared cache lines may not respond to a snoop request with data.

- Invalid
  - This block is NOT valid; it must be fetched to satisfy any attempted access.

### State Diagram

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2020-07-31%2011.54.26.png" alt="截屏2020-07-31 11.54.26" style="zoom:80%;" />

- **Invalidate**

  Send "Invalid"-singal to other processors and tell them: "Hey, I have changed the data. Your data is out-of-date and thus invalid"

- **Retry**

  Send "Retry"-signal and write data back to main memory, before other processors read this data. 

  In other words, O $\to$ I:

  1. Write cahce line back to main memory
  2. Remove this cache line

- **Shared**

  Send "Shared"-signal to other processors and tell them they don't have this data exclusively

  

### Active CPU

![img](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/500px-MOESI-Zustandsdiagramm_für_aktive_CPUs.png)

### Passive CPU

![img](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/500px-MOESI-Zustandsdiagramm_für_passive_CPUs.png)





## Example

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2020-07-31%2012.04.44.png" alt="截屏2020-07-31 12.04.44" style="zoom:67%;" />