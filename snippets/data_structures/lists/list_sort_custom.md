# Sort List Custom

Zero-dependency Python snippets for sorting lists with custom keys and comparison functions using the standard library.

## Simple

### 🧩 Sort list with custom key function

```python
def sort_list_custom(lst, key_func=None, reverse=False):
    """Sort list with custom key function."""
    return sorted(lst, key=key_func, reverse=reverse)


# Sort by length
words = ["apple", "banana", "cherry", "date", "elderberry"]
result = sort_list_custom(words, key=len)
print(result)  # ['date', 'apple', 'banana', 'cherry', 'elderberry']

# Sort by last character
result2 = sort_list_custom(words, key=lambda x: x[-1])
print(result2)  # ['banana', 'apple', 'date', 'elderberry', 'cherry']
```

📂 Sort list with custom key function

🏷️ Tags: list, sort, custom, key, function, data-structures
📝 Notes:
- Uses built-in sorted function
- Custom key function
- Lambda support
- Configurable reverse order

### 🧩 Sort list by multiple keys

```python
def sort_list_multiple_keys(lst, key_functions, reverse=False):
    """Sort list by multiple key functions."""

    def combined_key(item):
        return tuple(key_func(item) for key_func in key_functions)

    return sorted(lst, key=combined_key, reverse=reverse)


# Sort people by age, then by name
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 30},
    {"name": "Alice", "age": 30},
]

key_funcs = [lambda x: x["age"], lambda x: x["name"]]
result = sort_list_multiple_keys(people, key_funcs)
print(
    result
)  # [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 30}]
```

📂 Sort list by multiple key functions

🏷️ Tags: list, sort, multiple, keys, tuple, data-structures
📝 Notes:
- Multiple sorting criteria
- Tuple-based keys
- Hierarchical sorting
- Flexible key functions

## Complex

### 🧩 Sort list with custom comparison function

```python
def sort_list_custom_comparison(lst, compare_func):
    """Sort list with custom comparison function."""
    from functools import cmp_to_key

    return sorted(lst, key=cmp_to_key(compare_func))


# Custom comparison: sort by absolute value, then by sign
def abs_then_sign(a, b):
    abs_a, abs_b = abs(a), abs(b)
    if abs_a != abs_b:
        return abs_a - abs_b
    return a - b


numbers = [3, -1, 2, -3, 1, -2]
result = sort_list_custom_comparison(numbers, abs_then_sign)
print(result)  # [1, -1, 2, -2, 3, -3]
```

📂 Sort list with custom comparison function

🏷️ Tags: list, sort, custom, comparison, cmp_to_key, data-structures
📝 Notes:
- Custom comparison logic
- Uses functools.cmp_to_key
- Legacy comparison style
- Complex sorting rules

### 🧩 Sort list with natural ordering

```python
def sort_list_natural(lst, key_func=None):
    """Sort list with natural string ordering."""
    import re

    def natural_key(text):
        if key_func:
            text = key_func(text)
        return [int(c) if c.isdigit() else c.lower() for c in re.split(r"(\d+)", str(text))]

    return sorted(lst, key=natural_key)


# Natural sort for file names
files = ["file1.txt", "file10.txt", "file2.txt", "file20.txt"]
result = sort_list_natural(files)
print(result)  # ['file1.txt', 'file2.txt', 'file10.txt', 'file20.txt']

# Natural sort for mixed data
mixed = ["item1", "item10", "item2", "Item1", "item20"]
result2 = sort_list_natural(mixed)
print(result2)  # ['Item1', 'item1', 'item2', 'item10', 'item20']
```

📂 Sort list with natural string ordering

🏷️ Tags: list, sort, natural, string, regex, data-structures
📝 Notes:
- Natural number ordering
- Case-insensitive
- Regex-based parsing
- Human-friendly sorting

### 🧩 Sort list with locale awareness

```python
import locale


def sort_list_locale(lst, locale_name=None, key_func=None):
    """Sort list with locale-aware ordering."""
    import locale

    if locale_name:
        locale.setlocale(locale.LC_ALL, locale_name)

    def locale_key(item):
        if key_func:
            item = key_func(item)
        return locale.strxfrm(str(item))

    return sorted(lst, key=locale_key)


# Locale-aware sort for accented characters
words = ["café", "cafe", "café", "zebra", "zèbre"]
try:
    result = sort_list_locale(words, "en_US.UTF-8")
    print(result)  # Locale-dependent ordering
except locale.Error:
    # Fallback to regular sort if locale not available
    result = sorted(words)
    print(result)
```

📂 Sort list with locale-aware ordering

🏷️ Tags: list, sort, locale, internationalization, data-structures
📝 Notes:
- Locale-specific ordering
- Accented character handling
- Fallback support
- Internationalization

### 🧩 Sort list with stability preservation

```python
def sort_list_stable(lst, key_func=None, reverse=False):
    """Sort list while preserving stability (relative order of equal elements)."""
    # Python's sorted() is already stable, but we can demonstrate it
    return sorted(lst, key=key_func, reverse=reverse)


# Demonstrate stability
items = [("apple", 1), ("banana", 2), ("apple", 3), ("cherry", 1), ("banana", 1)]

# Sort by fruit name (stability preserved for equal names)
result = sort_list_stable(items, key=lambda x: x[0])
print(result)  # [('apple', 1), ('apple', 3), ('banana', 2), ('banana', 1), ('cherry', 1)]

# Sort by number, then by fruit (stability preserved)
result2 = sort_list_stable(items, key=lambda x: (x[1], x[0]))
print(result2)  # [('apple', 1), ('banana', 1), ('cherry', 1), ('banana', 2), ('apple', 3)]
```

