# 🧩 Access nested value (direct)
d = {"a": {"b": {"c": 42}}}
value = d["a"]["b"]["c"]
print(value)  # 42


# 🧩 Safe access with get()
d = {"a": {"b": {"c": 42}}}
value = d.get("a", {}).get("b", {}).get("c")
print(value)  # 42
missing = d.get("a", {}).get("x", {}).get("y")
print(missing)  # {}


# 🧩 Set default for nested key (setdefault)
d = {}
d.setdefault("a", {}).setdefault("b", {})["c"] = 42
print(d)  # {'a': {'b': {'c': 42}}}


# 🧩 Deep get (recursive function)
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


# 🧩 Deep set (recursive function)
def deep_set(d, keys, value):
    for k in keys[:-1]:
        d = d.setdefault(k, {})
    d[keys[-1]] = value


d = {}
deep_set(d, ["a", "b", "c"], 42)
print(d)  # {'a': {'b': {'c': 42}}}


# 🧩 Flatten nested dict (to single-level dict)
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


# 🧩 Update nested dict (deep update)
def deep_update(d, u):
    for k, v in u.items():
        if isinstance(v, dict) and isinstance(d.get(k), dict):
            deep_update(d[k], v)
        else:
            d[k] = v


d = {"a": {"b": 1}}
deep_update(d, {"a": {"c": 2}})
print(d)  # {'a': {'b': 1, 'c': 2}}


# 🧩 Delete nested key (safe)
def deep_del(d, keys):
    for k in keys[:-1]:
        d = d.get(k, {})
    d.pop(keys[-1], None)


d = {"a": {"b": {"c": 42}}}
deep_del(d, ["a", "b", "c"])
print(d)  # {'a': {'b': {}}}


# 🧩 Nested dict with defaultdict
from collections import defaultdict


def nested_dict():
    return defaultdict(nested_dict)


d = nested_dict()
d["a"]["b"]["c"] = 42
print(d["a"]["b"]["c"])  # 42


# 🧩 Large nested dicts (performance)
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


# 🧩 Edge cases: missing keys, non-dict values
def deep_get(d, keys, default=None):
    # Function is defined in one of the above code block
    pass


d = {"a": {"b": 1}}
print(deep_get(d, ["a", "x"], default="not found"))  # not found
print(deep_get(d, ["a", "b", "c"], default="not found"))  # not found
