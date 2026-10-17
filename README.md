# 🏦 Bank Passbook Generator

### 🔐 OTP-Based Login & Banking Passbook Simulation Using Python

A Python-based terminal application that simulates an OTP login system and generates a formatted bank passbook using user-provided account information.

This project demonstrates fundamental Python programming skills, including functions, conditional statements, loops, exception handling, random number generation, and terminal formatting.

> **Disclaimer:** This is an educational banking simulation and is not affiliated with Bank of India or any financial institution. No real banking authentication or transactions are performed.

---

## 🚀 Features

- 🔐 **OTP Generation:** Generates a random 4-digit OTP.
- ✅ **OTP Verification:** Validates the OTP entered by the user.
- 🔄 **Retry Mechanism:** Allows users to retry after entering an incorrect OTP.
- 🚪 **Exit Option:** Enter `555` to exit during an incorrect OTP retry.
- 👤 **Customer Details:** Collects customer name, branch, and customer ID.
- 💳 **Account Information:** Accepts account number, Aadhaar number, and IFSC code.
- 📖 **Passbook Generation:** Displays a formatted passbook in the terminal.
- ⏳ **Countdown Animation:** Shows a countdown before generating the passbook.
- 🎨 **Colorful Terminal UI:** Uses Colorama for terminal styling.
- ⚠️ **Input Handling:** Handles certain invalid numeric inputs using exception handling.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Random | Random OTP generation |
| Colorama | Colored terminal output |
| Time | Countdown animation |

---

## 📁 Project Structure

```text
LOGIN PROJECT WITH OTP/
│
├── login.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/sagarmeena004/Bank-Passbook-Generator.git
```

**2. Navigate to the project**

```bash
cd Bank-Passbook-Generator
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
python login.py
```

---

## 💻 How It Works

1. The application displays a banking-themed welcome screen.
2. The user enters a mobile number.
3. A random 4-digit OTP is displayed in the terminal.
4. The user enters the OTP for verification.
5. After successful verification, the application requests customer and account details.
6. A countdown animation begins.
7. The application displays a formatted bank passbook.

**Note:** OTP verification is simulated locally. The application does not send an actual SMS.

---

## 🧠 Python Concepts Demonstrated

- Functions and nested functions
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while`)
- Exception handling (`try`, `except`)
- User input handling
- Random number generation
- String formatting and f-strings
- Global variables
- Third-party Python libraries
- Terminal output formatting

---

## 🔒 Security Notice

This application is designed for educational purposes only.

- It does not connect to any banking server.
- OTPs are displayed locally rather than sent by SMS.
- Account information is entered manually.
- It does not perform real banking transactions.
- Avoid entering real Aadhaar numbers or sensitive banking credentials.

---

## 👨‍💻 Developer

**Sagar Meena**

Python Developer | Programming Enthusiast

**GitHub:** [sagarmeena004](https://github.com/sagarmeena004)

---

⭐ If you find this project useful, consider giving it a star!