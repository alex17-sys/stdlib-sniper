# Find All Leaf Nodes

Zero-dependency Python snippets using only the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Leaf nodes in general tree (recursive)

`tree` `leaf` `find` `recursive` `data-structures`

Find all leaf nodes in a general tree

```python
def find_leaves(tree):
    leaves = []
    for node, children in tree.items():
        if not children:
            leaves.append(node)
        else:
            leaves.extend(find_leaves(children))
    return leaves


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print(find_leaves(tree))  # ['B', 'D', 'E']
```

!!! note "Notes"
    - Leaf = node with no children (empty dict)

<hr class="snippet-divider">

### Leaf nodes in binary tree (recursive)

`tree` `binary` `leaf` `find` `recursive` `data-structures`

Find all leaf nodes in a binary tree

```python
def binary_leaves(node):
    if not node:
        return []
    if not node["left"] and not node["right"]:
        return [node["val"]]
    return binary_leaves(node["left"]) + binary_leaves(node["right"])


btree = {
    "val": "A",
    "left": {"val": "B", "left": None, "right": None},
    "right": {
        "val": "C",
        "left": {"val": "D", "left": None, "right": None},
        "right": {"val": "E", "left": None, "right": None},
    },
}
print(binary_leaves(btree))  # ['B', 'D', 'E']
```

!!! note "Notes"
    - Leaf = node with no left or right child

<hr class="snippet-divider">

## Complex

###  Leaf nodes in general tree (iterative, DFS)

`tree` `leaf` `dfs` `iterative` `data-structures`

Iterative DFS to find all leaf nodes

```python
def find_leaves_iterative(tree):
    stack = [tree]
    leaves = []
    while stack:
        current = stack.pop()
        for node, children in current.items():
            if not children:
                leaves.append(node)
            else:
                stack.append(children)
    return leaves


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print(find_leaves_iterative(tree))  # ['B', 'D', 'E']
```

!!! note "Notes"
    - Useful for very deep trees (avoids recursion limit)

<hr class="snippet-divider">

### Edge cases: empty tree, single node

`tree` `leaf` `edge-case` `data-structures`

Handle edge cases for leaf finding

```python
def find_leaves(tree):
    # Function is defined in one of the above code block
    pass


print(find_leaves({}))  # []
print(find_leaves({"A": {}}))  # ['A']
```

!!! note "Notes"
    - No leaves in empty tree, root is leaf if no children

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Tree Traversal (DFS/BFS)](tree_traversal.md)

## 🏷️ Tags

`tree`, `leaf`, `dfs`, `recursive`, `iterative`, `edge-case`, `data-structures`

## 📝 Notes
- Leaf finding is useful for pruning, summarizing, and more
- Use iterative methods for very deep trees
