# 🧩 Basic dictionary comprehension
squares = {x: x * x for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# 🧩 From list of tuples
pairs = [("a", 1), ("b", 2)]
d = {k: v for k, v in pairs}
print(d)  # {'a': 1, 'b': 2}


# 🧩 From two lists (zip)
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)  # {'a': 1, 'b': 2, 'c': 3}


# 🧩 Filter items by value
d = {"a": 1, "b": 2, "c": 3}
even = {k: v for k, v in d.items() if v % 2 == 0}
print(even)  # {'b': 2}


# 🧩 Transform keys and values
d = {"a": 1, "b": 2}
transformed = {k.upper(): v * 10 for k, v in d.items()}
print(transformed)  # {'A': 10, 'B': 20}


# 🧩 Conditional values
nums = [1, 2, 3, 4]
parity = {x: ("even" if x % 2 == 0 else "odd") for x in nums}
print(parity)  # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}


# 🧩 Nested dictionary comprehension
matrix = [[1, 2], [3, 4]]
d = {i: {j: val for j, val in enumerate(row)} for i, row in enumerate(matrix)}
print(d)  # {0: {0: 1, 1: 2}, 1: {0: 3, 1: 4}}


# 🧩 Flatten nested dict to single dict
nested = {"a": {"x": 1}, "b": {"y": 2}}
flat = {f"{k}_{ik}": iv for k, v in nested.items() for ik, iv in v.items()}
print(flat)  # {'a_x': 1, 'b_y': 2}


# 🧩 Enumerate with comprehension
lst = ["apple", "banana"]
d = {i: v for i, v in enumerate(lst)}
print(d)  # {0: 'apple', 1: 'banana'}


# 🧩 Default values with get()
keys = ["a", "b", "c"]
source = {"a": 1, "c": 3}
d = {k: source.get(k, 0) for k in keys}
print(d)  # {'a': 1, 'b': 0, 'c': 3}


# 🧩 Comprehension with try/except (error handling)
lst = ["1", "2", "x"]
d = {}
for s in lst:
    try:
        d[s] = int(s)
    except ValueError:
        d[s] = None
print(d)  # {'1': 1, '2': 2, 'x': None}


# 🧩 Dictionary comprehension from set
s = {"a", "b", "c"}
d = {k: ord(k) for k in s}
print(d)  # {'a': 97, 'b': 98, 'c': 99}


# 🧩 Dictionary comprehension with filtering and transformation
nums = range(10)
squares_even = {x: x * x for x in nums if x % 2 == 0}
print(squares_even)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


# 🧩 Large dict comprehensions (performance)
import time

N = 10**6
start = time.time()
d = {x: x * 2 for x in range(N)}
print("Time:", time.time() - start)


# 🧩 Avoiding key collisions
lst = ["a", "b", "a"]
d = {k: i for i, k in enumerate(lst)}
print(d)  # {'a': 2, 'b': 1}


# 🧩 Edge cases: empty input, non-hashable keys
print({k: v for k, v in []})  # {}
try:
    d = {[1, 2]: "x" for _ in range(1)}
except TypeError as e:
    print(e)  # unhashable type: 'list'
