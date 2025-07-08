# 🧩 Unique elements with set
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print(unique)  # [1, 2, 3, 4, 5] (order not guaranteed)


# 🧩 Unique elements preserving order (Python 3.7+)
def unique_preserve_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]


numbers = [1, 2, 2, 3, 4, 4, 5]
unique = unique_preserve_order(numbers)
print(unique)  # [1, 2, 3, 4, 5]


# 🧩 Unique elements by key
def unique_by_key(lst, key_func):
    seen = set()
    result = []
    for item in lst:
        key = key_func(item)
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result


# Example: unique by string length
words = ["a", "bb", "ccc", "dd", "eee", "f"]
unique = unique_by_key(words, len)
print(unique)  # ['a', 'bb', 'ccc']
