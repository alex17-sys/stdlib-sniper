# 🧩 DFS (recursive, undirected graph)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}
dfs(graph, "A")
# A B D C


# 🧩 DFS (iterative, undirected graph)
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)
            stack.extend(graph[node] - visited)


graph = {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}
dfs_iterative(graph, "A")
# A C D B (order may vary)


# 🧩 BFS (undirected graph)
from collections import deque


def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


graph = {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}
bfs(graph, "A")
# A B C D


# 🧩 DFS/BFS for directed graph
digraph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}


def dfs_directed(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_directed(graph, neighbor, visited)


def bfs_directed(graph, start):
    from collections import deque

    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


dfs_directed(digraph, "A")  # A B D C
bfs_directed(digraph, "A")  # A B C D


# 🧩 Path finding (DFS, undirected)
def find_path(graph, start, end, path=None):
    if path is None:
        path = [start]
    if start == end:
        return path
    for neighbor in graph[start]:
        if neighbor not in path:
            result = find_path(graph, neighbor, end, path + [neighbor])
            if result:
                return result
    return None


graph = {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}
print(find_path(graph, "A", "D"))  # ['A', 'B', 'D'] or ['A', 'C', 'D']


# 🧩 Edge cases: disconnected, not found
def find_path(graph, start, end, path=None):
    # Function is defined in one of the above code block
    pass


def shortest_path(graph, start, end):
    # Function is defined in (another file Shortest path (BFS, unweighted graph) cited below
    pass


graph = {"A": {"B"}, "B": {"A"}, "C": set()}
print(find_path(graph, "A", "C"))  # None
print(shortest_path(graph, "A", "C"))  # None
