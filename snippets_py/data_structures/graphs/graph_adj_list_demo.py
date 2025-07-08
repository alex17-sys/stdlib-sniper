# 🧩 Undirected graph with adjacency list (dict of sets)
graph = {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}
print(graph)
# {'A': {'B', 'C'}, 'B': {'A', 'D'}, 'C': {'A', 'D'}, 'D': {'B', 'C'}}


# 🧩 Directed graph with adjacency list (dict of lists)
digraph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
print(digraph)
# {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}


# 🧩 Add/remove nodes and edges (undirected)
def add_node(graph, node):
    if node not in graph:
        graph[node] = set()


def add_edge(graph, u, v):
    add_node(graph, u)
    add_node(graph, v)
    graph[u].add(v)
    graph[v].add(u)


def remove_edge(graph, u, v):
    graph[u].discard(v)
    graph[v].discard(u)


def remove_node(graph, node):
    for neighbor in graph[node]:
        graph[neighbor].discard(node)
    del graph[node]


graph = {}
add_edge(graph, "A", "B")
add_edge(graph, "A", "C")
add_edge(graph, "B", "D")
print(graph)  # {'A': {'B', 'C'}, 'B': {'A', 'D'}, 'C': {'A'}, 'D': {'B'}}
remove_edge(graph, "A", "B")
print(graph)  # {'A': {'C'}, 'B': {'D'}, 'C': {'A'}, 'D': {'B'}}
remove_node(graph, "C")
print(graph)  # {'A': set(), 'B': {'D'}, 'D': {'B'}}


# 🧩 Add/remove edges (directed)
def add_edge_directed(graph, u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)


def remove_edge_directed(graph, u, v):
    if v in graph.get(u, []):
        graph[u].remove(v)


digraph = {}
add_edge_directed(digraph, "A", "B")
add_edge_directed(digraph, "A", "C")
add_edge_directed(digraph, "B", "D")
print(digraph)  # {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
remove_edge_directed(digraph, "A", "B")
print(digraph)  # {'A': ['C'], 'B': ['D'], 'C': [], 'D': []}


# 🧩 Convert edge list to adjacency list
def edge_list_to_adj_list(edges, directed=False):
    adj = {}
    for u, v in edges:
        if u not in adj:
            adj[u] = set() if not directed else []
        if v not in adj:
            adj[v] = set() if not directed else []
        if directed:
            adj[u].append(v)
        else:
            adj[u].add(v)
            adj[v].add(u)
    return adj


edges = [("A", "B"), ("A", "C"), ("B", "D")]
print(edge_list_to_adj_list(edges))
# {'A': {'B', 'C'}, 'B': {'A', 'D'}, 'C': {'A'}, 'D': {'B'}}
print(edge_list_to_adj_list(edges, directed=True))
# {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
