# Tree Traversal (DFS/BFS)

Zero-dependency Python snippets for traversing trees using the standard library.

## Simple

### 🧩 Preorder DFS (recursive, general tree)

```python
def preorder(tree):
    for node, children in tree.items():
        print(node)
        preorder(children)


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
preorder(tree)
# A B C D E
```

📂 Preorder traversal: visit node, then children

🏷️ Tags: tree, dfs, preorder, recursive, data-structures
📝 Notes:
- Works for any tree with nested dicts

### 🧩 DFS (iterative, general tree)

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

📂 Iterative DFS using a stack

🏷️ Tags: tree, dfs, iterative, stack, data-structures
📝 Notes:
- Order may differ from recursive DFS

### 🧩 BFS (level-order, general tree)

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

📂 Breadth-First Search (level-order traversal)

🏷️ Tags: tree, bfs, queue, level-order, data-structures
📝 Notes:
- Uses deque for efficient queue operations

## Complex

### 🧩 Preorder, Inorder, Postorder (binary tree, recursive)

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

📂 Standard traversals for binary trees

🏷️ Tags: tree, binary, preorder, inorder, postorder, recursive, data-structures
📝 Notes:
- Each traversal visits nodes in a different order
- Works for any binary tree with dict nodes

### 🧩 BFS (level-order, binary tree)

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

📂 Level-order traversal for binary trees

🏷️ Tags: tree, binary, bfs, level-order, data-structures
📝 Notes:
- Handles None children gracefully


## 🔗 Cross Reference

- **Reference**: See [📂 Path to node (general tree, recursive)](tree_path_to_node.md)
- **Reference**: See [📂 Tree Parent Lookup](tree_parent_lookup.md)
- **Reference**: See [📂 Tree with Nested Dictionaries](tree_dict.md)

## 🏷️ Tags

`tree`, `dfs`, `bfs`, `preorder`, `inorder`, `postorder`, `path`, `binary`, `data-structures`

## 📝 Notes
- Traversal order matters for algorithms (search, printing, etc.)
- Use recursive or iterative methods as needed
