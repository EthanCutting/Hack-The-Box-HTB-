# 🧾 Logging in Python (Professional Scripting)

Logging is essential for real-world Python scripts. It replaces print statements and provides visibility, debugging, and auditing.

---

## Why Logging Matters

Logging allows you to:
- Track script execution
- Debug failures
- Create audit trails
- Monitor long-running scripts

---

## Basic Logging Setup

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Script started")
logging.warning("Suspicious activity detected")
logging.error("File not found")
```

---

## Logging Levels

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

---

## Logging to a File

```python
logging.basicConfig(
    filename="script.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

---

## Best Practices

- Avoid print() in production
- Do not log secrets
- Log meaningful events

---

## Summary

Logging turns scripts into maintainable and auditable tools.
