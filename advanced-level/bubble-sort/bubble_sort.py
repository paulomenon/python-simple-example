# Bubble Sort Algorithm
# Repeatedly steps through the list, compares adjacent elements,
# and swaps them if they are in the wrong order. Includes an
# optimized version with early exit when the list is already sorted.

import random
import time


def bubble_sort(arr):
    """Basic bubble sort. Modifies the list in place."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_optimized(arr):
    """Optimized bubble sort with early exit and shrinking range."""
    n = len(arr)
    comparisons = 0
    passes = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        passes += 1
        if not swapped:
            break

    return arr, passes, comparisons


def bubble_sort_visual(arr):
    """Bubble sort with step-by-step visualization."""
    n = len(arr)
    print(f"  Start:  {arr}")

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        print(f"  Pass {i + 1}: {arr}")
        if not swapped:
            print("  (No swaps — list is sorted, stopping early)")
            break

    return arr


print("Bubble Sort Algorithm")
print("-" * 30)

data = [random.randint(1, 50) for _ in range(8)]
print(f"\n--- Visual mode (8 elements) ---")
bubble_sort_visual(data.copy())

print(f"\n--- Optimized sort stats ---")
random_data = [random.randint(1, 100) for _ in range(20)]
_, passes, comps = bubble_sort_optimized(random_data.copy())
print(f"Random list (20 elements):    {passes} passes, {comps} comparisons")

sorted_data = list(range(1, 21))
_, passes, comps = bubble_sort_optimized(sorted_data.copy())
print(f"Already sorted (20 elements): {passes} passes, {comps} comparisons")

print(f"\n--- Performance test ---")
large = [random.randint(1, 10000) for _ in range(2000)]
start = time.time()
bubble_sort(large.copy())
elapsed = time.time() - start
print(f"Sorted 2,000 elements in {elapsed:.4f}s")
print("(Bubble sort is O(n²) — much slower than merge/quick sort for large lists)")
