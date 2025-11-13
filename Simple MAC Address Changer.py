import subprocess
import re
import os
import sys
import time


def clear_terminal():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')  

        print("\033[2J\033[H", end="")

        if not sys.stdout.isatty():
            print("\n" * 100)
    except Exception:
        print("\n" * 100)

interfaces = [
    "eth0", "eth1", "eth2",
    "wlan0", "wlan1",
    "enp0s3", "enp3s0", "enp5s0",
    "wlp2s0", "wlp3s0", "wlp4s0",
]

while True:
    print("Choose A Network Interfaces:\n")
    for i, iface in enumerate(interfaces, 1):
        print(f"  {i}. {iface}")
    try:
        pick = int(input("\nSelect an interface: "))
        if 1 <= pick <= len(interfaces):
            interface = interfaces[pick - 1]
            break
        else:
            clear_terminal()
            print("Please enter a valid interface.")
            time.sleep(1)
            clear_terminal()
    except ValueError:
        print()
        print("Please enter a valid interface.")
        time.sleep(1)
        clear_terminal()

while True:
    mac = input("Enter new MAC address (AA:BB:CC:DD:EE:FF format): ").strip()
    if not re.fullmatch(r"([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}", mac):
        print()
        clear_terminal()
        print("Invalid MAC Format Try Again\n")
        time.sleep(1)
        clear_terminal() 
    else:
        break

print()
print(f"Changing MAC Address for {interface} to {mac}")


subprocess.run(f"ifconfig {interface} down", shell=True)
subprocess.run(f"ifconfig {interface} hw ether {mac}", shell=True)
subprocess.run(f"ifconfig {interface} up", shell=True)




