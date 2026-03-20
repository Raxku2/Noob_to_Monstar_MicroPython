<h1 align="center"\>🛡️ Phase 07: The "Oops" Catcher (Error Handling) 🪂</h1>

<p align="center">
<a href="\#"><img src="https://img.shields.io/badge/Language-MicroPython-3776AB?style=flat-square\&logo=python\&logoColor=white" alt="MicroPython Badge"></a>
<a href="\#"><img src="https://img.shields.io/badge/Concept-Resilience-5C5C5C?style=flat-square\&logo=matrix\&logoColor=white" alt="Resilience Badge"></a>
<a href="\#"><img src="https://img.shields.io/badge/Status-Bulletproof-2EA043?style=flat-square\&logo=hackthebox\&logoColor=white" alt="Bulletproof Badge"></a>
</p>

> *"An elite computer science student writes code that works perfectly in a sterile lab. You are building hardware that will survive power spikes, dropped Wi-Fi signals, and disconnected wires. Crashing is fine. Staying dead is a failure."*

In the real world, IoT devices fail constantly. A sensor wire gets bumped, your home router reboots, or an API server goes down. If you don't anticipate these failures, your MicroPython script will throw a giant red error, the main loop will shatter, and your board will turn into a useless brick until you manually unplug it.

We fix this using **Try / Except** blocks. This is how you build a system that takes a punch to the face and keeps running.

-----

## 🪂 THE ANATOMY OF SURVIVAL

### 1\. The Basic `try / except` (The Safety Net)

Wrap your dangerous code (like connecting to Wi-Fi or reading an I2C sensor) in a `try` block. If it blows up, the script immediately jumps to the `except` block instead of crashing the board.

```python
# main.py
try:
    # ⚠️ DANGEROUS CODE: The sensor wire might be unplugged!
    temperature = dht_sensor.read()
    print(f"Temp is {temperature}")

except Exception as e:
    # 🛡️ THE FALLBACK: This only runs if the 'try' block fails
    print(f"SENSOR OFFLINE! Error details: {e}")
    temperature = "N/A"  # Set a safe default so the rest of the code survives
```

### 2\. Targeted Exceptions (The Sniper)

Catching *everything* with `Exception` is a bit sloppy because it will also catch your own typos. Pro developers catch the *exact* error they are expecting.

```python
try:
    payload = get_api_data()
    # If payload is missing the "temp" key, this throws a KeyError
    val = payload["temp"] 
    # If val is "unknown" instead of a number, this throws a ValueError
    math = int(val) * 2   

except KeyError:
    print("API changed their JSON format! Missing 'temp' key.")
except ValueError:
    print("API sent corrupted text instead of a number!")
```

### 3\. The `finally` Block (The Cleanup Crew)

Code inside `finally` runs **no matter what happens**—whether the `try` succeeds or fails.

  * *IoT Use Case:* If your smart heater loop crashes because of a Wi-Fi error, you want to guarantee the heater relay is turned *off* before the board restarts, so you don't burn your house down.

<!-- end list -->

```python
try:
    heater_relay.on()
    download_large_update() # Network crashes here!
except OSError:
    print("Network failed during update.")
finally:
    # This runs absolutely no matter what.
    heater_relay.off() 
    print("Heater safely disabled.")
```

### 4\. Raising Custom Errors (Throwing Grenades)

Sometimes, the hardware thinks everything is fine, but your *logic* knows it's broken. You can force the system to halt by throwing your own errors using `raise`.

```python
def check_battery(voltage):
    if voltage > 5.0:
        # The code is fine, but the hardware is about to fry. Force a crash!
        raise ValueError("CRITICAL: Overvoltage detected! Halting to save components.")
    return "Battery Normal"
```

-----

## 📜 THE ULTIMATE IOT ERROR CHEAT SHEET

When hacking MicroPython, you will see the same errors repeatedly. Here is the master list of what they mean and how to fix them.

