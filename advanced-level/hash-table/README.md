# Hash Table Implementation

A hash table built from scratch using an array of buckets with chaining (lists) for collision resolution. Supports insert, get, delete, auto-resizing, and displays the internal bucket structure.

## How to Run

```bash
python hash_table.py
```

## Example

```
Hash Table Implementation
------------------------------

--- Inserting items ---
  put('apple', 3)
  put('banana', 5)
  put('cherry', 2)
  put('date', 8)
  put('elderberry', 1)
  put('fig', 4)

--- Internal structure ---
  Hash Table (size=8, items=6):
    Bucket  0: [banana: 5, fig: 4]
    Bucket  2: [date: 8]
    Bucket  3: [apple: 3]
    Bucket  5: [elderberry: 1]
    Bucket  7: [cherry: 2]

--- Lookups ---
  get('banana'):     5
  get('cherry'):     2
  get('grape'):      NOT FOUND
  contains('apple'): True
  contains('grape'): False

--- Delete ---
  Deleted 'cherry'
  get('cherry'):     NOT FOUND

--- All keys:   ['banana', 'fig', 'date', 'apple', 'elderberry']
--- All values: [5, 4, 8, 3, 1]
```

## How It Works

1. **Hashing**: Convert a key to a bucket index using `hash(key) % size`
2. **Chaining**: Each bucket is a list — collisions are stored in the same bucket
3. **Auto-resize**: When the load factor exceeds 0.75, the table doubles in size and rehashes all entries

Average time complexity: **O(1)** for get/put/delete.

## What You'll Learn

- How hash tables work under the hood
- Collision resolution with chaining
- Dynamic resizing and load factor management
- Building a custom data structure with a class
