# Multithreaded Downloader

Downloads multiple files concurrently using Python threads. Compares sequential vs threaded performance to demonstrate the speed advantage of concurrent I/O.

## Prerequisites

```bash
pip install requests
```

## How to Run

```bash
python downloader.py
```

Requires an internet connection. Downloaded files are saved to a `downloads/` folder.

## Example

```
Multithreaded Downloader
------------------------------

Downloading 5 files to ./downloads/

--- Sequential download ---
  ✓ httpbin_1.json (404 bytes) — 1.32s
  ✓ httpbin_2.json (404 bytes) — 1.28s
  ✓ httpbin_3.json (404 bytes) — 1.31s
  ✓ httpbin_4.json (404 bytes) — 1.29s
  ✓ httpbin_5.json (404 bytes) — 1.30s
Total: 6.50s

--- Threaded download (5 threads) ---
  ✓ httpbin_2.json (404 bytes) — 1.31s
  ✓ httpbin_5.json (404 bytes) — 1.32s
  ✓ httpbin_1.json (404 bytes) — 1.33s
  ✓ httpbin_3.json (404 bytes) — 1.34s
  ✓ httpbin_4.json (404 bytes) — 1.35s
Total: 1.36s

--- Results ---
Sequential: 6.50s
Threaded:   1.36s
Speedup:    4.8x faster
```

## How It Works

1. **Sequential**: Downloads each file one after another — total time is the sum of all downloads
2. **Threaded**: Launches multiple threads that download simultaneously — total time is roughly the slowest single download
3. A **lock** ensures thread-safe printing and result tracking

## What You'll Learn

- `threading.Thread` for concurrent execution
- `threading.Lock` for thread-safe shared state
- Why threads are effective for I/O-bound tasks (network, disk)
- Comparing sequential vs concurrent performance
