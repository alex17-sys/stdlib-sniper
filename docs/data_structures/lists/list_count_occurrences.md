---
title: Count Occurrences
description: Zero-dependency Python snippets for counting occurrences of elements in lists and other data structures using the standard library.
keywords: all, case, categorization, conditional, count, data-structures, elements, error, filter, frequency, function, generator, group, handling, insensitive, list, matching, memory, monitoring, nested, occurrences, optimization, partial, performance, recursive, safe, string, timing
---

# Count Occurrences

Zero-dependency Python snippets for counting occurrences of elements in lists and other data structures using the standard library.

10 snippets available in this sub-category.

---

## Simple

###  Count occurrences in list

`list` `count` `occurrences` `frequency` `data-structures`

Count occurrences of target element in list

```python
def count_occurrences(lst, target):
    """Count occurrences of target element in list."""
    return lst.count(target)


numbers = [1, 2, 3, 2, 4, 2, 5]
result = count_occurrences(numbers, 2)
print(result)  # 3
```

!!! note "Notes"
    - Uses built-in count method
    - Simple and efficient
    - Returns integer count
    - Case-sensitive for strings

<hr class="snippet-divider">

### Count all elements in list

`list` `count` `all` `elements` `frequency` `data-structures`

Count occurrences of all elements in list

```python
def count_all_elements(lst):
    """Count occurrences of all elements in list."""
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return counts


fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
result = count_all_elements(fruits)
print(result)  # {'apple': 3, 'banana': 2, 'cherry': 1}
```

!!! note "Notes"
    - Uses dictionary for counting
    - Efficient for multiple elements
    - Returns frequency dictionary
    - Handles any hashable elements

<hr class="snippet-divider">

## Complex

###  Count occurrences with condition

`list` `count` `conditional` `filter` `data-structures`

Count elements that satisfy a condition

```python
def count_occurrences_conditional(lst, condition_func):
    """Count elements that satisfy a condition."""
    return sum(1 for item in lst if condition_func(item))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Count even numbers
def is_even(x):
    return x % 2 == 0


even_count = count_occurrences_conditional(numbers, is_even)
print(even_count)  # 5


# Count numbers greater than 5
def greater_than_5(x):
    return x > 5


greater_count = count_occurrences_conditional(numbers, lambda x: x > 5)
print(greater_count)  # 5
```

!!! note "Notes"
    - Flexible condition function
    - Lambda support
    - Boolean counting
    - Custom criteria

<hr class="snippet-divider">

### Count occurrences in nested list

`list` `count` `nested` `recursive` `data-structures`

Count occurrences in nested list structure

```python
def count_occurrences_nested(nested_list, target):
    """Count occurrences in nested list structure."""
    count = 0

    def count_recursive(lst):
        nonlocal count
        for item in lst:
            if isinstance(item, list):
                count_recursive(item)
            elif item == target:
                count += 1

    count_recursive(nested_list)
    return count


nested = [[1, 2, 3], [2, 4, 5], [1, 2, 6]]
result = count_occurrences_nested(nested, 2)
print(result)  # 3
```

!!! note "Notes"
    - Recursive traversal
    - Handles arbitrary nesting
    - Global counter
    - Deep search

<hr class="snippet-divider">

### Count occurrences with case insensitivity

`list` `count` `case` `insensitive` `string` `data-structures`

Count occurrences ignoring case for strings

```python
def count_occurrences_case_insensitive(lst, target):
    """Count occurrences ignoring case for strings."""
    if isinstance(target, str):
        return sum(1 for item in lst if isinstance(item, str) and item.lower() == target.lower())
    else:
        return lst.count(target)


words = ["Apple", "banana", "APPLE", "Cherry", "apple"]
result = count_occurrences_case_insensitive(words, "apple")
print(result)  # 3
```

!!! note "Notes"
    - Case-insensitive matching
    - String-specific handling
    - Preserves non-string behavior
    - Flexible type handling

<hr class="snippet-divider">

### Count occurrences with partial matching

`list` `count` `partial` `matching` `string` `data-structures`

Count occurrences with partial matching

```python
def count_occurrences_partial(lst, target, match_type="contains"):
    """Count occurrences with partial matching."""
    count = 0

    for item in lst:
        if isinstance(item, str) and isinstance(target, str):
            if match_type == "contains" and target in item:
                count += 1
            elif match_type == "startswith" and item.startswith(target):
                count += 1
            elif match_type == "endswith" and item.endswith(target):
                count += 1
        elif item == target:
            count += 1

    return count


words = ["apple", "application", "banana", "app", "cherry"]
result = count_occurrences_partial(words, "app", "startswith")
print(result)  # 3

result2 = count_occurrences_partial(words, "ana", "contains")
print(result2)  # 2
```

!!! note "Notes"
    - Multiple match types
    - String-specific operations
    - Flexible matching
    - Configurable behavior

<hr class="snippet-divider">

### Count occurrences with grouping

