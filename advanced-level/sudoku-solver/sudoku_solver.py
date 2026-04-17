# Sudoku Solver (Backtracking)
# Solves a 9x9 Sudoku puzzle using recursive backtracking.
# Tries placing digits 1-9 in each empty cell, checking constraints,
# and backtracks when no valid digit fits.

def print_board(board):
    """Print the Sudoku board with grid lines."""
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("  ------+-------+------")

        line = ""
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                line += "| "
            line += f"{val if val != 0 else '.'} "

        print(f"  {line}")


def find_empty(board):
    """Find the next empty cell (value 0). Returns (row, col) or None."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def is_valid(board, num, pos):
    """Check if placing num at pos (row, col) is valid."""
    row, col = pos

    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve(board, stats=None):
    """Solve the Sudoku board using backtracking. Returns True if solved."""
    if stats is None:
        stats = {"attempts": 0, "backtracks": 0}

    empty = find_empty(board)
    if empty is None:
        return True  # All cells filled — puzzle solved

    row, col = empty

    for num in range(1, 10):
        stats["attempts"] += 1
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board, stats):
                return True

            # Backtrack
            board[row][col] = 0
            stats["backtracks"] += 1

    return False


# ---- Example puzzles ----

easy_puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

hard_puzzle = [
    [0, 0, 0, 6, 0, 0, 4, 0, 0],
    [7, 0, 0, 0, 0, 3, 6, 0, 0],
    [0, 0, 0, 0, 9, 1, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 1, 8, 0, 0, 0, 3],
    [0, 0, 0, 3, 0, 6, 0, 4, 5],
    [0, 4, 0, 2, 0, 0, 0, 6, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 1, 0, 0],
]

import time
import copy

print("Sudoku Solver (Backtracking)")
print("=" * 35)

for name, puzzle in [("Easy", easy_puzzle), ("Hard", hard_puzzle)]:
    board = copy.deepcopy(puzzle)
    empties = sum(row.count(0) for row in board)

    print(f"\n--- {name} Puzzle ({empties} empty cells) ---\n")
    print_board(board)

    stats = {"attempts": 0, "backtracks": 0}
    start = time.time()
    solved = solve(board, stats)
    elapsed = time.time() - start

    if solved:
        print(f"\n  Solved!\n")
        print_board(board)
        print(f"\n  Attempts:    {stats['attempts']:,}")
        print(f"  Backtracks:  {stats['backtracks']:,}")
        print(f"  Time:        {elapsed:.4f}s")
    else:
        print("\n  No solution exists for this puzzle.")
