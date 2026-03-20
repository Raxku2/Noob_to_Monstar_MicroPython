<h1 align="center">⚔️ Phase 02\_Practice: The Data Forge Crucible 🛡️</h1>

<p align="center">
<a href="\#"><img src="[https://img.shields.io/badge/Language-MicroPython-3776AB?style=flat-square\&logo=python\&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Language-MicroPython-3776AB%3Fstyle%3Dflat-square%26logo%3Dpython%26logoColor%3Dwhite)" alt="MicroPython Badge"></a>
<a href="\#"><img src="[https://img.shields.io/badge/Status-Hardcore\_Mode-D22128?style=flat-square\&logo=hackthebox\&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Status-Hardcore_Mode-D22128%3Fstyle%3Dflat-square%26logo%3Dhackthebox%26logoColor%3Dwhite)" alt="Challenge Badge"></a>
</p>

> *"Simulation escalated. You now have the complete architectural toolkit: data structures, control flows, and modular subroutines. This gauntlet will test your ability to synthesize these components into complex, unbreakable logic."*

These challenges require combining everything you have learned: variables, dictionaries, lists, loops, conditionals, and advanced function parameters (`*args`, `**kwargs`, `global`, and recursion). **Do not use any external libraries.** Pure MicroPython logic only.

-----

## 🎯 THE CHALLENGES

### Challenge 01: The Corrupted Payload Parser

**Objective:** Master dictionary manipulation (`.get()`), list operations, loops, and conditionals.

**The Scenario:**
You are receiving a raw, unreliable stream of data payloads from a network of sensors. Some payloads are missing keys, and some are throwing errors.

```python
raw_payloads = [
    {"id": 1, "temp": 22.5, "status": "OK"},
    {"id": 2, "status": "ERROR", "error_code": 404},
    {"id": 3, "temp": 25.1, "status": "OK"},
    {"id": 4, "temp": -99, "status": "OK"}, # Faulty reading
    {"id": 5, "status": "OK"}               # Missing temp key entirely
]
```

**Your Task:**
Write a function `sanitize_payloads(payload_list)` that iterates through the list.

1.  If the `"status"` is not `"OK"`, skip the payload entirely.
2.  Use `.get()` to extract the `"temp"`. If the key doesn't exist, default it to `0.0`.
3.  If the temperature is valid (between `0.0` and `50.0`), append it to a new `clean_temps` list.
4.  Return the sorted `clean_temps` list in descending order.

-----

### Challenge 02: The Global Multiplexer

**Objective:** Handle variable scopes (`global`), arbitrary arguments (`*args`, `**kwargs`), and list mapping.

**The Scenario:**
You have a global system calibration multiplier that occasionally updates, and a logging function that must handle an unpredictable number of incoming readings.

**Your Task:**

1.  Define a global variable: `CALIBRATION_FACTOR = 1.5`
2.  Write a function `process_telemetry(*readings, **config)`.
3.  Inside the function, multiply every reading in `*readings` by the `CALIBRATION_FACTOR`. (Hint: You can use a `for` loop or `map()`).
4.  Check the `**config` dictionary. If `config.get("strict_mode")` is `True`, filter out any calibrated readings that exceed `100.0`.
5.  Return the final list of processed readings.

*Test your function with:* `process_telemetry(10, 50, 80, 25, strict_mode=True, location="Sector 7")`

-----

### Challenge 03: The Nested Cipher (Recursion)

**Objective:** Safely implement a recursive function, combine it with `type()` checking, and manage lists.

**The Scenario:**
A critical data packet arrived heavily fragmented and nested within multiple layers of arrays.

```python
fragmented_data = [1, [2, 3], [[4], 5], 6, [[[7]]]]
```

**Your Task:**
Write a recursive function `flatten_data(nested_list)` that breaks this down into a single, flat list: `[1, 2, 3, 4, 5, 6, 7]`.

  * *Hint:* Create an empty list `flat = []` inside the function. Loop through each item in `nested_list`. Use `if type(item) is list:` to check if the current item is another list. If it is, recursively call `flatten_data(item)` and `.extend()` the result into `flat`. Otherwise, just `.append()` the item.

-----

### Challenge 04: The Lambda Anomaly

**Objective:** Write highly condensed, functional code using `lambda`, `filter()`, `map()`, and the ternary operator.

**The Scenario:**
CPU cycles are critical, and you have exactly two lines of code to clean a raw array of voltage spikes.

```python
raw_voltages = [-5.0, 12.5, 105.0, 8.2, 0.0]
```

**Your Task:**
Without using any `def` functions or `for` loops:

1.  Create a variable `positive_only` and assign it the result of using `filter()` and a `lambda` to strip out any values less than or equal to `0.0`.
2.  Create a variable `capped_voltages` and assign it the result of using `map()` and a `lambda` with a **ternary operator** (`x if condition else y`) to cap the remaining values at `24.0` (i.e., if a value is greater than 24.0, change it to 24.0).
3.  Print `capped_voltages` as a list.

-----
