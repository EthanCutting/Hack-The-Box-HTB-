# Email Triage Script – HTB Sherlock (Phishing Investigation)

This script contains my hands-on **blue team email forensics work**, developed while completing **Hack The Box (HTB) Sherlock phishing investigations**.

The focus of this script is **SOC-style email triage automation**, reducing manual header inspection and accelerating phishing analysis.

---

## 🔍 Script Overview

This Python script parses a raw `.eml` email file and extracts key indicators used during phishing investigations, including authentication results, network indicators, and attachments.

---

## ⚙️ Script Capabilities

- Extracts sender, recipient, subject, and date headers  
- Parses SPF, DKIM, and DMARC authentication results  
- Extracts IP addresses from email headers  
- Identifies URLs found within the email body  
- Detects and lists attachment filenames  
- Outputs a structured triage summary to the terminal  

---

## 📂 Files
- EmailTriageScript.py
- email.eml

---

`EmailTriageScript.py` is the Python email triage and forensics script.  
`email.eml` is a sample phishing email used for analysis and testing.

---
```python
import email
import re
from email import policy
from email.parser import BytesParser

EML_FILE = "email.eml"

with open(EML_FILE, "rb") as file:
    msg = email.message_from_binary_file(file, policy=policy.default)

# Basic headers
results = {
    "From": msg["From"],
    "To": msg["To"],
    "Subject": msg["Subject"],
    "Date": msg["Date"],
}

# Authentication results
auth_results = msg.get("Authentication-Results", "")
results["SPF"] = "pass" if "spf=pass" in auth_results else "fail"
results["DKIM"] = "pass" if "dkim=pass" in auth_results else "fail"
results["DMARC"] = "pass" if "dmarc=pass" in auth_results else "fail"

# Extract IPs
raw_headers = str(msg)
ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', raw_headers)
results["IPs"] = list(set(ips))

# Extract URLs from body
urls = []
for part in msg.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_content()
        urls.extend(re.findall(r'http[s]?://\S+', body))

results["URLs"] = list(set(urls))

# Attachments
attachments = []
for part in msg.iter_attachments():
    attachments.append(part.get_filename())

results["Attachments"] = attachments

# Output
print("\n=== Email Triage Results ===")
for k, v in results.items():
    print(f"{k.upper():15}: {v}")


---



---

## ▶️ Usage

From the script directory, run:

```bash
python3 EmailTriageScript.py

The script outputs a structured email triage report directly to the terminal.

---
🧪 Example Output
=== Email Triage Results ===
FROM           : Finance Dept <finance@business-finance.com>
TO             : accounts@globalaccounting.com
SUBJECT        : Urgent: Invoice Payment Required - Overdue Notice
DATE           : Mon, 26 Feb 2025 10:15:00 +0000
SPF            : pass
DKIM           : pass
DMARC          : pass
IPS            : ['45.67.89.10', '198.51.100.45']
URLS           : ['https://secure.business-finance.com/invoice/details/view/...']
ATTACHMENTS    : ['Invoice_2025_Payment.zip']


---
🚩 Blue Team Observations

Financial urgency language is a common phishing tactic. ZIP file attachments represent a high-risk indicator. Passing SPF, DKIM, and DMARC does not guarantee email legitimacy, and header IP analysis remains critical during investigations.

---
🎯 Goals of This Script

The purpose of this script is to support HTB Sherlock phishing investigations, practice SOC-style email triage workflows, improve blue team Python scripting skills, and automate repetitive investigation tasks.

---


