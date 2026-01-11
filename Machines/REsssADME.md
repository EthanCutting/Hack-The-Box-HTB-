# Hack The Box — Cap (Easy)

This repository documents my complete walkthrough of the **Hack The Box – Cap** machine.  
The objective of this challenge was to gain initial access through enumeration and misconfiguration discovery, followed by Linux privilege escalation to obtain root access.

This machine is rated **Easy** and is a great introduction to real-world web enumeration and privilege escalation techniques.

---

## 🧠 Machine Information

- **Name:** Cap  
- **Difficulty:** Easy  
- **Operating System:** Linux  
- **Platform:** Hack The Box  
- **Status:** Retired  
- **Category:** Web Exploitation / Linux Privilege Escalation  

---

## 🛠 Tools & Techniques Used

- Nmap for port scanning and service enumeration  
- Web browser for manual HTTP inspection  
- SSH for remote access  
- Linux enumeration techniques  
- Manual privilege escalation methods  

---

## 🔍 Enumeration

The first step was performing reconnaissance on the target machine to identify open ports and running services.  
Service discovery revealed a web application that required further inspection.

Web enumeration was performed to identify exposed functionality and misconfigurations that could lead to initial access.

---

## 🚪 Initial Access

Through careful inspection of the web application, a misconfiguration was identified that allowed access to sensitive functionality.  
This access was leveraged to obtain valid user credentials, which were then used to log into the system via SSH.

At this stage, user-level access to the machine was achieved.

---

## 📁 User Flag

After gaining user access, basic enumeration of the home directory was performed to locate and retrieve the user flag.

---

## ⚡ Privilege Escalation

With a foothold on the system, local enumeration was conducted to identify privilege escalation vectors.  
Misconfigured permissions and system behaviour allowed escalation from user-level access to root.

Once root privileges were obtained, full control of the machine was achieved.

---

## 🔐 Root Flag

After escalating privileges, the root directory was accessed and the root flag was successfully captured.

---

## 🎯 Key Takeaways

- Importance of thorough enumeration  
- Identifying common web misconfigurations  
- Understanding Linux privilege escalation fundamentals  
- Practicing structured attack methodology  

---

## ⚠️ Disclaimer

This walkthrough is provided **for educational purposes only**.  
All techniques demonstrated should only be used on systems you own or have explicit permission to test.

---

## 🎥 Video Walkthrough

Full video walkthrough of this machine:  
https://www.youtube.com/watch?v=7HdQ3ZoxclA&t=9s
