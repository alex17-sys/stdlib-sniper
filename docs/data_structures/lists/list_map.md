---
title: Map List
description: Zero-dependency Python snippets for mapping functions over lists using the standard library.
keywords: attributes, chain, conditional, context, cross-product, data-structures, error, function, functions, generator, handling, index, lazy, list, map, memory, methods, monitoring, multiple, neighbors, nested, objects, optimization, parallel, performance, safe, timing, transform, validation
---

# Map List

Zero-dependency Python snippets for mapping functions over lists using the standard library.

9 snippets available in this sub-category.

---

## Simple

###  Map function over list

`list` `map` `function` `transform` `data-structures`

Map function over list using built-in map

```python
def map_list(lst, func):
    """Map function over list using built-in map."""
    return list(map(func, lst))


def map_list_comprehension(lst, func):
    """Map function over list using list comprehension."""
    return [func(x) for x in lst]


numbers = [1, 2, 3, 4, 5]

# Using built-in map
result1 = map_list(numbers, lambda x: x**2)
print(result1)  # [1, 4, 9, 16, 25]

# Using list comprehension
result2 = map_list_comprehension(numbers, lambda x: x**2)
print(result2)  # [1, 4, 9, 16, 25]
```

!!! note "Notes"
    - Uses built-in map function
    - List comprehension alternative
    - Function application
    - Element-wise transformation

<hr class="snippet-divider">

### Map with multiple functions

`list` `map` `multiple` `functions` `chain` `data-structures`

Map multiple functions over list

```python
def map_multiple_functions(lst, functions):
    """Map multiple functions over list."""
    result = []
    for func in functions:
        mapped = list(map(func, lst))
        result.append(mapped)
    return result


def map_functions_chain(lst, functions):
    """Chain multiple functions over list."""
    result = lst
    for func in functions:
        result = list(map(func, result))
    return result


numbers = [1, 2, 3, 4, 5]

# Multiple functions applied separately
funcs = [lambda x: x**2, lambda x: x + 1, lambda x: x * 2]
result1 = map_multiple_functions(numbers, funcs)
print(result1)  # [[1, 4, 9, 16, 25], [2, 3, 4, 5, 6], [2, 4, 6, 8, 10]]

# Functions chained together
result2 = map_functions_chain(numbers, funcs)
print(result2)  # [2, 8, 18, 32, 50]
```

!!! note "Notes"
    - Multiple function application
    - Function chaining
    - Separate vs combined results
    - Flexible function lists

<hr class="snippet-divider">

## Complex

###  Map with conditional logic

`list` `map` `conditional` `error` `data-structures`

Map function with conditional application

```python
def map_conditional(lst, func, condition_func=None):
    """Map function with conditional application."""
    if condition_func is None:
        def condition_func(x):
            return True

    result = []
    for item in lst:
        if condition_func(item):
            result.append(func(item))
        else:
            result.append(item)

    return result


def map_with_fallback(lst, func, fallback_func=None):
    """Map function with fallback for errors."""
    if fallback_func is None:
        def fallback_func(x):
            return x

    result = []
    for item in lst:
        try:
            result.append(func(item))
        except Exception:
            result.append(fallback_func(item))

    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Conditional mapping
def is_even(x):
    return x % 2 == 0


result1 = map_conditional(numbers, lambda x: x**2, is_even)
print(result1)  # [1, 4, 3, 16, 5, 36, 7, 64, 9, 100]


# Mapping with fallback
def risky_func(x):
    if x == 5:
        raise ValueError("Cannot process 5")
    return x**2


result2 = map_with_fallback(numbers, risky_func, lambda x: x)
print(result2)  # [1, 4, 9, 16, 5, 36, 49, 64, 81, 100]
```

!!! note "Notes"
    - Conditional function application
    - Error handling with fallback
    - Selective transformation
    - Robust mapping

<hr class="snippet-divider">

### Map with index awareness

`list` `map` `index` `neighbors` `context` `data-structures`

Map function with index awareness