### 🔌 Hardware & Sensor Errors (Usually `OSError`)

In MicroPython, almost all hardware failures fall under the `OSError` umbrella, usually accompanied by an `[Errno]`.

| Error Code | Name | What it means in the real world | How to fix it |
| :--- | :--- | :--- | :--- |
| `OSError: [Errno 19]` | `ENODEV` (No Device) | **The classic I2C error.** The MCU pinged an I2C address, but nothing replied. | Check your wiring. You likely forgot the Pull-Up resistors on the SDA/SCL lines, or the sensor is fried. |
| `OSError: [Errno 110]` | `ETIMEDOUT` | The sensor took too long to reply. | The wire might be too long (capacitance issue), or the sensor needs a few milliseconds of `sleep()` to wake up. |
| `ValueError` | Invalid Pin | You tried to assign a GPIO pin that the board doesn't have. | Check your board's pinout diagram. You might be calling `Pin(99)`. |
| `RuntimeError` | DHT/1-Wire Timeout | Specific to DHT11/22 sensors. The data pulse was missed. | DHT sensors are notoriously slow. Add a `sleep(2)` between reads. |

### 🌐 Network & API Errors (Wi-Fi, HTTP, MQTT)

| Error Code | Name | What it means in the real world | How to fix it |
| :--- | :--- | :--- | :--- |
| `OSError: [Errno 113]` | `EHOSTUNREACH` | Wi-Fi is connected, but the target server/API is dead or blocking you. | Check the API URL. Ensure you aren't blocked by a firewall. |
| `OSError: [Errno 104]` | `ECONNRESET` | The server forcefully hung up the phone on your microcontroller. | You might be sending requests too fast (rate-limited). Slow down your `while` loop. |
| `OSError: [Errno -2]` | DNS/Resolve Error | The board cannot translate "https://www.google.com/search?q=api.weather.com" into an IP address. | Your Wi-Fi router isn't assigning a DNS server. Try pinging `8.8.8.8` directly. |
| `IndexError` | MQTT Tuple Out of Range | Your MQTT callback function received a weirdly formatted packet. | Wrap your MQTT message parsing in a `try/except` so bad packets don't crash the broker connection. |

### 🧠 Memory & System Errors

| Error Code | Name | What it means in the real world | How to fix it |
| :--- | :--- | :--- | :--- |
| `MemoryError` | Out of RAM | You loaded too much data (like a massive JSON payload) and the microcontroller choked. | Use `.clear()` on your lists. Run `gc.collect()`. Stop parsing giant strings. |
| `RuntimeError` | Recursion Depth | A function called itself too many times, blowing up the call stack. | MicroPython limit is very low. Rewrite your recursive function as a `while` loop. |
| `KeyboardInterrupt` | User Abort | You clicked the "Stop" button or pressed `Ctrl+C` in Thonny. | Not a real error\! This is just the IDE telling the board to stop. |
| `ImportError` | Module Not Found | You typed `import requests` but `urequests.py` isn't saved to the board. | Download the required library and save it to the board's virtual hard drive via Thonny. |

### 🧩 Data Parsing & Logic Errors

| Error Code | Name | What it means in the real world | How to fix it |
| :--- | :--- | :--- | :--- |
| `KeyError` | JSON Map Fail | You asked a dictionary for `data["humidity"]`, but that key doesn't exist. | **Always** use `data.get("humidity", 0)` instead of hard brackets for IoT payloads. |
| `TypeError` | Bad Combinations | You tried to do math with a word: `"20" + 5`. | Cast your incoming data\! `int(payload) + 5`. |
| `AttributeError` | Bad Method | You tried to use `.append()` on a String instead of a List. | Check the `type()` of your variable. You might have overwritten it by accident. |
| `SyntaxError` | Typo | You forgot a colon `:` after an `if` statement, or missed a closing parenthesis `)`. | Read the line number Thonny gives you. The error is usually on the line *exactly above* it. |

-----