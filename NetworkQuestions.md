# Network Engineer Interview Questions & Answers

This document contains sample interview questions and answers covering network fundamentals, technical knowledge, and problem-solving skills. It can be used as part of a GitHub portfolio or study reference.

## Network Fundamentals

### What is a network?
A network is a collection of interconnected devices such as computers, servers, routers, and switches that communicate with each other to share data and resources. Networks allow systems to exchange information using standardized protocols like TCP/IP.

### What is a router?
A router is a networking device that forwards data packets between different networks. It operates at **Layer 3 (Network Layer)** of the OSI model and uses IP addresses to determine the best path for traffic to travel between networks.

Routers are commonly used to connect local networks to other networks, such as connecting a home or corporate LAN to the internet.

### Can you define the OSI model?
The **OSI (Open Systems Interconnection) model** is a conceptual framework used to understand how different networking protocols interact and communicate across a network.

It consists of **7 layers**:

1. **Physical** – Transmission of raw bits over physical media  
2. **Data Link** – Handles MAC addressing and frame transmission  
3. **Network** – Responsible for logical addressing and routing (IP)  
4. **Transport** – Ensures reliable data delivery (TCP/UDP)  
5. **Session** – Manages communication sessions between applications  
6. **Presentation** – Handles data formatting and encryption  
7. **Application** – Provides network services to applications (HTTP, FTP, DNS)

The OSI model helps engineers troubleshoot and design network systems.

### What is the difference between a switch and a router?

| Switch | Router |
|--------|--------|
| Operates at **Layer 2 (Data Link)** | Operates at **Layer 3 (Network)** |
| Uses **MAC addresses** | Uses **IP addresses** |
| Connects devices within the same network | Connects different networks together |
| Handles LAN traffic | Routes traffic between LANs and WANs |

Switches improve internal network efficiency, while routers allow communication between separate networks.

## Technical Knowledge

### What is a subnet?
A subnet (subnetwork) is a logical subdivision of an IP network that helps organize and manage network traffic more efficiently.

Subnetting allows administrators to:
- Divide large networks into smaller segments
- Improve network performance
- Enhance security
- Reduce broadcast traffic

Example:

```text
192.168.1.0/24
```

This network can be divided into smaller subnets such as:

```text
192.168.1.0/26
192.168.1.64/26
192.168.1.128/26
192.168.1.192/26
```

### How does DNS work?
DNS (Domain Name System) translates human-readable domain names into IP addresses.

Example:

```text
google.com -> 142.250.72.14
```

The process works as follows:

1. A user enters a domain name into a browser.
2. The request is sent to a **DNS resolver**.
3. If the resolver does not have the record cached, it queries:
   - Root DNS servers
   - Top Level Domain (TLD) servers
   - Authoritative DNS servers
4. The correct IP address is returned to the client.
5. The browser connects to the server using the IP address.

DNS acts like the **phonebook of the internet**.

### What are common software problems that can cause network defects?
Common issues include:

- Outdated network drivers
- Misconfigured IP settings
- Incorrect DNS configuration
- Firewall blocking network traffic
- Software bugs or corrupted updates
- Incorrect routing tables
- Application conflicts

These problems can cause connectivity issues, slow performance, or complete network failure.

### Can you explain what a LAN and WAN are?

**LAN (Local Area Network)**  
A LAN connects devices within a small geographic area such as a home, office, or campus. LANs typically use Ethernet or Wi-Fi and offer high speeds.

**Example:**  
An office network connecting computers, printers, and servers.

**WAN (Wide Area Network)**  
A WAN connects multiple LANs across large geographic distances using leased lines, fiber, or the internet.

**Example:**  
The Internet itself is the largest WAN.

## Problem Solving & Adaptability

### Describe a time you solved a technical problem
During my cybersecurity and networking studies, I frequently built and troubleshot home lab environments. One example involved configuring a Windows Server domain where client machines were unable to connect to the network.

I identified that the issue was caused by incorrect **DHCP and DNS configuration**. After verifying the IP addressing and ensuring the correct DNS server was assigned to the clients, the machines were able to successfully join the domain and communicate across the network.

This experience reinforced the importance of systematic troubleshooting and understanding how network services interact.

### How do you stay updated with new networking technologies?
I stay current with networking technologies through several methods:

- Building **home lab environments** using tools like Windows Server, virtual machines, and networking software
- Following cybersecurity and networking communities online
- Reading technical documentation and industry blogs
- Practicing with tools related to networking and security
- Continuing to develop personal projects and scripts related to network monitoring and scanning

As someone with a **Master's in Cybersecurity**, I enjoy continuously learning about networking, security, and infrastructure technologies.
