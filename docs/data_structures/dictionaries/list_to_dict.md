# List to Dictionary (Guide)

Zero-dependency Python snippets using only the standard library.

12 snippets available in this sub-category.

---

## Simple

###  From list of (key, value) tuples

`list` `dict` `to-dict` `tuple` `data-structures`

Convert list of tuples to dict

```python
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)
print(d)  # {'a': 1, 'b': 2}
```

!!! note "Notes"
    - Duplicate keys: last value wins
    - All keys must be hashable

<hr class="snippet-divider">

### From two lists (zip)

`list` `dict` `to-dict` `zip` `data-structures`

Build dict from zipped lists

```python
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)  # {'a': 1, 'b': 2, 'c': 3}
```

!!! note "Notes"
    - If lists are unequal length, extra items are ignored
    - Useful for pairing related data

<hr class="snippet-divider">

### From list with enumerate (index as key)

`list` `dict` `to-dict` `enumerate` `data-structures`

Use enumerate to build dict from list

```python
lst = ["apple", "banana"]
d = dict(enumerate(lst))
print(d)  # {0: 'apple', 1: 'banana'}
```

!!! note "Notes"
    - Index starts at 0 by default
    - Useful for mapping positions to values

<hr class="snippet-divider">

## Advanced Patterns

###  From list of keys with default value

`list` `dict` `to-dict` `fromkeys` `default` `data-structures`

Build dict from keys with default value

```python
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)
print(d)  # {'a': 0, 'b': 0, 'c': 0}
```

!!! note "Notes"
    - All keys share the same default value object
    - Use with immutable defaults to avoid bugs

<hr class="snippet-divider">

### From list of dicts (merge by key)

`list` `dict` `to-dict` `merge` `data-structures`

Merge list of dicts into one dict

```python
lst = [{"a": 1}, {"b": 2}, {"a": 3}]
merged = {}
for d in lst:
    merged.update(d)
print(merged)  # {'a': 3, 'b': 2}
```

!!! note "Notes"
    - Later dicts overwrite earlier keys
    - Useful for combining partial dicts

<hr class="snippet-divider">

### From list of pairs with duplicate keys (last wins)

`list` `dict` `to-dict` `duplicates` `data-structures`

Duplicate keys: last value wins

```python
pairs = [("a", 1), ("b", 2), ("a", 3)]
d = dict(pairs)
print(d)  # {'a': 3, 'b': 2}
```

!!! note "Notes"
    - Only the last value for each key is kept
    - Earlier values are overwritten

<hr class="snippet-divider">

### From list of pairs with aggregation (sum/count)

`list` `dict` `to-dict` `aggregate` `sum` `data-structures`

Aggregate values for duplicate keys

```python
from collections import defaultdict

pairs = [("a", 1), ("b", 2), ("a", 3)]
sums = defaultdict(int)
for k, v in pairs:
    sums[k] += v
print(dict(sums))  # {'a': 4, 'b': 2}
```

!!! note "Notes"
    - Use defaultdict for aggregation
    - Useful for counting or summing grouped data

<hr class="snippet-divider">

### From list of lists (flatten to dict)

`list` `dict` `to-dict` `flatten` `data-structures`

Convert list of lists to dict

```python
lst = [["a", 1], ["b", 2]]
d = dict(lst)
print(d)  # {'a': 1, 'b': 2}
```

!!! note "Notes"
    - Each sublist must have exactly two items
    - Raises ValueError if not

<hr class="snippet-divider">

### From list with transformation (comprehension)

`list` `dict` `to-dict` `comprehension` `data-structures`

Build dict from list with transformation

```python
lst = ["apple", "banana"]
d = {x: len(x) for x in lst}
print(d)  # {'apple': 5, 'banana': 6}
```

!!! note "Notes"
    - Comprehensions allow flexible key/value logic
    - Useful for mapping or transforming data

<hr class="snippet-divider">

### From list of tuples with error handling

`list` `dict` `to-dict` `error` `data-structures`

Skip invalid pairs when building dict

```python
lst = [("a", 1), ("b",), ("c", 3)]
d = {}
for item in lst:
    if len(item) == 2:
        k, v = item
        d[k] = v
print(d)  # {'a': 1, 'c': 3}
```

!!! note "Notes"
    - Skips items that are not valid pairs
    - Prevents ValueError from malformed input

<hr class="snippet-divider">

## Performance and Edge Cases

###  Large lists (performance)

`list` `dict` `to-dict` `performance` `data-structures`

Converting large lists to dicts is fast

```python
import time

N = 10**6
lst = [(x, x * 2) for x in range(N)]
start = time.time()
d = dict(lst)
print("Time:", time.time() - start)
```

!!! note "Notes"
    - dict() is efficient for large inputs
    - Performance depends on key hashability

<hr class="snippet-divider">

### Edge cases: empty list, non-hashable keys

`list` `dict` `to-dict` `edge-case` `data-structures`

Handle edge cases for list to dict

```python
print(dict([]))  # {}
try:
    d = dict([([1, 2], "x")])
except TypeError as e:
    print(e)  # unhashable type: 'list'
```

!!! note "Notes"
    - Empty list returns empty dict
    - Non-hashable keys raise TypeError

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Dict to List](dict_to_list.md)
- **Reference**: See [📂 Dictionary Comprehension](dict_comprehension.md)

## 🏷️ Tags

`list`, `dict`, `to-dict`, `fromkeys`, `zip`, `enumerate`, `merge`, `aggregate`, `flatten`, `comprehension`, `performance`, `edge-case`, `data-structures`

## 📝 Notes
- dict() is flexible for many list-to-dict patterns
- Use comprehensions for transformation
- Handle duplicates and errors as needed
