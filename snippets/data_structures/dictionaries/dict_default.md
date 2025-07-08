# Dictionary with Default Values (Guide)

Zero-dependency Python snippets for dictionaries with default values using the standard library.

## Simple

### 🧩 Using defaultdict for default values

```python
from collections import defaultdict

d = defaultdict(int)
d["a"] += 1
d["b"] += 2
print(dict(d))  # {'a': 1, 'b': 2}
```

📂 defaultdict provides automatic default values

🏷️ Tags: dict, defaultdict, default, data-structures
📝 Notes:
- int() gives default 0, list() gives [], set() gives set()
- No KeyError for missing keys

### 🧩 defaultdict with list (grouping)

```python
from collections import defaultdict

d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
print(dict(d))  # {'a': [1, 2]}
```

📂 defaultdict for grouping values

🏷️ Tags: dict, defaultdict, list, group, data-structures
📝 Notes:
- Each key gets its own independent list

### 🧩 setdefault for default value

```python
d = {}
d.setdefault("a", []).append(1)
print(d)  # {'a': [1]}
```

📂 setdefault for default value if key missing

🏷️ Tags: dict, setdefault, default, data-structures
📝 Notes:
- setdefault only sets value if key is missing

## Advanced Patterns

### 🧩 defaultdict with custom factory

```python
from collections import defaultdict


def zero():
    return 0


d = defaultdict(zero)
d["a"] += 5
print(dict(d))  # {'a': 5}
```

📂 Custom default value with factory function

🏷️ Tags: dict, defaultdict, custom, factory, data-structures
📝 Notes:
- Factory function called for missing keys

### 🧩 defaultdict for counting (Counter)

```python
from collections import Counter

lst = ["a", "b", "a"]
c = Counter(lst)
print(dict(c))  # {'a': 2, 'b': 1}
```

📂 Counter is a defaultdict(int) for counting

🏷️ Tags: dict, counter, count, defaultdict, data-structures
📝 Notes:
- Counter is optimized for counting hashable objects

### 🧩 Nested defaultdict (auto-vivify)

```python
from collections import defaultdict


def nested():
    return defaultdict(nested)


d = nested()
d["a"]["b"]["c"] = 42
print(d["a"]["b"]["c"])  # 42
```

📂 Auto-vivifying nested defaultdict

🏷️ Tags: dict, defaultdict, nested, auto, data-structures
📝 Notes:
- Allows arbitrary depth of nesting without KeyError

### 🧩 Custom dict with __missing__

```python
class DefaultDict(dict):
    def __missing__(self, key):
        return 0


d = DefaultDict(a=1)
print(d["a"])  # 1
print(d["b"])  # 0
```

📂 Custom dict with __missing__ method

🏷️ Tags: dict, custom, missing, default, data-structures
📝 Notes:
- __missing__ is called for missing keys

### 🧩 Handle missing keys with get()

```python
d = {"a": 1}
print(d.get("b", 0))  # 0
```

📂 Use get() for default value if key missing

🏷️ Tags: dict, get, default, data-structures
📝 Notes:
- get() does not add the key to the dict

### 🧩 setdefault vs defaultdict

```python
d = {}
d.setdefault("a", []).append(1)
from collections import defaultdict

dd = defaultdict(list)
dd["a"].append(1)
print(d, dict(dd))  # {'a': [1]} {'a': [1]}
```

📂 setdefault is explicit, defaultdict is automatic

🏷️ Tags: dict, setdefault, defaultdict, compare, data-structures
📝 Notes:
- setdefault only sets on missing; defaultdict always provides default

## Performance and Edge Cases

### 🧩 Large defaultdicts (performance)

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

📂 defaultdict is fast for large data

🏷️ Tags: dict, defaultdict, performance, data-structures
📝 Notes:
- defaultdict is efficient for high-volume inserts

### 🧩 Edge cases: missing keys, mutable defaults

```python
from collections import defaultdict

d = defaultdict(list)
d["a"].append(1)
print(d["b"])  # []
# All keys get independent lists
```

📂 Each key gets its own default value

🏷️ Tags: dict, defaultdict, edge-case, data-structures
📝 Notes:
- Each key gets a new object; no shared mutable default

## 🔗 Cross Reference

- **Reference**: See [📂 Nested Dictionary Access](nested_dict_access.md)
- **Reference**: See [📂 Group by Key](group_by_key.md)

## 🏷️ Tags

`dict`, `defaultdict`, `setdefault`, `default`, `counter`, `custom`, `missing`, `performance`, `edge-case`, `data-structures`

## 📝 Notes
- defaultdict is best for automatic defaults
- setdefault is explicit and works with normal dicts
- Counter is a specialized defaultdict for counting
