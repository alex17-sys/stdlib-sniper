# Sort List

Zero-dependency Python snippets using only the standard library.

10 snippets available in this sub-category.

---

## Simple

###  Sort list in place

`list` `sort` `inplace` `builtin` `data-structures`

Sort list in place using built-in sort method

```python
def sort_list_inplace(lst):
    """Sort list in place using built-in sort method."""
    lst.sort()
    return lst


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = sort_list_inplace(numbers)
print(result)  # [1, 1, 2, 3, 4, 5, 6, 9]
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9] (original list modified)
```

!!! note "Notes"
    - Modifies original list
    - Returns sorted list
    - Uses built-in sort method
    - Efficient for large lists

<hr class="snippet-divider">

### Sort list with new list

`list` `sort` `new` `sorted` `data-structures`

Sort list and return new sorted list

```python
def sort_list_new(lst):
    """Sort list and return new sorted list."""
    return sorted(lst)


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = sort_list_new(numbers)
print(result)  # [1, 1, 2, 3, 4, 5, 6, 9]
print(numbers)  # [3, 1, 4, 1, 5, 9, 2, 6] (original list unchanged)
```

!!! note "Notes"
    - Creates new list
    - Preserves original list
    - Uses built-in sorted function
    - Functional programming style

<hr class="snippet-divider">

## Complex

###  Sort list in reverse order

`list` `sort` `reverse` `order` `data-structures`

Sort list in reverse order

```python
def sort_list_reverse(lst, reverse=True):
    """Sort list in reverse order."""
    return sorted(lst, reverse=reverse)


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = sort_list_reverse(numbers)
print(result)  # [9, 6, 5, 4, 3, 2, 1, 1]


# Also works with in-place sorting
def sort_list_inplace_reverse(lst, reverse=True):
    """Sort list in place in reverse order."""
    lst.sort(reverse=reverse)
    return lst


sort_list_inplace_reverse(numbers)
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]
```

!!! note "Notes"
    - Descending order sorting
    - Configurable reverse parameter
    - Works with both sorted() and sort()
    - Common sorting requirement

<hr class="snippet-divider">

### Sort list with custom key function

`list` `sort` `key` `function` `custom` `data-structures`

Sort list using custom key function

```python
def sort_list_by_key(lst, key_func=None):
    """Sort list using custom key function."""
    return sorted(lst, key=key_func)


# Sort by length
words = ["cat", "dog", "elephant", "ant", "bird"]
result = sort_list_by_key(words, len)
print(result)  # ['cat', 'dog', 'ant', 'bird', 'elephant']

# Sort by last character
result2 = sort_list_by_key(words, lambda x: x[-1])
print(result2)  # ['bird', 'dog', 'ant', 'cat', 'elephant']

# Sort by multiple criteria (length, then alphabetically)
result3 = sort_list_by_key(words, lambda x: (len(x), x))
print(result3)  # ['ant', 'cat', 'dog', 'bird', 'elephant']
```

!!! note "Notes"
    - Flexible sorting criteria
    - Multiple sorting keys
    - Lambda functions supported
    - Complex sorting logic

<hr class="snippet-divider">

### Sort list of dictionaries

`list` `sort` `dictionary` `field` `data-structures`

Sort list of dictionaries by field

```python
def sort_list_of_dicts(lst, key_field, reverse=False):
    """Sort list of dictionaries by specified field."""
    return sorted(lst, key=lambda x: x.get(key_field), reverse=reverse)


people = [
    {"name": "Alice", "age": 25, "city": "NYC"},
    {"name": "Bob", "age": 30, "city": "LA"},
    {"name": "Charlie", "age": 20, "city": "Chicago"},
]

# Sort by age
result = sort_list_of_dicts(people, "age")
print(
    result
)  # [{'name': 'Charlie', 'age': 20, 'city': 'Chicago'}, {'name': 'Alice', 'age': 25, 'city': 'NYC'}, {'name': 'Bob', 'age': 30, 'city': 'LA'}]

# Sort by name
result2 = sort_list_of_dicts(people, "name")
print(
    result2
)  # [{'name': 'Alice', 'age': 25, 'city': 'NYC'}, {'name': 'Bob', 'age': 30, 'city': 'LA'}, {'name': 'Charlie', 'age': 20, 'city': 'Chicago'}]
```

!!! note "Notes"
    - Works with complex objects
    - Field-based sorting
    - Safe field access
    - Common data processing

<hr class="snippet-divider">

### Sort list with multiple criteria

`list` `sort` `multiple` `criteria` `data-structures`

Sort list using multiple criteria

```python
def sort_list_multiple_criteria(lst, criteria):
    """Sort list using multiple criteria."""

    def key_function(item):
        return tuple(criterion(item) for criterion in criteria)

    return sorted(lst, key=key_function)


# Sort by length, then by first letter
words = ["cat", "dog", "elephant", "ant", "bird", "apple"]
criteria = [len, lambda x: x[0]]
result = sort_list_multiple_criteria(words, criteria)
print(result)  # ['ant', 'cat', 'dog', 'apple', 'bird', 'elephant']

# Sort people by age (descending), then by name (ascending)
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 30}]
criteria = [lambda x: -x["age"], lambda x: x["name"]]  # Negative for descending
result2 = sort_list_multiple_criteria(people, criteria)
print(
    result2
)  # [{'name': 'Charlie', 'age': 30}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 25}]
```

