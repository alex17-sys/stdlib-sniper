---
title: Find Max Min
description: Zero-dependency Python snippets for finding maximum and minimum values in lists and other data structures using the standard library.
keywords: both, comparison, conditional, custom, data-structures, duplicates, error, filter, find, function, handling, index, indices, key, list, max, maximum, min, minimum, monitoring, multiple, nested, performance, position, recursive, safe, timing
---

# Find Max Min

Zero-dependency Python snippets for finding maximum and minimum values in lists and other data structures using the standard library.

11 snippets available in this sub-category.

---

## Simple

###  Find maximum value

`list` `max` `maximum` `find` `data-structures`

Find maximum value in list

```python
def find_max(lst):
    """Find maximum value in list."""
    if not lst:
        raise ValueError("Cannot find maximum of empty list")
    return max(lst)


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = find_max(numbers)
print(result)  # 9
```

!!! note "Notes"
    - Uses built-in max function
    - Raises error for empty list
    - Works with any comparable types
    - Simple and efficient

<hr class="snippet-divider">

### Find minimum value

`list` `min` `minimum` `find` `data-structures`

Find minimum value in list

```python
def find_min(lst):
    """Find minimum value in list."""
    if not lst:
        raise ValueError("Cannot find minimum of empty list")
    return min(lst)


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = find_min(numbers)
print(result)  # 1
```

!!! note "Notes"
    - Uses built-in min function
    - Raises error for empty list
    - Works with any comparable types
    - Simple and efficient

<hr class="snippet-divider">

### Find both max and min

`list` `max` `min` `both` `find` `data-structures`

Find both maximum and minimum values in list

```python
def find_max_min(lst):
    """Find both maximum and minimum values in list."""
    if not lst:
        raise ValueError("Cannot find max/min of empty list")
    return max(lst), min(lst)


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
max_val, min_val = find_max_min(numbers)
print(f"Max: {max_val}, Min: {min_val}")  # Max: 9, Min: 1
```

!!! note "Notes"
    - Single pass through list
    - Returns tuple of values
    - Efficient for both operations
    - Common pattern

<hr class="snippet-divider">

## Complex

###  Find max/min with custom key function

`list` `max` `min` `key` `function` `custom` `data-structures`

Find max/min using custom key function

```python
def find_max_with_key(lst, key_func=None):
    """Find maximum value using custom key function."""
    if not lst:
        raise ValueError("Cannot find maximum of empty list")
    return max(lst, key=key_func)


def find_min_with_key(lst, key_func=None):
    """Find minimum value using custom key function."""
    if not lst:
        raise ValueError("Cannot find minimum of empty list")
    return min(lst, key=key_func)


# Find longest string
words = ["apple", "banana", "cherry", "date"]
longest = find_max_with_key(words, key=len)
print(longest)  # 'banana'

# Find shortest string
shortest = find_min_with_key(words, key=len)
print(shortest)  # 'date'

# Find person with highest age
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 20}]
oldest = find_max_with_key(people, key=lambda x: x["age"])
print(oldest)  # {'name': 'Bob', 'age': 30}
```

!!! note "Notes"
    - Flexible comparison logic
    - Lambda support
    - Object attribute access
    - Complex criteria

<hr class="snippet-divider">

### Find max/min with condition

`list` `max` `min` `conditional` `filter` `data-structures`

Find max/min among elements that satisfy condition

```python
def find_max_conditional(lst, condition_func):
    """Find maximum value among elements that satisfy condition."""
    filtered = [x for x in lst if condition_func(x)]
    if not filtered:
        raise ValueError("No elements satisfy the condition")
    return max(filtered)


def find_min_conditional(lst, condition_func):
    """Find minimum value among elements that satisfy condition."""
    filtered = [x for x in lst if condition_func(x)]
    if not filtered:
        raise ValueError("No elements satisfy the condition")
    return min(filtered)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Find maximum even number
def is_even(x):
    return x % 2 == 0


max_even = find_max_conditional(numbers, is_even)
print(max_even)  # 10

# Find minimum odd number
min_odd = find_min_conditional(numbers, lambda x: x % 2 == 1)
print(min_odd)  # 1
```

