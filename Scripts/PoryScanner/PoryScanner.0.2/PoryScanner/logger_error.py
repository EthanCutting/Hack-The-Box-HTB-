"""
    PoryScanner.logger_error
    Created_Date: 10/02/26
"""
import os
import traceback
from datetime import datetime

LOG_DIR = "logs"
ERROR_FILE = os.path.join(LOG_DIR, "error.log")

def log_error(error_type: str, exc: Exception, context: dict | None = None):
    os.makedirs(LOG_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(ERROR_FILE, "a", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write(f"Time    :     {timestamp}")
        f.write(f"ERROR Type    :   {error_type}")

        if context:
            f.write("context :\n")
            for k, v in context.items():
                f.write(f"  - {k}: {v}\n")
        
        f.write("\nException:\n")
        f.write("".join(traceback.format_exception(type(exc), exc, exc.__traceback__)))
        f.write("\n")