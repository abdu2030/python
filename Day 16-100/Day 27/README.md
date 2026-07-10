# 📏 Mile to Kilometer Converter & Tkinter Playground (Day 27)

A collection of Python desktop GUI exercises exploring Python's standard **Tkinter** library. This project contains a simple Miles-to-Kilometers converter application, a grid-layout playground, and a script demonstrating Python's advanced argument passing patterns (`*args` and `**kwargs`).

---

## 📂 Project Structure

### 1. `mile to km.py`
A simple GUI utility that converts miles to kilometers:
*   Uses `Entry` for numeric input.
*   Calculates the conversion using the formula: `km = miles * 1.609`.
*   Updates a `Label` dynamically to display the result when the **Calculate** button is clicked.
*   Uses the `pack()` geometry manager for basic vertical stacking.

### 2. `main.py`
An exercise illustrating basic widget styling and positioning in Tkinter:
*   Sets up custom window paddings (`padx` and `pady`).
*   Configures label texts and button command callbacks.
*   Practices placing multiple widgets (labels, entry fields, buttons) in rows and columns using the `grid()` geometry manager.

### 3. `playground.py`
A CLI playground file explaining advanced Python syntax:
*   **`*args` (Variable Positional Arguments)**: Demonstrates how to write functions that accept an arbitrary number of arguments (accessing them as a tuple inside the function, e.g., to create a sum calculator).
*   **`**kwargs` (Variable Keyword Arguments)**: Demonstrates how functions accept arbitrary keyword arguments (accessing them as a dictionary, e.g., to create a flexible configuration class initialization).

---

## 🚀 How to Run the Scripts

### 1. Run the Converter App
Open your terminal inside the `Day 27` directory and run:
```bash
python "mile to km.py"
```

### 2. Run the Grid Layout Demo
```bash
python main.py
```

### 3. Run the Playground Script (CLI Output)
```bash
python playground.py
```

---

## 🛠️ Requirements
*   Python 3.x
*   Tkinter (comes built-in with standard Python installations)
