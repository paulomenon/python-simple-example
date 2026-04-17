# Quick Sort Algorithm

Implements quick sort in two styles: a clean list-comprehension version that creates new lists, and an in-place version using the Lomuto partition scheme. Includes a performance comparison.

## How to Run

```bash
python quick_sort.py
```

## Example

```
Quick Sort Algorithm
------------------------------

Original list: [73, 12, 98, 45, 31, 67, 54, 89, 23, 76]
Quick sort (new list): [12, 23, 31, 45, 54, 67, 73, 76, 89, 98]
Quick sort (in-place): [12, 23, 31, 45, 54, 67, 73, 76, 89, 98]

--- Performance comparison ---
New-list version:  5,000 elements in 0.0123s
In-place version:  5,000 elements in 0.0098s
```

## How It Works

1. **Pick a pivot** element from the list
2. **Partition**: rearrange so elements < pivot are on the left, > pivot on the right
3. **Recurse** on the left and right partitions

Average time complexity: **O(n log n)**. Worst case: **O(n²)** when the pivot is always the smallest or largest element.

## What You'll Learn

- Partition-based sorting with a pivot
- List comprehensions vs in-place swapping
- The Lomuto partition scheme
- Comparing algorithm variants with timing
