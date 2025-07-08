# Remove Whitespace

Zero-dependency Python snippets using only the standard library.

5 snippets available in this sub-category.

---

## Simple

###  Remove all whitespace

`string` `whitespace` `remove` `replace` `text`

Remove all spaces, tabs, and newlines from string

```python
text = "  Hello   World  Python  "
no_whitespace = text.replace(" ", "").replace("\t", "").replace("\n", "")
print(no_whitespace)
```

!!! note "Notes"
    - Removes spaces, tabs, and newlines
    - Preserves all other characters
    - Simple and straightforward
    - Works with any string

<hr class="snippet-divider">

### Remove leading and trailing whitespace

`string` `whitespace` `strip` `leading` `trailing` `text`

Remove whitespace from beginning and end of string

```python
text = "  Hello World  "
cleaned = text.strip()
print(cleaned)
```

!!! note "Notes"
    - Removes spaces, tabs, newlines from ends
    - Preserves internal whitespace
    - Most common whitespace cleaning
    - Safe for any string

<hr class="snippet-divider">

## Complex

###  Remove whitespace with custom characters

`string` `whitespace` `remove` `custom` `characters` `text`

Remove specific whitespace characters from string

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

!!! note "Notes"
    - Customizable character removal
    - Supports all whitespace types
    - Preserves non-whitespace characters
    - Flexible for different needs

<hr class="snippet-divider">

### Remove whitespace with normalization

`string` `whitespace` `normalize` `regex` `text`

Remove all whitespace and normalize to single characters

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

!!! note "Notes"
    - Uses regex for efficient processing
    - Normalizes multiple whitespace to single
    - Configurable replacement character
    - Useful for text cleaning

<hr class="snippet-divider">

### Check if string is empty

`string` `empty` `whitespace` `validation` `check` `text`

Check if string is empty or contains only whitespace

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

!!! note "Notes"
    - Handles empty strings
    - Handles whitespace-only strings
    - Common validation pattern
    - Safe for None values

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Strip Characters](./strip_chars.md)
- **Reference**: See [📂 Normalize Whitespace](./normalize_whitespace.md)

## 🏷️ Tags

`string`, `whitespace`, `remove`, `strip`, `text`

## 📝 Notes

- Use str.replace() or regex to remove whitespace
- Useful for data cleaning and normalization
- Related: stripping and normalizing whitespace
