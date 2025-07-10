---
title: Graph with Adjacency List
description: Zero-dependency Python snippets for representing and manipulating graphs using adjacency lists (dict of lists/sets).
keywords: add, adjacency-list, convert, data-structures, directed, edge, edge-list, graph, list, node, remove, set, undirected
---

# Graph with Adjacency List

Zero-dependency Python snippets for representing and manipulating graphs using adjacency lists (dict of lists/sets).

5 snippets available in this sub-category.

---

## Simple

###  Undirected graph with adjacency list (dict of sets)

`graph` `adjacency-list` `undirected` `set` `data-structures`

Represent an undirected graph with adjacency sets

```python
graph = {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}
print(graph)
# {'A': {'B', 'C'}, 'B': {'A', 'D'}, 'C': {'A', 'D'}, 'D': {'B', 'C'}}
```

!!! note "Notes"
    - Each key is a node; value is a set of neighbors
    - Sets avoid duplicate edges

<hr class="snippet-divider">

### Directed graph with adjacency list (dict of lists)

`graph` `adjacency-list` `directed` `list` `data-structures`

Represent a directed graph with adjacency lists

```python
digraph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
print(digraph)
# {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
```

!!! note "Notes"
    - Each key is a node; value is a list of outgoing neighbors

<hr class="snippet-divider">

## Complex

###  Add/remove nodes and edges (undirected)

`graph` `add` `remove` `node` `edge` `undirected` `data-structures`

Add/remove nodes and edges in an undirected graph

```python
def add_node(graph, node):
    if node not in graph:
        graph[node] = set()


def add_edge(graph, u, v):
    add_node(graph, u)
    add_node(graph, v)
    graph[u].add(v)
    graph[v].add(u)


def remove_edge(graph, u, v):
    graph[u].discard(v)
    graph[v].discard(u)


def remove_node(graph, node):
    for neighbor in graph[node]:
        graph[neighbor].discard(node)
    del graph[node]


graph = {}
add_edge(graph, "A", "B")
add_edge(graph, "A", "C")
add_edge(graph, "B", "D")
print(graph)  # {'A': {'B', 'C'}, 'B': {'A', 'D'}, 'C': {'A'}, 'D': {'B'}}
remove_edge(graph, "A", "B")
print(graph)  # {'A': {'C'}, 'B': {'D'}, 'C': {'A'}, 'D': {'B'}}
remove_node(graph, "C")
print(graph)  # {'A': set(), 'B': {'D'}, 'D': {'B'}}
```

!!! note "Notes"
    - discard() avoids KeyError if edge missing

<hr class="snippet-divider">

### Add/remove edges (directed)

`graph` `add` `remove` `edge` `directed` `data-structures`

Add/remove edges in a directed graph

```python
def add_edge_directed(graph, u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)


def remove_edge_directed(graph, u, v):
    if v in graph.get(u, []):
        graph[u].remove(v)


digraph = {}
add_edge_directed(digraph, "A", "B")
add_edge_directed(digraph, "A", "C")
add_edge_directed(digraph, "B", "D")
print(digraph)  # {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
remove_edge_directed(digraph, "A", "B")
print(digraph)  # {'A': ['C'], 'B': ['D'], 'C': [], 'D': []}
```

!!! note "Notes"
    - Handles missing nodes gracefully

<hr class="snippet-divider">

### Convert edge list to adjacency list

`graph` `edge-list` `adjacency-list` `convert` `data-structures`

Convert edge list to adjacency list (directed/undirected)

```python
def edge_list_to_adj_list(edges, directed=False):
    adj = {}
    for u, v in edges:
        if u not in adj:
            adj[u] = set() if not directed else []
        if v not in adj:
            adj[v] = set() if not directed else []
        if directed:
            adj[u].append(v)
        else:
            adj[u].add(v)
            adj[v].add(u)
    return adj


edges = [("A", "B"), ("A", "C"), ("B", "D")]
print(edge_list_to_adj_list(edges))
# {'A': {'B', 'C'}, 'B': {'A', 'D'}, 'C': {'A'}, 'D': {'B'}}
print(edge_list_to_adj_list(edges, directed=True))
# {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
```

!!! note "Notes"
    - Useful for parsing graph data

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Graph Traversal (DFS/BFS)](graph_traversal.md)

## 🏷️ Tags

`graph`, `adjacency-list`, `undirected`, `directed`, `add`, `remove`, `edge-list`, `convert`, `data-structures`

## 📝 Notes
- Adjacency lists are efficient for sparse graphs
- Use sets for undirected, lists for directed graphs
