#!/bin/bash

set -e

APP_NAME="datasaver"
INSTALL_DIR="/opt/$APP_NAME"
BIN_PATH="/usr/local/bin/$APP_NAME"
LOG_PATH="/var/log/datasaver_mtu.log"
ICON_PATH="/usr/share/icons/hicolor/128x128/apps/$APP_NAME.png"
DESKTOP_ENTRY="/usr/share/applications/$APP_NAME.desktop"
POLKIT_FILE="/usr/share/polkit-1/actions/com.$APP_NAME.policy"

# Ensure script is run as root
if [ "$EUID" -ne 0 ]; then
  echo "This script must be run as root."
  exit 1
fi

# Create installation directory
mkdir -p "$INSTALL_DIR"

# Copy application files to install directory
cp -r ./* "$INSTALL_DIR"
chmod +x "$INSTALL_DIR/$APP_NAME.py"

# Create symlink for CLI access and Export GUI session for root
cat <<EOF > "$BIN_PATH"
#!/bin/bash
# Export GUI session for root
XUSER=$(logname)
export DISPLAY=:0
export XAUTHORITY="/home/$XUSER/.Xauthority"
exec pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY /usr/bin/python3 $INSTALL_DIR/$APP_NAME.py "$@"
EOF

chmod +x "$BIN_PATH"

# Create log path to avoid permission issues for logging
touch "$LOG_PATH"
chmod 666 "$LOG_PATH"


# Install icon if available
if [ -f "$INSTALL_DIR/assets/datasaver.png" ]; then
  mkdir -p "$(dirname $ICON_PATH)"
  cp "$INSTALL_DIR/assets/datasaver.png" "$ICON_PATH"
fi

# Create .desktop launcher
cat <<EOF > "$DESKTOP_ENTRY"
[Desktop Entry]
Name=Datasaver
Exec=$BIN_PATH
Icon=$ICON_PATH
Terminal=false
Type=Application
Categories=Utility;Network;
StartupNotify=true
EOF

chmod +x "$DESKTOP_ENTRY"
update-desktop-database &>/dev/null || true

cat <<EOF > "$POLKIT_FILE"
<?xml version="1.0" encoding="UTF-8"?>
<policyconfig>
  <action id="com.datasaver.gui">
    <description>Launch Datasaver GUI</description>
    <message>Authentication is required to launch Datasaver.</message>
    <defaults>
      <allow_any>no</allow_any>
      <allow_inactive>no</allow_inactive>
      <allow_active>auth_admin</allow_active>
    </defaults>
  </action>
</policyconfig>
EOF

chmod 644 "$POLKIT_FILE"

# Enable lid close detection
LID_SCRIPT="/etc/systemd/system/datasaver-lid.service"
cat <<EOF > "$LID_SCRIPT"
[Unit]
Description=Monitor laptop lid and toggle datasaver
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 $INSTALL_DIR/lid_monitor.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

chmod +x "$INSTALL_DIR/lid_monitor.py"
systemctl daemon-reexec
systemctl daemon-reload
systemctl enable datasaver-lid.service

# Notify user
notify-send "Datasaver installed successfully!"
echo "Datasaver installed successfully. Launch from your applications menu or with: datasaver"

exit 0
