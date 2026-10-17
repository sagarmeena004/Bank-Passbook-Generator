# 🏦 Bank Passbook Generator — Project Overview

## 📌 Introduction

Bank Passbook Generator is a Python-based command-line application developed to demonstrate fundamental Python programming concepts through a simulated banking environment.

The application combines an OTP-based login simulation, customer information collection, and terminal-based passbook generation.

This project is designed for educational purposes and showcases practical Python programming skills.

---

## 🎯 Project Objectives

The primary objectives of this project are:

1. Implement an OTP verification system using Python.
2. Generate random OTPs using Python's `random` module.
3. Handle user inputs through interactive terminal prompts.
4. Apply conditional statements for OTP validation.
5. Use functions to organize application logic.
6. Implement exception handling for invalid numeric inputs.
7. Generate a formatted banking passbook.
8. Create a colorful terminal interface using Colorama.
9. Implement a countdown animation using the `time` module.

---

## ⚙️ Application Workflow

### Step 1: Welcome Screen

The application starts by displaying a Bank of India-themed welcome screen using formatted text and terminal colors.

### Step 2: Mobile Number Input

The user enters a mobile number through the terminal.

The application attempts to convert the entered value into an integer.

### Step 3: OTP Generation

A random four-digit OTP is generated using:

`randint(1000, 9999)`

The generated OTP is displayed in the terminal.

### Step 4: OTP Verification

The user enters the generated OTP.

The application compares the entered OTP with the generated value.

- Correct OTP: Proceed to customer information collection.
- Incorrect OTP: Display an error and allow another attempt.
- Enter `555` during the retry process to exit.

### Step 5: Customer Information

After successful OTP verification, the application collects:

- Customer name
- Branch name
- IFSC code
- Customer ID
- Aadhaar number
- Account number

### Step 6: Passbook Generation

The application displays a countdown animation before generating the passbook.

### Step 7: Passbook Display

A formatted passbook is displayed in the terminal with customer and account details.

---

## 🛠️ Technologies Used

| Technology | Application |
|---|---|
| Python | Application development |
| Random | OTP generation |
| Colorama | Terminal styling |
| Time | Countdown animation |

---

## 🧠 Python Programming Concepts

### 1. Functions

The application uses functions to organize operations such as input collection, OTP entry, customer information collection, and passbook generation.

### 2. Conditional Statements

`if`, `elif`, and `else` statements control OTP verification and exit conditions.

### 3. Loops

A `while` loop allows repeated OTP attempts.

### 4. Exception Handling

`try` and `except` blocks handle certain invalid numeric inputs.

### 5. Random Number Generation

The `random` module generates a four-digit OTP.

### 6. String Formatting

F-strings, capitalization, and formatted print statements are used to display customer information.

### 7. Global Variables

Global variables are used to share collected information between functions.

### 8. Terminal Styling

Colorama provides different colors for prompts, messages, and generated output.

---

## 📁 Project Structure

```text
LOGIN PROJECT WITH OTP/
│
├── login.py
├── requirements.txt
├── README.md
├── .gitignore
└── PROJECT_OVERVIEW.md
```

---

## 🔐 Security and Limitations

This project is a local educational simulation.

- OTPs are displayed in the terminal rather than delivered through SMS.
- No real banking authentication is performed.
- The application does not connect to a banking database.
- The generated passbook is terminal output, not an official bank document.
- The application does not verify the authenticity of entered account information.
- Users should avoid entering real sensitive banking information.

---

## 🚀 Future Improvements

Potential future enhancements include:

- SMS-based OTP delivery
- Secure OTP expiration
- Improved input validation
- Database integration
- Account balance management
- Transaction history
- PDF passbook generation
- Graphical user interface

These features are suggestions for future development and are not implemented in the current version.

---

## 👨‍💻 Developer

**Sagar Meena**

Python Programming | Command-Line Applications

GitHub: sagarmeena004

---

## 📜 Conclusion

Bank Passbook Generator demonstrates how fundamental Python concepts can be combined to build an interactive command-line application.

The project highlights skills in user input handling, control flow, functions, exception handling, random number generation, and formatted terminal output.
