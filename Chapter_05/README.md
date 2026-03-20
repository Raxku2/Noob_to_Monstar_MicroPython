<h1 align="center">🛠️ Phase 05: Functions & Recursion 🪃</h1>

<p align="center">
<a href="\#"><img src="[https://img.shields.io/badge/Language-MicroPython-3776AB?style=flat-square\&logo=python\&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Language-MicroPython-3776AB%3Fstyle%3Dflat-square%26logo%3Dpython%26logoColor%3Dwhite)" alt="MicroPython Badge"></a>
<a href="\#"><img src="[https://img.shields.io/badge/Concept-Modularity-5C5C5C?style=flat-square\&logo=matrix\&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Concept-Modularity-5C5C5C%3Fstyle%3Dflat-square%26logo%3Dmatrix%26logoColor%3Dwhite)" alt="Modularity Badge"></a>
</p>

> *"Subroutines defined. Encapsulating logic into modular, reusable blocks to optimize memory and keep the system architecture clean."*

Writing code line-by-line is fine for a quick test, but complex firmware requires modularity. Functions (or subroutines) allow you to write a block of logic once and call it infinitely. This adheres to the **DRY** (Don't Repeat Yourself) principle, saving precious flash memory on your microcontroller and making your code infinitely easier to debug.

-----

## 🏗️ FUNCTION ANATOMY & DECLARATION

In MicroPython, functions are defined using the `def` keyword, followed by the function name, parentheses, and a colon.

### 1\. The Basic Function & Multiple Returns

A function can take inputs, perform operations, and `return` an output.

  * **IoT Pro-Tip:** MicroPython functions can easily return multiple values (as a tuple). This is incredibly useful for sensors that read multiple metrics at once.

<!-- end list -->

```python
# main.py - Basic Function
def read_dht_sensor():
    # Simulated sensor logic
    temp = 24.5
    humidity = 60
    return temp, humidity  # Returns a tuple: (24.5, 60)

# Unpacking the returned values
current_temp, current_hum = read_dht_sensor()
```

-----

## 🎛️ ARGUMENTS & PARAMETERS

Functions become powerful when you pass data into them. MicroPython supports several ways to handle arguments.

### 1\. Positional Arguments

The most common type. The order in which you pass the arguments matters.

```python
def set_led_color(red, green, blue):
    print(f"Setting color to R:{red} G:{green} B:{blue}")

set_led_color(255, 0, 128) # Order is strictly R, G, B
```

### 2\. Keyword (Default) Arguments

You can assign default values to parameters. If the caller doesn't provide them, the function uses the defaults. Perfect for configuration settings.

```python
def connect_wifi(ssid, retries=5, timeout=10):
    print(f"Connecting to {ssid}. Max retries: {retries}")

connect_wifi("CyberNet")              # Uses default retries (5)
connect_wifi("CyberNet", retries=10)  # Overrides default retries
```

### 3\. Arbitrary Arguments (`*args` and `**kwargs`)

Sometimes you don't know how many items you need to process.

  * `*args`: Gathers remaining positional arguments into a **Tuple**. Great for processing a dynamic list of sensor pins.
  * `**kwargs`: Gathers remaining keyword arguments into a **Dictionary**. Great for passing dynamic JSON configuration payloads.

<!-- end list -->

```python
def log_sensor_data(sensor_id, *readings, **metadata):
    print(f"ID: {sensor_id}")
    print(f"Data: {readings}")      # Tuple of all unnamed arguments
    print(f"Meta: {metadata}")      # Dict of all named arguments

log_sensor_data("TEMP_01", 22.1, 22.4, 22.5, location="Server Room", status="Active")
```

-----

## 🌐 VARIABLE SCOPE (`global`)

Variables created *inside* a function are **local** (they die when the function ends to save RAM). Variables created *outside* are **global**.

If a function needs to modify a global variable (like a system-wide state flag or an interrupt counter), you must explicitly use the `global` keyword.

```python
system_armed = False

def toggle_alarm():
    global system_armed  # Pull the global variable into this function's scope
    system_armed = not system_armed
```

-----

## ⚡ LAMBDA FUNCTIONS (Anonymous Subroutines)

A `lambda` is a small, one-line function without a name. In embedded programming, these are frequently used as quick "callback" functions for hardware timers or button interrupts where defining a full `def` block is overkill.

```python
# Syntax: lambda arguments: expression

# Normal function:
# def square(x): return x * x

# Lambda equivalent:
square = lambda x: x * x

# Common IoT Use Case: Quick callback mapping
button.irq(trigger=Pin.IRQ_FALLING, handler=lambda p: print("Intruder detected!"))
```

-----

## 🪃 RECURSION

Recursion occurs when a function calls **itself** to solve a smaller piece of a problem. It consists of two main parts:

1.  **The Base Case:** The condition that stops the recursion. (Without this, it loops forever).
2.  **The Recursive Step:** The function calling itself with modified data.

<!-- end list -->

```python
def calculate_factorial(n):
    # 1. Base Case: Stop at 1
    if n == 1:
        return 1
    # 2. Recursive Step: n * factorial of (n-1)
    else:
        return n * calculate_factorial(n - 1)

print(calculate_factorial(5)) # Outputs: 120
```

### ⚠️ THE RECURSION WARNING (Hardware Constraint)

In standard Python, recursion is a powerful tool for traversing directories or complex data trees. **In MicroPython, use it with extreme caution.**

Microcontrollers have very limited RAM. Every time a function calls itself, the system must save the current state to the "Call Stack" in memory. If the recursion goes too deep, you will cause a **Stack Overflow**, resulting in a fatal `RuntimeError: maximum recursion depth exceeded` and crashing your board. For embedded systems, an iterative `while` or `for` loop is almost always safer and more memory-efficient than recursion.

-----
