---
title: Graph Topological Sort
description: Zero-dependency Python snippets for topological sorting of a directed acyclic graph (DAG) using the standard library.
keywords: bfs, dag, data-structures, dfs, directed, edge-case, graph, kahn, topological-sort
---

# Graph Topological Sort

Zero-dependency Python snippets for topological sorting of a directed acyclic graph (DAG) using the standard library.

3 snippets available in this sub-category.

---

## Simple

###  Topological sort (DFS-based)

`graph` `topological-sort` `dfs` `dag` `directed` `data-structures`

Topological sort using DFS (postorder)

```python
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
```

!!! note "Notes"
    - Only valid for DAGs (no cycles)
    - Order may vary if multiple valid sorts

<hr class="snippet-divider">

## Complex

###  Topological sort (Kahn's algorithm, BFS-based)

`graph` `topological-sort` `kahn` `bfs` `dag` `directed` `data-structures`

Topological sort using Kahn's algorithm (BFS)

```python
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
```

!!! note "Notes"
    - Raises ValueError if graph has a cycle
    - Order may vary if multiple valid sorts

<hr class="snippet-divider">

### Edge cases: empty graph, single node, cycle

`graph` `topological-sort` `edge-case` `data-structures`

Handle edge cases for topological sort

```python
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
```

!!! note "Notes"
    - Empty graph returns empty list
    - Cycle raises error in Kahn's algorithm

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Graph Cycle Detection](graph_cycle_detection.md)

## 🏷️ Tags

`graph`, `topological-sort`, `dfs`, `bfs`, `kahn`, `dag`, `edge-case`, `data-structures`

## 📝 Notes
- Topological sort is only valid for DAGs
- Use cycle detection to check for cycles before sorting
