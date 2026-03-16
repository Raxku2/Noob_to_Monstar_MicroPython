<h1 align="center">🔀 Phase 03: Conditional Statements 🚦</h1>

<p align="center">
<a href="#"><img src="[https://img.shields.io/badge/Language-MicroPython-3776AB?style=flat-square&logo=python&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Language-MicroPython-3776AB%3Fstyle%3Dflat-square%26logo%3Dpython%26logoColor%3Dwhite)" alt="MicroPython Badge"></a>
<a href="#"><img src="[https://img.shields.io/badge/Concept-Control_Flow-5C5C5C?style=flat-square&logo=matrix&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Concept-Control_Flow-5C5C5C%3Fstyle%3Dflat-square%26logo%3Dmatrix%26logoColor%3Dwhite)" alt="Control Flow Badge"></a>
</p>

> *"Decision matrix engaged. Routing execution flow based on real-time sensor telemetry and hardware states."*

Conditionals are the "brain" of any microcontroller. Without them, a script just runs top-to-bottom and stops. With conditionals, your ESP8266 can react to its environment—turning on a fan when it gets too hot, connecting to backup Wi-Fi if the main network drops, or putting the system to sleep when the battery is low.

---

## 🧮 CONDITIONAL OPERATORS

Before branching logic, the system needs to evaluate statements to `True` or `False`.

* **Comparison:** * `==` (Equal to), `!=` (Not equal to)
* `>` (Greater than), `<` (Less than)
* `>=` (Greater than or equal), `<=` (Less than or equal)


* **Logical:** * `and` (True if BOTH are true)
* `or` (True if AT LEAST ONE is true)
* `not` (Inverts the boolean state)


* **Identity & Membership:**
* `is` (Checks if two variables point to the exact same object in memory)
* `in` (Checks if a value exists within a list, string, or dictionary)



---

## 💻 IMPLEMENTATION & IOT USE CASES

Here are the different ways to structure decision-making in MicroPython, alongside exactly when you should use them in real-world hardware projects.

### 1. The Basic `if` (The Sentinel)

* **Concept:** Executes a block of code only if a specific condition is met. Does nothing otherwise.
* **IoT Use Case:** Emergency interrupts and critical thresholds. Use this when you only care about anomalous events (e.g., detecting a gas leak or a button press) and want the system to ignore normal operations.

```python
# main.py - Basic IF
gas_level = read_mq2_sensor()

if gas_level > 800:
    trigger_siren()
    send_alert_email()

```

### 2. The `if-else` (The Binary Switch)

* **Concept:** Provides a primary path and a guaranteed fallback path.
* **IoT Use Case:** Toggling binary hardware states. Perfect for Day/Night modes, On/Off relays, or Connected/Disconnected network states.

```python
# main.py - IF/ELSE
motion_detected = pir_sensor.value()

if motion_detected == 1:
    relay.on()  # Turn on lights
else:
    relay.off() # Keep lights off

```

### 3. The `if-elif-else` Chain (The State Machine)

* **Concept:** Checks multiple, mutually exclusive conditions in sequence. Once one is true, it skips the rest.
* **IoT Use Case:** Handling multi-tier states or device indicators. Commonly used for battery level mapping to RGB LEDs (Green/Yellow/Red) or processing different incoming MQTT command strings.

```python
# main.py - ELIF CHAIN
battery_voltage = get_adc_voltage()

if battery_voltage >= 4.0:
    led.color(0, 255, 0)  # Green
elif battery_voltage >= 3.5:
    led.color(255, 255, 0) # Yellow
else:
    led.color(255, 0, 0)  # Red - Needs charge
    deep_sleep()          # Protect battery

```

### 4. Nested Conditionals (The Verification Gate)

* **Concept:** Placing an `if` statement inside another `if` statement.
* **IoT Use Case:** Multi-step verification. Essential when dealing with network stacks where step B will crash if step A hasn't happened. For example, verifying Wi-Fi is connected *before* checking if the MQTT broker is reachable.

```python
# main.py - NESTED IF
if wifi.isconnected():
    if mqtt_client.ping():
        mqtt_client.publish("sensors/temp", str(temp))
    else:
        mqtt_client.reconnect()
else:
    connect_wifi()

```

### 5. The Shorthand `if` / Ternary Operator (The Payload Formatter)

* **Concept:** A one-line `if-else` statement used strictly for assigning values.
* *Syntax:* `value_if_true if condition else value_if_false`


* **IoT Use Case:** Fast, clean variable assignment. Excellent for formatting JSON payloads, formatting text for an OLED display, or mapping `1`/`0` sensor outputs to human-readable strings without wasting 4 lines of code.

```python
# main.py - TERNARY OPERATOR
water_detected = leak_sensor.value()

# Quick assignment for JSON payload
status_msg = "FLOOD" if water_detected else "DRY"

payload = {"status": status_msg}

```