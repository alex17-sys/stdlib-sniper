# Tree Height / Depth

Zero-dependency Python snippets for calculating the height (maximum depth) of a tree using the standard library.

## Simple

### 🧩 Height of general tree (nested dict, recursive)

```python
def tree_height(tree):
    if not tree:
        return 0
    return 1 + max((tree_height(child) for child in tree.values()), default=0)


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print(tree_height(tree))  # 3
```

📂 Calculate height of a general tree (root = 1)

🏷️ Tags: tree, height, depth, recursive, data-structures
📝 Notes:
- Height = number of nodes on longest path from root to leaf
- Returns 0 for empty tree

### 🧩 Height of binary tree (recursive)

```python
def binary_height(node):
    if not node:
        return 0
    return 1 + max(binary_height(node["left"]), binary_height(node["right"]))


btree = {
    "val": "A",
    "left": {"val": "B", "left": None, "right": None},
    "right": {
        "val": "C",
        "left": {"val": "D", "left": None, "right": None},
        "right": {"val": "E", "left": None, "right": None},
    },
}
print(binary_height(btree))  # 3
```

📂 Calculate height of a binary tree

🏷️ Tags: tree, binary, height, depth, recursive, data-structures
📝 Notes:
- Works for any binary tree with dict nodes

## Complex

### 🧩 Height of general tree (iterative, BFS)

```python
from collections import deque


def tree_height_bfs(tree):
    if not tree:
        return 0
    max_depth = 0
    queue = deque([(tree, 1)])
    while queue:
        current, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        for child in current.values():
            queue.append((child, depth + 1))
    return max_depth


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print(tree_height_bfs(tree))  # 3
```

📂 Calculate height using BFS (level-order)

🏷️ Tags: tree, height, bfs, iterative, data-structures
📝 Notes:
- Useful for very deep trees (avoids recursion limit)

### 🧩 Edge cases: empty tree, single node

```python
def tree_height(tree):
    # Function is defined in one of the above code block
    pass


print(tree_height({}))  # 0
print(tree_height({"A": {}}))  # 1
```

📂 Handle edge cases for tree height

🏷️ Tags: tree, height, edge-case, data-structures
📝 Notes:
- Height is 0 for empty, 1 for single node

## 🔗 Cross Reference

- **Reference**: See [📂 Tree Traversal (DFS/BFS)](tree_traversal.md)

## 🏷️ Tags

`tree`, `height`, `depth`, `bfs`, `recursive`, `iterative`, `edge-case`, `data-structures`

## 📝 Notes
- Height is a key property for tree algorithms
- Use BFS for very deep trees to avoid recursion depth issues
