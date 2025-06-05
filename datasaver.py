from multiprocessing import Process
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QStackedLayout, QLabel, QSystemTrayIcon, QMenu, QMessageBox, QAction
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap
from PyQt5.QtCore import Qt

import notify2
import os
import pyudev
import random
import re
import signal
import subprocess
import sys
import time

WATCHER_PID_FILE = "/tmp/datasaver_lid_watcher.pid"

class Datasaver:
    def __init__(self):
        self.iface = self.get_iface()
        self.watcher_process = None

    def get_iface(self):
        result = subprocess.run(['ip', '-details', 'link', 'show'], stdout=subprocess.PIPE, text=True)
        matches = re.finditer(r'^\d+: (\S+?):.*?<([^>]+)>', result.stdout, re.MULTILINE)
        interfaces = []
        for match in matches:
            iface, flags = match.group(1), match.group(2).split(',')
            if 'UP' in flags and iface != 'lo':
                interfaces.append(iface)
        return interfaces

    def notify(self, title, message):
        notify2.init("Datasaver")
        n = notify2.Notification(title, message)
        n.set_timeout(5000)
        n.show()

    def restart_network_services(self):
        subprocess.run(['systemctl', 'restart', 'NetworkManager', 'wpa_supplicant.service'])

    def watch_lid_event(self):
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
                            self.restart_network_services()
                            lid_closed = False
                        elif 'closed' in state.lower():
                            lid_closed = True
                except:
                    continue

    def start_watcher(self):
        if os.path.exists(WATCHER_PID_FILE):
            return
        self.watcher_process = Process(target=self.watch_lid_event)
        self.watcher_process.start()
        with open(WATCHER_PID_FILE, 'w') as f:
            f.write(str(self.watcher_process.pid))

    def stop_watcher(self):
        if os.path.exists(WATCHER_PID_FILE):
            with open(WATCHER_PID_FILE, 'r') as f:
                pid = int(f.read())
            try:
                os.kill(pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            os.remove(WATCHER_PID_FILE)

    def on(self):
        # Rotate MTU value upon click of the button
        self.rand = random.randrange(1000, 1400)
        print(f"[+] Turning datasaver ON with MTU {self.rand}")
        for i in self.iface:
            subprocess.run(['ip', 'link', 'set', i, 'down'])
            subprocess.run(['ip', 'link', 'set', i, 'mtu', str(self.rand)])
            subprocess.run(['ip', 'link', 'set', i, 'up'])
        self.log_mtu(self.rand)
        self.notify("Datasaver", f"Data saver ON. MTU set to {self.rand}")
        self.start_watcher()

    def log_mtu(self, mtu):
        '''
        Log MTU valuse to a file(experimental): with this, you will know which MTU value last used is best.
        '''
        with open("/var/log/datasaver_mtu.log", "a") as log:
            log.write(f"MTU set to {mtu} on interface {', '.join(self.iface)}\n")

    def off(self):
        for i in self.iface:
            subprocess.run(['ip', 'link', 'set', i, 'down'])
            subprocess.run(['ip', 'link', 'set', i, 'mtu', '1500'])
            subprocess.run(['ip', 'link', 'set', i, 'up'])
        subprocess.run(['systemctl', 'restart', 'NetworkManager', 'wpa_supplicant.service'])
        self.notify("Datasaver", "Data saver OFF. MTU reset to 1500")
        self.stop_watcher()

class DatasaverApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ds = Datasaver()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Datasaver GUI')
        self.setGeometry(100, 100, 360, 200)
        self.setStyleSheet("QPushButton { border-radius: 10px; padding: 10px; } QLabel { color: black; font-weight: bold; font-size: 14px; }")

        # Background image
        bg = QLabel(self)
        palette = QPalette()
        pixmap = QPixmap("/opt/datasaver/assets/datasaver.jpg").scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette.setBrush(QPalette.Window, QBrush(pixmap))
        self.setPalette(palette)
        bg.setPixmap(pixmap)
        bg.setScaledContents(True)

        stacked = QStackedLayout()
        stacked.addWidget(bg)

        # UI content
        layout = QVBoxLayout()

        self.label = QLabel('Datasaver Status: OFF', self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        button_style = """
        QPushButton {
            background-color: #2e86c1;
            color: white;
            border-radius: 15px;
            padding: 10px 20px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #3498db;
        }
        QPushButton:pressed {
            background-color: #21618c;
        }
        """


        # Style and center the ON button
        self.on_button = QPushButton('Turn On', self)
        self.on_button.setFixedWidth(200)
        self.on_button.setStyleSheet(button_style)
        self.on_button.clicked.connect(self.turn_on)
        layout.addWidget(self.on_button, alignment=Qt.AlignCenter)

        # Style and center the OFF button
        self.off_button = QPushButton('Turn Off', self)
        self.off_button.setFixedWidth(200)
        self.off_button.setStyleSheet(button_style)
        self.off_button.clicked.connect(self.turn_off)
        layout.addWidget(self.off_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

        stacked.addWidget(self)
        #self.setLayout(stacked)

        # Tray icon and menu
        self.tray_icon = QSystemTrayIcon(QIcon("/opt/datasaver/assets/datasaver.png"), self)
        tray_menu = QMenu()

        on_action = QAction("Turn On", self)
        on_action.triggered.connect(self.turn_on)
        tray_menu.addAction(on_action)

        off_action = QAction("Turn Off", self)
        off_action.triggered.connect(self.turn_off)
        tray_menu.addAction(off_action)

        hide_ui_action = QAction("Hide UI", self)
        hide_ui_action.triggered.connect(self.hide)
        tray_menu.addAction(hide_ui_action)

        show_ui_action = QAction("Show UI", self)
        show_ui_action.triggered.connect(self.show)
        tray_menu.addAction(show_ui_action)

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(QApplication.quit)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.setToolTip("Datasaver running")
        self.tray_icon.show()

    def turn_on(self):
        try:
            self.ds.on()
            #self.label.setText(f'Datasaver Status: ON')
            self.label.setText(f"Datasaver is ON with MTU {self.ds.rand}")
            self.on_button.setText("Applying...")
            QApplication.processEvents()
            self.on_button.setText("Toggle ON Datasaver")
        except Exception as os:
            QMessageBox.critical(self, "Error", str(os))

    def turn_off(self):
        self.ds.off()
        self.label.setText('Datasaver Status: OFF')

if __name__ == '__main__':
    if os.geteuid() != 0:
        print("This tool requires sudo privileges.")
        sys.exit(1)

    app = QApplication(sys.argv)
    window = DatasaverApp()
    window.show()
    sys.exit(app.exec_())
