# 🧩 Merge two lists
def merge_lists(list1, list2):
    """Merge two lists together."""
    return list1 + list2


list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = merge_lists(list1, list2)
print(result)  # [1, 2, 3, 4, 5, 6]


# 🧩 Merge multiple lists
def merge_multiple_lists(*lists):
    """Merge multiple lists together."""
    result = []
    for lst in lists:
        result.extend(lst)
    return result


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
result = merge_multiple_lists(list1, list2, list3)
print(result)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 🧩 Merge lists with deduplication
def merge_lists_unique(*lists):
    """Merge lists and remove duplicates while preserving order."""
    seen = set()
    result = []

    for lst in lists:
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)

    return result


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [5, 6, 7, 8]
result = merge_lists_unique(list1, list2, list3)
print(result)  # [1, 2, 3, 4, 5, 6, 7, 8]


# 🧩 Merge lists with custom merge function
def merge_multiple_lists(*lists):
    # Function is defined in one of the above code block
    pass


def merge_lists_custom(*lists, merge_func=None):
    """Merge lists using custom merge function."""
    if merge_func is None:

        def merge_func(x, y):
            return x + y

    # Find the longest list length
    max_length = max(len(lst) for lst in lists) if lists else 0

    result = []
    for i in range(max_length):
        # Collect elements at current index from all lists
        elements = []
        for lst in lists:
            if i < len(lst):
                elements.append(lst[i])

        # Apply merge function
        if elements:
            merged = elements[0]
            for element in elements[1:]:
                merged = merge_func(merged, element)
            result.append(merged)

    return result


# Merge by taking maximum at each position
def max_merge(a, b):
    return max(a, b)


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
list3 = [0, 9, 1, 2]

result = merge_lists_custom(list1, list2, list3, merge_func=max_merge)
print(result)  # [2, 9, 6, 8]


# 🧩 Merge lists with condition
def merge_lists_conditional(*lists, condition_func=None):
    """Merge lists with conditional filtering."""
    if condition_func is None:

        def condition_func(x):
            return True

    result = []
    for lst in lists:
        for item in lst:
            if condition_func(item):
                result.append(item)

    return result


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [11, 12, 13, 14, 15]


# Merge only even numbers
def is_even(x):
    return x % 2 == 0


result = merge_lists_conditional(list1, list2, list3, condition_func=is_even)
print(result)  # [2, 4, 6, 8, 10, 12, 14]


# 🧩 Merge lists with sorting
def merge_multiple_lists(*lists):
    # Function is defined in one of the above code block
    pass


def merge_lists_sorted(*lists, reverse=False):
    """Merge lists and sort the result."""
    merged = merge_multiple_lists(*lists)
    return sorted(merged, reverse=reverse)


list1 = [3, 1, 4]
list2 = [1, 5, 9]
list3 = [2, 6, 5]

result = merge_lists_sorted(list1, list2, list3)
print(result)  # [1, 1, 2, 3, 4, 5, 5, 6, 9]

result_desc = merge_lists_sorted(list1, list2, list3, reverse=True)
print(result_desc)  # [9, 6, 5, 5, 4, 3, 2, 1, 1]


# 🧩 Merge lists with interleaving
def merge_lists_interleaved(*lists):
    """Merge lists by interleaving elements."""
    result = []
    max_length = max(len(lst) for lst in lists) if lists else 0

    for i in range(max_length):
        for lst in lists:
            if i < len(lst):
                result.append(lst[i])

    return result


list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list3 = [True, False, True]

result = merge_lists_interleaved(list1, list2, list3)
print(result)  # [1, 'a', True, 2, 'b', False, 3, 'c', True]


# 🧩 Merge lists with priority
def merge_lists_priority(*lists, priority_func=None):
    """Merge lists with priority-based ordering."""
    if priority_func is None:

        def priority_func(x):
            return x

    # Flatten all lists with their source information
    all_items = []
    for list_idx, lst in enumerate(lists):
        for item_idx, item in enumerate(lst):
            all_items.append((item, list_idx, item_idx, priority_func(item)))

    # Sort by priority (higher priority first)
    all_items.sort(key=lambda x: x[3], reverse=True)

    # Extract items in priority order
    return [item[0] for item in all_items]


list1 = [1, 2, 3]  # Priority 1
list2 = [4, 5, 6]  # Priority 2
list3 = [7, 8, 9]  # Priority 3


# Priority based on list index (higher index = higher priority)
def list_priority(item_info):
    return item_info[1]  # list_idx


result = merge_lists_priority(list1, list2, list3, priority_func=list_priority)
print(result)  # [7, 8, 9, 4, 5, 6, 1, 2, 3]


# 🧩 Merge lists with performance monitoring
import time


def merge_lists_unique(*lists):
    # Function is defined in one of the above code block
    pass


def merge_multiple_lists(*lists):
    # Function is defined in one of the above code block
    pass


def merge_lists_with_timing(*lists, method="extend"):
    """Merge lists with performance monitoring."""
    start_time = time.time()

    if method == "extend":
        result = merge_multiple_lists(*lists)
    elif method == "concatenate":
        result = []
        for lst in lists:
            result = result + lst
    elif method == "unique":
        result = merge_lists_unique(*lists)
    else:
        raise ValueError("Method must be 'extend', 'concatenate', or 'unique'")

    end_time = time.time()

    return {
        "result": result,
        "execution_time": end_time - start_time,
        "num_lists": len(lists),
        "total_elements": sum(len(lst) for lst in lists),
        "method": method,
    }


# Performance comparison
large_list1 = list(range(10000))
large_list2 = list(range(10000))
large_list3 = list(range(10000))

extend_stats = merge_lists_with_timing(large_list1, large_list2, large_list3, "extend")
concat_stats = merge_lists_with_timing(large_list1, large_list2, large_list3, "concatenate")

print(f"Extend method: {extend_stats['execution_time']:.6f}s")
print(f"Concatenate method: {concat_stats['execution_time']:.6f}s")


# 🧩 Merge lists with error handling
def merge_multiple_lists(*lists):
    # Function is defined in one of the above code block
    pass


def merge_lists_safe(*lists):
    """Safely merge lists with error handling."""
    try:
        if not lists:
            return []

        # Validate all inputs are lists
        for i, lst in enumerate(lists):
            if not isinstance(lst, list):
                raise TypeError(f"Argument {i} must be a list, got {type(lst).__name__}")

        return merge_multiple_lists(*lists)

    except Exception as e:
        print(f"Error merging lists: {e}")
        return []  # Return empty list on error


# Safe merging with error handling
try:
    result = merge_lists_safe([1, 2, 3], [4, 5, 6])
    print(result)  # [1, 2, 3, 4, 5, 6]
except Exception as e:
    print(f"Error: {e}")


# 🧩 Merge lists with memory optimization
def merge_multiple_lists(*lists):
    # Function is defined in one of the above code block
    pass


def merge_lists_generator(*lists):
    """Merge lists using generator for memory efficiency."""
    for lst in lists:
        for item in lst:
            yield item


def merge_lists_memory_efficient(*lists):
    """Merge lists with memory optimization."""
    # Use generator for large lists
    if any(len(lst) > 10000 for lst in lists):
        return list(merge_lists_generator(*lists))
    else:
        return merge_multiple_lists(*lists)


# Memory efficient merging
large_list1 = list(range(50000))
large_list2 = list(range(50000))

# Generator approach for large lists
for item in merge_lists_generator(large_list1, large_list2):
    if item == 1000:  # Process until we find 1000
        break

# Convert to list if needed
result = list(merge_lists_generator(large_list1[:100], large_list2[:100]))
print(len(result))  # 200
