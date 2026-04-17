#!/usr/bin/env python3
"""
Automated test runner for python-simple-example.

Dynamically discovers all .py scripts inside the level folders and runs them.
Interactive scripts are fed input from a matching .input file if one exists
(e.g. welcome.py looks for welcome.input in the same directory).

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

LEVEL_DIRS = {
    "basic": "beginner-level",
    "intermediate": "intermediate-level",
    "advanced": "advanced-level",
}

SKIP_FILES = {"__init__.py"}


# Scan a level folder (e.g. beginner-level/) recursively and collect every .py
# script it contains. For each script, check if a matching .input file exists
# in the same directory — that file will be piped as stdin when the script runs.
# Returns a list of tuples: (display_name, rel_path, abs_path, input_path_or_None).
def discover_scripts(level_dir):
    scripts = []
    base = os.path.join(REPO_ROOT, level_dir)

    if not os.path.isdir(base):
        return scripts

    for root, _dirs, files in os.walk(base):
        py_files = sorted(f for f in files if f.endswith(".py") and f not in SKIP_FILES)
        for py_file in py_files:
            script_path = os.path.join(root, py_file)
            rel_path = os.path.relpath(script_path, REPO_ROOT)

            input_file = os.path.join(root, py_file.replace(".py", ".input"))
            input_path = input_file if os.path.exists(input_file) else None

            folder_name = os.path.relpath(root, base)
            name = f"{folder_name}/{py_file}" if folder_name != "." else py_file

            scripts.append((name, rel_path, script_path, input_path))

    return scripts


# Execute a single Python script as a subprocess. If an .input file was found
# during discovery, its contents are fed to the script's stdin so interactive
# scripts (ones that call input()) don't hang. The script runs inside its own
# directory so relative file paths within the script work correctly. A timeout
# guard kills scripts that take too long (e.g. infinite loops or missing input).
# Returns a tuple: (passed: bool, captured_output: str).
def run_script(script_path, input_path, verbose):
    if not os.path.exists(script_path):
        return False, f"File not found: {script_path}"

    stdin_input = None
    if input_path:
        with open(input_path, "r") as f:
            stdin_input = f.read()

    working_dir = os.path.dirname(script_path)

    try:
        result = subprocess.run(
            [sys.executable, script_path],
            input=stdin_input,
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
            cwd=working_dir,
        )
        output = result.stdout
        if result.stderr:
            output += result.stderr

        return result.returncode == 0, output.strip()

    except subprocess.TimeoutExpired:
        return False, f"Timed out after {TIMEOUT}s"
    except Exception as e:
        return False, str(e)


# Run every script in a discovered list and print PASS/FAIL for each one.
# In normal mode, only the result line is shown (plus the last error line on
# failure). In verbose mode (-v), the full stdout/stderr of every script is
# printed so you can see exactly what each example produced.
# Returns totals: (passed_count, failed_count, list_of_failed_names).
def run_suite(suite_name, scripts, verbose):
    passed = 0
    failed = 0
    failed_names = []

    print(f"\n{'=' * 50}")
    print(f"  {suite_name} ({len(scripts)} scripts)")
    print(f"{'=' * 50}")

    for name, rel_path, script_path, input_path in scripts:
        if verbose:
            has_input = " (with .input)" if input_path else ""
            print(f"\n--- Running: {name}{has_input} ---")

        ok, output = run_script(script_path, input_path, verbose)

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
                first_line = output.split("\n")[-1][:80]
                print(f"        {first_line}")

    return passed, failed, failed_names


# Entry point: parse CLI arguments (level and verbose flag), resolve which
# level folders to scan, discover scripts in each, run them all, and print
# a final summary. Exits with code 0 if everything passed, 1 if any failed.
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

    if args.level == "all":
        levels = ["basic", "intermediate", "advanced"]
    else:
        levels = [args.level]

    for level in levels:
        level_dir = LEVEL_DIRS[level]
        display_name = level_dir.replace("-", " ").title()
        scripts = discover_scripts(level_dir)

        if not scripts:
            print(f"\n  No scripts found in {level_dir}/")
            continue

        p, f, names = run_suite(display_name, scripts, args.verbose)
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
