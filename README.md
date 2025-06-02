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
- 💻 GUI interface for easy management
- 🔌 Lid-close detection with automatic actions
- 🔧 CLI for scripting and automation
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
```

---

## 📂 Project Structure
| File/Folder          | Description                              |
| -------------------- | ---------------------------------------- |
| `assets/`            | GUI and icon resources                   |
| `datasaverIcon.html` | Desktop integration (icon & shortcut)    |
| `install.sh`         | Post-install script for setup            |
| `lid_monitor.py`     | Handles lid-close event monitoring       |
| `netck.py`           | Network check and MTU optimization logic |
| `datasaver-cli.py`   | Command-line interface for datasaver     |
| `datasaver.py`       | GUI interface launcher                   |

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

---


## 🧾 License
This project is licensed under the Apache License 2.0.

