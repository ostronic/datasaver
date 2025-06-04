#!/bin/bash

APP_NAME="datasaver"
INSTALL_DIR="/opt/$APP_NAME"
BIN_PATH="/usr/local/bin/$APP_NAME"
DESKTOP_ENTRY="/usr/share/applications/$APP_NAME.desktop"
ICON_PATH="/usr/share/icons/hicolor/128x128/apps/$APP_NAME.png"
SERVICE_FILE="/etc/systemd/system/${APP_NAME}-lid.service"
POLKIT_FILE="/usr/share/polkit-1/actions/com.datasaver.policy"

echo "[*] Uninstalling $APP_NAME..."

systemctl disable "${APP_NAME}-lid.service" &>/dev/null
rm -f "$SERVICE_FILE"
rm -f "$DESKTOP_ENTRY"
rm -f "$POLKIT_FILE"
rm -f "$ICON_PATH"
rm -f "$BIN_PATH"
rm -rf "$INSTALL_DIR"

echo "[✓] Uninstalled $APP_NAME"
