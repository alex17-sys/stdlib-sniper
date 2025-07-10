# 🧩 Build parent map (general tree)
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


# 🧩 Find parent of a node
# Function is defined in one of the above code block (build_parent_map)


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
parent_map = build_parent_map(tree)


def find_parent(node, parent_map):
    return parent_map.get(node)


print(find_parent("D", parent_map))  # 'C'
print(find_parent("A", parent_map))  # None


# 🧩 Build parent map (binary tree)
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


# 🧩 Find ancestors of a node
# Function is defined in one of the above code block (build_parent_map)


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
