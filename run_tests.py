#!/usr/bin/env python3
"""
Automated test runner for python-simple-example.

Usage:
    python run_tests.py basic          # Run beginner-level examples
    python run_tests.py intermediate   # Run intermediate-level examples
    python run_tests.py advanced       # Run advanced-level examples
    python run_tests.py all            # Run everything

    Add -v for verbose output (shows each script's full output).
"""

import argparse
import subprocess
import sys
import os
import time

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
TIMEOUT = 15

# Each entry: (display_name, script_path_relative_to_repo, stdin_input or None)
# stdin_input feeds text to scripts that call input(), preventing hangs.

BASIC = [
    ("Hello World",              "hello-world-sample/hello_world.py",              None),
    ("Name Input Program",       "welcome-sample/welcome.py",                      "Tester\n"),
    ("Simple Calculator",        "calculator-sample/simple_calculator.py",          "1\n10\n5\n"),
    ("Even or Odd Checker",      "even-odd-sample/even_or_odd.py",                 "7\n"),
    ("Age Checker",              "age-checker-sample/age_checker.py",              "Tester\n25\n"),
    ("For Loop Counter",         "loop-samples/for_loop_sample.py",               None),
    ("While Loop Counter",       "loop-samples/while_loop_sample.py",             None),
    ("While Until Menu",         "loop-samples/while_until.py",                   "5\n"),
    ("Multiplication Table",     "multiplication-table-sample/multiplication_table.py", "7\n"),
    ("Temperature Converter",    "temperature-converter-sample/temperature_converter.py", "1\n100\n"),
    ("Miles to Km",              "constant/convert_miles_to_km.py",               None),
    ("Cm to Inches",             "constant/convert_cm_to_inches.py",              "100\n"),
    ("Metric/Imperial",          "constant/convert_metric_imperial.py",           "1\n50\n"),
    ("Simple Array",             "array-sample/simple_array.py",                  None),
    ("Array Names",              "array-sample/array_names.py",                   "4\n"),
    ("Array Numbers",            "array-sample/array_numbers.py",                 "6\n"),
    ("Welcome Function",         "welcome-function/welcome_function.py",          "Tester\n"),
    ("Calculate Area",           "welcome-function/calculate_area.py",            None),
    ("Match/Case Menu",          "match-choice-sample/match_choice.py",           "5\n"),
    ("Guess Number Game",        "game-samples/guess_number.py",                  "\n".join(str(i) for i in range(1, 101)) + "\n"),
    ("Magic 8-Ball",             "game-samples/simple_magic8.py",                 "Will it work?\nno\n"),
    ("Roulette Game",            "game-samples/simple_roulette.py",               "17\n"),
]

INTERMEDIATE = [
    ("Function-Based Calculator",  "intermediate-level/function-based-calculator/calculator.py", "1\n10\n5\n7\n"),
    ("Word Count Analyzer",        "intermediate-level/word-count-analyzer/word_count_analyzer.py", "The quick brown fox jumps over the lazy dog.\n\n"),
    ("Palindrome Checker",         "intermediate-level/palindrome-checker/palindrome_checker.py", "racecar\nquit\n"),
    ("Fibonacci Generator",        "intermediate-level/fibonacci-generator/fibonacci_generator.py", "10\n"),
    ("Number Base Converter",      "intermediate-level/number-base-converter/base_converter.py", "1\n255\n"),
    ("Caesar Cipher",              "intermediate-level/caesar-cipher/caesar_cipher.py", "1\nHello World\n3\n"),
    ("File Search Tool",           "intermediate-level/file-search-tool/file_search.py", ".\n2\n.py\n"),
    ("To-Do List",                 "intermediate-level/todo-list/todo_list.py", "2\nTest task\n1\n5\n"),
    ("Text Adventure Game",        "intermediate-level/text-adventure-game/text_adventure.py", "quit\n"),
    ("Email Slicer",               "intermediate-level/email-slicer/email_slicer.py", "user@example.com\nquit\n"),
]

