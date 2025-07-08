# Get Unique Elements from List

Zero-dependency Python snippets for extracting unique elements from a list using the standard library.

## Simple

### 🧩 Unique elements with set

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print(unique)  # [1, 2, 3, 4, 5] (order not guaranteed)
```

📂 Remove duplicates from a list using set

🏷️ Tags: set, unique, list, duplicates, data-structures
📝 Notes:
- set() removes duplicates but does not preserve order
- Convert back to list if needed

### 🧩 Unique elements preserving order (Python 3.7+)

```python
def unique_preserve_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]


numbers = [1, 2, 2, 3, 4, 4, 5]
unique = unique_preserve_order(numbers)
print(unique)  # [1, 2, 3, 4, 5]
```

📂 Remove duplicates while preserving order

🏷️ Tags: set, unique, order, list, data-structures
📝 Notes:
- Uses set for fast membership test
- Preserves first occurrence order

## Complex

### 🧩 Unique elements by key

```python
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
```

📂 Remove duplicates by custom key function

🏷️ Tags: set, unique, key, custom, data-structures
📝 Notes:
- Useful for lists of dicts or objects
- Customizable uniqueness criteria

## 🔗 Cross Reference

- **Reference**: See [📂 Create Set](set_create.md)

## 🏷️ Tags

`set`, `unique`, `duplicates`, `order`, `key`, `data-structures`

## 📝 Notes
- Use set() for fast deduplication
- Use custom logic to preserve order or uniqueness by key
