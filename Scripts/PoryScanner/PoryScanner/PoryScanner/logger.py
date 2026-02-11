"""
    PoryScanner.logger
    Created_Date: 7/02/26
"""
import json 
import os
from datetime import datetime
from typing import Any, Dict, Optional

LOG_DIR = "logs"

def _now_iso() -> str:
    return datetime.now().isoformat(timespec='seconds')

def  _ensure_log_dir(base_dir: str = LOG_DIR) -> str:
    os.makedirs(base_dir, exist_ok=True)
    return base_dir

def _log_path(base_dir: str = LOG_DIR) -> str:
    date_str = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(base_dir, f"{date_str}.jsonl")

def log_event(event: str, data: Optional[Dict[str, Any]] = None, base_dir: str = LOG_DIR) -> None:
    _ensure_log_dir(base_dir)
    path = _log_path(base_dir)

    payload = {
        "timestamp": _now_iso(),
        "event": event,
        "data": data or {}
    }

    with open(path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")
    return path

def log_error(where: str, exc: Exception, extra: Optional[Dict[str, Any]] = None, base_dir: str = LOG_DIR) -> None:
    data = {"where": where, "error": str(exc)}
    if extra:
        data.update(extra)
    return log_event("error", data, base_dir)

def summarize_scan(results: Dict[str, Any]) -> str:
    total = len(results) if results else 0
    open_ports = []
    for r in results or []:
        try:
            port, state, reason, rtt, service, banner = r
            if state == "open":
                open_ports.append(port)
        except Exception:
            pass
    
    return {
        "total": total,
        "open_count": len(open_ports),
        "open_ports": sorted(open_ports)
    }

def summarize_ping(results) -> Dict[str, Any]:
    up = 0
    down = 0
    err = 0
    hosts = []

    for host, status in results:
        status = str(status).upper()
        if status == "UP":
            up += 1
        elif status == "DOWN":
            down += 1
        else:
            err += 1
        hosts.append({"host": host, "status": status})
    
    return {
        "up": up,
        "down": down,
        "error": err,
        "hosts": hosts
    }