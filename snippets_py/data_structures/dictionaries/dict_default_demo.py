# 🧩 Using defaultdict for default values
from collections import defaultdict

d = defaultdict(int)
d["a"] += 1
d["b"] += 2
print(dict(d))  # {'a': 1, 'b': 2}


# 🧩 defaultdict with list (grouping)
from collections import defaultdict

d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
print(dict(d))  # {'a': [1, 2]}


# 🧩 setdefault for default value
d = {}
d.setdefault("a", []).append(1)
print(d)  # {'a': [1]}


# 🧩 defaultdict with custom factory
from collections import defaultdict


def zero():
    return 0


d = defaultdict(zero)
d["a"] += 5
print(dict(d))  # {'a': 5}


# 🧩 defaultdict for counting (Counter)
from collections import Counter

lst = ["a", "b", "a"]
c = Counter(lst)
print(dict(c))  # {'a': 2, 'b': 1}


# 🧩 Nested defaultdict (auto-vivify)
from collections import defaultdict


def nested():
    return defaultdict(nested)


d = nested()
d["a"]["b"]["c"] = 42
print(d["a"]["b"]["c"])  # 42


# 🧩 Custom dict with __missing__
class DefaultDict(dict):
    def __missing__(self, key):
        return 0


d = DefaultDict(a=1)
print(d["a"])  # 1
print(d["b"])  # 0


# 🧩 Handle missing keys with get()
d = {"a": 1}
print(d.get("b", 0))  # 0


# 🧩 setdefault vs defaultdict
d = {}
d.setdefault("a", []).append(1)
from collections import defaultdict

dd = defaultdict(list)
dd["a"].append(1)
print(d, dict(dd))  # {'a': [1]} {'a': [1]}


# 🧩 Large defaultdicts (performance)
import time
from collections import defaultdict

N = 10**6
d = defaultdict(int)
start = time.time()
for i in range(N):
    d[i] += 1
print("Time:", time.time() - start)


# 🧩 Edge cases: missing keys, mutable defaults
from collections import defaultdict

d = defaultdict(list)
d["a"].append(1)
print(d["b"])  # []
# All keys get independent lists
