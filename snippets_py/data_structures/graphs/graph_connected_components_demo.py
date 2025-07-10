# 🧩 Connected components with DFS
def connected_components(graph):
    visited = set()
    components = []

    def dfs(node, comp):
        visited.add(node)
        comp.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, comp)

    for node in graph:
        if node not in visited:
            comp = []
            dfs(node, comp)
            components.append(comp)
    return components


graph = {"A": {"B"}, "B": {"A"}, "C": {"D"}, "D": {"C"}, "E": set()}
print(connected_components(graph))  # [['A', 'B'], ['C', 'D'], ['E']]


# 🧩 Connected components with BFS
from collections import deque


def connected_components_bfs(graph):
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            comp = []
            queue = deque([node])
            visited.add(node)
            while queue:
                curr = queue.popleft()
                comp.append(curr)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            components.append(comp)
    return components


graph = {"A": {"B"}, "B": {"A"}, "C": {"D"}, "D": {"C"}, "E": set()}
print(connected_components_bfs(graph))  # [['A', 'B'], ['C', 'D'], ['E']]


# 🧩 Edge cases: empty graph, all isolated nodes
# Function is defined in one of the above code block (connected_components)


print(connected_components({}))  # []
print(connected_components({"A": set(), "B": set()}))  # [['A'], ['B']]
