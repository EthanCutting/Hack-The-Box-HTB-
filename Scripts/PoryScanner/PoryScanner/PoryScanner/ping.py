"""
    PoryScanner.ping
    Created_Date: 7/02/26
"""
import subprocess
import platform
from concurrent.futures import ThreadPoolExecutor as Thread, as_completed

def ping_helper(host):
    param = '-n' if platform.system().lower() == "windows" else '-c'
    cmd = ["ping", param, "1", host]
    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return (host, "UP")
    except subprocess.CalledProcessError:
        return (host, "DOWN")
    except Exception:
        return (host, "ERROR")

def ping_test(targets):
    target = [t.strip() for t in targets if t.strip()] # Strip whitespace from targets
    
    if not targets:
        return []

    workers = min(20, len(target)) # Limit threads to 20 or number of targets
    results = []
    # Thread
    with Thread(max_workers=workers) as executor:
        futures = [executor.submit(ping_helper, t) for t in target]

        for f in as_completed(futures):
            results.append(f.result())

    return results