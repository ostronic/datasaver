#!/usr/bin/python3
#:  Title:  datasaver - reduces the MTU(that is the MSS value plus header)
#:          randomly, to minimize the data consumed by scavenging websites
#:  Synopsis:   sudo python3 parrotLinux.py 
#:  Date:   2025-04-12
#:  Version:    1.0
#:  Author: ostronics {fg_daemon}
#:  Mail:   zagzag.passinbox.com
#:

import os
import random
import sys
import subprocess

if not 'SUDO_UID' in os.environ.keys():
    print('You must run this program with sudo or as root!')
    exit()

rand = random.randrange(1000, 1399)

try:
    subprocess.run(['ip', 'link', 'set', 'wlo1', 'down'])
    subprocess.run(['ip', 'link', 'set', 'wlo1', 'mtu', f'{rand}'])
    subprocess.run(['ip', 'link', 'set', 'wlo1', 'up']) 
    print('\nNew MTU value is now {}'.format(rand))
except Exception as e:
    print(f'{e}')
    #print("You must run this program with sudo or as root !!!\n sudo python3\'prog%name'")
