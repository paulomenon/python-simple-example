# Recursive Merge Sort

Implements the merge sort algorithm — a classic divide-and-conquer sorting method. The script includes a verbose mode that visualizes each recursive split and merge step.

## How to Run

```bash
python merge_sort.py
```

## Example

```
Recursive Merge Sort
------------------------------

Original list: [42, 17, 83, 5, 61, 29, 74, 38]

--- Step-by-step ---
merge_sort([42, 17, 83, 5, 61, 29, 74, 38])
  merge_sort([42, 17, 83, 5])
    merge_sort([42, 17])
      merge_sort([42])
      merge_sort([17])
      → merged: [17, 42]
    merge_sort([83, 5])
      merge_sort([83])
      merge_sort([5])
      → merged: [5, 83]
    → merged: [5, 17, 42, 83]
  ...
  → merged: [5, 17, 29, 38, 42, 61, 74, 83]

Sorted result: [5, 17, 29, 38, 42, 61, 74, 83]

--- Performance test ---
Sorted 1,000 elements in 0.0051 seconds
```

## How It Works

1. **Divide**: Split the list into two halves
2. **Conquer**: Recursively sort each half
3. **Merge**: Combine the two sorted halves into one sorted list

Time complexity: **O(n log n)** in all cases (best, average, worst).

## What You'll Learn

- Recursion with a base case
- Divide-and-conquer algorithm design
- Merging two sorted lists efficiently
- Visualizing recursive call depth
