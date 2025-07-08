# 🧩 From list of (key, value) tuples
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)
print(d)  # {'a': 1, 'b': 2}


# 🧩 From two lists (zip)
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)  # {'a': 1, 'b': 2, 'c': 3}


# 🧩 From list with enumerate (index as key)
lst = ["apple", "banana"]
d = dict(enumerate(lst))
print(d)  # {0: 'apple', 1: 'banana'}


# 🧩 From list of keys with default value
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)
print(d)  # {'a': 0, 'b': 0, 'c': 0}


# 🧩 From list of dicts (merge by key)
lst = [{"a": 1}, {"b": 2}, {"a": 3}]
merged = {}
for d in lst:
    merged.update(d)
print(merged)  # {'a': 3, 'b': 2}


# 🧩 From list of pairs with duplicate keys (last wins)
pairs = [("a", 1), ("b", 2), ("a", 3)]
d = dict(pairs)
print(d)  # {'a': 3, 'b': 2}


# 🧩 From list of pairs with aggregation (sum/count)
from collections import defaultdict

pairs = [("a", 1), ("b", 2), ("a", 3)]
sums = defaultdict(int)
for k, v in pairs:
    sums[k] += v
print(dict(sums))  # {'a': 4, 'b': 2}


# 🧩 From list of lists (flatten to dict)
lst = [["a", 1], ["b", 2]]
d = dict(lst)
print(d)  # {'a': 1, 'b': 2}


# 🧩 From list with transformation (comprehension)
lst = ["apple", "banana"]
d = {x: len(x) for x in lst}
print(d)  # {'apple': 5, 'banana': 6}


# 🧩 From list of tuples with error handling
lst = [("a", 1), ("b",), ("c", 3)]
d = {}
for item in lst:
    if len(item) == 2:
        k, v = item
        d[k] = v
print(d)  # {'a': 1, 'c': 3}


# 🧩 Large lists (performance)
import time

N = 10**6
lst = [(x, x * 2) for x in range(N)]
start = time.time()
d = dict(lst)
print("Time:", time.time() - start)


# 🧩 Edge cases: empty list, non-hashable keys
print(dict([]))  # {}
try:
    d = dict([([1, 2], "x")])
except TypeError as e:
    print(e)  # unhashable type: 'list'
