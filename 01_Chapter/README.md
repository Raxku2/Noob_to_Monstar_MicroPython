<h1 align="center">🧠 Phase 01: Variables & Data Types 🧱</h1>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Language-MicroPython-3776AB?style=flat-square&logo=python&logoColor=white" alt="MicroPython Badge"></a>
  <a href="#"><img src="https://img.shields.io/badge/Concept-Core_Logic-5C5C5C?style=flat-square&logo=matrix&logoColor=white" alt="Core Logic Badge"></a>
</p>

> *"Memory allocated. Defining the building blocks of the system's logic."*

This module covers the absolute fundamentals of storing and identifying information in MicroPython. Before we can manipulate hardware, we must understand how to store data in the system's memory.

---

## 🗃️ CORE DATA TYPES

In this chapter, we define variables and explore the primary data structures used in MicroPython:
* **`int`**: Integer numbers (whole numbers).
* **`float`**: Floating-point numbers (decimals).
* **`str`**: Strings (text and characters).
* **`list`**: Ordered, mutable arrays of items.
* **`dict`**: Dictionaries containing key-value pairs.

---

## 💻 THE SCRIPT (`main.py`)

Below is the code demonstrating how to assign these data types to variables and verify their types in the system.

```python
# Integer assignment
a = 1
b = 2
print(type(a))

# Float assignment
c = 1.2
print(type(c))

# String assignment
name = "Rax"
print(type(name))

# List assignment (Array of strings)
list_of_names = ['Rakesh', 'Rim']
print(type(list_of_names))

# Dictionary assignment (Key-Value pairs)
dic_of_user = {
    'name': "Rakesh",
    'address': "Guptipara",
    'github': True 
}
print(type(dic_of_user))

```

---

## 🛠️ BUILT-IN FUNCTIONS USED

To inspect our data and output the results, we utilize two essential built-in Python functions in this script:

* **`print()`**: A function used to print or write data directly to the console/shell.
* **`type()`**: A function that evaluates the argument passed to it and returns the object name (class) of that specific data type.
