# Tree Parent Lookup

Zero-dependency Python snippets for storing and looking up parent pointers in a tree using the standard library.

## Simple

### 🧩 Build parent map (general tree)

```python
def build_parent_map(tree, parent=None, parent_map=None):
    if parent_map is None:
        parent_map = {}
    for node, children in tree.items():
        parent_map[node] = parent
        build_parent_map(children, node, parent_map)
    return parent_map


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
parent_map = build_parent_map(tree)
print(parent_map)  # {'A': None, 'B': 'A', 'C': 'A', 'D': 'C', 'E': 'C'}
```

📂 Map each node to its parent in a general tree

🏷️ Tags: tree, parent, map, lookup, data-structures
📝 Notes:
- Root's parent is None
- Useful for path finding, ancestor queries

### 🧩 Find parent of a node

```python
def build_parent_map(tree, parent=None, parent_map=None):
    # Function is defined in one of the above code block
    pass


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
parent_map = build_parent_map(tree)


def find_parent(node, parent_map):
    return parent_map.get(node)


print(find_parent("D", parent_map))  # 'C'
print(find_parent("A", parent_map))  # None
```

📂 Lookup parent of a node using parent map

🏷️ Tags: tree, parent, lookup, data-structures
📝 Notes:
- Returns None if node is root or not found

## Complex

### 🧩 Build parent map (binary tree)

```python
def build_parent_map_binary(node, parent=None, parent_map=None):
    if parent_map is None:
        parent_map = {}
    if node:
        parent_map[node["val"]] = parent
        build_parent_map_binary(node["left"], node["val"], parent_map)
        build_parent_map_binary(node["right"], node["val"], parent_map)
    return parent_map


btree = {
    "val": "A",
    "left": {"val": "B", "left": None, "right": None},
    "right": {
        "val": "C",
        "left": {"val": "D", "left": None, "right": None},
        "right": {"val": "E", "left": None, "right": None},
    },
}
parent_map = build_parent_map_binary(btree)
print(parent_map)  # {'A': None, 'B': 'A', 'C': 'A', 'D': 'C', 'E': 'C'}
```

📂 Map each node to its parent in a binary tree

🏷️ Tags: tree, binary, parent, map, data-structures
📝 Notes:
- Works for any binary tree with dict nodes

### 🧩 Find ancestors of a node

```python
def build_parent_map(tree, parent=None, parent_map=None):
    # Function is defined in one of the above code block
    pass


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
parent_map = build_parent_map(tree)
def find_ancestors(node, parent_map):
    ancestors = []
    while node is not None:
        node = parent_map.get(node)
        if node:
            ancestors.append(node)
    return ancestors


print(find_ancestors("E", parent_map))  # ['C', 'A']
```

📂 Find all ancestors of a node using parent map

🏷️ Tags: tree, ancestor, parent, map, data-structures
📝 Notes:
- Returns list from parent up to root

## 🔗 Cross Reference

- **Reference**: See [📂 Find Path to Node](tree_path_to_node.md)

## 🏷️ Tags

`tree`, `parent`, `ancestor`, `map`, `lookup`, `binary`, `data-structures`

## 📝 Notes
- Parent maps are useful for path finding, LCA, and more
- Can be built in a single traversal
