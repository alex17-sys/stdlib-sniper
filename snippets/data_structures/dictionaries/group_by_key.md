# Group by Key (Dictionary Grouping Guide)

Zero-dependency Python snippets for grouping items by key using the standard library.

## Simple

### 🧩 Group list of pairs by key (defaultdict)

```python
from collections import defaultdict

pairs = [("a", 1), ("b", 2), ("a", 3)]
groups = defaultdict(list)
for k, v in pairs:
    groups[k].append(v)
print(dict(groups))  # {'a': [1, 3], 'b': [2]}
```

📂 Group values by key using defaultdict

🏷️ Tags: dict, group, defaultdict, pairs, data-structures
📝 Notes:
- defaultdict(list) is the idiomatic way to group

### 🧩 Manual grouping by key

```python
pairs = [("a", 1), ("b", 2), ("a", 3)]
groups = {}
for k, v in pairs:
    if k not in groups:
        groups[k] = []
    groups[k].append(v)
print(groups)  # {'a': [1, 3], 'b': [2]}
```

📂 Group values by key without defaultdict

🏷️ Tags: dict, group, manual, data-structures
📝 Notes:
- Manual approach for grouping if defaultdict is unavailable

## Advanced Patterns

### 🧩 Group by value (invert one-to-many)

```python
from collections import defaultdict


pairs = [("a", 1), ("b", 2), ("c", 1)]
groups = defaultdict(list)
for k, v in pairs:
    groups[v].append(k)
print(dict(groups))  # {1: ['a', 'c'], 2: ['b']}
```

📂 Group keys by value (invert one-to-many)

🏷️ Tags: dict, group, invert, value, data-structures
📝 Notes:
- Useful for inverting mappings (one-to-many)

### 🧩 Group by custom function (e.g., length)

```python
from collections import defaultdict


words = ["apple", "pear", "banana", "fig"]
groups = defaultdict(list)
for word in words:
    groups[len(word)].append(word)
print(dict(groups))  # {5: ['apple'], 4: ['pear'], 6: ['banana'], 3: ['fig']}
```

📂 Group items by custom function of key/value

🏷️ Tags: dict, group, custom, function, data-structures
📝 Notes:
- Grouping can use any function of the item

### 🧩 Group by multiple keys (tuple/grouping)

```python
from collections import defaultdict


records = [
    {"city": "NY", "type": "A", "val": 1},
    {"city": "NY", "type": "B", "val": 2},
    {"city": "LA", "type": "A", "val": 3},
]
groups = defaultdict(list)
for rec in records:
    key = (rec["city"], rec["type"])
    groups[key].append(rec["val"])
print(dict(groups))  # {('NY', 'A'): [1], ('NY', 'B'): [2], ('LA', 'A'): [3]}
```

📂 Group by multiple fields (tuple as key)

🏷️ Tags: dict, group, tuple, multi-key, data-structures
📝 Notes:
- Tuples allow grouping by multiple fields

### 🧩 Group and aggregate (sum, count, min, max)

```python
from collections import defaultdict

pairs = [("a", 1), ("b", 2), ("a", 3)]
sums = defaultdict(int)
for k, v in pairs:
    sums[k] += v
print(dict(sums))  # {'a': 4, 'b': 2}

counts = defaultdict(int)
for k, _ in pairs:
    counts[k] += 1
print(dict(counts))  # {'a': 2, 'b': 1}
```

📂 Group and aggregate values by key

🏷️ Tags: dict, group, aggregate, sum, count, data-structures
📝 Notes:
- Aggregation patterns: sum, count, min, max

### 🧩 Group and flatten (single list of all values)

```python
from collections import defaultdict


pairs = [("a", 1), ("b", 2), ("a", 3)]
groups = defaultdict(list)
for k, v in pairs:
    groups[k].append(v)
flat = [v for group in groups.values() for v in group]
print(flat)  # [1, 3, 2]
```

📂 Flatten grouped values to a single list

🏷️ Tags: dict, group, flatten, data-structures
📝 Notes:
- Flattening combines all grouped values into one list

### 🧩 Group by key with set (unique values)

```python
from collections import defaultdict


pairs = [("a", 1), ("a", 1), ("b", 2)]
groups = defaultdict(set)
for k, v in pairs:
    groups[k].add(v)
print(dict(groups))  # {'a': {1}, 'b': {2}}
```

📂 Group values by key, unique only

🏷️ Tags: dict, group, set, unique, data-structures
📝 Notes:
- set ensures only unique values per key

### 🧩 Group by key with order preserved (OrderedDict)

```python
from collections import OrderedDict

pairs = [("a", 1), ("b", 2), ("a", 3)]
groups = OrderedDict()
for k, v in pairs:
    if k not in groups:
        groups[k] = []
    groups[k].append(v)
print(groups)  # OrderedDict([('a', [1, 3]), ('b', [2])])
```

📂 Group values by key, preserving insertion order

🏷️ Tags: dict, group, order, ordered-dict, data-structures
📝 Notes:
- OrderedDict preserves insertion order of keys

### 🧩 Group by key with itertools.groupby (sorted input)

```python
from itertools import groupby

pairs = [("a", 1), ("a", 2), ("b", 3)]
pairs.sort(key=lambda x: x[0])
groups = {k: [v for _, v in group] for k, group in groupby(pairs, key=lambda x: x[0])}
print(groups)  # {'a': [1, 2], 'b': [3]}
```

📂 Group by key using itertools.groupby (requires sorted input)

🏷️ Tags: dict, group, itertools, groupby, data-structures
📝 Notes:
- groupby requires sorted input by key

## Performance and Edge Cases

### 🧩 Large groupings (performance)

```python
import time
from collections import defaultdict

N = 10**6
pairs = [("a", i) for i in range(N)]
start = time.time()
groups = defaultdict(list)
for k, v in pairs:
    groups[k].append(v)
print("Time:", time.time() - start)
```

📂 defaultdict is fast for large groupings

🏷️ Tags: dict, group, performance, data-structures
📝 Notes:
- defaultdict is efficient for high-volume grouping

### 🧩 Edge cases: empty input, all unique keys

```python
from collections import defaultdict


print(dict(defaultdict(list)))  # {}
pairs = [("a", 1), ("b", 2)]
groups = defaultdict(list)
for k, v in pairs:
    groups[k].append(v)
print(dict(groups))  # {'a': [1], 'b': [2]}
```

📂 Handle edge cases for grouping

🏷️ Tags: dict, group, edge-case, data-structures
📝 Notes:
- Handles empty input and all-unique keys gracefully

## 🔗 Cross Reference

- **Reference**: See [📂 Dictionary Comprehension](dict_comprehension.md)
- **Reference**: See [📂 Invert Key-Value Pairs](invert_dict.md)

## 🏷️ Tags

`dict`, `group`, `defaultdict`, `aggregate`, `custom`, `flatten`, `order`, `itertools`, `edge-case`, `performance`, `data-structures`

## 📝 Notes
- defaultdict is the idiomatic way to group by key
- Use groupby for sorted/grouped data
- Aggregation and flattening are common patterns
