# 🧩 Pretty-print general tree (nested dict)
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


# 🧩 Pretty-print binary tree (sideways)
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


# 🧩 Print tree with node values/attributes
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


# 🧩 Edge cases: empty tree, single node
def print_tree(tree, indent=0):
    for node, children in tree.items():
        print("  " * indent + str(node))
        print_tree(children, indent + 1)


print_tree({})  # (prints nothing)
print_tree({"A": {}})  # A
