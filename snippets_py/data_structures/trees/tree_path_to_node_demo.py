# 🧩 Path to node (general tree, recursive)
def find_path(tree, target, path=None):
    if path is None:
        path = []
    for node, children in tree.items():
        if node == target:
            return path + [node]
        result = find_path(children, target, path + [node])
        if result:
            return result
    return None


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print(find_path(tree, "E"))  # ['A', 'C', 'E']


# 🧩 Path to node (binary tree, recursive)
def find_path_binary(node, target, path=None):
    if path is None:
        path = []
    if not node:
        return None
    if node["val"] == target:
        return path + [node["val"]]
    left = find_path_binary(node["left"], target, path + [node["val"]])
    if left:
        return left
    right = find_path_binary(node["right"], target, path + [node["val"]])
    if right:
        return right
    return None


btree = {
    "val": "A",
    "left": {"val": "B", "left": None, "right": None},
    "right": {
        "val": "C",
        "left": {"val": "D", "left": None, "right": None},
        "right": {"val": "E", "left": None, "right": None},
    },
}
print(find_path_binary(btree, "E"))  # ['A', 'C', 'E']


# 🧩 Path to node (general tree, iterative DFS)
def find_path_iterative(tree, target):
    stack = [(tree, [])]
    while stack:
        current, path = stack.pop()
        for node, children in current.items():
            if node == target:
                return path + [node]
            stack.append((children, path + [node]))
    return None


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print(find_path_iterative(tree, "D"))  # ['A', 'C', 'D']


# 🧩 Edge cases: not found, root only
# Function is defined in one of the above code block (find_path)


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print(find_path(tree, "Z"))  # None
print(find_path({"A": {}}, "A"))  # ['A']
