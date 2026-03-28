# Network Design
---
## Topology
PC1 ----\
Ubuntu -- SW1 ---- SW2 ---- R1 ---- R2 ---- Internet
PC2 ----/

## Suggested links
SW1 to SW2 = trunk
SW2 to R1 = trunk
R1 to R2 = routed link
End devices plug into SW1

---
## Subnet Table
## Subnet Plan

| VLAN | Name       | Subnet          | Default Gateway | Devices               |
|------|------------|-----------------|-----------------|-----------------------|
| 10   | USERS      | 192.168.10.0/24 | 192.168.10.1    | User PCs              |
| 20   | ADMIN      | 192.168.20.0/24 | 192.168.20.1    | Ubuntu, Admin devices |
| 30   | HR         | 192.168.30.0/24 | 192.168.30.1    | HR PCs                |
| 40   | ACCOUNTING | 192.168.40.0/24 | 192.168.40.1    | Accounting PCs        |
| N/A  | R1-R2 LINK | 10.0.12.0/30    | N/A             | R1: 10.0.12.1 / R2: 10.0.12.2 |
| N/A  | INTERNET   | 203.0.113.0/24  | 203.0.113.1     | R2 outside interface  |
