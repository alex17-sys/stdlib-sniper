---
title: Tree Traversal (DFS/BFS)
description: Zero-dependency Python snippets for traversing trees using the standard library.
keywords: bfs, binary, data-structures, dfs, inorder, iterative, level-order, postorder, preorder, queue, recursive, stack, tree
---

# Tree Traversal (DFS/BFS)

Zero-dependency Python snippets for traversing trees using the standard library.

5 snippets available in this sub-category.

---

## Simple

###  Preorder DFS (recursive, general tree)

`tree` `dfs` `preorder` `recursive` `data-structures`

Preorder traversal: visit node, then children

```python
def preorder(tree):
    for node, children in tree.items():
        print(node)
        preorder(children)


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
preorder(tree)
# A B C D E
```

!!! note "Notes"
    - Works for any tree with nested dicts

<hr class="snippet-divider">

### DFS (iterative, general tree)

`tree` `dfs` `iterative` `stack` `data-structures`

Iterative DFS using a stack

```python
def dfs_iterative(tree):
    stack = [tree]
    while stack:
        current = stack.pop()
        for node, children in current.items():
            print(node)
            stack.append(children)


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
dfs_iterative(tree)
# A C E D B (order may vary)
```

!!! note "Notes"
    - Order may differ from recursive DFS

<hr class="snippet-divider">

### BFS (level-order, general tree)

`tree` `bfs` `queue` `level-order` `data-structures`

Breadth-First Search (level-order traversal)

```python
from collections import deque


def bfs(tree):
    queue = deque([tree])
    while queue:
        current = queue.popleft()
        for node, children in current.items():
            print(node)
            queue.append(children)


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
bfs(tree)
# A B C D E
```

!!! note "Notes"
    - Uses deque for efficient queue operations

<hr class="snippet-divider">

## Complex

###  Preorder, Inorder, Postorder (binary tree, recursive)

`tree` `binary` `preorder` `inorder` `postorder` `recursive` `data-structures`

Standard traversals for binary trees

```python
def preorder(node):
    if node:
        print(node["val"])
        preorder(node["left"])
        preorder(node["right"])


def inorder(node):
    if node:
        inorder(node["left"])
        print(node["val"])
        inorder(node["right"])


def postorder(node):
    if node:
        postorder(node["left"])
        postorder(node["right"])
        print(node["val"])


# Example binary tree as nested dicts
btree = {
    "val": "A",
    "left": {"val": "B", "left": None, "right": None},
    "right": {
        "val": "C",
        "left": {"val": "D", "left": None, "right": None},
        "right": {"val": "E", "left": None, "right": None},
    },
}

print("Preorder:")
preorder(btree)  # A B C D E
print("Inorder:")
inorder(btree)  # B A D C E
print("Postorder:")
postorder(btree)  # B D E C A
```

!!! note "Notes"
    - Each traversal visits nodes in a different order
    - Works for any binary tree with dict nodes

<hr class="snippet-divider">

### BFS (level-order, binary tree)

`tree` `binary` `bfs` `level-order` `data-structures`

Level-order traversal for binary trees

```python
from collections import deque


btree = {
    "val": "A",
    "left": {"val": "B", "left": None, "right": None},
    "right": {
        "val": "C",
        "left": {"val": "D", "left": None, "right": None},
        "right": {"val": "E", "left": None, "right": None},
    },
}


def bfs_binary(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            print(node["val"])
            queue.append(node["left"])
            queue.append(node["right"])


bfs_binary(btree)
# A B C D E
```

!!! note "Notes"
    - Handles None children gracefully

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Path to node (general tree, recursive)](tree_path_to_node.md)
- **Reference**: See [📂 Tree Parent Lookup](tree_parent_lookup.md)
- **Reference**: See [📂 Tree with Nested Dictionaries](tree_dict.md)

## 🏷️ Tags

`tree`, `dfs`, `bfs`, `preorder`, `inorder`, `postorder`, `path`, `binary`, `data-structures`

## 📝 Notes
- Traversal order matters for algorithms (search, printing, etc.)
- Use recursive or iterative methods as needed
