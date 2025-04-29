#!/bin/ !python
#!/usr/bin/python3
#:  Title:  datasaver - reduces the MTU(that is the MSS value plus header)
#:          randomly, to minimize the data consumed by scavenging websites
#:  Synopsis:   sudo python3 datasaver_compact.py on  -   To turn on the 
#:                  datsaver, allow inputting of your Network Device local 
#:                  to your Operating system and randomly changes the MTU 
#:                  value every 600secs.
#:              sudo python3 datasaver_compact.py off -   To turn off the 
#:                  datasaver and return all devices to the normal MTU size
#:  Date:   2025-04-24
#:  Version:    2.1b
#:  Author: ostronics {fg_daemon}
#:  Mail:   zagzag.passinbox.com
#:  Update: Added option to input Network Device(s) local to your 
#:          Operating System. 

from colorama import Fore, Back, Style

import os
import random
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
    *******************************************************************
    *** Copyright of ostronics(fg_daemon) 2025                       **
    ** Buy me a coffee(Mail):   zagzag.drank337@passinbox.com       ***
    *******************************************************************
        """

rand = random.randrange(1000, 1399)
dev = []
try:
    while True:
        devices = input(Style.BRIGHT + 'Enter Network Device(s) Name, Ctrl+C to continue:   ')
        dev.append(devices)
except KeyboardInterrupt:
    pass

def on():
    try:
        for i in dev:
            subprocess.run(['ip', 'link', 'set', f'{i}', 'down'])
            subprocess.run(['ip', 'link', 'set', f'{i}', 'mtu', f'{rand}'])
            subprocess.run(['ip', 'link', 'set', f'{i}', 'up']) 
            print('\n[-] New MTU value is now {}'.format(rand))
    except Exception as e:
        print(f'[*] {e}')
        sys.exit(1)

def off():
    try:
        for _ in dev:
            subprocess.run(['ip', 'link', 'set', f'{_}', 'down'])
            subprocess.run(['ip', 'link', 'set', f'{_}', 'mtu', '1500'])
            subprocess.run(['ip', 'link', 'set', f'{_}', 'up'])
            print('\n[+] MTU value for all dev. is now 1500(default)')
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
            print('n',text + usage)
            time.sleep(3)
            os.system('clear')
        if value == 'on':
            on()
        if value == 'off':
            off()
    except Exception as e:
        print(Fore.RED + Style.BRIGHT +'sudo python3 datasaver_compact.py ? or -h or --help or help\r')
        sys.exit(3)
