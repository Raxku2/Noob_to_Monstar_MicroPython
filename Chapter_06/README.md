<h1 align="center">👻 Phase 06: System Override & Memory Hacks 🧠</h1>

<p align="center">
<a href="\#"><img src="https://img.shields.io/badge/Language-MicroPython-3776AB?style=flat-square\&logo=python\&logoColor=white" alt="MicroPython Badge"></a>
<a href="\#"><img src="https://img.shields.io/badge/Concept-Architecture-5C5C5C?style=flat-square\&logo=linux\&logoColor=white" alt="Architecture Badge"></a>
</p>

> *"Desktop computers have Gigabytes of RAM; they forgive sloppy code. Your microcontroller has Kilobytes. If you code like a desktop developer, your hardware will choke and die. This is how you control the machine's brain, manage its memory, and survive."*

Welcome to the real engineering underground. We aren't touching sensors or blinking lights yet. This module is about the invisible mechanics of your microcontroller: how it wakes up, how it reads files, and how it avoids drowning in its own data. If your board keeps crashing after running for 2 hours, the solution isn't physical, it's right here.

-----

## 🚀 THE WAKE-UP SEQUENCE (`boot.py` vs `main.py`)

When you plug power into your board, it doesn't just start running your code blindly. It follows a strict two-step startup sequence.

### 1\. `boot.py` (The BIOS)

This file runs the millisecond your board gets power. It is the "under-the-hood" initialization script.

  * **What to do here:** Keep it incredibly short. Setup the Wi-Fi connection, mount the file system, or configure deep-sleep wake reasons.
  * **What NOT to do here:** **Never** put infinite `while True:` loops in `boot.py`. If you do, the board will get stuck here, `main.py` will never run, and you might have to hard-erase the firmware to save it.

### 2\. `main.py` (The Payload)

Once `boot.py` finishes, the system automatically looks for `main.py` and executes it.

  * **What to do here:** This is your actual project. Your sensor reading, your webhooks, your primary `while True:` heartbeat loop. Everything lives here.

-----

## 🧹 MEMORY ASSASSINATION (`gc` & `del`)

In standard Python, you create variables, use them, and forget about them. On a microcontroller, forgotten variables become "Ghosts in the RAM," eating up memory until the system throws a `MemoryError` and crashes.

### The `gc` Module (The Janitor)

The Garbage Collector (`gc`) is a built-in cleaner that hunts down dead variables and frees up RAM. However, if you let the system run the janitor automatically, your CPU will randomly "freeze" for a few milliseconds while it cleans.

  * **The Hacker Rule:** Don't let the system surprise you. Run the garbage collector manually at the *end* of your loop so you control exactly when the system pauses.

<!-- end list -->

```python
import gc

# Check how much free RAM you have before your loop
print(f"Free RAM: {gc.mem_free()} bytes")

while True:
    payload = "{"data": "massive_string_that_takes_up_memory"}"
    # Send payload to server...
    
    # Manually trigger the janitor at a safe time
    gc.collect() 
```

### The `del` Keyword (The Assassin)

If you download a massive JSON file from an API and extract the one string you need, the massive JSON file is still sitting in your RAM. Don't wait for the janitor. Kill it immediately using `del`.

```python
import gc

raw_api_response = get_massive_data() # Takes up 20KB of RAM
my_target_value = raw_api_response["critical_data"]

# Assassinate the massive variable to free RAM instantly
del raw_api_response
gc.collect() # Sweep up the body
```

### Variable Reusability (The "Lego Block" Method)

Creating a *new* object in memory is highly taxing. Overwriting an *existing* object is basically free.

  * **Bad:** `buffer = []` (Creates a brand new list in memory every time it loops).
  * **Elite:** `buffer.clear()` (Empties the existing list, keeping the same memory block perfectly intact).

-----

## 🗄️ THE VIRTUAL HARD DRIVE (`os` module)

Your microcontroller has an internal flash memory drive. You usually view it using Thonny's left-hand sidebar. But what if your code needs to check if a configuration file exists before trying to read it? You use the `os` (Operating System) module.

  * **`os.listdir()`**: Lists all files and folders on the board.
  * **`os.remove('filename')`**: Deletes a file. Great for clearing out old error logs automatically so your board's hard drive doesn't fill up and crash.
  * **`os.stat('filename')`**: Gets file info (like size). Use this to check if your `error_log.txt` is getting too big\!

<!-- end list -->

```python
import os

files = os.listdir()
print(files)  # Output: ['boot.py', 'main.py', 'config.json']

# Prevent crashing: Only try to open the file if it actually exists!
if 'config.json' in files:
    print("Config found. Booting normal mode.")
else:
    print("No config found! Booting setup mode.")
```

-----

## 🛑 SYSTEM BAILOUTS (`sys` module)

Sometimes things go catastrophically wrong, or you need to know exactly what hardware you are running on dynamically.

  * **`sys.platform`**: Returns the board type (e.g., `'esp8266'` or `'rp2'`). Perfect if you write one script and want it to run differently depending on which board you flashed it to.
  * **`sys.exit()`**: The emergency rip-cord. If a critical component fails (like a database password missing), use this to gracefully kill the script rather than letting it spew errors forever.

<!-- end list -->

```python
import sys

# Dynamic hardware adaptation (Lego Block engineering)
if sys.platform == 'esp8266':
    print("Loaded ESP8266 specific drivers")
elif sys.platform == 'esp32':
    print("Loaded ESP32 specific drivers")

# Fatal error handling
if not wifi_connected_after_10_tries:
    print("FATAL: Network unreachable. Halting system.")
    sys.exit() # Kills the script cleanly
```

-----
