# Graph Node Degree

Zero-dependency Python snippets using only the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Degree in undirected graph

`graph` `degree` `undirected` `data-structures`

Calculate degree of a node in an undirected graph

```python
graph = {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}


def degree(graph, node):
    return len(graph[node])


print(degree(graph, "A"))  # 2
```

!!! note "Notes"
    - Degree = number of neighbors

<hr class="snippet-divider">

## Complex

###  In-degree and out-degree in directed graph

`graph` `in-degree` `out-degree` `directed` `data-structures`

Calculate in-degree and out-degree in a directed graph

```python
digraph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}


def out_degree(graph, node):
    return len(graph[node])


def in_degree(graph, node):
    return sum(node in neighbors for neighbors in graph.values())


print(out_degree(digraph, "A"))  # 2
print(in_degree(digraph, "D"))  # 2
```

!!! note "Notes"
    - Out-degree = number of outgoing edges
    - In-degree = number of incoming edges

<hr class="snippet-divider">

### Degree sequence for all nodes

`graph` `degree` `sequence` `undirected` `data-structures`

Get degree of all nodes in undirected graph

```python
graph = {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}


def degree_sequence(graph):
    return {node: len(neighbors) for node, neighbors in graph.items()}


print(degree_sequence(graph))  # {'A': 2, 'B': 2, 'C': 2, 'D': 2}
```

!!! note "Notes"
    - Useful for graph analysis

<hr class="snippet-divider">

### Edge cases: isolated node, empty graph

`graph` `degree` `edge-case` `data-structures`

Handle edge cases for node degree

```python
def degree(graph, node):
    return len(graph[node])


def degree_sequence(graph):
    return {node: len(neighbors) for node, neighbors in graph.items()}


graph = {"A": set(), "B": {"A"}}
print(degree(graph, "A"))  # 0
print(degree_sequence({}))  # {}
```

!!! note "Notes"
    - Degree is 0 for isolated node
    - Empty graph returns empty dict

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Graph with Adjacency List](graph_adj_list.md)

## 🏷️ Tags

`graph`, `degree`, `in-degree`, `out-degree`, `sequence`, `edge-case`, `data-structures`

## 📝 Notes
- Node degree is fundamental for graph analysis
- In-degree/out-degree only for directed graphs
