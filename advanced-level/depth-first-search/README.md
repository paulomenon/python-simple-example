# Depth-First Search (DFS)

Explores a graph by diving as deep as possible along each branch before backtracking. Includes recursive and iterative implementations, plus a path-finding variant.

## How to Run

```bash
python dfs.py
```

## Example

```
Depth-First Search (DFS)
------------------------------

Graph (adjacency list):
  A → ['B', 'C']
  B → ['A', 'D', 'E']
  C → ['A', 'F']
  D → ['B']
  E → ['B', 'F']
  F → ['C', 'E']

DFS recursive from 'A':  ['A', 'B', 'D', 'E', 'F', 'C']
DFS iterative from 'A':  ['A', 'B', 'D', 'E', 'F', 'C']

Path from A to F: A → B → E → F
Path from D to F: D → B → A → C → F

Disconnected graph — DFS from '1': ['1', '2', '3']
(Nodes X, Y are unreachable from 1)
```

## How It Works

1. Start at a node, mark it as visited
2. Visit an unvisited neighbor and repeat
3. When a node has no unvisited neighbors, backtrack
4. Uses a **stack** (explicit or call stack) — last-in, first-out

Time complexity: **O(V + E)** where V = vertices, E = edges.

## What You'll Learn

- Graph representation with adjacency lists (dictionaries)
- Recursive vs iterative traversal
- Using a stack for backtracking
- Path finding through a graph
