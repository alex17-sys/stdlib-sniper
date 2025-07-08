# 🧩 Topological sort (DFS-based)
def topological_sort_dfs(graph):
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        order.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)
    order.reverse()
    return order


digraph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
print(topological_sort_dfs(digraph))  # ['A', 'C', 'B', 'D'] or similar


# 🧩 Topological sort (Kahn's algorithm, BFS-based)
from collections import deque, defaultdict


def topological_sort_kahn(graph):
    in_degree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    queue = deque([u for u in graph if in_degree[u] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) != len(graph):
        raise ValueError("Graph has a cycle!")
    return order


digraph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
print(topological_sort_kahn(digraph))  # ['A', 'B', 'C', 'D'] or similar


# 🧩 Edge cases: empty graph, single node, cycle
def topological_sort_dfs(graph):
    # Function is defined in one of the above code block
    pass


def topological_sort_kahn(graph):
    # Function is defined in one of the above code block
    pass


print(topological_sort_dfs({}))  # []
print(topological_sort_dfs({"A": []}))  # ['A']
try:
    print(topological_sort_kahn({"A": ["B"], "B": ["A"]}))
except ValueError as e:
    print(e)  # Graph has a cycle!
