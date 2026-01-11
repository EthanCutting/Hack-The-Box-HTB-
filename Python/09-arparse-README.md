# 🖥️ argparse (Command-Line Interfaces)

argparse allows Python scripts to behave like real command-line tools.

---

## Why argparse

- Accept user input safely
- Avoid hard-coded values
- Improve script usability

---

## Basic Example

```python
import argparse

parser = argparse.ArgumentParser(description="Simple scanner")
parser.add_argument("-t", "--target", required=True)
parser.add_argument("-p", "--port", type=int, default=80)

args = parser.parse_args()

print(f"Scanning {args.target} on port {args.port}")
```

---

## Running the Script

```bash
python scan.py -t 192.168.1.10 -p 22
```

---

## Summary

argparse separates scripts from professional tools.
