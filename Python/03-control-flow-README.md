# 🔁 Control Flow in Python

Control flow determines **how your script makes decisions and repeats actions**.

---

## ✅ Conditional Statements

```python
if attempts > 5:
    print("Alert")
elif attempts > 2:
    print("Warning")
else:
    print("Normal")
```

Used for:
- Decision making
- Alerts and thresholds

---

## 🔁 Loops

### For Loop
```python
for port in [22, 80, 443]:
    print(port)
```

### While Loop
```python
retries = 0
while retries < 3:
    retries += 1
```

---

## 🏁 Summary
Control flow allows scripts to react dynamically instead of running line-by-line.
