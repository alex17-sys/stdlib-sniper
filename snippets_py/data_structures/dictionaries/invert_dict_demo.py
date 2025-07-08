# 🧩 Invert 1:1 dictionary (values unique)
d = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in d.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}


# 🧩 Invert with duplicate values (many-to-one)
d = {"a": 1, "b": 2, "c": 1}
inverted = {}
for k, v in d.items():
    inverted[v] = k  # Last key wins
print(inverted)  # {1: 'c', 2: 'b'}


# 🧩 Invert to one-to-many (group keys by value)
d = {"a": 1, "b": 2, "c": 1}
inverted = {}
for k, v in d.items():
    inverted.setdefault(v, []).append(k)
print(inverted)  # {1: ['a', 'c'], 2: ['b']}


# 🧩 Invert with defaultdict
from collections import defaultdict

d = {"a": 1, "b": 2, "c": 1}
inverted = defaultdict(list)
for k, v in d.items():
    inverted[v].append(k)
print(dict(inverted))  # {1: ['a', 'c'], 2: ['b']}


# 🧩 Invert with non-hashable values (error handling)
d = {"a": [1, 2], "b": [3, 4]}
try:
    inverted = {v: k for k, v in d.items()}
except TypeError as e:
    print(e)  # unhashable type: 'list'


# 🧩 Invert nested dictionary (swap inner keys/values)
d = {"x": {"a": 1, "b": 2}, "y": {"c": 3}}
inverted = {outer: {v: k for k, v in inner.items()} for outer, inner in d.items()}
print(inverted)  # {'x': {1: 'a', 2: 'b'}, 'y': {3: 'c'}}


# 🧩 Edge cases: empty dict, non-unique values
print({v: k for k, v in {}.items()})  # {}
print({v: k for k, v in {"a": 1, "b": 1}.items()})  # {1: 'b'}
