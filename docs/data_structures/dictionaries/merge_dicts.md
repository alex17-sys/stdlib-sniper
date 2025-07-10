---
title: Merge Dictionaries
description: Zero-dependency Python snippets for merging multiple dictionaries using the standard library.
keywords: conflict, custom, data-structures, deep, dict, edge-case, inplace, merge, multiple, new, operator, or, recursive, reduce, unpacking, update
---

# Merge Dictionaries

Zero-dependency Python snippets for merging multiple dictionaries using the standard library.

7 snippets available in this sub-category.

---

## Simple

###  Merge with update()

`dict` `merge` `update` `inplace` `data-structures`

Merge two dicts in-place (right overwrites left)

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(d1)  # {'a': 1, 'b': 3, 'c': 4}
```

!!! note "Notes"
    - update() modifies the first dict
    - Overwrites keys present in both

<hr class="snippet-divider">

### Merge with dict unpacking (Python 3.5+)

`dict` `merge` `unpacking` `new` `data-structures`

Merge two or more dicts into a new dict

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = {**d1, **d2}
print(merged)  # {'a': 1, 'b': 3, 'c': 4}
```

!!! note "Notes"
    - Later dicts overwrite earlier ones
    - Works for any number of dicts: {**d1, **d2, **d3, ...}

<hr class="snippet-divider">

### Merge with | operator (Python 3.9+)

`dict` `merge` `or` `operator` `data-structures`

Merge dicts with | (returns new dict)

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1 | d2
print(merged)  # {'a': 1, 'b': 3, 'c': 4}
```

!!! note "Notes"
    - d1 | d2 returns a new dict
    - d1 |= d2 updates in-place

<hr class="snippet-divider">

## Complex

###  Merge multiple dicts (reduce)

`dict` `merge` `multiple` `reduce` `data-structures`

Merge a list of dicts (rightmost wins)

```python
from functools import reduce

dicts = [{"a": 1}, {"b": 2}, {"a": 3}]
merged = reduce(lambda a, b: {**a, **b}, dicts)
print(merged)  # {'a': 3, 'b': 2}
```

!!! note "Notes"
    - Useful for merging arbitrary number of dicts

<hr class="snippet-divider">

### Deep merge (recursive)

`dict` `merge` `deep` `recursive` `data-structures`

Recursively merge nested dictionaries

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

!!! note "Notes"
    - Only merges nested dicts, not lists/sets

<hr class="snippet-divider">

### Conflict resolution (custom merge)

`dict` `merge` `conflict` `custom` `data-structures`

Merge dicts with custom conflict resolution

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

!!! note "Notes"
    - conflict is a function: (old, new) -> result

<hr class="snippet-divider">

### Edge cases: empty dicts, overlapping keys

`dict` `merge` `edge-case` `data-structures`

Handle edge cases for merging

```python
print({**{}, **{}})  # {}
print({**{"a": 1}, **{}})  # {'a': 1}
print({**{}, **{"a": 1}})  # {'a': 1}
```

!!! note "Notes"
    - Merging with empty dict returns the other dict

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Invert Key-Value Pairs](invert_dict.md)

## 🏷️ Tags

`dict`, `merge`, `update`, `unpacking`, `or`, `deep`, `conflict`, `edge-case`, `data-structures`

## 📝 Notes
- Use update(), unpacking, or | for shallow merges
- Use recursion for deep merges
