# Simple File Search Tool

Searches a directory and all its subdirectories for files matching a name or extension. Displays the full path and file size for each match.

## How to Run

```bash
python file_search.py
```

## Example

```
File Search Tool
------------------------------
Enter directory to search (or '.' for current): ../..

Search by:
1. Filename (partial match)
2. File extension
Choose (1/2): 2
Enter extension (e.g. .py, .txt): .py

Found 23 file(s):

  ../../hello-world-sample/hello_world.py  (43.0 B)
  ../../calculator-sample/simple_calculator.py  (789.0 B)
  ...
```

## What You'll Learn

- Using `os.walk()` to traverse directory trees
- `os.path.join()` for building file paths
- `os.path.getsize()` to read file sizes
- String methods (`lower()`, `endswith()`) for case-insensitive matching
