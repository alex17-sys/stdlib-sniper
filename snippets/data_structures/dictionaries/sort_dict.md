# Sort Dictionary

Zero-dependency Python snippets for sorting dictionaries using the standard library.

## Simple

### 🧩 Sort by key (ascending)

```python
d = {"b": 2, "a": 1, "c": 3}
sorted_by_key = dict(sorted(d.items()))
print(sorted_by_key)  # {'a': 1, 'b': 2, 'c': 3}
```

📂 Sort dictionary by key (ascending)

🏷️ Tags: dict, sort, key, ascending, data-structures
📝 Notes:
- sorted() returns a list of tuples; wrap with dict() for new dict
- Preserves order in Python 3.7+

### 🧩 Sort by value (ascending)

```python
d = {"b": 2, "a": 1, "c": 3}
sorted_by_value = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_by_value)  # {'a': 1, 'b': 2, 'c': 3}
```

📂 Sort dictionary by value (ascending)

🏷️ Tags: dict, sort, value, ascending, data-structures
📝 Notes:
- key argument sorts by value
- Stable sort: order of equal values is preserved

### 🧩 Sort by key (descending)

```python
d = {"b": 2, "a": 1, "c": 3}
sorted_by_key_desc = dict(sorted(d.items(), reverse=True))
print(sorted_by_key_desc)  # {'c': 3, 'b': 2, 'a': 1}
```

📂 Sort dictionary by key (descending)

🏷️ Tags: dict, sort, key, descending, data-structures
📝 Notes:
- reverse=True for descending order
- Preserves order in Python 3.7+

### 🧩 Sort by value (descending)

```python
d = {"b": 2, "a": 1, "c": 3}
sorted_by_value_desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print(sorted_by_value_desc)  # {'c': 3, 'b': 2, 'a': 1}
```

📂 Sort dictionary by value (descending)

🏷️ Tags: dict, sort, value, descending, data-structures
📝 Notes:
- Use reverse=True to sort values descending
- Stable sort: order of equal values is preserved

## Complex

### 🧩 Sort by custom key (length, function)

```python
d = {"apple": 5, "banana": 2, "pear": 10}
sorted_by_len = dict(sorted(d.items(), key=lambda item: len(item[0])))
print(sorted_by_len)  # {'pear': 10, 'apple': 5, 'banana': 2}

# Sort by value squared
d = {"a": 2, "b": -3, "c": 1}
sorted_by_val_sq = dict(sorted(d.items(), key=lambda item: item[1] ** 2))
print(sorted_by_val_sq)  # {'c': 1, 'a': 2, 'b': -3}
```

📂 Sort dictionary by custom key function

🏷️ Tags: dict, sort, custom, function, data-structures
📝 Notes:
- key can be any function of (key, value)
- Useful for advanced sorting (e.g., by string length, abs value)

### 🧩 Stable sort (preserve order for equal keys/values)

```python
d = {"a": 2, "b": 2, "c": 1}
sorted_stable = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_stable)  # {'c': 1, 'a': 2, 'b': 2}
```

📂 Python's sort is stable (preserves order for equal values)

🏷️ Tags: dict, sort, stable, data-structures
📝 Notes:
- Order of equal values is preserved
- Useful for multi-level sorting

### 🧩 Sort nested dictionary by inner value

```python
d = {"a": {"score": 2}, "b": {"score": 1}, "c": {"score": 3}}
sorted_nested = dict(sorted(d.items(), key=lambda item: item[1]["score"]))
print(sorted_nested)  # {'b': {'score': 1}, 'a': {'score': 2}, 'c': {'score': 3}}
```

📂 Sort dictionary by value of nested key

🏷️ Tags: dict, sort, nested, custom, data-structures
📝 Notes:
- Use key=lambda item: item[1]['nested'] for nested dicts
- Raises KeyError if nested key missing

### 🧩 Edge cases: empty dict, all equal values

```python
print(dict(sorted({}.items())))  # {}
print(dict(sorted({"a": 1, "b": 1}.items(), key=lambda item: item[1])))  # {'a': 1, 'b': 1}
```

📂 Handle edge cases for sorting

🏷️ Tags: dict, sort, edge-case, data-structures
📝 Notes:
- Sorting empty dict returns empty dict
- All equal values: preserves original order

## 🔗 Cross Reference

- **Reference**: See [📂 Dictionary Comprehension](dict_comprehension.md)

## 🏷️ Tags

`dict`, `sort`, `key`, `value`, `custom`, `stable`, `nested`, `edge-case`, `data-structures`

## 📝 Notes
- sorted() always returns a list of tuples; wrap with dict() for a new dict
- Sorting does not modify the original dict
