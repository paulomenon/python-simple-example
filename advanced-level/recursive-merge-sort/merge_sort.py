# Recursive Merge Sort
# Divide-and-conquer sorting: split the list in half recursively,
# then merge the sorted halves back together.

def merge_sort(arr):
    """Sort a list using merge sort and return the sorted list."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """Merge two sorted lists into a single sorted list."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_verbose(arr, depth=0):
    """Merge sort with step-by-step output to visualize the recursion."""
    indent = "  " * depth
    print(f"{indent}merge_sort({arr})")

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_verbose(arr[:mid], depth + 1)
    right = merge_sort_verbose(arr[mid:], depth + 1)

    merged = merge(left, right)
    print(f"{indent}  → merged: {merged}")
    return merged


import random

print("Recursive Merge Sort")
print("-" * 30)

data = [random.randint(1, 100) for _ in range(8)]
print(f"\nOriginal list: {data}")

print("\n--- Step-by-step ---")
sorted_data = merge_sort_verbose(data)

print(f"\nSorted result: {sorted_data}")

print("\n--- Performance test ---")
large = [random.randint(1, 10000) for _ in range(1000)]
import time
start = time.time()
merge_sort(large)
elapsed = time.time() - start
print(f"Sorted 1,000 elements in {elapsed:.4f} seconds")
