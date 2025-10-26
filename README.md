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

The app is ideal for learning Flask fundamentals, front-end integration, or as a base for more advanced conversion utilities.

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

## 🗂️ Project Structure

Unit_Converter/
├── api.py # Flask app entry point
├── converter.py # Core conversion logic
├── get_unit_suffix.py # Handles suffix display for units
├── static/
│ └── css/
│ └── styles.css # Styling for pages
├── templates/
│ ├── convert_page.html
│ ├── length_page.html
│ ├── temperature_page.html
│ └── weight_page.html
└── README.md

yaml
Copy code

---

## ⚙️ Installation

Follow these steps to set up the project locally.

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Unit_Converter
2. Create and activate a virtual environment
bash
Copy code
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
(If no requirements.txt exists, you can install Flask manually:)

bash
Copy code
pip install flask
🚀 Usage
Run the app locally:

bash
Copy code
python api.py
Then open your browser and go to:

cpp
Copy code
http://127.0.0.1:5000/
You’ll see the home page, where you can choose the unit type to convert.

🔧 Configuration
You can modify or add conversion logic in converter.py.
To add new conversion categories (like speed or volume):

Create a new HTML page in templates/.

Add corresponding logic to converter.py.

Update Flask routes in api.py.

🧠 Examples
Example 1 — Length Conversion
Input: 5 meters → Output: 16.404 feet

Example 2 — Weight Conversion
Input: 1 kilogram → Output: 2.205 pounds

Example 3 — Temperature Conversion
Input: 100°C → Output: 212°F

🛠️ Troubleshooting
Problem	Solution
Flask app won’t start	Ensure Flask is installed (pip install flask).
CSS not loading	Check the static/css/styles.css file path.
Changes not showing	Restart Flask after code edits.

👥 Contributors
Your Name — Developer & Maintainer
