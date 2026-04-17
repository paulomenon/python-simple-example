# Python Simple Example

This repository contains a simple Python project demonstrating basic programming concepts and functionalities. It serves as a practical example for beginners to understand Python syntax, structures, and standard libraries.

## Table of Contents

- [Python Simple Example](#python-simple-example)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Features

- Basic Python syntax
- Functions and modules
- Exception handling
- Input and output operations
- Simple data structures (lists, dictionaries)
- Spreadsheet to SQLite database conversion
- PDF report generation from database data
- Intermediate examples: algorithms, file I/O, ciphers, text games
- Advanced examples: sorting algorithms, graph traversal, data structures, REST APIs, threading, backtracking

## Beginner Examples

Each folder contains a self-contained example with its own README explaining how to run it.

| Folder | Example | What it covers |
|---|---|---|
| `hello-world-sample/` | Hello World | `print()`, basic script structure |
| `welcome-sample/` | Name Input Program | `input()`, string concatenation |
| `calculator-sample/` | Simple Calculator | User input, `if/elif/else`, arithmetic, division by zero |
| `even-odd-sample/` | Even or Odd Checker | Modulo operator (`%`), conditionals |
| `age-checker-sample/` | Age Checker | Chained conditionals, comparison operators, f-strings |
| `loop-samples/` | Basic For Loop Counter | `for` loop, `range()`, patterns |
| `multiplication-table-sample/` | Multiplication Table | `for` loop, string formatting, arithmetic in loops |
| `temperature-converter-sample/` | Temperature Converter | Math formulas, float formatting, multiple conversions |
| `constant/` | Unit Converters | Constants, functions, miles/km, cm/inches |
| `array-sample/` | Arrays and Lists | Lists, iteration, basic data structures |
| `welcome-function/` | Functions | Defining and calling functions, return values |
| `match-choice-sample/` | Match/Case | Python 3.10+ structural pattern matching |
| `game-samples/` | Mini Games | Loops, random numbers, user interaction |
| `spreadsheet-sample/` | Spreadsheet to SQLite to PDF | File I/O, databases, PDF generation |

## Intermediate Examples

The `intermediate-level/` folder contains examples that build on the basics. Each subfolder is self-contained with its own README.

| Folder | Example | What it covers |
|---|---|---|
| `intermediate-level/function-based-calculator/` | Function-Based Calculator | Functions, return values, dict-based dispatch |
| `intermediate-level/word-count-analyzer/` | Word Count Analyzer | String methods, dictionaries, sorting |
| `intermediate-level/palindrome-checker/` | Palindrome Checker | String slicing, reversal, input cleaning |
| `intermediate-level/fibonacci-generator/` | Fibonacci Sequence Generator | Loops, sequences, list indexing |
| `intermediate-level/number-base-converter/` | Number Base Converter | `bin()`, `hex()`, `int()` with base, validation |
| `intermediate-level/caesar-cipher/` | Caesar Cipher Encoder/Decoder | `ord()`/`chr()`, modular arithmetic |
| `intermediate-level/file-search-tool/` | Simple File Search Tool | `os.walk()`, directory traversal, file filtering |
| `intermediate-level/todo-list/` | To-Do List (with file saving) | JSON file I/O, persistent data, CRUD operations |
| `intermediate-level/text-adventure-game/` | Basic Text Adventure Game | Game state, dictionaries as data, input parsing |
| `intermediate-level/email-slicer/` | Email Slicer | `split()`, `rsplit()`, input validation |

## Advanced Examples

The `advanced-level/` folder covers algorithms, data structures, networking, concurrency, and backtracking. Each subfolder is self-contained with its own README.

| Folder | Example | What it covers |
|---|---|---|
| `advanced-level/recursive-merge-sort/` | Recursive Merge Sort | Divide and conquer, recursion, merging sorted halves |
| `advanced-level/quick-sort/` | Quick Sort Algorithm | Partitioning, pivot selection, in-place sorting |
| `advanced-level/depth-first-search/` | Depth-First Search (DFS) | Graph traversal, stacks, recursion |
| `advanced-level/breadth-first-search/` | Breadth-First Search (BFS) | Queues, shortest path, level-order |
| `advanced-level/bubble-sort/` | Bubble Sort Algorithm | Nested loops, swapping, early exit optimization |
| `advanced-level/hash-table/` | Hash Table Implementation | Hashing, collision chaining, auto-resize |
| `advanced-level/binary-tree-traversal/` | Binary Tree Traversal | BST, in/pre/post-order, level-order |
| `advanced-level/rest-api-client/` | REST API Client | HTTP requests, JSON parsing, error handling |
| `advanced-level/multithreaded-downloader/` | Multithreaded Downloader | Threading, concurrent I/O, performance comparison |
| `advanced-level/sudoku-solver/` | Sudoku Solver (Backtracking) | Backtracking, constraint satisfaction, recursion |

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/paulomenon/python-simple-example.git
   ```
2. Navigate to the project directory:
   ```bash
   cd python-simple-example
   ```
3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Navigate into any example folder and run the script:

```bash
cd hello-world-sample
python hello_world.py
```

Each folder has its own README with instructions and expected output.

## Spreadsheet Sample

The `spreadsheet-sample/` folder demonstrates how to read an Excel spreadsheet, save the data into a SQLite database, and export a PDF report. It contains three scripts that run in sequence.

### Install dependencies

```bash
pip install -r spreadsheet-sample/requirements.txt
```

### Step 1: Create a sample spreadsheet

Generates an `employees.xlsx` file with 10 sample rows (id, name, department, salary, start_date):

```bash
cd spreadsheet-sample
python create_sample_spreadsheet.py
```

You can also use your own `.xlsx` file instead.

### Step 2: Import the spreadsheet into SQLite

Reads the Excel file, detects column types automatically, creates a matching SQLite table, and inserts all rows:

```bash
python spreadsheet_to_sqlite.py
```

This creates a `data.db` file with an `employees` table. The script prints the generated SQL so you can see exactly what it does:

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
```

You can point it at any spreadsheet and database:

```bash
python spreadsheet_to_sqlite.py --file my_data.xlsx --db my_database.db
```

### Step 3: Export a PDF report from the database

Reads the data back from SQLite and generates a formatted PDF report with a summary and data table:

```bash
python sqlite_to_pdf_report.py
```

This creates a `report.pdf` with:
- A title and timestamp
- Summary statistics (row count, min/max/avg for numeric columns)
- A formatted table with all rows and alternating row colors

You can customize the table and output path:

```bash
python sqlite_to_pdf_report.py --db my_database.db --table employees --output my_report.pdf
```

### Run all three steps at once

```bash
cd spreadsheet-sample
python create_sample_spreadsheet.py && python spreadsheet_to_sqlite.py && python sqlite_to_pdf_report.py
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to create a pull request. Please ensure your code follows the project's style guidelines and includes appropriate tests.

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Python community for the vast resources and libraries that make development easier.
- Inspired by various Python tutorials and documentation.

```

Feel free to adjust sections as necessary based on your project’s specifics, especially in the **Features**, **Usage**, and **Contributing** sections. Let me know if you need any more help!