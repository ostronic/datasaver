#!/bin/bash

# Exit on error
set -e

REPO_URL="https://github.com/yourusername/datasaver-gui.git"
INSTALL_DIR="/opt/datasaver-gui"
DESKTOP_FILE="/usr/share/applications/datasaver.desktop"
PYTHON_CMD=$(command -v python3)

echo "[*] Checking for root privileges..."
if [[ "$EUID" -ne 0 ]]; then
    echo "Please run this script with sudo."
    exit 1
fi

echo "[*] Installing system dependencies..."
apt update
apt install -y python3 python3-pip python3-venv git

echo "[*] Cloning Datasaver GUI repo..."
rm -rf "$INSTALL_DIR"
git clone "$REPO_URL" "$INSTALL_DIR"

echo "[*] Creating virtual environment..."
python3 -m venv "$INSTALL_DIR/dsvenv"
source "$INSTALL_DIR/dsvenv/bin/activate"

echo "[*] Installing Python requirements..."
pip install -r "$INSTALL_DIR/requirements.txt"

echo "[*] Creating launcher..."
cat <<EOF > "$DESKTOP_FILE"
[Desktop Entry]
Type=Application
Name=Datasaver
Exec=$INSTALL_DIR/dsvenv/bin/python $INSTALL_DIR/datasaver_gui.py
Icon=network-wireless
Terminal=false
Categories=Network;Utility;
EOF

chmod +x "$DESKTOP_FILE"
update-desktop-database &>/dev/null || true

echo "[*] Done. Datasaver GUI is now installed system-wide."
echo "You can launch it from the application menu."

