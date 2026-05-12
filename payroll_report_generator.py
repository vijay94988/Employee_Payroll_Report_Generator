import os
import sqlite3
import pandas as pd

# create folders if not present
os.makedirs("data", exist_ok=True)
os.makedirs("output", exist_ok=True)
os.makedirs("database", exist_ok=True)

# sample employee data
csv_data = """emp_id,name,department,basic_salary,hours_worked
E001,Ravi Kumar,HR,50000,160
E002,Sneha Patel,Finance,65000,155
E003,Arjun Singh,IT,80000,170
E004,Priya Nair,HR,45000,148
E005,Rahul Mehta,Finance,72000,160
"""

# save csv file
with open("data/employees.csv", "w") as file:
    file.write(csv_data)

# read employee data
df = pd.read_csv("data/employees.csv")

# tax calculation function
def calculate_tax(salary):
    if salary <= 25000:
        tax = 0
    elif salary <= 50000:
        tax = salary * 0.05
    elif salary <= 75000:
        tax = salary * 0.10
    else:
        tax = salary * 0.15
    return tax

# create new columns
df["tax_deduction"] = df["basic_salary"].apply(calculate_tax)
df["net_pay"] = df["basic_salary"] - df["tax_deduction"]

# display payroll data
print("\nEmployee Payroll Report\n")
print(df[[
    "name",
    "department",
    "basic_salary",
    "tax_deduction",
    "net_pay"
]])

# department wise average salary
print("\nAverage Salary By Department\n")
dept_summary = df.groupby("department")["net_pay"].mean()
print(dept_summary)

# export report to excel
excel_path = "output/payroll_report.xlsx"
df.to_excel(excel_path, index=False)
print(f"\nExcel report saved at: {excel_path}")

# store data in sqlite database
conn = sqlite3.connect("database/payroll.db")
df.to_sql(
    "employees",
    conn,
    if_exists="replace",
    index=False
)
conn.close()
print("\nEmployee data stored in SQLite database")