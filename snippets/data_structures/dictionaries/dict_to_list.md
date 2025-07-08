# Convert Dictionary to List (Guide)

Zero-dependency Python snippets for converting dictionaries to lists using the standard library.

## Simple

### 🧩 Get list of keys

```python
d = {"a": 1, "b": 2, "c": 3}
keys = list(d.keys())
print(keys)  # ['a', 'b', 'c']
```

📂 Convert dict keys to list

🏷️ Tags: dict, to-list, keys, data-structures
📝 Notes:
- Order matches insertion order (Python 3.7+)
- Returns empty list for empty dict

### 🧩 Get list of values

```python
d = {"a": 1, "b": 2, "c": 3}
values = list(d.values())
print(values)  # [1, 2, 3]
```

📂 Convert dict values to list

🏷️ Tags: dict, to-list, values, data-structures
📝 Notes:
- Order matches insertion order
- Values can be any type

### 🧩 Get list of (key, value) tuples

```python
d = {"a": 1, "b": 2, "c": 3}
items = list(d.items())
print(items)  # [('a', 1), ('b', 2), ('c', 3)]
```

📂 Convert dict items to list of tuples

🏷️ Tags: dict, to-list, items, tuple, data-structures
📝 Notes:
- Each tuple is (key, value)
- Useful for iteration and unpacking

## Advanced Patterns

### 🧩 Flatten nested dict to list of (outer, inner, value)

```python
nested = {"a": {"x": 1}, "b": {"y": 2}}
flat = [(k, ik, iv) for k, v in nested.items() for ik, iv in v.items()]
print(flat)  # [('a', 'x', 1), ('b', 'y', 2)]
```

📂 Flatten nested dict to list of tuples

🏷️ Tags: dict, to-list, flatten, nested, data-structures
📝 Notes:
- Only works for two-level nesting
- Useful for tabular data

### 🧩 List of keys/values/items with filtering

```python
d = {"a": 1, "b": 2, "c": 3}
even_keys = [k for k, v in d.items() if v % 2 == 0]
print(even_keys)  # ['b']

values_gt1 = [v for v in d.values() if v > 1]
print(values_gt1)  # [2, 3]
```

📂 Filtered lists from dict

🏷️ Tags: dict, to-list, filter, data-structures
📝 Notes:
- List comprehensions allow flexible filtering
- Can filter by key or value

### 🧩 List of sorted keys/values/items

```python
d = {"b": 2, "a": 1, "c": 3}
sorted_keys = sorted(d)
print(sorted_keys)  # ['a', 'b', 'c']
sorted_items = sorted(d.items(), key=lambda item: item[1])
print(sorted_items)  # [('a', 1), ('b', 2), ('c', 3)]
```

📂 Sorted lists from dict

🏷️ Tags: dict, to-list, sort, data-structures
📝 Notes:
- sorted() returns a new list
- Can sort by key or value

### 🧩 List of unique values

```python
d = {"a": 1, "b": 2, "c": 1}
unique_values = list(set(d.values()))
print(unique_values)  # [1, 2]
```

📂 Get unique values from dict

🏷️ Tags: dict, to-list, unique, values, data-structures
📝 Notes:
- set() removes duplicates
- Order is not preserved

### 🧩 List of keys/values/items with transformation

```python
d = {"a": 1, "b": 2}
keys_upper = [k.upper() for k in d]
print(keys_upper)  # ['A', 'B']
values_squared = [v**2 for v in d.values()]
print(values_squared)  # [1, 4]
```

📂 Transform keys/values to list

🏷️ Tags: dict, to-list, transform, data-structures
📝 Notes:
- Use comprehensions for transformation
- Can apply any function to keys or values

### 🧩 List of dicts from list of keys/values

```python
keys = ["a", "b"]
values = [1, 2]
dicts = [{k: v} for k, v in zip(keys, values)]
print(dicts)  # [{'a': 1}, {'b': 2}]
```

📂 Build list of single-item dicts

🏷️ Tags: dict, to-list, keys, values, data-structures
📝 Notes:
- Each dict has one key-value pair
- Useful for splitting data

## Performance and Edge Cases

### 🧩 Large dicts (performance)

```python
import time

N = 10**6
d = {x: x * 2 for x in range(N)}
start = time.time()
keys = list(d.keys())
print("Time:", time.time() - start)
```

📂 Converting large dicts to lists is fast

🏷️ Tags: dict, to-list, performance, data-structures
📝 Notes:
- list() is efficient for large dicts
- Performance depends on dict size

### 🧩 Edge cases: empty dict, non-hashable values

```python
print(list({}.keys()))  # []
print(list({}.values()))  # []
print(list({}.items()))  # []
```

📂 Handle edge cases for dict to list

🏷️ Tags: dict, to-list, edge-case, data-structures
📝 Notes:
- Empty dict returns empty lists
- Works for any dict type

## 🔗 Cross Reference

- **Reference**: See [📂 List to Dictionary](list_to_dict.md)
- **Reference**: See [📂 Dictionary Comprehension](dict_comprehension.md)

## 🏷️ Tags

`dict`, `to-list`, `keys`, `values`, `items`, `flatten`, `filter`, `sort`, `unique`, `transform`, `performance`, `edge-case`, `data-structures`

## 📝 Notes
- Use list() to convert dict views to lists
- List comprehensions allow filtering and transformation
