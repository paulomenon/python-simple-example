# Multithreaded Downloader
# Downloads multiple files concurrently using threads.
# Demonstrates threading, progress tracking, and comparison
# between sequential and concurrent downloads.

import threading
import time
import os

try:
    import requests
except ImportError:
    print("This example requires the 'requests' library.")
    print("Install it with:  pip install requests")
    exit(1)

# Public domain sample files for testing
URLS = [
    ("httpbin_1.json", "https://httpbin.org/delay/1"),
    ("httpbin_2.json", "https://httpbin.org/delay/1"),
    ("httpbin_3.json", "https://httpbin.org/delay/1"),
    ("httpbin_4.json", "https://httpbin.org/delay/1"),
    ("httpbin_5.json", "https://httpbin.org/delay/1"),
]

OUTPUT_DIR = "downloads"
lock = threading.Lock()
results = {}


def download_file(filename, url):
    """Download a single file and track the result."""
    start = time.time()
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "wb") as f:
            f.write(response.content)

        elapsed = time.time() - start
        size = len(response.content)

        with lock:
            results[filename] = {"status": "ok", "size": size, "time": elapsed}
            print(f"  ✓ {filename} ({size:,} bytes) — {elapsed:.2f}s")

    except Exception as e:
        elapsed = time.time() - start
        with lock:
            results[filename] = {"status": "error", "error": str(e), "time": elapsed}
            print(f"  ✗ {filename} — Error: {e}")


def download_sequential(urls):
    """Download files one at a time."""
    for filename, url in urls:
        download_file(filename, url)


def download_threaded(urls, max_threads=5):
    """Download files concurrently using threads."""
    threads = []

    for filename, url in urls:
        t = threading.Thread(target=download_file, args=(filename, url))
        threads.append(t)
        t.start()

        if len(threads) >= max_threads:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()


os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Multithreaded Downloader")
print("-" * 30)
print(f"\nDownloading {len(URLS)} files to ./{OUTPUT_DIR}/\n")

print("--- Sequential download ---")
results.clear()
start = time.time()
download_sequential(URLS)
seq_time = time.time() - start
print(f"Total: {seq_time:.2f}s\n")

print("--- Threaded download (5 threads) ---")
results.clear()
start = time.time()
download_threaded(URLS, max_threads=5)
thr_time = time.time() - start
print(f"Total: {thr_time:.2f}s\n")

speedup = seq_time / thr_time if thr_time > 0 else 0
print(f"--- Results ---")
print(f"Sequential: {seq_time:.2f}s")
print(f"Threaded:   {thr_time:.2f}s")
print(f"Speedup:    {speedup:.1f}x faster")
