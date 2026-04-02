# Lab08 -

<img width="835" height="579" alt="lab08" src="https://github.com/user-attachments/assets/ae2384f8-e429-4117-95d3-02b3515b5081" />

# IPv4 Addressing Lab

## Objective
This lab practices basic router interface configuration and end-device IP addressing.

## Router Interfaces
| Interface | IP Address       | Subnet Mask       | Network         |
|-----------|------------------|-------------------|-----------------|
| G0/0      | 15.255.255.254   | 255.0.0.0         | 15.0.0.0/8      |
| G0/1      | 182.98.255.254   | 255.255.0.0       | 182.98.0.0/16   |
| G0/2      | 201.191.20.254   | 255.255.255.0     | 201.191.20.0/24 |

## PC Addresses
| PC  | IP Address     | Subnet Mask       | Default Gateway   |
|-----|----------------|-------------------|-------------------|
| PC1 | 15.0.0.1       | 255.0.0.0         | 15.255.255.254    |
| PC2 | 182.98.0.1     | 255.255.0.0       | 182.98.255.254    |
| PC3 | 201.191.20.1   | 255.255.255.0     | 201.191.20.254    |

## Key Commands
```bash
show ip interface brief
show running-config
interface g0/0
ip address 15.255.255.254 255.0.0.0
no shutdown
description LAN to SW1 / PC1
```

---

## What happens in this lab

This lab shows how a router connects multiple different networks and allows devices in those networks to communicate with each other.

R1 has three interfaces, and each interface is connected to a different LAN:

- G0/0 connects to the **15.0.0.0/8** network
- G0/1 connects to the **182.98.0.0/16** network
- G0/2 connects to the **201.191.20.0/24** network

Each router interface is given an IP address in its own network. These IP addresses act as the **default gateways** for the PCs in each LAN.

### Router interface roles
- **G0/0 = 15.255.255.254** → default gateway for PC1's network
- **G0/1 = 182.98.255.254** → default gateway for PC2's network
- **G0/2 = 201.191.20.254** → default gateway for PC3's network

This means:
- PC1 sends traffic for other networks to G0/0
- PC2 sends traffic for other networks to G0/1
- PC3 sends traffic for other networks to G0/2

### How communication works
If a PC wants to communicate with another device in the same network, it can send the traffic directly.

If a PC wants to communicate with a device in a different network, it must send the traffic to its **default gateway**, which is the router interface connected to that LAN.

For example, if **PC1 wants to ping PC2**:
1. PC1 checks the destination IP address
2. PC1 sees that PC2 is in a different network
3. PC1 sends the packet to its default gateway, **15.255.255.254**
4. R1 receives the packet on **G0/0**
5. R1 checks its routing table and sees that the **182.98.0.0/16** network is directly connected to **G0/1**
6. R1 forwards the packet out **G0/1**
7. PC2 receives the packet and sends a reply back through the router

The same process happens for communication between any of the three networks.

### Why the switches are there
The switches are used to connect the PCs to the router interfaces within each LAN.

- SW1 connects PC1 to R1
- SW2 connects PC2 to R1
- SW3 connects PC3 to R1

The switches operate at Layer 2 and forward frames based on MAC addresses inside their local network.

The router operates at Layer 3 and forwards packets between different IP networks.

### Why `no shutdown` is needed
Router interfaces are often administratively down by default. The `no shutdown` command enables the interface so it can send and receive traffic.

Without `no shutdown`, the interface will stay down and the PCs will not be able to communicate through it.

### Why default gateways matter
Each PC must have the correct default gateway configured. Without a default gateway, a PC can only talk to devices in its own local network and will not know where to send traffic for remote networks.

### What this lab is teaching
This lab teaches the basics of:
- assigning IP addresses to router interfaces
- enabling interfaces
- using the router as a default gateway
- understanding directly connected networks
- testing connectivity with pings
- seeing how a router forwards traffic between different networks

### Simple summary
The router acts as the central device that connects three separate IP networks. Each router interface belongs to one network and serves as that network’s gateway. When a PC needs to reach a different network, it sends the traffic to the router, and the router forwards it out the correct interface.