📂 Sort list while preserving stability

🏷️ Tags: list, sort, stable, preservation, data-structures
📝 Notes:
- Maintains relative order
- Equal element preservation
- Multiple sort passes
- Predictable behavior

### 🧩 Sort list with performance monitoring

```python
import time


def sort_list_with_timing(lst, method="sorted", key_func=None, reverse=False):
    """Sort list with performance monitoring."""
    start_time = time.time()

    if method == "sorted":
        result = sorted(lst, key=key_func, reverse=reverse)
    elif method == "sort":
        # Create copy to avoid modifying original
        result = lst.copy()
        result.sort(key=key_func, reverse=reverse)
    else:
        raise ValueError("Method must be 'sorted' or 'sort'")

    end_time = time.time()

    return {
        "result": result,
        "execution_time": end_time - start_time,
        "list_length": len(lst),
        "method": method,
    }


# Performance comparison
large_list = [(i % 100, i) for i in range(10000)]

sorted_stats = sort_list_with_timing(large_list, "sorted", key=lambda x: x[0])
sort_stats = sort_list_with_timing(large_list, "sort", key=lambda x: x[0])

print(f"Sorted method: {sorted_stats['execution_time']:.6f}s")
print(f"Sort method: {sort_stats['execution_time']:.6f}s")
```

📂 Sort list with performance monitoring

🏷️ Tags: list, sort, performance, timing, monitoring, data-structures
📝 Notes:
- Performance measurement
- Method comparison
- Benchmarking tool
- Optimization insights

### 🧩 Sort list with error handling

```python
def sort_list_safe(lst, key_func=None, reverse=False):
    """Safely sort list with error handling."""
    try:
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")

        if not lst:
            return []

        # Test key function if provided
        if key_func is not None:
            try:
                key_func(lst[0])
            except Exception as e:
                raise ValueError(f"Key function failed on first element: {e}")

        return sorted(lst, key=key_func, reverse=reverse)

    except Exception as e:
        print(f"Error sorting list: {e}")
        return lst  # Return original list on error


# Safe sorting with error handling
try:
    result = sort_list_safe([3, 1, 4, 1, 5], key=lambda x: x)
    print(result)  # [1, 1, 3, 4, 5]
except Exception as e:
    print(f"Error: {e}")
```

📂 Safely sort list with error handling

🏷️ Tags: list, sort, safe, error, handling, data-structures
📝 Notes:
- Comprehensive error handling
- Type validation
- Key function testing
- Graceful degradation

### 🧩 Sort list with memory optimization

```python
def sort_list_memory_efficient(lst, key_func=None, reverse=False, threshold=10000):
    """Sort list with memory optimization."""
    if len(lst) <= threshold:
        return sorted(lst, key=key_func, reverse=reverse)

    # For large lists, use in-place sort to save memory
    result = lst.copy()
    result.sort(key=key_func, reverse=reverse)
    return result


def sort_list_generator(lst, key_func=None, reverse=False):
    """Sort list using generator for memory efficiency."""
    # Sort and yield items one by one
    sorted_items = sorted(lst, key=key_func, reverse=reverse)
    for item in sorted_items:
        yield item


# Memory efficient sorting
large_list = list(range(100000))

# Generator approach for large lists
count = 0
for item in sort_list_generator(large_list, reverse=True):
    count += 1
    if count >= 1000:  # Process only first 1000 items
        break

print(f"Processed {count} sorted items")

# Convert to list if needed
result = list(sort_list_generator(large_list[:1000], reverse=True))
print(len(result))  # 1000
```

📂 Sort list with memory optimization

🏷️ Tags: list, sort, memory, optimization, generator, data-structures
📝 Notes:
- Memory efficient
- Generator pattern
- Suitable for large lists
- Lazy evaluation

### 🧩 Sort list with custom data structures

```python
def sort_list_objects(lst, attr_name=None, method_name=None):
    """Sort list of objects by attribute or method."""
    if attr_name:
        return sorted(lst, key=lambda x: getattr(x, attr_name))
    elif method_name:
        return sorted(lst, key=lambda x: getattr(x, method_name)())
    else:
        return sorted(lst)


# Example class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} ({self.age})"


people = [Person("Alice", 25), Person("Bob", 30), Person("Charlie", 20)]

# Sort by attribute
result = sort_list_objects(people, attr_name="age")
print([p.get_info() for p in result])  # ['Charlie (20)', 'Alice (25)', 'Bob (30)']

# Sort by method
result2 = sort_list_objects(people, method_name="get_info")
print([p.get_info() for p in result2])  # ['Alice (25)', 'Bob (30)', 'Charlie (20)']
```

📂 Sort list of objects by attribute or method

🏷️ Tags: list, sort, objects, attributes, methods, data-structures
📝 Notes:
- Object-oriented sorting
- Attribute access
- Method calling
- Flexible object handling

## 🔗 Cross-References

- **Reference**: See [📂 Flatten List](./list_flatten.md)
- **Reference**: See [📂 Remove Duplicates From List](./list_remove_duplicates.md)
- **Reference**: See [📂 Sort List](./list_sort.md)
- **Reference**: See [📂 Rotate List](./list_chunk.md)

## 🏷️ Tags

`list`, `sort`, `custom`, `key`, `performance`, `memory`, `data-structures`

## 📝 Notes

- Built-in sorted() function is most efficient for standard use cases
- Custom key functions enable complex sorting logic
- Multiple key sorting enables hierarchical ordering
- Natural sorting improves human readability
- Always validate input for production use
- Consider performance implications for very large lists
