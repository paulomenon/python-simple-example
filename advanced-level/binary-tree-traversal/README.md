# Binary Tree Traversal

Builds a binary search tree (BST) and demonstrates four traversal methods: in-order, pre-order, post-order, and level-order. Includes a visual tree printer.

## How to Run

```bash
python binary_tree.py
```

## Example

```
Binary Tree Traversal
------------------------------

Inserting: [50, 30, 70, 20, 40, 60, 80, 10, 35]

Tree structure:
          ┌── 80
      ┌── 70
      │   └── 60
  └── 50
      │   ┌── 40
      │   │   └── 35
      └── 30
          └── 20
              └── 10

In-order   (sorted): [10, 20, 30, 35, 40, 50, 60, 70, 80]
Pre-order  (root first): [50, 30, 20, 10, 40, 35, 70, 60, 80]
Post-order (root last):  [10, 20, 35, 40, 30, 60, 80, 70, 50]
Level-order (BFS):       [50, 30, 70, 20, 40, 60, 80, 10, 35]

Tree height: 4
```

## Traversal Methods

| Method | Order | Use Case |
|---|---|---|
| In-order | Left → Root → Right | Sorted output from a BST |
| Pre-order | Root → Left → Right | Copying or serializing a tree |
| Post-order | Left → Right → Root | Safe deletion (children before parent) |
| Level-order | Top to bottom, left to right | BFS, finding shortest depth |

## What You'll Learn

- Implementing a binary search tree with classes
- Recursive tree traversal patterns
- Level-order traversal with a queue (BFS)
- Visual tree printing with Unicode box-drawing characters
