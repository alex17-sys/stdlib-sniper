# 🧩 Flatten nested list
def flatten_list(nested_list):
    """Flatten a nested list into a single-level list."""
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened


nested = [1, [2, 3], [4, [5, 6]], 7]
result = flatten_list(nested)
print(result)  # [1, 2, 3, 4, 5, 6, 7]


# 🧩 Flatten list with list comprehension
def flatten_list_comprehension(nested_list):
    """Flatten nested list using list comprehension."""
    return [
        item
        for sublist in nested_list
        for item in (
            flatten_list_comprehension(sublist) if isinstance(sublist, list) else [sublist]
        )
    ]


nested = [[1, 2], [3, [4, 5]], 6]
result = flatten_list_comprehension(nested)
print(result)  # [1, 2, 3, 4, 5, 6]


# 🧩 Flatten list with depth limit
def flatten_list_with_depth(nested_list, max_depth=None, current_depth=0):
    """Flatten nested list with optional depth limit."""
    if max_depth is not None and current_depth >= max_depth:
        return nested_list

    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list_with_depth(item, max_depth, current_depth + 1))
        else:
            flattened.append(item)
    return flattened


nested = [1, [2, [3, [4, 5]]], 6]
result = flatten_list_with_depth(nested, max_depth=2)
print(result)  # [1, 2, 3, [4, 5], 6]


# 🧩 Flatten list with type filtering
def flatten_list_with_filter(nested_list, filter_type=None):
    """Flatten nested list with optional type filtering."""
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list_with_filter(item, filter_type))
        elif filter_type is None or isinstance(item, filter_type):
            flattened.append(item)
    return flattened


nested = [1, [2, "hello", 3], [4, [5, 6.5]], "world"]
result = flatten_list_with_filter(nested, int)
print(result)  # [1, 2, 3, 4, 5]


# 🧩 Flatten list with custom flattening rules
def flatten_list_custom(nested_list, flatten_func=None):
    """Flatten nested list with custom flattening function."""
    if flatten_func is None:

        def flatten_func(x):
            return isinstance(x, list)

    flattened = []
    for item in nested_list:
        if flatten_func(item):
            flattened.extend(flatten_list_custom(item, flatten_func))
        else:
            flattened.append(item)
    return flattened


# Flatten only lists with even numbers
def should_flatten_even(item):
    return isinstance(item, list) and all(isinstance(x, int) and x % 2 == 0 for x in item)


nested = [1, [2, 4, [6, 8]], [3, 5], [10, 12]]
result = flatten_list_custom(nested, should_flatten_even)
print(result)  # [1, 2, 4, 6, 8, [3, 5], 10, 12]


# 🧩 Flatten list with position tracking
def flatten_list_with_positions(nested_list):
    """Flatten nested list while tracking original positions."""
    flattened = []
    positions = []

    def flatten_with_path(items, path=[]):
        for i, item in enumerate(items):
            current_path = path + [i]
            if isinstance(item, list):
                flatten_with_path(item, current_path)
            else:
                flattened.append(item)
                positions.append(current_path)

    flatten_with_path(nested_list)
    return flattened, positions


nested = [1, [2, 3], [4, [5, 6]]]
result, positions = flatten_list_with_positions(nested)
print(result)  # [1, 2, 3, 4, 5, 6]
print(positions)  # [[0], [1, 0], [1, 1], [2, 0], [2, 1, 0], [2, 1, 1]]


# 🧩 Flatten list with memory optimization
def flatten_list_generator(nested_list):
    """Flatten nested list using generator for memory efficiency."""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list_generator(item)
        else:
            yield item


nested = [1, [2, [3, 4]], 5]
result = list(flatten_list_generator(nested))
print(result)  # [1, 2, 3, 4, 5]

# Memory efficient iteration
for item in flatten_list_generator(nested):
    print(item, end=" ")  # 1 2 3 4 5


# 🧩 Flatten list with error handling
def flatten_list_safe(nested_list, max_recursion=1000):
    """Safely flatten nested list with error handling."""

    def flatten_recursive(items, depth=0):
        if depth > max_recursion:
            raise RecursionError("Maximum recursion depth exceeded")

        try:
            flattened = []
            for item in items:
                if isinstance(item, list):
                    flattened.extend(flatten_recursive(item, depth + 1))
                else:
                    flattened.append(item)
            return flattened
        except Exception as e:
            raise ValueError(f"Error flattening list: {e}")

    return flatten_recursive(nested_list)


# Safe flattening with error handling
try:
    result = flatten_list_safe([1, [2, 3], [4, 5]])
    print(result)  # [1, 2, 3, 4, 5]
except (RecursionError, ValueError) as e:
    print(f"Error: {e}")


# 🧩 Flatten list with performance monitoring
import time


def flatten_list(nested_list):
    # Function is defined in one of the above code block
    pass


def flatten_list_with_timing(nested_list):
    """Flatten nested list with performance monitoring."""
    start_time = time.time()

    def count_elements(items):
        count = 0
        for item in items:
            if isinstance(item, list):
                count += count_elements(item)
            else:
                count += 1
        return count

    total_elements = count_elements(nested_list)
    result = flatten_list(nested_list)
    end_time = time.time()

    return {
        "result": result,
        "execution_time": end_time - start_time,
        "total_elements": total_elements,
        "original_depth": max(len(str(nested_list).split("[")) - 1, 1),
    }


nested = [1, [2, [3, 4]], [5, 6, [7, 8, 9]]]
stats = flatten_list_with_timing(nested)
print(f"Result: {stats['result']}")
print(f"Time: {stats['execution_time']:.6f}s")
print(f"Elements: {stats['total_elements']}")
print(f"Max Depth: {stats['original_depth']}")
