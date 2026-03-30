# GNS3 LAB 03 - Enterprise Network Setup
<img width="761" height="405" alt="Lab03" src="https://github.com/user-attachments/assets/33a30b36-e6a2-42a0-b2d4-9935a1c7711a" />

## Traffic Flow
PC1 / Ubuntu → Switch1 → R2 → ISP → R3 → Switch3 → PC2

---

## Overview
buidling a multi-site network with:
- HQ / Admin network (left side switch1 and router1)
- Branch network (Right side , switch3 and router3)
- Core router (R1)
- ISP (middle) connecting everything

## Features Implemented
| Feature | Description |
|---|---|
| VLANs | Segmented the network into multiple logical departments |
| Router-on-a-Stick | Used subinterfaces for inter-VLAN routing |
| DHCP | Assigned IP addresses automatically to end devices |
| OSPF | Dynamically exchanged routes between routers |
| NAT/PAT | Allowed internal networks to reach the simulated internet |
| Default Routing | Directed unknown traffic toward the ISP router |
| Switch Management | Configured management IP addresses on switches |
| Ubuntu Admin Host | Used for testing, management, and later automation |

## Network Breakdown
### Left side (Admin/HQ)
Devices:
- Ubuntu-1 (Admin machine)
- PC1
- Switch1
- R2
What this side is doing:
- Acting as your internal LAN
- Ubuntu = admin / management device
- Likely VLAN + DHCP here
  
This is your controlled/internal network

### TOP (R1 + PC3)
Devices:
- PC3
- Switch2
- R1
What this part is:
- Another network connected to R1
- Could represent:
  - Another department
  - Server network
  - Or test VLAN
    
R1 = core router / distribution layer

### Middle (ISP)
Device:
- ISP Router
What this does:
- Connects ALL networks together
- Simulates the internet
- Where you would do:
  - NAT (VERY important)
  - Default routing

### Right side (Branch)
Devices:
- R3
- Switch3
- PC2
What this side is:
- A remote branch office
- Separate network from HQ
This is key for:
- Routing (OSPF or static)
- Security rules

---
## Addressing Table
| Device  | Interface | IP Address      | Subnet Mask     | Default Gateway |
|---------|-----------|-----------------|-----------------|-----------------|
| R1      | G0/0      | 192.168.10.254  | 255.255.255.0   | N/A             |
| R1      | G0/1      | 192.168.20.254  | 255.255.255.0   | N/A             |
| SW1     | VLAN 1    | 192.168.10.100  | 255.255.255.0   | 192.168.10.254  |
| SW2     | VLAN 1    | 192.168.20.100  | 255.255.255.0   | 192.168.20.254  |
| PC1     | NIC       | 192.168.10.1    | 255.255.255.0   | 192.168.10.254  |
| PC2     | NIC       | 192.168.10.2    | 255.255.255.0   | 192.168.10.254  |
| PC3     | NIC       | 192.168.20.1    | 255.255.255.0   | 192.168.20.254  |
| PC4     | NIC       | 192.168.20.2    | 255.255.255.0   | 192.168.20.254  |
| Ubuntu  | ens3      | 192.168.10.10   | 255.255.255.0   | 192.168.10.254  |

---
## Commands
### Router1 Configuration

### Switch1 XConfiguration

### Switch2 Configuration


### Switch3 Configuration

### VPCS Configuration


### Ubuntu Configuration



---
