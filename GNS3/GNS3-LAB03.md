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
## Addressing Table & VLANS
| VLAN | Name    | Subnet            | Gateway            |
|------|--------|-------------------|--------------------|
| 10   | USERS  | 192.168.10.0/24   | 192.168.10.1       |
| 20   | ADMIN  | 192.168.20.0/24   | 192.168.20.1       |
| 30   | SERVER | 192.168.30.0/24   | 192.168.30.1       |

---
## Commands
### Switch Config (SW1 / SW2 / SW3 Same)
| Step | Command |
|------|--------|
| 1 | enable |
| 2 | configure terminal |
| 3 | vlan 10 |
| 4 | name USERS |
| 5 | vlan 20 |
| 6 | name ADMIN |
| 7 | vlan 30 |
| 8 | name SERVER |
| 9 | interface range e0/1-2 |
| 10 | switchport mode access |
| 11 | switchport access vlan 10 |
| 12 | exit |
| 13 | interface e0/3 |
| 14 | switchport mode access |
| 15 | switchport access vlan 20 |
| 16 | exit |
| 17 | interface e0/0 |
| 18 | switchport trunk encapsulation dot1q |
| 19 | switchport mode trunk |
| 20 | exit |
| 21 | interface vlan 1 |
| 22 | ip address 192.168.X.100 255.255.255.0 |
| 23 | no shutdown |
| 24 | exit |
| 25 | ip default-gateway 192.168.X.1 |
| 26 | end |
| 27 | write memory |

### R1 (Main Router - DHCP + INTER-VLAN + OSPF + NAT)
| Step | Command |
|------|--------|
| 1 | enable |
| 2 | configure terminal |
| 3 | hostname R1 |
| 4 | no ip domain-lookup |
| 5 | interface g0/0 |
| 6 | no shutdown |
| 7 | exit |
| 8 | interface g0/0.10 |
| 9 | encapsulation dot1Q 10 |
| 10 | ip address 192.168.10.1 255.255.255.0 |
| 11 | ip nat inside |
| 12 | exit |
| 13 | interface g0/0.20 |
| 14 | encapsulation dot1Q 20 |
| 15 | ip address 192.168.20.1 255.255.255.0 |
| 16 | ip nat inside |
| 17 | exit |
| 18 | interface g0/0.30 |
| 19 | encapsulation dot1Q 30 |
| 20 | ip address 192.168.30.1 255.255.255.0 |
| 21 | ip nat inside |
| 22 | exit |
| 23 | interface g0/1 |
| 24 | ip address 10.0.0.1 255.255.255.252 |
| 25 | ip nat outside |
| 26 | no shutdown |
| 27 | exit |
| 28 | ip dhcp excluded-address 192.168.10.1 192.168.10.10 |
| 29 | ip dhcp excluded-address 192.168.20.1 192.168.20.10 |
| 30 | ip dhcp excluded-address 192.168.30.1 192.168.30.10 |
| 31 | ip dhcp pool VLAN10 |
| 32 | network 192.168.10.0 255.255.255.0 |
| 33 | default-router 192.168.10.1 |
| 34 | dns-server 8.8.8.8 |
| 35 | exit |
| 36 | ip dhcp pool VLAN20 |
| 37 | network 192.168.20.0 255.255.255.0 |
| 38 | default-router 192.168.20.1 |
| 39 | dns-server 8.8.8.8 |
| 40 | exit |
| 41 | ip dhcp pool VLAN30 |
| 42 | network 192.168.30.0 255.255.255.0 |
| 43 | default-router 192.168.30.1 |
| 44 | dns-server 8.8.8.8 |
| 45 | exit |
| 46 | access-list 1 permit 192.168.0.0 0.0.255.255 |
| 47 | ip nat inside source list 1 interface g0/1 overload |
| 48 | router ospf 1 |
| 49 | network 10.0.0.0 0.0.0.3 area 0 |
| 50 | network 192.168.0.0 0.0.255.255 area 0 |
| 51 | exit |
| 52 | ip route 0.0.0.0 0.0.0.0 10.0.0.2 |
| 53 | end |
| 54 | write memory |

### ISP Router
| Step | Command |
|------|--------|
| 1 | enable |
| 2 | configure terminal |
| 3 | hostname ISP |
| 4 | interface g0/0 |
| 5 | ip address 10.0.0.2 255.255.255.252 |
| 6 | no shutdown |
| 7 | exit |
| 8 | interface loopback0 |
| 9 | ip address 8.8.8.8 255.255.255.255 |
| 10 | exit |
| 11 | router ospf 1 |
| 12 | network 10.0.0.0 0.0.0.3 area 0 |
| 13 | exit |
| 14 | ip route 192.168.0.0 255.255.0.0 10.0.0.1 |
| 15 | end |
| 16 | write memory |

### Testing
| Test | Command |
|------|--------|
| Check IP | ipconfig / ip addr |
| Ping gateway | ping 192.168.10.1 |
| Ping other VLAN | ping 192.168.20.1 |
| Ping internet | ping 8.8.8.8 |
| OSPF check | show ip route |
| NAT check | show ip nat translations |

---
