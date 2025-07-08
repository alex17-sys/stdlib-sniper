# Check String Ends With

Check if a string ends with a specific suffix using the standard library.

## Simple

### 🧩 Check if string ends with suffix

```python
def ends_with(text, suffix):
    """Check if string ends with suffix."""
    return text.endswith(suffix)


text = "Hello World"
result = ends_with(text, "World")
print(result)  # True
```

📂 Check if string ends with a specific suffix

🏷️ Tags: string, endswith, suffix, check, text
📝 Notes:
- Uses str.endswith() method
- Case-sensitive matching
- Returns boolean
- Simple and efficient

### 🧩 Check with case-insensitive matching

```python
def ends_with_ignore_case(text, suffix):
    """Check if string ends with suffix ignoring case."""
    return text.lower().endswith(suffix.lower())


text = "Hello World"
result = ends_with_ignore_case(text, "world")
print(result)  # True
```

📂 Check string suffix ignoring case differences

🏷️ Tags: string, endswith, suffix, case-insensitive, text
📝 Notes:
- Converts both strings to lowercase
- Handles mixed case text
- Useful for user input matching
- Maintains original text

## Complex

### 🧩 Check multiple suffixes

```python
def ends_with_any(text, suffixes):
    """Check if string ends with any of the suffixes."""
    return text.endswith(tuple(suffixes))


text = "Hello World"
suffixes = ["World", "Python", "Java"]
result = ends_with_any(text, suffixes)
print(result)  # True
```

📂 Check if string ends with any of multiple suffixes

🏷️ Tags: string, endswith, multiple, suffixes, tuple, text
📝 Notes:
- Uses tuple of suffixes
- Efficient for multiple checks
- Returns True if any match
- Useful for file extensions

### 🧩 Check with position offset

```python
def ends_with_at_position(text, suffix, start=0, end=None):
    """Check if string ends with suffix at specific position."""
    return text.endswith(suffix, start, end)


text = "Hello World Python"
result = ends_with_at_position(text, "World", 0, 11)
print(result)  # True
```

📂 Check suffix match at specific position

🏷️ Tags: string, endswith, position, offset, slice, text
📝 Notes:
- Uses start and end parameters
- Checks substring at position
- Useful for parsing
- Flexible position control

### 🧩 Check file extensions

```python
def has_file_extension(filename, extensions):
    """Check if filename has specific extension(s)."""
    return filename.lower().endswith(tuple(ext.lower() for ext in extensions))


filename = "document.PDF"
extensions = [".pdf", ".doc", ".txt"]
result = has_file_extension(filename, extensions)
print(result)  # True
```

📂 Check if filename has specific file extension

🏷️ Tags: string, endswith, file, extension, filename, text
📝 Notes:
- Case-insensitive extension check
- Handles multiple extensions
- Useful for file processing
- Common use case

### 🧩 Check with regex pattern

```python
import re


def ends_with_pattern(text, pattern):
    """Check if string ends with regex pattern."""
    return bool(re.search(pattern + "$", text))


text = "Hello123World"
result = ends_with_pattern(text, r"\d+World$")
print(result)  # True
```

📂 Check if string ends with regex pattern

🏷️ Tags: string, endswith, regex, pattern, search, text
📝 Notes:
- Uses re.search() with end anchor
- Supports complex patterns
- More flexible than endswith
- Powerful pattern matching

### 🧩 Check with custom function

```python
def ends_with_custom(text, check_func):
    """Check if string ends with custom condition."""
    if not text:
        return False
    return check_func(text[-1])


text = "Hello World"
result = ends_with_custom(text, str.isalpha)
print(result)  # True (ends with letter)
```

📂 Check string end with custom condition function

🏷️ Tags: string, endswith, custom, function, condition, text
📝 Notes:
- Uses custom check function
- Flexible condition checking
- Useful for validation
- Supports any condition

### 🧩 Check with multiple conditions

```python
def ends_with_conditions(text, conditions):
    """Check if string ends with multiple conditions."""
    if not text:
        return False

    last_char = text[-1]
    return all(condition(last_char) for condition in conditions)


text = "Hello World"
conditions = [str.isalpha, lambda c: c in "abcdefghijklmnopqrstuvwxyz"]
result = ends_with_conditions(text, conditions)
print(result)  # True
```

📂 Check string end with multiple conditions

🏷️ Tags: string, endswith, conditions, multiple, validation, text
📝 Notes:
- Combines multiple checks
- All conditions must pass
- Flexible validation
- Useful for complex rules

### 🧩 Check with word boundaries

```python
import re


def ends_with_word(text, word):
    """Check if string ends with complete word."""
    pattern = r"\b" + re.escape(word) + r"$"
    return bool(re.search(pattern, text))


text = "Hello World"
result = ends_with_word(text, "World")
print(result)  # True

text2 = "Hello World!"
result2 = ends_with_word(text2, "World")
print(result2)  # False (ends with punctuation)
```

📂 Check if string ends with complete word

🏷️ Tags: string, endswith, word, boundaries, regex, text
📝 Notes:
- Uses word boundaries
- Excludes partial matches
- Handles punctuation
- More precise matching

## 🔗 Cross-References

- **Reference**: See [📂 Starts With](./starts_with.md)
- **Reference**: See [📂 Find String](./find_string.md)

## 🏷️ Tags

`string`, `endswith`, `suffix`, `validation`, `text`

## 📝 Notes

- Use str.endswith() to check for suffixes
- Supports tuples for multiple suffixes
- Useful for file extension and pattern checks
