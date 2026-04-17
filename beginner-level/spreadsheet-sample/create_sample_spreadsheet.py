# Create a sample Excel spreadsheet with employee data
# Run this once to generate the sample file: employees.xlsx

import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "employees"

# Header row
headers = ["id", "name", "department", "salary", "start_date"]
sheet.append(headers)

# Sample employee data
employees = [
    [1, "Alice Johnson", "Engineering", 95000, "2021-03-15"],
    [2, "Bob Smith", "Marketing", 72000, "2020-07-01"],
    [3, "Charlie Brown", "Engineering", 88000, "2022-01-10"],
    [4, "Diana Ross", "Sales", 67000, "2019-11-20"],
    [5, "Eve Martinez", "Engineering", 102000, "2018-05-30"],
    [6, "Frank Wilson", "Marketing", 75000, "2023-02-14"],
    [7, "Grace Lee", "Sales", 71000, "2021-08-22"],
    [8, "Henry Davis", "Engineering", 93000, "2020-04-05"],
    [9, "Iris Chen", "Marketing", 68000, "2022-09-18"],
    [10, "Jack Taylor", "Sales", 79000, "2019-06-12"],
]

for emp in employees:
    sheet.append(emp)

workbook.save("employees.xlsx")
print("Created employees.xlsx with 10 sample rows.")
