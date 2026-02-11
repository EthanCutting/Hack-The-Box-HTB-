"""
    PoryScanner.menu
    Created_Date: 6/02/26
"""
import shutil
import ipaddress
from tabulate import tabulate
from colorama import init, Fore, Back
init(autoreset=True)

from .banner import banner_sections
from .config import PINK, TOOL_NAME, VERSION, AUTHOR, GREEN, RED, CYAN, YELLOW, RESET
from .scanner import quick_scan, full_scan
from .ping import ping_test
from .utils import save_open_results, clear_screen, boxed_center, mid_input, mid_print, box_inner_width, mid_inline_input
from collections import Counter
from .info import show_info
from .logger import log_event, summarize_scan, summarize_ping, log_error
from .logger_error import log_error

def is_valid_ipv4(ip: str) -> bool:
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False
    
def ui_panel(title: str, lines: list[str], width: int):
    panel = [f"{CYAN}{title}{RESET}", ""] + lines
    print(boxed_center(panel, padding=2, width=width, bg=Back.BLACK, fg=Fore.WHITE))

def ui_error(lines, width: int):
    if isinstance(lines, str):
        lines = [lines]
    print(boxed_center(lines, padding=2, width=width, bg=Back.BLACK, fg=Fore.LIGHTRED_EX))
    print()

def ui_tit_panel(title: str, pairs: list[tuple[str, str]], width: int):
    key_w = max(len(k) for k, _ in pairs)
    lines = [f"{CYAN}{title}{RESET}", ""]
    for k, v in pairs:
        lines.append(f"{GREEN}[+] {k.ljust(key_w)} : {CYAN}{v}{RESET}")
    print(boxed_center(lines, padding=2, width=width, bg=Back.BLACK, fg=Fore.WHITE))

def debug_summary(results):
    counts = Counter(r[1] for r in results)
    print("[*] Scan counts:", dict(counts))

def show_results(results):
    open_results = [r for r in results if r[1] == "open"]
    if not open_results:
        print(f"{RED}No open ports found.{RESET}")
        return  
    
    rows = []

    for port, state, reason, rtt, service, banner in sorted(open_results, key=lambda x: x[0]):
        version = banner.splitlines()[0] if banner else "UKNOWN-VERSION"
        rows.append([port, state, reason, f"{rtt} ms", service, version])
    
    table = tabulate(
            rows,
            headers=["Port", "State", "Reason", "RTT", "Service", "Version"],
            tablefmt="git"
    )

    # center it using the boxed_center
    tables_lines = table.splitlines()
    print(boxed_center(tables_lines, padding=1, bg=Back.BLACK, fg=Fore.WHITE))

    # save results to file
    path = save_open_results(open_results)
    mid_print(f"{GREEN}[+] Saved to: {path}{RESET}")
    print()
    mid_input(f"{GREEN}Press Enter to continue...{RESET}")

def info_screen():
    clear_screen()

    logo, welcome = banner_sections()
    banner_w = box_inner_width(logo, padding=2)

    print(boxed_center(logo, padding=2, bg=Back.BLACK, fg=Fore.CYAN))
    print()
    print(boxed_center(welcome, padding=1, width=banner_w, bg=Back.BLACK, fg=Fore.CYAN))
    print()

    mid_print(f"\n{CYAN}=== {TOOL_NAME} V{VERSION} ==={RESET}")
    mid_print(f"{GREEN}[+] Tool    : {TOOL_NAME}{RESET}")
    mid_print(f"{GREEN}[+] Version : {VERSION}{RESET}")
    mid_print(f"{GREEN}[+] Author  : {AUTHOR}{RESET}")
    mid_input(f"{GREEN}Press Enter to return to the main menu...{RESET}")

