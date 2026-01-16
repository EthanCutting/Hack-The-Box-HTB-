
""""
    PoryScanner 0.1
    By Ethan PP Cuting
"""
# 
import socket
from colorama import Fore, Style, init
init(autoreset=True)

VERSION = "0.1"
TOOL_NAME = "PortyScanner"
AUTHOR = "Ethan PP Cuting"

GREEN = Fore.GREEN
RED = Fore.RED
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
RESET = Style.RESET_ALL
BLUE = Fore.BLUE
WHITE = Fore.WHITE
BLACK = Fore.BLACK

# Main Menu
def main_menu():
    # Display menu options
    print(f"\n{CYAN}=== {TOOL_NAME} V{VERSION} ==={RESET}") #
    print(f"{YELLOW}1.{RESET} INFO")
    print(f"{YELLOW}2.{RESET} Scan POrts")
    print(f"{YELLOW}3.{RESET} EXIT")
    choice = input(f"{GREEN}Select an option:{RESET}")
    # Handle user choice
    if choice == '1':
        option_one()
    elif choice == '2':
        option_two()
    elif choice == '3':
        option_three()
        exit()
    # Handle invalid choice
    else:
        print(f"{RED}[-] Invalid choice. Please try again.{RESET}")
        input("Press Enter to continue...")
        
# Functions for each menu option
def option_one():
    # Display tool information
    print(r"""
        ██████╗  ██████╗ ██████╗ ██╗   ██╗
        ██╔══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝
        ██████╔╝██║   ██║██████╔╝ ╚████╔╝ 
        ██╔═══╝ ██║   ██║██╔══██╗  ╚██╔╝  
        ██║     ╚██████╔╝██║  ██║   ██║   
        ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝ 
    """)
    print(f"\n{CYAN}=== {TOOL_NAME} V{VERSION} ==={RESET}") #
    print(f"{GREEN}[+] Tool    :   {TOOL_NAME}{RESET}") 
    print(f"{GREEN}[+] Version :   {VERSION}{RESET}")
    print(f"{GREEN}[+] Author  :   {AUTHOR}{RESET}")
    print(f"{GREEN}[+] GitHub  :   https://github.com/EthanCutting/Hack-The-Box-HTB-/blob/main/Scripts/PoryScanner.py{RESET} ")
    print(f"{CYAN} ==================================================================================================\n{RESET}")
    # Additional info
    print(f"""{YELLOW}
          INFO: This is a basic port scanner script.
          It allows you to scan a range of ports on a specified IP address.
          {RESET}""")
    print(f"{CYAN} ===================================================================================================\n{RESET}")

    input("Press Enter to return to the main menu...")
    
# Scan Ports Function
def option_two():
    ipaddress = input("Enter IP address to scan: ")
    first_port = int(input("Enter first port number: "))
    end_port = int(input("Enter last port number: "))

    print(f"[+] Target IP: {ipaddress}")
    print(f"[+] Port Range: {first_port} to {end_port}")
    print(f"[*] Scan Started...\n")
    
    open_ports = []  # List to hold open ports

    # Scan ports in the specified range
    print(f"Scanning ports from {first_port} to {end_port} on {ipaddress}...")
    for port in range(first_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create a TCP socket
        sock.settimeout(1) # Set timeout for socket
        
        result = sock.connect_ex((ipaddress, port)) # Attempt to connect to the port
        # Check if the port is open
        if result == 0:
            print(f"Port {port}: Open")
            open_ports.append(port)  # Add open port to the list
        sock.close() # Close the socket

    print("Scanning complete.")

    if open_ports:
        print("[+] Open Ports: ", ", ".join(map(str, open_ports)))
    else:
        print("[-] No open ports found.")

    input("Press Enter to return to the main menu...")
    
# Exit Function
def option_three():
    print("Exiting the program.")
    exit()

# Main program loop
if __name__ == "__main__":
    while True:
        main_menu()


""""
    INFO:
    Defing colors
        GREEN = Fore.GREEN
        RED = Fore.RED
        CYAN = Fore.CYAN
        YELLOW = Fore.YELLOW
        MAGENTA = Fore.MAGENTA
        RESET = Style.RESET_ALL
        BLUE = Fore.BLUE
        WHITE = Fore.WHITE
        BLACK = Fore.BLACK

"""
