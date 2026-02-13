""""
    PoryScanner 0.1
    By Ethan PP Cuting
"""
import os
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
start = time.time()
from tabulate import tabulate
from colorama import Fore, Style, init
init(autoreset=True)
import subprocess
import platform
#-------------------------------------------------------------------------------------------------------------------------------
# Tool Information
VERSION = "0.1"
TOOL_NAME = "PortyScanner"
AUTHOR = "Ethan PP Cuting"
#-------------------------------------------------------------------------------------------------------------------------------
# Define colors
GREEN = Fore.GREEN
RED = Fore.RED
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
RESET = Style.RESET_ALL
BLUE = Fore.BLUE
WHITE = Fore.WHITE
BLACK = Fore.BLACK
#-------------------------------------------------------------------------------------------------------------------------------
#  services for ports
COMMON_SERVICES = {
    20: 'FTP Data',
    21: 'FTP Control',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    67: 'DHCP',
    68: 'DHCP',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    3306: 'MySQL',
    3389: 'RDP',
    5900: 'VNC',
    8080: 'HTTP Proxy',
}
#-------------------------------------------------------------------------------------------------------------------------------
# 100 Most Common Ports
TOP_100_PORTS = [
    20, 21, 22, 23, 25, 53, 67, 68, 69, 80,
    110, 119, 123, 137, 138, 139, 143, 161, 162, 179,
    389, 443, 445, 465, 500, 514, 515, 520, 587, 636,
    989, 990, 993, 995, 1080, 1433, 1521, 2049, 2082,
    2083, 2086, 2087, 2095, 2096, 2181, 2375, 2483,
    2484, 3000, 3128, 3306, 3389, 3690, 4444, 5432,
    5601, 5672, 5900, 5985, 5986, 6379, 6667, 7001,
    7002, 8000, 8008, 8080, 8081, 8443, 8888, 9000,
    9042, 9200, 9418, 9999, 10000, 11211, 27017
]
#-------------------------------------------------------------------------------------------------------------------------------
# Welcome Banner
def welcome_banner():
    print(rf"""{CYAN}
        ██████╗  ██████╗ ██████╗ ██╗   ██╗
        ██╔══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝
        ██████╔╝██║   ██║██████╔╝ ╚████╔╝ 
        ██╔═══╝ ██║   ██║██╔══██╗  ╚██╔╝  
        ██║     ╚██████╔╝██║  ██║   ██║   
        ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   

        Welcome, to {TOOL_NAME} v{VERSION}! 
        Ready to do some scanning?, if not leave me alone... {MAGENTA}:-){CYAN}
    {RESET}""")
#-------------------------------------------------------------------------------------------------------------------------------
# Main Menu
def main_menu():
    welcome_banner()
    # Display menu options
    print(f"\n{CYAN}=== {TOOL_NAME} V{VERSION} ==={RESET}") #
    print(f"{YELLOW}1.{RESET} INFO")
    print(f"{YELLOW}2.{RESET} QUICK SCAN (top ports)")
    print(f"{YELLOW}3.{RESET} FULL SCAN (custom range)")
    print(f"{YELLOW}4.{RESET} PING TEST")
    print(f"{YELLOW}5.{RESET} EXIT")
    choice = input(f"{GREEN}Select an option:{RESET}")
    # Handle user choice
    if choice == '1':
        INFO_Option()
    elif choice == '2':
        QUICK_Option()
    elif choice == '3':
        FULL_Option()
    elif choice == '4':
        PING_TEST()
    elif choice == '5':
        EXIT_Option()
        exit()
    # Handle invalid choice
    else:
        print(f"{RED}[-] Invalid choice. Please try again.{RESET}")
        input("Press Enter to continue...")