!!! note "Notes"
    - Conditional filtering
    - Flexible criteria
    - Error handling
    - Combined operations

<hr class="snippet-divider">

### Find max/min with index

`list` `max` `min` `index` `position` `data-structures`

Find max/min value and its index

```python
def find_max_with_index(lst):
    """Find maximum value and its index."""
    if not lst:
        raise ValueError("Cannot find maximum of empty list")

    max_val = max(lst)
    max_index = lst.index(max_val)
    return max_val, max_index


def find_min_with_index(lst):
    """Find minimum value and its index."""
    if not lst:
        raise ValueError("Cannot find minimum of empty list")

    min_val = min(lst)
    min_index = lst.index(min_val)
    return min_val, min_index


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
max_val, max_idx = find_max_with_index(numbers)
min_val, min_idx = find_min_with_index(numbers)

print(f"Max: {max_val} at index {max_idx}")  # Max: 9 at index 5
print(f"Min: {min_val} at index {min_idx}")  # Min: 1 at index 1
```

!!! note "Notes"
    - Returns value and position
    - Uses index method
    - First occurrence for duplicates
    - Position tracking

<hr class="snippet-divider">

### Find max/min with multiple indices

`list` `max` `min` `indices` `multiple` `duplicates` `data-structures`

Find max/min value and all its indices

```python
def find_max_all_indices(lst):
    """Find maximum value and all its indices."""
    if not lst:
        raise ValueError("Cannot find maximum of empty list")

    max_val = max(lst)
    indices = [i for i, x in enumerate(lst) if x == max_val]
    return max_val, indices


def find_min_all_indices(lst):
    """Find minimum value and all its indices."""
    if not lst:
        raise ValueError("Cannot find minimum of empty list")

    min_val = min(lst)
    indices = [i for i, x in enumerate(lst) if x == min_val]
    return min_val, indices


numbers = [3, 1, 4, 1, 5, 9, 2, 6, 1]
max_val, max_indices = find_max_all_indices(numbers)
min_val, min_indices = find_min_all_indices(numbers)

print(f"Max: {max_val} at indices {max_indices}")  # Max: 9 at indices [5]
print(f"Min: {min_val} at indices {min_indices}")  # Min: 1 at indices [1, 3, 8]
```

!!! note "Notes"
    - Handles duplicate values
    - Returns all positions
    - List comprehension
    - Complete information

<hr class="snippet-divider">

### Find max/min in nested list

`list` `max` `min` `nested` `recursive` `data-structures`

Find max/min value in nested list structure

```python
def find_max_nested(nested_list):
    """Find maximum value in nested list structure."""
    if not nested_list:
        raise ValueError("Cannot find maximum of empty list")

    max_val = float("-inf")

    def find_max_recursive(lst):
        nonlocal max_val
        for item in lst:
            if isinstance(item, list):
                find_max_recursive(item)
            else:
                max_val = max(max_val, item)

    find_max_recursive(nested_list)
    return max_val if max_val != float("-inf") else None


def find_min_nested(nested_list):
    """Find minimum value in nested list structure."""
    if not nested_list:
        raise ValueError("Cannot find minimum of empty list")

    min_val = float("inf")

    def find_min_recursive(lst):
        nonlocal min_val
        for item in lst:
            if isinstance(item, list):
                find_min_recursive(item)
            else:
                min_val = min(min_val, item)

    find_min_recursive(nested_list)
    return min_val if min_val != float("inf") else None


nested = [[1, 2, 3], [4, 5, [6, 7]], [8, 9]]
max_val = find_max_nested(nested)
min_val = find_min_nested(nested)

print(f"Max: {max_val}")  # Max: 9
print(f"Min: {min_val}")  # Min: 1
```

!!! note "Notes"
    - Recursive traversal
    - Handles arbitrary nesting
    - Global tracking
    - Deep search

<hr class="snippet-divider">

### Find max/min with performance monitoring

`list` `max` `min` `performance` `timing` `monitoring` `data-structures`

Find max/min with performance monitoring

