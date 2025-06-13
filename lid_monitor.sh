#!/bin/bash

# Lid state file (may vary depending on hardware)
LID_STATE_FILE="/proc/acpi/button/lid/LID0/state"
CHECK_INTERVAL=2  # seconds

restart_network_services() {
    echo "[*] Restarting NetworkManager and wpa_supplicant..." 
    systemctl restart NetworkManager wpa_supplicant.service
}

apply_datasaver() {
    echo "[*] Re-applying datasaver settings..."
    /usr/bin/python3 /opt/datasaver/datasaver-cli.py on
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
    echo "[*] Starting lid monitor..."
    lid_was_closed=false
    while true; do
        if is_lid_closed; then
            closed=true
        else
            closed=false
        fi

        if $lid_was_closed && ! $closed; then
            echo "[+] Lid just opened."
            restart_network_services
            apply_datasaver
        fi

        lid_was_closed=$closed
        sleep "$CHECK_INTERVAL"
    done
}

monitor_lid
