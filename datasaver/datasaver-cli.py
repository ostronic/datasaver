#!/usr/bin/python3

import notify2
import os
import pyudev
import random
import re
import subprocess
import sys
import time

from collections import deque

def check_sudo():
    if 'SUDO_UID' not in os.environ:
        print("This tool requires sudo privileges.")
        sys.exit(1)

def get_iface():
    result = subprocess.run(['ip', '-details', 'link', 'show'], stdout=subprocess.PIPE, text=True)
    matches = re.finditer(r'^\d+: (\S+?):.*?<([^>]+)>', result.stdout, re.MULTILINE)

    interfaces = []
    for match in matches:
        iface, flags = match.group(1), match.group(2).split(',')
        if 'UP' in flags and iface != 'lo':
            interfaces.append(iface)
    return interfaces

def notify(title, message):
    notify2.init("Datasaver")
    n = notify2.Notification(title, message)
    n.set_timeout(5000)
    n.show()

class Datasaver:
    def __init__(self):
        self.rand = random.randint(1000, 1400)
        self.iface = get_iface()

    def on(self):
        try:
            for i in self.iface:
                subprocess.run(['ip', 'link', 'set', i, 'down'])
                subprocess.run(['ip', 'link', 'set', i, 'mtu', str(self.rand)])
                subprocess.run(['ip', 'link', 'set', i, 'up'])
            notify("Datasaver", f"Data saver ON. MTU set to {self.rand}")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(2)

    def off(self):
        try:
            for i in self.iface:
                subprocess.run(['ip', 'link', 'set', i, 'down'])
                subprocess.run(['ip', 'link', 'set', i, 'mtu', '1500'])
                subprocess.run(['ip', 'link', 'set', i, 'up'])
            subprocess.run(['systemctl', 'restart', 'NetworkManager', 'wpa_supplicant.service'])
            notify("Datasaver", "Data saver OFF. MTU reset to 1500")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(3)

def watch_lid_event(callback):
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by('power_supply')

    for device in iter(monitor.poll, None):
        if device.action == "change" and "lid" in device.sys_name.lower():
            callback()
            notify("Datasaver", "Network interfaces have been restarted")

def restart_network_services():
    subprocess.run(['systemctl', 'restart', 'NetworkManager', 'wpa_supplicant.service'])

def main():
    check_sudo()

    if len(sys.argv) < 2:
        print("Usage: sudo python3 datasaver.py <on|off|watch>")
        sys.exit(1)

    ds = Datasaver()
    cmd = sys.argv[1].lower()

    if cmd == "on":
        ds.on()
    elif cmd == "off":
        ds.off()
    elif cmd == "watch":
        print("Watching for lid events...")
        watch_lid_event(restart_network_services)
    else:
        print("Unknown command:", cmd)

if __name__ == '__main__':
    main()
