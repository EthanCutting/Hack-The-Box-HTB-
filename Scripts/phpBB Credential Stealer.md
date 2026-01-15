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


Task 3
Identify the Malicious Post ID

Goal:
Find the post_id of the malicious post made by the contractor.

Script Used: find_post_id.py
# basic script to find the user post id only
import sqlite3

db = sqlite3.connect('phpbb.sqlite3')
cur = db.cursor()

username = input("Username:")

cur.execute("SELECT user_id FROM phpbb_users WHERE username = ?", (username,))
user_id = cur.fetchone()[0]

cur.execute("SELECT post_id FROM phpbb_posts WHERE poster_id = ?", (user_id,))
for (post_id,) in cur.fetchall():
    print("POST ID: ", post_id)

db.close()

How It Works

Takes a username as input

Retrieves the corresponding user_id

Queries the phpbb_posts table

Outputs all post_id values created by that user
