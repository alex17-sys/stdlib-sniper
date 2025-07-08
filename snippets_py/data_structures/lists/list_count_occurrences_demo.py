# 🧩 Count occurrences in list
def count_occurrences(lst, target):
    """Count occurrences of target element in list."""
    return lst.count(target)


numbers = [1, 2, 3, 2, 4, 2, 5]
result = count_occurrences(numbers, 2)
print(result)  # 3


# 🧩 Count all elements in list
def count_all_elements(lst):
    """Count occurrences of all elements in list."""
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return counts


fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
result = count_all_elements(fruits)
print(result)  # {'apple': 3, 'banana': 2, 'cherry': 1}


# 🧩 Count occurrences with condition
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


# 🧩 Count occurrences in nested list
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


# 🧩 Count occurrences with case insensitivity
def count_occurrences_case_insensitive(lst, target):
    """Count occurrences ignoring case for strings."""
    if isinstance(target, str):
        return sum(1 for item in lst if isinstance(item, str) and item.lower() == target.lower())
    else:
        return lst.count(target)


words = ["Apple", "banana", "APPLE", "Cherry", "apple"]
result = count_occurrences_case_insensitive(words, "apple")
print(result)  # 3


# 🧩 Count occurrences with partial matching
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


# 🧩 Count occurrences with grouping
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


# 🧩 Count occurrences with performance monitoring
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


# 🧩 Count occurrences with error handling
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


# 🧩 Count occurrences with memory optimization
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
