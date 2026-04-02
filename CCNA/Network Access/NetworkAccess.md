# CCNA Network Access Notes

These notes cover the main **Network Access** topics from the CCNA. This section focuses on how devices connect to a network, how switches forward traffic inside a LAN, and how networks are designed to be efficient, secure, and reliable.

The topics in this section build the foundation for understanding how local networks operate. They include switching, VLANs, trunking, inter-VLAN routing, loop prevention, link aggregation, wireless basics, and basic switch security.

These notes are useful for:
- understanding core CCNA concepts
- revising key terms and definitions
- preparing for Packet Tracer labs
- reviewing commands and common exam points

The main topics covered are:
- network access basics
- VLANs
- trunking
- inter-VLAN routing
- switching basics
- STP
- EtherChannel
- wireless basics
- port security
- key commands

---

# VLANs
## What a VLAN is
A VLAN (Virtual Local Area Network) is a logical way to divide a switch network into separate broadcast domains. Devices can be connected to the same physical switch but placed in different VLANs so they behave as if they are on separate networks.

This improves network organization and allows administrators to separate groups of users without needing separate physical switches for each group.

## Why VLANs are used 
VLANs are used to:
- improve security by separating users and departments
- reduce broadcast traffic
- make the network easier to manage
- organize devices by department or role
- separate different types of traffic, such as voice and data

For example, HR devices can be placed in one VLAN, Sales in another, and Admin in another. This keeps traffic logically separated.

## Access port
An access port is a switch port that belongs to a single VLAN. It is usually connected to end devices such as:
- PCs
- printers
- IP phones
- servers

Traffic sent on an access port is not tagged with multiple VLAN information. The device connected to that port simply becomes part of the configured VLAN.

Example:
- If interface F0/1 is configured as an access port in VLAN 10, then any PC connected to F0/1 belongs to VLAN 10.

## VLAN membership
VLAN membership means assigning a device or switch port to a specific VLAN.

For example:
- PC on F0/1 → VLAN 10
- PC on F0/2 → VLAN 20
- PC on F0/3 → VLAN 30

A device becomes part of a VLAN based on the port it is connected to, unless more advanced methods are used. On the CCNA, you will usually work with port-based VLAN membership.

## Default VLAN
The default VLAN on Cisco switches is usually VLAN 1.
Key points:
- all switch ports are in VLAN 1 by default
- VLAN 1 exists automatically
- it is best practice not to use VLAN 1 for normal user traffic in production networks

VLAN 1 is commonly used at the start of labs, but in real networks it is better to move user devices into other VLANs.

## Native VLAN
The native VLAN is used on an 802.1Q trunk port. Frames in the native VLAN are sent untagged by default.

Key points:
- trunk ports carry traffic for multiple VLANs
- most VLAN traffic is tagged
- native VLAN traffic is untagged
- both ends of the trunk should use the same native VLAN

If the native VLAN does not match on both ends, it can cause communication and security issues.

## Voice VLAN
A voice VLAN is a special VLAN used for IP phone traffic.

It is used to:
- separate voice traffic from normal data traffic
- improve voice quality
- make it easier to apply QoS policies

A common setup is:
- the IP phone uses the voice VLAN
- the PC connected through the phone uses the data VLAN

This allows one switch port to support both a phone and a PC while keeping the traffic separated.

## Example of separating departments like HR, Sales, Admin
A company may use VLANs to separate departments like this:

| Department | VLAN ID | Subnet |
|-----------|---------|--------|
| HR        | 10      | 192.168.10.0/24 |
| Sales     | 20      | 192.168.20.0/24 |
| Admin     | 30      | 192.168.30.0/24 |

In this design:
- HR users are placed in VLAN 10
- Sales users are placed in VLAN 20
- Admin users are placed in VLAN 30

This means:
- broadcasts from HR stay inside VLAN 10
- Sales traffic stays in VLAN 20
- Admin traffic stays in VLAN 30
- communication between VLANs requires inter-VLAN routing

---

# Trunking 
## What a trunk port is
A trunk port is a switch port that carries traffic for multiple VLANs over a single link. Trunk ports are normally used between network devices such as:
- switch to switch
- switch to router
- switch to multilayer switch

## Why Trunks are needed 
Trunks are needed when multiple VLANs must be carried between devices.

For example, if SW1 and SW2 both have:
- VLAN 10 for HR
- VLAN 20 for Sales
- VLAN 30 for Admin

Then the link between the switches must carry traffic for all of those VLANs. Instead of using a separate cable for each VLAN, one trunk link can carry all VLAN traffic.

This makes the network:
- more efficient
- easier to scale
- easier to manage
- less expensive because fewer physical links are required

## 802.1Q tagging 
802.1Q is the standard used to identify which VLAN a frame belongs to when it travels across a trunk link.

When a frame is sent over a trunk:
- the switch adds a VLAN tag to the Ethernet frame
- the tag tells the receiving device which VLAN the traffic belongs to
- the receiving switch reads the tag and forwards the frame in the correct VLAN

This process is called **VLAN tagging**.

### Key point
Traffic on a trunk is usually tagged so that multiple VLANs can share the same link without mixing their traffic.

## Native VLAN behavior
The native VLAN is a special VLAN on an 802.1Q trunk.

Frames in the native VLAN are sent **untagged** by default.

### Important points
- all other VLAN traffic is normally tagged
- native VLAN traffic is untagged
- both ends of the trunk should have the same native VLAN configured
- a native VLAN mismatch can cause traffic problems and security issues

By default on many Cisco switches, VLAN 1 is the native VLAN unless it is changed.

## Trunk vs access port
| Port Type   | Description |
|------------|-------------|
| Access Port | Carries traffic for one VLAN only. Usually connects to end devices such as PCs, printers, or phones. |
| Trunk Port  | Carries traffic for multiple VLANs. Usually connects to other switches, routers, or multilayer switches. |

### Simple example
- A PC connected to F0/1 uses an **access port**
- A link between SW1 and SW2 uses a **trunk port**


---
# Inter-VLAN Routing
why VLANs cannot talk without a Layer 3 device
router-on-a-stick
multilayer switch idea
subinterfaces
default gateway for each VLAN

---
# Switching Basic
MAC address table
how a switch learns MAC addresses
unicast, broadcast, unknown unicast
collision domain
broadcast domain

---
# STP
why STP exists
switching loops
broadcast storms
root bridge
blocked ports
forwarding ports
STP vs RSTP basic difference

---
# EtherChannel
what EtherChannel is
why it is used
load balancing idea
LACP vs PAgP

---
# Wireless Basic
AP
WLC
SSID
WPA2/WPA3
lightweight AP vs autonomous AP

---
# Port Secruity
what it does
limiting MAC addresses
sticky MAC
violation modes


---
# Key Commands
- show vlan brief
- show interfaces trunk
- show mac address-table
- show spanning-tree
- show etherchannel summary
- show port-security
