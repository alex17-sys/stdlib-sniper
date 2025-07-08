# Filter List

Zero-dependency Python snippets for filtering lists using the standard library.

## Simple

### 🧩 Filter list with condition

```python
def filter_list(lst, condition_func):
    """Filter list based on condition function."""
    return [item for item in lst if condition_func(item)]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Filter even numbers
def is_even(x):
    return x % 2 == 0


result = filter_list(numbers, is_even)
print(result)  # [2, 4, 6, 8, 10]
```

📂 Filter list based on condition function

🏷️ Tags: list, filter, condition, comprehension, data-structures
📝 Notes:
- Uses list comprehension
- Flexible condition function
- Lambda support
- Simple and efficient

### 🧩 Filter list with built-in filter

```python
def filter_list_builtin(lst, condition_func):
    """Filter list using built-in filter function."""
    return list(filter(condition_func, lst))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter numbers greater than 5
result = filter_list_builtin(numbers, lambda x: x > 5)
print(result)  # [6, 7, 8, 9, 10]
```

📂 Filter list using built-in filter function

🏷️ Tags: list, filter, builtin, function, data-structures
📝 Notes:
- Uses built-in filter
- Returns filter object
- Converts to list
- Functional approach

## Complex

### 🧩 Filter list with multiple conditions

```python
def filter_list_multiple_conditions(lst, conditions):
    """Filter list with multiple conditions (all must be True)."""

    def combined_condition(item):
        return all(condition(item) for condition in conditions)

    return [item for item in lst if combined_condition(item)]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Multiple conditions
def is_even(x):
    return x % 2 == 0


def is_greater_than_3(x):
    return x > 3


def is_less_than_8(x):
    return x < 8


conditions = [is_even, is_greater_than_3, is_less_than_8]
result = filter_list_multiple_conditions(numbers, conditions)
print(result)  # [4, 6]
```

📂 Filter list with multiple conditions (all must be True)

🏷️ Tags: list, filter, multiple, conditions, all, data-structures
📝 Notes:
- Multiple condition functions
- All conditions must be True
- Flexible condition list
- Combined logic

### 🧩 Filter list with any condition

```python
def filter_list_any_condition(lst, conditions):
    """Filter list with multiple conditions (any can be True)."""

    def combined_condition(item):
        return any(condition(item) for condition in conditions)

    return [item for item in lst if combined_condition(item)]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Any condition can be True
def is_even(x):
    return x % 2 == 0


def is_prime(x):
    return x in [2, 3, 5, 7]


conditions = [is_even, is_prime]
result = filter_list_any_condition(numbers, conditions)
print(result)  # [2, 3, 4, 5, 6, 7, 8, 10]
```

📂 Filter list with multiple conditions (any can be True)

🏷️ Tags: list, filter, multiple, conditions, any, data-structures
📝 Notes:
- Multiple condition functions
- Any condition can be True
- OR logic
- Flexible filtering

### 🧩 Filter list with custom logic

```python
def filter_list_custom_logic(lst, logic_func):
    """Filter list with custom logic function."""
    return [item for item in lst if logic_func(item)]


def filter_list_with_context(lst, context_func):
    """Filter list with context-aware function."""
    context = {}
    result = []

    for item in lst:
        should_include, context = context_func(item, context)
        if should_include:
            result.append(item)

    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Custom logic: keep every third number
def every_third(item):
    return item % 3 == 0


result = filter_list_custom_logic(numbers, every_third)
print(result)  # [3, 6, 9]


# Context-aware: keep alternating items
def alternating_filter(item, context):
    context["count"] = context.get("count", 0) + 1
    return context["count"] % 2 == 1, context


result2 = filter_list_with_context(numbers, alternating_filter)
print(result2)  # [1, 3, 5, 7, 9]
```

📂 Filter list with custom logic function

🏷️ Tags: list, filter, custom, logic, context, data-structures
📝 Notes:
- Custom filtering logic
- Context-aware filtering
- Stateful operations
- Complex conditions

