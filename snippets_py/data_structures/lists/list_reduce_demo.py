# 🧩 Reduce list to sum
def reduce_sum(lst):
    """Reduce list to sum using built-in sum."""
    return sum(lst)


def reduce_sum_manual(lst):
    """Reduce list to sum using manual iteration."""
    total = 0
    for item in lst:
        total += item
    return total


numbers = [1, 2, 3, 4, 5]

# Using built-in sum
result1 = reduce_sum(numbers)
print(result1)  # 15

# Using manual iteration
result2 = reduce_sum_manual(numbers)
print(result2)  # 15


# 🧩 Reduce list with custom function
def reduce_list(lst, func, initial=None):
    """Reduce list with custom function using functools.reduce."""
    from functools import reduce

    if initial is not None:
        return reduce(func, lst, initial)
    else:
        return reduce(func, lst)


def reduce_list_manual(lst, func, initial=None):
    """Reduce list with custom function using manual iteration."""
    if not lst:
        return initial

    if initial is None:
        result = lst[0]
        items = lst[1:]
    else:
        result = initial
        items = lst

    for item in items:
        result = func(result, item)

    return result


numbers = [1, 2, 3, 4, 5]


# Multiply all numbers
def multiply(a, b):
    return a * b


result1 = reduce_list(numbers, multiply)
print(result1)  # 120

# Find maximum
result2 = reduce_list(numbers, max)
print(result2)  # 5

# Concatenate strings
words = ["hello", "world", "python"]
result3 = reduce_list(words, lambda x, y: x + " " + y)
print(result3)  # 'hello world python'


# 🧩 Reduce list with conditional logic
def reduce_list(lst, func, initial=None):
    # Function is defined in one of the above code block
    pass


def reduce_conditional(lst, func, condition_func=None, initial=None):
    """Reduce list with conditional logic."""
    if condition_func is None:

        def condition_func(x):
            return True

    filtered = [x for x in lst if condition_func(x)]
    return reduce_list(filtered, func, initial)


def reduce_with_accumulator(lst, func, initial=None):
    """Reduce list with accumulator tracking."""
    if not lst:
        return initial

    if initial is None:
        accumulator = lst[0]
        items = lst[1:]
    else:
        accumulator = initial
        items = lst

    for item in items:
        accumulator = func(accumulator, item)

    return accumulator


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Sum only even numbers
def is_even(x):
    return x % 2 == 0


result1 = reduce_conditional(numbers, lambda x, y: x + y, is_even)
print(result1)  # 30


# Multiply with accumulator tracking
def multiply_with_log(acc, item):
    print(f"Multiplying {acc} by {item}")
    return acc * item


result2 = reduce_with_accumulator(numbers, multiply_with_log)
print(result2)  # 3628800


# 🧩 Reduce list with multiple values
def reduce_multiple_values(lst, func):
    """Reduce list to multiple values."""
    if not lst:
        return None

    result = lst[0]
    for item in lst[1:]:
        result = func(result, item)

    return result


def reduce_to_statistics(lst):
    """Reduce list to basic statistics."""
    if not lst:
        return {"count": 0, "sum": 0, "min": None, "max": None, "avg": 0}

    stats = {
        "count": len(lst),
        "sum": sum(lst),
        "min": min(lst),
        "max": max(lst),
        "avg": sum(lst) / len(lst),
    }

    return stats


def reduce_to_grouped_data(lst, key_func):
    """Reduce list to grouped data."""
    groups = {}
    for item in lst:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)

    return groups


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic statistics
stats = reduce_to_statistics(numbers)
print(stats)  # {'count': 10, 'sum': 55, 'min': 1, 'max': 10, 'avg': 5.5}


# Group by even/odd
def even_odd_key(x):
    return "even" if x % 2 == 0 else "odd"


grouped = reduce_to_grouped_data(numbers, even_odd_key)
print(grouped)  # {'odd': [1, 3, 5, 7, 9], 'even': [2, 4, 6, 8, 10]}


# 🧩 Reduce list with error handling
def reduce_list(lst, func, initial=None):
    # Function is defined in one of the above code block
    pass


def reduce_safe(lst, func, initial=None):
    """Safely reduce list with error handling."""
    try:
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")

        if not lst and initial is None:
            raise ValueError("Cannot reduce empty list without initial value")

        return reduce_list(lst, func, initial)

    except Exception as e:
        print(f"Error in reduce operation: {e}")
        return initial


def reduce_with_validation(lst, func, validator=None, initial=None):
    """Reduce list with input validation."""
    if validator is None:

        def validator(x):
            return True

    valid_items = [x for x in lst if validator(x)]

    if not valid_items and initial is None:
        raise ValueError("No valid items to reduce")

    return reduce_list(valid_items, func, initial)


# Safe reduction with error handling
def risky_func(acc, item):
    if item == 0:
        raise ValueError("Cannot process zero")
    return acc / item


numbers = [10, 2, 0, 3, 4]

try:
    result = reduce_safe(numbers, risky_func, 100)
    print(result)  # 4.166666666666667 (0 is skipped)
except Exception as e:
    print(f"Error: {e}")


# 🧩 Reduce list with generator optimization
def reduce_generator(lst, func, initial=None):
    """Reduce list using generator for memory efficiency."""
    if initial is None:
        if not lst:
            raise ValueError("Cannot reduce empty list without initial value")
        result = lst[0]
        items = (x for x in lst[1:])
    else:
        result = initial
        items = (x for x in lst)

    for item in items:
        result = func(result, item)

    return result


