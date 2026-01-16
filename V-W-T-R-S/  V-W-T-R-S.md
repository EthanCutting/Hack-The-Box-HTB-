# Malware Fundamentals 🦠  
## Viruses, Worms, Trojans, Ransomware & Spyware

Understanding malware is a **core cybersecurity skill**.  
This document explains the most common malware types, how they work, how they spread, and how to defend against them.

---

## What Is Malware?

**Malware (Malicious Software)** is any software intentionally designed to:
- Damage systems
- Steal data
- Disrupt operations
- Spy on users
- Gain unauthorized access

Malware often relies on **human interaction**, **software vulnerabilities**, or **poor security practices** to succeed.

---

## 1. Virus 🧬

### What Is a Virus?
A **virus** is malware that **attaches itself to a legitimate file or program** and executes when the host file is run.

### Key Characteristics
- Requires **user interaction** to spread
- Attaches to files (executables, documents)
- Can modify, corrupt, or destroy data

### How It Spreads
- Downloading infected software
- Email attachments
- USB drives
- Cracked or pirated programs

### Example
A Word document with a malicious macro that runs when the file is opened.

### Defense Measures
- Antivirus software
- Disable macros by default
- Avoid untrusted downloads
- Regular system updates

---

## 2. Worm 🐛

### What Is a Worm?
A **worm** is self-replicating malware that spreads **without user interaction**, typically across networks.

### Key Characteristics
- Exploits network vulnerabilities
- Spreads automatically
- Can overwhelm networks and systems

### How It Spreads
- Unpatched services
- Open ports
- Weak network security

### Example
The **WannaCry worm** spread using an SMB vulnerability.

### Defense Measures
- Patch systems regularly
- Firewalls and IDS/IPS
- Network segmentation
- Disable unused services

---

## 3. Trojan 🐴

### What Is a Trojan?
A **Trojan** disguises itself as legitimate software to trick users into installing it.

### Key Characteristics
- Does **not self-replicate**
- Relies on deception
- Often installs backdoors

### Common Trojan Types
- Remote Access Trojans (RATs)
- Banking Trojans
- Downloader Trojans

### Example
A fake “free game” that installs a backdoor.

### Defense Measures
- Software from trusted sources only
- Application whitelisting
- User awareness training
- Endpoint detection & response (EDR)

---

## 4. Ransomware 🔐

### What Is Ransomware?
Ransomware encrypts a victim’s files and demands payment for the decryption key.

### Key Characteristics
- Data encryption
- Ransom demand
- Often combined with data exfiltration

### How It Spreads
- Phishing emails
- Exploited vulnerabilities
- Remote Desktop Protocol (RDP) attacks

### Example
LockBit, REvil, WannaCry

### Defense Measures
- Regular offline backups
- Patch management
- Email filtering
- Least privilege access
- Incident response planning

---

## 5. Spyware 👁️

### What Is Spyware?
Spyware secretly monitors user activity and collects sensitive information.

### Key Characteristics
- Stealthy operation
- Data theft (credentials, keystrokes)
- Often bundled with legitimate apps

### Types of Spyware
- Keyloggers
- Screen capture tools
- Browser tracking spyware

### Example
Keylogger capturing login credentials.

### Defense Measures
- Anti-spyware tools
- Secure browsing habits
- Permission auditing
- OS hardening

---

## Malware Comparison Table

| Malware Type | User Interaction | Self-Spreading | Main Goal |
|-------------|------------------|----------------|----------|
| Virus       | Yes              | No             | Damage / Corruption |
| Worm        | No               | Yes            | Rapid spread |
| Trojan      | Yes              | No             | Backdoor / Control |
| Ransomware  | Often Yes        | Sometimes      | Financial extortion |
| Spyware     | Yes / No         | No             | Data theft |

---

## Common Infection Vectors

- Phishing emails
- Malicious attachments
- Fake software updates
- Drive-by downloads
- Weak passwords
- Unpatched systems

---

## Detection & Prevention Best Practices

- Defense in depth
- Least privilege
- Regular backups
- Security awareness training
- Endpoint monitoring
- Patch management
- Network segmentation

---

## Why This Matters in Cybersecurity

Understanding malware:
- Helps detect real-world attacks
- Improves incident response
- Builds strong defensive strategies
- Is foundational for SOC, blue team, and red team roles

---

