# Lab06
<img width="543" height="433" alt="Lab06" src="https://github.com/user-attachments/assets/114bd010-c74c-4cb2-b2d6-523398de3f2d" />

Because all PCs are in 192.168.1.0/24 and connected through layer 2 switches only, PC1 can reach PC3 direclty with no router involved.

---

## 1. If PC1 pings PC3, what messages are sent and who receives them?
starting the lab both switches have empty MAC tables, and all PCs have empty ARP tables.
So PC1 does not know PC3's MAC address yet.

### Step 1: ARP Request
PC1 will send an ARP request asking who has "192.168.1.3?", This is a broadcast frame.

Next who will receives it?
- SW1 receives it on F0/1
- SW1 fllods it out all other ports:
  - F0/2 to PC2
  - G0/1 toward SW2
-SW2 receives it on G0/1 and floods it out:
  - F0/1 to PC3
  - F0/2 to PC4
so the ARP request is received by:
- PC2
- PC3
- PC4

### Step 2: ARP Reply
PC3 sees that the ARP request is for "192.168.1.3", so it sends an ARP reply back to PC1.
This is a unicast frame so who will receives it:
- SW2 receives it from PC3 on F0/1
- SW2 forwards it to SW1 via G0/1
- S1 forwards it to PC1 via F0/1
so the ARP reply is recoved by:
- SW2
- SW1
- PC1

### Step 3: ICMP Echo Request
Next PC1 knows PC3's MAC address, so it sends the ping. This is the ICMP echo request, and it is unicast.
Path:
- PC1 to SW1
- SW1 to SW2
- SW2 to PC3
so it is received by:
- SW1
- SW2
- PC3

### Step 4: ICMP Echo Reply
PC3 replies to the ping with ICMP echo reply, also unicast
Path:
- PC3 to SW2
- SW2 to SW1
- SW1 to PC1
so it is received by:
- SW2
- SW1
- PC1

---

## 2. Commands Used
### Show mac address-table & show mac address-table dynamic

Switch1

<img width="357" height="107" alt="sw1" src="https://github.com/user-attachments/assets/f848eac4-cbeb-4768-910f-8a707bfae04b" />


Switch2

<img width="375" height="94" alt="sw2" src="https://github.com/user-attachments/assets/26f8a93b-c855-4462-9947-2c4436638227" />



