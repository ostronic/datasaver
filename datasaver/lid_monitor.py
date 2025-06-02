#!/usr/bin/python3

import notify2
import os
import subprocess
import sys
import time

LID_PATH = "/proc/acpi/button/lid"
CHECK_INTERVAL = 2  # seconds

def notify (title, message):
    notify2.init("Datasaver")
    n = notify2.Notification(title, message)
    n.set_timeout(5000)
    n.show()

def get_lid_device():
    try:
        for entry in os.listdir(LID_PATH):
            if entry.startswith("LID") or entry.lower().startswith("lid"):
                return os.path.join(LID_PATH, entry, "state")
    except FileNotFoundError:
        notify("Datasaver", "Lid monitoring not supported on this system")
        print("Lid monitoring not supported on this system.")
        sys.exit(1)
    return None

def read_lid_state(state_file):
    try:
        with open(state_file, 'r') as f:
            content = f.read()
            if "closed" in content.lower():
                return "closed"
            elif "open" in content.lower():
                return "open"
    except Exception as e:
        notify("Datasaver", f"[!] Failed to read lid state: {e}")
        print(f"[!] Failed to read lid state: {e}")
    return None

def restart_network_services():
    notify("Datasaver", f"[*] Restarting network services...")
    print("[*] Restarting network services...")
    subprocess.run(['systemctl', 'restart', 'NetworkManager', 'wpa_supplicant.service'])

def apply_datasaver():
    notify("Datasaver", "Re-applying datasaver settings...")
    print("[*] Re-applying datasaver settings...")
    subprocess.run(["/usr/bin/python3", "/opt/datasaver-gui/datasaver_gui.py", "on"])

def main():
    lid_file = get_lid_device()
    if not lid_file:
        print("[!] Lid state file not found.")
        return

    print(f"[*] Monitoring lid events via: {lid_file}")
    last_state = read_lid_state(lid_file)

    while True:
        time.sleep(CHECK_INTERVAL)
        current_state = read_lid_state(lid_file)
        if current_state and current_state != last_state:
            print(f"[+] Lid changed: {current_state}")
            if current_state == "open":
                restart_network_services()
                apply_datasaver()
            last_state = current_state

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Please run this script with sudo.")
        sys.exit(1)
    main()

