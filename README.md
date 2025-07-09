# 📶 Datasaver Linux Utility

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Build](https://img.shields.io/github/actions/workflow/status/ostronic/datasaver/python-app.yml?label=build)](https://github.com/ostronic/datasaver/actions)

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

**datasaver** is a lightweight Python-based Linux utility to reduce background data usage, optimize MTU/network settings, and improve laptop power efficiency. It includes system tray icon, lid-close detection; both CLI and GUI components.

---

## 📸 Preview

asaver GUI screenshot](assets/datasaver.png)

<sub>_Example of the datasaver GUI interface_</sub>

---

## ⚡ Features

- 🧠 Smart MTU/network tuning
- 💻 GUI interface for easy management (Taskbar icon and management,hide/show options button)
- 🔌 Lid-close detection with automatic actions(Auto-reactivates on laptop lid-open events)
- 🔧 CLI for scripting and automation(Allow logging /var/log/datasaver_mtu.log)
- 📡 Optimized for low-data usage environments
- 📦 Easy packaging: `.deb` and installer scripts included

## 📦 Step 3: Cross-platform Packaging

🧊 .AppImage (for all Linux distros)

📦 .rpm (for Fedora, RHEL, CentOS)

🌍 GitHub Actions to auto-build .deb and .rpm on push

---

## 🛠️ Installation

Option 1:    Use `.deb` package (recommended)
```bash
sudo dpkg -i deb/datasaver_1.0_all.deb
```

Option 2:    Manual Installation
Run the following commands to install `datasaver` on a Debian/Ubuntu-based system:

```bash
sudo apt update
sudo apt install -y python3 python3-pip git
git clone https://github.com/ostronic/datasaver.git
cd datasaver/
pip3 install -r requirements.txt
sudo bash install.sh
cd
sudo rm -rfd datasaver/
datasaver
```
To run CLI version,
```bash
cd /opt/datasaver
sudo python3 datasaver-cli.py <on|off>
```
---

## 🧊 1. Build .AppImage (Universal Linux App)
Why .AppImage?
Works on almost any Linux distro

No need to install or elevate privileges

Portable: run from anywhere with ./Datasaver.AppImage

✅ Step-by-Step to Build .AppImage
📦 1. Install AppImage Tools
On Ubuntu/Debian:

```bash
sudo apt install appimagetool libfuse2
```
Also make sure python3, pip, and pyqt5 are available.

Run the following file:
```bash
sudo bash AppImage
```
This generates Datasaver-x86_64.AppImage

📦 2. Build .rpm (for Fedora/RHEL/CentOS)
.....

---

```dir
datasaver/
├── AppImage
├── datasaver.py
├── datasaver-cli.py
├── lid_monitor.py
├── lid_monitor.sh
├── netck.py
├── requirements.txt
├── install.sh
├── uninstall.sh
├── README.md
├── assets/
│   └── datasaver.png
│   └── datasaver.jpg
├── config/
│   ├── datasaver.desktop
|   ├── datasaver_app.desktop
│   ├── datasaver-lid.service
│   └── com.datasaver.policy
├── deb/
│   ├── datasaver_1.0_all.deb
│   └── datasaver-deb.zip
```
## 📂 Project Structure
| File/Folder          | Description                                  |
| -------------------- | ---------------------------------------------|
| `deb`                | Debian installation package folder and file  |
| `assets/`            | GUI and icon resources                       |
| `config`             | Configuration/ runtime files                 |
| `datasaverIcon.html` | Desktop integration (icon & shortcut)        |
| `requirements.txt`   | Installs prerequisites for runtime           |
| `install.sh`         | Post-install script for setup                |
| `uninstall.sh`       | Uninstall script for package removal         |
| `lid_monitor.py`     | Handles lid-close event monitoring           |
| `lid_monitor.sh`     | Handles lid-close event Monitoring in bash   |
| `netck.py`           | Network check and MTU optimization logic     |
| `datasaver-cli.py`   | Command-line interface for datasaver         |
| `datasaver.py`       | GUI interface launcher                       |

---

## 🧪 Usage
Launch the GUI:

```bash
    datasaver
```
Use the CLI:

```bash
    python3 datasaver-cli.py --help
```

Or simply launch the application through the GUI in Menu/Applications

---

## 🛠️ Uninstall

Run the following commands to uninstall `datasaver` on a Debian/Ubuntu-based system:

```bash
    cd /opt/datasaver
    sudo bash uninstall.sh
```

---

## 🧾 License
This project is licensed under the [![Apache License 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)].

---

## 🙌 Contributing
Pull requests and suggestions are welcome! If you find a bug or want to help improve this project, feel free to open an issue or PR.

---

## ✨ Author
Created with ❤️ by @ostronic
