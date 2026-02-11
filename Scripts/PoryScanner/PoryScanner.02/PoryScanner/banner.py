"""
    PoryScanner.banner
    Created_Date: 6/02/26
"""
from colorama import Fore, Style
from .utils import rainbow_text

def banner_sections():
    logo = [
        "██████╗  ██████╗ ██████╗ ██╗   ██╗",
        "██╔══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝",
        "██████╔╝██║   ██║██████╔╝ ╚████╔╝ ",
        "██╔═══╝ ██║   ██║██╔══██╗  ╚██╔╝  ",
        "██║     ╚██████╔╝██║  ██║   ██║   ",
        "╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ",
    ]

    welcome = [
        f"{Fore.CYAN}Welcome to PoryScanner v0.2{Style.RESET_ALL}",
        f"{Fore.LIGHTBLUE_EX}Ready to scan? If not, leave me alone....{Style.RESET_ALL}",
    ]

    rainbow_logo = [rainbow_text(line) for line in logo]

    return rainbow_logo, welcome
