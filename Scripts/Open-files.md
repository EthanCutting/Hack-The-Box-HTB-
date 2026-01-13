

# count fail logins (status 403 / 500)
failed = 0

with open("access.log", "r") as log_file:
    for line in log_file:
        parts = line.split()
        status = parts[8]

        if status in ["403", "500"]:
            failed += 1
print(f"Total failed login attempts: {failed}")




# Detect suspicious admin access (beginner SOC logic)
with open("access.log", "r") as log_file:
    for line in log_file:
        if "/adm/" in line:
            print("[ALERT] Suspicious admin access detected:")
            print(line.strip())




"""""""""
# Extract IP, HTTP method, URL, status code
with open("access.log", "r") as log_file:
    for line in log_file:
        parts = line.split()

        ip = parts[0]   
        method = parts[5].replace('"', '')
        url = parts[6]
        status = parts[8]

        print(f"IP: {ip}, Method: {method}, URL: {url}, Status: {status}")
"""""""""""


"""""""""
# OPen file 
with open("access.log", "r") as log_file:
    for line in log_file
        print(line.strip())

# info
- for line in file: will read line by line
- .stript(): remove \n

"""""""""

