#!/usr/bin/python3

from collections import deque
from datetime import datetime, timezone
from multiprocessing import Process

import notify2
import os
import pyudev
import random
import re
import signal
import subprocess
import sys
import time

# File to save process ID of the watching process for lid open or close.
WATCHER_PID_FILE = "/tmp/datasaver_lid_watcher.pid"

def check_sudo():
    '''
    Program must be run with sudo not root.
    '''
    if 'SUDO_UID' not in os.environ:
        print("This tool requires sudo privileges.")
        sys.exit(1)

def Netfunc():
    '''
    You must be connected to a Network(Wireless or Ethernet), for datasaver to work. 
    Like the blur button on the datasaver icon when your cellular data connection is not turned on
    '''
    ostronics = subprocess.call(['ping', 'google.com', '-c', '1'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if ostronics != 0:
        print('CHECK YOUR NETWORK CONNECTION, VPN, OR CONNECT TO A WIFI NETWORK!!! \n TO START DATASAVER')
        sys.exit(2)
    elif ostronics == 0:
        pass

def get_iface():
    '''
    Retrieve all network interfaces that are UP, excluding the loopback 'lo'.
    Uses 'ip -details link show' command output and regex to parse interface names and flags.
    Returns a list of interface names that are active.
    '''
    # Run the 'ip' command to get detailed link info
    result = subprocess.run(['ip', '-details', 'link', 'show'], stdout=subprocess.PIPE, text=True)
    matches = re.finditer(r'^\d+: (\S+?):.*?<([^>]+)>', result.stdout, re.MULTILINE)

    interfaces = []
    for match in matches:
        iface, flags = match.group(1), match.group(2).split(',')
        # Only include interfaces that are UP and not the lo
        if 'UP' in flags and iface != 'lo':
            interfaces.append(iface)
    return interfaces

def notify(title, message):
    '''
    Create a notify event on the screen to show datasaver has be turned on or off.
    '''
    notify2.init("Datasaver")
    n = notify2.Notification(title, message)
    n.set_timeout(5000)
    n.show()

def restart_network_services():
    '''
    Method gets called to restart the NetworkManager on turning off the datasaver.
    '''
    subprocess.run(['systemctl', 'restart', 'NetworkManager', 'wpa_supplicant.service'])

def watch_lid_event():
    '''
    Watch for when the laptop lid gets closed and opened, creating a process 
    id to monitor the change, and call the 'restart_network_service' method
    '''
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by('power_supply')
    lid_closed = False

    for device in iter(monitor.poll, None):
        if device.action == "change" and "lid" in device.sys_name.lower():
            state_path = f"/proc/acpi/button/lid/{device.sys_name}/state"
            try:
                with open(state_path) as f:
                    state = f.read()
                    if 'open' in state.lower() and lid_closed:
                        restart_network_services()
                        lid_closed = False
                    elif 'closed' in state.lower():
                        lid_closed = True
            except:
                continue

class Datasaver:
    '''
    Datasaver class controls toggling the MTU size of network interfaces
    to save data (lower MTU) or reset to default (1500).
    '''
    def __init__(self):
        # Pick a random MTU between 1000 and 1400 for 'on' mode
        self.rand = random.randint(1000, 1400)
        # Get list of active interface to modify
        self.iface = get_iface()
        self.watcher_process = None

    def start_watcher(self):
        '''
        Start the process 'watch_lid_event' using multiprocessing
        '''
        if os.path.exists(WATCHER_PID_FILE):
            return
        self.watcher_process = Process(target=watch_lid_event)
        self.watcher_process.start()
        with open(WATCHER_PID_FILE, 'w') as f:
            f.write(str(self.watcher_process.pid))

    def stop_watcher(self):
        '''
        Stop the process by killing the process, and deleting the pid file 
        assigned to the 'watch_lid_event'.
        '''
        if os.path.exists(WATCHER_PID_FILE):
            with open(WATCHER_PID_FILE, 'r') as f:
                pid = int(f.read())
            try:
                os.kill(pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            os.remove(WATCHER_PID_FILE)

    def log_mtu_cli(self, mtu):
        '''
        Log MTU valuse to a file(experimental): with this, you will know which MTU value last used is best.
        '''
        CURRENT_DATETIME = datetime.now(timezone.utc).astimezone().ctime()
        CURRENT_DATETIME0 = datetime.now(timezone.utc).astimezone().tzinfo

        with open("/var/log/datasaver_mtu.log", "a") as log:
            log.write(f"[{CURRENT_DATETIME}-{CURRENT_DATETIME0}][CLI] MTU set to {mtu} on interface {', '.join(self.iface)}\n")

    def on(self):
        '''
         Enables the datasaver by setting MTU of active interfaces to a random lower value.
        Brings interfaces down before setting MTU and up afterwards to apply changes.
        '''
        try:
            for i in self.iface:
                subprocess.run(['ip', 'link', 'set', i, 'down'])
                subprocess.run(['ip', 'link', 'set', i, 'mtu', str(self.rand)])
                subprocess.run(['ip', 'link', 'set', i, 'up'])
            self.log_mtu_cli(self.rand)
            notify("Datasaver", f"Data saver ON. MTU set to {self.rand}")
            self.start_watcher()
        except Exception as e:
            pass
            print(f"Error: {e}")
            sys.exit(3)

    def off(self):
        '''
         Disables the datasaver by resetting MTU of interfaces to 1500 (default).
        Also restarts network services to ensure proper operation.
        '''
        try:
            for i in self.iface:
                subprocess.run(['ip', 'link', 'set', i, 'down'])
                subprocess.run(['ip', 'link', 'set', i, 'mtu', '1500'])
                subprocess.run(['ip', 'link', 'set', i, 'up'])
            subprocess.run(['systemctl', 'restart', 'NetworkManager', 'wpa_supplicant.service'])
            notify("Datasaver", "Data saver OFF. MTU reset to 1500")
            self.stop_watcher()
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(4)

def main():
    '''
      Runs the command given via CLI.
      Supports 'on', 'off' commands.
      Ensure the program is run with sudo priviledges.
      Ensure the user is connected to a Network before the program is started.
    '''
    check_sudo()
    #Netfunc()

    if len(sys.argv) < 2:
        print("Usage: sudo python3 datasaver.py <on|off|--help>")
        sys.exit(1)

    ds = Datasaver()
    cmd = sys.argv[1].lower()

    if cmd == "on":
        ds.on()
    elif cmd == "off":
        ds.off()
    elif cmd == "--help":
        print("Usage: sudo python3 datasaver.py <on|off>")
    else:
        # Informs user of Unknown command, and exit
        print("Unknown command:", cmd)

if __name__ == '__main__':
    main()

