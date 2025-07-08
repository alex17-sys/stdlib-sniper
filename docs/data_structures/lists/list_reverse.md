# Reverse List

Zero-dependency Python snippets using only the standard library.

10 snippets available in this sub-category.

---

## Simple

###  Reverse list in place

`list` `reverse` `inplace` `builtin` `data-structures`

Reverse list in place using built-in reverse method

```python
def reverse_list_inplace(lst):
    """Reverse list in place using built-in reverse method."""
    lst.reverse()
    return lst


numbers = [1, 2, 3, 4, 5]
result = reverse_list_inplace(numbers)
print(result)  # [5, 4, 3, 2, 1]
print(numbers)  # [5, 4, 3, 2, 1] (original list modified)
```

!!! note "Notes"
    - Modifies original list
    - Returns reversed list
    - Uses built-in reverse method
    - Efficient for large lists

<hr class="snippet-divider">

### Reverse list with new list

`list` `reverse` `new` `slice` `data-structures`

Reverse list and return new reversed list

```python
def reverse_list_new(lst):
    """Reverse list and return new reversed list."""
    return lst[::-1]


numbers = [1, 2, 3, 4, 5]
result = reverse_list_new(numbers)
print(result)  # [5, 4, 3, 2, 1]
print(numbers)  # [1, 2, 3, 4, 5] (original list unchanged)
```

!!! note "Notes"
    - Creates new list
    - Preserves original list
    - Uses slice notation
    - Functional programming style

<hr class="snippet-divider">

## Complex

###  Reverse list with custom step

`list` `reverse` `step` `custom` `data-structures`

Reverse list with custom step size

```python
def reverse_list_with_step(lst, step=1):
    """Reverse list with custom step size."""
    if step == 1:
        return lst[::-1]
    elif step > 1:
        # Reverse every nth element
        result = []
        for i in range(0, len(lst), step):
            chunk = lst[i : i + step]
            result.extend(chunk[::-1])
        return result
    else:
        return lst


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = reverse_list_with_step(numbers, 2)
print(result)  # [2, 1, 4, 3, 6, 5, 8, 7]

result2 = reverse_list_with_step(numbers, 3)
print(result2)  # [3, 2, 1, 6, 5, 4, 8, 7]
```

!!! note "Notes"
    - Configurable step size
    - Chunk-based reversal
    - Preserves original list
    - Advanced reversal patterns

<hr class="snippet-divider">

### Reverse list partially

`list` `reverse` `partial` `slice` `data-structures`

Reverse a portion of the list

```python
def reverse_list_partial(lst, start=None, end=None):
    """Reverse a portion of the list."""
    if start is None:
        start = 0
    if end is None:
        end = len(lst)

    # Create a copy to avoid modifying original
    result = lst.copy()
    # Reverse the specified portion
    result[start:end] = result[start:end][::-1]
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = reverse_list_partial(numbers, 2, 6)
print(result)  # [1, 2, 6, 5, 4, 3, 7, 8]

# Reverse first half
result2 = reverse_list_partial(numbers, 0, 4)
print(result2)  # [4, 3, 2, 1, 5, 6, 7, 8]
```

!!! note "Notes"
    - Selective reversal
    - Configurable range
    - Preserves original list
    - Useful for specific operations

<hr class="snippet-divider">

### Reverse list with condition

`list` `reverse` `conditional` `filter` `data-structures`

Reverse list elements based on condition

```python
def reverse_list_conditional(lst, condition_func):
    """Reverse list elements that meet a condition."""
    result = []
    for item in lst:
        if condition_func(item):
            result.insert(0, item)  # Add to beginning (reverse order)
        else:
            result.append(item)  # Add to end (normal order)
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Reverse even numbers
result = reverse_list_conditional(numbers, lambda x: x % 2 == 0)
print(result)  # [8, 6, 4, 2, 1, 3, 5, 7]

# Reverse numbers greater than 4
result2 = reverse_list_conditional(numbers, lambda x: x > 4)
print(result2)  # [8, 7, 6, 5, 1, 2, 3, 4]
```

!!! note "Notes"
    - Conditional reversal
    - Flexible filtering
    - Preserves non-matching elements
    - Complex reversal logic

<hr class="snippet-divider">

### Reverse list with grouping

`list` `reverse` `groups` `chunk` `data-structures`

Reverse list by groups

```python
def reverse_list_groups(lst, group_size):
    """Reverse list by groups of specified size."""
    result = []
    for i in range(0, len(lst), group_size):
        group = lst[i : i + group_size]
        result.extend(group[::-1])
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = reverse_list_groups(numbers, 3)
print(result)  # [3, 2, 1, 6, 5, 4, 9, 8, 7]

# Group by 2
result2 = reverse_list_groups(numbers, 2)
print(result2)  # [2, 1, 4, 3, 6, 5, 8, 7, 9]
```

