# Nested Dictionary Access (Guide)

Zero-dependency Python snippets for accessing and manipulating nested dictionaries using the standard library.

## Simple

### 🧩 Access nested value (direct)

```python
d = {"a": {"b": {"c": 42}}}
value = d["a"]["b"]["c"]
print(value)  # 42
```

📂 Direct access to nested value

🏷️ Tags: dict, nested, access, data-structures
📝 Notes:
- Direct access will raise KeyError if any key is missing
- Use only when all keys are guaranteed to exist

### 🧩 Safe access with get()

```python
d = {"a": {"b": {"c": 42}}}
value = d.get("a", {}).get("b", {}).get("c")
print(value)  # 42
missing = d.get("a", {}).get("x", {}).get("y")
print(missing)  # {}
```

📂 Safe access to nested value with get()

🏷️ Tags: dict, nested, get, safe, data-structures
📝 Notes:
- Returns default (empty dict or specified) if any key is missing
- Can return unexpected types if structure is not uniform

### 🧩 Set default for nested key (setdefault)

```python
d = {}
d.setdefault("a", {}).setdefault("b", {})["c"] = 42
print(d)  # {'a': {'b': {'c': 42}}}
```

📂 Set default for nested keys

🏷️ Tags: dict, nested, setdefault, default, data-structures
📝 Notes:
- setdefault creates intermediate dicts if missing
- Useful for building nested dicts incrementally

## Advanced Patterns

### 🧩 Deep get (recursive function)

```python
def deep_get(d, keys, default=None):
    for k in keys:
        if isinstance(d, dict):
            d = d.get(k, default)
        else:
            return default
    return d


d = {"a": {"b": {"c": 42}}}
print(deep_get(d, ["a", "b", "c"]))  # 42
print(deep_get(d, ["a", "x", "y"], default="not found"))  # not found
```

📂 Recursively get value from nested dict

🏷️ Tags: dict, nested, deep-get, recursive, data-structures
📝 Notes:
- Handles arbitrary depth
- Returns default if any key is missing or value is not a dict

### 🧩 Deep set (recursive function)

```python
def deep_set(d, keys, value):
    for k in keys[:-1]:
        d = d.setdefault(k, {})
    d[keys[-1]] = value


d = {}
deep_set(d, ["a", "b", "c"], 42)
print(d)  # {'a': {'b': {'c': 42}}}
```

📂 Recursively set value in nested dict

🏷️ Tags: dict, nested, deep-set, recursive, data-structures
📝 Notes:
- Creates intermediate dicts as needed
- Overwrites existing values at the target key

### 🧩 Flatten nested dict (to single-level dict)

```python
def flatten(d, parent_key="", sep="."):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items


d = {"a": {"b": {"c": 42}}, "x": 1}
print(flatten(d))  # {'a.b.c': 42, 'x': 1}
```

📂 Flatten nested dict to single-level dict

🏷️ Tags: dict, nested, flatten, recursive, data-structures
📝 Notes:
- Uses dot notation for keys by default
- Key separator can be customized
- Useful for config or serialization

### 🧩 Update nested dict (deep update)

```python
def deep_update(d, u):
    for k, v in u.items():
        if isinstance(v, dict) and isinstance(d.get(k), dict):
            deep_update(d[k], v)
        else:
            d[k] = v


d = {"a": {"b": 1}}
deep_update(d, {"a": {"c": 2}})
print(d)  # {'a': {'b': 1, 'c': 2}}
```

📂 Recursively update nested dict

🏷️ Tags: dict, nested, update, recursive, data-structures
📝 Notes:
- Updates only matching nested dicts
- Overwrites non-dict values at any level

### 🧩 Delete nested key (safe)

```python
def deep_del(d, keys):
    for k in keys[:-1]:
        d = d.get(k, {})
    d.pop(keys[-1], None)


d = {"a": {"b": {"c": 42}}}
deep_del(d, ["a", "b", "c"])
print(d)  # {'a': {'b': {}}}
```

📂 Safely delete nested key

🏷️ Tags: dict, nested, delete, safe, data-structures
📝 Notes:
- Does nothing if any intermediate key is missing
- No error if key does not exist

### 🧩 Nested dict with defaultdict

```python
from collections import defaultdict


def nested_dict():
    return defaultdict(nested_dict)


d = nested_dict()
d["a"]["b"]["c"] = 42
print(d["a"]["b"]["c"])  # 42
```

📂 Auto-vivifying nested dict with defaultdict

🏷️ Tags: dict, nested, defaultdict, auto, data-structures
📝 Notes:
- Automatically creates nested dicts on access
- Useful for dynamic or unknown-depth structures

## Performance and Edge Cases

### 🧩 Large nested dicts (performance)

```python
import time


def deep_get(d, keys, default=None):
    # Function is defined in one of the above code block
    pass


def deep_set(d, keys, value):
    # Function is defined in one of the above code block
    pass


d = {}
N = 10**4
for i in range(N):
    deep_set(d, ["a", str(i)], i)
start = time.time()
_ = deep_get(d, ["a", str(N - 1)])
print("Time:", time.time() - start)
```

📂 Deep access/set is fast for reasonable depth

🏷️ Tags: dict, nested, performance, data-structures
📝 Notes:
- Performance is good for shallow or moderate depth
- Deeply nested structures may impact speed

### 🧩 Edge cases: missing keys, non-dict values

```python
def deep_get(d, keys, default=None):
    # Function is defined in one of the above code block
    pass


d = {"a": {"b": 1}}
print(deep_get(d, ["a", "x"], default="not found"))  # not found
print(deep_get(d, ["a", "b", "c"], default="not found"))  # not found
```

📂 Handle missing keys and non-dict values

🏷️ Tags: dict, nested, edge-case, data-structures
📝 Notes:
- Returns default if any key is missing or value is not a dict
- Useful for robust code in uncertain data

## 🔗 Cross Reference

- **Reference**: See [📂 Dictionary with Default Values](dict_default.md)
- **Reference**: See [📂 Dictionary Comprehension](dict_comprehension.md)

## 🏷️ Tags

`dict`, `nested`, `get`, `setdefault`, `deep-get`, `deep-set`, `flatten`, `update`, `delete`, `defaultdict`, `performance`, `edge-case`, `data-structures`

## 📝 Notes
- Use get/setdefault for safe access
- Use recursion for deep access, set, update, and flatten
- defaultdict can auto-create nested dicts
