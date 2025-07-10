---
title: Dictionary Comprehension Guide
description: Zero-dependency Python snippets for dictionary comprehensions using the standard library.
keywords: basic, collision, comprehension, conditional, data-structures, default, dict, edge-case, enumerate, error, filter, flatten, get, nested, performance, set, transform, try-except, tuple, zip
---

# Dictionary Comprehension Guide

Zero-dependency Python snippets for dictionary comprehensions using the standard library.

16 snippets available in this sub-category.

---

## Simple

###  Basic dictionary comprehension

`dict` `comprehension` `basic` `data-structures`

Create a dict from an iterable

```python
squares = {x: x * x for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

!!! note "Notes"
    - Most concise way to build a dict from an iterable

<hr class="snippet-divider">

### From list of tuples

`dict` `comprehension` `tuple` `data-structures`

Build dict from list of (key, value) tuples

```python
pairs = [("a", 1), ("b", 2)]
d = {k: v for k, v in pairs}
print(d)  # {'a': 1, 'b': 2}
```

!!! note "Notes"
    - Each tuple must have exactly two elements (key, value)

<hr class="snippet-divider">

### From two lists (zip)

`dict` `comprehension` `zip` `data-structures`

Build dict from zipped lists

```python
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)  # {'a': 1, 'b': 2, 'c': 3}
```

!!! note "Notes"
    - Stops at shortest list if lengths differ

<hr class="snippet-divider">

## Filtering and Transforming

###  Filter items by value

`dict` `comprehension` `filter` `data-structures`

Filter dict by value

```python
d = {"a": 1, "b": 2, "c": 3}
even = {k: v for k, v in d.items() if v % 2 == 0}
print(even)  # {'b': 2}
```

!!! note "Notes"
    - Only includes items where value matches condition

<hr class="snippet-divider">

### Transform keys and values

`dict` `comprehension` `transform` `data-structures`

Transform keys and values in comprehension

```python
d = {"a": 1, "b": 2}
transformed = {k.upper(): v * 10 for k, v in d.items()}
print(transformed)  # {'A': 10, 'B': 20}
```

!!! note "Notes"
    - Can change both keys and values in one step

<hr class="snippet-divider">

### Conditional values

`dict` `comprehension` `conditional` `data-structures`

Use conditionals in value expression

```python
nums = [1, 2, 3, 4]
parity = {x: ("even" if x % 2 == 0 else "odd") for x in nums}
print(parity)  # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
```

!!! note "Notes"
    - Ternary operator allows inline if/else for values

<hr class="snippet-divider">

## Advanced Patterns

###  Nested dictionary comprehension

`dict` `comprehension` `nested` `data-structures`

Build nested dicts with comprehensions

```python
matrix = [[1, 2], [3, 4]]
d = {i: {j: val for j, val in enumerate(row)} for i, row in enumerate(matrix)}
print(d)  # {0: {0: 1, 1: 2}, 1: {0: 3, 1: 4}}
```

!!! note "Notes"
    - Useful for matrices or multi-level data

<hr class="snippet-divider">

### Flatten nested dict to single dict

`dict` `comprehension` `flatten` `data-structures`

Flatten nested dicts with comprehension

```python
nested = {"a": {"x": 1}, "b": {"y": 2}}
flat = {f"{k}_{ik}": iv for k, v in nested.items() for ik, iv in v.items()}
print(flat)  # {'a_x': 1, 'b_y': 2}
```

!!! note "Notes"
    - Key names are combined for uniqueness

<hr class="snippet-divider">

### Enumerate with comprehension

`dict` `comprehension` `enumerate` `data-structures`

Use enumerate in dict comprehension

```python
lst = ["apple", "banana"]
d = {i: v for i, v in enumerate(lst)}
print(d)  # {0: 'apple', 1: 'banana'}
```

!!! note "Notes"
    - Indexes become keys

<hr class="snippet-divider">

### Default values with get()

`dict` `comprehension` `default` `get` `data-structures`

Set default value if key missing

```python
keys = ["a", "b", "c"]
source = {"a": 1, "c": 3}
d = {k: source.get(k, 0) for k in keys}
print(d)  # {'a': 1, 'b': 0, 'c': 3}
```

!!! note "Notes"
    - get() provides fallback for missing keys

<hr class="snippet-divider">

### Comprehension with try/except (error handling)

`dict` `comprehension` `error` `try-except` `data-structures`

Handle errors in dict building (not possible in pure comprehension)

```python
lst = ["1", "2", "x"]
d = {}
for s in lst:
    try:
        d[s] = int(s)
    except ValueError:
        d[s] = None
print(d)  # {'1': 1, '2': 2, 'x': None}
```

!!! note "Notes"
    - Use a for loop for error handling (comprehensions can't catch exceptions)

<hr class="snippet-divider">

### Dictionary comprehension from set

`dict` `comprehension` `set` `data-structures`

Build dict from set

```python
s = {"a", "b", "c"}
d = {k: ord(k) for k in s}
print(d)  # {'a': 97, 'b': 98, 'c': 99}
```

!!! note "Notes"
    - Set elements become keys

<hr class="snippet-divider">

### Dictionary comprehension with filtering and transformation

`dict` `comprehension` `filter` `transform` `data-structures`

Combine filtering and transformation

```python
nums = range(10)
squares_even = {x: x * x for x in nums if x % 2 == 0}
print(squares_even)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

!!! note "Notes"
    - Only even numbers included as keys

<hr class="snippet-divider">

## Performance and Idioms

###  Large dict comprehensions (performance)

`dict` `comprehension` `performance` `data-structures`

Dict comprehensions are fast and memory efficient

```python
import time

N = 10**6
start = time.time()
d = {x: x * 2 for x in range(N)}
print("Time:", time.time() - start)
```

!!! note "Notes"
    - Comprehensions are faster than for-loops for building dicts

<hr class="snippet-divider">

### Avoiding key collisions

`dict` `comprehension` `collision` `data-structures`

Last occurrence wins for duplicate keys

```python
lst = ["a", "b", "a"]
d = {k: i for i, k in enumerate(lst)}
print(d)  # {'a': 2, 'b': 1}
```

!!! note "Notes"
    - Later values overwrite earlier ones for duplicate keys

<hr class="snippet-divider">

### Edge cases: empty input, non-hashable keys

`dict` `comprehension` `edge-case` `data-structures`

Handle edge cases for dict comprehensions

```python
print({k: v for k, v in []})  # {}
try:
    d = {[1, 2]: "x" for _ in range(1)}
except TypeError as e:
    print(e)  # unhashable type: 'list'
```

!!! note "Notes"
    - Keys must be hashable; empty input returns empty dict

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Sort Dictionary](sort_dict.md)
- **Reference**: See [📂 Group by Key](group_by_key.md)

## 🏷️ Tags

`dict`, `comprehension`, `filter`, `transform`, `nested`, `flatten`, `enumerate`, `zip`, `default`, `performance`, `edge-case`, `data-structures`

## 📝 Notes
- Dict comprehensions are powerful for building, filtering, and transforming dicts
- Use for-loops for error handling or more complex logic
