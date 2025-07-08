# Graph Connected Components

Zero-dependency Python snippets using only the standard library.

3 snippets available in this sub-category.

---

## Simple

###  Connected components with DFS

`graph` `connected-components` `dfs` `undirected` `data-structures`

Find all connected components using DFS

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

!!! note "Notes"
    - Each component is a list of nodes
    - Handles isolated nodes

<hr class="snippet-divider">

## Complex

###  Connected components with BFS

`graph` `connected-components` `bfs` `undirected` `data-structures`

Find all connected components using BFS

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

!!! note "Notes"
    - BFS is an alternative to DFS for components

<hr class="snippet-divider">

### Edge cases: empty graph, all isolated nodes

`graph` `connected-components` `edge-case` `data-structures`

Handle edge cases for connected components

```python
def connected_components(graph):
    # Function is defined in one of the above code block
    pass


print(connected_components({}))  # []
print(connected_components({"A": set(), "B": set()}))  # [['A'], ['B']]
```

!!! note "Notes"
    - Returns empty list for empty graph
    - Each isolated node is its own component

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Graph Traversal (DFS/BFS)](graph_traversal.md)

## 🏷️ Tags

`graph`, `connected-components`, `dfs`, `bfs`, `undirected`, `edge-case`, `data-structures`

## 📝 Notes
- Connected components are useful for clustering, network analysis, and more
- Use BFS or DFS as needed