```python
def map_with_index(lst, func):
    """Map function with index awareness."""
    return [func(item, i) for i, item in enumerate(lst)]


def map_with_neighbors(lst, func):
    """Map function with access to neighboring elements."""
    result = []
    for i in range(len(lst)):
        prev = lst[i - 1] if i > 0 else None
        curr = lst[i]
        next_item = lst[i + 1] if i < len(lst) - 1 else None
        result.append(func(prev, curr, next_item))
    return result


numbers = [1, 2, 3, 4, 5]

# Map with index
result1 = map_with_index(numbers, lambda x, i: x + i)
print(result1)  # [1, 3, 5, 7, 9]


# Map with neighbors
def neighbor_func(prev, curr, next_item):
    total = curr
    if prev is not None:
        total += prev
    if next_item is not None:
        total += next_item
    return total


result2 = map_with_neighbors(numbers, neighbor_func)
print(result2)  # [3, 6, 9, 12, 9]
```

!!! note "Notes"
    - Index-aware mapping
    - Neighbor access
    - Context-aware functions
    - Position-based logic

<hr class="snippet-divider">

### Map with multiple lists

`list` `map` `multiple` `parallel` `cross-product` `data-structures`

Map function over multiple lists

```python
def map_multiple_lists(*lists, func):
    """Map function over multiple lists."""
    return list(map(func, *lists))


def map_lists_parallel(*lists, func):
    """Map function over lists in parallel."""
    return [func(*items) for items in zip(*lists)]


def map_lists_cross_product(list1, list2, func):
    """Map function over cross product of two lists."""
    return [func(x, y) for x in list1 for y in list2]


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]


# Map over multiple lists
def sum_three(a, b, c):
    return a + b + c


result1 = map_multiple_lists(list1, list2, list3, func=sum_three)
print(result1)  # [12, 15, 18]

# Parallel mapping
result2 = map_lists_parallel(list1, list2, lambda x, y: x * y)
print(result2)  # [4, 10, 18]

# Cross product mapping
result3 = map_lists_cross_product(list1, list2, lambda x, y: x * y)
print(result3)  # [4, 5, 6, 8, 10, 12, 12, 15, 18]
```

!!! note "Notes"
    - Multiple list iteration
    - Parallel processing
    - Cross product operations
    - Flexible function signatures

<hr class="snippet-divider">

### Map with generator optimization

`list` `map` `generator` `memory` `optimization` `lazy` `data-structures`

Map function using generator for memory efficiency

```python
def map_generator(lst, func):
    """Map function using generator for memory efficiency."""
    return (func(x) for x in lst)


def map_lazy(lst, func, batch_size=1000):
    """Lazy mapping with batch processing."""
    for i in range(0, len(lst), batch_size):
        batch = lst[i : i + batch_size]
        for item in batch:
            yield func(item)


def map_memory_efficient(lst, func, threshold=10000):
    """Memory efficient mapping."""
    if len(lst) <= threshold:
        return list(map(func, lst))
    else:
        return map_generator(lst, func)


# Memory efficient mapping
large_list = list(range(100000))

# Generator approach
count = 0
for item in map_generator(large_list, lambda x: x**2):
    count += 1
    if count >= 1000:  # Process only first 1000 items
        break

print(f"Processed {count} items")

# Lazy mapping with batches
batch_count = 0
for item in map_lazy(large_list, lambda x: x**2, batch_size=100):
    batch_count += 1
    if batch_count >= 100:  # Process only first 100 items
        break

print(f"Processed {batch_count} items in batches")
```

!!! note "Notes"
    - Memory efficient
    - Generator pattern
    - Lazy evaluation
    - Batch processing

<hr class="snippet-divider">

### Map with performance monitoring

`list` `map` `performance` `timing` `monitoring` `data-structures`

Map function with performance monitoring

```python
import time


def map_with_timing(lst, func, method="map"):
    """Map function with performance monitoring."""
    start_time = time.time()

    if method == "map":
        result = list(map(func, lst))
    elif method == "comprehension":
        result = [func(x) for x in lst]
    elif method == "loop":
        result = []
        for x in lst:
            result.append(func(x))
    else:
        raise ValueError("Method must be 'map', 'comprehension', or 'loop'")

    end_time = time.time()

    return {
        "result": result,
        "execution_time": end_time - start_time,
        "list_length": len(lst),
        "method": method,
    }


# Performance comparison
large_list = list(range(100000))


def square(x):
    return x**2


map_stats = map_with_timing(large_list, square, "map")
comp_stats = map_with_timing(large_list, square, "comprehension")
loop_stats = map_with_timing(large_list, square, "loop")

print(f"Map method: {map_stats['execution_time']:.6f}s")
print(f"Comprehension method: {comp_stats['execution_time']:.6f}s")
print(f"Loop method: {loop_stats['execution_time']:.6f}s")
```

