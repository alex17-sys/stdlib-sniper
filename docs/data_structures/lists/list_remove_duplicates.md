---
title: Remove Duplicates from List
description: Zero-dependency Python snippets for removing duplicates from lists using the standard library.
keywords: analysis, case-insensitive, comparison, conversion, counter, custom, data-structures, dictionary, duplicates, error, fields, frequency, function, generator, handling, key, list, memory, monitoring, optimization, order, performance, remove, safe, set, string, timing
---

# Remove Duplicates from List

Zero-dependency Python snippets for removing duplicates from lists using the standard library.

10 snippets available in this sub-category.

---

## Simple

###  Remove duplicates preserving order

`list` `duplicates` `remove` `order` `data-structures`

Remove duplicates while preserving original order

```python
def remove_duplicates_ordered(lst):
    """Remove duplicates from list while preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


numbers = [1, 2, 2, 3, 4, 4, 5, 1]
result = remove_duplicates_ordered(numbers)
print(result)  # [1, 2, 3, 4, 5]
```

!!! note "Notes"
    - Preserves original order
    - Uses set for O(1) lookup
    - Memory efficient
    - Works with any hashable items

<hr class="snippet-divider">

### Remove duplicates using set

`list` `duplicates` `set` `conversion` `data-structures`

Remove duplicates using set conversion

```python
def remove_duplicates_set(lst):
    """Remove duplicates using set conversion."""
    return list(set(lst))


numbers = [1, 2, 2, 3, 4, 4, 5, 1]
result = remove_duplicates_set(numbers)
print(result)  # [1, 2, 3, 4, 5] (order may vary)
```

!!! note "Notes"
    - Simple one-liner
    - Order not guaranteed
    - Very efficient
    - Works with hashable items

<hr class="snippet-divider">

## Complex

###  Remove duplicates with custom key function

`list` `duplicates` `key` `function` `custom` `data-structures`

Remove duplicates using custom key function

```python
def remove_duplicates_by_key(lst, key_func=None):
    """Remove duplicates based on custom key function."""
    if key_func is None:
        def key_func(x):
            return x

    seen = set()
    result = []
    for item in lst:
        key = key_func(item)
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result


# Remove duplicates by first letter
words = ["apple", "banana", "apricot", "cherry", "blueberry"]
result = remove_duplicates_by_key(words, lambda x: x[0])
print(result)  # ['apple', 'banana', 'cherry']

# Remove duplicates by length
result2 = remove_duplicates_by_key(words, len)
print(result2)  # ['apple', 'banana', 'apricot']
```

!!! note "Notes"
    - Flexible key function
    - Preserves order
    - Useful for complex objects
    - Custom comparison logic

<hr class="snippet-divider">

### Remove duplicates with case-insensitive comparison

`list` `duplicates` `case-insensitive` `string` `data-structures`

Remove duplicates with case-insensitive comparison

```python
def remove_duplicates_case_insensitive(lst):
    """Remove duplicates ignoring case for strings."""
    seen = set()
    result = []
    for item in lst:
        if isinstance(item, str):
            key = item.lower()
        else:
            key = item

        if key not in seen:
            seen.add(key)
            result.append(item)
    return result


words = ["Apple", "apple", "BANANA", "banana", "Cherry"]
result = remove_duplicates_case_insensitive(words)
print(result)  # ['Apple', 'BANANA', 'Cherry']
```

!!! note "Notes"
    - Handles string case variations
    - Preserves original case
    - Works with mixed data types
    - Common text processing need

<hr class="snippet-divider">

### Remove duplicates from list of dictionaries

`list` `duplicates` `dictionary` `fields` `data-structures`

Remove duplicate dictionaries by specified fields

```python
def remove_duplicates_dicts(lst, key_fields=None):
    """Remove duplicate dictionaries based on specified fields."""
    if key_fields is None:
        key_fields = list(lst[0].keys()) if lst else []

    seen = set()
    result = []
    for item in lst:
        # Create tuple of key field values
        key = tuple(item.get(field) for field in key_fields)
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result


people = [
    {"name": "Alice", "age": 25, "city": "NYC"},
    {"name": "Bob", "age": 30, "city": "LA"},
    {"name": "Alice", "age": 25, "city": "Boston"},
    {"name": "Charlie", "age": 35, "city": "NYC"},
]

# Remove duplicates by name and age
result = remove_duplicates_dicts(people, ["name", "age"])
print(
    result
)  # [{'name': 'Alice', 'age': 25, 'city': 'NYC'}, {'name': 'Bob', 'age': 30, 'city': 'LA'}, {'name': 'Charlie', 'age': 35, 'city': 'NYC'}]
```

!!! note "Notes"
    - Works with complex objects
    - Configurable field selection
    - Preserves original structure
    - Useful for data cleaning

<hr class="snippet-divider">

### Remove duplicates with frequency tracking

`list` `duplicates` `frequency` `counter` `analysis` `data-structures`

Remove duplicates with frequency analysis

```python
from collections import Counter


def remove_duplicates_with_frequency(lst):
    """Remove duplicates and return frequency information."""
    counter = Counter(lst)
    unique_items = list(counter.keys())
    frequencies = list(counter.values())

    return {
        "unique_items": unique_items,
        "frequencies": frequencies,
        "total_duplicates": len(lst) - len(unique_items),
        "most_common": counter.most_common(1)[0] if counter else None,
    }


numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]
result = remove_duplicates_with_frequency(numbers)
print(f"Unique items: {result['unique_items']}")
print(f"Frequencies: {result['frequencies']}")
print(f"Total duplicates: {result['total_duplicates']}")
print(f"Most common: {result['most_common']}")
```

