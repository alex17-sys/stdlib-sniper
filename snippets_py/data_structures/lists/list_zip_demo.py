# 🧩 Zip two lists
def zip_lists(list1, list2):
    """Zip two lists together."""
    return list(zip(list1, list2))


names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
result = zip_lists(names, ages)
print(result)  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


# 🧩 Zip multiple lists
def zip_multiple_lists(*lists):
    """Zip multiple lists together."""
    return list(zip(*lists))


names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]
result = zip_multiple_lists(names, ages, cities)
print(result)  # [('Alice', 25, 'NYC'), ('Bob', 30, 'LA'), ('Charlie', 35, 'Chicago')]


# 🧩 Zip lists with different lengths
def zip_lists_different_lengths(*lists, fill_value=None):
    """Zip lists with different lengths using fill value."""
    max_length = max(len(lst) for lst in lists)
    padded_lists = []

    for lst in lists:
        # Pad shorter lists with fill value
        padded = lst + [fill_value] * (max_length - len(lst))
        padded_lists.append(padded)

    return list(zip(*padded_lists))


names = ["Alice", "Bob", "Charlie"]
ages = [25, 30]
cities = ["NYC", "LA", "Chicago", "Boston"]
result = zip_lists_different_lengths(names, ages, cities, fill_value="N/A")
print(
    result
)  # [('Alice', 25, 'NYC'), ('Bob', 30, 'LA'), ('Charlie', 'N/A', 'Chicago'), ('N/A', 'N/A', 'Boston')]


# 🧩 Zip lists with custom pairing function
def zip_lists_custom(*lists, pair_func=None):
    """Zip lists with custom pairing function."""
    if pair_func is None:

        def pair_func(*args):
            return args

    zipped = zip(*lists)
    return [pair_func(*pair) for pair in zipped]


names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]


# Custom pairing: create dictionary
def create_person_dict(name, age):
    return {"name": name, "age": age}


result = zip_lists_custom(names, ages, pair_func=create_person_dict)
print(
    result
)  # [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 35}]


# Custom pairing: create formatted string
def format_person(name, age):
    return f"{name} is {age} years old"


result2 = zip_lists_custom(names, ages, pair_func=format_person)
print(result2)  # ['Alice is 25 years old', 'Bob is 30 years old', 'Charlie is 35 years old']


# 🧩 Zip lists with condition
def zip_lists_conditional(*lists, condition_func=None):
    """Zip lists with conditional filtering."""
    if condition_func is None:

        def condition_func(*args):
            True

    zipped = zip(*lists)
    return [pair for pair in zipped if condition_func(*pair)]


names = ["Alice", "Bob", "Charlie", "David"]
ages = [25, 30, 35, 20]
cities = ["NYC", "LA", "Chicago", "Boston"]


# Filter by age > 25
def age_filter(name, age, city):
    return age > 25


result = zip_lists_conditional(names, ages, cities, condition_func=age_filter)
print(result)  # [('Bob', 30, 'LA'), ('Charlie', 35, 'Chicago')]


# Filter by city starting with 'C'
def city_filter(name, age, city):
    return city.startswith("C")


result2 = zip_lists_conditional(names, ages, cities, condition_func=city_filter)
print(result2)  # [('Charlie', 35, 'Chicago')]


# 🧩 Zip lists with index
def zip_lists_with_index(*lists):
    """Zip lists with their indices."""
    return list(enumerate(zip(*lists)))


names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
result = zip_lists_with_index(names, ages)
print(result)  # [(0, ('Alice', 25)), (1, ('Bob', 30)), (2, ('Charlie', 35))]


# Alternative: include index in each tuple
def zip_lists_with_index_inline(*lists):
    """Zip lists with index included in each tuple."""
    return [(i, *pair) for i, pair in enumerate(zip(*lists))]


result2 = zip_lists_with_index_inline(names, ages)
print(result2)  # [(0, 'Alice', 25), (1, 'Bob', 30), (2, 'Charlie', 35)]


# 🧩 Zip lists with generator
def zip_lists_generator(*lists):
    """Zip lists using generator for memory efficiency."""
    return zip(*lists)


names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

# Memory efficient iteration
for name, age, city in zip_lists_generator(names, ages, cities):
    print(f"{name} ({age}) from {city}")

# Convert to list if needed
result = list(zip_lists_generator(names, ages, cities))
print(result)  # [('Alice', 25, 'NYC'), ('Bob', 30, 'LA'), ('Charlie', 35, 'Chicago')]


# 🧩 Zip lists with error handling
# Function is defined in one of the above code block (zip_lists_different_lengths)


def zip_lists_safe(*lists, fill_value=None):
    """Safely zip lists with error handling."""
    try:
        if not lists:
            return []

        # Validate all inputs are lists
        for i, lst in enumerate(lists):
            if not isinstance(lst, list):
                raise TypeError(f"Argument {i} must be a list, got {type(lst).__name__}")

        if fill_value is not None:
            return zip_lists_different_lengths(*lists, fill_value=fill_value)
        else:
            return list(zip(*lists))

    except Exception as e:
        print(f"Error zipping lists: {e}")
        return []  # Return empty list on error


# Safe zipping with error handling
try:
    result = zip_lists_safe(["Alice", "Bob"], [25, 30], fill_value="N/A")
    print(result)  # [('Alice', 25), ('Bob', 30)]
except Exception as e:
    print(f"Error: {e}")


# 🧩 Zip lists with performance monitoring
import time


# Function is defined in one of the above code block (zip_lists_generator)


# Function is defined in one of the above code block (zip_lists_different_lengths)


def zip_lists_with_timing(*lists, method="standard"):
    """Zip lists with performance monitoring."""
    start_time = time.time()

    if method == "standard":
        result = list(zip(*lists))
    elif method == "generator":
        result = list(zip_lists_generator(*lists))
    elif method == "fill_value":
        result = zip_lists_different_lengths(*lists, fill_value=None)
    else:
        raise ValueError("Method must be 'standard', 'generator', or 'fill_value'")

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

std_stats = zip_lists_with_timing(large_list1, large_list2, large_list3, method="standard")
gen_stats = zip_lists_with_timing(large_list1, large_list2, large_list3, method="generator")

print(f"Standard method: {std_stats['execution_time']:.6f}s")
print(f"Generator method: {gen_stats['execution_time']:.6f}s")


# 🧩 Zip lists with custom aggregation
def zip_lists_aggregate(*lists, aggregate_func=None):
    """Zip lists with custom aggregation function."""
    if aggregate_func is None:

        def aggregate_func(*args):
            return args

    zipped = zip(*lists)
    aggregated = []

    for pair in zipped:
        result = aggregate_func(*pair)
        aggregated.append(result)

    return aggregated


numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7, 8]
numbers3 = [9, 10, 11, 12]


# Sum aggregation
def sum_aggregate(a, b, c):
    return a + b + c


result = zip_lists_aggregate(numbers1, numbers2, numbers3, aggregate_func=sum_aggregate)
print(result)  # [15, 18, 21, 24]


# Average aggregation
def avg_aggregate(a, b, c):
    return (a + b + c) / 3


result2 = zip_lists_aggregate(numbers1, numbers2, numbers3, aggregate_func=avg_aggregate)
print(result2)  # [5.0, 6.0, 7.0, 8.0]