`list` `count` `group` `function` `categorization` `data-structures`

Count occurrences grouped by a function

```python
def count_occurrences_grouped(lst, group_func=None):
    """Count occurrences grouped by a function."""
    if group_func is None:
        def group_func(x):
            return x


    groups = {}
    for item in lst:
        key = group_func(item)
        if key not in groups:
            groups[key] = 0
        groups[key] += 1

    return groups


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Group by even/odd
def even_odd_group(x):
    return "even" if x % 2 == 0 else "odd"


result = count_occurrences_grouped(numbers, even_odd_group)
print(result)  # {'odd': 5, 'even': 5}


# Group by range
def range_group(x):
    if x <= 3:
        return "low"
    elif x <= 7:
        return "medium"
    else:
        return "high"


result2 = count_occurrences_grouped(numbers, range_group)
print(result2)  # {'low': 3, 'medium': 4, 'high': 3}
```

!!! note "Notes"
    - Custom grouping logic
    - Flexible categorization
    - Dictionary output
    - Multiple grouping strategies

<hr class="snippet-divider">

### Count occurrences with performance monitoring

`list` `count` `performance` `timing` `monitoring` `data-structures`

Count occurrences with performance monitoring

```python
import time


def count_occurrences_with_timing(lst, target, method="count"):
    """Count occurrences with performance monitoring."""
    start_time = time.time()

    if method == "count":
        result = lst.count(target)
    elif method == "loop":
        result = sum(1 for item in lst if item == target)
    elif method == "filter":
        result = len(list(filter(lambda x: x == target, lst)))
    else:
        raise ValueError("Method must be 'count', 'loop', or 'filter'")

    end_time = time.time()

    return {
        "result": result,
        "execution_time": end_time - start_time,
        "list_length": len(lst),
        "method": method,
    }


# Performance comparison
large_list = [i % 100 for i in range(100000)]  # 1000 occurrences of each number 0-99

count_stats = count_occurrences_with_timing(large_list, 42, "count")
loop_stats = count_occurrences_with_timing(large_list, 42, "loop")
filter_stats = count_occurrences_with_timing(large_list, 42, "filter")

print(f"Count method: {count_stats['execution_time']:.6f}s")
print(f"Loop method: {loop_stats['execution_time']:.6f}s")
print(f"Filter method: {filter_stats['execution_time']:.6f}s")
```

!!! note "Notes"
    - Performance measurement
    - Method comparison
    - Benchmarking tool
    - Optimization insights

<hr class="snippet-divider">

### Count occurrences with error handling

`list` `count` `safe` `error` `handling` `data-structures`

Safely count occurrences with error handling

```python
def count_occurrences_safe(lst, target):
    """Safely count occurrences with error handling."""
    try:
        if not isinstance(lst, list):
            raise TypeError("First argument must be a list")

        if lst is None:
            return 0

        return lst.count(target)

    except Exception as e:
        print(f"Error counting occurrences: {e}")
        return 0  # Return 0 on error


# Safe counting with error handling
try:
    result = count_occurrences_safe([1, 2, 3, 2, 4], 2)
    print(result)  # 2
except Exception as e:
    print(f"Error: {e}")
```

!!! note "Notes"
    - Comprehensive error handling
    - Type validation
    - Graceful degradation
    - Production ready

<hr class="snippet-divider">

### Count occurrences with memory optimization

`list` `count` `memory` `optimization` `generator` `data-structures`

Count occurrences using generator for memory efficiency

```python
def count_occurrences_memory_efficient(lst, target):
    """Count occurrences using generator for memory efficiency."""
    return sum(1 for item in lst if item == target)


def count_all_elements_memory_efficient(lst):
    """Count all elements using generator for memory efficiency."""
    from collections import defaultdict

    counts = defaultdict(int)
    for item in lst:
        counts[item] += 1
    return dict(counts)


# Memory efficient counting
large_list = [i % 1000 for i in range(1000000)]

# Count specific element
result = count_occurrences_memory_efficient(large_list, 42)
print(result)  # 1000

# Count all elements
all_counts = count_all_elements_memory_efficient(large_list)
print(len(all_counts))  # 1000 unique elements
```

!!! note "Notes"
    - Memory efficient
    - Generator pattern
    - Suitable for large lists
    - defaultdict optimization

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Flatten List](./list_flatten.md)
- **Reference**: See [📂 Remove Duplicates From List](./list_remove_duplicates.md)
- **Reference**: See [📂 Sort List](./list_sort.md)
- **Reference**: See [📂 Zip List](./list_zip.md)

## 🏷️ Tags

`list`, `count`, `occurrences`, `frequency`, `performance`, `memory`, `data-structures`

## 📝 Notes

- Built-in count method is most efficient for simple counting
- Generators provide memory efficiency for large lists
- Conditional counting enables complex filtering
- Grouping functions enable categorization
- Always validate input for production use
- Consider performance implications for very large lists
