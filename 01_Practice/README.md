<h1 align="center">⚔️ Phase 01_Practice: The Logic Gauntlet 🧩</h1>

<p align="center">
<a href="#"><img src="[https://img.shields.io/badge/Language-MicroPython-3776AB?style=flat-square&logo=python&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Language-MicroPython-3776AB%3Fstyle%3Dflat-square%26logo%3Dpython%26logoColor%3Dwhite)" alt="MicroPython Badge"></a>
<a href="#"><img src="[https://img.shields.io/badge/Status-Challenge_Mode-D22128?style=flat-square&logo=hackthebox&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Status-Challenge_Mode-D22128%3Fstyle%3Dflat-square%26logo%3Dhackthebox%26logoColor%3Dwhite)" alt="Challenge Badge"></a>
</p>

> *"Simulation active. Testing pure computational logic, control flows, and algorithmic endurance before hardware integration."*

Before touching physical pins or reading sensor voltages, the core software engine must be flawless. This module contains pure logic challenges designed to stress-test your understanding of variables, mathematical/logical operators, conditionals, and loop controls.

---

## 🎯 THE CHALLENGES

Create a new file for each challenge in your IDE and execute them in the terminal. No hardware required.

### Challenge 01: The FizzBuzz Matrix

**Objective:** Master the modulo operator (`%`), `for` loops, and `if-elif-else` chains.

**Task:**
Write a script that loops through the numbers 1 to 50.

* If the number is perfectly divisible by 3, print `"Fizz"`.
* If the number is perfectly divisible by 5, print `"Buzz"`.
* If the number is divisible by BOTH 3 and 5, print `"FizzBuzz"`.
* Otherwise, just print the number itself.

### Challenge 02: The Prime Hunter

**Objective:** Utilize nested loops, arithmetic operators, and the `break` statement to optimize execution.

**Task:**
Write a program that finds and prints all prime numbers between 1 and 100.

* *Hint:* A prime number is only divisible by 1 and itself. Use a `for` loop inside another `for` loop to test for factors. If a factor is found, use `break` to shatter the inner loop early and save CPU cycles.

### Challenge 03: The Data Sanitizer

**Objective:** Practice `while` loops, the `continue` statement, and logical operators (`and`/`or`).

**Task:**
You are given a raw list of integers: `raw_data = [15, -4, 0, 42, 999, 8, -1]`
Write a `while` loop to process this list item by item until it is empty (using `.pop(0)`).

* If the number is negative or exactly `0`, use `continue` to skip the rest of the loop and move to the next iteration without printing anything.
* If the number is `999` (simulating a fatal system error), print `"SYSTEM HALT"` and use `break` to escape the loop entirely.
* Otherwise, print `"Valid entry: [number]"`.

### Challenge 04: The Terminal Password Validator

**Objective:** Combine string traversal, boolean flags, and complex logical conditions.

**Task:**
Create a variable: `password = "Secure9X"`
Write a script that verifies if the password meets the following strict criteria:

1. It must be at least 8 characters long (use the `len()` function).
2. It must contain at least one numeric digit.

* *Hint:* Set a boolean flag `has_number = False`. Loop through each character in the string. If a character is a digit (you can check this using `"0" <= char <= "9"`), flip the flag to `True`. Finally, use a master `if` statement with the `and` operator to evaluate both conditions and print `"ACCESS GRANTED"` or `"ACCESS DENIED"`.

---

## 🧠 RULES OF ENGAGEMENT

* Do not use built-in external Python libraries to solve these. Rely entirely on your raw loops, operators, and conditionals.
* Keep your code clean, indent properly, and use descriptive variable names.

