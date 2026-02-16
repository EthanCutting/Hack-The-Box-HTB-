# PoryScanner v0.2

yoo welcome !!, 

**PoryScanner** is a Python-based TCP port scanning tool built for **MEEEE!!!**.  
It provides a clean terminal UI, THREADS scanning, and noob service/banner detection.


## Features

- **Interactive terminal menu** with boxed UI
- **Quick Scan**
  - Scans a  list of common ports
  - Uses multithreading for faster scans
- **Full Scan**
  - Scans whater range you want
  - runs "sequentially"  for better scan control
- **Service identification**
  - Detects services (HTTP, SSH, FTP, DNS, etc.) using common port mapping !
- **Banner grabbing**
  - Will try and collect service/version information
- **Clean table output**
  - Displays PORT / STATE / REASON / RTT / SERVICE / VERSION in TUI
- **Ping Test**
  - Check if hosts are UP or DOWN
- **Results saving**
  - Open ports and banners saved to a file ".txt"
- **Scan timing**
  - Shows total scan execution time

---

## How It Works !

- Uses **TCP sockets** (`AF_INET`, `SOCK_STREAM`)
- connect to each port using `connect_ex()`
  - `0` → **OPEN**
  - Non-zero → **CLOSED / FILTERED**
- Quick Scan uses **threading** 
- Full Scan runs **sequentially** for predictable behavior
- Banner grabbing reads any data returned after a successful connection

> Some services won’t return banners unless protocol-specific communication is used  
> (e.g. HTTP request, TLS handshake).  
> **No banner ≠ no service.**

---