#-------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------
# Functions for options
def INFO_Option():
    # Display tool information
    welcome_banner()
    print(f"\n{CYAN}=== {TOOL_NAME} V{VERSION} ==={RESET}") #
    print(f"{GREEN}[+] Tool    :   {TOOL_NAME}{RESET}") 
    print(f"{GREEN}[+] Version :   {VERSION}{RESET}")
    print(f"{GREEN}[+] Author  :   {AUTHOR}{RESET}")
    print(f"{GREEN}[+] GitHub  :   https://github.com/EthanCutting/Hack-The-Box-HTB-/blob/main/Scripts/PoryScanner.py{RESET} ")
    print(f"{CYAN} ==================================================================================================\n{RESET}")
    # Additional info
    print(f"""{YELLOW}
          INFO:
            PortyScanner is a TCP-based port scanning tool designed for learning,
            testing, and basic network reconnaissance.

            WHAT THIS SCRIPT CAN DO:
            - Scan a target IPv4 address for open TCP ports
            - Perform a QUICK SCAN using common ports (Top Ports list)
            - Perform a FULL SCAN on a custom user-defined port range
            - Identify likely services running on open ports (HTTP, SSH, FTP, etc.)
            - Attempt banner grabbing to collect service/version information
            - Display scan results in a clean table format
            - Save discovered open ports and banners to a file (open_ports.txt)
            - Measure and display scan execution time

            HOW IT WORKS:
            - Uses TCP sockets (AF_INET + SOCK_STREAM) to test ports
            - Attempts a TCP connection to each port using connect_ex()
            - A return value of 0 means the port is OPEN
            - Non-zero return values indicate CLOSED or FILTERED ports
            - QUICK SCAN uses multithreading for faster results
            - FULL SCAN checks ports sequentially for full control
            - Banner grabbing attempts to read service responses after connection

            NOTE:
            Some services may not return banners unless protocol-specific
            communication is used. 

          {RESET}""")
    print(f"{CYAN} ===================================================================================================\n{RESET}")

    input("Press Enter to return to the main menu...")
#-------------------------------------------------------------------------------------------------------------------------------
def tcp_port(ip, port, timeout=0.3):
    service = COMMON_SERVICES.get(port, 'Unknown Service') # GUESSING service based on common ports

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout) # Set socket timeout

    t0 = time.perf_counter() # high precision timer to calculate RTT
    try:
        result = s.connect_ex((ip, port))
        rtt_ms = (time.perf_counter() - t0) * 1000  # RTT in milliseconds

        if result == 0:
            banner = grab_banner(ip, port)
            return (port, "open", "syn-ack", round(rtt_ms, 2), service, banner)

        # common CLOSED code on many systems
        if result == 111:
            return (port, "closed", "rst", round(rtt_ms, 2), service, "N/A")
    
        return (port, "close/filtered", f"err-{result}", round(rtt_ms, 2), service, "N/A")
    except socket.timeout:
        rtt_ms = (time.perf_counter() - t0) * 1000  # RTT in milliseconds
        return (port, "filtered", "timeout", round(rtt_ms, 2), service, "N/A")
    
    except Exception as e:
        rtt_ms = (time.perf_counter() - t0) * 1000
        return (port, "error", type(e).__name__, round(rtt_ms, 2), service, "N/A")
    finally:
        s.close()
#-------------------------------------------------------------------------------------------------------------------------------
# Quick Scan Function
def QUICK_Option():
    
    ipaddress = input(f"{GREEN}Enter IP address to scan: {RESET}")
    first_port = 1
    end_port = 1024

    print(f"[+] Target IP: {ipaddress}")
    print(f"[+] Port Range: {first_port} to {end_port}")
    print(f"[*] Scan Started...\n")

    open_ports = []  # List to hold open ports

    workers = 200 # Number of threads for scanning
    timeout = 0.3 # Timeout for socket connections

    results = []

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(tcp_port, ipaddress, port, timeout) for port in TOP_100_PORTS]

        for f in  as_completed(futures):
            results.append(f.result())

    open_results = [res for res in results if res[1] == "open"]

    if open_results:
        rows = []
        for port, state, reason, rtt, service, banner in sorted(open_results, key=lambda x: x[0]):
            version = banner.splitlines()[0] if banner else "UNKNOWN"
            rows.append([port, state, reason, f"{rtt} ms", service, version])
        
        print(tabulate(rows, headers=["PORT", "STATE", "REASON", "RTT", "SERVICE", "VERSION|BANNER"], tablefmt="git"))


        # save open port to a file 
        with open("open_ports.txt", "w") as file:
            for port, state, reason, rtt,service, banner in sorted(open_results, key=lambda x: x[0]): # write open ports to file
                first_line = banner.splitlines()[0] if banner else "UNKNOWN" # Get first line of banner
                file.write(f"Port: {port}, Service: {service}, Banner: {banner}\n") # Save open ports to file
        print(f"{GREEN}[+] Saved to: {os.path.abspath('open_ports.txt')}{RESET}")
    else:
        print(f"{RED}[-] No open ports found.{RESET}")
    
    input("Press Enter to return to the main menu...")

