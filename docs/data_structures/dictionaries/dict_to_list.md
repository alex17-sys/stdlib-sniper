---
title: Convert Dictionary to List (Guide)
description: Zero-dependency Python snippets for converting dictionaries to lists using the standard library.
keywords: data-structures, dict, edge-case, filter, flatten, items, keys, nested, performance, sort, to-list, transform, tuple, unique, values
---

# Convert Dictionary to List (Guide)

Zero-dependency Python snippets for converting dictionaries to lists using the standard library.

11 snippets available in this sub-category.

---

## Simple

###  Get list of keys

`dict` `to-list` `keys` `data-structures`

Convert dict keys to list

```python
d = {"a": 1, "b": 2, "c": 3}
keys = list(d.keys())
print(keys)  # ['a', 'b', 'c']
```

!!! note "Notes"
    - Order matches insertion order (Python 3.7+)
    - Returns empty list for empty dict

<hr class="snippet-divider">

### Get list of values

`dict` `to-list` `values` `data-structures`

Convert dict values to list

```python
d = {"a": 1, "b": 2, "c": 3}
values = list(d.values())
print(values)  # [1, 2, 3]
```

!!! note "Notes"
    - Order matches insertion order
    - Values can be any type

<hr class="snippet-divider">

### Get list of (key, value) tuples

`dict` `to-list` `items` `tuple` `data-structures`

Convert dict items to list of tuples

```python
d = {"a": 1, "b": 2, "c": 3}
items = list(d.items())
print(items)  # [('a', 1), ('b', 2), ('c', 3)]
```

!!! note "Notes"
    - Each tuple is (key, value)
    - Useful for iteration and unpacking

<hr class="snippet-divider">

## Advanced Patterns

###  Flatten nested dict to list of (outer, inner, value)

`dict` `to-list` `flatten` `nested` `data-structures`

Flatten nested dict to list of tuples

```python
nested = {"a": {"x": 1}, "b": {"y": 2}}
flat = [(k, ik, iv) for k, v in nested.items() for ik, iv in v.items()]
print(flat)  # [('a', 'x', 1), ('b', 'y', 2)]
```

!!! note "Notes"
    - Only works for two-level nesting
    - Useful for tabular data

<hr class="snippet-divider">

### List of keys/values/items with filtering

`dict` `to-list` `filter` `data-structures`

Filtered lists from dict

```python
d = {"a": 1, "b": 2, "c": 3}
even_keys = [k for k, v in d.items() if v % 2 == 0]
print(even_keys)  # ['b']

values_gt1 = [v for v in d.values() if v > 1]
print(values_gt1)  # [2, 3]
```

!!! note "Notes"
    - List comprehensions allow flexible filtering
    - Can filter by key or value

<hr class="snippet-divider">

### List of sorted keys/values/items

`dict` `to-list` `sort` `data-structures`

Sorted lists from dict

```python
d = {"b": 2, "a": 1, "c": 3}
sorted_keys = sorted(d)
print(sorted_keys)  # ['a', 'b', 'c']
sorted_items = sorted(d.items(), key=lambda item: item[1])
print(sorted_items)  # [('a', 1), ('b', 2), ('c', 3)]
```

!!! note "Notes"
    - sorted() returns a new list
    - Can sort by key or value

<hr class="snippet-divider">

### List of unique values

`dict` `to-list` `unique` `values` `data-structures`

Get unique values from dict

```python
d = {"a": 1, "b": 2, "c": 1}
unique_values = list(set(d.values()))
print(unique_values)  # [1, 2]
```

!!! note "Notes"
    - set() removes duplicates
    - Order is not preserved

<hr class="snippet-divider">

### List of keys/values/items with transformation

`dict` `to-list` `transform` `data-structures`

Transform keys/values to list

```python
d = {"a": 1, "b": 2}
keys_upper = [k.upper() for k in d]
print(keys_upper)  # ['A', 'B']
values_squared = [v**2 for v in d.values()]
print(values_squared)  # [1, 4]
```

!!! note "Notes"
    - Use comprehensions for transformation
    - Can apply any function to keys or values

<hr class="snippet-divider">

### List of dicts from list of keys/values

`dict` `to-list` `keys` `values` `data-structures`

Build list of single-item dicts

```python
keys = ["a", "b"]
values = [1, 2]
dicts = [{k: v} for k, v in zip(keys, values)]
print(dicts)  # [{'a': 1}, {'b': 2}]
```

!!! note "Notes"
    - Each dict has one key-value pair
    - Useful for splitting data

<hr class="snippet-divider">

## Performance and Edge Cases

###  Large dicts (performance)

`dict` `to-list` `performance` `data-structures`

Converting large dicts to lists is fast

```python
import time

N = 10**6
d = {x: x * 2 for x in range(N)}
start = time.time()
keys = list(d.keys())
print("Time:", time.time() - start)
```

!!! note "Notes"
    - list() is efficient for large dicts
    - Performance depends on dict size

<hr class="snippet-divider">

### Edge cases: empty dict, non-hashable values

`dict` `to-list` `edge-case` `data-structures`

Handle edge cases for dict to list

```python
print(list({}.keys()))  # []
print(list({}.values()))  # []
print(list({}.items()))  # []
```

!!! note "Notes"
    - Empty dict returns empty lists
    - Works for any dict type

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 List to Dictionary](list_to_dict.md)
- **Reference**: See [📂 Dictionary Comprehension](dict_comprehension.md)

## 🏷️ Tags

`dict`, `to-list`, `keys`, `values`, `items`, `flatten`, `filter`, `sort`, `unique`, `transform`, `performance`, `edge-case`, `data-structures`

## 📝 Notes
- Use list() to convert dict views to lists
- List comprehensions allow filtering and transformation
