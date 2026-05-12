# Employee Payroll Automation System

A simple Python project that automates employee payroll processing using Pandas and SQLite.

---

## Features

* Read employee data from a CSV file
* Calculate tax deductions based on salary slabs
* Generate net pay automatically
* Export payroll report to Excel
* Store employee records in SQLite database
* Department-wise salary summary

---

## Technologies Used

* Python
* Pandas
* SQLite3
* OpenPyXL

---

## Project Structure

```text
project/
│
├── data/
│   └── employees.csv
│
├── output/
│   └── payroll_report.xlsx
│
├── database/
│   └── payroll.db
│
└── main.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/payroll-automation-system.git
cd payroll-automation-system
```

Install dependencies:

```bash
pip install pandas openpyxl
```

---

## Run The Project

```bash
python main.py
```

---

## Sample Output

```text
Employee Payroll Report

           name department  basic_salary  tax_deduction   net_pay
0    Ravi Kumar         HR         50000         2500.0   47500.0
1   Sneha Patel    Finance         65000         6500.0   58500.0
2   Arjun Singh         IT         80000        12000.0   68000.0
```

---

## Future Improvements

* Add overtime salary calculation
* Build a GUI using Tkinter or Streamlit
* Add employee search system
* Generate PDF salary slips
* Add login authentication

---

## Learning Goals

This project helped practice:

* File handling
* Working with CSV files
* Data analysis using Pandas
* Functions in Python
* SQLite database operations
* Exporting Excel reports

---

## Author

Alex