!!! note "Notes"
    - Performance measurement
    - Method comparison
    - Benchmarking tool
    - Optimization insights

<hr class="snippet-divider">

### Map with error handling

`list` `map` `safe` `error` `handling` `validation` `data-structures`

Safely map function with error handling

```python
def map_safe(lst, func):
    """Safely map function with error handling."""
    try:
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")

        if not lst:
            return []

        result = []
        for item in lst:
            try:
                result.append(func(item))
            except Exception as e:
                print(f"Error processing {item}: {e}")
                result.append(None)  # Use None for failed items

        return result

    except Exception as e:
        print(f"Error in map operation: {e}")
        return []  # Return empty list on error


def map_with_validation(lst, func, validator=None):
    """Map function with input validation."""
    if validator is None:
        def validator(x):
            return True

    result = []
    for item in lst:
        if validator(item):
            result.append(func(item))
        else:
            result.append(None)

    return result


# Safe mapping with error handling
def risky_func(x):
    if x == 0:
        raise ValueError("Cannot process zero")
    return 10 / x


numbers = [1, 2, 0, 3, 4]
result = map_safe(numbers, risky_func)
print(result)  # [10.0, 5.0, None, 3.3333333333333335, 2.5]
```

!!! note "Notes"
    - Comprehensive error handling
    - Input validation
    - Graceful degradation
    - Production ready

<hr class="snippet-divider">

### Map with custom data structures

`list` `map` `objects` `attributes` `methods` `nested` `data-structures`

Map over objects with attribute or method access

```python
def map_objects(lst, attr_name=None, method_name=None, transform_func=None):
    """Map over objects with attribute or method access."""
    if transform_func is None:
        def transform_func(x):
            return x

    result = []
    for obj in lst:
        if attr_name:
            value = getattr(obj, attr_name)
        elif method_name:
            value = getattr(obj, method_name)()
        else:
            value = obj

        result.append(transform_func(value))

    return result


def map_nested_structures(data, func, max_depth=None):
    """Map function over nested data structures."""

    def map_recursive(item, depth=0):
        if max_depth is not None and depth >= max_depth:
            return func(item)

        if isinstance(item, list):
            return [map_recursive(x, depth + 1) for x in item]
        elif isinstance(item, dict):
            return {k: map_recursive(v, depth + 1) for k, v in item.items()}
        else:
            return func(item)

    return map_recursive(data)


# Example class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} ({self.age})"


people = [Person("Alice", 25), Person("Bob", 30), Person("Charlie", 20)]

# Map over object attributes
result1 = map_objects(people, attr_name="age", transform_func=lambda x: x * 2)
print(result1)  # [50, 60, 40]

# Map over object methods
result2 = map_objects(people, method_name="get_info", transform_func=str.upper)
print(result2)  # ['ALICE (25)', 'BOB (30)', 'CHARLIE (20)']

# Map over nested structures
nested_data = [[1, 2, 3], [4, 5, 6], {"a": 7, "b": 8}]
result3 = map_nested_structures(nested_data, lambda x: x * 2)
print(result3)  # [[2, 4, 6], [8, 10, 12], {'a': 14, 'b': 16}]
```

!!! note "Notes"
    - Object-oriented mapping
    - Attribute and method access
    - Nested structure handling
    - Recursive mapping

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Flatten List](./list_flatten.md)
- **Reference**: See [📂 Remove Duplicates From List](./list_remove_duplicates.md)
- **Reference**: See [📂 Sort List](./list_sort.md)

## 🏷️ Tags

`list`, `map`, `function`, `performance`, `memory`, `objects`, `data-structures`

## 📝 Notes

- Built-in map function is efficient for simple transformations
- Generators provide memory efficiency for large lists
- List comprehensions offer readable alternatives
- Error handling ensures robust operation
- Always validate input for production use
- Consider performance implications for very large lists
