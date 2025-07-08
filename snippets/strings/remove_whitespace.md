# Remove Whitespace

Zero-dependency Python snippets for removing whitespace from strings using the standard library.

## Simple

### 🧩 Remove all whitespace

```python
text = "  Hello   World  Python  "
no_whitespace = text.replace(" ", "").replace("\t", "").replace("\n", "")
print(no_whitespace)
```

📂 Remove all spaces, tabs, and newlines from string

🏷️ Tags: string, whitespace, remove, replace, text
📝 Notes:
- Removes spaces, tabs, and newlines
- Preserves all other characters
- Simple and straightforward
- Works with any string

### 🧩 Remove leading and trailing whitespace

```python
text = "  Hello World  "
cleaned = text.strip()
print(cleaned)
```

📂 Remove whitespace from beginning and end of string

🏷️ Tags: string, whitespace, strip, leading, trailing, text
📝 Notes:
- Removes spaces, tabs, newlines from ends
- Preserves internal whitespace
- Most common whitespace cleaning
- Safe for any string

## Complex

### 🧩 Remove whitespace with custom characters

```python
def remove_whitespace_custom(text, chars=None):
    """Remove specified whitespace characters from string."""
    if chars is None:
        chars = " \t\n\r\f\v"  # All whitespace characters

    result = text
    for char in chars:
        result = result.replace(char, "")
    return result


text = "  Hello\tWorld\nPython\r\n"
result = remove_whitespace_custom(text)
print(result)  # "HelloWorldPython"

# Remove only spaces and tabs
result = remove_whitespace_custom(text, " \t")
print(result)  # "HelloWorld\nPython\r\n"
```

📂 Remove specific whitespace characters from string

🏷️ Tags: string, whitespace, remove, custom, characters, text
📝 Notes:
- Customizable character removal
- Supports all whitespace types
- Preserves non-whitespace characters
- Flexible for different needs

### 🧩 Remove whitespace with normalization

```python
import re


def normalize_whitespace(text, replace_with=" "):
    """Remove all whitespace and normalize to single spaces."""
    # Replace all whitespace sequences with single space
    normalized = re.sub(r"\s+", replace_with, text)
    # Remove leading/trailing whitespace
    return normalized.strip()


text = "  Hello   World\n\nPython\t\tProgramming  "
result = normalize_whitespace(text)
print(result)  # "Hello World Python Programming"

# Normalize to single character
result = normalize_whitespace(text, "")
print(result)  # "HelloWorldPythonProgramming"
```

📂 Remove all whitespace and normalize to single characters

🏷️ Tags: string, whitespace, normalize, regex, text
📝 Notes:
- Uses regex for efficient processing
- Normalizes multiple whitespace to single
- Configurable replacement character
- Useful for text cleaning

### 🧩 Check if string is empty

```python
def is_empty(text):
    """Check if string is empty or whitespace only."""
    return not text or not text.strip()


# Examples
print(is_empty(""))  # True
print(is_empty("   "))  # True
print(is_empty("Hello"))  # False
print(is_empty("\t\n"))  # True
```

📂 Check if string is empty or contains only whitespace

🏷️ Tags: string, empty, whitespace, validation, check, text
📝 Notes:
- Handles empty strings
- Handles whitespace-only strings
- Common validation pattern
- Safe for None values

## 🔗 Cross-References

- **Reference**: See [📂 Strip Characters](./strip_chars.md)
- **Reference**: See [📂 Normalize Whitespace](./normalize_whitespace.md)

## 🏷️ Tags

`string`, `whitespace`, `remove`, `strip`, `text`

## 📝 Notes

- Use str.replace() or regex to remove whitespace
- Useful for data cleaning and normalization
- Related: stripping and normalizing whitespace
