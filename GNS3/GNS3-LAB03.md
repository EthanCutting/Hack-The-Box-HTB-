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

### Right side (Branch)


---
