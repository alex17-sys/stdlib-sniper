# Check String Starts With

Zero-dependency Python snippets using only the standard library.

7 snippets available in this sub-category.

---

## Simple

###  Check if string starts with prefix

`string` `startswith` `prefix` `check` `text`

Check if string starts with a specific prefix

```python
def starts_with(text, prefix):
    """Check if string starts with prefix."""
    return text.startswith(prefix)


text = "Hello World"
result = starts_with(text, "Hello")
print(result)  # True
```

!!! note "Notes"
    - Uses str.startswith() method
    - Case-sensitive matching
    - Returns boolean
    - Simple and efficient

<hr class="snippet-divider">

### Check with case-insensitive matching

`string` `startswith` `prefix` `case-insensitive` `text`

Check string prefix ignoring case differences

```python
def starts_with_ignore_case(text, prefix):
    """Check if string starts with prefix ignoring case."""
    return text.lower().startswith(prefix.lower())


text = "Hello World"
result = starts_with_ignore_case(text, "hello")
print(result)  # True
```

!!! note "Notes"
    - Converts both strings to lowercase
    - Handles mixed case text
    - Useful for user input matching
    - Maintains original text

<hr class="snippet-divider">

## Complex

###  Check multiple prefixes

`string` `startswith` `multiple` `prefixes` `tuple` `text`

Check if string starts with any of multiple prefixes

```python
def starts_with_any(text, prefixes):
    """Check if string starts with any of the prefixes."""
    return text.startswith(tuple(prefixes))


text = "Hello World"
prefixes = ["Hello", "Hi", "Hey"]
result = starts_with_any(text, prefixes)
print(result)  # True
```

!!! note "Notes"
    - Uses tuple of prefixes
    - Efficient for multiple checks
    - Returns True if any match
    - Useful for categorization

<hr class="snippet-divider">

### Check with position offset

`string` `startswith` `position` `offset` `slice` `text`

Check prefix match at specific position

```python
def starts_with_at_position(text, prefix, start=0, end=None):
    """Check if string starts with prefix at specific position."""
    return text.startswith(prefix, start, end)


text = "Hello World Python"
result = starts_with_at_position(text, "World", 6)
print(result)  # True
```

!!! note "Notes"
    - Uses start and end parameters
    - Checks substring at position
    - Useful for parsing
    - Flexible position control

<hr class="snippet-divider">

### Check with regex pattern

`string` `startswith` `regex` `pattern` `match` `text`

Check if string starts with regex pattern

```python
import re


def starts_with_pattern(text, pattern):
    """Check if string starts with regex pattern."""
    return bool(re.match(pattern, text))


text = "Hello123World"
result = starts_with_pattern(text, r"Hello\d+")
print(result)  # True
```

!!! note "Notes"
    - Uses re.match() for start anchor
    - Supports complex patterns
    - More flexible than startswith
    - Powerful pattern matching

<hr class="snippet-divider">

### Check with custom function

`string` `startswith` `custom` `function` `condition` `text`

Check string start with custom condition function

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

!!! note "Notes"
    - Uses custom check function
    - Flexible condition checking
    - Useful for validation
    - Supports any condition

<hr class="snippet-divider">

### Check with multiple conditions

`string` `startswith` `conditions` `multiple` `validation` `text`

Check string start with multiple conditions

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

!!! note "Notes"
    - Combines multiple checks
    - All conditions must pass
    - Flexible validation
    - Useful for complex rules

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Ends With](./ends_with.md)
- **Reference**: See [📂 Find String](./find_string.md)

## 🏷️ Tags

`string`, `startswith`, `prefix`, `validation`, `text`

## 📝 Notes

- Use str.startswith() to check for prefixes
- Supports tuples for multiple prefixes
- Useful for URL, file, and pattern checks
