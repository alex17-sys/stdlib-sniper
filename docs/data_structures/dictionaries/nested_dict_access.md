---
title: Nested Dictionary Access (Guide)
description: Zero-dependency Python snippets for accessing and manipulating nested dictionaries using the standard library.
keywords: access, auto, data-structures, deep-get, deep-set, default, defaultdict, delete, dict, edge-case, flatten, get, nested, performance, recursive, safe, setdefault, update
---

# Nested Dictionary Access (Guide)

Zero-dependency Python snippets for accessing and manipulating nested dictionaries using the standard library.

11 snippets available in this sub-category.

---

## Simple

###  Access nested value (direct)

`dict` `nested` `access` `data-structures`

Direct access to nested value

```python
d = {"a": {"b": {"c": 42}}}
value = d["a"]["b"]["c"]
print(value)  # 42
```

!!! note "Notes"
    - Direct access will raise KeyError if any key is missing
    - Use only when all keys are guaranteed to exist

<hr class="snippet-divider">

### Safe access with get()

`dict` `nested` `get` `safe` `data-structures`

Safe access to nested value with get()

```python
d = {"a": {"b": {"c": 42}}}
value = d.get("a", {}).get("b", {}).get("c")
print(value)  # 42
missing = d.get("a", {}).get("x", {}).get("y")
print(missing)  # {}
```

!!! note "Notes"
    - Returns default (empty dict or specified) if any key is missing
    - Can return unexpected types if structure is not uniform

<hr class="snippet-divider">

### Set default for nested key (setdefault)

`dict` `nested` `setdefault` `default` `data-structures`

Set default for nested keys

```python
d = {}
d.setdefault("a", {}).setdefault("b", {})["c"] = 42
print(d)  # {'a': {'b': {'c': 42}}}
```

!!! note "Notes"
    - setdefault creates intermediate dicts if missing
    - Useful for building nested dicts incrementally

<hr class="snippet-divider">

## Advanced Patterns

###  Deep get (recursive function)

`dict` `nested` `deep-get` `recursive` `data-structures`

Recursively get value from nested dict

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

!!! note "Notes"
    - Handles arbitrary depth
    - Returns default if any key is missing or value is not a dict

<hr class="snippet-divider">

### Deep set (recursive function)

`dict` `nested` `deep-set` `recursive` `data-structures`

Recursively set value in nested dict

```python
def deep_set(d, keys, value):
    for k in keys[:-1]:
        d = d.setdefault(k, {})
    d[keys[-1]] = value


d = {}
deep_set(d, ["a", "b", "c"], 42)
print(d)  # {'a': {'b': {'c': 42}}}
```

!!! note "Notes"
    - Creates intermediate dicts as needed
    - Overwrites existing values at the target key

<hr class="snippet-divider">

### Flatten nested dict (to single-level dict)

`dict` `nested` `flatten` `recursive` `data-structures`

Flatten nested dict to single-level dict

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

!!! note "Notes"
    - Uses dot notation for keys by default
    - Key separator can be customized
    - Useful for config or serialization

<hr class="snippet-divider">

### Update nested dict (deep update)

`dict` `nested` `update` `recursive` `data-structures`

Recursively update nested dict

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

!!! note "Notes"
    - Updates only matching nested dicts
    - Overwrites non-dict values at any level

<hr class="snippet-divider">

### Delete nested key (safe)

`dict` `nested` `delete` `safe` `data-structures`

Safely delete nested key

```python
def deep_del(d, keys):
    for k in keys[:-1]:
        d = d.get(k, {})
    d.pop(keys[-1], None)


d = {"a": {"b": {"c": 42}}}
deep_del(d, ["a", "b", "c"])
print(d)  # {'a': {'b': {}}}
```

!!! note "Notes"
    - Does nothing if any intermediate key is missing
    - No error if key does not exist

<hr class="snippet-divider">

### Nested dict with defaultdict

`dict` `nested` `defaultdict` `auto` `data-structures`

Auto-vivifying nested dict with defaultdict

```python
from collections import defaultdict


def nested_dict():
    return defaultdict(nested_dict)


d = nested_dict()
d["a"]["b"]["c"] = 42
print(d["a"]["b"]["c"])  # 42
```

!!! note "Notes"
    - Automatically creates nested dicts on access
    - Useful for dynamic or unknown-depth structures

<hr class="snippet-divider">

## Performance and Edge Cases

###  Large nested dicts (performance)

`dict` `nested` `performance` `data-structures`

Deep access/set is fast for reasonable depth

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

!!! note "Notes"
    - Performance is good for shallow or moderate depth
    - Deeply nested structures may impact speed

<hr class="snippet-divider">

### Edge cases: missing keys, non-dict values

`dict` `nested` `edge-case` `data-structures`

Handle missing keys and non-dict values

```python
def deep_get(d, keys, default=None):
    # Function is defined in one of the above code block
    pass


d = {"a": {"b": 1}}
print(deep_get(d, ["a", "x"], default="not found"))  # not found
print(deep_get(d, ["a", "b", "c"], default="not found"))  # not found
```

!!! note "Notes"
    - Returns default if any key is missing or value is not a dict
    - Useful for robust code in uncertain data

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Dictionary with Default Values](dict_default.md)
- **Reference**: See [📂 Dictionary Comprehension](dict_comprehension.md)

## 🏷️ Tags

`dict`, `nested`, `get`, `setdefault`, `deep-get`, `deep-set`, `flatten`, `update`, `delete`, `defaultdict`, `performance`, `edge-case`, `data-structures`

## 📝 Notes
- Use get/setdefault for safe access
- Use recursion for deep access, set, update, and flatten
- defaultdict can auto-create nested dicts
