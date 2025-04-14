#!/bin/ !python
#!/usr/bin/python3
#:  Title:  datasaver - reduces the MTU(that is the MSS value plus header)
#:          randomly, to minimize the data consumed by scavenging websites
#:  Synopsis:   sudo python3 parrotLinuxv2.py on  -   To turn on the datsaver
#:                      which randomly changes the MTU value every 600secs
#:              sudo python3 parrotLinuxv2.py off -   To turn off the data
#:                              saver and return it to the normal MTU size
#:  Date:   2025-04-13
#:  Version:    2.0
#:  Author: ostronics {fg_daemon}
#:  Mail:   zagzag.passinbox.com
#:  Update: Added datasaver to VPN devices(tun0).

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
    \n****************************************************************
    \n* Copyright of ostronics(fg_daemon) 2025                       *
    \n* Buy me a coffe(Mail):   zagzag.drank337@passinbox.com        *
    \n****************************************************************
        """

rand = random.randrange(1000, 1399)

def on():
    try:
        subprocess.run(['ip', 'link', 'set', 'wlo1', 'down'])
        subprocess.run(['ip', 'link', 'set', 'wlo1', 'mtu', f'{rand}'])
        subprocess.run(['ip', 'link', 'set', 'tun0', 'mtu', f'{rand}'])
        subprocess.run(['ip', 'link', 'set', 'wlo1', 'up']) 
        print('\nNew MTU value is now {}'.format(rand))
    except Exception as e:
        print(f'{e}')
        #print("You must run this program with sudo or as root !!!\n sudo python3\'prog%name'")
        sys.exit(1)

def off():
    try:
        subprocess.run(['ip', 'link', 'set', 'wlo1', 'down'])
        subprocess.run(['ip', 'link', 'set', 'wlo1', 'mtu', '1500'])
        subprocess.run(['ip', 'link', 'set', 'wlo1', 'up'])
        print('\nMTU value is now 1500(default)')
        subprocess.run(['systemctl', 'restart', 'NetworkManager', 'wpa_supplicant.service'])
        time.sleep(1)
        subprocess.call('clear', shell=True)
    except Exception as e:
        print(f'{e}')
        sys.exit(2)

if __name__ == '__main__':
    turn_on = Fore.WHITE + 'sudo python3 parrotLinuxv2.py on # To power on the datasaver and choose a random MTU size range(1000-1400)'
    turn_off = Fore.RED + 'sudo python3 parrotLinuxv2.py off # To power off the datasaver, and return the MTU size to 1500(default) value'

    usage = 'Usage: \n\t' + turn_on +'\n\t'+turn_off+'\r'

    try:
        value = str(sys.argv[1])
        if value == '-h' or '--help' or 'help':
            print(text + '\n',usage)
            time.sleep(10)
            os.system('clear')
        if value == 'on':
            on()
        if value == 'off':
            off()
    except:
        print(text + '\n',usage)
        sys.exit(3)