#-------------------------------------------------------------------------------------------------------------------------------
# Banner Grabbing Function
def grab_banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, port))

        try:
            banner = s.recv(1024)
            s.close()
            return banner.decode(errors="ignore").strip()
        except socket.timeout:
            s.close()
            return "No banner received"
    except Exception:
        return "Connection failed"
#-------------------------------------------------------------------------------------------------------------------------------
# full scan Function
def FULL_Option():
    ipaddress = input(f"{GREEN}Enter IP address to scan: {RESET}")
    first_port = int(input(f"{GREEN}Enter first port number:{RESET} "))
    end_port = int(input(f"{GREEN}Enter last port number:{RESET} "))

    print(f"[+] Target IP: {ipaddress}") # Target IP
    print(f"[+] Port Range: {first_port} to {end_port}") # Port Range
    print(f"[*] Scan Started...\n") # Scan start message
    
    open_ports = []  # List to hold open ports

    workers = 300 # Number of threads for scanning
    timeout = 0.3 # Timeout for socket connections

    ports = range(first_port, end_port + 1)

    results = []

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(tcp_port, ipaddress, port, timeout) for port in ports]

        for f in  as_completed(futures):
            results.append(f.result())

    open_results = [res for res in results if res[1] == "open"]

    if open_results:
        rows = []
        for port, state, reason, rtt, service, banner in sorted(open_results, key=lambda x: x[0]):
            version = banner.splitlines()[0] if banner else "UNKNOWN"
            rows.append([port, state, reason, f"{rtt} ms", service, version])
        
        print(tabulate(rows, headers=["PORT", "STATE", "REASON", "RTT", "SERVICE", "VERSION|BANNER"], tablefmt="git"))


        # save open port to a file 
        with open("open_ports.txt", "w") as file:
            for port, state, reason, rtt,service, banner in sorted(open_results, key=lambda x: x[0]): # write open ports to file
                first_line = banner.splitlines()[0] if banner else "UNKNOWN" # Get first line of banner
                file.write(f"Port: {port}, Service: {service}, Banner: {banner}\n") # Save open ports to file
        print(f"{GREEN}[+] Saved to: {os.path.abspath('open_ports.txt')}{RESET}")
    else:
        print(f"{RED}[-] No open ports found.{RESET}")
    
    input("Press Enter to return to the main menu...")
#-------------------------------------------------------------------------------------------------------------------------------
def ping_helper(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]

    try:
        subprocess.run(command, capture_output=True, text=True, check=True)
        return (host, "UP")
    except subprocess.CalledProcessError:
        return (host, "DOWN")
    except Exception as e:
        return (host, "ERROR")
#-------------------------------------------------------------------------------------------------------------------------------
def PING_TEST():
    print(f"{CYAN}=== PING TEST ==={RESET}")
    target = input(f"{GREEN}Enter IP address or hostname to ping: {RESET}").split(",")

    target = [t.strip() for t in target] # Strip whitespace from targets
    workers = min(20, len(target)) # Limit threads to 20 or number of targets

    print(f"\n{GREEN}Pinging {target}...{RESET}\n")

    results = []

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(ping_helper, t) for t in target]

        for f in as_completed(futures):
            results.append(f.result())
    
    # display results
    for host, status in results:
        if status == "UP":
            print(f"{GREEN}[+] {host} is UP{RESET}")
        elif status == "DOWN":
            print(f"{RED}[-] {host} is DOWN{RESET}")
        else:
            print(f"{YELLOW}[!] {host} ping ERROR: {status}{RESET}")
    input("\nPress Enter to return to the main menu...")
#-------------------------------------------------------------------------------------------------------------------------------
# Exit Function
def EXIT_Option():
    print("Exiting the program.")
    exit()
#-------------------------------------------------------------------------------------------------------------------------------
# Main loop
if __name__ == "__main__":
    while True:
        main_menu()

"""
    OPEN PORTS FOR TESTING:
    python3 - << 'EOF'
    import socket
    s = socket.socket()
    s.bind(("0.0.0.0", 4444))
    s.listen(1)
    print("Listening on port 4444")
    conn, addr = s.accept()
    EOF

    python3 - << 'EOF'
    import socket
    s = socket.socket()
    s.bind(("0.0.0.0", 8080))
    s.listen(1)
    print("Listening on port 8080")
    conn, addr = s.accept()
    EOF

    python3 -m http.server 8000

    sudo systemctl start ssh
"""