!!! note "Notes"
    - Group-based reversal
    - Configurable group size
    - Handles incomplete groups
    - Useful for data processing

<hr class="snippet-divider">

### Reverse list with recursion

`list` `reverse` `recursive` `tail` `data-structures`

Reverse list using recursion

```python
def reverse_list_recursive(lst):
    """Reverse list using recursion."""
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + reverse_list_recursive(lst[:-1])


numbers = [1, 2, 3, 4, 5]
result = reverse_list_recursive(numbers)
print(result)  # [5, 4, 3, 2, 1]


# Tail-recursive version (more efficient)
def reverse_list_tail_recursive(lst, acc=None):
    """Reverse list using tail recursion."""
    if acc is None:
        acc = []
    if not lst:
        return acc
    return reverse_list_tail_recursive(lst[:-1], acc + [lst[-1]])


result2 = reverse_list_tail_recursive(numbers)
print(result2)  # [5, 4, 3, 2, 1]
```

!!! note "Notes"
    - Recursive approach
    - Educational value
    - Tail recursion optimization
    - Functional programming style

<hr class="snippet-divider">

### Reverse list with generator

`list` `reverse` `generator` `memory` `optimization` `data-structures`

Reverse list using generator

```python
def reverse_list_generator(lst):
    """Reverse list using generator for memory efficiency."""
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]


numbers = [1, 2, 3, 4, 5]
result = list(reverse_list_generator(numbers))
print(result)  # [5, 4, 3, 2, 1]

# Memory efficient iteration
for item in reverse_list_generator(numbers):
    print(item, end=" ")  # 5 4 3 2 1
```

!!! note "Notes"
    - Memory efficient
    - Lazy evaluation
    - Suitable for large lists
    - Generator pattern

<hr class="snippet-divider">

### Reverse list with performance monitoring

`list` `reverse` `performance` `timing` `monitoring` `data-structures`

Reverse list with performance monitoring

```python
import time


def reverse_list_generator(lst):
    # Function is defined in one of the above code block
    pass


def reverse_list_with_timing(lst, method="slice"):
    """Reverse list with performance monitoring."""
    start_time = time.time()

    if method == "slice":
        result = lst[::-1]
    elif method == "reverse":
        lst_copy = lst.copy()
        lst_copy.reverse()
        result = lst_copy
    elif method == "generator":
        result = list(reverse_list_generator(lst))
    else:
        raise ValueError("Method must be 'slice', 'reverse', or 'generator'")

    end_time = time.time()

    return {
        "result": result,
        "execution_time": end_time - start_time,
        "list_length": len(lst),
        "method": method,
    }


# Performance comparison
large_list = list(range(100000))

slice_stats = reverse_list_with_timing(large_list, "slice")
reverse_stats = reverse_list_with_timing(large_list, "reverse")
generator_stats = reverse_list_with_timing(large_list, "generator")

print(f"Slice method: {slice_stats['execution_time']:.6f}s")
print(f"Reverse method: {reverse_stats['execution_time']:.6f}s")
print(f"Generator method: {generator_stats['execution_time']:.6f}s")
```

!!! note "Notes"
    - Performance measurement
    - Method comparison
    - Benchmarking tool
    - Optimization insights

<hr class="snippet-divider">

### Reverse list with error handling

`list` `reverse` `safe` `error` `handling` `data-structures`

Safely reverse list with error handling

```python
def reverse_list_safe(lst, inplace=False):
    """Safely reverse list with error handling."""
    try:
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")

        if not lst:
            return []

        if inplace:
            lst.reverse()
            return lst
        else:
            return lst[::-1]

    except Exception as e:
        print(f"Error reversing list: {e}")
        return lst  # Return original list on error


# Safe reversal with error handling
try:
    result = reverse_list_safe([1, 2, 3, 4, 5])
    print(result)  # [5, 4, 3, 2, 1]
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
- **Reference**: See [📂 Remove Duplicates From List](./list_remove_duplicates.md)
- **Reference**: See [📂 Sort List](./list_sort.md)

## 🏷️ Tags

`list`, `reverse`, `inplace`, `slice`, `recursion`, `generator`, `performance`, `data-structures`

## 📝 Notes

- In-place reversal modifies the original list
- Slice notation creates a new list and preserves the original
- Recursive approaches are educational but less efficient
- Generators provide memory efficiency for large lists
- Consider performance implications for very large lists
- Partial reversal is useful for specific data processing needs
