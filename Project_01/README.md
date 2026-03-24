<h1 align="center">🕹️ Project\_01: The "War Games" Simulation (Tic-Tac-Toe) ✖️⭕</h1>

<p align="center">
<a href="\#"><img src="https://img.shields.io/badge/Language-MicroPython-3776AB?style=flat-square\&logo=python\&logoColor=white" alt="MicroPython Badge"></a>
<a href="\#"><img src="https://img.shields.io/badge/Concept-Game\_Loop-5C5C5C?style=flat-square\&logo=matrix\&logoColor=white" alt="Game Loop Badge"></a>
<a href="\#"><img src="https://img.shields.io/badge/Status-Playable-2EA043?style=flat-square\&logo=hackthebox\&logoColor=white" alt="Playable Badge"></a>
</p>

> *"Shall we play a game? Before we connect this microcontroller to the global internet, you must prove you can build a closed-loop, interactive system. This is your first real dopamine hit: pure logic turned into a playable simulation."*

This project synthesizes everything you have learned so far: variables, loops, functions, lists, and crucially, the **error handling**. We are building a fully playable, two-player Tic-Tac-Toe game that runs directly inside the Thonny shell.

-----

## 🧩 THE ARCHITECTURE (How It Works)

We aren't just writing spaghetti code. We are engineering a state machine. The game relies on four distinct "Lego Blocks" of logic snapping together:

### 1\. The Matrix (Data Structure)

The board is just a standard Python list containing 9 elements, representing slots `1` through `9`. As players make moves, we overwrite the numbers with an `"X"` or an `"O"`.

```python
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
```

### 2\. The Render Engine (Display)

A function that clears the mental clutter and prints the `board` list into a beautiful, human-readable 3x3 grid in the console.

### 3\. The Input Sanitizer (Error Handling)

Users are unpredictable. If you ask for a number and they type the letter `"A"`, a normal script will crash. We use a `try/except` block to catch the `ValueError`, scold the user, and keep the game running flawlessly.

### 4\. The Referee (Win Logic)

After every single turn, a function checks all 8 possible winning combinations (3 rows, 3 columns, 2 diagonals). If it finds three matching symbols, it halts the loop and declares a victor.

-----