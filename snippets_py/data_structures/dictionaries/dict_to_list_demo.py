# 🧩 Get list of keys
d = {"a": 1, "b": 2, "c": 3}
keys = list(d.keys())
print(keys)  # ['a', 'b', 'c']


# 🧩 Get list of values
d = {"a": 1, "b": 2, "c": 3}
values = list(d.values())
print(values)  # [1, 2, 3]


# 🧩 Get list of (key, value) tuples
d = {"a": 1, "b": 2, "c": 3}
items = list(d.items())
print(items)  # [('a', 1), ('b', 2), ('c', 3)]


# 🧩 Flatten nested dict to list of (outer, inner, value)
nested = {"a": {"x": 1}, "b": {"y": 2}}
flat = [(k, ik, iv) for k, v in nested.items() for ik, iv in v.items()]
print(flat)  # [('a', 'x', 1), ('b', 'y', 2)]


# 🧩 List of keys/values/items with filtering
d = {"a": 1, "b": 2, "c": 3}
even_keys = [k for k, v in d.items() if v % 2 == 0]
print(even_keys)  # ['b']

values_gt1 = [v for v in d.values() if v > 1]
print(values_gt1)  # [2, 3]


# 🧩 List of sorted keys/values/items
d = {"b": 2, "a": 1, "c": 3}
sorted_keys = sorted(d)
print(sorted_keys)  # ['a', 'b', 'c']
sorted_items = sorted(d.items(), key=lambda item: item[1])
print(sorted_items)  # [('a', 1), ('b', 2), ('c', 3)]


# 🧩 List of unique values
d = {"a": 1, "b": 2, "c": 1}
unique_values = list(set(d.values()))
print(unique_values)  # [1, 2]


# 🧩 List of keys/values/items with transformation
d = {"a": 1, "b": 2}
keys_upper = [k.upper() for k in d]
print(keys_upper)  # ['A', 'B']
values_squared = [v**2 for v in d.values()]
print(values_squared)  # [1, 4]


# 🧩 List of dicts from list of keys/values
keys = ["a", "b"]
values = [1, 2]
dicts = [{k: v} for k, v in zip(keys, values)]
print(dicts)  # [{'a': 1}, {'b': 2}]


# 🧩 Large dicts (performance)
import time

N = 10**6
d = {x: x * 2 for x in range(N)}
start = time.time()
keys = list(d.keys())
print("Time:", time.time() - start)


# 🧩 Edge cases: empty dict, non-hashable values
print(list({}.keys()))  # []
print(list({}.values()))  # []
print(list({}.items()))  # []
