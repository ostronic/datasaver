#!/usr/bin/python3
#:  Title:  datasaver - reduces the MTU(that is the MSS value plus header)
#:          randomly, to minimize the data consumed by scavenging websites
#:  Synopsis:   sudo python3 datasaver.py on  -   To turn on the datsaver
#:                      which randomly changes the MTU value every 600secs
#:              sudo python3 datasaver.py off -   To turn off the data
#:                              saver and return it to the normal MTU size
#:  Date:   2025-05-12
#:  Version:    3 complete standalone.
#:  Author: ostronics {fg_daemon}
#:  Mail:   ostronics@proton.me

from collections import deque
from colorama import Fore, Back, Style
from netck import Netfunc

import os
import random
import re
import subprocess
import sys
import time

# Must allow user run the program as sudo 
if not 'SUDO_UID' in os.environ.keys():
    print(Style.DIM + 'You must run this program with sudo')
    exit()

# Check to see PC is conected to a network through Ethernet or Wirelessly before starting the datasaver.
if not Netfunc():
    pass

# Display banner on help argument
banner = Fore.CYAN + r"""
    ░█████╗░░██████╗████████╗██████╗░░█████╗░███╗░░██╗██╗░█████╗░░██████╗
    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗████╗░██║██║██╔══██╗██╔════╝
    ██║░░██║╚█████╗░░░░██║░░░██████╔╝██║░░██║██╔██╗██║██║██║░░╚═╝╚█████╗░
    ██║░░██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║██║╚████║██║██║░░██╗░╚═══██╗
    ╚█████╔╝██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░╚███║██║╚█████╔╝██████╔╝
    ░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░╚════╝░╚═════╝░
    *********************************************************************
    * Copyright of ostronics(fg_daemon) 2025                            *
    * 'What a wonderful world' :)   zagzag.drank337@passinbox.com       *
    *********************************************************************
        """
turn_on = Fore.WHITE + 'sudo python3 parrotLinuxv2.py on # To power on the datasaver and choose a random MTU size range(1000-1400)'
turn_off = Fore.RED + 'sudo python3 parrotLinuxv2.py off # To power off the datasaver, and return the MTU size to 1500(default) value'

usage = 'Usage: \n\t' + turn_on +'\n\t'+turn_off+'\r'


def get_iface():
    '''
        Function to retrieve the interfaces that is UP, saving to a list and queue while excluding the loopback interface
    '''
    result = subprocess.run(['ip', '-details', 'link', 'show'], stdout=subprocess.PIPE, text=True)

    # List and queue to store Interface names
    interface_list = []
    interface_queue = deque()

    # Regex to match interface name and check if it's up.
    # Matches lines like: "2: lo: <...> <BROADCAST,MULTICAST,UP,LOWER_UP> ..."
    matches = re.finditer(r'^\d+: (\S+?):.*?<([^>]+)>', result.stdout, re.MULTILINE)

    for match in matches:
        iface = match.group(1)
        flags = match.group(2).split(',')

        # Filter: Must be UP, and not 'lo'
        if ('UP' in flags and iface != 'lo'):
            interface_list.append(iface)
            interface_queue.append(iface)
            list(interface_queue)
    return interface_list

class Datasaver():
    def __init__(self):
        self.rand = random.randrange(999, 1399)
        self.iface = get_iface()

        if len(sys.argv) > 1:
            self.value = str(sys.argv[1])
        else:
            print("Usage: python3 datasaver.py <on|off|help>")
            sys.exit(1)

    def on(self):
        try:
            for i in self.iface:
                subprocess.run(['ip', 'link', 'set', f'{i}', 'down'])
                subprocess.run(['ip', 'link', 'set', f'{i}', 'mtu', f'{self.rand}'])
                subprocess.run(['ip', 'link', 'set', f'{i}', 'up']) 
            print('\n[+] Datasaver is on:   {}'.format(self.rand))
        except Exception as e:
            print(f'{e}')
            sys.exit(2)

    def off(self):
        try:
            for _ in self.iface:
                subprocess.run(['ip', 'link', 'set', f'{_}', 'down'])
                subprocess.run(['ip', 'link', 'set', f'{_}', 'mtu', '1500'])
                subprocess.run(['ip', 'link', 'set', f'{_}', 'up'])
            print('\n[-] Datasaver is off:  {}'.format(1500))
            subprocess.run(['systemctl', 'restart', 'NetworkManager', 'wpa_supplicant.service'])
            time.sleep(1)
            subprocess.call('clear', shell=True)
        except Exception as e:
            print(f'[*] {e}')
            sys.exit(3)

    def on_win(self):
        '''
            Power on datasaver for Windows
        '''
        pass
        #netsh interface ipv4 set subinterface "Interface Name" mtu=#### store=persistent    # store=persistent ensures the change remains after a reboot
        #netsh interface ipv4 show subinterfaces # Check the "Interface Name" and the Current "MTU" size for the network interface you want to modify

    def off_win(self):
        '''
            Power off datasaver for Windows
        '''
        pass

    def run(self):
        try:
            if self.value in ('-h','--help', 'help', '?'):
                print(banner + '\n' + usage)
                time.sleep(3)
                os.system('clear')
            elif self.value == 'on':
                self.on()
            elif self.value == 'off':
                self.off()
            else:
                print(f'Unknown option: {self.value}')
        except Exception as e:
            print(f"{e}")
            print(Fore.RED + Style.BRIGHT +'sudo python3 datasaver.py ? or -h or --help or help\r')
            sys.exit(4)

if __name__ == '__main__':
    ds = Datasaver()
    ds.run()
