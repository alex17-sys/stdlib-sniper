# Graph Traversal (DFS/BFS)

Zero-dependency Python snippets for traversing graphs using the standard library.

## Simple

### 🧩 DFS (recursive, undirected graph)

```python
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
```

📂 Depth-First Search (DFS) for undirected graph

🏷️ Tags: graph, dfs, recursive, undirected, data-structures
📝 Notes:
- Uses set for visited nodes
- Order may vary

### 🧩 DFS (iterative, undirected graph)

```python
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
```

📂 Iterative DFS using a stack

🏷️ Tags: graph, dfs, iterative, stack, undirected, data-structures
📝 Notes:
- Order may differ from recursive DFS

### 🧩 BFS (undirected graph)

```python
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
```

📂 Breadth-First Search (BFS) for undirected graph

🏷️ Tags: graph, bfs, queue, undirected, data-structures
📝 Notes:
- Uses deque for efficient queue operations

## Complex

### 🧩 DFS/BFS for directed graph

```python
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
```

📂 DFS and BFS for directed graphs

🏷️ Tags: graph, dfs, bfs, directed, data-structures
📝 Notes:
- Works for any adjacency list

### 🧩 Path finding (DFS, undirected)

```python
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
```

📂 Find a path between two nodes (DFS)

🏷️ Tags: graph, path, dfs, find, undirected, data-structures
📝 Notes:
- Returns first found path, not necessarily shortest

### 🧩 Edge cases: disconnected, not found

```python
def find_path(graph, start, end, path=None):
    # Function is defined in one of the above code block
    pass


def shortest_path(graph, start, end):
    # Function is defined in (another file Shortest path (BFS, unweighted graph) cited below also imported
    pass


from .graph_shortest_path_demo import shortest_path


graph = {"A": {"B"}, "B": {"A"}, "C": set()}
print(find_path(graph, "A", "C"))  # None
print(shortest_path(graph, "A", "C"))  # None
```

📂 Handle disconnected graphs and missing paths

🏷️ Tags: graph, path, edge-case, data-structures
📝 Notes:
- Returns None if no path exists

## 🔗 Cross Reference

- **Reference**: See [📂 Shortest Path Function](graph_shortest_path.md)
- **Reference**: See [📂 Graph with Adjacency List](graph_adj_list.md)
- **Reference**: See [📂 Graph Shortest Path](graph_shortest_path.md)

## 🏷️ Tags

`graph`, `dfs`, `bfs`, `path`, `shortest`, `directed`, `undirected`, `edge-case`, `data-structures`

## 📝 Notes
- Traversal is fundamental for search, connectivity, and more
- Use BFS for shortest path in unweighted graphs
