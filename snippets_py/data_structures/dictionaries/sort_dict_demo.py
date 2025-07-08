# 🧩 Sort by key (ascending)
d = {"b": 2, "a": 1, "c": 3}
sorted_by_key = dict(sorted(d.items()))
print(sorted_by_key)  # {'a': 1, 'b': 2, 'c': 3}


# 🧩 Sort by value (ascending)
d = {"b": 2, "a": 1, "c": 3}
sorted_by_value = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_by_value)  # {'a': 1, 'b': 2, 'c': 3}


# 🧩 Sort by key (descending)
d = {"b": 2, "a": 1, "c": 3}
sorted_by_key_desc = dict(sorted(d.items(), reverse=True))
print(sorted_by_key_desc)  # {'c': 3, 'b': 2, 'a': 1}


# 🧩 Sort by value (descending)
d = {"b": 2, "a": 1, "c": 3}
sorted_by_value_desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print(sorted_by_value_desc)  # {'c': 3, 'b': 2, 'a': 1}


# 🧩 Sort by custom key (length, function)
d = {"apple": 5, "banana": 2, "pear": 10}
sorted_by_len = dict(sorted(d.items(), key=lambda item: len(item[0])))
print(sorted_by_len)  # {'pear': 10, 'apple': 5, 'banana': 2}

# Sort by value squared
d = {"a": 2, "b": -3, "c": 1}
sorted_by_val_sq = dict(sorted(d.items(), key=lambda item: item[1] ** 2))
print(sorted_by_val_sq)  # {'c': 1, 'a': 2, 'b': -3}


# 🧩 Stable sort (preserve order for equal keys/values)
d = {"a": 2, "b": 2, "c": 1}
sorted_stable = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_stable)  # {'c': 1, 'a': 2, 'b': 2}


# 🧩 Sort nested dictionary by inner value
d = {"a": {"score": 2}, "b": {"score": 1}, "c": {"score": 3}}
sorted_nested = dict(sorted(d.items(), key=lambda item: item[1]["score"]))
print(sorted_nested)  # {'b': {'score': 1}, 'a': {'score': 2}, 'c': {'score': 3}}


# 🧩 Edge cases: empty dict, all equal values
print(dict(sorted({}.items())))  # {}
print(dict(sorted({"a": 1, "b": 1}.items(), key=lambda item: item[1])))  # {'a': 1, 'b': 1}
