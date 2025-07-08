# Tree with Nested Dictionaries

Zero-dependency Python snippets for representing and manipulating trees using nested dictionaries.

## Simple

### 🧩 Create a tree with nested dicts

```python
tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print(tree)
# {'A': {'B': {}, 'C': {'D': {}, 'E': {}}}}
```

📂 Represent a tree structure with nested dictionaries

🏷️ Tags: tree, dict, nested, data-structures
📝 Notes:
- Each key is a node; value is a dict of children
- Leaves have empty dicts

### 🧩 Add a child node

```python
def add_child(tree, parent, child):
    if parent in tree:
        tree[parent][child] = {}
    else:
        for node in tree.values():
            add_child(node, parent, child)


tree = {"A": {"B": {}, "C": {}}}
add_child(tree, "C", "D")
print(tree)
# {'A': {'B': {}, 'C': {'D': {}}}}
```

📂 Add a child node to a given parent

🏷️ Tags: tree, add, child, dict, data-structures
📝 Notes:
- Recursively searches for parent
- Adds child as empty dict

### 🧩 Remove a node

```python
def remove_node(tree, target):
    keys_to_remove = [k for k in tree if k == target]
    for k in keys_to_remove:
        del tree[k]
    for child in tree.values():
        remove_node(child, target)


tree = {"A": {"B": {}, "C": {"D": {}}}}
remove_node(tree, "C")
print(tree)
# {'A': {'B': {}}}
```

📂 Remove a node (and its subtree) from the tree

🏷️ Tags: tree, remove, node, dict, data-structures
📝 Notes:
- Recursively deletes all matching nodes

## Complex

### 🧩 Traverse all nodes (preorder)

```python
def traverse_preorder(tree):
    for node, children in tree.items():
        print(node)
        traverse_preorder(children)


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
traverse_preorder(tree)
# A B C D E
```

📂 Preorder traversal of all nodes

🏷️ Tags: tree, traverse, preorder, dict, data-structures
📝 Notes:
- Visits node, then children recursively


## 🔗 Cross Reference

- **Reference**: See [📂 Tree Leaf nodes in general tree](tree_leaf_nodes.md)
- **Reference**: See [📂 Tree Traversal (DFS/BFS)](tree_traversal.md)
- **Reference**: See [📂 Pretty-print general tree](tree_traversal.md)

## 🏷️ Tags

`tree`, `dict`, `nested`, `add`, `remove`, `traverse`, `leaf`, `print`, `data-structures`

## 📝 Notes
- Nested dicts are a flexible way to represent trees in Python
- For large or complex trees, consider custom classes or third-party libraries
