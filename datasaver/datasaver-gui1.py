from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

import random
import subprocess
import sys

def check_sudo():
    pass

def get_iface():
    result = subprocess.run(['ip', '-details', 'link', 'show'], stdout=subprocess.PIPE, text=True)
    interfaces = []
    for line in result.stdout.splitlines():
        if ': <' in line and 'lo' not in line:
            parts = line.split(':')
            if len(parts) > 1:
                iface = parts[1].strip()
                if '<UP,' in line or ',UP,' in line or ',UP>' in line:
                    interfaces.append(iface)
    return interfaces

class Datasaver:
    def __init__(self):
        self.rand = random.randrange(999, 1399)
        self.iface = get_iface()

    def on(self):
        print("[+] Turning datasaver ON")
        for i in self.iface:
            subprocess.run(['ip', 'link', 'set', i, 'down'])
            subprocess.run(['ip', 'link', 'set', i, 'mtu', str(self.rand)])
            subprocess.run(['ip', 'link', 'set', i, 'up'])
        print(f"Datasaver ON with MTU {self.rand}")

    def off(self):
        print("[-] Turning datasaver OFF")
        for i in self.iface:
            subprocess.run(['ip', 'link', 'set', i, 'down'])
            subprocess.run(['ip', 'link', 'set', i, 'mtu', '1500'])
            subprocess.run(['ip', 'link', 'set', i, 'up'])
        subprocess.run(['systemctl', 'restart', 'NetworkManager', 'wpa_supplicant'])
        print("Datasaver OFF and services restarted")

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.datasaver = Datasaver()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Datasaver')
        self.setGeometry(100, 100, 300, 200)
        self.setWindowIcon(QIcon())

        layout = QVBoxLayout()

        self.status_label = QLabel("Click a button to toggle Datasaver", self)
        self.status_label.setAlignment(Qt.AlignCenter)

        self.on_btn = QPushButton('Turn ON Datasaver', self)
        self.on_btn.clicked.connect(self.turn_on)

        self.off_btn = QPushButton('Turn OFF Datasaver', self)
        self.off_btn.clicked.connect(self.turn_off)

        layout.addWidget(self.status_label)
        layout.addWidget(self.on_btn)
        layout.addWidget(self.off_btn)

        self.setLayout(layout)

    def turn_on(self):
        try:
            self.datasaver.on()
            self.status_label.setText("Datasaver is ON")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def turn_off(self):
        try:
            self.datasaver.off()
            self.status_label.setText("Datasaver is OFF")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

