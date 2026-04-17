# Depth-First Search (DFS)
# Explores a graph by going as deep as possible along each branch
# before backtracking. Implemented both recursively and iteratively.

def dfs_recursive(graph, node, visited=None):
    """DFS using recursion. Returns the list of visited nodes in order."""
    if visited is None:
        visited = []

    visited.append(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited


def dfs_iterative(graph, start):
    """DFS using an explicit stack. Returns the list of visited nodes in order."""
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # Add neighbors in reverse to visit leftmost first
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited


def find_path_dfs(graph, start, goal):
    """Find a path from start to goal using DFS. Returns the path or None."""
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()
        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None


# Example graph (adjacency list)
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print("Depth-First Search (DFS)")
print("-" * 30)

print("\nGraph (adjacency list):")
for node, neighbors in graph.items():
    print(f"  {node} → {neighbors}")

print(f"\nDFS recursive from 'A':  {dfs_recursive(graph, 'A')}")
print(f"DFS iterative from 'A':  {dfs_iterative(graph, 'A')}")

path = find_path_dfs(graph, "A", "F")
print(f"\nPath from A to F: {' → '.join(path) if path else 'No path found'}")

path2 = find_path_dfs(graph, "D", "F")
print(f"Path from D to F: {' → '.join(path2) if path2 else 'No path found'}")

# Disconnected graph to show unreachable nodes
disconnected = {
    "1": ["2"],
    "2": ["1", "3"],
    "3": ["2"],
    "X": ["Y"],
    "Y": ["X"],
}

print(f"\nDisconnected graph — DFS from '1': {dfs_recursive(disconnected, '1')}")
print("(Nodes X, Y are unreachable from 1)")
