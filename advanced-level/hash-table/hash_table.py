# Hash Table Implementation
# A custom hash table built from scratch using an array of buckets
# with chaining (linked lists) for collision handling.

class HashTable:
    """Hash table with separate chaining for collision resolution."""

    def __init__(self, size=16):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        """Compute a bucket index for the given key."""
        return hash(key) % self.size

    def put(self, key, value):
        """Insert or update a key-value pair."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1

        if self.count / self.size > 0.75:
            self._resize()

    def get(self, key, default=None):
        """Retrieve a value by key. Returns default if not found."""
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return default

    def delete(self, key):
        """Remove a key-value pair. Returns True if found, False otherwise."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.count -= 1
                return True
        return False

    def contains(self, key):
        """Check if a key exists in the table."""
        return self.get(key, _sentinel := object()) is not _sentinel

    def keys(self):
        """Return all keys."""
        return [k for bucket in self.buckets for k, v in bucket]

    def values(self):
        """Return all values."""
        return [v for bucket in self.buckets for k, v in bucket]

    def _resize(self):
        """Double the table size and rehash all entries."""
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def display(self):
        """Print the internal bucket structure."""
        print(f"  Hash Table (size={self.size}, items={self.count}):")
        for i, bucket in enumerate(self.buckets):
            if bucket:
                entries = ", ".join(f"{k}: {v}" for k, v in bucket)
                print(f"    Bucket {i:2d}: [{entries}]")

    def __repr__(self):
        items = ", ".join(f"{k!r}: {v!r}" for bucket in self.buckets for k, v in bucket)
        return f"HashTable({{{items}}})"


print("Hash Table Implementation")
print("-" * 30)

ht = HashTable(size=4)

print("\n--- Inserting items ---")
data = {"apple": 3, "banana": 5, "cherry": 2, "date": 8, "elderberry": 1, "fig": 4}
for key, value in data.items():
    ht.put(key, value)
    print(f"  put('{key}', {value})")

print(f"\n--- Internal structure ---")
ht.display()

print(f"\n--- Lookups ---")
print(f"  get('banana'):     {ht.get('banana')}")
print(f"  get('cherry'):     {ht.get('cherry')}")
print(f"  get('grape'):      {ht.get('grape', 'NOT FOUND')}")
print(f"  contains('apple'): {ht.contains('apple')}")
print(f"  contains('grape'): {ht.contains('grape')}")

print(f"\n--- Delete ---")
ht.delete("cherry")
print(f"  Deleted 'cherry'")
print(f"  get('cherry'):     {ht.get('cherry', 'NOT FOUND')}")

print(f"\n--- All keys:   {ht.keys()}")
print(f"--- All values: {ht.values()}")