!!! note "Notes"
    - Provides frequency information
    - Uses Counter for efficiency
    - Statistical analysis
    - Data insights

<hr class="snippet-divider">

### Remove duplicates with custom comparison function

`list` `duplicates` `custom` `comparison` `function` `data-structures`

Remove duplicates with custom comparison function

```python
def remove_duplicates_custom_compare(lst, compare_func):
    """Remove duplicates using custom comparison function."""
    result = []
    for item in lst:
        # Check if item is already in result using custom comparison
        is_duplicate = any(compare_func(item, existing) for existing in result)
        if not is_duplicate:
            result.append(item)
    return result


# Custom comparison: items are equal if their absolute difference is <= 1
def within_one(a, b):
    return abs(a - b) <= 1


numbers = [1, 2, 4, 5, 7, 8, 10]
result = remove_duplicates_custom_compare(numbers, within_one)
print(result)  # [1, 4, 7, 10]
```

!!! note "Notes"
    - Flexible comparison logic
    - Complex matching rules
    - Preserves order
    - Advanced use cases

<hr class="snippet-divider">

### Remove duplicates with memory optimization

`list` `duplicates` `generator` `memory` `optimization` `data-structures`

Remove duplicates using generator

```python
def remove_duplicates_generator(lst):
    """Remove duplicates using generator for memory efficiency."""
    seen = set()
    for item in lst:
        if item not in seen:
            seen.add(item)
            yield item


numbers = [1, 2, 2, 3, 4, 4, 5, 1]
result = list(remove_duplicates_generator(numbers))
print(result)  # [1, 2, 3, 4, 5]

# Memory efficient iteration
for item in remove_duplicates_generator(numbers):
    print(item, end=" ")  # 1 2 3 4 5
```

!!! note "Notes"
    - Memory efficient
    - Lazy evaluation
    - Suitable for large lists
    - Generator pattern

<hr class="snippet-divider">

### Remove duplicates with performance monitoring

`list` `duplicates` `performance` `timing` `monitoring` `data-structures`

Remove duplicates with performance monitoring

```python
import time


def remove_duplicates_ordered(lst):
    # Function is defined in one of the above code block
    pass


def remove_duplicates_set(lst):
    # Function is defined in one of the above code block
    pass


def remove_duplicates_with_timing(lst, method="ordered"):
    """Remove duplicates with performance monitoring."""
    start_time = time.time()

    if method == "ordered":
        result = remove_duplicates_ordered(lst)
    elif method == "set":
        result = remove_duplicates_set(lst)
    else:
        raise ValueError("Method must be 'ordered' or 'set'")

    end_time = time.time()

    return {
        "result": result,
        "execution_time": end_time - start_time,
        "original_length": len(lst),
        "final_length": len(result),
        "duplicates_removed": len(lst) - len(result),
    }


# Performance comparison
large_list = list(range(10000)) + list(range(5000))  # 15000 items with 5000 duplicates

ordered_stats = remove_duplicates_with_timing(large_list, "ordered")
set_stats = remove_duplicates_with_timing(large_list, "set")

print(f"Ordered method: {ordered_stats['execution_time']:.6f}s")
print(f"Set method: {set_stats['execution_time']:.6f}s")
```

!!! note "Notes"
    - Performance measurement
    - Method comparison
    - Benchmarking tool
    - Optimization insights

<hr class="snippet-divider">

### Remove duplicates with error handling

`list` `duplicates` `safe` `error` `handling` `data-structures`

Safely remove duplicates with error handling

```python
def remove_duplicates_ordered(lst):
    # Function is defined in one of the above code block
    pass


def remove_duplicates_by_key(lst, key_func=None):
    # Function is defined in one of the above code block
    pass


def remove_duplicates_safe(lst, key_func=None):
    """Safely remove duplicates with error handling."""
    try:
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")

        if not lst:
            return []

        if key_func is not None:
            return remove_duplicates_by_key(lst, key_func)
        else:
            return remove_duplicates_ordered(lst)

    except Exception as e:
        print(f"Error removing duplicates: {e}")
        return lst  # Return original list on error


# Safe duplicate removal
try:
    result = remove_duplicates_safe([1, 2, 2, 3, 4, 4, 5, 1])
    print(result)  # [1, 2, 3, 4, 5]
except Exception as e:
    print(f"Error: {e}")
```

!!! note "Notes"
    - Comprehensive error handling
    - Type validation
    - Graceful degradation
    - Production ready

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Flatten List](./list_flatten.md)
- **Reference**: See [📂 Sort List](./list_sort.md)
- **Reference**: See [📂 Rotate List](./list_filter.md)

## 🏷️ Tags

`list`, `duplicates`, `remove`, `set`, `order`, `key`, `performance`, `data-structures`

## 📝 Notes

- Set-based removal is fastest but doesn't preserve order
- Ordered removal is slower but maintains original sequence
- Custom key functions enable complex deduplication logic
- Consider memory usage for very large lists
- Always handle edge cases like empty lists and non-hashable items
