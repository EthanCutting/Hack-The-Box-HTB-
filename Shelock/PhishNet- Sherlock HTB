# PhishNet – Very Easy (HTB Sherlock)

This repository documents my investigation of the **PhishNet – Very Easy** Sherlock challenge on **Hack The Box**, focusing on **blue team email forensics and phishing analysis**.

The scenario involves an accounting team receiving an urgent payment request from a trusted vendor. Although the email appears legitimate, it contains a suspicious link and a malicious ZIP attachment. The objective is to analyze the email safely and uncover the attacker’s infrastructure and intent.

---

## 🧠 What PhishNet Is Testing

You are **NOT** meant to:
- Detonate malware
- Reverse binaries
- Perform Windows internals analysis

You **ARE** meant to:
- Read and interpret email headers correctly
- Identify spoofing and impersonation
- Trace sender infrastructure
- Safely extract URLs and attachments
- Apply SOC-style investigative reasoning

---

## 📌 Investigation Tasks & Answers

### Task 1 – What is the originating IP address of the sender?

45.67.89.10

---

### Task 2 – Which mail server relayed this email before reaching the victim?

203.0.113.5

---

### Task 3 – What is the sender's email address?

finance@business-finance.com

---

### Task 4 – What is the `Reply-To` email address specified in the email?

mailto:support@business-finance.com

---

### Task 5 – What is the SPF (Sender Policy Framework) result for this email?

Authentication-Results: spf=pass (domain business-finance.com designates 45.67.89.10 as permitted sender) = pass


---

### Task 6 – What is the domain used in the phishing URL inside the email?

**Command Used:**
```bash
grep -Eo 'https?://[^"]+' email.eml

Output:

https://secure.business-finance.com/invoice/details/view/INV2025-0987/payment

Answer:

secure.business-finance.com

---

Task 7 – What is the fake company name used in the email?

Command Used:

grep -Ei 'From:|Return-Path:|X-Originating-|Organization|X-Organization' email.eml


Output: 

Return-Path: <finance@business-finance.com>
X-Originating-IP: [45.67.89.10]
X-Organization: Business Finance Ltd.
X-Envelope-From: finance@business-finance.com
From: "Finance Dept" <finance@business-finance.com>

Answer:

Business Finance Ltd.


---

Task 8 – What is the name of the attachment included in the email?

Command Used:

grep -Ei 'Content-Type:|Content-Disposition:' email.eml


Output:

Content-Type: multipart/mixed; boundary="boundary123"
Content-Type: text/html; charset="UTF-8"
Content-Type: application/zip; name="Invoice_2025_Payment.zip"
Content-Disposition: attachment; filename="Invoice_2025_Payment.zip"


Answer:

Invoice_2025_Payment.zip


---

Task 9 – What is the SHA-256 hash of the attachment?

Command Used:

sha256sum out/Invoice_2025_Payment.zip

Output:
8379c41239e9af845b2ab6c27a7509ae8804d7d73e455c800a551b22ba25bb4a

Task 10 – What is the filename of the malicious file contained within the ZIP attachment?

Command Used:

strings Invoice_2025_Payment.zip


Output:

invoice_document.pdf.bat

---
Task 11 – Which MITRE ATT&CK technique is associated with this attack?

T1566.001 – Phishing: Spearphishing Attachment












