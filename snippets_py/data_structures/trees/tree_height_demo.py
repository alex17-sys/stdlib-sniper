# 🧩 Height of general tree (nested dict, recursive)
def tree_height(tree):
    if not tree:
        return 0
    return 1 + max((tree_height(child) for child in tree.values()), default=0)


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print(tree_height(tree))  # 3


# 🧩 Height of binary tree (recursive)
def binary_height(node):
    if not node:
        return 0
    return 1 + max(binary_height(node["left"]), binary_height(node["right"]))


btree = {
    "val": "A",
    "left": {"val": "B", "left": None, "right": None},
    "right": {
        "val": "C",
        "left": {"val": "D", "left": None, "right": None},
        "right": {"val": "E", "left": None, "right": None},
    },
}
print(binary_height(btree))  # 3


# 🧩 Height of general tree (iterative, BFS)
from collections import deque


def tree_height_bfs(tree):
    if not tree:
        return 0
    max_depth = 0
    queue = deque([(tree, 1)])
    while queue:
        current, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        for child in current.values():
            queue.append((child, depth + 1))
    return max_depth


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print(tree_height_bfs(tree))  # 3


# 🧩 Edge cases: empty tree, single node
# Function is defined in one of the above code block (tree_height)


print(tree_height({}))  # 0
print(tree_height({"A": {}}))  # 1
