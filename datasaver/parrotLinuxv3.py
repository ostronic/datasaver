#!/bin/ !python
#!/usr/bin/python3
#:  Title:  datasaver - reduces the MTU(that is the MSS value plus header)
#:          randomly, to minimize the data consumed by scavenging websites
#:  Synopsis:   sudo python3 parrotLinuxv2.py on  -   To turn on the datsaver
#:                      which randomly changes the MTU value every 600secs
#:              sudo python3 parrotLinuxv2.py off -   To turn off the data
#:                              saver and return it to the normal MTU size
#:  Date:   2025-05-12
#:  Version:    3
#:  Author: ostronics {fg_daemon}
#:  Mail:   zagzag.passinbox.com
#:  Update: Updated the data saver code, to follow the real time mtu value 
#:          after a change, for all interfaces, and stores the value in a 
#:          dictionary for future use.

from colorama import Fore, Back, Style

import os
import random
import re
import subprocess
import sys
import time

if not 'SUDO_UID' in os.environ.keys():
    print(Style.DIM + 'You must run this program with sudo')
    exit()

text = Fore.CYAN + r"""
    ░█████╗░░██████╗████████╗██████╗░░█████╗░███╗░░██╗██╗░█████╗░░██████╗
    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗████╗░██║██║██╔══██╗██╔════╝
    ██║░░██║╚█████╗░░░░██║░░░██████╔╝██║░░██║██╔██╗██║██║██║░░╚═╝╚█████╗░
    ██║░░██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║██║╚████║██║██║░░██╗░╚═══██╗
    ╚█████╔╝██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░╚███║██║╚█████╔╝██████╔╝
    ░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░╚════╝░╚═════╝░
    *********************************************************************
    * Copyright of ostronics(fg_daemon) 2025                            *
    * Buy me a sleep pills(Mail):   zagzag.drank337@passinbox.com       *
    *********************************************************************
        """

rand = random.randrange(1000, 1399)
dev = ['wlo1', 'tun0']
mtu_values = {}

def reg():
    # Run the `ip link` command and capture its output
    result = subprocess.run(['ip', 'link'], stdout=subprocess.PIPE, text=True)

    # Dictionary to store interface name and corresponding MTU value
    #mtu_values = {}

    # Regular expression to extract interface name and MTU value
    # Matches lines like: "2: lo: <...> mtu 65535 ..."
    matches = re.finditer(r'^\d+: (\S+?):.*?mtu (\d+)', result.stdout, re.MULTILINE)

    for match in matches:
        interface = match.group(1)
        mtu = int(match.group(2))
        mtu_values[interface] = mtu
        #print("{}:  {}\n".format(interface,mtu))
    return interface, mtu
    #return f"Interface: {interface}, MTU:   {mtu}\n"
    #return mtu_values

    # You can now use mtu_values as a dictionary containing all MTU info
'''
Using ifconfig for just the MTU values
rdm = subprocess.run(['ifconfig'], stdout=subprocess.PIPE, text=True)
        dev1 = re.finditer(r'mtu (\d+)', rdm.stdout, re.MULTILINE)
        for _ in dev1:
            dev2 = int(_.group(1))
            print(f"{dev2}"
'''


def on():
    try:
        for i in dev:
            subprocess.run(['ip', 'link', 'set', f'{i}', 'down'])
            subprocess.run(['ip', 'link', 'set', f'{i}', 'mtu', f'{rand}'])
            subprocess.run(['ip', 'link', 'set', f'{i}', 'up']) 
        print('\n[-] New MTU value is {}'.format(reg()))
    except Exception as e:
        print(f'{e}')
        sys.exit(1)

def off():
    try:
        for _ in dev:
            subprocess.run(['ip', 'link', 'set', f'{_}', 'down'])
            subprocess.run(['ip', 'link', 'set', f'{_}', 'mtu', '1500'])
            subprocess.run(['ip', 'link', 'set', f'{_}', 'up'])
        print('\n[+] MTU value is now default {}'.format(reg()))
        subprocess.run(['systemctl', 'restart', 'NetworkManager', 'wpa_supplicant.service'])
        time.sleep(3)
        subprocess.call('clear', shell=True)
    except Exception as e:
        print(f'[*] {e}')
        sys.exit(2)

if __name__ == '__main__':
    turn_on = Fore.WHITE + 'sudo python3 parrotLinuxv2.py on # To power on the datasaver and choose a random MTU size range(1000-1400)'
    turn_off = Fore.RED + 'sudo python3 parrotLinuxv2.py off # To power off the datasaver, and return the MTU size to 1500(default) value'

    usage = 'Usage: \n\t' + turn_on +'\n\t'+turn_off+'\r'

    try:
        value = str(sys.argv[1])
        if value == '-h' or '--help' or 'help' or '?':
            print(text + '\n',usage)
            time.sleep(3)
            os.system('clear')
        if value == 'on':
            on()
        if value == 'off':
            off()
    except Exception as e:
        print(Fore.RED + Style.BRIGHT +'sudo python3 parrotLinuxv2-1.py ? or -h or --help or help\r')
        sys.exit(3)
