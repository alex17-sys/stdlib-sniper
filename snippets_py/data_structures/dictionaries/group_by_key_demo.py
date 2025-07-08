# 🧩 Group list of pairs by key (defaultdict)
from collections import defaultdict

pairs = [("a", 1), ("b", 2), ("a", 3)]
groups = defaultdict(list)
for k, v in pairs:
    groups[k].append(v)
print(dict(groups))  # {'a': [1, 3], 'b': [2]}


# 🧩 Manual grouping by key
pairs = [("a", 1), ("b", 2), ("a", 3)]
groups = {}
for k, v in pairs:
    if k not in groups:
        groups[k] = []
    groups[k].append(v)
print(groups)  # {'a': [1, 3], 'b': [2]}


# 🧩 Group by value (invert one-to-many)
from collections import defaultdict


pairs = [("a", 1), ("b", 2), ("c", 1)]
groups = defaultdict(list)
for k, v in pairs:
    groups[v].append(k)
print(dict(groups))  # {1: ['a', 'c'], 2: ['b']}


# 🧩 Group by custom function (e.g., length)
from collections import defaultdict


words = ["apple", "pear", "banana", "fig"]
groups = defaultdict(list)
for word in words:
    groups[len(word)].append(word)
print(dict(groups))  # {5: ['apple'], 4: ['pear'], 6: ['banana'], 3: ['fig']}


# 🧩 Group by multiple keys (tuple/grouping)
from collections import defaultdict


records = [
    {"city": "NY", "type": "A", "val": 1},
    {"city": "NY", "type": "B", "val": 2},
    {"city": "LA", "type": "A", "val": 3},
]
groups = defaultdict(list)
for rec in records:
    key = (rec["city"], rec["type"])
    groups[key].append(rec["val"])
print(dict(groups))  # {('NY', 'A'): [1], ('NY', 'B'): [2], ('LA', 'A'): [3]}


# 🧩 Group and aggregate (sum, count, min, max)
from collections import defaultdict

pairs = [("a", 1), ("b", 2), ("a", 3)]
sums = defaultdict(int)
for k, v in pairs:
    sums[k] += v
print(dict(sums))  # {'a': 4, 'b': 2}

counts = defaultdict(int)
for k, _ in pairs:
    counts[k] += 1
print(dict(counts))  # {'a': 2, 'b': 1}


# 🧩 Group and flatten (single list of all values)
from collections import defaultdict


pairs = [("a", 1), ("b", 2), ("a", 3)]
groups = defaultdict(list)
for k, v in pairs:
    groups[k].append(v)
flat = [v for group in groups.values() for v in group]
print(flat)  # [1, 3, 2]


# 🧩 Group by key with set (unique values)
from collections import defaultdict


pairs = [("a", 1), ("a", 1), ("b", 2)]
groups = defaultdict(set)
for k, v in pairs:
    groups[k].add(v)
print(dict(groups))  # {'a': {1}, 'b': {2}}


# 🧩 Group by key with order preserved (OrderedDict)
from collections import OrderedDict

pairs = [("a", 1), ("b", 2), ("a", 3)]
groups = OrderedDict()
for k, v in pairs:
    if k not in groups:
        groups[k] = []
    groups[k].append(v)
print(groups)  # OrderedDict([('a', [1, 3]), ('b', [2])])


# 🧩 Group by key with itertools.groupby (sorted input)
from itertools import groupby

pairs = [("a", 1), ("a", 2), ("b", 3)]
pairs.sort(key=lambda x: x[0])
groups = {k: [v for _, v in group] for k, group in groupby(pairs, key=lambda x: x[0])}
print(groups)  # {'a': [1, 2], 'b': [3]}


# 🧩 Large groupings (performance)
import time
from collections import defaultdict

N = 10**6
pairs = [("a", i) for i in range(N)]
start = time.time()
groups = defaultdict(list)
for k, v in pairs:
    groups[k].append(v)
print("Time:", time.time() - start)


# 🧩 Edge cases: empty input, all unique keys
from collections import defaultdict


print(dict(defaultdict(list)))  # {}
pairs = [("a", 1), ("b", 2)]
groups = defaultdict(list)
for k, v in pairs:
    groups[k].append(v)
print(dict(groups))  # {'a': [1], 'b': [2]}
