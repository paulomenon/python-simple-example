# Sudoku Solver (Backtracking)

Solves any valid 9x9 Sudoku puzzle using recursive backtracking. Includes two built-in puzzles (easy and hard) and reports solving statistics.

## How to Run

```bash
python sudoku_solver.py
```

## Example

```
Sudoku Solver (Backtracking)
===================================

--- Easy Puzzle (51 empty cells) ---

  5 3 . | . 7 . | . . .
  6 . . | 1 9 5 | . . .
  . 9 8 | . . . | . 6 .
  ------+-------+------
  8 . . | . 6 . | . . 3
  4 . . | 8 . 3 | . . 1
  7 . . | . 2 . | . . 6
  ------+-------+------
  . 6 . | . . . | 2 8 .
  . . . | 4 1 9 | . . 5
  . . . | . 8 . | . 7 9

  Solved!

  5 3 4 | 6 7 8 | 9 1 2
  6 7 2 | 1 9 5 | 3 4 8
  1 9 8 | 3 4 2 | 5 6 7
  ------+-------+------
  8 5 9 | 7 6 1 | 4 2 3
  4 2 6 | 8 5 3 | 7 9 1
  7 1 3 | 9 2 4 | 8 5 6
  ------+-------+------
  9 6 1 | 5 3 7 | 2 8 4
  2 8 7 | 4 1 9 | 6 3 5
  3 4 5 | 2 8 6 | 1 7 9

  Attempts:    244
  Backtracks:  4
  Time:        0.0012s
```

## How It Works

1. **Find** the next empty cell (value `0`)
2. **Try** digits 1-9 in that cell
3. **Check** if the digit is valid (not already in the same row, column, or 3x3 box)
4. **Recurse** to the next empty cell
5. **Backtrack** if no valid digit works — reset the cell and try the next option

This is a classic example of **constraint satisfaction** solved by **backtracking**.

## What You'll Learn

- Recursive backtracking as a problem-solving strategy
- Constraint checking (rows, columns, 3x3 boxes)
- Deep copying to preserve original puzzle state
- Tracking algorithm performance (attempts, backtracks, timing)
