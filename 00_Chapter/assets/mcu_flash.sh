#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -e

# ==========================================
# Color formatting for verbose output
# ==========================================
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}==========================================${NC}"
echo -e "${CYAN}    MicroPython ESP Flashing Utility      ${NC}"
echo -e "${CYAN}==========================================${NC}"

# ==========================================
# 1. Dependency Check
# ==========================================
echo -e "\n[*] Checking for esptool..."
if ! command -v esptool &> /dev/null; then
    if command -v esptool.py &> /dev/null; then
        ESPTOOL_CMD="esptool.py"
    else
        echo -e "${RED}[-] Error: esptool is not installed or not in your PATH.${NC}"
        echo -e "    Install it using: pip install esptool"
        exit 1
    fi
else
    ESPTOOL_CMD="esptool"
fi
echo -e "${GREEN}[+] Found $ESPTOOL_CMD!${NC}"

# ==========================================
# 2. Port Auto-Detection
# ==========================================
echo -e "\n[*] Scanning for connected devices..."
ports=()

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    for port in /dev/ttyUSB* /dev/ttyACM*; do
        [ -e "$port" ] && ports+=("$port")
    done
elif [[ "$OSTYPE" == "darwin"* ]]; then
    for port in /dev/cu.usbserial* /dev/cu.usbmodem*; do
        [ -e "$port" ] && ports+=("$port")
    done
else
    echo -e "${RED}[-] Unsupported OS for auto-detection. Please specify manually.${NC}"
    exit 1
fi

TARGET_PORT=""

if [ ${#ports[@]} -eq 0 ]; then
    echo -e "${RED}[-] No serial ports detected. Please ensure your device is plugged in.${NC}"
    exit 1
elif [ ${#ports[@]} -eq 1 ]; then
    TARGET_PORT="${ports[0]}"
    echo -e "${GREEN}[+] Auto-detected single device on port: $TARGET_PORT${NC}"
else
    echo -e "${YELLOW}[?] Multiple devices detected. Please select the correct port:${NC}"
    PS3="Enter the number of your choice: "
    select p in "${ports[@]}"; do
        if [ -n "$p" ]; then
            TARGET_PORT="$p"
            echo -e "${GREEN}[+] Selected port: $TARGET_PORT${NC}"
            break
        else
            echo -e "${RED}[-] Invalid selection. Please try again.${NC}"
        fi
    done
fi

# ==========================================
# 3. Action Menu
# ==========================================
echo -e "\n${YELLOW}[?] What would you like to do with the device on $TARGET_PORT?${NC}"
echo "  1) Erase flash"
echo "  2) Install new firmware (.bin)"
# Added -e here for arrow-key support
read -e -p "Enter choice (1 or 2): " ACTION_CHOICE

# ==========================================
# 4. Execute User Choice
# ==========================================
if [ "$ACTION_CHOICE" == "1" ]; then
    
    echo -e "\n[*] Initiating flash erase on $TARGET_PORT..."
    set +e 
    $ESPTOOL_CMD --port "$TARGET_PORT" erase_flash
    set -e
    echo -e "${GREEN}[+] Erase complete!${NC}"

elif [ "$ACTION_CHOICE" == "2" ]; then
    
    echo -e "\n${YELLOW}[?] Please provide the path to your firmware file.${NC}"
    echo -e "    (Tip: You can use TAB to autocomplete paths or drag-and-drop the file)"
    
    # -e enables Readline (arrow keys, backspace, and TAB completion!)
    read -e -p "Firmware path: " BIN_PATH

    # --- INPUT CLEANUP MAGIC ---
    # 1. Remove leading/trailing spaces (handles drag-and-drop trailing spaces)
    BIN_PATH="${BIN_PATH#"${BIN_PATH%%[![:space:]]*}"}"
    BIN_PATH="${BIN_PATH%"${BIN_PATH##*[![:space:]]}"}"
    
    # 2. Strip single quotes (') if terminal auto-added them
    BIN_PATH="${BIN_PATH#\'}"
    BIN_PATH="${BIN_PATH%\'}"
    
    # 3. Strip double quotes (") just in case
    BIN_PATH="${BIN_PATH#\"}"
    BIN_PATH="${BIN_PATH%\"}"
    
    # 4. Expand tilde (~) to full home directory path
    BIN_PATH="${BIN_PATH/#\~/$HOME}"
    # ---------------------------

    if [ ! -f "$BIN_PATH" ]; then
        echo -e "${RED}[-] Error: The file '$BIN_PATH' does not exist. Aborting.${NC}"
        exit 1
    fi

    echo -e "\n[*] Installing firmware from '$BIN_PATH' onto $TARGET_PORT..."
    set +e
    $ESPTOOL_CMD --port "$TARGET_PORT" --baud 460800 write_flash --flash_size=detect 0 "$BIN_PATH"
    set -e
    echo -e "${GREEN}[+] Firmware installation finished!${NC}"

else
    echo -e "${RED}[-] Invalid choice. Please run the script again and select 1 or 2.${NC}"
    exit 1
fi

echo -e "\n${CYAN}Done. Have a great day!${NC}"
