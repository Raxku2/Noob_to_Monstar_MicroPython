<h1 align="center">🌡️ Project_03: The Thermal Processor (Temp Converter) ❄️🔥</h1>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Language-MicroPython-3776AB?style=flat-square&logo=python&logoColor=white" alt="MicroPython Badge"></a>
  <a href="#"><img src="https://img.shields.io/badge/Concept-Mathematical_Mapping-5C5C5C?style=flat-square&logo=matrix&logoColor=white" alt="Math Mapping Badge"></a>
  <a href="#"><img src="https://img.shields.io/badge/Status-Calculation_Ready-2EA043?style=flat-square&logo=hackthebox&logoColor=white" alt="Ready Badge"></a>
</p>

> *"Data is raw; information is processed. A sensor might give you a value in Celsius, but your user might need Kelvin. This project is about building the mathematical engine that powers real-world weather stations and industrial monitors."*

Welcome to the Thermal Processor. In this project, you are transitioning from simple data management to **Mathematical Mapping**. You are building a high-precision converter that handles the four most common temperature transitions used in science and engineering.

This project proves you can handle floating-point arithmetic, user-defined functions for specific formulas, and a clean user interface that doesn't break when a decimal point is entered.

---

## 🚀 SYSTEM FEATURES

The application provides a centralized terminal menu allowing the user to input a base value and select a target conversion matrix:

* 🔹 **Celsius to Fahrenheit (C ⮕ F):** The standard commercial conversion.
* 🔸 **Fahrenheit to Celsius (F ⮕ C):** Reversing the scalar for global data standards.
* 🔹 **Celsius to Kelvin (C ⮕ K):** The scientific standard for absolute thermal analysis.
* 🔸 **Kelvin to Celsius (K ⮕ C):** Transitioning from lab data to human-readable metrics.

---

## 🧠 THE ARCHITECTURE (Formula Logic)



[Image of Temperature scale comparison chart showing Celsius, Fahrenheit, and Kelvin]


Instead of writing one giant block of code, this project follows the **Modular Subroutine** method. Each conversion is its own "Lego Block" (function). This makes the code easy to read, easy to test, and easy to reuse in future IoT projects.

The logic flow:
1. **Input Interface:** Captures the raw number (float) and the choice of conversion.
2. **Formula Engine:** The script passes the raw number into a specific function (e.g., `c_to_f(val)`) which contains the hardcoded mathematical constant.
3. **Precision Output:** The result is returned and formatted to 2 decimal places using Python string formatting to keep the console clean.

---

## 🛡️ THE "OOPS" CATCHER (Validation)

Even a simple calculator can be crashed by a bad user. This project implements strict validation:
* **Float Validation:** If the user enters `25,5` (with a comma) or `abc`, the `try/except` block catches the `ValueError` and prevents the "Blue Screen of Death" for your script.
* **The Absolute Zero Gate:** (Extra Challenge) In a pro-grade version, the script should check if a Kelvin value is below `0` or a Celsius value is below `-273.15` and raise a `ValueError` because those temperatures are physically impossible in our universe.

---

## 💻 DEPLOYMENT INSTRUCTIONS

1. Connect your Microcontroller and launch Thonny.
2. Open the `main.py` file from this directory.
3. Press **F5** to boot the Thermal Processor.
4. Follow the terminal prompts to perform your calculations.

***