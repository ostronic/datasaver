#!/bin/bash

# Exit on error
set -e

REPO_URL="https://github.com/yourusername/datasaver-gui.git"
INSTALL_DIR="$HOME/.local/share/datasaver"
DESKTOP_FILE="$HOME/.local/share/applications/datasaver.desktop"
PYTHON_CMD=$(command -v python3)

echo "[*] Cloning Datasaver GUI..."
git clone "$REPO_URL" "$INSTALL_DIR"

echo "[*] Installing dependencies..."
$PYTHON_CMD -m pip3 install --user -r "$INSTALL_DIR/requirements.txt" --break-system-packages

echo "[*] Creating launcher..."
cat <<EOF > "$DESKTOP_FILE"
[Desktop Entry]
Type=Application
Name=Datasaver
Exec=$PYTHON_CMD $INSTALL_DIR/datasaver_gui.py
Icon=network-wireless
Terminal=false
Categories=Utility;Network;
EOF

chmod +x "$DESKTOP_FILE"

echo "[*] Done. You can now launch Datasaver from your application menu."

