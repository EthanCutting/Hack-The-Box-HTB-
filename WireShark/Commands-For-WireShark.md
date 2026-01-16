# Wireshark Commands & Filters Cheat Sheet

## 📌 Overview

This README focuses specifically on **Wireshark commands, filters, and practical analysis expressions** used during network troubleshooting, cybersecurity investigations, and blue-team operations.

The goal of this file is to serve as a **quick-reference command and filter guide** for everyday Wireshark usage.

---

## 🖥️ Starting Wireshark

### Launch Wireshark (Linux)

```bash
wireshark
```

### Capture as Root (if required)

```bash
sudo wireshark
```

### Capture via Terminal (tshark)

```bash
tshark -i eth0
```

---

## 📡 Interface Commands (tshark)

| Command           | Description               |
| ----------------- | ------------------------- |
| `tshark -D`       | List available interfaces |
| `tshark -i eth0`  | Capture on eth0           |
| `tshark -i wlan0` | Capture on Wi-Fi          |
| `tshark -i any`   | Capture on all interfaces |
| `tshark -c 100`   | Capture first 100 packets |

---

## 🎯 Capture Filters (BPF Syntax)

> Applied **before capture starts**

```text
host 192.168.1.10
```

Capture traffic to or from a specific host

```text
net 10.0.0.0/24
```

Capture a specific network

```text
port 80
```

Capture traffic on port 80

```text
tcp
```

Capture only TCP traffic

```text
udp
```

Capture only UDP traffic

```text
icmp
```

Capture ICMP traffic (ping)

```text
port 80 or port 443
```

Capture HTTP and HTTPS traffic

---

## 🔍 Display Filters (Wireshark Syntax)

> Applied **after capture** for analysis

```text
ip.addr == 192.168.1.10
```

Show packets involving an IP

```text
tcp.port == 443
```

Show HTTPS traffic

```text
udp.port == 53
```

Show DNS traffic

```text
http
```

Show HTTP traffic

```text
icmp
```

Show ICMP packets

---

## 🔑 TCP Analysis Filters

```text
tcp.flags.syn == 1 and tcp.flags.ack == 0
```

Detect SYN scans

```text
tcp.flags.reset == 1
```

Detect connection resets

```text
tcp.analysis.retransmission
```

Show retransmitted packets

```text
tcp.analysis.duplicate_ack
```

Detect network congestion

---

## 🧪 HTTP Filters

```text
http.request
```

Show HTTP requests

```text
http.response
```

Show HTTP responses

```text
http.request.method == "GET"
```

Filter GET requests

```text
http.request.method == "POST"
```

Detect POST submissions (credentials, forms)

```text
http.response.code == 401
```

Unauthorized responses

---

## 🔐 TLS / HTTPS Filters

```text
tls
```

Show TLS traffic

```text
tls.handshake
```

Show TLS handshakes

```text
tls.handshake.type == 1
```

Client Hello packets

```text
tls.handshake.extensions_server_name
```

Reveal SNI (Server Name Indication)

---

## 🌐 DNS Filters

```text
dns
```

Show DNS traffic

```text
dns.qry.name contains "google"
```

Filter specific domain queries

```text
dns.flags.response == 0
```

DNS queries only

```text
dns.flags.response == 1
```

DNS responses only

---

## 🚨 Security & Threat Hunting Filters

```text
ip.dst != 192.168.0.0/16
```

Outbound internet traffic

```text
tcp.port == 4444
```

Common malware C2 port

```text
frame.len > 1000
```

Large packets (exfiltration)

```text
http.user_agent
```

Identify suspicious user agents

---

## 🧰 Useful Wireshark Shortcuts

| Shortcut           | Action               |
| ------------------ | -------------------- |
| `Ctrl + E`         | Start / Stop capture |
| `Ctrl + K`         | Clear packets        |
| `Ctrl + F`         | Find packets         |
| `Ctrl + Shift + P` | Preferences          |
| `Ctrl + .`         | Next packet          |

---

## 📁 PCAP Handling Commands

```bash
tshark -r capture.pcap
```

Read a PCAP file

```bash
tshark -r capture.pcap -Y "http"
```

Apply display filter to PCAP

```bash
tshark -r capture.pcap -T fields -e ip.src -e ip.dst
```

Extract IP addresses

---

📌 *Author:* Ethan Cutting
📌 *Focus:* Cybersecurity | Blue Team | Network Traffic Analysis
