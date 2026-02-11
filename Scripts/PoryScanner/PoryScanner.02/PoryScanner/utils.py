"""
    PoryScanner.utils
    Created_Date: 6/02/26
"""
import os
import re
import shutil
from colorama import Fore, Back, init, Style
#from .menu import ui_error
init(autoreset=True)

RESET = Style.RESET_ALL
_ansi_re = re.compile(r"\x1b\[[0-9;]*m")

def _normalizse_lines(lines):
    if lines is None:
        return [""]
    if isinstance(lines, str):
        return [lines]
    
    out = []
    for item in lines:
        if item is None:
            continue
        if isinstance(item, str):
            out.append(item)
        elif isinstance(item, (list, tuple)):
            for sub in item:
                if sub is None:
                    continue
                out.append(str(sub))
        else:
            out.append(str(item))
    return out if out else [""]

RAINBOW = [
    Fore.LIGHTRED_EX,
    Fore.LIGHTYELLOW_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTMAGENTA_EX
]

def rainbow_text(text: str) -> str:
    out = ""
    i = 0
    for ch in text:
        if ch != " ":
            out += RAINBOW[i % len(RAINBOW)] + ch
            i += 1
        else:
            out += ch
    return out + Style.RESET_ALL

def mid_input(prompt: str) -> str:
    width = shutil.get_terminal_size().columns

    pad_prompt = max(0, (width - visible_length(prompt)) // 2)
    print(" " * pad_prompt + prompt)

    pad_input = max(0, (width - 20) // 2)  # Assume input w 20 chars
    return input(" " * pad_input).strip()

def mid_inline_input(prompt: str) -> str:
    width = shutil.get_terminal_size().columns
    pad = max(0, (width - visible_length(prompt) - 15) // 2) 
    return input(" " * pad + prompt).strip()

def mid_print(text: str):
    width = shutil.get_terminal_size().columns
    print(text.center(width))

def clear_screen():
    print("\033[2J\033[H", end="")

def visible_length(text: str) -> int:
    text = str(text)
    return len(_ansi_re.sub("", text))

def mid_status(text: str):
    width = shutil.get_terminal_size().columns
    pad = max(0, (width - visible_length(text)) // 2)
    print("\r" + " " * pad + text, end="", flush=True)

def boxed_center(lines, padding=2, width=None, bg=Back.BLACK, fg=Fore.WHITE, align="left"):
    term_w = shutil.get_terminal_size().columns
    lines = _normalizse_lines(lines)

    # emplty input handling 
    if not lines:
        lines = [""]

    max_w = max(visible_length(line) for line in lines)
    inner_W = width if width is not None else (max_w + padding * 2)
    inner_w = min(inner_W, max(10, term_w - 4))

    top = f"┌{'─' * inner_w}┐"
    bot = f"└{'─' * inner_w}┘"

    box_lines = [top]
    
    for line in lines:
        vis = visible_length(line)
        max_text = inner_w - padding * 2
        for line in lines:
            vis = visible_length(line)
            max_text = inner_W - padding * 2

            if vis > max_text:
                clip_len = max(0, max_text - 3)
                line = line[:clip_len] + "..."
                vis = visible_length(line)

            extra = max_text - vis # fills space
            left_extra = extra // 2
            right_extra = extra - left_extra
            
            if align == "center":
                left_extra = extra // 2
                right_extra = extra - left_extra
            else:
                left_extra = 0
                right_extra = extra

            box_lines.append(
                f"│{bg}{fg}"
                + " " * (padding + left_extra)
                + line
                + " " * (padding + right_extra)
                + f"{RESET}│"
            )
        box_lines.append(bot)

        box_w = inner_w + 2
        left_pad = max(0, (term_w - box_w) // 2)
        return "\n".join((" " * left_pad) + l for l in box_lines)

def box_inner_width(lines, padding=2, width=None) -> int:
    term_w = shutil.get_terminal_size().columns
    lines = _normalizse_lines(lines)

    max_w = max(visible_length(line) for line in lines)
    inner_W = width if width is not None else (max_w + padding * 2)
    inner_w = min(inner_W, max(10, term_w - 4))
    return inner_w    

def mid_text(text: str) -> str:
    width = shutil.get_terminal_size().columns
    return text.center(width)

def save_open_results(open_results, filename="REsults.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for port, state, reason, rtt, service, banner in sorted(open_results, key=lambda x: x[0]):
            f.write(f"Port {port}/tcp: {state} ({reason}), RTT: {rtt}ms, Service: {service}\n")
        return os.path.abspath(filename)