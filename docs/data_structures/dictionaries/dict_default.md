# Dictionary with Default Values (Guide)

Zero-dependency Python snippets using only the standard library.

11 snippets available in this sub-category.

---

## Simple

###  Using defaultdict for default values

`dict` `defaultdict` `default` `data-structures`

defaultdict provides automatic default values

```python
from collections import defaultdict

d = defaultdict(int)
d["a"] += 1
d["b"] += 2
print(dict(d))  # {'a': 1, 'b': 2}
```

!!! note "Notes"
    - int() gives default 0, list() gives [], set() gives set()
    - No KeyError for missing keys

<hr class="snippet-divider">

### defaultdict with list (grouping)

`dict` `defaultdict` `list` `group` `data-structures`

defaultdict for grouping values

```python
from collections import defaultdict

d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
print(dict(d))  # {'a': [1, 2]}
```

!!! note "Notes"
    - Each key gets its own independent list

<hr class="snippet-divider">

### setdefault for default value

`dict` `setdefault` `default` `data-structures`

setdefault for default value if key missing

```python
d = {}
d.setdefault("a", []).append(1)
print(d)  # {'a': [1]}
```

!!! note "Notes"
    - setdefault only sets value if key is missing

<hr class="snippet-divider">

## Advanced Patterns

###  defaultdict with custom factory

`dict` `defaultdict` `custom` `factory` `data-structures`

Custom default value with factory function

```python
from collections import defaultdict


def zero():
    return 0


d = defaultdict(zero)
d["a"] += 5
print(dict(d))  # {'a': 5}
```

!!! note "Notes"
    - Factory function called for missing keys

<hr class="snippet-divider">

### defaultdict for counting (Counter)

`dict` `counter` `count` `defaultdict` `data-structures`

Counter is a defaultdict(int) for counting

```python
from collections import Counter

lst = ["a", "b", "a"]
c = Counter(lst)
print(dict(c))  # {'a': 2, 'b': 1}
```

!!! note "Notes"
    - Counter is optimized for counting hashable objects

<hr class="snippet-divider">

### Nested defaultdict (auto-vivify)

`dict` `defaultdict` `nested` `auto` `data-structures`

Auto-vivifying nested defaultdict

```python
from collections import defaultdict


def nested():
    return defaultdict(nested)


d = nested()
d["a"]["b"]["c"] = 42
print(d["a"]["b"]["c"])  # 42
```

!!! note "Notes"
    - Allows arbitrary depth of nesting without KeyError

<hr class="snippet-divider">

### Custom dict with __missing__

`dict` `custom` `missing` `default` `data-structures`

Custom dict with __missing__ method

```python
class DefaultDict(dict):
    def __missing__(self, key):
        return 0


d = DefaultDict(a=1)
print(d["a"])  # 1
print(d["b"])  # 0
```

!!! note "Notes"
    - __missing__ is called for missing keys

<hr class="snippet-divider">

### Handle missing keys with get()

`dict` `get` `default` `data-structures`

Use get() for default value if key missing

```python
d = {"a": 1}
print(d.get("b", 0))  # 0
```

!!! note "Notes"
    - get() does not add the key to the dict

<hr class="snippet-divider">

### setdefault vs defaultdict

`dict` `setdefault` `defaultdict` `compare` `data-structures`

setdefault is explicit, defaultdict is automatic

```python
d = {}
d.setdefault("a", []).append(1)
from collections import defaultdict

dd = defaultdict(list)
dd["a"].append(1)
print(d, dict(dd))  # {'a': [1]} {'a': [1]}
```

!!! note "Notes"
    - setdefault only sets on missing; defaultdict always provides default

<hr class="snippet-divider">

## Performance and Edge Cases

###  Large defaultdicts (performance)

`dict` `defaultdict` `performance` `data-structures`

defaultdict is fast for large data

```python
import time
from collections import defaultdict

N = 10**6
d = defaultdict(int)
start = time.time()
for i in range(N):
    d[i] += 1
print("Time:", time.time() - start)
```

!!! note "Notes"
    - defaultdict is efficient for high-volume inserts

<hr class="snippet-divider">

### Edge cases: missing keys, mutable defaults

`dict` `defaultdict` `edge-case` `data-structures`

Each key gets its own default value

```python
from collections import defaultdict

d = defaultdict(list)
d["a"].append(1)
print(d["b"])  # []
# All keys get independent lists
```

!!! note "Notes"
    - Each key gets a new object; no shared mutable default

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Nested Dictionary Access](nested_dict_access.md)
- **Reference**: See [📂 Group by Key](group_by_key.md)

## 🏷️ Tags

`dict`, `defaultdict`, `setdefault`, `default`, `counter`, `custom`, `missing`, `performance`, `edge-case`, `data-structures`

## 📝 Notes
- defaultdict is best for automatic defaults
- setdefault is explicit and works with normal dicts
- Counter is a specialized defaultdict for counting
