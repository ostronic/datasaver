#!/bin/bash

LID_STATE_FILE="/proc/acpi/button/lid/LID0/state"
CHECK_INTERVAL=2  # seconds
DATASAVER_SCRIPT="/opt/datasaver-gui/datasaver_gui.py"

restart_network_services() {
    echo "[*] Restarting NetworkManager and wpa_supplicant..."
    systemctl restart NetworkManager
    systemctl restart wpa_supplicant.service
}

apply_datasaver() {
    echo "[*] Re-applying datasaver settings..."
    python3 "$DATASAVER_SCRIPT" on
}

is_lid_closed() {
    if [[ -f "$LID_STATE_FILE" ]]; then
        grep -qi "closed" "$LID_STATE_FILE"
        return $?
    else
        echo "[!] Lid state file not found: $LID_STATE_FILE"
        return 1
    fi
}

monitor_lid() {
    echo "[*] Starting lid monitor in background..."
    lid_was_closed=false
    while true; do
        if is_lid_closed; then
            closed=true
        else
            closed=false
        fi

        if $lid_was_closed && ! $closed; then
            notify-send "Lid Opened" "Re-applying datasaver settings..."
            restart_network_services
            apply_datasaver
        fi

        lid_was_closed=$closed
        sleep "$CHECK_INTERVAL"
    done
}

start_tray_icon() {
    yad --notification \
        --image=network-wireless \
        --text="Datasaver Monitor" \
        --command="notify-send 'Datasaver' 'Tray icon clicked. Lid monitor running in background...'" &
}

# Main
if [[ $EUID -ne 0 ]]; then
    echo "[-] This script must be run as root."
    exit 1
fi

start_tray_icon
monitor_lid

