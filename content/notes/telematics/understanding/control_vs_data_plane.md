---
linktitle: ''
summary: ''
weight: 204
title: Control Plane Vs. Data Plane
date: 2021-03-12
draft: false
type: book
authors:
- admin
tags:
- Telematics
- Understanding
categories:
- Telematics
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

Abstract view on an IP router

![截屏2021-03-12 10.22.31](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-12 10.22.31.png)

## Control Plane

**Determines/controls how data packets are forwarded** — meaning how data is sent from one place to another.

- Responsible for 

  - Creating a routing table
  - populating the routing table
  - drawing network topology forwarding table and hence enabling the data plane functions

  $\rightarrow$ Here the router makes its decision

- Routers use various [protocols](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) to identify network paths, and they store these paths in routing tables.

## Data Plane / Forwarding Plane

- In contrast to the control plane, which determines how packets should be forwarded, **the data plane actually forwards the packets.**

- Data plane packet goes through the router and incoming and outgoing of frames are done based on control plane logic.

## Summary

Think of the control plane as being like the stoplights that operate at the intersections of a city. Meanwhile, the data plane (or the forwarding plane) is more like the cars that drive on the roads, stop at the intersections, and obey the stoplights.

## Reference

- [What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)

- [Difference between Control Plane and Data Plane](https://www.geeksforgeeks.org/difference-between-control-plane-and-data-plane/)