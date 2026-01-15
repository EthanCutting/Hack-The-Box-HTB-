# Incident Investigation – phpBB Credential Stealer

This repository contains small Python scripts used to investigate a security incident involving unauthorized admin access and a malicious forum post in a phpBB application.

The investigation focuses on identifying:
1. The external contractor’s username
2. Admin access based on IP addresses
3. The post ID of the malicious post made by the contractor

---

## Task 1 & Task 2  
### Identify the External Contractor Username

**Goal:**  
Determine which user accounts accessed the phpBB Admin Control Panel (`/adm/`) by correlating Apache access logs with the phpBB database.

---

### Script Used: `find_contractor.py`

```python
# basic script to find the user
import sqlite3 

access_log = 'access.log'
DB_FILE = 'phpbb.sqlite3'

def get_admin_ips(log_file):
    ips = set()
    # open file and read lines
    with open(log_file, 'r') as f:
        for line in f:
            if '/adm/' in line:
                parts = line.split()
                ip = parts[0]
                ips.add(ip)

    return ips

def find_users_by_ips(DB_FILE, ips):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    for ip in ips:
        print(f"\n[+] Checking IP: {ip}")
        cursor.execute("""
            SELECT user_id, username, user_type, user_ip
            FROM phpbb_users
            WHERE user_ip = ?
        """, (ip,))

        results = cursor.fetchall()

        if results:
            for user_id, username, user_type, user_ip in results:
                print(f"    User ID  : {user_id}")
                print(f"    Username : {username}")
                print(f"    User IP  : {user_ip}")
        else:
            print("No users found for this IP.")

    conn.close()

if __name__ == "__main__":
    admin_ips = get_admin_ips(access_log)
    print(f"[+] Found admin access from IPs: {admin_ips}")
    find_users_by_ips(DB_FILE, admin_ips)
