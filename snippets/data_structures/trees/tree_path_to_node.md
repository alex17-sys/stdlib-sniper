# Find Path to Node

Zero-dependency Python snippets for finding the path from root to a given node in a tree using the standard library.

## Simple

### 🧩 Path to node (general tree, recursive)

```python
def find_path(tree, target, path=None):
    if path is None:
        path = []
    for node, children in tree.items():
        if node == target:
            return path + [node]
        result = find_path(children, target, path + [node])
        if result:
            return result
    return None


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print(find_path(tree, "E"))  # ['A', 'C', 'E']
```

📂 Find path from root to a node in a general tree

🏷️ Tags: tree, path, find, recursive, data-structures
📝 Notes:
- Returns list of nodes from root to target
- Returns None if not found

### 🧩 Path to node (binary tree, recursive)

```python
def find_path_binary(node, target, path=None):
    if path is None:
        path = []
    if not node:
        return None
    if node["val"] == target:
        return path + [node["val"]]
    left = find_path_binary(node["left"], target, path + [node["val"]])
    if left:
        return left
    right = find_path_binary(node["right"], target, path + [node["val"]])
    if right:
        return right
    return None


btree = {
    "val": "A",
    "left": {"val": "B", "left": None, "right": None},
    "right": {
        "val": "C",
        "left": {"val": "D", "left": None, "right": None},
        "right": {"val": "E", "left": None, "right": None},
    },
}
print(find_path_binary(btree, "E"))  # ['A', 'C', 'E']
```

📂 Find path from root to a node in a binary tree

🏷️ Tags: tree, binary, path, find, recursive, data-structures
📝 Notes:
- Returns list of node values from root to target

## Complex

### 🧩 Path to node (general tree, iterative DFS)

```python
def find_path_iterative(tree, target):
    stack = [(tree, [])]
    while stack:
        current, path = stack.pop()
        for node, children in current.items():
            if node == target:
                return path + [node]
            stack.append((children, path + [node]))
    return None


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print(find_path_iterative(tree, "D"))  # ['A', 'C', 'D']
```

📂 Iterative DFS to find path from root to node

🏷️ Tags: tree, path, dfs, iterative, data-structures
📝 Notes:
- Useful for very deep trees (avoids recursion limit)

### 🧩 Edge cases: not found, root only

```python
def find_path(tree, target, path=None):
    # Function is defined in one of the above code block
    pass


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print(find_path(tree, "Z"))  # None
print(find_path({"A": {}}, "A"))  # ['A']
```

📂 Handle edge cases for path finding

🏷️ Tags: tree, path, edge-case, data-structures
📝 Notes:
- Returns None if not found, root if only node

## 🔗 Cross Reference

- **Reference**: See [📂 Tree Parent Lookup](tree_parent_lookup.md)

## 🏷️ Tags

`tree`, `path`, `dfs`, `recursive`, `iterative`, `edge-case`, `data-structures`

## 📝 Notes
- Path finding is useful for search, ancestry, and more
- Use iterative methods for very deep trees
