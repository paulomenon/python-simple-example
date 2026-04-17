# Quick Sort Algorithm
# Partition-based sorting: pick a pivot, split elements into
# smaller-than-pivot and larger-than-pivot groups, then recurse.

import random
import time


def quick_sort(arr):
    """Sort a list using quick sort (creates new lists)."""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_in_place(arr, low, high):
    """In-place quick sort using Lomuto partition scheme."""
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """Lomuto partition: use last element as pivot."""
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


print("Quick Sort Algorithm")
print("-" * 30)

data = [random.randint(1, 100) for _ in range(10)]
print(f"\nOriginal list: {data}")

sorted_new = quick_sort(data)
print(f"Quick sort (new list): {sorted_new}")

data_copy = data.copy()
quick_sort_in_place(data_copy, 0, len(data_copy) - 1)
print(f"Quick sort (in-place): {data_copy}")

print("\n--- Performance comparison ---")
large = [random.randint(1, 10000) for _ in range(5000)]

start = time.time()
quick_sort(large)
elapsed_new = time.time() - start
print(f"New-list version:  5,000 elements in {elapsed_new:.4f}s")

large_copy = large.copy()
start = time.time()
quick_sort_in_place(large_copy, 0, len(large_copy) - 1)
elapsed_ip = time.time() - start
print(f"In-place version:  5,000 elements in {elapsed_ip:.4f}s")
