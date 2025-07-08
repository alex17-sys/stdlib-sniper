# Check String Starts With

Check if a string starts with a specific prefix using the standard library.

## Simple

### 🧩 Check if string starts with prefix

```python
def starts_with(text, prefix):
    """Check if string starts with prefix."""
    return text.startswith(prefix)


text = "Hello World"
result = starts_with(text, "Hello")
print(result)  # True
```

📂 Check if string starts with a specific prefix

🏷️ Tags: string, startswith, prefix, check, text
📝 Notes:
- Uses str.startswith() method
- Case-sensitive matching
- Returns boolean
- Simple and efficient

### 🧩 Check with case-insensitive matching

```python
def starts_with_ignore_case(text, prefix):
    """Check if string starts with prefix ignoring case."""
    return text.lower().startswith(prefix.lower())


text = "Hello World"
result = starts_with_ignore_case(text, "hello")
print(result)  # True
```

📂 Check string prefix ignoring case differences

🏷️ Tags: string, startswith, prefix, case-insensitive, text
📝 Notes:
- Converts both strings to lowercase
- Handles mixed case text
- Useful for user input matching
- Maintains original text

## Complex

### 🧩 Check multiple prefixes

```python
def starts_with_any(text, prefixes):
    """Check if string starts with any of the prefixes."""
    return text.startswith(tuple(prefixes))


text = "Hello World"
prefixes = ["Hello", "Hi", "Hey"]
result = starts_with_any(text, prefixes)
print(result)  # True
```

📂 Check if string starts with any of multiple prefixes

🏷️ Tags: string, startswith, multiple, prefixes, tuple, text
📝 Notes:
- Uses tuple of prefixes
- Efficient for multiple checks
- Returns True if any match
- Useful for categorization

### 🧩 Check with position offset

```python
def starts_with_at_position(text, prefix, start=0, end=None):
    """Check if string starts with prefix at specific position."""
    return text.startswith(prefix, start, end)


text = "Hello World Python"
result = starts_with_at_position(text, "World", 6)
print(result)  # True
```

📂 Check prefix match at specific position

🏷️ Tags: string, startswith, position, offset, slice, text
📝 Notes:
- Uses start and end parameters
- Checks substring at position
- Useful for parsing
- Flexible position control

### 🧩 Check with regex pattern

```python
import re


def starts_with_pattern(text, pattern):
    """Check if string starts with regex pattern."""
    return bool(re.match(pattern, text))


text = "Hello123World"
result = starts_with_pattern(text, r"Hello\d+")
print(result)  # True
```

📂 Check if string starts with regex pattern

🏷️ Tags: string, startswith, regex, pattern, match, text
📝 Notes:
- Uses re.match() for start anchor
- Supports complex patterns
- More flexible than startswith
- Powerful pattern matching

### 🧩 Check with custom function

```python
def starts_with_custom(text, check_func):
    """Check if string starts with custom condition."""
    if not text:
        return False
    return check_func(text[0])


text = "Hello World"
result = starts_with_custom(text, str.isupper)
print(result)  # True (starts with uppercase)
```

📂 Check string start with custom condition function

🏷️ Tags: string, startswith, custom, function, condition, text
📝 Notes:
- Uses custom check function
- Flexible condition checking
- Useful for validation
- Supports any condition

### 🧩 Check with multiple conditions

```python
def starts_with_conditions(text, conditions):
    """Check if string starts with multiple conditions."""
    if not text:
        return False

    first_char = text[0]
    return all(condition(first_char) for condition in conditions)


text = "Hello World"
conditions = [str.isupper, lambda c: c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
result = starts_with_conditions(text, conditions)
print(result)  # True
```

📂 Check string start with multiple conditions

🏷️ Tags: string, startswith, conditions, multiple, validation, text
📝 Notes:
- Combines multiple checks
- All conditions must pass
- Flexible validation
- Useful for complex rules

## 🔗 Cross-References

- **Reference**: See [📂 Ends With](./ends_with.md)
- **Reference**: See [📂 Find String](./find_string.md)

## 🏷️ Tags

`string`, `startswith`, `prefix`, `validation`, `text`

## 📝 Notes

- Use str.startswith() to check for prefixes
- Supports tuples for multiple prefixes
- Useful for URL, file, and pattern checks
