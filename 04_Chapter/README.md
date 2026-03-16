<h1 align="center">🔁 Phase 04: Loops in Embedded Programming 🔄</h1>

<p align="center">
<a href="#"><img src="[https://img.shields.io/badge/Language-MicroPython-3776AB?style=flat-square&logo=python&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Language-MicroPython-3776AB%3Fstyle%3Dflat-square%26logo%3Dpython%26logoColor%3Dwhite)" alt="MicroPython Badge"></a>
<a href="#"><img src="[https://img.shields.io/badge/Concept-Iteration-5C5C5C?style=flat-square&logo=matrix&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Concept-Iteration-5C5C5C%3Fstyle%3Dflat-square%26logo%3Dmatrix%26logoColor%3Dwhite)" alt="Iteration Badge"></a>
</p>

> *"Continuous execution cycles initialized. Polling sensors, maintaining the system heartbeat, and processing data streams."*

In standard Python scripts, a program runs to the end and exits. In embedded programming, a script that exits means a dead device. Loops are the heartbeat of your microcontroller. They keep the board awake, continuously listening to sensors, checking network traffic, and updating outputs.

---

## ♾️ THE `while` LOOP (The System Heartbeat)

A `while` loop runs as long as its condition evaluates to `True`.

* **`while True:` (or `while 1:`):** The "Super Loop." Every microcontroller project has one of these at the bottom of the script. It is the infinite cycle that keeps the device running forever.
* **Conditional `while`:** Used to halt the system until a specific state is reached (e.g., waiting for Wi-Fi to connect before moving on).

```python
# main.py - The Super Loop
while not wifi.isconnected():
    print("Connecting...")
    sleep_ms(500)

while True:
    read_sensors()
    update_display()
    sleep_ms(100) # Feed the watchdog timer

```

---

## 🔄 THE `for` LOOP (The Iterator)

A `for` loop executes a specific number of times or iterates over a collection of items (like a list or a dictionary).

* **`for i in range(x):`** Best for executing a hardware action a fixed number of times (e.g., blinking an LED 5 times on boot).
* **`for item in iterable:`** Best for scanning. Used to loop through I2C addresses on a bus or iterate through a buffer of recent sensor readings to calculate an average.

```python
# main.py - Iterating over hardware
# Blink LED 3 times
for _ in range(3):
    led.on()
    sleep_ms(200)
    led.off()
    sleep_ms(200)

# Process a batch of sensor readings
for reading in sensor_buffer:
    process_data(reading)

```

---

## 🎛️ LOOP CONTROL (`break`, `continue`, `pass`)

You must be able to control the flow from *inside* the loop.

* **`break`:** Instantly shatters the loop and escapes it entirely. (e.g., Breaking out of a connection loop once the MQTT broker finally responds).
* **`continue`:** Skips the rest of the current cycle and jumps back to the top. (e.g., If a sensor returns a `None` or error value, `continue` to the next reading instead of crashing the math functions below).
* **`pass`:** A null operation. Keeps the syntax valid but does nothing.

---

## ⚡ FUNCTIONAL LOOPS (`map` & `filter`)

In MicroPython, memory and CPU cycles are limited. `map` and `filter` are executed in optimized C code under the hood, making them faster and more memory-efficient than writing standard `for` loops.

### 1. `map(function, iterable)`

Applies a function to every item in an iterable.

* **IoT Use Case:** Applying a calibration formula to a raw array of ADC (Analog-to-Digital) values.

```python
raw_adc = [4095, 2048, 1024, 0]

# Convert 12-bit ADC (0-4095) to Voltage (0-3.3V)
def to_voltage(val):
    return (val / 4095.0) * 3.3

voltages = list(map(to_voltage, raw_adc))

```

### 2. `filter(function, iterable)`

Creates an iterator of elements for which a function returns true.

* **IoT Use Case:** Stripping out erroneous `0`s, `None`s, or out-of-bounds noise from a sensor data buffer before sending the payload.

```python
temp_readings = [22.5, 23.1, -999.0, 22.8, 0.0]

# Filter out dead sensor reads (-999.0 or 0.0)
def is_valid(temp):
    return temp > 0.0

clean_data = list(filter(is_valid, temp_readings))

```

---

## ⚠️ LOOP SURVIVAL GUIDE: Do's & Don'ts

Embedded loops act differently than desktop Python loops. If you write a bad loop, your ESP8266 will crash, run out of RAM, or reboot via the Watchdog Timer (WDT).

### 🟢 WHAT TO DO (Best Practices)

* **DO use Non-Blocking Delays:** Instead of using `time.sleep()` which freezes the entire microcontroller (blocking network traffic and missing button presses), use `time.ticks_ms()` to check elapsed time, letting the loop run freely.
* **DO pre-allocate memory:** Create your lists and dictionaries *outside* the `while True:` loop. Inside the loop, clear them or update them in place to save RAM.
* **DO yield to the RTOS:** Always include at least a `sleep_ms(10)` or `await asyncio.sleep(0)` in infinite loops so the underlying system can process Wi-Fi packets.

### 🔴 WHAT NOT TO DO (Fatal Pitfalls)

* **DON'T allocate memory inside the Super Loop:**
* *Bad:* `while True: buffer = []` (Creates a new list object every millisecond, fragmenting RAM until the Garbage Collector halts the CPU).
* *Good:* `buffer.clear()` inside the loop.


* **DON'T write tight infinite loops without escapes:** `while True: pass` will trigger the hardware Watchdog Timer to reboot the board because the system thinks it has frozen.
* **DON'T block the main thread:** Never put a 10-second `sleep()` inside your main `while` loop if your device is connected to a network, or the server will drop your connection for ping-timeouts.