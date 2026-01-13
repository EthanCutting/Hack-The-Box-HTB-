# 🧩 Python Data Types (Scripting Fundamentals)

This README covers **Python data types**, which are the foundation of all scripting, automation, and problem-solving in Python.

Understanding data types helps you:
- Store information correctly
- Choose the right structure for the task
- Write efficient and readable scripts

---

## 🔢 Numbers

```python
x = 10        # int
y = 3.14      # float
z = 2 + 3j    # complex
```

Used for:
- Counters
- Calculations
- Networking math

---

## 🔤 Strings (`str`)

```python
username = "admin"
ip_address = "192.168.1.1"
```

Common operations:
```python
username.upper()
ip_address.split(".")
"error" in log_line
```

---

## 🔁 Lists

```python
ports = [22, 80, 443]
ports.append(8080)
```

Use when:
- Order matters
- Data changes
- Looping is required

---

## 🧺 Tuples

```python
coordinates = (192, 168, 1, 1)
```

Used for fixed values and constants.

---

## 🧩 Sets

```python
users = {"admin", "root", "guest"}
```

Used for uniqueness and membership testing.

---

## 🗂️ Dictionaries

```python
user = {
    "username": "admin",
    "failed_logins": 5,
    "role": "root"
}
```

Essential for structured data and scripting.

---
