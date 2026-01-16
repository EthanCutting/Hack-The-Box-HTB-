# Wireshark – Network Traffic Analysis Guide

## 📌 Overview

**Wireshark** is a powerful open-source packet analyzer used to capture, inspect, and analyze network traffic in real time. It is widely used by **network engineers, cybersecurity professionals, SOC analysts, and incident responders** to troubleshoot networks, detect malicious activity, and understand protocol behavior.

This repository documents my **Wireshark learning notes, practical usage, filters, and blue-team focused workflows** for network analysis and cybersecurity investigations.

---

## 🔍 What Wireshark Is Used For

* Network troubleshooting and performance analysis
* Packet inspection and protocol analysis
* Detecting suspicious or malicious traffic
* Incident response and digital forensics
* Learning TCP/IP and application-layer protocols
* Malware traffic analysis
* Blue-team monitoring and threat hunting

---

## 🧠 How Wireshark Works

Wireshark captures packets from a selected network interface and decodes them into human-readable protocol fields.

Each packet typically includes:

* Source and destination IP addresses
* Source and destination ports
* Protocol hierarchy (Ethernet → IP → TCP/UDP → Application)
* Packet length and timestamps
* Payload data (if not encrypted)

Captured traffic can be saved as **PCAP / PCAPNG** files for offline analysis and reporting.

---

## 🖥️ Installation

### Linux (Debian / Kali)

```bash
sudo apt update
sudo apt install wireshark
```

### Windows

* Download from: [https://www.wireshark.org](https://www.wireshark.org)
* Install **Npcap** when prompted
* Run Wireshark as Administrator for live captures

### macOS

```bash
brew install wireshark
```

---

## 📡 Network Interfaces

Common interfaces used in captures:

* `eth0` – Wired Ethernet
* `wlan0` – Wireless interface
* `lo` – Loopback traffic (127.0.0.1)
* `any` – Capture from all interfaces (Linux)

Choose the interface that matches the traffic you want to analyze.

---

## 🎯 Capture Filters vs Display Filters

### Capture Filters

* Applied **before** capturing starts
* Reduce storage and noise
* Use **BPF (Berkeley Packet Filter)** syntax

Examples:

```text
host 192.168.1.10
port 80
net 10.0.0.0/24
```

---

### Display Filters

* Applied **after** packets are captured
* Much more powerful and flexible
* Used for analysis and investigation

Examples:

```text
ip.addr == 192.168.1.10
tcp.port == 443
http
ftp
```

---

## 🔑 Common Display Filters

| Purpose               | Filter                 |
| --------------------- | ---------------------- |
| HTTP traffic          | `http`                 |
| HTTPS                 | `tcp.port == 443`      |
| DNS queries           | `dns`                  |
| ICMP (ping)           | `icmp`                 |
| TCP only              | `tcp`                  |
| UDP only              | `udp`                  |
| Failed TCP handshakes | `tcp.flags.reset == 1` |

---

## 🧪 TCP Three-Way Handshake

A normal TCP connection consists of:

1. **SYN** – Client initiates connection
2. **SYN-ACK** – Server responds
3. **ACK** – Client acknowledges

Wireshark allows easy identification of failed or suspicious handshakes.

---

## 🔐 Encryption & TLS Traffic

* HTTPS traffic payloads are encrypted
* Headers (IP, TCP, TLS handshake) are still visible
* Can identify:

  * Server Name Indication (SNI)
  * Certificate details
  * Cipher suites
  * TLS versions

Wireshark is useful even when payloads cannot be decrypted.

---

## 🚨 Security & Incident Response Use Cases

* Detecting suspicious outbound connections
* Identifying beaconing or C2 traffic
* Analyzing malware PCAPs
* Finding credential leaks in plaintext protocols
* Investigating DNS tunneling
* Detecting port scans and brute-force attempts

---

## 🛡️ Useful Security Filters

```text
tcp.flags.syn == 1 and tcp.flags.ack == 0
```

*Detect SYN scans*

```text
dns and !(dns.qry.name contains "trusted-domain")
```

*Suspicious DNS queries*

```text
http.request.method == "POST"
```

*Sensitive HTTP submissions*

---

## 📁 PCAP Files

* `.pcap` / `.pcapng` files store captured traffic
* Can be opened and analyzed later
* Used heavily in:

  * CTF challenges
  * Malware analysis labs
  * Forensics investigations

Always document findings when working with PCAPs.

---

## 🧠 Best Practices

* Capture only what you need
* Use filters early to reduce noise
* Label and document PCAP files
* Understand normal network behavior
* Combine Wireshark with logs (SIEM, firewall, IDS)

---

## 🏁 Conclusion

Wireshark is an essential tool for anyone working in **networking or cybersecurity**. Mastering it provides deep insight into how networks operate and how attacks move through them.

This repository serves as a reference and learning log as I continue developing my **blue-team and network analysis skills**.

---

📌 *Author:* Ethan Cutting
📌 *Focus:* Cybersecurity | Blue Team | Network Analysis

