# Graph Shortest Path

Zero-dependency Python snippets for finding shortest paths in graphs using the standard library.

## Simple

### 🧩 Shortest path (BFS, unweighted graph)

```python
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
```

📂 Find shortest path in unweighted graph using BFS

🏷️ Tags: graph, shortest-path, bfs, unweighted, data-structures
📝 Notes:
- Returns shortest path as list of nodes
- Returns None if no path exists

## Complex

### 🧩 Dijkstra's algorithm (weighted graph)

```python
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
```

📂 Find shortest path in weighted graph using Dijkstra's algorithm

🏷️ Tags: graph, shortest-path, dijkstra, weighted, heapq, data-structures
📝 Notes:
- Returns (cost, path) tuple
- Returns (inf, None) if no path exists

### 🧩 Edge cases: disconnected, not found

```python
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
```

📂 Handle edge cases for shortest path

🏷️ Tags: graph, shortest-path, edge-case, data-structures
📝 Notes:
- Returns None or (inf, None) if no path exists

## 🔗 Cross Reference

- **Reference**: See [📂 Graph Traversal (DFS/BFS)](graph_traversal.md)

## 🏷️ Tags

`graph`, `shortest-path`, `bfs`, `dijkstra`, `weighted`, `unweighted`, `edge-case`, `data-structures`

## 📝 Notes
- Use BFS for unweighted, Dijkstra for weighted graphs
- Dijkstra's algorithm requires non-negative weights
