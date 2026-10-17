# 🏦 Bank Passbook Generator — Installation & Execution Guide

## 📌 Introduction

This guide explains how to install and run the Bank Passbook Generator Python project on Windows.

The application is a command-line banking simulation featuring OTP verification and terminal-based passbook generation.

---

## 🛠️ Prerequisites

Before running the project, make sure you have:

- Python 3 installed
- Git installed (optional, for cloning)
- An internet connection to install dependencies
- A terminal such as PowerShell or VS Code Terminal

### Verify Python Installation

Open PowerShell and run:

```powershell
python --version
```

### Verify Git Installation

```powershell
git --version
```

---

## 📥 Step 1 — Download the Project

Clone the repository:

```powershell
git clone https://github.com/sagarmeena004/Bank-Passbook-Generator.git
```

Alternatively, download the project as a ZIP file from GitHub and extract it.

---

## 📂 Step 2 — Open the Project Directory

```powershell
cd Bank-Passbook-Generator
```

The project contains the following files:

```text
Bank-Passbook-Generator/
│
├── login.py
├── requirements.txt
├── README.md
├── .gitignore
├── PROJECT_OVERVIEW.md
├── FEATURES.md
├── HOW_TO_RUN.md
└── CHANGELOG.md
```

---

## 📦 Step 3 — Install Dependencies

The project uses Colorama for colored terminal output.

Install dependencies using:

```powershell
python -m pip install -r requirements.txt
```

**Note:** The `random` and `time` modules are included with Python and do not require separate installation.

---

## ▶️ Step 4 — Run the Application

Execute the main Python file:

```powershell
python login.py
```

The application will display a banking-themed welcome screen.

---

## 🔐 Step 5 — OTP Verification

1. Enter a mobile number when prompted.
2. The application generates a random four-digit OTP.
3. The OTP is displayed in the terminal.
4. Enter the displayed OTP.
5. After successful verification, the application proceeds to the customer information form.

### Incorrect OTP

If an incorrect OTP is entered, the application provides a retry option.

During the retry process, enter `555` to exit.

**Important:** The OTP is generated and verified locally. No SMS is sent to the mobile number.

---

## 👤 Step 6 — Enter Customer Information

After OTP verification, the application requests:

- Customer name
- Branch name
- IFSC code
- Customer ID
- Aadhaar number
- Account number

For testing, use fictional account information rather than real banking details.

---

## 📖 Step 7 — Generate the Passbook

After entering the requested information:

1. A countdown animation starts.
2. The application displays a success message.
3. A formatted passbook appears in the terminal.

The passbook contains the entered customer and account information.

**Note:** The output is displayed in the terminal and is not saved as a PDF or official banking document.

---

## 🧪 Example Test Workflow

```text
Welcome to Bank of India Bhopal

Login with OTP

Please Enter your number : 9000000000

<#> 4826 is your Account Login OTP.

Please Enter OTP : 4826

Correct Otp !
Login Sucessful

Enter Your Name : Demo User
Enter your Branch Name : Demo Branch
ENter your IFC CODE : DEMO0000001
Enter customer Id : 123456
Enter your adhar NO. : 111122223333
Enter your account no : 1234567890

Login Sucessful

Your PASSBOOK is Generating...

10
9
8
7
6
5
4
3
2
1

SUCESSFULLY GENERETED!
```

The OTP shown above is only an example. The actual OTP changes between program runs.

---

## ⚠️ Troubleshooting

### Problem 1: Python Is Not Recognized

If PowerShell cannot find Python, check that Python is installed and available in your system PATH.

### Problem 2: Colorama Module Not Found

If you see:

```text
ModuleNotFoundError: No module named 'colorama'
```

Run:

```powershell
python -m pip install colorama
```

### Problem 3: Incorrect OTP

Enter the OTP displayed in the terminal.

If you enter an incorrect OTP, the application allows another attempt.

### Problem 4: Invalid Numeric Input

The application expects numeric input for certain fields.

For testing, enter digits for the mobile number, OTP, customer ID, Aadhaar number, and account number.

---

## 🔒 Security Notice

This application is an educational simulation.

- Do not enter real banking credentials.
- Do not enter actual Aadhaar numbers.
- The application does not communicate with banking servers.
- It does not perform real financial transactions.
- The generated passbook is not an official bank record.

---

## 👨‍💻 Developer

**Sagar Meena**

Python Developer

GitHub: sagarmeena004

---

## ✅ Conclusion

You can now run the Bank Passbook Generator application using Python.

This project demonstrates OTP verification logic, user input handling, conditional statements, loops, exception handling, and formatted terminal output.
