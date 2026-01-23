
""""
    PoryScanner 0.1
    By Ethan PP Cuting
"""
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
start = time.time()
from tabulate import tabulate
from colorama import Fore, Style, init
init(autoreset=True)
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
# Common services for ports
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
# Main Menu
def main_menu():
    print(rf"""{CYAN}
        ██████╗  ██████╗ ██████╗ ██╗   ██╗
        ██╔══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝
        ██████╔╝██║   ██║██████╔╝ ╚████╔╝ 
        ██╔═══╝ ██║   ██║██╔══██╗  ╚██╔╝  
        ██║     ╚██████╔╝██║  ██║   ██║   
        ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   

        Welcome, friend 
        Ready to scan some ports today?
    {RESET}""")
    # Display menu options
    print(f"\n{CYAN}=== {TOOL_NAME} V{VERSION} ==={RESET}") #
    print(f"{YELLOW}1.{RESET} INFO")
    print(f"{YELLOW}2.{RESET} QUICK SCAN")
    print(f"{YELLOW}3.{RESET} FULL SCAN")
    print(f"{YELLOW}4.{RESET} EXIT")
    choice = input(f"{GREEN}Select an option:{RESET}")
    # Handle user choice
    if choice == '1':
        INFO_Option()
    elif choice == '2':
        QUICK_Option()
    elif choice == '3':
        FULL_Option()
    elif choice == '4':
        EXIT_Option()
        exit()
    # Handle invalid choice
    else:
        print(f"{RED}[-] Invalid choice. Please try again.{RESET}")
        input("Press Enter to continue...")
#-------------------------------------------------------------------------------------------------------------------------------
def welcome_banner():
    print(rf"""{CYAN}
        ██████╗  ██████╗ ██████╗ ██╗   ██╗
        ██╔══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝
        ██████╔╝██║   ██║██████╔╝ ╚████╔╝ 
        ██╔═══╝ ██║   ██║██╔══██╗  ╚██╔╝  
        ██║     ╚██████╔╝██║  ██║   ██║   
        ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   

        Welcome, friend 
        Ready to scan some ports today?
    {RESET}""")
#-------------------------------------------------------------------------------------------------------------------------------
# Functions for each menu option
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
          INFO: This is a basic port scanner script.
          It allows you to scan a range of ports on a specified IP address.{RESET}
            """)
    print(f"{CYAN} ===================================================================================================\n{RESET}")

    input("Press Enter to return to the main menu...")
#-------------------------------------------------------------------------------------------------------------------------------
def T_S_Ports(ip, port, timeout=0.3):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        s.close()

        if result == 0:
            service = COMMON_SERVICES.get(port, 'Unknown Service')
            banner = grab_banner(ip, port)
            return (port, service, banner)
    except Exception:
        return None
    
    return None
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

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(T_S_Ports, ipaddress, port, timeout) for port in TOP_100_PORTS]

        for f in  as_completed(futures):
            result = f.result()
            if result is not None:
                open_ports.append(result)
                print(f"Found open port: {result}")

    # OUTPUT 
    if open_ports:
        print("PORT   SERVICE   VERION|BANNER") # Header
        print("-" * 60) # Separator line

        rows = []

        for port, service, banner in open_ports:
            version = banner.splitlines()[0] if banner else "UNKNOWN"
            rows.append([port, service, version])
        print(tabulate(rows, headers=[
                "PORT", "SERVICE", "VERSION|BANNER"], tablefmt="git"))

        end = time.time() # End time
        print(f"{GREEN}[+] Scan completed in {end - start:.2f} seconds.{RESET}") # Print scan duration

        # save open port to a file 
        with open("open_ports.txt", "w") as file:
            for port, service, banner in open_ports: # Write open ports to file
                file.write(f"Port: {port}, Service: {service}, Banner: {banner}\n") # Save open ports to file
        print(f"{GREEN}[+] Open ports saved to open_ports.txt{RESET}")
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
# Scan Ports Function
def FULL_Option():
    ipaddress = input(f"{GREEN}Enter IP address to scan: {RESET}")
    first_port = int(input(f"{GREEN}Enter first port number:{RESET} "))
    end_port = int(input(f"{GREEN}Enter last port number:{RESET} "))

    print(f"[+] Target IP: {ipaddress}") # Target IP
    print(f"[+] Port Range: {first_port} to {end_port}") # Port Range
    print(f"[*] Scan Started...\n") # Scan start message
    
    open_ports = []  # List to hold open ports

    # Scan ports in the specified range
    print(f"Scanning ports from {first_port} to {end_port} on {ipaddress}...")
    for port in range(first_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create a TCP socket
        sock.settimeout(1) # Set timeout for socket
        
        result = sock.connect_ex((ipaddress, port)) # Attempt to connect to the port
        print(f"{CYAN}\n Scanning complete.\n{RESET}") # Completion message , \n \n for spacing
        print(f"Scanning port {port}/{end_port}", end="\r") 
        # Check if the port is open
        if result == 0:
            service = COMMON_SERVICES.get(port, 'Unknown Service') # Get service name
            banner = grab_banner(ipaddress, port)
            open_ports.append((port, service, banner))  # Add open port to the list

        sock.close() # Close the socket

        # print(f"{CYAN}\n Scanning complete.\n{RESET}") # Completion message , \n \n for spacing

    if open_ports:
        print("PORT   SERVICE   VERION|BANNER") # Header
        print("-" * 60) # Separator line

        rows = []

        for port, service, banner in open_ports:
            version = banner.splitlines()[0] if banner else "UNKNOWN"
            rows.append([port, service, version])
        print(tabulate(rows, headers=["PORT", "SERVICE", "VERSION|BANNER"], tablefmt="git"))

        end = time.time() # End time
        print(f"{GREEN}[+] Scan completed in {end - start:.2f} seconds.{RESET}") # Print scan duration
        
        # Save open ports to a file
        with open("open_ports.txt", "w") as file: 
            for port, service, banner in open_ports: # Write open ports to file
                file.write(f"Port: {port}, Service: {service}, Banner: {banner}\n") # Save open ports to file
        print(f"{GREEN}[+] Open ports saved to open_ports.txt{RESET}")
    else:
        print(f"{RED}[-] No open ports found.{RESET}")

    input("Press Enter to return to the main menu...")
#-------------------------------------------------------------------------------------------------------------------------------
# Exit Function
def EXIT_Option():
    print("Exiting the program.")
    exit()
#-------------------------------------------------------------------------------------------------------------------------------
# Main program loop
if __name__ == "__main__":
    while True:
        main_menu()