!!! note "Notes"
    - Complex sorting logic
    - Priority-based sorting
    - Flexible criteria combination
    - Advanced sorting needs

<hr class="snippet-divider">

### Sort list with natural sorting

`list` `sort` `natural` `numbers` `string` `data-structures`

Sort list using natural sorting

```python
import re


def natural_sort_key(text):
    """Generate key for natural sorting of strings with numbers."""

    def atoi(text):
        return int(text) if text.isdigit() else text

    return [atoi(c) for c in re.split(r"(\d+)", text)]


def sort_list_natural(lst):
    """Sort list using natural sorting (handles numbers in strings)."""
    return sorted(lst, key=natural_sort_key)


# Natural sorting example
files = ["file1.txt", "file10.txt", "file2.txt", "file20.txt"]
result = sort_list_natural(files)
print(result)  # ['file1.txt', 'file2.txt', 'file10.txt', 'file20.txt']

# Without natural sorting
print(sorted(files))  # ['file1.txt', 'file10.txt', 'file2.txt', 'file20.txt']
```

!!! note "Notes"
    - Handles numbers in strings
    - Human-readable ordering
    - Useful for file names
    - Complex string parsing

<hr class="snippet-divider">

### Sort list with stability preservation

`list` `sort` `stable` `preservation` `data-structures`

Sort list with stable sorting

```python
def sort_list_stable(lst, primary_key, secondary_key):
    """Sort list with stable sorting (preserves relative order)."""
    # Sort by secondary key first (stable)
    temp = sorted(lst, key=secondary_key)
    # Then sort by primary key (stable)
    return sorted(temp, key=primary_key)


# Example: Sort by grade (primary), then by name (secondary)
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "David", "grade": "B"},
]

result = sort_list_stable(students, lambda x: x["grade"], lambda x: x["name"])
print(
    result
)  # [{'name': 'Alice', 'grade': 'A'}, {'name': 'Charlie', 'grade': 'A'}, {'name': 'Bob', 'grade': 'B'}, {'name': 'David', 'grade': 'B'}]
```

!!! note "Notes"
    - Preserves relative order
    - Multiple sorting passes
    - Predictable results
    - Important for complex sorting

<hr class="snippet-divider">

### Sort list with performance optimization

`list` `sort` `performance` `timing` `monitoring` `data-structures`

Sort list with performance monitoring

```python
import time


def sort_list_with_timing(lst, method="sorted"):
    """Sort list with performance monitoring."""
    start_time = time.time()

    if method == "sorted":
        result = sorted(lst)
    elif method == "sort":
        lst_copy = lst.copy()
        lst_copy.sort()
        result = lst_copy
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
large_list = list(range(10000, 0, -1))  # Reverse order

sorted_stats = sort_list_with_timing(large_list, "sorted")
sort_stats = sort_list_with_timing(large_list, "sort")

print(f"Sorted method: {sorted_stats['execution_time']:.6f}s")
print(f"Sort method: {sort_stats['execution_time']:.6f}s")
```

!!! note "Notes"
    - Performance measurement
    - Method comparison
    - Benchmarking tool
    - Optimization insights

<hr class="snippet-divider">

### Sort list with error handling

`list` `sort` `safe` `error` `handling` `data-structures`

Safely sort list with error handling

```python
def sort_list_safe(lst, key_func=None, reverse=False):
    """Safely sort list with error handling."""
    try:
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")

        if not lst:
            return []

        # Handle non-comparable items
        if key_func is None:
            # Check if all items are comparable
            try:
                return sorted(lst, reverse=reverse)
            except TypeError:
                # Fall back to string representation
                return sorted(lst, key=str, reverse=reverse)
        else:
            return sorted(lst, key=key_func, reverse=reverse)

    except Exception as e:
        print(f"Error sorting list: {e}")
        return lst  # Return original list on error


# Safe sorting with mixed types
mixed_list = [1, "hello", 3.14, "world"]
result = sort_list_safe(mixed_list)
print(result)  # [1, 3.14, 'hello', 'world']
```

!!! note "Notes"
    - Comprehensive error handling
    - Type validation
    - Graceful degradation
    - Production ready

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Flatten List](./list_flatten.md)
- **Reference**: See [📂 Remove Duplicates From List](./list_remove_duplicates.md)
- **Reference**: See [📂 Sort List](./list_filter.md)

## 🏷️ Tags

`list`, `sort`, `inplace`, `sorted`, `key`, `reverse`, `performance`, `data-structures`

## 📝 Notes

- In-place sorting modifies the original list
- sorted() creates a new list and preserves the original
- Custom key functions enable complex sorting logic
- Natural sorting is useful for human-readable ordering
- Stable sorting preserves relative order of equal elements
- Consider performance implications for large lists
