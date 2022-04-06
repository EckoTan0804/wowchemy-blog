---
linktitle: ''
summary: ''
weight: 103
title: Internet Routing
date: 2021-03-04
draft: false
type: book
authors:
- admin
tags:
- Telematics
- Lecture Notes
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

{{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/Internet_Routing.png" caption="Summary" numbered="true" >}}

## Baiscs

Internet: network of networks

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2013.02.45.png" alt="截屏2021-03-04 13.02.45" style="zoom:67%;" />



### High-level View on an IP Router

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2013.03.49.png" alt="截屏2021-03-04 13.03.49" style="zoom: 67%;" />

- **Control Plane**
  - Routing protocols

  - Exchange of routing messages for calculation of routes

- **Data Plane**
  - Lookup

  - Forwarding of packets at layer 3

- **Routing table**
  - Generated by routing protocol
  - Entries: Mapping of destination IP prefixes to next hop (IP address)
  - Optimized for the particular routing algorithm
  - Performance is not critical 
    - Implemented in software

- **Forwarding table**
  - Used for packet forwarding
  - Entries: Mapping of IP prefixes to outgoing ports (interface ID and MAC address)
  - Optimized for longest prefix matching
  - Performance is critical (lookup in line speed)!
    - Partially uses dedicated hardware

- **Routing metric** (also named **cost**, **weight**)
  - Metric used by a router to make routing decision

  - Can be applied to an individual link or to the overall path
  - *Examples*
    - *Utilization, latency, data rate* 
    - *Number of hops*

- **Routing policy**
  - Policy-based routing decisions
  - Policies are defined by network operator / owner

### Distributed Adaptive Routing

- Currently most commonly used in the Internet
- An instance of the routing protocol **in each router** 
  - Exchange of routing information via routing messages
- Adaptation of the paths to the current situation in the network

![截屏2021-03-04 14.29.56](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2014.29.56.png)

### Path computation

Network is modeled as **graph**
$$
G = (N, E)
$$

- $N$: nodes (routers)
- $E$: edges
  - Links between routers are edges 
  - Edges are associated with metric

Example

![截屏2021-03-04 14.31.28](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2014.31.28.png)



## Autonomous Systems

### Structuring into autonomous systems

Internet routing can be divided into **Autonomous Systems (AS)**

- Routing **inside** an autonomous system using **Interior Gateway Protocol (IGP)**
- Routing between autonomous systems using **Exterior Gateway Protocol (EGP)**

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2014.42.27.png" alt="截屏2021-03-04 14.42.27" style="zoom: 67%;" />

#### Autonomous Systems

- Identification: Unique number called **Autonomous Systems Number (ASN)**
  - earlier 16 bit; now 32 bit
- Properties
  - Appears as a single entity to the outside
  - Uniform routing policy
  - Typically uniform interior routing protocol
    - Different ASes can use different interior routing protocols
- 👍 Advantages
  - Separated administrative domains
  - Scalability by using two logical levels
    - Routing protocol inside an AS (not global) 
    - Routing protocol between ASes

- **Important Properties**
  - Scalability of routing protocols
    - Overhead increases with size of the network 📈
      - Space for storing routing information
      - Number of routing messages to exchange 
      - Computation overhead
  - Operator autonomy
    - Choice of interior routing protocol 
    - Hiding of internal network structure

- Allocation
  - IANA (Internet Assigned Numbers Authority) delegates allocation to **Regional Internet Registries (RIR)**, e.g.,
    - ARIN (North America)

    - RIPE NCC (Europe, Middle East and Central Asia) APNIC (Asia-Pacific)

    - LACNIC (Latin America, Caribbean)

    - AfriNIC (Africa)

#### Subdivision into ASs

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2014.53.42.png" alt="截屏2021-03-04 14.53.42" style="zoom: 67%;" />

#### Classification of ASes

- Classification based on **role**
  - **Stub AS**
    - Small organizations and enterprises (Mostly operate only regionally) 
    - Connected to exactly one provider
    - No transit traffic
  - **Multihomed AS**
    - Large enterprises

    - Connected to several providers (reliability) 
    - No transit traffic
  - **Transit AS**
    - Provider (Often global scope)

- Classification based on **“economic position/influence”**

  - Tier 1, tier 2, tier 3 ...

  ![截屏2021-03-04 14.57.26](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2014.57.26.png)

#### Different Roles

- **End customer**
  - Uses Internet application
  - Examples
    - Universities
    - Enterprises
    - Customers of Internet Service Providers (ISP)
- [**Content delivery provider**](#content-delivery-provider)
  - Requested by end customers / Internet application 
    - Provide content
  - Examples: Google, Akamai, Yahoo, YouTube, Facebook...

### Reachability across autonomous systems

#### Reachability

Main problem

- How to ensure mutual reachability? 
- Cooperation among autonomous systems?

Basic concepts

- [**Transit**](#connectivity-and-transit): Purchased connectivity 💸
- [**Peering**](#peering): Direct connection, typically between ASes of the same tier

#### Connectivity and Transit

- Establish connectivity
  - Establish paths to all other ASes in the Internet

  - AS operator purchases connectivity from one or more ASes

- **Transit**

  > **Internet transit** is the service of allowing network traffic to cross or "transit" a computer network, usually used to connect a smaller [Internet service provider](https://en.wikipedia.org/wiki/Internet_service_provider) (ISP) to the larger [Internet](https://en.wikipedia.org/wiki/Internet). ([wiki](https://en.wikipedia.org/wiki/Internet_transit))

  - Purchased connectivity 💸
    - Upstream: provider (seller) of transit 
    - Downstream: customer (buyer)
  - Traffic exchange
    - In both directions

    - **Only downstream AS must pay**; usually volume rate

  - Transit AS: Provider AS that offers transit

- Options for connecting a stub AS

  - Stub AS

    ![截屏2021-03-04 15.23.16](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2015.23.16.png)

  - Dualhomed stub AS

    ![截屏2021-03-04 15.23.52](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2015.23.52.png)

  - Multihomed stub AS

    ![截屏2021-03-04 15.24.16](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2015.24.16.png)

#### Peering

- **Private peering**

  - Direct connection between two ASes, usually of same tier

  - No cost for traffic exchange; costs for network infrastructure apply

  - However

    - Mostly **only data traffic between privately peered ASes** 
    - NO transit traffic of other ASes

  - Video explanation

    {{< youtube T2jb1tzXzMw>}}

  - Example: peering and transit combination

    <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2015.34.37.png" alt="截屏2021-03-04 15.34.37" style="zoom:80%;" />

  - 👍 Advantages
    - Benefits both ASes: save transit costs, that otherwise would apply 
    - Shorter data paths: fewer AS hops between source and destination
  - 🔴 Problems
    - Direct connection of ASes complicated (Different geographical locations)
    - Full mesh of $n$ ASes ($\frac{(n-1)n}{2}$ separate connections!)

- **Public peering**

  - Through **Internet exchange points (IXPs)**

    - Central public authority for interconnection

    <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2015.59.13.png" alt="截屏2021-03-04 15.59.13" style="zoom:67%;" />
    - Neutral traffic forwarding on layer 2
    - No differentiation regardless of customer, content, or type of service
    - Examples
      - DECIX (the world’s biggest IXP)

  - Members / customers: Monthly fixed charges per network port
  
- Necessary for operation and maintenance of IXP‘s switching platform
  
  - Different peering policies
    - **Open**: AS is open for peering with all other ASes
    - **Selective**: Peering only under given terms and conditions
    - **Restrictive**: AS does not engage in new peering relationships
    - **No Peering**: AS does not do any peering

#### Autonomous Systems and Transit/Peering

- **Tier 1**
  - Large global ASes with access to (all) other ASes
    - Do not buy any transit. Sell transit
    - Peering with other tier 1 ASes
  - *Examples: Deutsche Telekom, AT&T...*
- **Tier 2**
  - Big national and inter-regional ASes
    - Connection to providers of Internet applications
  - Downstream of tier 1 ASes
    - Sell transit to other ASes 
    - Usually employ peering
  - *Examples: Vodafone, Comcast, Tele2*

- **Tier 3**
  - Small mostly regional ASes
    - Connections with small providers of Internet applications
  - Downstream of tier 2 providers
    - Usually do not sell transit to other ASes 
    - Sell transit mostly to end customers/users 
    - Usually employ peering
  - *Examples: KabelBW, NETHINKS, Alice*

#### Content Delivery Provider

- **🎯 Goal: FAST delivery of content (i.e. low latencies)**

  $\rightarrow$ Locations close to tier 1 peering points are preferred

- Two basic alternatives
  - Web servers are hosted **directly in tier 1 ASes** (Does not require an own AS number)
  - Web servers are connected over own routers
    - [**Content delivery network (CDN)**](#content-delivery-network)
    - Own AS number required

    - Peering with essential providers at important peering points 
    - *Examples: Google, Yahoo, Akamai*

#### Content Delivery Network

- World wide network with own AS number

  - Thousands of **Points of Presence (PoP)** spread across the world

- Point of Presence

  - Consists of access routers und core routers 
    - Access router at the edge of a CDN

    - Core router inside a CDN

  - Customers are connecting through access routers

- Objectives
  - Load balancing at access routers
  - Be close to customers $\rightarrow$ low latencies

### Routing in and between Autonomous Systems

Classification

- **Interior gateway protocols (IGPs)** *INSIDE* one AS
  - A.k.a **intra-domain routing protocols**
  - Are encapsulated inside an AS, i.e., not visible to the outside 
  - Different IGPs in different ASes possible

  - Metric-based
- **Exterior gateway protocols (EGPs)** *BETWEEN* ASes 
  - Also named **inter-domain routing protocols**

  - Single protocol between *all* ASes

  - Policy-based

![截屏2021-03-04 16.48.23](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2016.48.23.png)

## RIP: Routing Information Protocol 

- **Interior** gateway protocol
- Very simple protocol that requires very little configuration

### RIP in the Protocol Stack

- Application process routed implements RIP and manages forwarding table
- RIP routing messages are sent over UDP $\rightarrow$ NOT reliable

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2023.16.57.png" alt="截屏2021-03-04 23.16.57" style="zoom:80%;" />

### Routing Metric

- **Distance between source and destination = number of hops on the path (hop count)**

- Hop count

  - Refer to the number of intermediate devices through which data must pass between source and destination.

    - Each time that a packet of data moves from one router (or device) to another, that is considered one HOP.

    {{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/Hop-count-trans-20210304235011333.png" caption="An illustration of hops in a wired network. The hop count between the computers in this case is 2." numbered="true" >}}

  - Limited range of values: 1 - 15 

  - Value of 16 corresponds to "infinity"

### RIP Routing Messages

- RIP protocol entities exchange routing messages 
  - UDP is used as transport protocol
- Types of routing messages
  - **Request** message
    - Requires complete routing table or part of it
  - **Response** message for different reasons
    - Response to specific query
    - Regular update
    - Triggered update

### Routing Updates

#### Outgoing

- Regular routing update
  - Periodically, every 30 seconds
  - Sends entire routing table to all its neighbors
  - Entries in the routing table are periodically refreshed
  - No refresh for at least 180 seconds? $\rightarrow$ Hop-Count is set to 16 („infinite“), corresponding route is invalidated
- Metric for route changes (*triggered* update)
  - Only changes since the last update are communicated, not the complete routing table
  - Rate limitation in order to reduce load on the network

#### Incoming

- Entry for a destination address does not exist in routing table and received metric is not „infinite“ $\rightarrow$ **Insert** new entry in routing table

- Current entry for a destination address in routing table has larger metric **or** routing update was sent by the “next router” for this destination $\rightarrow$ **Modify** entry

- Otherwise $\rightarrow$ **Ignore** routing update

#### Example

Scenario

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2023.42.49.png" alt="截屏2021-03-04 23.42.49" style="zoom:80%;" />

- Connecting lines represent either direct links or LANs between routers
- Ovals represent routers

We have the routing table of router D

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2023.44.02.png" alt="截屏2021-03-04 23.44.02" style="zoom:80%;" />

30 seconds later D receives new routing update from Router A

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-04%2023.44.38.png" alt="截屏2021-03-04 23.44.38" style="zoom:80%;" />

- A tells D: "Hey, now I can reach Z through 4 hops".
- I.e., now D can reach Z through $4+1=5$ hops

As 5 < 7 (the old number of hops to reach Z), D updates its routing table:

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-05%2000.03.37.png" alt="截屏2021-03-05 00.03.37" style="zoom:80%;" />

## OSPF: Open Shortest Path First 

### OSPF Basics

- **Interior** gateway protocol

- **Link state** protocol

  - Each router in the network needs to learn complete *topology* of the network (Otherwise, calculated paths are inconsistent)
    - Topology = Nodes and links with their costs (weights)

  - Each router separately computes shortest paths based on network topology
    - Dijkstra shortest path algorithm

#### OSPF in the Protocol Stack

OSPF is located on top of IP $\rightarrow$  OSPF uses an *unreliable* communication service

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-07%2011.51.52.png" alt="截屏2021-03-07 11.51.52" style="zoom:80%;" />

#### Know the Neighbors

Each router 

- learns its neighbors and 
- monitors the state of the links to them

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-07%2011.56.39.png" alt="截屏2021-03-07 11.56.39" style="zoom:80%;" />

#### Link States of a Router

- **Router ID of neighbors**: dynamically discovered by hello protocol

- Availability: dynamically discovered by hello protocol or physical layer
- Everything else is configured

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-07%2012.03.17.png" alt="截屏2021-03-07 12.03.17" style="zoom:80%;" />

#### Pre-Configuration of OSPF Router

Each router is **pre-configured** with the following parameters

- **Router ID**: unique ID of a router in the network

- **Per-interface parameters**
  - Interface IP address (and mask)
  - Interface output cost – metric
    - Typically, *inversely proportional* to link data rate

#### Routing Metric

Each link is associated with **link costs**

Example: prefer links with higher data rate
$$
\text { Cost }=\frac{\text { Reference Data Rate }}{\text { Interface Data Rate }}
$$

- $\text{Reference Data Rate}$ can be configured
  - E.g., to 1 $𝐺𝑏𝑖𝑡/𝑠$ or 10 $𝐺𝑏𝑖𝑡/𝑠$
  - Should be consistent across all routers in network

#### Link State Advertisement (LSA)

Each router constructs router **link state advertisements (LSAs)**

- Router LSAs consist of information about its neighbors and links
- Example

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-07%2012.19.30.png" alt="截屏2021-03-07 12.19.30" style="zoom:80%;" />

Router floods its LSA on *all* its interfaces $\rightarrow$ All routers in the network must receive an identical copy of this LSA

![截屏2021-03-07 12.47.21](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-07%2012.47.21.png)

#### Link State Database

- Each router maintains a link state database

  - Stores most recent LSAs from all other routers in the network

  ![截屏2021-03-07 12.48.45](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-07%2012.48.45.png)

- Link state database is used to
  - Construct topology graph of the network  
  - Calculate routing table

{{% callout note %}} 

Routers have identical knowledge of network topology iff their link state databases are **synchronized**, i.e., they have identical content at all routers.

{{% /callout %}}

- Initial Synchronization of link state database

  - **(Re-)start** of a router

    New router has an empty link state database

  - Initial database synchronization

    - Router asks neighboring router to share its database Performed 
    - immediately after a “handshake” of the hello protocol 
    - Routers exchange LSA headers with each other

    - If an LSA is missing it is requested from the neighbor router

    $\rightarrow$ the routers are now considered as adjacent to each other

### Link State Advertisement

Example

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-07%2013.02.37.png" alt="截屏2021-03-07 13.02.37" style="zoom:80%;" />

Each LSA is associated with a lifetime (**LS `Age`**)

- Set to “0” by advertising router
  - When flooded, incremented by transmission delay (estimated value) 
  - As LSA is stored in database, Age is **incremented over time**

- When LSA’s age reaches **`MaxAge`**, LSA is considered **out-of-date** 
  - `MaxAge `is set to 1 hour

- Consequence: routers must refresh their LSAs every `LSRefreshTime`
  - `LSRefreshTime `is set to 30 minutes
  - Minimum value between generation of any particular LSA: 5 seconds

### Hello Protocol

- 🎯 Goals
  - Ensure bi-directional communication between neighboring OSPF routers 
  - Establish and maintain logical adjacencies

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-07%2013.06.50.png" alt="截屏2021-03-07 13.06.50" style="zoom:80%;" />

- Determines identity and liveliness of neighboring routers

#### Hello Message

- Contains own `router ID`
- Contains `router ID` of neighboring router, if known
  - If not yet known $\rightarrow$ `router ID` is set to `0.0.0.0`
  - If own `router ID` is contained in neighbor's hello message $\rightarrow$ Communication is considered to be **bi-directional**

- Destination IP address of hello message: `224.0.0.5` (multicast address, “`AllSPFRouters`”)

  $\rightarrow$  hello message is received and processed only by OSPF routers

#### Simplified Workflow

- A router **periodically** sends a hello message on all its links 

  - *“Hello, I am R1, I am still here”*
  - If known, hello message contains `router ID` of neighboring router 
    - *“my neighbor on this link is R2”*

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-09%2011.40.56.png" alt="截屏2021-03-09 11.40.56" style="zoom:80%;" />

- If no hello message is received for a pre-defined period of time $\rightarrow$ the link is considered to be down 🤪
  - Standard value for periodic hello messages: every 10-30 seconds 
  - Fast hello extension: < 1 second

### OSPF Message

#### **Header** of OSPF messages

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-07 13.27.37.png" alt="截屏2021-03-07 13.27.37" style="zoom:67%;" />

- **Version**: OSPF Version, currently 2 for IPv4 and 3 for IPv6
- **Type**
  - Hello
  - database description
  - link state request
  - link state update
  - link state acknowledgement
- **Router ID**: ID of originating router
- **Area ID**: OSPF area
- **Checksum**: Internet checksum over entire OSPF message
- **AUType and Authentication**: Optional authentication of originating router

#### Link State Update Message

Structure of a Link State Advertisement

- Consists of a **header** and a **body**
- **LSA header**: contains information used to uniquely identify the LSA
  - Advertising router
  - Sequence number of LSA at advertising router 
  - ...
- **LSA body**: contains information of all operational links of the router
  - Associated cost
  - Type of link
  - Reachability information
  - ...

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-07%2013.32.39.png" alt="截屏2021-03-07 13.32.39" style="zoom:67%;" />

LSA Header

- **LS Age**

  Time in seconds since LSA was originated

- **Options**
   Optional capabilities supported by OSPF domain

- **LS Type**
   Router LSA, network LSA ...

- **Link State ID**
   Uniquely identifies an LSA

- **Advertising Router**
   OSPF router ID of originating router

- **LS Sequence Number**
   Incremented each time a new LSA is generated

- **Checksum**
   Over entire message exept age field

- **Length**
   \#bytes for entire LSA including header

### Coping with Dynamic Changes

#### Issuing LSAs

- If nothing changes (link, router), nothing needs to be reported with respect to routing $\rightarrow$ **keep quiet**
  - LSAs are refreshed every 30 minutes
- Besides periodic refreshes, communication is only needed in case of changes
  - Interface changed to up or down 
  - Neighboring router on link is unreachable 
  - Configuration changes
- Minimum time between two consecutive LSAs of a router is set to 5 seconds (Due to stability reasons) 

#### Synchronized Link State Databases

🎯 Goal: link state databases of all routers need to have **identical** content (need to be **synchronized**)

Following actions are needed

- Ensure that each LSA is received by every router in the network (**[reliable flooding](#reliable-flooding)**)
- Ensure that all routers consistently either store or discard each LSA $\rightarrow$ fully deterministic comparison rules
- Ensure that expired LSAs are deleted from link state databases of every router

#### Reliable Flooding

- Reception of each LSA is **acknowledged** by neighboring router

  - Hop-by-hop acknowledgements

  ![截屏2021-03-07 14.32.37](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-07%2014.32.37.png)

- Router **R** stores received LSA

  - If R **does not have** an LSA from the advertising router

  - If the received LSA is **newer** than the one in the database

    ```python
    def is_new_LSA(received_LSA, cur_stored_LSA, MAX_AGE=60):
        if received_LSA.sequence_Nr > cur_stored_LSA.sequence_Nr:
            return True
        elif received_LSA.sequence_Nr == cur_stored_LSA.sequence_Nr:
            if received_LSA.checksum > cur_stored_LSA.checksum or 
               cur_stored_LSA.age == MAX_AGE or 
               received_LSA.age < cur_stored_LSA.age: 
                return True
        else:
        	return False
            
    ```

    

- If R stores the LSA, it forwards it to its neighbors 
  
  - Uses multicast address `224.0.0.5` with hop limit of 1

#### LSA Flooding Example

Router R receives LSA from advertising router R1

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-07%2014.47.58.png" alt="截屏2021-03-07 14.47.58" style="zoom:80%;" />

- if `received_LSA.age == MAX_AGE` **and** no LSA from R1 is known

  $\rightarrow$ Send ACK and discard

- If there is no LSA from R1 in database **or** received LSA is newer $\rightarrow$
  - Store/replace LSA
  - Send ACK

  - Update Age and flood LSA to neighbors

- If already stored copy is newer

  $\rightarrow$ Send stored copy back to advertising router R1

- If LSA and stored copy are the same

  $\rightarrow$ Discard LSA

Re-compute routes if content of link state database changed

### OSPF Areas

- Basic situation: Autonomous systems can grow rather large

- Scalability problem

  - LSA flooding and
  - Route computation overhead

  $\rightarrow$ do NOT scale 🤪

- 🔧 Solution: Divide an AS into **areas** (i.e., introduce additional level of hierarchy)
  - Apply routing only within an area 
    - LSA flooding and route computation limited to an area
    - Only routers within the same area have identical link state databases.
  - Areas exchange summary information with each other
    - Addresses reachable from these areas
  - Typical size of an area: <100 routers

### OSPF Areas structure

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-08%2016.47.53.png" alt="截屏2021-03-08 16.47.53" style="zoom:80%;" />

- Two levels of hierarchy
  - **Area 0** – **backbone** of the autonomous system Backbone must be always connected
  - All other areas are directly connected to backbone
- **Area border routers (ABRs)** interconnect areas
  - They belong to both: their area and the backbone

  - They run an instance of OSPF for each area they are connected to
  - They generate summary LSAs
    - Contain ABR’s routing table for corresponding area
      - List of destinations reachable within the area 
      - Associated with path cost from the ABR to destination
    - ABR ́s routing table is constructed after intra-area path computation
  - Handle summary LSAs: Same way as “regular” LSAs
    - ABR forward summary LSAs of an area into backbone 
    - ABR forward summary LSAs from backbone into the area

### Inter-Area Forwarding

- Data between areas are forwarded through backbone (area 0)
- End-to-end path consists of **path segments**
  - Segment between source and ABR of originating area 
  - Segment between two ABRs in area 0, and

  - Segment between ABR of target area and destination
- Routers within an area select ABRs so that resulting end-to-end path is a **shortest** path
  
- Based on path costs of ABRs
  
- Example

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-08%2017.02.09.png" alt="截屏2021-03-08 17.02.09" style="zoom:80%;" />

![截屏2021-03-08 17.02.36](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-08%2017.02.36.png)

### RIP vs. OSPF

**RIP**: based on distance vector

- 🔴 Problems
  - Limited in metric selection and size  
    - Only one metric (hop count)

    - Maximum path length of 15 hops
  - Periodic updates every 30 seconds, even without changes
  - Slow convergence, count-to-infinity $\rightarrow$ Not suitable for large networks 🤪

- 👍 Advantage: easier and requires less resources than OSPF 
  - Still sometimes used in small networks

**OSPF**: based on link-state

- Addresses shortcomings of RIP
  - Faster convergence, no count-to-infinity, lower signaling overhead ... 👏
- Large networks can be divided into areas 
- Standard in large ASes (together with IS-IS)

## BGP: Border Gateway Protocol

> Good explanation:
>
> - [BGP for Humans: Making Sense of Border Gateway Protocol](https://www.imperva.com/blog/bgp-routing-explained/)

### Exterior Gateway Protocols

In aforementioned section, we have devided a large networks into different autonomous systems (ASes). In order to make autonomous systems to be able to communicate with each other, there should be at least one special intermediate system that serves as an **interface to other ASes**.

👍 Advantages:

- **Scalability**
  - Size of routing tables depends on size of AS

  - Changes in routing tables are only propagated within an AS
- **Autonomy**
  - Internet = network of networks
  - Routing can be controlled in the own network
    - Uniform interior routing protocol within the AS

    - Interior routing protocols of different ASes do not have to be identical

### Border Gateway Protocol

- The most important **exterior** gateway protocol
- **Path vector** protocol
  - Extension of distance vector approach
  - BGP distributed **paths**, not metrics like costs etc. 
    - With paths it is easy to guarantee that no loops exist
  - Based on policies of network operator

### BGP in a Nutshell

- What exactly is being distributed?
  - **Paths** (also called **routes**) that consist of
    - Target: **prefixes** (also called: network, network prefixes, IP address ranges)
    - Attributes: path, next hop
      - Each traversed AS adds its own AS number to the path

- Traffic "follows" UPDATE messages in opposite direction

  ![截屏2021-03-08 22.01.15](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-08%2022.01.15.png)



<details>
<summary><b>Example: HW07</b></summary>
<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-09%2022.53.41.png" alt="截屏2021-03-09 22.53.41" style="zoom:67%;" />

AS 100 announces prefix `1.6.17.0/24`. Describe how the routing information is distributed in the network.

![截屏2021-03-09 22.54.30](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-09%2022.54.30.png)

![截屏2021-03-09 22.54.41](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-09%2022.54.41.png)

![截屏2021-03-09 22.54.58](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-09%2022.54.58.png)



![截屏2021-03-09 22.55.12](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-09%2022.55.12.png)

![截屏2021-03-09 22.55.45](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-09%2022.55.45.png)



![截屏2021-03-09 22.55.57](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-09%2022.55.57.png)

![截屏2021-03-09 22.56.15](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-09%2022.56.15.png)

![截屏2021-03-09 22.58.43](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-09%2022.58.43.png)

![截屏2021-03-09 22.59.08](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-09%2022.59.08.png)

The other two UPDATE messages (sent from R1 to R31 and R21) are handled in a similar way.
</details>





























### BGP Structure

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-08%2022.02.02.png" alt="截屏2021-03-08 22.02.02" style="zoom:80%;" />

- **External BGP (EBGP)**
  - Spoken between BGP routers of **neighboring** ASes 
  - Announcement and forwarding of path information 
  - Internal details of AS are NOT exchanged

- **Internal BGP (IBGP)**
  - Between BGP routers **within** an AS
  - Synchronization of BGP routers of an AS
  - Establishment of transit routes

### Categorization of Routing Protocols

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-08%2022.05.46.png" alt="截屏2021-03-08 22.05.46" style="zoom: 67%;" />

### Interplay of the Routing Approaches

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-08%2022.07.37.png" alt="截屏2021-03-08 22.07.37" style="zoom:80%;" />

### Routing with BGP and IGPs

![截屏2021-03-08 22.09.40](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-08%2022.09.40.png)

Assume Alice wants to sent a packet to an external target ( not part of the local IGP domain, e.g., `2.3.4.5`).

How does IGP router know what to do with this packet?

- Is not strictly prescribed by BGP

- Network operators can configure this freely
- Different approaches possible

#### Approach 1: IGP distributes "default" routes

- Unknown address/prefix packets are routed to **default BGP** router via shortest path
  - Good option for stub ASes
  - Not practicable for transit ASes

- Example

  ![截屏2021-03-08 22.14.45](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-08%2022.14.45.png)

#### Approach 2: Publication of external routes via IGP

- Allows more fine-grained control such as *„all Google traffic goes this way“* 

- Cannot be done with all external routes (scalability!)

- Usually combined with default route

- Example

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-09%2014.59.38.png" alt="截屏2021-03-09 14.59.38" style="zoom:80%;" />

#### Approach 3: IGP router also speaks BGP

- Forwarding table is build from two routing tables (BGP + IGP) 

- Often the case with big backbone providers

- Example

  ![截屏2021-03-08 22.25.22](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-08%2022.25.22.png)

### BGP-Sessions

- **Point-to-point**

  ![截屏2021-03-08 22.33.53](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-08%2022.33.53.png)

  - Usually only between **directly connected routers**
    - Neighbors are called "**peers**"
    - BGP uses TCP connections between these routers

- How to establish TCP connection without working IP routing?

  - IBGP: IGP of AS can be used
  - EBGP
    - Usually direct physical connection $\rightarrow$ no routing required 
    - Manual configuration at both ends of connection

### IBGP Connections

- Simplest case: all BGP routers are fully meshed and connected directly to each other
  - BGP sessions must be kept active all the time 
  - Bad scalability 👎

- Alternative: Concentrate IBGP traffic in a single router 
  - Called **route reflector**
  - Only route reflector has to maintain sessions with everyone else
  - More than one reflector used in practice for reliability reasons
- Alternative: Form hierarchies of sub ASes
  - Called **AS confederations**

  - Can also be used to implement more complex policies 
  - Confederation appears to outside as single AS

### BGP Messages

- **OPEN**

  - Establishment of BGP connection to peer BGP router 
    - Important: TCP connection must already exist!

  - Authentication

- **UPDATE**

  - Announcement of new or withdrawal of outdated path
  - Attention: Only sent if new, better paths available

- **KEEPALIVE**
  - Keeps connection alive in absence of UDPATE messages 
  - Acknowledgment for an OPEN request

  - Recommended KeepAliveTimer: 30 s

- **NOTIFICATION**
  - Error message and tear down of BGP connection

### Routing Information Base

- BGP provides mechanisms for distributing path information
  - Does NOT dictate how routes should be chosen
  - No predefined routing metric
- BGP uses **policies**

- BGP instance of a router collects received and dispatched routing information in various internal tables
  - **Routing Information Base (RIB)**
  - Mainly for logical structuring

- Structure

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-08%2022.48.36.png" alt="截屏2021-03-08 22.48.36" style="zoom:80%;" />

  - **Adj-RIB-In (Adjacency RIB Incoming)**

    - Exists per peer
    - Stores information received from this peer

  - **Loc-RIB (Local RIB, Routing Information Base)**

    - „Actual routing table“
      - Only p**referred (= best=shortest)** routes to destination networks are included here 
      - Forwarding Information Base (FIB) is build based on Loc-RIB

  - **Adj-RIB-Out (Adjacency RIB Outgoing)** 

    - Exists per peer
- Contains routes published to this peer

<details>
<summary><b>Routing Table example: HW08</b></summary>

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-09%2022.53.41.png" alt="截屏2021-03-09 22.53.41" style="zoom:67%;" />

AS 100 announces prefix `1.6.17.0/24`. Fill out the simplified routing table of R5

![截屏2021-03-10 11.02.53](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-10%2011.02.53.png)

![截屏2021-03-10 11.02.56](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-10%2011.02.56.png)

![截屏2021-03-10 11.03.24](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-10%2011.03.24.png)

![截屏2021-03-10 11.03.43](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-10%2011.03.43.png)

![截屏2021-03-10 11.04.07](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-10%2011.04.07.png)

![截屏2021-03-10 11.04.27](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-03-10%2011.04.27.png)
</details>





















### 🔴 Challenges

BGP "struggles" with many challenges and problems, e.g., 

- Maintaining scalability

- Security problems