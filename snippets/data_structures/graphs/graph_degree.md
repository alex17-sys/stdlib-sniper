# Graph Node Degree

Zero-dependency Python snippets for calculating node degrees in graphs using the standard library.

## Simple

### 🧩 Degree in undirected graph

```python
graph = {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}


def degree(graph, node):
    return len(graph[node])


print(degree(graph, "A"))  # 2
```

📂 Calculate degree of a node in an undirected graph

🏷️ Tags: graph, degree, undirected, data-structures
📝 Notes:
- Degree = number of neighbors

## Complex

### 🧩 In-degree and out-degree in directed graph

```python
digraph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}


def out_degree(graph, node):
    return len(graph[node])


def in_degree(graph, node):
    return sum(node in neighbors for neighbors in graph.values())


print(out_degree(digraph, "A"))  # 2
print(in_degree(digraph, "D"))  # 2
```

📂 Calculate in-degree and out-degree in a directed graph

🏷️ Tags: graph, in-degree, out-degree, directed, data-structures
📝 Notes:
- Out-degree = number of outgoing edges
- In-degree = number of incoming edges

### 🧩 Degree sequence for all nodes

```python
graph = {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}


def degree_sequence(graph):
    return {node: len(neighbors) for node, neighbors in graph.items()}


print(degree_sequence(graph))  # {'A': 2, 'B': 2, 'C': 2, 'D': 2}
```

📂 Get degree of all nodes in undirected graph

🏷️ Tags: graph, degree, sequence, undirected, data-structures
📝 Notes:
- Useful for graph analysis

### 🧩 Edge cases: isolated node, empty graph

```python
def degree(graph, node):
    return len(graph[node])


def degree_sequence(graph):
    return {node: len(neighbors) for node, neighbors in graph.items()}


graph = {"A": set(), "B": {"A"}}
print(degree(graph, "A"))  # 0
print(degree_sequence({}))  # {}
```

📂 Handle edge cases for node degree

🏷️ Tags: graph, degree, edge-case, data-structures
📝 Notes:
- Degree is 0 for isolated node
- Empty graph returns empty dict

## 🔗 Cross Reference

- **Reference**: See [📂 Graph with Adjacency List](graph_adj_list.md)

## 🏷️ Tags

`graph`, `degree`, `in-degree`, `out-degree`, `sequence`, `edge-case`, `data-structures`

## 📝 Notes
- Node degree is fundamental for graph analysis
- In-degree/out-degree only for directed graphs
