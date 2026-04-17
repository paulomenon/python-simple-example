# Spreadsheet Sample

This example demonstrates a complete data pipeline: reading an Excel spreadsheet, storing it in a SQLite database, and exporting a formatted PDF report.

## What's Inside

| Script | What it does |
|---|---|
| `create_sample_spreadsheet.py` | Generates a sample `employees.xlsx` with 10 rows of employee data |
| `spreadsheet_to_sqlite.py` | Reads any `.xlsx` file, auto-detects column types, creates a SQLite table, and inserts all rows |
| `sqlite_to_pdf_report.py` | Reads from the SQLite database and exports a styled PDF report with summary statistics |

## Prerequisites

Install the required Python packages:

```bash
pip install -r requirements.txt
```

This installs:
- **openpyxl** -- for reading and writing Excel files
- **reportlab** -- for generating PDF documents

SQLite is built into Python, so no extra install is needed for the database.

## How to Run

### 1. Create the sample spreadsheet

```bash
python create_sample_spreadsheet.py
```

This creates `employees.xlsx` with the following columns:

| id | name | department | salary | start_date |
|----|------|------------|--------|------------|
| 1 | Alice Johnson | Engineering | 95000 | 2021-03-15 |
| 2 | Bob Smith | Marketing | 72000 | 2020-07-01 |
| ... | ... | ... | ... | ... |

You can skip this step and use your own `.xlsx` file instead.

### 2. Import the spreadsheet into SQLite

```bash
python spreadsheet_to_sqlite.py
```

The script:
- Opens the Excel file and reads the header row as column names
- Detects column types automatically (TEXT, INTEGER, or REAL)
- Creates a matching SQLite table
- Inserts every row from the spreadsheet

It prints the generated SQL so you can see exactly what happens:

```
Generated SQL:
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER,
    start_date TEXT
);

Inserted 10 row(s) into 'employees'.
Done! Database saved to 'data.db' — table: 'employees'
```

**Custom file and database:**

```bash
python spreadsheet_to_sqlite.py --file my_data.xlsx --db my_database.db
```

### 3. Export a PDF report from the database

```bash
python sqlite_to_pdf_report.py
```

This generates `report.pdf` containing:
- A title with the table name and a timestamp
- Summary statistics (total rows, min/max/avg for numeric columns)
- A formatted data table with alternating row colors

**Custom database, table, and output:**

```bash
python sqlite_to_pdf_report.py --db my_database.db --table employees --output my_report.pdf
```

## Run Everything at Once

```bash
python create_sample_spreadsheet.py && python spreadsheet_to_sqlite.py && python sqlite_to_pdf_report.py
```

After running, you will have three generated files:

```
employees.xlsx   -- the spreadsheet
data.db          -- the SQLite database
report.pdf       -- the PDF report
```

## Using Your Own Spreadsheet

You can use any `.xlsx` file. The script reads the first row as column headers and all subsequent rows as data. Just point it at your file:

```bash
python spreadsheet_to_sqlite.py --file your_file.xlsx
python sqlite_to_pdf_report.py --table your_sheet_name
```

The table name in SQLite is taken from the Excel sheet name (the tab at the bottom of the spreadsheet).
