# SSH Log Analysis & Password Spray Detection (Blue Team Lab)

This walkthrough documents a **blue team SSH log analysis lab**, focused on detecting **brute-force and password spray attacks** using Linux authentication logs and Python automation.

The lab simulates real SOC workflows: collecting logs, parsing failed login attempts, identifying attacker behavior, and generating alerts and reports.

---

## 🧠 Lab Objectives

This lab is designed to help practice:

- SSH server setup and log generation
- Manual log inspection (`auth.log`)
- Secure log transfer between machines
- Python-based log parsing and detection logic
- Identifying brute-force vs password spray attacks
- SOC-style alerting and reporting

## 🛠️ Phase 1: SSH Server Setup

### 1️⃣ Install SSH Server

```bash
sudo apt update
sudo apt install openssh-server -y

2️⃣ Start and Enable SSH

sudo systemctl start ssh
sudo systemctl enable ssh

3️⃣ Verify SSH Status

sudo systemctl status ssh

4️⃣ Create Test Users

sudo adduser testuser
sudo adduser adminuser

5️⃣ Monitor SSH Logs

sudo tail -f /var/log/auth.log


🧠 Phase 2: Log Collection & Transfer
Sending logs to an analysis machine
scp /tmp/auth.log kali@192.168.74.134:/home/kali/ssh_lab_logs.txt

Retrieving logs from a target machine
scp ethan@192.168.74.133:/var/log/auth.log ~/ssh_lab_logs.txt

🧠 Phase 3: Analyze SSH Logs with Python

The following Python script parses SSH authentication logs to detect failed login attempts, identify attacking IPs, classify attack types, and generate alerts.

🐍 SSH Failed Login Detection Script
#!/usr/bin/env python3
import re
import csv
import sys

LOG_FILE = "ssh_lab_logs.txt"
ALERT_THRESHOLD = 5

IP_PATTERN = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")
USER_PATTERN = re.compile(r"Failed password for (?:invalid user )?([a-zA-Z0-9._-]+)")

def load_lines(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"[!] Log file not found: {path}")
        sys.exit(1)

def parse_failed_logins(lines):
    failed = {}
    for line in lines:
        if "Failed password" not in line:
            continue

        ip_match = IP_PATTERN.search(line)
        user_match = USER_PATTERN.search(line)

        if not ip_match:
            continue

        ip = ip_match.group(0)
        user = user_match.group(1) if user_match else "UNKNOWN"

        if ip not in failed:
            failed[ip] = {"count": 0, "users": set()}

        failed[ip]["count"] += 1
        failed[ip]["users"].add(user)

    return failed

def classify_attack(users):
    return "Brute force" if len(users) <= 2 else "Password spray"

def main():
    lines = load_lines(LOG_FILE)
    failed = parse_failed_logins(lines)

    sorted_items = sorted(failed.items(), key=lambda x: x[1]["count"], reverse=True)

    print("\n=== SSH Failed Login Summary ===")
    for ip, data in sorted_items:
        print(f"{ip} -> {data['count']} failures | Users: {', '.join(data['users'])} | Type: {classify_attack(data['users'])}")

    print(f"\n=== Alerts (threshold > {ALERT_THRESHOLD}) ===")
    for ip, data in sorted_items:
        if data["count"] > ALERT_THRESHOLD:
            print(f"ALERT: {ip} -> {data['count']} failures | {classify_attack(data['users'])}")

    with open("ssh_alerts.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ip", "failures", "users", "attack_type"])
        for ip, data in sorted_items:
            writer.writerow([ip, data["count"], ";".join(data["users"]), classify_attack(data["users"])])

    print("\n[i] Saved CSV report: ssh_alerts.csv")

if __name__ == "__main__":
    main()

▶️ Output
=== SSH Failed Login Summary ===
192.168.74.134 -> 7 failures | Users: admin, user1, user2 | Type: Password spray

=== Alerts (threshold > 5) ===
ALERT: 192.168.74.134 -> 7 failures | Password spray

[i] Saved CSV report: ssh_alerts.csv

🧠 Executable Script
chmod +x ssh_detector.py
./ssh_detector.py

🧠 SOC Fundamentals: Counting Patterns

Key counting patterns used in SOC detections:

Total count

Count by key (IP, user, etc.)

Unique count (sets)

Count with context (IP + users)

Time-bucket counting

Mastering these patterns allows you to build almost any detection logic.


### The 2 rules that fix everything
- **Never do**: ```markdown above headings  
- **Always do**: headings as normal text, and only wrap *actual code/commands* in ```bash / ```python blocks

If you paste that into your README, you’ll get exactly: **white text/headers + gray co
