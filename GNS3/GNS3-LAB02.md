# GNS3 LAB 02 - Enterprise Network Setup

This lab demonstrates a small enterprise network in GNS3 using two switches, VLAN segmentation, inter-VLAN routing, DHCP, and NAT.
---
## Network Topology
<img width="934" height="491" alt="lab02" src="https://github.com/user-attachments/assets/1c721b5a-6786-41f8-9d44-b0cf681c103a" />

PCs / Ubuntu -> SW2 -> SW1 -> R1 -> R2 -> Internet

## Subnet Plan

| VLAN | Name        | Subnet           | Gateway        |
|------|------------|------------------|---------------|
| 10   | USERS      | 192.168.10.0/24  | 192.168.10.1  |
| 20   | ADMIN      | 192.168.20.0/24  | 192.168.20.1  |
| 30   | HR         | 192.168.30.0/24  | 192.168.30.1  |
| 40   | ACCOUNTING | 192.168.40.0/24  | 192.168.40.1  |
| N/A  | R1–R2 LINK | 10.0.12.0/30     | -             |
| N/A  | INTERNET   | DHCP (NAT)       | -             |

- VLAN segmentation across multiple switches  
- 802.1Q trunking between switches  
- Router-on-a-Stick inter-VLAN routing  
- DHCP for automatic IP assignment  
- NAT overload for internet access  
- Static routing between R1 and R2  
- ACL to restrict VLAN access  
---
## Management IPs
- SW1 VLAN 20: 192.168.20.4/24
- SW2 VLAN 20: 192.168.20.3/24
---
## Switch1
<img width="488" height="1143" alt="switch1" src="https://github.com/user-attachments/assets/bd2b4b38-30f2-43a6-8086-a09e9f0c15c0" />

Switch1 is the main access switch in the network. It is connecting end devices (PCs and Ubuntu) and forwards traffic to the router (Router1) for inter-VLAN Routing.
on switch1, I created multiple VLANs (10,20,30,40) to put different departments such as Users, Admim, HR and Accounting. Each device port was assigned to the correct VLAN to ensure proper network segmentation.

I configured trunk links between:
- Switch1 and Router1 this is for Router-on-a-Stick
- Switch and Switch2 this will allow VLAN traffic between switches
Switch1 is responible for:
- Separating traffic using VLANs
- Forwarding tagged traffic to the router for routing
- Allowing communication between switches through trunk links

overall, Switch1 acts as the central layer 2 device that organises network traffic and sends it to the router when communication between VLANs required.
---
## Switch2
<img width="548" height="1220" alt="switch2" src="https://github.com/user-attachments/assets/76209a40-ce60-4340-b8d7-c9eb19d2bdff" />

---
## Router1
### Sub-Interface
 <img width="340" height="1021" alt="subinterface" src="https://github.com/user-attachments/assets/863e9835-7c01-48c3-934b-c7b00c849f5b" />


### DHCP
<img width="285" height="244" alt="dhcp" src="https://github.com/user-attachments/assets/ea632634-e65d-4e67-96f3-36932c70df1c" />

---
## Router2
<img width="503" height="1010" alt="r2" src="https://github.com/user-attachments/assets/85573f5a-61e6-4051-ad75-8e26735d84ba" />

---
## Ubuntu

### ACL - Run on Ubuntu
<img width="1040" height="1003" alt="2run" src="https://github.com/user-attachments/assets/bd0f7cde-aa3f-4362-8f95-a00e2a970236" />

---
# Python Script

```python

from netmiko import ConnectHandler
from getpass import getpass


def wildcard_from_mask(mask: str) -> str:
    parts = mask.split(".")
    wildcard = [str(255 - int(part)) for part in parts]
    return ".".join(wildcard)


def build_acl_config(
    acl_name: str,
    src_net: str,
    src_mask: str,
    dst_net: str,
    dst_mask: str,
    interface: str,
    direction: str = "in",
) -> list[str]:
    src_wc = wildcard_from_mask(src_mask)
    dst_wc = wildcard_from_mask(dst_mask)

    return [
        f"ip access-list extended {acl_name}",
        f"deny ip {src_net} {src_wc} {dst_net} {dst_wc}",
        "permit ip any any",
        "exit",
        f"interface {interface}",
        f"ip access-group {acl_name} {direction}",
    ]


def main() -> None:
    router = {
        "device_type": "cisco_ios",
        "host": input("Router IP: ").strip(),
        "username": input("Username: ").strip(),
        "password": getpass("Password: "),
        "secret": getpass("Enable secret: "),
    }

    print("\nChoose ACL policy:")
    print("1. Block HR VLAN 30 -> ADMIN VLAN 20")
    print("2. Block USERS VLAN 10 -> ACCOUNTING VLAN 40")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        acl_name = "HR_BLOCK_ADMIN"
        src_net = "192.168.30.0"
        src_mask = "255.255.255.0"
        dst_net = "192.168.20.0"
        dst_mask = "255.255.255.0"
        interface = "FastEthernet0/0.30"
    elif choice == "2":
        acl_name = "USERS_BLOCK_ACCOUNTING"
        src_net = "192.168.10.0"
        src_mask = "255.255.255.0"
        dst_net = "192.168.40.0"
        dst_mask = "255.255.255.0"
        interface = "FastEthernet0/0.10"
    else:
        print("Invalid choice.")
        return

    commands = build_acl_config(
        acl_name=acl_name,
        src_net=src_net,
        src_mask=src_mask,
        dst_net=dst_net,
        dst_mask=dst_mask,
        interface=interface,
        direction="in",
    )

    try:
        with ConnectHandler(**router) as conn:
            conn.enable()
            output = conn.send_config_set(commands)
            print("\n=== CONFIG OUTPUT ===")
            print(output)

            print("\n=== ACL VERIFICATION ===")
            print(conn.send_command("show access-lists"))

            print("\n=== INTERFACE VERIFICATION ===")
            print(conn.send_command(f"show run interface {interface}"))

    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()

```
