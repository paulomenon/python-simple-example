# Breadth-First Search (BFS)

Explores a graph level by level using a queue. BFS guarantees the shortest path in unweighted graphs. Includes basic traversal, shortest path finding, and level-order grouping.

## How to Run

```bash
python bfs.py
```

## Example

```
Breadth-First Search (BFS)
------------------------------

Graph (adjacency list):
  A → ['B', 'C']
  B → ['A', 'D', 'E']
  C → ['A', 'F']
  D → ['B']
  E → ['B', 'F']
  F → ['C', 'E']

BFS traversal from 'A': ['A', 'B', 'C', 'D', 'E', 'F']
Shortest path A → F:   A → C → F (length: 2)
Shortest path D → F:   D → B → A → C → F (length: 4)

Level-order traversal from 'A':
  Level 0: ['A']
  Level 1: ['B', 'C']
  Level 2: ['D', 'E', 'F']
```

## How It Works

1. Start at a node, add it to a **queue**
2. Dequeue the front node, visit all its unvisited neighbors, enqueue them
3. Repeat until the queue is empty

The queue ensures nodes are visited in order of their distance from the start — first-in, first-out.

Time complexity: **O(V + E)** where V = vertices, E = edges.

## What You'll Learn

- `collections.deque` for efficient queue operations
- BFS vs DFS — when to use which
- Finding shortest paths in unweighted graphs
- Level-order grouping of nodes by distance
