import subprocess
import re
from collections import deque

def get_iface():
    # Run `ip link show` to get interface details
    result = subprocess.run(['ip', '-details', 'link', 'show'], stdout=subprocess.PIPE, text=True)

    # Store interface names here
    interface_list = []
    interface_queue = deque()

    # Regex to match interface name and check if it's UP
    # Sample match: "2: enp3s0: <BROADCAST,MULTICAST,UP,LOWER_UP> ..."
    pattern = re.finditer(r'^\d+: (\S+?):.*?<([^>]+)>', result.stdout, re.MULTILINE)

    for match in pattern:
        iface = match.group(1)
        flags = match.group(2).split(',')

        # Filter: Must be UP, and not 'lo'
        if ('UP' in flags and iface != 'lo'):
            interface_list.append(iface)
            interface_queue.append(iface)

    # Output
    #print("UP Interfaces (list):", interface_list)
    #print("UP Interfaces (queue):", list(interface_queue))

    return interface_list
