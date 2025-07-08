# Dictionary Comprehension Guide

Zero-dependency Python snippets for dictionary comprehensions using the standard library.

## Simple

### 🧩 Basic dictionary comprehension

```python
squares = {x: x * x for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

📂 Create a dict from an iterable

🏷️ Tags: dict, comprehension, basic, data-structures
📝 Notes:
- Most concise way to build a dict from an iterable

### 🧩 From list of tuples

```python
pairs = [("a", 1), ("b", 2)]
d = {k: v for k, v in pairs}
print(d)  # {'a': 1, 'b': 2}
```

📂 Build dict from list of (key, value) tuples

🏷️ Tags: dict, comprehension, tuple, data-structures
📝 Notes:
- Each tuple must have exactly two elements (key, value)

### 🧩 From two lists (zip)

```python
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)  # {'a': 1, 'b': 2, 'c': 3}
```

📂 Build dict from zipped lists

🏷️ Tags: dict, comprehension, zip, data-structures
📝 Notes:
- Stops at shortest list if lengths differ

## Filtering and Transforming

### 🧩 Filter items by value

```python
d = {"a": 1, "b": 2, "c": 3}
even = {k: v for k, v in d.items() if v % 2 == 0}
print(even)  # {'b': 2}
```

📂 Filter dict by value

🏷️ Tags: dict, comprehension, filter, data-structures
📝 Notes:
- Only includes items where value matches condition

### 🧩 Transform keys and values

```python
d = {"a": 1, "b": 2}
transformed = {k.upper(): v * 10 for k, v in d.items()}
print(transformed)  # {'A': 10, 'B': 20}
```

📂 Transform keys and values in comprehension

🏷️ Tags: dict, comprehension, transform, data-structures
📝 Notes:
- Can change both keys and values in one step

### 🧩 Conditional values

```python
nums = [1, 2, 3, 4]
parity = {x: ("even" if x % 2 == 0 else "odd") for x in nums}
print(parity)  # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
```

📂 Use conditionals in value expression

🏷️ Tags: dict, comprehension, conditional, data-structures
📝 Notes:
- Ternary operator allows inline if/else for values

## Advanced Patterns

### 🧩 Nested dictionary comprehension

```python
matrix = [[1, 2], [3, 4]]
d = {i: {j: val for j, val in enumerate(row)} for i, row in enumerate(matrix)}
print(d)  # {0: {0: 1, 1: 2}, 1: {0: 3, 1: 4}}
```

📂 Build nested dicts with comprehensions

🏷️ Tags: dict, comprehension, nested, data-structures
📝 Notes:
- Useful for matrices or multi-level data

### 🧩 Flatten nested dict to single dict

```python
nested = {"a": {"x": 1}, "b": {"y": 2}}
flat = {f"{k}_{ik}": iv for k, v in nested.items() for ik, iv in v.items()}
print(flat)  # {'a_x': 1, 'b_y': 2}
```

📂 Flatten nested dicts with comprehension

🏷️ Tags: dict, comprehension, flatten, data-structures
📝 Notes:
- Key names are combined for uniqueness

### 🧩 Enumerate with comprehension

```python
lst = ["apple", "banana"]
d = {i: v for i, v in enumerate(lst)}
print(d)  # {0: 'apple', 1: 'banana'}
```

📂 Use enumerate in dict comprehension

🏷️ Tags: dict, comprehension, enumerate, data-structures
📝 Notes:
- Indexes become keys

### 🧩 Default values with get()

```python
keys = ["a", "b", "c"]
source = {"a": 1, "c": 3}
d = {k: source.get(k, 0) for k in keys}
print(d)  # {'a': 1, 'b': 0, 'c': 3}
```

📂 Set default value if key missing

🏷️ Tags: dict, comprehension, default, get, data-structures
📝 Notes:
- get() provides fallback for missing keys

### 🧩 Comprehension with try/except (error handling)

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

📂 Handle errors in dict building (not possible in pure comprehension)

🏷️ Tags: dict, comprehension, error, try-except, data-structures
📝 Notes:
- Use a for loop for error handling (comprehensions can't catch exceptions)

### 🧩 Dictionary comprehension from set

```python
s = {"a", "b", "c"}
d = {k: ord(k) for k in s}
print(d)  # {'a': 97, 'b': 98, 'c': 99}
```

📂 Build dict from set

🏷️ Tags: dict, comprehension, set, data-structures
📝 Notes:
- Set elements become keys

### 🧩 Dictionary comprehension with filtering and transformation

```python
nums = range(10)
squares_even = {x: x * x for x in nums if x % 2 == 0}
print(squares_even)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

📂 Combine filtering and transformation

🏷️ Tags: dict, comprehension, filter, transform, data-structures
📝 Notes:
- Only even numbers included as keys

## Performance and Idioms

### 🧩 Large dict comprehensions (performance)

```python
import time

N = 10**6
start = time.time()
d = {x: x * 2 for x in range(N)}
print("Time:", time.time() - start)
```

📂 Dict comprehensions are fast and memory efficient

🏷️ Tags: dict, comprehension, performance, data-structures
📝 Notes:
- Comprehensions are faster than for-loops for building dicts

### 🧩 Avoiding key collisions

```python
lst = ["a", "b", "a"]
d = {k: i for i, k in enumerate(lst)}
print(d)  # {'a': 2, 'b': 1}
```

📂 Last occurrence wins for duplicate keys

🏷️ Tags: dict, comprehension, collision, data-structures
📝 Notes:
- Later values overwrite earlier ones for duplicate keys

### 🧩 Edge cases: empty input, non-hashable keys

```python
print({k: v for k, v in []})  # {}
try:
    d = {[1, 2]: "x" for _ in range(1)}
except TypeError as e:
    print(e)  # unhashable type: 'list'
```

📂 Handle edge cases for dict comprehensions

🏷️ Tags: dict, comprehension, edge-case, data-structures
📝 Notes:
- Keys must be hashable; empty input returns empty dict

## 🔗 Cross Reference

- **Reference**: See [📂 Sort Dictionary](sort_dict.md)
- **Reference**: See [📂 Group by Key](group_by_key.md)

## 🏷️ Tags

`dict`, `comprehension`, `filter`, `transform`, `nested`, `flatten`, `enumerate`, `zip`, `default`, `performance`, `edge-case`, `data-structures`

## 📝 Notes
- Dict comprehensions are powerful for building, filtering, and transforming dicts
- Use for-loops for error handling or more complex logic
