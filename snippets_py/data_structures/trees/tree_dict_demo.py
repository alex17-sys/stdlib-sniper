# 🧩 Create a tree with nested dicts
tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
print(tree)
# {'A': {'B': {}, 'C': {'D': {}, 'E': {}}}}


# 🧩 Add a child node
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


# 🧩 Remove a node
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


# 🧩 Traverse all nodes (preorder)
def traverse_preorder(tree):
    for node, children in tree.items():
        print(node)
        traverse_preorder(children)


tree = {"A": {"B": {}, "C": {"D": {}, "E": {}}}}
traverse_preorder(tree)
# A B C D E
