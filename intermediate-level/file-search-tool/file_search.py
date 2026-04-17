# Simple File Search Tool
# Searches a directory (and subdirectories) for files matching a name or extension.

import os


def search_files(directory, query, search_type="name"):
    """
    Search for files in a directory tree.

    search_type:
      "name"      — match files whose name contains the query
      "extension" — match files with the given extension (e.g. ".py")
    """
    matches = []

    for root, dirs, files in os.walk(directory):
        for filename in files:
            full_path = os.path.join(root, filename)

            if search_type == "name" and query.lower() in filename.lower():
                matches.append(full_path)
            elif search_type == "extension" and filename.lower().endswith(query.lower()):
                matches.append(full_path)

    return matches


def format_size(size_bytes):
    """Convert bytes to a human-readable format."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


print("File Search Tool")
print("-" * 30)

directory = input("Enter directory to search (or '.' for current): ").strip()
if not directory:
    directory = "."

if not os.path.isdir(directory):
    print(f"Error: '{directory}' is not a valid directory.")
    exit()

print("\nSearch by:")
print("1. Filename (partial match)")
print("2. File extension")
choice = input("Choose (1/2): ")

if choice == "1":
    query = input("Enter search term: ")
    search_type = "name"
elif choice == "2":
    query = input("Enter extension (e.g. .py, .txt): ")
    if not query.startswith("."):
        query = "." + query
    search_type = "extension"
else:
    print("Invalid choice.")
    exit()

results = search_files(directory, query, search_type)

if results:
    print(f"\nFound {len(results)} file(s):\n")
    for path in results:
        size = os.path.getsize(path)
        print(f"  {path}  ({format_size(size)})")
else:
    print(f"\nNo files found matching '{query}' in '{directory}'.")
