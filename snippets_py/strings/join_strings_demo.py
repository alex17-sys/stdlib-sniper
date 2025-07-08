# 🧩 Join list of strings
words = ["Hello", "World", "Python"]
result = " ".join(words)
print(result)  # "Hello World Python"


# 🧩 Join with custom separator
fruits = ["apple", "banana", "orange"]
result = ", ".join(fruits)
print(result)  # "apple, banana, orange"


# 🧩 Join with newlines
lines = ["Line 1", "Line 2", "Line 3"]
result = "\n".join(lines)
print(result)
# Line 1
# Line 2
# Line 3


# 🧩 Join with conditional formatting
def join_with_formatting(items, separator=" ", format_func=None):
    """Join items with optional formatting."""
    if format_func is None:
        return separator.join(str(item) for item in items)

    formatted_items = [format_func(item) for item in items]
    return separator.join(formatted_items)


# Join numbers with formatting
numbers = [1, 2, 3, 4, 5]
result = join_with_formatting(numbers, ", ", lambda x: f"#{x}")
print(result)  # "#1, #2, #3, #4, #5"

# Join with conditional formatting
words = ["hello", "WORLD", "python"]
result = join_with_formatting(words, " ", lambda x: x.title())
print(result)  # "Hello World Python"


# 🧩 Join with filtering
def join_filtered(items, separator=" ", filter_func=None):
    """Join items with optional filtering."""
    if filter_func is None:
        return separator.join(str(item) for item in items)

    filtered_items = [str(item) for item in items if filter_func(item)]
    return separator.join(filtered_items)


# Join only non-empty strings
texts = ["Hello", "", "World", "", "Python"]
result = join_filtered(texts, " ", lambda x: x.strip())
print(result)  # "Hello World Python"

# Join only positive numbers
numbers = [1, -2, 3, -4, 5]
result = join_filtered(numbers, ", ", lambda x: x > 0)
print(result)  # "1, 3, 5"


# 🧩 Join with grouping
def join_grouped(items, group_size, separator=" ", group_separator="\n"):
    """Join items in groups."""
    groups = []
    for i in range(0, len(items), group_size):
        group = items[i : i + group_size]
        groups.append(separator.join(str(item) for item in group))

    return group_separator.join(groups)


# Join numbers in groups of 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = join_grouped(numbers, 3, ", ", "\n")
print(result)
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
