# 📶 datasaver

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

**datasaver** is a lightweight Python-based Linux utility to reduce background data usage, optimize MTU/network settings, and improve laptop power efficiency. It includes both CLI and GUI components.

---

## 📸 Preview

![datasaver GUI screenshot](assets/datasaver.png)  
<sub>_Example of the datasaver GUI interface_</sub>

---

## ⚡ Features

- 🧠 Smart MTU/network tuning
- 💻 GUI interface for easy management (Taskbar icon and management,Hide button)
- 🔌 Lid-close detection with automatic actions
- 🔧 CLI for scripting and automation(Allow logging /var/log/datasaver_mtu.log)
- 📡 Optimized for low-data usage environments

---

## 🛠️ Installation

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
```
cd /opt/datasaver
sudo python3 datasaver-cli.py <on|off>
```

---

## 📂 Project Structure
| File/Folder          | Description                                  |
| -------------------- | ---------------------------------------------|
| `assets/`            | GUI and icon resources                       |
| `config`             | Configuration/ runtime files                 |
| `datasaverIcon.html` | Desktop integration (icon & shortcut)        |
| `requirements.txt`   | Installs prerequisites for runtime           |
| `install.sh`         | Post-install script for setup                |
| `uninstall.sh`       | Uninstall script for package removal         |
| `lid_monitor.py`     | Handles lid-close event monitoring           |
| `lid_monitor.sh`     | HAndles lid-close event Monitoring in bash   |
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
