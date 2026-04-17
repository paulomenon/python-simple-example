# To-Do List (with File Saving)

A simple command-line to-do list manager. Tasks are saved to a JSON file so they persist between runs. You can add, view, complete, and delete tasks.

## How to Run

```bash
python todo_list.py
```

Tasks are stored in `todos.json` in the same directory, created automatically on first use.

## Example

```
===== To-Do List =====
1. View tasks
2. Add task
3. Mark task as done
4. Delete task
5. Quit
======================
Choose (1-5): 2
Enter a new task: Buy groceries
  Added: 'Buy groceries'

Choose (1-5): 2
Enter a new task: Finish homework
  Added: 'Finish homework'

Choose (1-5): 1

  Your To-Do List (2 item(s)):
  -----------------------------------
  1. [    ] Buy groceries
  2. [    ] Finish homework

Choose (1-5): 3
  1. [    ] Buy groceries
  2. [    ] Finish homework
Enter task number to mark as done: 1
  Marked 'Buy groceries' as done!

Choose (1-5): 1
  1. [done] Buy groceries
  2. [    ] Finish homework
```

## What You'll Learn

- File I/O with `json.load()` and `json.dump()`
- Persistent storage — data survives program restarts
- Working with lists of dictionaries
- Building a menu-driven CLI application
