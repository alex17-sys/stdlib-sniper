---
title: Find Path to Node
description: Zero-dependency Python snippets for finding the path from root to a given node in a tree using the standard library.
keywords: binary, data-structures, dfs, edge-case, find, iterative, path, recursive, tree
---

# Find Path to Node

Zero-dependency Python snippets for finding the path from root to a given node in a tree using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Path to node (general tree, recursive)

`tree` `path` `find` `recursive` `data-structures`

Find path from root to a node in a general tree

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

!!! note "Notes"
    - Returns list of nodes from root to target
    - Returns None if not found

<hr class="snippet-divider">

### Path to node (binary tree, recursive)

`tree` `binary` `path` `find` `recursive` `data-structures`

Find path from root to a node in a binary tree

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

!!! note "Notes"
    - Returns list of node values from root to target

<hr class="snippet-divider">

## Complex

###  Path to node (general tree, iterative DFS)

`tree` `path` `dfs` `iterative` `data-structures`

Iterative DFS to find path from root to node

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

!!! note "Notes"
    - Useful for very deep trees (avoids recursion limit)

<hr class="snippet-divider">

### Edge cases: not found, root only

`tree` `path` `edge-case` `data-structures`

Handle edge cases for path finding

```python
def find_path(tree, target, path=None):
    # Function is defined in one of the above code block
    pass


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print(find_path(tree, "Z"))  # None
print(find_path({"A": {}}, "A"))  # ['A']
```

!!! note "Notes"
    - Returns None if not found, root if only node

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Tree Parent Lookup](tree_parent_lookup.md)

## 🏷️ Tags

`tree`, `path`, `dfs`, `recursive`, `iterative`, `edge-case`, `data-structures`

## 📝 Notes
- Path finding is useful for search, ancestry, and more
- Use iterative methods for very deep trees