def main_menu():
    while True:
        clear_screen()

        logo, welcome = banner_sections()
        banner_w = box_inner_width(logo, padding=2)

        # logo box
        print(boxed_center(logo, padding=2, width=banner_w, bg=Back.BLACK, fg=Fore.WHITE))
        print()
        print(boxed_center(welcome, padding=1, width=banner_w, bg=Back.BLACK, fg=Fore.CYAN))
        print()

        menu_lines = [
            "",
            f"{CYAN}=== {TOOL_NAME} V{VERSION} ==={RESET}",
            "",
            f"{YELLOW}1.{RESET} INFO",
            f"{YELLOW}2.{RESET} QUICK SCAN (top ports)",
            f"{YELLOW}3.{RESET} FULL SCAN (custom range)",
            f"{YELLOW}4.{RESET} PING TEST",
            f"{YELLOW}5.{RESET} EXIT",
            "",
            f"{GREEN}Select an option (1-5){RESET}",
        ]

        mid_print(boxed_center(menu_lines, padding=3, width=banner_w, bg=Back.BLACK, fg=Fore.CYAN))
        choice = mid_input("").strip()

        log_event("menu_choice", {"choice": choice})
        mid_print(f"{GREEN}You selected option: {YELLOW}{choice}{RESET}")
     
        #choice = input(center_text(f"{GREEN}Select an option (1-5):{RESET}")).strip()
        # choice 1
        if choice == '1':
            clear_screen()
            log_event("info_view", {})
            logo, welcome = banner_sections()
            banner_w = box_inner_width(logo, padding=2)

            print(boxed_center(logo, padding=2, width=banner_w, bg=Back.BLACK, fg=Fore.WHITE))
            print()
            print(boxed_center(welcome, padding=2, width=banner_w, bg=Back.BLACK, fg=Fore.CYAN))
            print()

            ui_tit_panel(
                f"{TOOL_NAME} V{VERSION}",
                [
                    ("Tool", TOOL_NAME),
                    ("Version", TOOL_NAME),
                    ("Author", TOOL_NAME),
                ],
                width=banner_w
            )
            
            mid_print(f"{CYAN}Mode:{RESET} INFO")
            show_info(show_mode=True)
        
        # choice 2
        elif choice == '2':
            mid_print(f"{GREEN}Mode:{RESET} QUICK SCAN")

            attempts = 0
            max_attempts = 3
            
            while attempts < max_attempts:
                clear_screen()
                ui_panel(
                    "QUICK SCAN",
                    [
                        f"{YELLOW}Example:{RESET} 192.168.1.1",
                        f"{YELLOW}Attempts:{RESET} {attempts}/{max_attempts}",
                    ],
                    width=banner_w
                )

                ip = mid_inline_input(f"{GREEN}Enter target IPv4 address:{RESET}")

                if not is_valid_ipv4(ip):
                    attempts += 1
                    ui_error(
                        [
                            f"{RED}Invalid IPv4 address..{RESET}", 
                            f"{YELLOW}Example:{RESET} 192.168.1.1 {YELLOW}Attempts:{RESET}{attempts}/{max_attempts}{RESET}",
                        ],
                        width=banner_w
                    )
                    print()
                    continue

                # valid ip
                break
            else:
                ui_error(f"{RED}Too many invalid attempts. Returning to menu.", width=banner_w)
                log_event(f"invalid_ip_quick_scan", {"attempts": attempts})
                mid_input(f"{GREEN}Press Enter to return to the main menu...{RESET}")
                continue

            # RUN SCAN
            log_event("scan_start", {"mode": "quick", "target": ip})

            try:
                mid_print("[*] Scan Started...")
                results = quick_scan(ip)
                show_results(results)
                log_event("scan_end", {"mode": "quick", "target": ip, **summarize_scan(results)})
            except Exception as e:
                log_error("quick_scan", e, {"target": ip})
                ui_error(f"{RED}[!] SCAN ERROR: {e}{RESET}", width=banner_w)
            

            mid_input(f"{GREEN}Press ENter to return to the main menu...{RESET}")

        # choice 3
        elif choice == '3':
            mid_print(f"{GREEN}Mode:{RESET} FULL SCAN")

            attempts = 0
            max_attempts = 3

            while attempts < max_attempts:
                clear_screen()
                ui_panel(
                    "FULL SCAN",
                    [
                        f"{GREEN}Example:{RESET} 192.168.1.1",
                        f"{YELLOW}Attempts:{RESET} {attempts}/{max_attempts}",
                    ],
                    width=banner_w

                )

                ip = mid_input(f"{GREEN}Enter IP address to scan:{RESET}").strip()

                if not is_valid_ipv4(ip):
                    attempts += 1
                    ui_error(
                        [
                            f"{YELLOW}Example: 192.168.1.1 {RESET}"
                            f"{YELLOW}Attempts:{RESET}{attempts}/{max_attempts}",
                        ],
                        width=banner_w
                    )
                    continue


                break
            else:
                ui_error(
                    [f"{RED}Too many invalid attempts.{RESET}"],
                    width=banner_w
                )
                log_event("invalid_ip_full_scan", {"attempts": attempts})
                mid_input(f"{GREEN}Press Enter to return to the main menu...{RESET}")
                continue
            
            try:
                start_p = int(mid_input(f"{GREEN}Enter starting port (1-65535):{RESET}").strip())
                end_p = int(mid_input(f"{GREEN}Enter ending port (1-65535):{RESET}").strip())
            except ValueError:
                mid_print(f"{RED}Ports must be numbers. Returning to menu.{RESET}")
                log_event("invalid_port_input", {"target": ip})
                mid_input(f"{GREEN}Press Enter to return to the main menu...{RESET}")
                continue
            if not (1 <= start_p <= 65535 and 1 <= end_p < 65535):
                mid_print(f"{RED}Ports must be between 1 and 65535. Returing to men.{RESET}")
                log_event("port_out_of_range", {"target": ip, "start_port": start_p, "end_port": end_p})
                mid_input(f"{GREEN}Press Enter to return to the main menu...{RESET}")
                continue
            if start_p > end_p:
                mid_print(f"{RED}Ports must be between 1 and 65535. Returing to men.{RESET}")
                log_event("port_out_of_range", {"target": ip, "start_port": start_p, "end_port": end_p})
                mid_input(f"{GREEN}Press Enter to return to the main menu...{RESET}")
                continue

            # run scan
            log_event("scan_start", {"mode": "full", "target": ip, "start_port": start_p, "end_port": end_p})

            try:
                mid_print("[*] Scan Started...")
                results = full_scan(ip, start_p, end_p)
                show_results(results)
                log_event("scan_end", {"mode": "full", "target": ip, "start_port": start_p, "end_port": end_p, **summarize_scan(results)})
            except Exception as e:
                log_error("full_scan", e, {"target": ip, "start_port": start_p, "end_port": end_p})
                mid_print(f"{RED}[!] SCAN ERROR: {e}{RESET}")

            mid_input(f"{GREEN}Press Enter to return to the main menu...{RESET}")

        # choice 4
        elif choice == '4':
            mid_print(f"{GREEN}Mode:{RESET} PING TEST")

            attempts = 0
            max_attempts = 3

            while attempts < max_attempts:
                clear_screen()
                ui_panel(
                    "PING TEST",
                    [
                        f"{YELLOW}Example:{RESET} 192.168.1.1",
                        f"{YELLOW}Attempts:{RESET} {attempts}/{max_attempts}"
                    ],
                    width=banner_w
                )

                raw = mid_input(f"{GREEN}Enter IP addresses to ping:{RESET}").strip()
            
                if not raw:
                    attempts += 1
                    ui_error(
                        [
                            f"{RED}No IP address provided.{RESET}",
                            f"{YELLOW}Example:{RESET} 8.8.8.8 1.1.1.1",
                            f"{YELLOW}Attempts:{RESET} {attempts}/{max_attempts}",
                        ],
                        width=banner_w
                    )
                    continue
                    
                targets = [t.strip() for t in raw.replace(",", " ").split() if t.strip()]

                if not targets:
                    attempts += 1
                    ui_error(
                        [
                            f"{RED}Invalid IPv4 address..{RESET}",
                            f"{YELLOW}Example:{RESET} 192.168.1.1",
                            f"{YELLOW}Attempts:{RESET} {attempts}/{max_attempts}",
                        ],
                        width=banner_w
                    )
                    continue

                break
            
            else:
                ui_error(
                    [f"{RED}Too Many invalid attempts{RESET}"],
                    width=banner_w
                )
                log_event("ping_input_failed", {"attempts": attempts})
                mid_input(f"{GREEN}Press Enter to return to the main menu...{RESET}")
                continue

                # LOG START
            log_event("ping_test_start", {"targets": targets})

            try:
                results = ping_test(targets)
            except Exception as e:
                log_error("ping_test", e, {"target": targets})
                mid_print(f"{RED}[!] Ping test error: {e}{RESET}")
                mid_input(f"{GREEN}Press Enter to return to the main menu...{RESET}")
                continue

                # LOG END
            summary = summarize_ping(results)
            log_event("ping_end", summarize_ping(results))
                    
                # display
            mid_print(f"{CYAN}=== Ping Test Results ==={RESET}")

            if not results:
                mid_print(f"{RED}No results to display.{RESET}")
            else:
                for host, status in results:
                    if status == "UP":
                        mid_print(f"{YELLOW}[+] {host} is UP{RESET}")
                    elif status == "DOWN":
                        mid_print(f"{RED}[-] {host} is DOWN{RESET}")
                    else:
                        mid_print(f"{YELLOW}[?] {host} status is ERROR!!!!!{RESET}")

            mid_input(f"{GREEN}Press Enter to return to the main menu...{RESET}")
            
        # choice 5
        elif choice == '5':
            mid_print(f"{GREEN}Mode:{RESET} EXIT")
            log_event("exit", {"tool": TOOL_NAME, "version": VERSION})
            mid_print(f"{PINK}Exiting {TOOL_NAME}. Goodbye!{RESET}")
            log_event("session_end", {"tool": TOOL_NAME, "version": VERSION})
            break
        else:
            mid_print(f"{RED}Invalid choice. Please select a valid option.{RESET}")
            mid_input("Press Enter to continue...")