### 🧩 Filter list by type

```python
def filter_list_by_type(lst, target_type):
    """Filter list to keep only items of specified type."""
    return [item for item in lst if isinstance(item, target_type)]


def filter_list_by_types(lst, target_types):
    """Filter list to keep items of any specified types."""
    return [item for item in lst if any(isinstance(item, t) for t in target_types)]


mixed_data = [1, "hello", 2.5, True, [1, 2], "world", 3, False]

# Filter by single type
strings = filter_list_by_type(mixed_data, str)
print(strings)  # ['hello', 'world']

# Filter by multiple types
numbers = filter_list_by_types(mixed_data, (int, float))
print(numbers)  # [1, 2.5, 3]
```

📂 Filter list to keep only items of specified type

🏷️ Tags: list, filter, type, isinstance, data-structures
📝 Notes:
- Type-based filtering
- Single or multiple types
- isinstance checking
- Type safety

### 🧩 Filter list with index

```python
def filter_list_with_index(lst, condition_func):
    """Filter list based on condition that includes index."""
    return [item for i, item in enumerate(lst) if condition_func(item, i)]


def filter_list_by_position(lst, position_condition):
    """Filter list based on position condition."""
    return [item for i, item in enumerate(lst) if position_condition(i)]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Filter based on value and position
def value_and_position_condition(item, index):
    return item > 5 and index % 2 == 0


result = filter_list_with_index(numbers, value_and_position_condition)
print(result)  # [7, 9]


# Filter by position only
def even_positions(index):
    return index % 2 == 0


result2 = filter_list_by_position(numbers, even_positions)
print(result2)  # [1, 3, 5, 7, 9]
```

📂 Filter list based on condition that includes index

🏷️ Tags: list, filter, index, position, enumerate, data-structures
📝 Notes:
- Index-aware filtering
- Position-based filtering
- Enumerate usage
- Combined conditions

### 🧩 Filter list with performance monitoring

```python
import time


def filter_list_with_timing(lst, condition_func, method="comprehension"):
    """Filter list with performance monitoring."""
    start_time = time.time()

    if method == "comprehension":
        result = [item for item in lst if condition_func(item)]
    elif method == "builtin":
        result = list(filter(condition_func, lst))
    elif method == "loop":
        result = []
        for item in lst:
            if condition_func(item):
                result.append(item)
    else:
        raise ValueError("Method must be 'comprehension', 'builtin', or 'loop'")

    end_time = time.time()

    return {
        "result": result,
        "execution_time": end_time - start_time,
        "original_length": len(lst),
        "filtered_length": len(result),
        "method": method,
    }


# Performance comparison
large_list = list(range(100000))


def is_even(x):
    return x % 2 == 0


comp_stats = filter_list_with_timing(large_list, is_even, "comprehension")
builtin_stats = filter_list_with_timing(large_list, is_even, "builtin")
loop_stats = filter_list_with_timing(large_list, is_even, "loop")

print(f"Comprehension: {comp_stats['execution_time']:.6f}s")
print(f"Built-in filter: {builtin_stats['execution_time']:.6f}s")
print(f"Loop: {loop_stats['execution_time']:.6f}s")
```

📂 Filter list with performance monitoring

🏷️ Tags: list, filter, performance, timing, monitoring, data-structures
📝 Notes:
- Performance measurement
- Method comparison
- Benchmarking tool
- Optimization insights

### 🧩 Filter list with error handling

```python
def filter_list_safe(lst, condition_func):
    """Safely filter list with error handling."""
    try:
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")

        if not lst:
            return []

        result = []
        for item in lst:
            try:
                if condition_func(item):
                    result.append(item)
            except Exception as e:
                print(f"Error evaluating condition for item {item}: {e}")
                continue

        return result

    except Exception as e:
        print(f"Error filtering list: {e}")
        return []  # Return empty list on error


# Safe filtering with error handling
def risky_condition(x):
    if x == 5:
        raise ValueError("Cannot process 5")
    return x > 3


try:
    result = filter_list_safe([1, 2, 3, 4, 5, 6], risky_condition)
    print(result)  # [4, 6] (5 is skipped due to error)
except Exception as e:
    print(f"Error: {e}")
```

