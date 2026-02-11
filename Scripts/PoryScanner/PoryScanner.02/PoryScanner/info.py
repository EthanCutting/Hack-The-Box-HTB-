"""
    PoryScanner.info
    Created_Date: 6/02/26
"""
from colorama import Fore, Style, Back
from .banner import banner_sections
from .config import TOOL_NAME, VERSION, AUTHOR, GREEN
from .utils import boxed_center, mid_input, mid_print, clear_screen, box_inner_width

CYAN = Fore.CYAN
RESET = Style.RESET_ALL

def show_info(show_mode=False):
    clear_screen()
    
    logo, welcome = banner_sections()
    banner_w = box_inner_width(logo, padding=2)

    print(boxed_center(logo, padding=2, width=banner_w, bg=Back.BLACK, fg=Fore.CYAN))
    print()
    print(boxed_center(welcome, padding=1, width=banner_w, bg=Back.BLACK, fg=Fore.CYAN))
    print()

    header_lines = [
        f"{CYAN}=== {TOOL_NAME} V{VERSION} ==={RESET}",
    ]
    mid_print(boxed_center(header_lines, padding=1, bg=Back.BLACK, fg=Fore.CYAN))

    mid_print(f"{GREEN}[+] Tool    : {TOOL_NAME}{RESET}")
    mid_print(f"{GREEN}[+] Version : {VERSION}{RESET}")
    mid_print(f"{GREEN}[+] Author  : {AUTHOR}{RESET}")
    print()

    if show_mode:
        mid_print(f"{GREEN}Mode:{RESET} INFO")
        print()

    info_lines = [
        "INFO:",
        "  Welcome to PoryScanner V0.2, this used to be a messy 300+ lines script",
        "  but I cleaned it up, please let me know what you think and let me know what",
        "  functions to add next."
        "  PortyScanner is a TCP port scanning tool, I built for myself <3,",
        "  and basic network reconnaissance, will be doing updates, this is "
        "  patch v0.2.",
        "",
        "FEATURES:",
        "  - QUICK SCAN: scans Top Ports list using threads ",
        "  - FULL SCAN: do whatever ranges you want",
        "  - Service guessing (HTTP, SSH, FTP, DNS, etc.) from common port mapping in config.py",
        "  - Banner grabbing attempts to collect version/info",
        "  - Results printed in a clean table (PORT / STATE / RTT / SERVICE / BANNER)",
        "  - Saves findings to: a .txt",
        "  - Shows total scan time",
        "",
        "HOW IT WORKS (simple):",
        "  - Uses TCP sockets (AF_INET + SOCK_STREAM)",
        "  - Connect to each port with connect_ex()",
        "  - return = 0  -> OPEN",
        "  - return != 0 -> CLOSED / FILTERED (depends on firewall/network)",
        "  - QUICK SCAN uses multithreading to speed things up",
        "  - FULL SCAN is usually sequential (easier to control)",
        "",
        "Still IN WORKS!:",
        "  This is only update v0.2, still in works ",
    ]

    mid_print(boxed_center(info_lines, padding=1, bg=Back.BLACK, fg=Fore.CYAN))
    print() 

    mid_input(f"{GREEN}Press Enter to return to the main menu...{Style.RESET_ALL}")