ADVANCED = [
    ("Recursive Merge Sort",       "advanced-level/recursive-merge-sort/merge_sort.py",        None),
    ("Quick Sort",                 "advanced-level/quick-sort/quick_sort.py",                   None),
    ("Depth-First Search",         "advanced-level/depth-first-search/dfs.py",                  None),
    ("Breadth-First Search",       "advanced-level/breadth-first-search/bfs.py",                None),
    ("Bubble Sort",                "advanced-level/bubble-sort/bubble_sort.py",                  None),
    ("Hash Table",                 "advanced-level/hash-table/hash_table.py",                    None),
    ("Binary Tree Traversal",      "advanced-level/binary-tree-traversal/binary_tree.py",        None),
    ("Sudoku Solver",              "advanced-level/sudoku-solver/sudoku_solver.py",               None),
]

# These require network or external packages — listed separately so failures
# are reported clearly rather than crashing the whole suite.
ADVANCED_NETWORK = [
    ("REST API Client",            "advanced-level/rest-api-client/api_client.py",                None),
    ("Multithreaded Downloader",   "advanced-level/multithreaded-downloader/downloader.py",       None),
]

# Spreadsheet sample needs openpyxl/reportlab — skip in default basic run
SPREADSHEET = [
    ("Create Sample Spreadsheet",  "spreadsheet-sample/create_sample_spreadsheet.py",  None),
    ("Spreadsheet to SQLite",      "spreadsheet-sample/spreadsheet_to_sqlite.py",      None),
    ("SQLite to PDF Report",       "spreadsheet-sample/sqlite_to_pdf_report.py",       None),
]


def run_script(name, script_path, stdin_input, verbose):
    """Run a single script and return (passed: bool, output: str)."""
    full_path = os.path.join(REPO_ROOT, script_path)

    if not os.path.exists(full_path):
        return False, f"File not found: {script_path}"

    working_dir = os.path.dirname(full_path)

    try:
        result = subprocess.run(
            [sys.executable, full_path],
            input=stdin_input,
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
            cwd=working_dir,
        )
        output = result.stdout
        if result.stderr:
            output += result.stderr

        passed = result.returncode == 0
        return passed, output.strip()

    except subprocess.TimeoutExpired:
        return False, f"Timed out after {TIMEOUT}s"
    except Exception as e:
        return False, str(e)


def run_suite(suite_name, tests, verbose):
    """Run a list of tests and return (passed_count, failed_count, failed_names)."""
    passed = 0
    failed = 0
    failed_names = []

    print(f"\n{'=' * 50}")
    print(f"  {suite_name}")
    print(f"{'=' * 50}")

    for name, script_path, stdin_input in tests:
        if verbose:
            print(f"\n--- Running: {name} ({script_path}) ---")

        ok, output = run_script(name, script_path, stdin_input, verbose)

        if ok:
            passed += 1
            print(f"  PASS  {name}")
            if verbose and output:
                for line in output.split("\n"):
                    print(f"        {line}")
        else:
            failed += 1
            failed_names.append(name)
            print(f"  FAIL  {name}")
            if verbose and output:
                for line in output.split("\n"):
                    print(f"        {line}")
            elif not verbose and output:
                # Show first line of error even in quiet mode
                first_line = output.split("\n")[-1][:80]
                print(f"        {first_line}")

    return passed, failed, failed_names


def main():
    parser = argparse.ArgumentParser(
        description="Run automated tests for python-simple-example",
    )
    parser.add_argument(
        "level",
        choices=["basic", "intermediate", "advanced", "all"],
        help="Which examples to test",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show full output for each script",
    )
    args = parser.parse_args()

    start_time = time.time()
    total_passed = 0
    total_failed = 0
    all_failed = []

    suites = []

    if args.level in ("basic", "all"):
        suites.append(("Beginner Level", BASIC))
        suites.append(("Spreadsheet Sample", SPREADSHEET))

    if args.level in ("intermediate", "all"):
        suites.append(("Intermediate Level", INTERMEDIATE))

    if args.level in ("advanced", "all"):
        suites.append(("Advanced Level", ADVANCED))
        suites.append(("Advanced Level (Network)", ADVANCED_NETWORK))

    for suite_name, tests in suites:
        p, f, names = run_suite(suite_name, tests, args.verbose)
        total_passed += p
        total_failed += f
        all_failed.extend(names)

    elapsed = time.time() - start_time

    print(f"\n{'=' * 50}")
    print(f"  RESULTS: {total_passed} passed, {total_failed} failed  ({elapsed:.1f}s)")
    print(f"{'=' * 50}")

    if all_failed:
        print(f"\n  Failed tests:")
        for name in all_failed:
            print(f"    - {name}")
        print()
        sys.exit(1)
    else:
        print(f"\n  All tests passed!\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
