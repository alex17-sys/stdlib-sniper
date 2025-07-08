# 🧩 Shortest path (BFS, unweighted graph)
from collections import deque


def shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None


graph = {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}
print(shortest_path(graph, "A", "D"))  # ['A', 'B', 'D'] or ['A', 'C', 'D']


# 🧩 Dijkstra's algorithm (weighted graph)
import heapq


def dijkstra(graph, start, end):
    heap = [(0, start, [start])]
    visited = set()
    while heap:
        cost, node, path = heapq.heappop(heap)
        if node == end:
            return (cost, path)
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor, path + [neighbor]))
    return (float("inf"), None)


# Weighted graph as adjacency list: node -> list of (neighbor, weight)
wgraph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("D", 2)],
    "C": [("A", 4), ("D", 1)],
    "D": [("B", 2), ("C", 1)],
}
print(dijkstra(wgraph, "A", "D"))  # (3, ['A', 'B', 'D']) or (5, ['A', 'C', 'D'])


# 🧩 Edge cases: disconnected, not found
def shortest_path(graph, start, end):
    # Function is defined in one of the above code block
    pass


def dijkstra(graph, start, end):
    # Function is defined in one of the above code block
    pass


graph = {"A": {"B"}, "B": {"A"}, "C": set()}
print(shortest_path(graph, "A", "C"))  # None
wgraph = {"A": [("B", 1)], "B": [("A", 1)], "C": []}
print(dijkstra(wgraph, "A", "C"))  # (inf, None)
