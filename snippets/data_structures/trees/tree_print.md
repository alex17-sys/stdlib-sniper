# Pretty-Print Tree Structure

Zero-dependency Python snippets for pretty-printing tree structures using the standard library.

## Simple

### 🧩 Pretty-print general tree (nested dict)

```python
def print_tree(tree, indent=0):
    for node, children in tree.items():
        print("  " * indent + str(node))
        print_tree(children, indent + 1)


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print_tree(tree)
# A
#   B
#   C
#     D
#     E
```

📂 Print general tree with indentation for levels

🏷️ Tags: tree, print, pretty, indent, data-structures
📝 Notes:
- Indentation shows depth/level
- Works for any nested dict tree

### 🧩 Pretty-print binary tree (sideways)

```python
def print_binary_tree(node, indent=0):
    if node:
        print_binary_tree(node["right"], indent + 4)
        print(" " * indent + str(node["val"]))
        print_binary_tree(node["left"], indent + 4)


btree = {
    "val": "A",
    "left": {"val": "B", "left": None, "right": None},
    "right": {
        "val": "C",
        "left": {"val": "D", "left": None, "right": None},
        "right": {"val": "E", "left": None, "right": None},
    },
}
print_binary_tree(btree)
#     E
#   C
#     D
# A
#   B
```

📂 Print binary tree sideways (root at left)

🏷️ Tags: tree, binary, print, pretty, data-structures
📝 Notes:
- Right subtree printed above, left below
- Indentation shows depth

## Complex

### 🧩 Print tree with node values/attributes

```python
def print_tree_with_values(tree, values, indent=0):
    for node, children in tree.items():
        val = values.get(node, "")
        print("  " * indent + f"{node} ({val})")
        print_tree_with_values(children, values, indent + 1)


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
values = {"A": 10, "B": 5, "C": 7, "D": 2, "E": 3}
print_tree_with_values(tree, values)
# A (10)
#   B (5)
#   C (7)
#     D (2)
#     E (3)
```

📂 Print tree with custom node values/attributes

🏷️ Tags: tree, print, value, attribute, data-structures
📝 Notes:
- Useful for trees with extra data per node

### 🧩 Edge cases: empty tree, single node

```python
def print_tree(tree, indent=0):
    for node, children in tree.items():
        print("  " * indent + str(node))
        print_tree(children, indent + 1)


print_tree({})  # (prints nothing)
print_tree({"A": {}})  # A
```

📂 Handle edge cases for pretty-printing

🏷️ Tags: tree, print, edge-case, data-structures
📝 Notes:
- Prints nothing for empty tree, root for single node

## 🔗 Cross Reference

- **Reference**: See [📂 Tree with Nested Dictionaries](tree_dict.md)

## 🏷️ Tags

`tree`, `print`, `pretty`, `indent`, `value`, `attribute`, `binary`, `data-structures`

## 📝 Notes
- Pretty-printing helps visualize and debug trees
- Customize for your tree structure and data
