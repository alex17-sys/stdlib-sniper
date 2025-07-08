# Graph Cycle Detection

Zero-dependency Python snippets using only the standard library.

3 snippets available in this sub-category.

---

## Simple

###  Cycle detection in undirected graph (DFS)

`graph` `cycle` `dfs` `undirected` `data-structures`

Detect cycles in undirected graphs using DFS

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

!!! note "Notes"
    - Checks for back edges (neighbor not parent)

<hr class="snippet-divider">

## Complex

###  Cycle detection in directed graph (DFS, recursion stack)

`graph` `cycle` `dfs` `directed` `data-structures`

Detect cycles in directed graphs using DFS and recursion stack

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

!!! note "Notes"
    - Uses recursion stack to detect back edges

<hr class="snippet-divider">

### Edge cases: empty graph, isolated nodes

`graph` `cycle` `edge-case` `data-structures`

Handle edge cases for cycle detection

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

!!! note "Notes"
    - No cycles in empty or all-isolated graphs

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Graph Traversal (DFS/BFS)](graph_traversal.md)
- **Reference**: See [📂 Graph Connected Components](graph_connected_components.md)

## 🏷️ Tags

`graph`, `cycle`, `dfs`, `undirected`, `directed`, `edge-case`, `data-structures`

## 📝 Notes
- Cycle detection is key for many algorithms (DAGs, topological sort, etc.)
- Use recursion stack for directed graphs
