# PhishNet – Very Easy (HTB Sherlock)

This repository documents my investigation of the **PhishNet – Very Easy** Sherlock challenge on **Hack The Box**, focusing on **blue team email forensics and phishing analysis**.

The scenario involves an accounting team receiving an urgent payment request from a trusted vendor. Although the email appears legitimate, it contains a suspicious link and a malicious ZIP attachment.  
The objective is to analyze the email safely and uncover the attacker’s infrastructure and intent.

---

## 🧠 What PhishNet Is Testing

You are **NOT meant to**:
- Detonate malware
- Reverse binaries
- Perform Windows internals analysis

You **ARE meant to**:
- Read and interpret email headers correctly
- Identify spoofing and impersonation
- Trace sender infrastructure
- Safely extract URLs and attachments
- Apply SOC-style investigative reasoning

---

## 🔎 Investigation Tasks & Answers

### Task 1 — What is the originating IP address of the sender?

```text
45.67.89.10
```

---

### Task 2 — Which mail server relayed this email before reaching the victim?

```text
203.0.113.5
```

---

### Task 3 — What is the sender’s email address?

```text
finance@business-finance.com
```

---

### Task 4 — What is the Reply-To email address specified in the email?

```text
support@business-finance.com
```

---

### Task 5 — What is the SPF (Sender Policy Framework) result for this email?

```text
Authentication-Results: spf=pass (domain business-finance.com designates 45.67.89.10 as permitted sender)
```

---

### Task 6 — What is the domain used in the phishing URL inside the email?

**Command Used**
```bash
grep -Eo 'https?://[^"]+' email.eml
```

**Output**
```text
https://secure.business-finance.com/invoice/details/view/INV2025-0987/payment
```

**Answer**
```text
secure.business-finance.com
```

---

### Task 7 — What is the fake company name used in the email?

**Command Used**
```bash
grep -Ei 'From:|Return-Path:|X-Originating-Organization|X-Organization' email.eml
```

**Output**
```text
Return-Path: <finance@business-finance.com>
X-Originating-IP: [45.67.89.10]
X-Organization: Business Finance Ltd.
From: "Finance Dept" <finance@business-finance.com>
```

**Answer**
```text
Business Finance Ltd.
```

---

### Task 8 — What is the name of the attachment included in the email?

**Command Used**
```bash
grep -Ei 'Content-Type|Content-Disposition' email.eml
```

**Output**
```text
Content-Type: multipart/mixed; boundary="boundary123"
Content-Type: application/zip; name="Invoice_2025_Payment.zip"
Content-Disposition: attachment; filename="Invoice_2025_Payment.zip"
```

**Answer**
```text
Invoice_2025_Payment.zip
```

---

### Task 9 — What is the SHA-256 hash of the attachment?

**Command Used**
```bash
sha256sum Invoice_2025_Payment.zip
```

**Output**
```text
837c41339e78452ab27a259a8884d27d34455c889a55b12b2b5f34a
```

---

### Task 10 — What is the filename of the malicious file contained within the ZIP attachment?

**Command Used**
```bash
strings Invoice_2025_Payment.zip
```

**Output**
```text
invoice_document.pdf.bat
```

---

### Task 11 — Which MITRE ATT&CK technique is associated with this attack?

```text
T1566.001 – Phishing: Spearphishing Attachment
```

---

## 🧠 Key Takeaways

- Email headers provide critical infrastructure intelligence
- Legitimate-looking domains can still be malicious
- ZIP attachments commonly disguise executable files
- MITRE ATT&CK helps classify attacker behavior consistently

---

