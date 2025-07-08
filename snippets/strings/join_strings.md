# Join Strings

Zero-dependency Python snippets for joining strings using the standard library.

## Simple

### 🧩 Join list of strings

```python
words = ["Hello", "World", "Python"]
result = " ".join(words)
print(result)  # "Hello World Python"
```

📂 Join list of strings with space separator

🏷️ Tags: string, join, list, separator, text
📝 Notes:
- Uses str.join() method
- Efficient for multiple strings
- Flexible separator choice
- Preferred over + operator

### 🧩 Join with custom separator

```python
fruits = ["apple", "banana", "orange"]
result = ", ".join(fruits)
print(result)  # "apple, banana, orange"
```

📂 Join strings with custom delimiter

🏷️ Tags: string, join, delimiter, separator, text
📝 Notes:
- Customizable separator
- Common for CSV-like output
- Handles any separator string
- Clean formatting

### 🧩 Join with newlines

```python
lines = ["Line 1", "Line 2", "Line 3"]
result = "\n".join(lines)
print(result)
# Line 1
# Line 2
# Line 3
```

📂 Join strings with newline separator

🏷️ Tags: string, join, newline, lines, text
📝 Notes:
- Creates multi-line text
- Common for file output
- Platform-independent
- Preserves line structure

## Complex

### 🧩 Join with conditional formatting

```python
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
```

📂 Join items with custom formatting function

🏷️ Tags: string, join, formatting, conditional, function, text
📝 Notes:
- Flexible formatting options
- Custom transformation per item
- Maintains separator control
- Useful for data presentation

### 🧩 Join with filtering

```python
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
```

📂 Join items with filtering conditions

🏷️ Tags: string, join, filter, conditional, text
📝 Notes:
- Filters items before joining
- Removes unwanted elements
- Maintains data integrity
- Clean output generation

### 🧩 Join with grouping

```python
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
```

📂 Join items in grouped format

🏷️ Tags: string, join, group, formatting, text
📝 Notes:
- Organizes items in groups
- Customizable group size
- Separate group separators
- Useful for display formatting

## 🔗 Cross-References

- **Reference**: See [📂 Split String](./split_string.md)
- **Reference**: See [📂 Format String](./format_string.md)

## 🏷️ Tags

`string`, `join`, `list`, `separator`, `delimiter`, `newline`, `formatting`, `filter`, `conditional`, `text`

## 📝 Notes

- Use str.join() for efficient string concatenation
- Custom separators allow for flexible output (CSV, newlines, etc.)
- Filtering and formatting can be combined with joining
- Related: splitting and formatting strings
