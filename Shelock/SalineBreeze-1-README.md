# SalineBreeze-1 — Sherlock (Hack The Box)

This repository documents my investigation and answers for the **SalineBreeze-1 Sherlock** challenge on **Hack The Box**, which focuses on the **Salt Typhoon** (aka **GhostEmperor / Earth Estries**) advanced persistent threat group.

> ⚠️ This content is for **educational purposes only** and reflects analysis performed in a legal, controlled environment (HTB Sherlock).

---

## 🧠 Scenario Overview

Salt Typhoon is a **China-nexus, state-sponsored threat actor** known for long-term espionage campaigns targeting **telecommunications and ISP infrastructure**.  
This Sherlock scenario walks through threat intelligence research, MITRE ATT&CK mapping, and malware analysis across multiple vendor reports.

---

## 🎯 Tasks & Findings

### Task 1 — Country Attribution
**Answer:** 🇨🇳 **China (People’s Republic of China)**

---

### Task 2 — First Known Activity
**Answer:** **2019**

---

### Task 3 — Targeted Infrastructure
**Answer:** **Telecommunications & ISP network infrastructure**

---

### Task 4 — Malware (S1206)
**Answer:** **JumbledPath**

---

### Task 5 — Targeted Operating System
**Answer:** **Linux**

---

### Task 6 — Programming Language
**Answer:** **Go (Golang)**

---

### Task 7 — Affected Vendor Devices
**Answer:** **Cisco**

---

### Task 8 — Indicator Removal Technique
**Answer:** **T1070.002**

---

### Task 9 — Sophos Firewall CVE
**Answer:** **CVE-2022-3236**

---

### Task 10 — Registry Key for Persistence

```text
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
```

**ATT&CK ID:** `T1547.001`

---

### Task 11 — Registry Modification Technique
**Answer:** **T1112**

---

### Task 12 — Trend Micro Threat Actor Name
**Answer:** **Earth Estries**

---

### Task 13 — Modular Backdoor Malware
**Answer:** **GhostSpider**

---

### Task 14 — .dev C2 Domain

```text
telcom.grishamarkovgf8936.workers.dev
```

---

### Task 15 — First C2 GET Request Filename
**Answer:** **index.php**

---

### Task 16 — Kaspersky (2021) Threat Actor Name
**Answer:** **GhostEmperor**

---

### Task 17 — Malware Focused in Securelist Article
**Answer:** **Demodex**

---

### Task 18 — Malware Type
**Answer:** **Kernel-mode rootkit**

---

### Task 19 — PowerShell Dropper Encryption
**Answer:** **AES**

---

### Task 20 — IOCTL Code for Service Hiding

```text
0x220300
```

---

## 🧠 Key Takeaways

- Long-term nation-state espionage campaigns are common
- Network infrastructure is a prime target
- MITRE ATT&CK enables cross-vendor correlation
- Kernel-mode malware is extremely stealthy

---

## 📚 References

- MITRE ATT&CK
- Picus Security
- Trend Micro
- Kaspersky Securelist

---

🧩 **Sherlock completed — threat intelligence successfully mapped.**
