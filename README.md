# 📶 datasaver

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Build](https://img.shields.io/github/actions/workflow/status/ostronic/datasaver/python-app.yml?label=build)](https://github.com/ostronic/datasaver/actions)

**datasaver** is a lightweight Python-based Linux utility to reduce background data usage, optimize MTU/network settings, and improve laptop power efficiency. It includes both CLI and GUI components.

---

## 📸 Preview

![datasaver GUI screenshot](assets/datasaver.png)  
<sub>_Example of the datasaver GUI interface_</sub>

> 🔧 Don't forget to replace `assets/datasaver.png` with your actual screenshot!

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
