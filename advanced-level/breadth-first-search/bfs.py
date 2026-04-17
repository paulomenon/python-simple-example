# Breadth-First Search (BFS)
# Explores a graph level by level using a queue.
# Guarantees the shortest path in an unweighted graph.

from collections import deque


def bfs(graph, start):
    """BFS traversal. Returns the list of visited nodes in order."""
    visited = [start]
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return visited


def bfs_shortest_path(graph, start, goal):
    """Find the shortest path from start to goal using BFS."""
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


def bfs_level_order(graph, start):
    """BFS that returns nodes grouped by their distance from start."""
    levels = {}
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        node, level = queue.popleft()
        levels.setdefault(level, []).append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))

    return levels


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print("Breadth-First Search (BFS)")
print("-" * 30)

print("\nGraph (adjacency list):")
for node, neighbors in graph.items():
    print(f"  {node} → {neighbors}")

print(f"\nBFS traversal from 'A': {bfs(graph, 'A')}")

path = bfs_shortest_path(graph, "A", "F")
print(f"Shortest path A → F:   {' → '.join(path)} (length: {len(path) - 1})")

path2 = bfs_shortest_path(graph, "D", "F")
print(f"Shortest path D → F:   {' → '.join(path2)} (length: {len(path2) - 1})")

print("\nLevel-order traversal from 'A':")
levels = bfs_level_order(graph, "A")
for level, nodes in levels.items():
    print(f"  Level {level}: {nodes}")
