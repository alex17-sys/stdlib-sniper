---
title: Check String Ends With
description: Check if a string ends with a specific suffix using the standard library.
keywords: boundaries, case-insensitive, check, condition, conditions, custom, endswith, extension, file, filename, function, multiple, offset, pattern, position, regex, search, slice, string, suffix, suffixes, text, tuple, validation, word
---

# Check String Ends With

Check if a string ends with a specific suffix using the standard library.

9 snippets available in this sub-category.

---

## Simple

###  Check if string ends with suffix

`string` `endswith` `suffix` `check` `text`

Check if string ends with a specific suffix

```python
def ends_with(text, suffix):
    """Check if string ends with suffix."""
    return text.endswith(suffix)


text = "Hello World"
result = ends_with(text, "World")
print(result)  # True
```

!!! note "Notes"
    - Uses str.endswith() method
    - Case-sensitive matching
    - Returns boolean
    - Simple and efficient

<hr class="snippet-divider">

### Check with case-insensitive matching

`string` `endswith` `suffix` `case-insensitive` `text`

Check string suffix ignoring case differences

```python
def ends_with_ignore_case(text, suffix):
    """Check if string ends with suffix ignoring case."""
    return text.lower().endswith(suffix.lower())


text = "Hello World"
result = ends_with_ignore_case(text, "world")
print(result)  # True
```

!!! note "Notes"
    - Converts both strings to lowercase
    - Handles mixed case text
    - Useful for user input matching
    - Maintains original text

<hr class="snippet-divider">

## Complex

###  Check multiple suffixes

`string` `endswith` `multiple` `suffixes` `tuple` `text`

Check if string ends with any of multiple suffixes

```python
def ends_with_any(text, suffixes):
    """Check if string ends with any of the suffixes."""
    return text.endswith(tuple(suffixes))


text = "Hello World"
suffixes = ["World", "Python", "Java"]
result = ends_with_any(text, suffixes)
print(result)  # True
```

!!! note "Notes"
    - Uses tuple of suffixes
    - Efficient for multiple checks
    - Returns True if any match
    - Useful for file extensions

<hr class="snippet-divider">

### Check with position offset

`string` `endswith` `position` `offset` `slice` `text`

Check suffix match at specific position

```python
def ends_with_at_position(text, suffix, start=0, end=None):
    """Check if string ends with suffix at specific position."""
    return text.endswith(suffix, start, end)


text = "Hello World Python"
result = ends_with_at_position(text, "World", 0, 11)
print(result)  # True
```

!!! note "Notes"
    - Uses start and end parameters
    - Checks substring at position
    - Useful for parsing
    - Flexible position control

<hr class="snippet-divider">

### Check file extensions

`string` `endswith` `file` `extension` `filename` `text`

Check if filename has specific file extension

```python
def has_file_extension(filename, extensions):
    """Check if filename has specific extension(s)."""
    return filename.lower().endswith(tuple(ext.lower() for ext in extensions))


filename = "document.PDF"
extensions = [".pdf", ".doc", ".txt"]
result = has_file_extension(filename, extensions)
print(result)  # True
```

!!! note "Notes"
    - Case-insensitive extension check
    - Handles multiple extensions
    - Useful for file processing
    - Common use case

<hr class="snippet-divider">

### Check with regex pattern

`string` `endswith` `regex` `pattern` `search` `text`

Check if string ends with regex pattern

```python
import re


def ends_with_pattern(text, pattern):
    """Check if string ends with regex pattern."""
    return bool(re.search(pattern + "$", text))


text = "Hello123World"
result = ends_with_pattern(text, r"\d+World$")
print(result)  # True
```

!!! note "Notes"
    - Uses re.search() with end anchor
    - Supports complex patterns
    - More flexible than endswith
    - Powerful pattern matching

<hr class="snippet-divider">

### Check with custom function

`string` `endswith` `custom` `function` `condition` `text`

Check string end with custom condition function

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

!!! note "Notes"
    - Uses custom check function
    - Flexible condition checking
    - Useful for validation
    - Supports any condition

<hr class="snippet-divider">

### Check with multiple conditions

`string` `endswith` `conditions` `multiple` `validation` `text`

Check string end with multiple conditions

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

!!! note "Notes"
    - Combines multiple checks
    - All conditions must pass
    - Flexible validation
    - Useful for complex rules

<hr class="snippet-divider">

### Check with word boundaries

`string` `endswith` `word` `boundaries` `regex` `text`

Check if string ends with complete word

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

!!! note "Notes"
    - Uses word boundaries
    - Excludes partial matches
    - Handles punctuation
    - More precise matching

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Starts With](./starts_with.md)
- **Reference**: See [📂 Find String](./find_string.md)

## 🏷️ Tags

`string`, `endswith`, `suffix`, `validation`, `text`

## 📝 Notes

- Use str.endswith() to check for suffixes
- Supports tuples for multiple suffixes
- Useful for file extension and pattern checks