def reduce_lazy(lst, func, initial=None, batch_size=1000):
    """Lazy reduction with batch processing."""
    if initial is None:
        if not lst:
            raise ValueError("Cannot reduce empty list without initial value")
        result = lst[0]
        items = lst[1:]
    else:
        result = initial
        items = lst

    for i in range(0, len(items), batch_size):
        batch = items[i : i + batch_size]
        for item in batch:
            result = func(result, item)

    return result


# Memory efficient reduction
large_list = list(range(100000))

# Generator approach
result1 = reduce_generator(large_list, lambda x, y: x + y)
print(result1)  # 4999950000

# Lazy reduction with batches
result2 = reduce_lazy(large_list, lambda x, y: x + y, batch_size=10000)
print(result2)  # 4999950000


# 🧩 Reduce list with performance monitoring
import time


def reduce_generator(lst, func, initial=None):
    # Function is defined in one of the above code block
    pass


def reduce_list_manual(lst, func, initial=None):
    # Function is defined in one of the above code block
    pass


def reduce_list(lst, func, initial=None):
    # Function is defined in one of the above code block
    pass


def reduce_with_timing(lst, func, method="reduce", initial=None):
    """Reduce list with performance monitoring."""
    start_time = time.time()

    if method == "reduce":
        result = reduce_list(lst, func, initial)
    elif method == "manual":
        result = reduce_list_manual(lst, func, initial)
    elif method == "generator":
        result = reduce_generator(lst, func, initial)
    else:
        raise ValueError("Method must be 'reduce', 'manual', or 'generator'")

    end_time = time.time()

    return {
        "result": result,
        "execution_time": end_time - start_time,
        "list_length": len(lst),
        "method": method,
    }


# Performance comparison
large_list = list(range(100000))


def add(a, b):
    return a + b


reduce_stats = reduce_with_timing(large_list, add, "reduce")
manual_stats = reduce_with_timing(large_list, add, "manual")
generator_stats = reduce_with_timing(large_list, add, "generator")

print(f"Reduce method: {reduce_stats['execution_time']:.6f}s")
print(f"Manual method: {manual_stats['execution_time']:.6f}s")
print(f"Generator method: {generator_stats['execution_time']:.6f}s")


# 🧩 Reduce list with custom data structures
def reduce_objects(lst, attr_name=None, method_name=None, func=None):
    """Reduce list of objects with attribute or method access."""
    if func is None:

        def func(x, y):
            x + y

    if not lst:
        return None

    if attr_name:
        result = getattr(lst[0], attr_name)
        items = [getattr(obj, attr_name) for obj in lst[1:]]
    elif method_name:
        result = getattr(lst[0], method_name)()
        items = [getattr(obj, method_name)() for obj in lst[1:]]
    else:
        result = lst[0]
        items = lst[1:]

    for item in items:
        result = func(result, item)

    return result


def reduce_nested_structures(data, func, max_depth=None):
    """Reduce nested data structures."""

    def reduce_recursive(items, depth=0):
        if max_depth is not None and depth >= max_depth:
            return items

        if isinstance(items, list):
            if not items:
                return None
            result = items[0]
            for item in items[1:]:
                result = func(result, item)
            return result
        elif isinstance(items, dict):
            if not items:
                return {}
            result = {}
            for k, v in items.items():
                if k in result:
                    result[k] = func(result[k], v)
                else:
                    result[k] = v
            return result
        else:
            return items

    return reduce_recursive(data)


# Example class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


people = [Person("Alice", 25), Person("Bob", 30), Person("Charlie", 20)]

# Reduce by age attribute
result1 = reduce_objects(people, attr_name="age", func=lambda x, y: x + y)
print(result1)  # 75

# Reduce by method
result2 = reduce_objects(people, method_name="get_age", func=max)
print(result2)  # 30

# Reduce nested structures
nested_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result3 = reduce_nested_structures(nested_data, lambda x, y: x + y)
print(result3)  # [12, 15, 18]


# 🧩 Reduce list with advanced patterns
def reduce_with_state(lst, func, initial_state=None):
    """Reduce list with state tracking."""
    if not lst:
        return initial_state

    if initial_state is None:
        state = {"result": lst[0], "count": 1, "history": [lst[0]]}
        items = lst[1:]
    else:
        state = initial_state.copy()
        items = lst

    for item in items:
        state = func(state, item)

    return state


def reduce_with_early_termination(lst, func, condition_func, initial=None):
    """Reduce list with early termination condition."""
    if initial is None:
        if not lst:
            return None
        result = lst[0]
        items = lst[1:]
    else:
        result = initial
        items = lst

    for item in items:
        result = func(result, item)
        if condition_func(result):
            break

    return result


# Stateful reduction
def stateful_func(state, item):
    state["result"] += item
    state["count"] += 1
    state["history"].append(item)
    state["average"] = state["result"] / state["count"]
    return state


numbers = [1, 2, 3, 4, 5]

initial_state = {"result": 0, "count": 0, "history": [], "average": 0}
final_state = reduce_with_state(numbers, stateful_func, initial_state)
print(final_state)  # {'result': 15, 'count': 5, 'history': [1, 2, 3, 4, 5], 'average': 3.0}


# Early termination
def early_termination_condition(result):
    return result > 10


result = reduce_with_early_termination(numbers, lambda x, y: x + y, early_termination_condition)
print(result)  # 15 (continues until end)
