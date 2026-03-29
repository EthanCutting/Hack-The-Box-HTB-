# GNS3 LAB 02 - Enterprise Network Setup

This lab demonstrates a small enterprise network in GNS3 using two switches, VLAN segmentation, inter-VLAN routing, DHCP, and NAT.
---
## Topology

PCs / Ubuntu -> SW1 -> SW2 -> R1 -> R2 -> Internet

## Subnet Plan

| VLAN | Name       | Subnet          | Default Gateway | Devices               |
|------|------------|-----------------|-----------------|-----------------------|
| 10   | USERS      | 192.168.10.0/24 | 192.168.10.1    | User PCs              |
| 20   | ADMIN      | 192.168.20.0/24 | 192.168.20.1    | Ubuntu, Admin devices |
| 30   | HR         | 192.168.30.0/24 | 192.168.30.1    | HR PCs                |
| 40   | ACCOUNTING | 192.168.40.0/24 | 192.168.40.1    | Accounting PCs        |
| N/A  | R1-R2 LINK | 10.0.12.0/30    | N/A             | R1: 10.0.12.1 / R2: 10.0.12.2 |
| N/A  | INTERNET   | 203.0.113.0/24  | 203.0.113.1     | R2 outside interface  |

## Management IPs

- SW1 VLAN 20: 192.168.20.2/24
- SW2 VLAN 20: 192.168.20.3/24
- Ubuntu: 192.168.20.10/24
- Default gateway: 192.168.20.1

---


'''python

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

    '''
