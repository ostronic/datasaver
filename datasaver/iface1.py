import subprocess

def get_iface():
    result = subprocess.run(['ip', '-details', 'link', 'show'], stdout=subprocess.PIPE, text=True)
    interfaces = []
    for line in result.stdout.splitlines():
        if (': <' in line and 'lo' not in line):
            parts = line.split(':')
            if len(parts) > 1:
                i_face = parts[1].strip()
                if ('<UP,' in line or ',UP,' in line or ',UP>' in line):
                    interfaces.append(iface)
    print(interfaces)
    print(i_face)
    return interfaces

if __name__ == '__main__':
    get_iface()
