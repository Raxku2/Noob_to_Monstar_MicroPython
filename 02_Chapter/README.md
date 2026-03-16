<h1 align="center">📦 Phase 02: Data Structures & Manipulation 🧬</h1>

<p align="center">
<a href="#"><img src="https://img.shields.io/badge/Language-MicroPython-3776AB?style=flat-square&logo=python&logoColor=white" alt="MicroPython Badge"></a>
<a href="#"><img src="https://img.shields.io/badge/Concept-Data_Structures-5C5C5C?style=flat-square&logo=matrix&logoColor=white" alt="Data Structures Badge"></a>
</p>

> *"Memory mapping initialized. Organizing, buffering, and parsing incoming data payloads efficiently to save CPU cycles and prevent RAM fragmentation."*

Once data is in memory, it must be structured and manipulated. In MicroPython and IoT applications, managing lists (buffers/queues) and dictionaries (JSON payloads) efficiently is critical to keeping the microcontroller running smoothly without crashing or halting for Garbage Collection.

---

## 📊 LISTS (Arrays & Data Buffers)

Lists are ordered sequences, heavily used for buffering sensor data or creating task queues.

### 1. Adding Data (Sensor Readings, Payloads)

* **`append(x)`**: Adds an item to the end of the list.
* *IoT Use Case:* Continuously recording sensor data (e.g., temperature readings) into a buffer before sending it to a cloud server via MQTT or HTTP.


* **`extend(iterable)`**: Appends all items from an iterable to the end.
* *IoT Use Case:* Concatenating incoming data packets or merging a batch of new sensor readings into your main transmission queue.


* **`insert(i, x)`**: Inserts an item at a given position `i`.
* *IoT Use Case:* Maintaining priority queues (e.g., inserting a high-priority "system alert" message at the front of a queue).
* ⚠️ *MicroPython Warning:* Use sparingly. Inserting at the beginning/middle forces the MCU to shift elements in memory, consuming CPU cycles.



### 2. Removing Data (Processing Queues, Memory Management)

* **`pop([i])`**: Removes and returns the item at the given position (defaults to the last item).
* *IoT Use Case:* Processing data. `pop(0)` treats the list like a FIFO queue for network commands, while `pop()` (LIFO) handles stack-based state machines.


* **`clear()`**: Removes all items from the list.
* *IoT Use Case:* **Crucial for memory management.** Reusing a buffer via `.clear()` prevents memory fragmentation and stops the Garbage Collector from pausing your CPU, unlike re-declaring a list `[]`.


* **`remove(x)`**: Removes the first item equal to `x`.
* *IoT Use Case:* Managing lists of connected clients or active tasks (e.g., removing a disconnected device ID).



### 3. Searching and Analyzing Data

* **`index(x)`**: Returns the zero-based index of the first item equal to `x`.
* *IoT Use Case:* Parsing serial/UART data to find a specific start-byte or delimiter.


* **`count(x)`**: Returns the number of times `x` appears.
* *IoT Use Case:* Analyzing a data window (e.g., counting how many times an error code appeared in the last 60 readings).



### 4. Organizing Data

* **`sort()`**: Sorts the items in place.
* *IoT Use Case:* Filtering noisy sensor data. Sort a batch of readings and slice off the highest/lowest values to eliminate outliers.


* **`reverse()`**: Reverses the elements in place.
* *IoT Use Case:* Iterating through time-series data backward (newest to oldest) without creating a duplicate in RAM.



### 💻 The Script: Lists (`main.py`)

```python
numbers = [1, 2, 3, 4, 4, 5]

# numbers.append(6)
another_numbers = [6, 7, 8, 9]

# numbers.extend(another_numbers)
# numbers.insert(4, 11)
# numbers.pop()
# numbers.pop(2)
# numbers.clear()
# numbers.remove(2)
# numbers.sort(reverse=True)
# numbers.reverse()

print(numbers)

```

---

## 🗂️ DICTIONARIES (Key-Value Pairs & JSON)

Dictionaries map keys to values. In IoT, they are the backbone of handling configuration files and parsing incoming/outgoing JSON payloads.

### 1. Data Retrieval (Parsing Payloads)

* **`get(key[, default])`**: Returns the value for `key` if it exists, otherwise returns a default value.
* *IoT Use Case:* **The most important dict method.** When receiving JSON payloads via MQTT/HTTP, you can never guarantee perfect formation. Using `.get("temperature", 20.0)` prevents a fatal `KeyError` crash if a sensor fails to send that data point.



### 2. Iterating (Formatting for Transmission)

* **`items()`**: Returns a view of the key-value pairs.
* *IoT Use Case:* Formatting data to send out (e.g., looping through mapped sensor pins and their read values to build a JSON object).


* **`keys()` & `values()**`: Returns views of just keys or just values.
* *IoT Use Case:* Validating an incoming command payload to ensure it contains only authorized fields before processing.



### 3. Removing Data (Task Processing & RAM Management)

* **`pop(key[, default])`**: Removes the specified key and returns its value.
* *IoT Use Case:* Processing mixed payloads. Extract an action command (`payload.pop("command")`) to process it, leaving only metadata in the dictionary for logging.


* **`clear()`**: Removes all items from the dictionary.
* *IoT Use Case:* **RAM optimization.** When building a dictionary for sensor readings before JSON serialization, use `.clear()` on every loop instead of `{}` to reuse the existing memory block and prevent Garbage Collection halts.



### 💻 The Script: Dictionaries (`main.py`)

```python
config = {"sleep_time": 10, "mode": "eco"}

# print(config.items())
# print(config.keys())
# print(config.values())
# print(config.get('mode'))
# print(config.pop('mode'))
# print(config)

config.clear()

```