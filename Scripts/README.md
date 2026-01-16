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

- ✅ GUI built with Tkinter  
- ✅ Validates IPv4 addresses and subnet masks  
- ✅ Calculates Network ID, usable IP range, and broadcast address  
- ✅ Handles invalid input gracefully  
- ✅ Uses Python’s `ipaddress` module for validation  

---

## ▶️ How to Run

### Prerequisites
- Python 3 installed

### Run the program
```bash
python subnet_calculator.py
```

---

## 📜 Source Code

```python
import tkinter as tk
import ipaddress

def calculate_subnet(ip_address, subnet_mask):
    ip_bin = ''.join(format(int(octet), '08b') for octet in ip_address.split('.'))
    mask_bin = ''.join(format(int(octet), '08b') for octet in subnet_mask.split('.'))
    network_id_bin = ''.join(str(int(ip_bit) & int(mask_bit)) for ip_bit, mask_bit in zip(ip_bin, mask_bin))

    num_hosts = 2 ** (32 - sum(int(bit) for bit in mask_bin))

    usable_range_start = network_id_bin[:-1] + '1'
    usable_range_end = bin(int(network_id_bin, 2) + num_hosts - 2)[2:].zfill(32)

    network_id = '.'.join(str(int(network_id_bin[i:i + 8], 2)) for i in range(0, 32, 8))
    usable_range = '.'.join(str(int(usable_range_start[i:i + 8], 2)) for i in range(0, 32, 8)) + " - " +                    '.'.join(str(int(usable_range_end[i:i + 8], 2)) for i in range(0, 32, 8))

    inverted_mask_bin = ''.join(str(1 - int(mask_bit)) for mask_bit in mask_bin)
    broadcast_address_bin = ''.join(str(int(ip_bit) | int(inverted_mask_bit))
                                    for ip_bit, inverted_mask_bit in zip(network_id_bin, inverted_mask_bin))
    broadcast_address = '.'.join(str(int(broadcast_address_bin[i:i + 8], 2)) for i in range(0, 32, 8))

    return {
        "Network ID": network_id,
        "Usable Range": usable_range,
        "Subnet Mask": subnet_mask,
        "Broadcast Address": broadcast_address
    }

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def is_valid_subnet(subnet):
    try:
        ipaddress.ip_network(subnet, strict=False)
        return True
    except ValueError:
        return False

def show_subnet_details():
    ip_address = ip_entry.get()
    subnet_mask = mask_entry.get()

    if not is_valid_ip(ip_address):
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Invalid IP Address")
        return

    if not is_valid_subnet(subnet_mask):
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Invalid Subnet Mask")
        return

    subnet_details = calculate_subnet(ip_address, subnet_mask)

    result_text.delete(1.0, tk.END)
    for key, value in subnet_details.items():
        result_text.insert(tk.END, f"{key}: {value}\n")

root = tk.Tk()
root.title("Subnet Calculator")
root.configure(bg="light blue")

tk.Label(root, text="IP Address:").pack()
ip_entry = tk.Entry(root, bg="light gray")
ip_entry.pack()

tk.Label(root, text="Subnet Mask:").pack()
mask_entry = tk.Entry(root, bg="light gray")
mask_entry.pack()

tk.Button(root, text="Calculate", command=show_subnet_details).pack()

result_text = tk.Text(root, bg="light gray")
result_text.pack()

root.mainloop()
```

---

## 👤 Author

**Ethan Cutting**  
Master of Cybersecurity
