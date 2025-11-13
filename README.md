# Simple MAC Address Changer

A simple Python script to change the MAC address of network interfaces on Linux.


WARNING: This software is provided for educational and authorized testing purposes only. The author disclaims any liability for misuse. Do not use this software to access, interfere with, or damage systems you do not own or have explicit permission to test. Using this software in an unlawful manner is solely the responsibility of the user.

---

# Description

This script allows you to select a network interface and assign a new MAC address in the format `AA:BB:CC:DD:EE:FF`. It works for physical Ethernet and Wi-Fi interfaces. Virtual interfaces like Docker or VPN interfaces are not supported.

---

# Requirements

- Python 3
- Linux system
- Root privileges (run with `sudo`)
- `ifconfig` installed 

---

# Usage
Run the script with root privileges:

sudo python 'Simple MAC Address Changer'.py

Select the interface you want to change.

Enter a new MAC address in the correct format: AA:BB:CC:DD:EE:FF 

