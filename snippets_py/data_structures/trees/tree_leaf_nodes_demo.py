# 🧩 Leaf nodes in general tree (recursive)
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


# 🧩 Leaf nodes in binary tree (recursive)
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


# 🧩 Leaf nodes in general tree (iterative, DFS)
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


# 🧩 Edge cases: empty tree, single node
# Function is defined in one of the above code block (find_leaves)


print(find_leaves({}))  # []
print(find_leaves({"A": {}}))  # ['A']
