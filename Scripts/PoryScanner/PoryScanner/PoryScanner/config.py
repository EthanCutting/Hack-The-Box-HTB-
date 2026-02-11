"""
    PoryScanner.config
    Created_Date: 6/02/26
"""
from colorama import Fore, Style, Back

# Tool Information
VERSION = "0.2"
TOOL_NAME = "PoryScanner"
AUTHOR = "Ethan PP Cuting"

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
PINK = Fore.LIGHTMAGENTA_EX

# text 
PRIMARY = Fore.CYAN
ACCENT  = Fore.YELLOW
MUTED   = Fore.BLUE
ERROR   = Fore.RED
SUCCESS = Fore.GREEN

# Panels
PANEL_BG = Back.BLACK
PANEL_FG = Fore.WHITE
RESET = Style.RESET_ALL

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