```python
import time


def find_max_min_with_timing(lst, operation="both"):
    """Find max/min with performance monitoring."""
    start_time = time.time()

    if operation == "max":
        result = max(lst)
    elif operation == "min":
        result = min(lst)
    elif operation == "both":
        result = (max(lst), min(lst))
    else:
        raise ValueError("Operation must be 'max', 'min', or 'both'")

    end_time = time.time()

    return {
        "result": result,
        "execution_time": end_time - start_time,
        "list_length": len(lst),
        "operation": operation,
    }


# Performance comparison
large_list = list(range(100000))

max_stats = find_max_min_with_timing(large_list, "max")
min_stats = find_max_min_with_timing(large_list, "min")
both_stats = find_max_min_with_timing(large_list, "both")

print(f"Max only: {max_stats['execution_time']:.6f}s")
print(f"Min only: {min_stats['execution_time']:.6f}s")
print(f"Both: {both_stats['execution_time']:.6f}s")
```

!!! note "Notes"
    - Performance measurement
    - Operation comparison
    - Benchmarking tool
    - Optimization insights

<hr class="snippet-divider">

### Find max/min with error handling

`list` `max` `min` `safe` `error` `handling` `data-structures`

Safely find max/min with error handling

```python
def find_max_safe(lst):
    """Safely find maximum value with error handling."""
    try:
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")

        if not lst:
            return None

        return max(lst)

    except Exception as e:
        print(f"Error finding maximum: {e}")
        return None


def find_min_safe(lst):
    """Safely find minimum value with error handling."""
    try:
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")

        if not lst:
            return None

        return min(lst)

    except Exception as e:
        print(f"Error finding minimum: {e}")
        return None


# Safe max/min with error handling
try:
    result = find_max_safe([3, 1, 4, 1, 5, 9, 2, 6])
    print(result)  # 9
except Exception as e:
    print(f"Error: {e}")
```

!!! note "Notes"
    - Comprehensive error handling
    - Type validation
    - Graceful degradation
    - Production ready

<hr class="snippet-divider">

### Find max/min with custom comparison

`list` `max` `min` `custom` `comparison` `function` `data-structures`

Find max/min using custom comparison function

```python
def find_max_custom_comparison(lst, compare_func):
    """Find maximum value using custom comparison function."""
    if not lst:
        raise ValueError("Cannot find maximum of empty list")

    max_val = lst[0]
    for item in lst[1:]:
        if compare_func(item, max_val) > 0:
            max_val = item

    return max_val


def find_min_custom_comparison(lst, compare_func):
    """Find minimum value using custom comparison function."""
    if not lst:
        raise ValueError("Cannot find minimum of empty list")

    min_val = lst[0]
    for item in lst[1:]:
        if compare_func(item, min_val) < 0:
            min_val = item

    return min_val


# Custom comparison for strings (case-insensitive)
def case_insensitive_compare(a, b):
    if isinstance(a, str) and isinstance(b, str):
        return (a.lower() > b.lower()) - (a.lower() < b.lower())
    return (a > b) - (a < b)


words = ["Apple", "banana", "Cherry", "date"]
max_word = find_max_custom_comparison(words, case_insensitive_compare)
min_word = find_min_custom_comparison(words, case_insensitive_compare)

print(f"Max: {max_word}")  # Max: date
print(f"Min: {min_word}")  # Min: Apple
```

!!! note "Notes"
    - Custom comparison logic
    - Manual iteration
    - Flexible ordering
    - Complex criteria

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Flatten List](./list_flatten.md)
- **Reference**: See [📂 Remove Duplicates From List](./list_remove_duplicates.md)
- **Reference**: See [📂 Sort List](./list_sort.md)
- **Reference**: See [📂 Zip List](./list_zip.md)

## 🏷️ Tags

`list`, `max`, `min`, `find`, `performance`, `custom`, `data-structures`

## 📝 Notes

- Built-in max/min functions are most efficient for standard use cases
- Custom key functions enable complex comparisons
- Conditional filtering enables subset operations
- Index tracking provides position information
- Always validate input for production use
- Consider performance implications for very large lists
