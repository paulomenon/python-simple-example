# Bubble Sort Algorithm

Implements bubble sort — the simplest comparison-based sorting algorithm. Includes a basic version, an optimized version with early exit, and a visual step-by-step mode.

## How to Run

```bash
python bubble_sort.py
```

## Example

```
Bubble Sort Algorithm
------------------------------

--- Visual mode (8 elements) ---
  Start:  [34, 12, 47, 8, 23, 41, 5, 29]
  Pass 1: [12, 34, 8, 23, 41, 5, 29, 47]
  Pass 2: [12, 8, 23, 34, 5, 29, 41, 47]
  Pass 3: [8, 12, 23, 5, 29, 34, 41, 47]
  Pass 4: [8, 12, 5, 23, 29, 34, 41, 47]
  Pass 5: [8, 5, 12, 23, 29, 34, 41, 47]
  Pass 6: [5, 8, 12, 23, 29, 34, 41, 47]
  Pass 7: [5, 8, 12, 23, 29, 34, 41, 47]
  (No swaps — list is sorted, stopping early)

--- Optimized sort stats ---
Random list (20 elements):    17 passes, 164 comparisons
Already sorted (20 elements): 1 passes, 19 comparisons

--- Performance test ---
Sorted 2,000 elements in 0.3421s
(Bubble sort is O(n²) — much slower than merge/quick sort for large lists)
```

## How It Works

1. Walk through the list, comparing each pair of adjacent elements
2. Swap them if they're in the wrong order
3. Repeat until no swaps are needed (the list is sorted)

After each pass, the largest unsorted element "bubbles up" to its correct position.

Time complexity: **O(n²)** average/worst, **O(n)** best (already sorted, with optimization).

## What You'll Learn

- Nested loops for pairwise comparisons
- In-place swapping with tuple unpacking
- Early exit optimization (stop when no swaps occur)
- Why O(n²) algorithms don't scale for large data
