# 🧮 Python Subnet Calculator (Tkinter GUI)

This project is a **Python-based Subnet Calculator** with a simple **Tkinter graphical user interface**, developed while studying **Networking, Switching, and Network Administration** during my Master’s degree.

Subnetting isn’t my favourite topic, so instead of memorising formulas, I built this tool to **automate subnet calculations** and reinforce my understanding in a practical, hands-on way.

---

## 🎯 Project Purpose

The goal of this project was to:

- Reinforce subnetting concepts through hands-on coding  
- Visualise subnet calculations using a GUI  
- Automate common networking tasks such as:
  - Network ID calculation  
  - Usable IP range determination  
  - Broadcast address identification  
- Make subnetting more approachable and less error-prone  

---

## ✨ Features

- ✅ GUI built with **Tkinter**
- ✅ Validates IPv4 addresses and subnet masks
- ✅ Calculates:
  - Network ID  
  - Subnet Mask  
  - Usable host IP range  
  - Broadcast address  
- ✅ Handles invalid input gracefully
- ✅ Uses Python’s `ipaddress` module for validation  

---

## 🧠 How It Works

1. The user enters:
   - An IPv4 address (e.g. `192.168.1.10`)
   - A subnet mask (e.g. `255.255.255.0`)

2. The user clicks **Calculate**

3. The application:
   - Converts the IP address and subnet mask to binary  
   - Applies bitwise operations  
   - Calculates subnet properties  
   - Displays results in the GUI  

---

## 🛠 Technologies Used

- Python 3  
- Tkinter (GUI)  
- `ipaddress` module  
- Bitwise operations  
- Binary-to-decimal conversion  

---

## ▶️ How to Run

### Prerequisites

- Python 3 installed

### Run the program

```bash
python subnet_calculator.py
```

---

## 📁 Project Structure

```text
.
├── subnet_calculator.py
└── README.md
```

---

## 📌 Notes

- Designed for **educational purposes**
- IPv4 only
- GUI intentionally kept simple for clarity

---

## 👤 Author

**Ethan Cutting**  
Master of Cybersecurity  
