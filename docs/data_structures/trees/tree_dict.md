# Tree with Nested Dictionaries

Zero-dependency Python snippets using only the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Create a tree with nested dicts

`tree` `dict` `nested` `data-structures`

Represent a tree structure with nested dictionaries

```python
tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print(tree)
# {'A': {'B': {}, 'C': {'D': {}, 'E': {}}}}
```

!!! note "Notes"
    - Each key is a node; value is a dict of children
    - Leaves have empty dicts

<hr class="snippet-divider">

### Add a child node

`tree` `add` `child` `dict` `data-structures`

Add a child node to a given parent

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

!!! note "Notes"
    - Recursively searches for parent
    - Adds child as empty dict

<hr class="snippet-divider">

### Remove a node

`tree` `remove` `node` `dict` `data-structures`

Remove a node (and its subtree) from the tree

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

!!! note "Notes"
    - Recursively deletes all matching nodes

<hr class="snippet-divider">

## Complex

###  Traverse all nodes (preorder)

`tree` `traverse` `preorder` `dict` `data-structures`

Preorder traversal of all nodes

```python
def traverse_preorder(tree):
    for node, children in tree.items():
        print(node)
        traverse_preorder(children)


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
traverse_preorder(tree)
# A B C D E
```

!!! note "Notes"
    - Visits node, then children recursively

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Tree Leaf nodes in general tree](tree_leaf_nodes.md)
- **Reference**: See [📂 Tree Traversal (DFS/BFS)](tree_traversal.md)
- **Reference**: See [📂 Pretty-print general tree](tree_traversal.md)

## 🏷️ Tags

`tree`, `dict`, `nested`, `add`, `remove`, `traverse`, `leaf`, `print`, `data-structures`

## 📝 Notes
- Nested dicts are a flexible way to represent trees in Python
- For large or complex trees, consider custom classes or third-party libraries