📂 Safely filter list with error handling

🏷️ Tags: list, filter, safe, error, handling, data-structures
📝 Notes:
- Comprehensive error handling
- Type validation
- Graceful degradation
- Production ready

### 🧩 Filter list with memory optimization

```python
def filter_list_generator(lst, condition_func):
    """Filter list using generator for memory efficiency."""
    for item in lst:
        if condition_func(item):
            yield item


def filter_list_memory_efficient(lst, condition_func, threshold=10000):
    """Filter list with memory optimization."""
    # Use generator for large lists
    if len(lst) > threshold:
        return list(filter_list_generator(lst, condition_func))
    else:
        return [item for item in lst if condition_func(item)]


# Memory efficient filtering
large_list = list(range(100000))


def is_even(x):
    return x % 2 == 0


# Generator approach for large lists
count = 0
for item in filter_list_generator(large_list, is_even):
    count += 1
    if count >= 1000:  # Process only first 1000 even numbers
        break

print(f"Processed {count} even numbers")

# Convert to list if needed
result = list(filter_list_generator(large_list[:1000], is_even))
print(len(result))  # 500
```

📂 Filter list using generator for memory efficiency

🏷️ Tags: list, filter, memory, optimization, generator, data-structures
📝 Notes:
- Memory efficient
- Generator pattern
- Suitable for large lists
- Lazy evaluation

### 🧩 Filter list with transformation

```python
def filter_list_with_transform(lst, condition_func, transform_func=None):
    """Filter list and optionally transform filtered items."""
    if transform_func is None:
        def transform_func(x):
            return x

    return [transform_func(item) for item in lst if condition_func(item)]


def filter_list_conditional_transform(
    lst, condition_func, true_transform=None, false_transform=None
):
    """Filter list with conditional transformation."""
    if true_transform is None:
        def true_transform(x):
            return x
    if false_transform is None:
        def false_transform(x):
            return x

    result = []
    for item in lst:
        if condition_func(item):
            result.append(true_transform(item))
        else:
            result.append(false_transform(item))

    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Filter and transform
def is_even(x):
    return x % 2 == 0


def square(x):
    return x**2


result = filter_list_with_transform(numbers, is_even, square)
print(result)  # [4, 16, 36, 64, 100]


# Conditional transform
def is_greater_than_5(x):
    return x > 5


result2 = filter_list_conditional_transform(
    numbers,
    is_greater_than_5,
    true_transform=lambda x: x * 2,  # Double if > 5
    false_transform=lambda x: x // 2,  # Halve if <= 5
)
print(result2)  # [0, 1, 1, 2, 2, 12, 14, 16, 18, 20]
```

📂 Filter list and optionally transform filtered items

🏷️ Tags: list, filter, transform, conditional, data-structures
📝 Notes:
- Combined filter and transform
- Conditional transformation
- Flexible operations
- Efficient processing

## 🔗 Cross-References

- **Reference**: See [📂 Flatten List](./list_flatten.md)
- **Reference**: See [📂 Remove Duplicates From List](./list_remove_duplicates.md)
- **Reference**: See [📂 Sort List](./list_sort.md)
- **Reference**: See [📂 Chunk List](./list_chunk.md)

## 🏷️ Tags

`list`, `filter`, `condition`, `performance`, `memory`, `transform`, `data-structures`

## 📝 Notes

- List comprehension is most efficient for simple filtering
- Generators provide memory efficiency for large lists
- Built-in filter function offers functional approach
- Custom logic enables complex filtering scenarios
- Always validate input for production use
- Consider performance implications for very large lists
