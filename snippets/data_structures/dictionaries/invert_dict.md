# Invert Key-Value Pairs

Zero-dependency Python snippets for inverting key-value pairs in dictionaries using the standard library.

## Simple

### 🧩 Invert 1:1 dictionary (values unique)

```python
d = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in d.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
```

📂 Invert a dictionary with unique values

🏷️ Tags: dict, invert, 1-to-1, comprehension, data-structures
📝 Notes:
- Only works if values are unique and hashable

### 🧩 Invert with duplicate values (many-to-one)

```python
d = {"a": 1, "b": 2, "c": 1}
inverted = {}
for k, v in d.items():
    inverted[v] = k  # Last key wins
print(inverted)  # {1: 'c', 2: 'b'}
```

📂 Invert with duplicate values (last key wins)

🏷️ Tags: dict, invert, many-to-one, overwrite, data-structures
📝 Notes:
- Only one key per value (last wins)

## Complex

### 🧩 Invert to one-to-many (group keys by value)

```python
d = {"a": 1, "b": 2, "c": 1}
inverted = {}
for k, v in d.items():
    inverted.setdefault(v, []).append(k)
print(inverted)  # {1: ['a', 'c'], 2: ['b']}
```

📂 Invert to group keys by value (one-to-many)

🏷️ Tags: dict, invert, one-to-many, group, data-structures
📝 Notes:
- Values become keys, keys grouped in lists

### 🧩 Invert with defaultdict

```python
from collections import defaultdict

d = {"a": 1, "b": 2, "c": 1}
inverted = defaultdict(list)
for k, v in d.items():
    inverted[v].append(k)
print(dict(inverted))  # {1: ['a', 'c'], 2: ['b']}
```

📂 Use defaultdict for grouping keys by value

🏷️ Tags: dict, invert, defaultdict, group, data-structures
📝 Notes:
- defaultdict simplifies grouping

### 🧩 Invert with non-hashable values (error handling)

```python
d = {"a": [1, 2], "b": [3, 4]}
try:
    inverted = {v: k for k, v in d.items()}
except TypeError as e:
    print(e)  # unhashable type: 'list'
```

📂 Handle non-hashable values when inverting

🏷️ Tags: dict, invert, error, non-hashable, data-structures
📝 Notes:
- Only hashable values can be used as keys

### 🧩 Invert nested dictionary (swap inner keys/values)

```python
d = {"x": {"a": 1, "b": 2}, "y": {"c": 3}}
inverted = {outer: {v: k for k, v in inner.items()} for outer, inner in d.items()}
print(inverted)  # {'x': {1: 'a', 2: 'b'}, 'y': {3: 'c'}}
```

📂 Invert inner dictionaries in a nested dict

🏷️ Tags: dict, invert, nested, comprehension, data-structures
📝 Notes:
- Useful for structured data

### 🧩 Edge cases: empty dict, non-unique values

```python
print({v: k for k, v in {}.items()})  # {}
print({v: k for k, v in {"a": 1, "b": 1}.items()})  # {1: 'b'}
```

📂 Handle edge cases for inverting

🏷️ Tags: dict, invert, edge-case, data-structures
📝 Notes:
- Empty dict inverts to empty
- Duplicate values: last key wins

## 🔗 Cross Reference

- **Reference**: See [📂 Merge Dictionaries](merge_dicts.md)

## 🏷️ Tags

`dict`, `invert`, `group`, `defaultdict`, `nested`, `edge-case`, `data-structures`

## 📝 Notes
- Use grouping for one-to-many inversion
- Only hashable values can be used as keys
