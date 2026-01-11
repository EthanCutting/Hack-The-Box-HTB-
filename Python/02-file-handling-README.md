# 📁 Python File Handling (Scripting Essentials)

This README covers **file handling**, one of the most important skills in Python scripting.

---

## 📖 Opening Files

Recommended approach:
```python
with open("data.txt", "r") as f:
    content = f.read()
```

---

## 📥 Reading Files

Read line-by-line:
```python
with open("log.txt", "r") as f:
    for line in f:
        print(line.strip())
```

---

## 📤 Writing Files

Write (overwrite):
```python
with open("output.txt", "w") as f:
    f.write("Scan complete")
```

Append:
```python
with open("output.txt", "a") as f:
    f.write("\nNew entry")
```

---

## 📄 File Modes

- `r` → Read
- `w` → Write
- `a` → Append
- `rb` → Read binary
- `wb` → Write binary

---

## 🚨 Error Handling

```python
try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
```

---
