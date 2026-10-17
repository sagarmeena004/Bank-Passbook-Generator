# 🏦 Bank Passbook Generator — Features Documentation

## 📌 Overview

Bank Passbook Generator is a Python-based command-line application that simulates a banking login system using OTP verification and generates a formatted bank passbook.

The project demonstrates Python programming concepts such as functions, loops, conditional statements, exception handling, and terminal formatting.

---

## 🔐 1. OTP Generation System

The application generates a random four-digit OTP using Python's built-in `random` module.

### Functionality

- Generates an OTP between 1000 and 9999.
- Displays the generated OTP in the terminal.
- Requests the user to enter the OTP.
- Compares the entered OTP with the generated value.

### Python Concepts

- Random number generation
- Variables
- User input
- Conditional statements

---

## ✅ 2. OTP Verification System

The application verifies the OTP entered by the user.

### Functionality

- Correct OTP allows the user to proceed.
- Incorrect OTP displays an error message.
- Users can retry entering the OTP.
- Entering `555` during the retry process exits the application.

### Python Concepts

- `if` statements
- `elif` statements
- `else` statements
- `while` loops

**Note:** OTP verification is performed locally. No actual SMS is sent.

---

## 👤 3. Customer Information Collection

After successful OTP verification, the application collects customer information.

### Information Collected

- Customer name
- Branch name
- IFSC code
- Customer ID
- Aadhaar number
- Account number

### Python Concepts

- `input()`
- Type conversion
- Functions
- Global variables
- Exception handling

---

## 📖 4. Bank Passbook Generation

The application generates a formatted passbook in the terminal.

### Passbook Information

- Bank name
- Branch name
- Customer name
- Branch address
- IFSC code
- Account number
- Customer ID
- Aadhaar number

The passbook also displays a banking-themed warning message and customer support information.

**Note:** The generated passbook is a terminal-based demonstration, not an official bank document.

---

## ⏳ 5. Countdown Animation

Before displaying the passbook, the application shows a countdown from 10 to 1.

### Technology

Python's built-in `time` module.

### Purpose

- Simulates a passbook generation process.
- Improves the terminal interaction experience.
- Demonstrates time delays in Python.

---

## 🎨 6. Colorful Terminal Interface

The application uses the `colorama` library to display colored terminal text.

### Features

- Colored welcome screen
- Highlighted input prompts
- OTP verification messages
- Login success messages
- Formatted passbook output

### Python Concepts

- Third-party libraries
- String formatting
- Terminal styling

---

## ⚠️ 7. Input Error Handling

The application uses `try` and `except` blocks for certain numeric inputs.

### Functionality

- Handles nonnumeric mobile number input.
- Handles nonnumeric OTP input during initial verification.
- Handles invalid numeric conversions for customer ID, Aadhaar number, and account number.

**Limitation:** The application does not perform complete format or length validation of these values.

---

## 🚪 8. Exit Mechanism

The application provides an exit option during incorrect OTP retries.

### Functionality

- Enter `555` after an incorrect OTP attempt.
- The application displays a thank-you message.
- The OTP retry loop terminates.

---

## 🧠 Python Skills Demonstrated

| Python Concept | Implementation |
|---|---|
| Functions | Organizing program operations |
| Conditional Statements | OTP verification |
| Loops | OTP retry mechanism |
| Exception Handling | Numeric input conversion |
| Random Module | OTP generation |
| Time Module | Countdown animation |
| Colorama | Terminal styling |
| F-Strings | Dynamic text formatting |
| Global Variables | Sharing user information |

---

## 🔒 Project Limitations

This application is an educational simulation.

- No real SMS OTP delivery.
- No banking server integration.
- No database connection.
- No real account authentication.
- No transaction processing.
- No PDF passbook export.
- No actual OTP expiration enforcement.

Users should avoid entering real banking credentials or sensitive personal information.

---

## 👨‍💻 Developer

**Sagar Meena**

Python Developer

GitHub: sagarmeena004

---

## 📜 Conclusion

This project demonstrates the practical application of fundamental Python programming concepts through a banking-themed command-line application.

It highlights skills in user input handling, OTP verification logic, functions, loops, exception handling, and formatted terminal output.
