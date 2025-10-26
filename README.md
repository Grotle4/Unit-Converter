# 🧮 Unit Converter

A simple and elegant **Flask-based web application** that allows users to convert between multiple unit types — including **length, weight, and temperature** — through a clean, responsive web interface.

---

## 📋 Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Configuration](#configuration)
7. [Examples](#examples)
8. [Troubleshooting](#troubleshooting)
9. [Contributors](#contributors)
10. [License](#license)

---

## 🧩 Introduction

The **Unit Converter** is a lightweight Flask web app designed for quick and accurate unit conversions.  
It includes separate pages for **length**, **weight**, and **temperature**, each providing user-friendly interfaces and instant conversion results.


---

## ✨ Features

- 🌡️ Convert between multiple **unit types**:
  - Length (meters, feet, miles, etc.)
  - Weight (grams, kilograms, pounds, etc.)
  - Temperature (Celsius, Fahrenheit, Kelvin)
- ⚡ Real-time results using Flask backend logic
- 🎨 Responsive design using HTML + CSS
- 🧠 Modular code with clean separation (`api.py`, `converter.py`, etc.)
- 🧩 Easy to extend with new unit types

---

## ⚙️ Installation

Follow these steps to set up the project locally.

### 1. Clone the repository

```
bash
git clone <https://github.com/Grotle4/Unit-Converter>
cd Unit_Converter
```

### 2. Create and activate a virtual environment
```
bash
python -m venv venv
```
# On Windows
```
bash
venv\Scripts\activate
```
# On macOS/Linux
```
bash
source venv/bin/activate
```

### 3. Install dependencies
```
bash
pip install -r requirements.txt
(If no requirements.txt exists, you can install Flask manually:)
```

```
bash
pip install flask
```

🚀 Usage
Run the app locally:
```bash
python api.py
```
Then open your browser and go to:
```
http://127.0.0.1:5000/
```

You’ll see the home page, where you can choose the unit type to convert.

### 🔧 Configuration
You can modify or add conversion logic in converter.py.
To add new conversion categories (like speed or volume):

Create a new HTML page in templates/.

Add corresponding logic to converter.py.

Update Flask routes in api.py.

### 🧠 Examples
Example 1 — Length Conversion
Input: 5 meters → Output: 16.404 feet

Example 2 — Weight Conversion
Input: 1 kilogram → Output: 2.205 pounds

Example 3 — Temperature Conversion
Input: 100°C → Output: 212°F

### 🛠️ Troubleshooting
Problem	Solution
Flask app won’t start	Ensure Flask is installed (pip install flask).
CSS not loading	Check the static/css/styles.css file path.
Changes not showing	Restart Flask after code edits.

### 👥 Contributors
Dylan Troche — Developer & Maintainer

### Inspiration
https://roadmap.sh/projects/unit-converter
