# GNS3 LAB 01 – Enterprise Network Setup

## Topology

PC → Switch → R1 → R2 (ISP) → Internet

---

## Subnet Plan

### VLAN Subnet Table

| VLAN | Name        | Subnet            | Gateway (R1)     | Devices                  |
|------|------------|------------------|------------------|--------------------------|
| 10   | USERS       | 192.168.10.0/24  | 192.168.10.1     | PCs                      |
| 20   | ADMIN       | 192.168.20.0/24  | 192.168.20.1     | Ubuntu + Switch mgmt     |
| 30   | HR          | 192.168.30.0/24  | 192.168.30.1     | PCs                      |
| 40   | ACCOUNTING  | 192.168.40.0/24  | 192.168.40.1     | PCs                      |

---

## Ubuntu Setup

### Static IP Configuration

```bash
sudo ip addr add 192.168.20.10/24 dev eth0
sudo ip link set eth0 up
sudo ip route add default via 192.168.20.1
```
# DNS fix
```bash
sudo nano /etc/resolv.conf
```
Add:
```bash
nameserver 8.8.8.8
```
# LIB
```bash
sudo apt update
sudo apt install net-tools curl -y

curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --break-system-packages
python3 -m pip install --break-system-packages netmiko
```
# Verify Installtion
```bash
  python3 -c "import netmiko; print(netmiko.__version__)"
```
---

# Switch1 Configuration
## Vlan
```bash
conf t

vlan 10
 name USERS

vlan 20
 name ADMIN

vlan 30
 name HR

vlan 40
 name ACCOUNTING

end
wr
```
## Configure Access Ports
```bash
interface g0/0
 switchport mode access
 switchport access vlan 20
 no shutdown
```
## Configure Trunk Port (to Router1)
```bash
interface g0/3
 switchport mode trunk
 no shutdown
```
## Switch Management
```bash
interface vlan 20
 ip address 192.168.20.2 255.255.255.0
 no shutdown

ip default-gateway 192.168.20.1
```
---

# Router1 Configuration
## Basic setup
```bash
conf t
hostname R1
no ip domain-lookup
```
## Interface
```bash
interface f0/0
 no shutdown

interface f1/0
 ip address 10.0.12.1 255.255.255.252
 no shutdown
## Router-on-a-Stick
```bash
interface f0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0

interface f0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0

interface f0/0.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0

interface f0/0.40
 encapsulation dot1Q 40
 ip address 192.168.40.1 255.255.255.0
```
## DHCP Configuration
```bash
ip dhcp excluded-address 192.168.10.1 192.168.10.20
ip dhcp excluded-address 192.168.20.1 192.168.20.20
ip dhcp excluded-address 192.168.30.1 192.168.30.20
ip dhcp excluded-address 192.168.40.1 192.168.40.20

ip dhcp pool VLAN10
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 8.8.8.8

ip dhcp pool VLAN20
 network 192.168.20.0 255.255.255.0
 default-router 192.168.20.1
 dns-server 8.8.8.8

ip dhcp pool VLAN30
 network 192.168.30.0 255.255.255.0
 default-router 192.168.30.1
 dns-server 8.8.8.8

ip dhcp pool VLAN40
 network 192.168.40.0 255.255.255.0
 default-router 192.168.40.1
 dns-server 8.8.8.8
```
## Default Route
```bash
ip route 0.0.0.0 0.0.0.0 10.0.12.2
```
## Verification
```bash
ping 10.0.12.2
ping 8.8.8.8 source 192.168.20.1
show ip route
```

---

# Router two (ISP)
interface f0/0   ! to R1
ip address 10.0.12.2 255.255.255.252
ip nat inside
no shut/

interface f1/0   ! to NAT cloud
ip address dhcp
ip nat outside
no shutdown

access-list 1 permit 192.168.0.0 0.0.255.255
access-list 1 permit 10.0.12.0 0.0.0.3

ip nat inside source list 1 interface f1/0 overload

ip route 192.168.10.0 255.255.255.0 10.0.12.1
ip route 192.168.20.0 255.255.255.0 10.0.12.1
ip route 192.168.30.0 255.255.255.0 10.0.12.1
ip route 192.168.40.0 255.255.255.0 10.0.12.1



---


# clear nat if issuess
clear ip nat translation *



# telnet testing  (scripting)
username admin privilege 15 secret cisco
line vty 0 4
password cisco
login local
transport input telnet
end
wr


----------------------------------------------------------------------------------------------------------------------------------------

### scirpting
""python 
from netmiko import ConnectHandler
devices = [
  {
    "device_name": "Switch1",
    ],
  }
}
for device in devices:
  print(f"\nconnecting now to {device['device_name']}........")
  conn = ConnectHandler(
    device_type=device["device_type"],

""
