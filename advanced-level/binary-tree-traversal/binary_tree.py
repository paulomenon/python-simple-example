# Binary Tree Traversal
# Builds a binary search tree and demonstrates in-order, pre-order,
# post-order, and level-order (BFS) traversals.

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the BST."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def in_order(self, node=None, result=None):
        """Left → Root → Right (returns sorted order for BST)."""
        if result is None:
            result = []
            node = self.root

        if node:
            self.in_order(node.left, result)
            result.append(node.value)
            self.in_order(node.right, result)

        return result

    def pre_order(self, node=None, result=None):
        """Root → Left → Right (useful for copying/serializing a tree)."""
        if result is None:
            result = []
            node = self.root

        if node:
            result.append(node.value)
            self.pre_order(node.left, result)
            self.pre_order(node.right, result)

        return result

    def post_order(self, node=None, result=None):
        """Left → Right → Root (useful for deletion/cleanup)."""
        if result is None:
            result = []
            node = self.root

        if node:
            self.post_order(node.left, result)
            self.post_order(node.right, result)
            result.append(node.value)

        return result

    def level_order(self):
        """BFS level-by-level traversal."""
        if self.root is None:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            result.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def height(self, node=None):
        """Calculate the height of the tree."""
        if node is None:
            node = self.root
        if node is None:
            return 0

        left_h = self.height(node.left) if node.left else 0
        right_h = self.height(node.right) if node.right else 0
        return 1 + max(left_h, right_h)

    def display(self, node=None, prefix="", is_left=True):
        """Print the tree structure visually."""
        if node is None:
            node = self.root
        if node is None:
            print("  (empty tree)")
            return

        if node.right:
            self.display(node.right, prefix + ("│   " if is_left else "    "), False)

        connector = "└── " if is_left else "┌── "
        print(f"  {prefix}{connector}{node.value}")

        if node.left:
            self.display(node.left, prefix + ("    " if is_left else "│   "), True)


print("Binary Tree Traversal")
print("-" * 30)

bst = BinarySearchTree()
values = [50, 30, 70, 20, 40, 60, 80, 10, 35]
print(f"\nInserting: {values}")
for v in values:
    bst.insert(v)

print("\nTree structure:")
bst.display()

print(f"\nIn-order   (sorted): {bst.in_order()}")
print(f"Pre-order  (root first): {bst.pre_order()}")
print(f"Post-order (root last):  {bst.post_order()}")
print(f"Level-order (BFS):       {bst.level_order()}")
print(f"\nTree height: {bst.height()}")
