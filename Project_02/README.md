<h1 align="center">🗄️ Project_02: The Personnel Vault (Student Management) 🆔</h1>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Language-MicroPython-3776AB?style=flat-square&logo=python&logoColor=white" alt="MicroPython Badge"></a>
  <a href="#"><img src="https://img.shields.io/badge/Concept-State_Management-5C5C5C?style=flat-square&logo=matrix&logoColor=white" alt="State Management Badge"></a>
  <a href="#"><img src="https://img.shields.io/badge/Status-Database_Active-2EA043?style=flat-square&logo=hackthebox&logoColor=white" alt="Database Active Badge"></a>
</p>

> *"Data is only as useful as the structure that holds it. Before we send telemetry to the cloud, you must master the art of local data manipulation and persistent state logic."*

Welcome to the Personnel Vault. Moving beyond simple games, this project simulates a real-world backend database. You are building a Command Line Interface (CLI) application that acts as a Student Management System. 

This project proves you can manage complex, nested data structures (dictionaries inside of dictionaries) and navigate users through a multi-tiered menu system without crashing the main loop.

---

## 🚀 SYSTEM FEATURES

When the script executes, it traps the user in a continuous `while` loop, offering a terminal-based menu to perform CRUD (Create, Read, Update, Delete) operations on the student database.

* 🟢 **Register Entity (Add Student):** Dynamically generate a new profile in the system with a unique ID, capturing their name and initializing their metrics.
* 🟡 **Log Telemetry (Attendance Tracker):** Update a specific student's attendance record (present/absent) and calculate their real-time attendance percentage.
* 🔴 **Update Metrics (Marks Management):** Append new test scores to a student's profile and instantly calculate their current grade average.
* 🔵 **Access Records (View Database):** Print a beautifully formatted, tabular readout of all registered students and their current stats to the console.

---

## 🧠 THE ARCHITECTURE (Data Structures)



The secret to this project isn't complex math; it's **Nested Dictionaries**. Instead of creating hundreds of separate variables, the entire system state is stored in a single master dictionary. 

The architecture looks like this conceptually:
1. **The Master Vault:** A primary dictionary where the "Key" is the Student's unique Roll Number or ID.
2. **The Profile:** The "Value" attached to that ID is *another* dictionary containing their `name`, `attendance_count`, `total_days`, and a `marks` list.

When a teacher wants to add a test score, the system's logic simply navigates the path: 
`Find Master Vault -> Find Student ID -> Find 'Marks' List -> .append(new_score)`

---

## 🛡️ ERROR HANDLING EXPECTATIONS
This system is designed to be bulletproof. As you interact with it, notice how the "Oops" Catcher intercepts bad behavior:
* **Lookup Failures:** If you try to add marks to a Student ID that doesn't exist, the system catches the `KeyError` and returns you to the main menu instead of crashing.
* **Input Sanitization:** If the system asks for a numerical test score and you type `"Eighty"`, the `ValueError` is caught, and the system prompts you to try again.

---
