# Graph Cycle Detection

Zero-dependency Python snippets for detecting cycles in graphs using the standard library.

## Simple

### 🧩 Cycle detection in undirected graph (DFS)

```python
def has_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False


graph = {"A": {"B"}, "B": {"A", "C"}, "C": {"B", "D"}, "D": {"C", "A"}}
print(has_cycle_undirected(graph))  # True

graph2 = {"A": {"B"}, "B": {"A", "C"}, "C": {"B"}, "D": set()}
print(has_cycle_undirected(graph2))  # False
```

📂 Detect cycles in undirected graphs using DFS

🏷️ Tags: graph, cycle, dfs, undirected, data-structures
📝 Notes:
- Checks for back edges (neighbor not parent)

## Complex

### 🧩 Cycle detection in directed graph (DFS, recursion stack)

```python
def has_cycle_directed(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False


digraph = {"A": ["B"], "B": ["C"], "C": ["A"], "D": []}
print(has_cycle_directed(digraph))  # True

digraph2 = {"A": ["B"], "B": ["C"], "C": [], "D": []}
print(has_cycle_directed(digraph2))  # False
```

📂 Detect cycles in directed graphs using DFS and recursion stack

🏷️ Tags: graph, cycle, dfs, directed, data-structures
📝 Notes:
- Uses recursion stack to detect back edges

### 🧩 Edge cases: empty graph, isolated nodes

```python
def has_cycle_undirected(graph):
    # Function is defined in one of the above code block
    pass


def has_cycle_directed(graph):
    # Function is defined in one of the above code block
    pass


print(has_cycle_undirected({}))  # False
print(has_cycle_directed({"A": [], "B": []}))  # False
```

📂 Handle edge cases for cycle detection

🏷️ Tags: graph, cycle, edge-case, data-structures
📝 Notes:
- No cycles in empty or all-isolated graphs

## 🔗 Cross Reference

- **Reference**: See [📂 Graph Traversal (DFS/BFS)](graph_traversal.md)
- **Reference**: See [📂 Graph Connected Components](graph_connected_components.md)

## 🏷️ Tags

`graph`, `cycle`, `dfs`, `undirected`, `directed`, `edge-case`, `data-structures`

## 📝 Notes
- Cycle detection is key for many algorithms (DAGs, topological sort, etc.)
- Use recursion stack for directed graphs
