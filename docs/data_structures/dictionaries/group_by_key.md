# Group by Key (Dictionary Grouping Guide)

Zero-dependency Python snippets using only the standard library.

12 snippets available in this sub-category.

---

## Simple

###  Group list of pairs by key (defaultdict)

`dict` `group` `defaultdict` `pairs` `data-structures`

Group values by key using defaultdict

```python
from collections import defaultdict

pairs = [("a", 1), ("b", 2), ("a", 3)]
groups = defaultdict(list)
for k, v in pairs:
    groups[k].append(v)
print(dict(groups))  # {'a': [1, 3], 'b': [2]}
```

!!! note "Notes"
    - defaultdict(list) is the idiomatic way to group

<hr class="snippet-divider">

### Manual grouping by key

`dict` `group` `manual` `data-structures`

Group values by key without defaultdict

```python
pairs = [("a", 1), ("b", 2), ("a", 3)]
groups = {}
for k, v in pairs:
    if k not in groups:
        groups[k] = []
    groups[k].append(v)
print(groups)  # {'a': [1, 3], 'b': [2]}
```

!!! note "Notes"
    - Manual approach for grouping if defaultdict is unavailable

<hr class="snippet-divider">

## Advanced Patterns

###  Group by value (invert one-to-many)

`dict` `group` `invert` `value` `data-structures`

Group keys by value (invert one-to-many)

```python
from collections import defaultdict


pairs = [("a", 1), ("b", 2), ("c", 1)]
groups = defaultdict(list)
for k, v in pairs:
    groups[v].append(k)
print(dict(groups))  # {1: ['a', 'c'], 2: ['b']}
```

!!! note "Notes"
    - Useful for inverting mappings (one-to-many)

<hr class="snippet-divider">

### Group by custom function (e.g., length)

`dict` `group` `custom` `function` `data-structures`

Group items by custom function of key/value

```python
from collections import defaultdict


words = ["apple", "pear", "banana", "fig"]
groups = defaultdict(list)
for word in words:
    groups[len(word)].append(word)
print(dict(groups))  # {5: ['apple'], 4: ['pear'], 6: ['banana'], 3: ['fig']}
```

!!! note "Notes"
    - Grouping can use any function of the item

<hr class="snippet-divider">

### Group by multiple keys (tuple/grouping)

`dict` `group` `tuple` `multi-key` `data-structures`

Group by multiple fields (tuple as key)

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

!!! note "Notes"
    - Tuples allow grouping by multiple fields

<hr class="snippet-divider">

### Group and aggregate (sum, count, min, max)

`dict` `group` `aggregate` `sum` `count` `data-structures`

Group and aggregate values by key

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

!!! note "Notes"
    - Aggregation patterns: sum, count, min, max

<hr class="snippet-divider">

### Group and flatten (single list of all values)

`dict` `group` `flatten` `data-structures`

Flatten grouped values to a single list

```python
from collections import defaultdict


pairs = [("a", 1), ("b", 2), ("a", 3)]
groups = defaultdict(list)
for k, v in pairs:
    groups[k].append(v)
flat = [v for group in groups.values() for v in group]
print(flat)  # [1, 3, 2]
```

!!! note "Notes"
    - Flattening combines all grouped values into one list

<hr class="snippet-divider">

### Group by key with set (unique values)

`dict` `group` `set` `unique` `data-structures`

Group values by key, unique only

```python
from collections import defaultdict


pairs = [("a", 1), ("a", 1), ("b", 2)]
groups = defaultdict(set)
for k, v in pairs:
    groups[k].add(v)
print(dict(groups))  # {'a': {1}, 'b': {2}}
```

!!! note "Notes"
    - set ensures only unique values per key

<hr class="snippet-divider">

### Group by key with order preserved (OrderedDict)

`dict` `group` `order` `ordered-dict` `data-structures`

Group values by key, preserving insertion order

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

!!! note "Notes"
    - OrderedDict preserves insertion order of keys

<hr class="snippet-divider">

### Group by key with itertools.groupby (sorted input)

`dict` `group` `itertools` `groupby` `data-structures`

Group by key using itertools.groupby (requires sorted input)

```python
from itertools import groupby

pairs = [("a", 1), ("a", 2), ("b", 3)]
pairs.sort(key=lambda x: x[0])
groups = {k: [v for _, v in group] for k, group in groupby(pairs, key=lambda x: x[0])}
print(groups)  # {'a': [1, 2], 'b': [3]}
```

!!! note "Notes"
    - groupby requires sorted input by key

<hr class="snippet-divider">

## Performance and Edge Cases

###  Large groupings (performance)

`dict` `group` `performance` `data-structures`

defaultdict is fast for large groupings

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

!!! note "Notes"
    - defaultdict is efficient for high-volume grouping

<hr class="snippet-divider">

### Edge cases: empty input, all unique keys

`dict` `group` `edge-case` `data-structures`

Handle edge cases for grouping

```python
from collections import defaultdict


print(dict(defaultdict(list)))  # {}
pairs = [("a", 1), ("b", 2)]
groups = defaultdict(list)
for k, v in pairs:
    groups[k].append(v)
print(dict(groups))  # {'a': [1], 'b': [2]}
```

!!! note "Notes"
    - Handles empty input and all-unique keys gracefully

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Dictionary Comprehension](dict_comprehension.md)
- **Reference**: See [📂 Invert Key-Value Pairs](invert_dict.md)

## 🏷️ Tags

`dict`, `group`, `defaultdict`, `aggregate`, `custom`, `flatten`, `order`, `itertools`, `edge-case`, `performance`, `data-structures`

## 📝 Notes
- defaultdict is the idiomatic way to group by key
- Use groupby for sorted/grouped data
- Aggregation and flattening are common patterns
