<h1 align="center">💻 Phase 00: Initialization & Setup ⚙️</h1>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/OS-Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux Badge"></a>
  <a href="#"><img src="https://img.shields.io/badge/Tool-esptool-5C5C5C?style=flat-square&logo=gnu-bash&logoColor=white" alt="esptool Badge"></a>
  <a href="#"><img src="https://img.shields.io/badge/Hardware-ESP8266-2EA043?style=flat-square&logo=espressif&logoColor=white" alt="ESP8266 Badge"></a>
</p>

# 💻 Chapter 00: Installation & Setup
> *"Boot sequence initiated. Preparing the Linux environment and flashing the core logic."*

This guide covers the necessary steps to set up your Linux environment for ESP8266 development and how to flash the MicroPython firmware using our custom automated script.

---

## 📂 SYSTEM ASSETS
Before beginning, ensure you have the required firmware and flashing utility. Both are located in the local `assets` directory:

* 📁 [**`./assets/`**](./assets/)
  * 💾 [`ESP8266_GENERIC-20250415-v1.25.0.bin`](./assets/ESP8266_GENERIC-20250415-v1.25.0.bin) *(MicroPython Firmware)*
  * 📜 [`mcu_flash.sh`](./assets/mcu_flash.sh) *(Custom Flashing Utility)*

---

## 🛠️ ENVIRONMENT PREPARATION
Before connecting your ESP8266, ensure your Linux environment is prepared with the necessary tools and user permissions.

### 1. Install System Dependencies
We use the system package manager to install `esptool`, avoiding conflicts with managed Python environments. Open your terminal and execute:
```bash
sudo apt update
sudo apt install esptool

```

### 2. Configure Serial Permissions

To allow your user account to communicate with serial ports (like `/dev/ttyUSB0`) without requiring root access every time, add your user to the `dialout` group:

```bash
sudo usermod -a -G dialout $USER

```

> ⚠️ **CRITICAL:** You must log out and log back in (or restart your system) for this permission change to take effect.

### 3. Initialize the IDE

We use **Thonny** for writing and uploading MicroPython code. Install it using the official bash script to ensure you get the latest version tailored for your system:

* Navigate to [thonny.org](https://thonny.org) and follow the Linux installation instructions provided on the homepage.

---

## ⚡ FLASHING THE FIRMWARE

We use a custom, interactive bash script (`mcu_flash.sh`) to streamline the erasing and flashing process via `esptool`.

### Step-by-Step Execution

1. **Download the Firmware:** Ensure you have the latest ESP8266 MicroPython `.bin` file in your working directory (available in the `./assets` folder linked above).
2. **Connect the Device:** Plug your ESP8266 into your computer via a data-capable USB cable.
3. **Make the Script Executable:**
```bash
chmod +x ./assets/mcu_flash.sh

```


4. **Run the Flashing Utility:**
```bash
./assets/mcu_flash.sh

```



### Expected Telemetry (Output)

The script will auto-detect your connected device and prompt you for the action. Select option `2` to install new firmware and provide the path to your `.bin` file.

```console
==========================================
    MicroPython ESP Flashing Utility      
==========================================

[*] Checking for esptool...
[+] Found esptool!

[*] Scanning for connected devices...
[+] Auto-detected single device on port: /dev/ttyUSB0

[?] What would you like to do with the device on /dev/ttyUSB0?
  1) Erase flash
  2) Install new firmware (.bin)
Enter choice (1 or 2): 2

[?] Please provide the path to your firmware file.
    (Tip: You can use TAB to autocomplete paths or drag-and-drop the file)
Firmware path: ./assets/ESP8266_GENERIC-20250415-v1.25.0.bin

[*] Installing firmware from './assets/ESP8266_GENERIC-20250415-v1.25.0.bin' onto /dev/ttyUSB0...
esptool.py v4.7.0
Serial port /dev/ttyUSB0
Connecting....
Detecting chip type... ESP8266
Chip is ESP8266EX
...
Auto-detected Flash size: 4MB
Flash will be erased from 0x00000000 to 0x0009bfff...
Flash params set to 0x0040
Compressed 636820 bytes to 426256...
Wrote 636820 bytes (426256 compressed) at 0x00000000 in 10.1 seconds (effective 502.8 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
[+] Firmware installation finished!

Done. Have a great day!

```

> 🟢 *Once you see the `Hash of data verified` and `Firmware installation finished!` messages, your ESP8266 is successfully running MicroPython and is ready to be connected to Thonny.*

```