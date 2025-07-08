# Merge Dictionaries

Zero-dependency Python snippets for merging multiple dictionaries using the standard library.

## Simple

### 🧩 Merge with update()

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(d1)  # {'a': 1, 'b': 3, 'c': 4}
```

📂 Merge two dicts in-place (right overwrites left)

🏷️ Tags: dict, merge, update, inplace, data-structures
📝 Notes:
- update() modifies the first dict
- Overwrites keys present in both

### 🧩 Merge with dict unpacking (Python 3.5+)

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = {**d1, **d2}
print(merged)  # {'a': 1, 'b': 3, 'c': 4}
```

📂 Merge two or more dicts into a new dict

🏷️ Tags: dict, merge, unpacking, new, data-structures
📝 Notes:
- Later dicts overwrite earlier ones
- Works for any number of dicts: {**d1, **d2, **d3, ...}

### 🧩 Merge with | operator (Python 3.9+)

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1 | d2
print(merged)  # {'a': 1, 'b': 3, 'c': 4}
```

📂 Merge dicts with | (returns new dict)

🏷️ Tags: dict, merge, or, operator, data-structures
📝 Notes:
- d1 | d2 returns a new dict
- d1 |= d2 updates in-place

## Complex

### 🧩 Merge multiple dicts (reduce)

```python
from functools import reduce

dicts = [{"a": 1}, {"b": 2}, {"a": 3}]
merged = reduce(lambda a, b: {**a, **b}, dicts)
print(merged)  # {'a': 3, 'b': 2}
```

📂 Merge a list of dicts (rightmost wins)

🏷️ Tags: dict, merge, multiple, reduce, data-structures
📝 Notes:
- Useful for merging arbitrary number of dicts

### 🧩 Deep merge (recursive)

```python
def deep_merge(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = v
    return result


d1 = {"a": 1, "b": {"x": 10}}
d2 = {"b": {"y": 20}, "c": 3}
print(deep_merge(d1, d2))  # {'a': 1, 'b': {'x': 10, 'y': 20}, 'c': 3}
```

📂 Recursively merge nested dictionaries

🏷️ Tags: dict, merge, deep, recursive, data-structures
📝 Notes:
- Only merges nested dicts, not lists/sets

### 🧩 Conflict resolution (custom merge)

```python
def merge_with_conflict(d1, d2, conflict):
    result = d1.copy()
    for k, v in d2.items():
        if k in result:
            result[k] = conflict(result[k], v)
        else:
            result[k] = v
    return result


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = merge_with_conflict(d1, d2, lambda x, y: x + y)
print(merged)  # {'a': 1, 'b': 5, 'c': 4}
```

📂 Merge dicts with custom conflict resolution

🏷️ Tags: dict, merge, conflict, custom, data-structures
📝 Notes:
- conflict is a function: (old, new) -> result

### 🧩 Edge cases: empty dicts, overlapping keys

```python
print({**{}, **{}})  # {}
print({**{"a": 1}, **{}})  # {'a': 1}
print({**{}, **{"a": 1}})  # {'a': 1}
```

📂 Handle edge cases for merging

🏷️ Tags: dict, merge, edge-case, data-structures
📝 Notes:
- Merging with empty dict returns the other dict

## 🔗 Cross Reference

- **Reference**: See [📂 Invert Key-Value Pairs](invert_dict.md)

## 🏷️ Tags

`dict`, `merge`, `update`, `unpacking`, `or`, `deep`, `conflict`, `edge-case`, `data-structures`

## 📝 Notes
- Use update(), unpacking, or | for shallow merges
- Use recursion for deep merges
