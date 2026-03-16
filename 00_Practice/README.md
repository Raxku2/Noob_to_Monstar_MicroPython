<h1 align="center">🚀 Phase 00_Practice: First Run 🌍</h1>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Language-MicroPython-3776AB?style=flat-square&logo=python&logoColor=white" alt="MicroPython Badge"></a>
  <a href="#"><img src="https://img.shields.io/badge/IDE-Thonny-5C5C5C?style=flat-square&logo=databricks&logoColor=white" alt="Thonny Badge"></a>
  <a href="#"><img src="https://img.shields.io/badge/Hardware-ESP8266-2EA043?style=flat-square&logo=espressif&logoColor=white" alt="ESP8266 Badge"></a>
</p>

> *"Uplink established. Executing the first continuous loop directly on the hardware."*

This guide walks you through connecting your IDE to the flashed ESP8266, creating the main boot file, and running your very first script.

---

## 🔌 ESTABLISHING THE CONNECTION

1. **Launch the IDE:** Open Thonny on your system.
2. **Switch the Interpreter:** Look at the **bottom right corner** of the Thonny window. Click on the text displaying your local Python version (e.g., "Local Python 3") and change it to **MicroPython (ESP8266)**.


---

## 💾 WRITING THE SCRIPT

1. Locate the **Files** pane on the left side of Thonny.
2. Under the **MicroPython device** section, create a new file and name it `main.py`. 
3. Open `main.py` and paste the following script:

```python
from utime import sleep

while 1:
    print('Good byee world')
    sleep(1)

```

---

## ⚡ EXECUTION & CONTROL

* **Execute:** Click the green **"Run current script"** button in the top toolbar, or simply press `F5` on your keyboard. You will see the text begin to stream in the Shell below.
* **Abort:** To break the loop and regain control of the hardware prompt, click inside the Shell area and press `Ctrl+C` on your keyboard.


