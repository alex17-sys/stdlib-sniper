# Sort Dictionary

Zero-dependency Python snippets using only the standard library.

8 snippets available in this sub-category.

---

## Simple

###  Sort by key (ascending)

`dict` `sort` `key` `ascending` `data-structures`

Sort dictionary by key (ascending)

```python
d = {"b": 2, "a": 1, "c": 3}
sorted_by_key = dict(sorted(d.items()))
print(sorted_by_key)  # {'a': 1, 'b': 2, 'c': 3}
```

!!! note "Notes"
    - sorted() returns a list of tuples; wrap with dict() for new dict
    - Preserves order in Python 3.7+

<hr class="snippet-divider">

### Sort by value (ascending)

`dict` `sort` `value` `ascending` `data-structures`

Sort dictionary by value (ascending)

```python
d = {"b": 2, "a": 1, "c": 3}
sorted_by_value = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_by_value)  # {'a': 1, 'b': 2, 'c': 3}
```

!!! note "Notes"
    - key argument sorts by value
    - Stable sort: order of equal values is preserved

<hr class="snippet-divider">

### Sort by key (descending)

`dict` `sort` `key` `descending` `data-structures`

Sort dictionary by key (descending)

```python
d = {"b": 2, "a": 1, "c": 3}
sorted_by_key_desc = dict(sorted(d.items(), reverse=True))
print(sorted_by_key_desc)  # {'c': 3, 'b': 2, 'a': 1}
```

!!! note "Notes"
    - reverse=True for descending order
    - Preserves order in Python 3.7+

<hr class="snippet-divider">

### Sort by value (descending)

`dict` `sort` `value` `descending` `data-structures`

Sort dictionary by value (descending)

```python
d = {"b": 2, "a": 1, "c": 3}
sorted_by_value_desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print(sorted_by_value_desc)  # {'c': 3, 'b': 2, 'a': 1}
```

!!! note "Notes"
    - Use reverse=True to sort values descending
    - Stable sort: order of equal values is preserved

<hr class="snippet-divider">

## Complex

###  Sort by custom key (length, function)

`dict` `sort` `custom` `function` `data-structures`

Sort dictionary by custom key function

```python
d = {"apple": 5, "banana": 2, "pear": 10}
sorted_by_len = dict(sorted(d.items(), key=lambda item: len(item[0])))
print(sorted_by_len)  # {'pear': 10, 'apple': 5, 'banana': 2}

# Sort by value squared
d = {"a": 2, "b": -3, "c": 1}
sorted_by_val_sq = dict(sorted(d.items(), key=lambda item: item[1] ** 2))
print(sorted_by_val_sq)  # {'c': 1, 'a': 2, 'b': -3}
```

!!! note "Notes"
    - key can be any function of (key, value)
    - Useful for advanced sorting (e.g., by string length, abs value)

<hr class="snippet-divider">

### Stable sort (preserve order for equal keys/values)

`dict` `sort` `stable` `data-structures`

Python's sort is stable (preserves order for equal values)

```python
d = {"a": 2, "b": 2, "c": 1}
sorted_stable = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_stable)  # {'c': 1, 'a': 2, 'b': 2}
```

!!! note "Notes"
    - Order of equal values is preserved
    - Useful for multi-level sorting

<hr class="snippet-divider">

### Sort nested dictionary by inner value

`dict` `sort` `nested` `custom` `data-structures`

Sort dictionary by value of nested key

```python
d = {"a": {"score": 2}, "b": {"score": 1}, "c": {"score": 3}}
sorted_nested = dict(sorted(d.items(), key=lambda item: item[1]["score"]))
print(sorted_nested)  # {'b': {'score': 1}, 'a': {'score': 2}, 'c': {'score': 3}}
```

!!! note "Notes"
    - Use key=lambda item: item[1]['nested'] for nested dicts
    - Raises KeyError if nested key missing

<hr class="snippet-divider">

### Edge cases: empty dict, all equal values

`dict` `sort` `edge-case` `data-structures`

Handle edge cases for sorting

```python
print(dict(sorted({}.items())))  # {}
print(dict(sorted({"a": 1, "b": 1}.items(), key=lambda item: item[1])))  # {'a': 1, 'b': 1}
```

!!! note "Notes"
    - Sorting empty dict returns empty dict
    - All equal values: preserves original order

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Dictionary Comprehension](dict_comprehension.md)

## 🏷️ Tags

`dict`, `sort`, `key`, `value`, `custom`, `stable`, `nested`, `edge-case`, `data-structures`

## 📝 Notes
- sorted() always returns a list of tuples; wrap with dict() for a new dict
- Sorting does not modify the original dict
