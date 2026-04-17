# Advanced Level Examples

This folder contains Python examples that tackle real-world patterns and classic computer science problems: sorting algorithms, graph traversal, data structures from scratch, networking, concurrency, and backtracking.

## Examples

| Folder | Example | Key Concepts |
|---|---|---|
| `recursive-merge-sort/` | Recursive Merge Sort | Divide and conquer, recursion, merging sorted halves |
| `quick-sort/` | Quick Sort Algorithm | Partitioning, pivot selection, in-place sorting |
| `depth-first-search/` | Depth-First Search (DFS) | Graph traversal, stacks, recursion |
| `breadth-first-search/` | Breadth-First Search (BFS) | Graph traversal, queues, shortest path |
| `bubble-sort/` | Bubble Sort Algorithm | Nested loops, swapping, optimization with early exit |
| `hash-table/` | Hash Table Implementation | Hashing, collision handling, custom data structures |
| `binary-tree-traversal/` | Binary Tree Traversal | Trees, in-order / pre-order / post-order, recursion |
| `rest-api-client/` | REST API Client | HTTP requests, JSON parsing, error handling |
| `multithreaded-downloader/` | Multithreaded Downloader | Threading, concurrent I/O, progress tracking |
| `sudoku-solver/` | Sudoku Solver (Backtracking) | Backtracking, constraint satisfaction, recursion |

## How to Run

Each subfolder is self-contained. Navigate into any folder, read its README, and run the script:

```bash
cd advanced-level/sudoku-solver
python sudoku_solver.py
```

Most examples use only the Python standard library. The REST API Client requires the `requests` package — see its README for details.

## Prerequisites

- Python 3.6 or higher
- A terminal or command prompt
- `requests` library (only for `rest-api-client/`)

## Structure

Every example follows the same pattern:

```
folder-name/
├── script_name.py    # The Python script
└── README.md         # How to run it, example output, what you'll learn
```
