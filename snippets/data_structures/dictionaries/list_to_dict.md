# List to Dictionary (Guide)

Zero-dependency Python snippets for converting lists to dictionaries using the standard library.

## Simple

### 🧩 From list of (key, value) tuples

```python
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)
print(d)  # {'a': 1, 'b': 2}
```

📂 Convert list of tuples to dict

🏷️ Tags: list, dict, to-dict, tuple, data-structures
📝 Notes:
- Duplicate keys: last value wins
- All keys must be hashable

### 🧩 From two lists (zip)

```python
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)  # {'a': 1, 'b': 2, 'c': 3}
```

📂 Build dict from zipped lists

🏷️ Tags: list, dict, to-dict, zip, data-structures
📝 Notes:
- If lists are unequal length, extra items are ignored
- Useful for pairing related data

### 🧩 From list with enumerate (index as key)

```python
lst = ["apple", "banana"]
d = dict(enumerate(lst))
print(d)  # {0: 'apple', 1: 'banana'}
```

📂 Use enumerate to build dict from list

🏷️ Tags: list, dict, to-dict, enumerate, data-structures
📝 Notes:
- Index starts at 0 by default
- Useful for mapping positions to values

## Advanced Patterns

### 🧩 From list of keys with default value

```python
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)
print(d)  # {'a': 0, 'b': 0, 'c': 0}
```

📂 Build dict from keys with default value

🏷️ Tags: list, dict, to-dict, fromkeys, default, data-structures
📝 Notes:
- All keys share the same default value object
- Use with immutable defaults to avoid bugs

### 🧩 From list of dicts (merge by key)

```python
lst = [{"a": 1}, {"b": 2}, {"a": 3}]
merged = {}
for d in lst:
    merged.update(d)
print(merged)  # {'a': 3, 'b': 2}
```

📂 Merge list of dicts into one dict

🏷️ Tags: list, dict, to-dict, merge, data-structures
📝 Notes:
- Later dicts overwrite earlier keys
- Useful for combining partial dicts

### 🧩 From list of pairs with duplicate keys (last wins)

```python
pairs = [("a", 1), ("b", 2), ("a", 3)]
d = dict(pairs)
print(d)  # {'a': 3, 'b': 2}
```

📂 Duplicate keys: last value wins

🏷️ Tags: list, dict, to-dict, duplicates, data-structures
📝 Notes:
- Only the last value for each key is kept
- Earlier values are overwritten

### 🧩 From list of pairs with aggregation (sum/count)

```python
from collections import defaultdict

pairs = [("a", 1), ("b", 2), ("a", 3)]
sums = defaultdict(int)
for k, v in pairs:
    sums[k] += v
print(dict(sums))  # {'a': 4, 'b': 2}
```

📂 Aggregate values for duplicate keys

🏷️ Tags: list, dict, to-dict, aggregate, sum, data-structures
📝 Notes:
- Use defaultdict for aggregation
- Useful for counting or summing grouped data

### 🧩 From list of lists (flatten to dict)

```python
lst = [["a", 1], ["b", 2]]
d = dict(lst)
print(d)  # {'a': 1, 'b': 2}
```

📂 Convert list of lists to dict

🏷️ Tags: list, dict, to-dict, flatten, data-structures
📝 Notes:
- Each sublist must have exactly two items
- Raises ValueError if not

### 🧩 From list with transformation (comprehension)

```python
lst = ["apple", "banana"]
d = {x: len(x) for x in lst}
print(d)  # {'apple': 5, 'banana': 6}
```

📂 Build dict from list with transformation

🏷️ Tags: list, dict, to-dict, comprehension, data-structures
📝 Notes:
- Comprehensions allow flexible key/value logic
- Useful for mapping or transforming data

### 🧩 From list of tuples with error handling

```python
lst = [("a", 1), ("b",), ("c", 3)]
d = {}
for item in lst:
    if len(item) == 2:
        k, v = item
        d[k] = v
print(d)  # {'a': 1, 'c': 3}
```

📂 Skip invalid pairs when building dict

🏷️ Tags: list, dict, to-dict, error, data-structures
📝 Notes:
- Skips items that are not valid pairs
- Prevents ValueError from malformed input

## Performance and Edge Cases

### 🧩 Large lists (performance)

```python
import time

N = 10**6
lst = [(x, x * 2) for x in range(N)]
start = time.time()
d = dict(lst)
print("Time:", time.time() - start)
```

📂 Converting large lists to dicts is fast

🏷️ Tags: list, dict, to-dict, performance, data-structures
📝 Notes:
- dict() is efficient for large inputs
- Performance depends on key hashability

### 🧩 Edge cases: empty list, non-hashable keys

```python
print(dict([]))  # {}
try:
    d = dict([([1, 2], "x")])
except TypeError as e:
    print(e)  # unhashable type: 'list'
```

📂 Handle edge cases for list to dict

🏷️ Tags: list, dict, to-dict, edge-case, data-structures
📝 Notes:
- Empty list returns empty dict
- Non-hashable keys raise TypeError

## 🔗 Cross Reference

- **Reference**: See [📂 Dict to List](dict_to_list.md)
- **Reference**: See [📂 Dictionary Comprehension](dict_comprehension.md)

## 🏷️ Tags

`list`, `dict`, `to-dict`, `fromkeys`, `zip`, `enumerate`, `merge`, `aggregate`, `flatten`, `comprehension`, `performance`, `edge-case`, `data-structures`

## 📝 Notes
- dict() is flexible for many list-to-dict patterns
- Use comprehensions for transformation
- Handle duplicates and errors as needed
