"""
    PoryScanner.scanner
    Created_Date: 6/02/26
"""
import socket 
import time
import ssl
from concurrent.futures import ThreadPoolExecutor as Thread, as_completed

from .utils import mid_status
from .config import COMMON_SERVICES, TOP_100_PORTS

def _recv_some(sock: socket.socket, max_bytes=4096) -> str:
    try:
        data = sock.recv(max_bytes)
        return data.decode("utf-8", errors="ignore").strip()
    except Exception:
        return ""
    
def _http_probe(sock: socket.socket, host: str) -> str:
    req = (
        f"GET / HTTP/1.1\r\n"
        f"Host: example.com\r\n"
        f"User-Agent: PoryScanner/0.2\r\n"
        f"Connection: close\r\n\r\n"
    ).encode()

    try:
        sock.sendall(req)
        resp = _recv_some(sock, 8192)
        if not resp:
            return "No HTTP response"
        
        lines = resp.splitlines()
        status = lines[0] if lines else "Unknown HTTP response"

        server = ""
        for line in lines:
            if line.lower().startswith("server:"):
                server = line
                break

        return f"{status} | {server}".strip(" |")
    except Exception:
        return "No HTTP BANNER"
    
def grab_banner(host: str, port: int, timeout: float = 0.1) -> str:
    text_greeting_ports = {21, 22, 23, 25, 110, 143, 3306}
    http_ports = {80, 8080, 8000, 8888}
    https_ports = {443, 8443}

    try:
        # tcp connect
        with socket.create_connection((host, port), timeout=timeout) as sock:
            sock.settimeout(timeout)

            # SSH / FTP / SMTP/ IMAP / Telnet 
            if port in text_greeting_ports:
                banner = _recv_some(sock, 4096)
                return banner if banner else "No banner"
            
            # HTTP
            if port in http_ports:
                banner = _http_probe(sock, host)
                return banner if banner else "No HTTP banner"
            
            # HTTPS
            if port in http_ports:
                ctx = ssl.create_default_context()
                with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                    ssock.settimeout(timeout)
                    banner = _http_probe(ssock, host)
                    return banner if banner else "No HTTPS banner"
                
        # default attempt
        banner = _recv_some(sock, 2048)
        return banner if banner else "No banner"
    except (ConnectionRefusedError, TimeoutError, socket.timeout):
        return "No banner (connection issue)"
    except ssl.SSLError:
        return "TLS handshake failed"
    except Exception:
        return "Connection error"


def tcp_port(ip, port, timeout=0.3):
    service = COMMON_SERVICES.get(port, 'Unknown Service') # GUESSING service based on common ports

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout) # Set socket timeout

    t0 = time.perf_counter() # high precision timer to calculate RTT
    try:
        result = s.connect_ex((ip, port))
        rtt_ms = (time.perf_counter() - t0) * 1000  # RTT in milliseconds

        if result == 0:
            banner = grab_banner(ip, port, timeout=0.8)
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

def run_scan(ip, ports, workers=200, timeout=0.3):
    results = []
    total = len(ports)
    completed = 0

    start_time = time.time()

    with Thread(max_workers=workers) as ex:
        futures = [ex.submit(tcp_port, ip, port, timeout) for port in ports]

        for f in as_completed(futures):
            results.append(f.result())
            completed += 1

            elapsed = time.time() - start_time
            avg = elapsed / completed
            remaining = total - completed
            eta = remaining * avg

            percent = (completed / total) * 100

            status = (
                f"[*] Scanning: {completed}/{total}"
                f"({percent:.1f}%) | ETA: {eta:.1f}s"
            )
            mid_status(status)

        print() # move to next line after scan completes
        return results

def quick_scan(ip):
    return run_scan(ip, TOP_100_PORTS, workers=150, timeout=1.2)

def full_scan(ip, start_port, end_port):
    ports = range(start_port, end_port + 1)
    return run_scan(ip, ports, workers=200, timeout=1.8)