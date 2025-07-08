# 🧩 Degree in undirected graph
graph = {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}


def degree(graph, node):
    return len(graph[node])


print(degree(graph, "A"))  # 2


# 🧩 In-degree and out-degree in directed graph
digraph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}


def out_degree(graph, node):
    return len(graph[node])


def in_degree(graph, node):
    return sum(node in neighbors for neighbors in graph.values())


print(out_degree(digraph, "A"))  # 2
print(in_degree(digraph, "D"))  # 2


# 🧩 Degree sequence for all nodes
graph = {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}


def degree_sequence(graph):
    return {node: len(neighbors) for node, neighbors in graph.items()}


print(degree_sequence(graph))  # {'A': 2, 'B': 2, 'C': 2, 'D': 2}


# 🧩 Edge cases: isolated node, empty graph
def degree(graph, node):
    return len(graph[node])


def degree_sequence(graph):
    return {node: len(neighbors) for node, neighbors in graph.items()}


graph = {"A": set(), "B": {"A"}}
print(degree(graph, "A"))  # 0
print(degree_sequence({}))  # {}
