# To-Do List with File Saving
# Manages a to-do list that persists between runs using a JSON file.

import json
import os

TODO_FILE = "todos.json"


def load_todos():
    """Load the to-do list from the JSON file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []


def save_todos(todos):
    """Save the to-do list to the JSON file."""
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def display_todos(todos):
    """Display all to-do items."""
    if not todos:
        print("\n  Your to-do list is empty.")
        return

    print(f"\n  Your To-Do List ({len(todos)} item(s)):")
    print("  " + "-" * 35)
    for i, item in enumerate(todos, start=1):
        status = "done" if item["done"] else "    "
        print(f"  {i}. [{status}] {item['task']}")


def add_todo(todos):
    task = input("Enter a new task: ").strip()
    if task:
        todos.append({"task": task, "done": False})
        save_todos(todos)
        print(f"  Added: '{task}'")
    else:
        print("  Task cannot be empty.")


def complete_todo(todos):
    display_todos(todos)
    if not todos:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(todos):
            todos[num - 1]["done"] = True
            save_todos(todos)
            print(f"  Marked '{todos[num - 1]['task']}' as done!")
        else:
            print("  Invalid task number.")
    except ValueError:
        print("  Please enter a number.")


def delete_todo(todos):
    display_todos(todos)
    if not todos:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(todos):
            removed = todos.pop(num - 1)
            save_todos(todos)
            print(f"  Deleted: '{removed['task']}'")
        else:
            print("  Invalid task number.")
    except ValueError:
        print("  Please enter a number.")


def main():
    todos = load_todos()

    while True:
        print("\n===== To-Do List =====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Quit")
        print("======================")

        choice = input("Choose (1-5): ")

        if choice == "1":
            display_todos(todos)
        elif choice == "2":
            add_todo(todos)
        elif choice == "3":
            complete_todo(todos)
        elif choice == "4":
            delete_todo(todos)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("  Invalid choice.")


main()
