# Graph Connected Components

Zero-dependency Python snippets for finding all connected components in an undirected graph using the standard library.

## Simple

### 🧩 Connected components with DFS

```python
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
```

📂 Find all connected components using DFS

🏷️ Tags: graph, connected-components, dfs, undirected, data-structures
📝 Notes:
- Each component is a list of nodes
- Handles isolated nodes

## Complex

### 🧩 Connected components with BFS

```python
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
```

📂 Find all connected components using BFS

🏷️ Tags: graph, connected-components, bfs, undirected, data-structures
📝 Notes:
- BFS is an alternative to DFS for components

### 🧩 Edge cases: empty graph, all isolated nodes

```python
def connected_components(graph):
    # Function is defined in one of the above code block
    pass


print(connected_components({}))  # []
print(connected_components({"A": set(), "B": set()}))  # [['A'], ['B']]
```

📂 Handle edge cases for connected components

🏷️ Tags: graph, connected-components, edge-case, data-structures
📝 Notes:
- Returns empty list for empty graph
- Each isolated node is its own component

## 🔗 Cross Reference

- **Reference**: See [📂 Graph Traversal (DFS/BFS)](graph_traversal.md)

## 🏷️ Tags

`graph`, `connected-components`, `dfs`, `bfs`, `undirected`, `edge-case`, `data-structures`

## 📝 Notes
- Connected components are useful for clustering, network analysis, and more
- Use BFS or DFS as needed
