# Invert Key-Value Pairs

Zero-dependency Python snippets using only the standard library.

7 snippets available in this sub-category.

---

## Simple

###  Invert 1:1 dictionary (values unique)

`dict` `invert` `1-to-1` `comprehension` `data-structures`

Invert a dictionary with unique values

```python
d = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in d.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
```

!!! note "Notes"
    - Only works if values are unique and hashable

<hr class="snippet-divider">

### Invert with duplicate values (many-to-one)

`dict` `invert` `many-to-one` `overwrite` `data-structures`

Invert with duplicate values (last key wins)

```python
d = {"a": 1, "b": 2, "c": 1}
inverted = {}
for k, v in d.items():
    inverted[v] = k  # Last key wins
print(inverted)  # {1: 'c', 2: 'b'}
```

!!! note "Notes"
    - Only one key per value (last wins)

<hr class="snippet-divider">

## Complex

###  Invert to one-to-many (group keys by value)

`dict` `invert` `one-to-many` `group` `data-structures`

Invert to group keys by value (one-to-many)

```python
d = {"a": 1, "b": 2, "c": 1}
inverted = {}
for k, v in d.items():
    inverted.setdefault(v, []).append(k)
print(inverted)  # {1: ['a', 'c'], 2: ['b']}
```

!!! note "Notes"
    - Values become keys, keys grouped in lists

<hr class="snippet-divider">

### Invert with defaultdict

`dict` `invert` `defaultdict` `group` `data-structures`

Use defaultdict for grouping keys by value

```python
from collections import defaultdict

d = {"a": 1, "b": 2, "c": 1}
inverted = defaultdict(list)
for k, v in d.items():
    inverted[v].append(k)
print(dict(inverted))  # {1: ['a', 'c'], 2: ['b']}
```

!!! note "Notes"
    - defaultdict simplifies grouping

<hr class="snippet-divider">

### Invert with non-hashable values (error handling)

`dict` `invert` `error` `non-hashable` `data-structures`

Handle non-hashable values when inverting

```python
d = {"a": [1, 2], "b": [3, 4]}
try:
    inverted = {v: k for k, v in d.items()}
except TypeError as e:
    print(e)  # unhashable type: 'list'
```

!!! note "Notes"
    - Only hashable values can be used as keys

<hr class="snippet-divider">

### Invert nested dictionary (swap inner keys/values)

`dict` `invert` `nested` `comprehension` `data-structures`

Invert inner dictionaries in a nested dict

```python
d = {"x": {"a": 1, "b": 2}, "y": {"c": 3}}
inverted = {outer: {v: k for k, v in inner.items()} for outer, inner in d.items()}
print(inverted)  # {'x': {1: 'a', 2: 'b'}, 'y': {3: 'c'}}
```

!!! note "Notes"
    - Useful for structured data

<hr class="snippet-divider">

### Edge cases: empty dict, non-unique values

`dict` `invert` `edge-case` `data-structures`

Handle edge cases for inverting

```python
print({v: k for k, v in {}.items()})  # {}
print({v: k for k, v in {"a": 1, "b": 1}.items()})  # {1: 'b'}
```

!!! note "Notes"
    - Empty dict inverts to empty
    - Duplicate values: last key wins

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Merge Dictionaries](merge_dicts.md)

## 🏷️ Tags

`dict`, `invert`, `group`, `defaultdict`, `nested`, `edge-case`, `data-structures`

## 📝 Notes
- Use grouping for one-to-many inversion
- Only hashable values can be used as keys
