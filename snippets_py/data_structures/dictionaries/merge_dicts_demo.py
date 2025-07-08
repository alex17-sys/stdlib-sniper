# 🧩 Merge with update()
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(d1)  # {'a': 1, 'b': 3, 'c': 4}


# 🧩 Merge with dict unpacking (Python 3.5+)
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = {**d1, **d2}
print(merged)  # {'a': 1, 'b': 3, 'c': 4}


# 🧩 Merge with | operator (Python 3.9+)
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1 | d2
print(merged)  # {'a': 1, 'b': 3, 'c': 4}


# 🧩 Merge multiple dicts (reduce)
from functools import reduce

dicts = [{"a": 1}, {"b": 2}, {"a": 3}]
merged = reduce(lambda a, b: {**a, **b}, dicts)
print(merged)  # {'a': 3, 'b': 2}


# 🧩 Deep merge (recursive)
def deep_merge(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = v
    return result


d1 = {"a": 1, "b": {"x": 10}}
d2 = {"b": {"y": 20}, "c": 3}
print(deep_merge(d1, d2))  # {'a': 1, 'b': {'x': 10, 'y': 20}, 'c': 3}


# 🧩 Conflict resolution (custom merge)
def merge_with_conflict(d1, d2, conflict):
    result = d1.copy()
    for k, v in d2.items():
        if k in result:
            result[k] = conflict(result[k], v)
        else:
            result[k] = v
    return result


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = merge_with_conflict(d1, d2, lambda x, y: x + y)
print(merged)  # {'a': 1, 'b': 5, 'c': 4}


# 🧩 Edge cases: empty dicts, overlapping keys
print({**{}, **{}})  # {}
print({**{"a": 1}, **{}})  # {'a': 1}
print({**{}, **{"a": 1}})  # {'a': 1}
