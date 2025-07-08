# 🧩 Preorder DFS (recursive, general tree)
def preorder(tree):
    for node, children in tree.items():
        print(node)
        preorder(children)


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
preorder(tree)
# A B C D E


# 🧩 DFS (iterative, general tree)
def dfs_iterative(tree):
    stack = [tree]
    while stack:
        current = stack.pop()
        for node, children in current.items():
            print(node)
            stack.append(children)


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
dfs_iterative(tree)
# A C E D B (order may vary)


# 🧩 BFS (level-order, general tree)
from collections import deque


def bfs(tree):
    queue = deque([tree])
    while queue:
        current = queue.popleft()
        for node, children in current.items():
            print(node)
            queue.append(children)


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
bfs(tree)
# A B C D E


# 🧩 Preorder, Inorder, Postorder (binary tree, recursive)
def preorder(node):
    if node:
        print(node["val"])
        preorder(node["left"])
        preorder(node["right"])


def inorder(node):
    if node:
        inorder(node["left"])
        print(node["val"])
        inorder(node["right"])


def postorder(node):
    if node:
        postorder(node["left"])
        postorder(node["right"])
        print(node["val"])


# Example binary tree as nested dicts
btree = {
    "val": "A",
    "left": {"val": "B", "left": None, "right": None},
    "right": {
        "val": "C",
        "left": {"val": "D", "left": None, "right": None},
        "right": {"val": "E", "left": None, "right": None},
    },
}

print("Preorder:")
preorder(btree)  # A B C D E
print("Inorder:")
inorder(btree)  # B A D C E
print("Postorder:")
postorder(btree)  # B D E C A


# 🧩 BFS (level-order, binary tree)
from collections import deque


btree = {
    "val": "A",
    "left": {"val": "B", "left": None, "right": None},
    "right": {
        "val": "C",
        "left": {"val": "D", "left": None, "right": None},
        "right": {"val": "E", "left": None, "right": None},
    },
}


def bfs_binary(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            print(node["val"])
            queue.append(node["left"])
            queue.append(node["right"])


bfs_binary(btree)
# A B C D E
