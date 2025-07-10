---
title: Check if String is Alphanumeric
description: Check if a string contains alphanumeric characters using the standard library.
keywords: alphanumeric, characters, custom, digit, end, identifier, isalnum, length, letter, maximum, minimum, pattern, range, regex, spaces, start, string, text, username, validation
---

# Check if String is Alphanumeric

Check if a string contains alphanumeric characters using the standard library.

12 snippets available in this sub-category.

---

## Simple

###  Check if string is alphanumeric

`string` `alphanumeric` `isalnum` `validation` `text`

Check if string contains only alphanumeric characters

```python
def is_alphanumeric(text):
    """Check if string contains only alphanumeric characters."""
    return text.isalnum()


text = "Hello123"
result = is_alphanumeric(text)
print(result)  # True
```

!!! note "Notes"
    - Uses str.isalnum() method
    - Checks for letters and digits
    - Returns boolean
    - Simple validation

<hr class="snippet-divider">

### Check if string is alphanumeric with spaces

`string` `alphanumeric` `spaces` `validation` `text`

Check if string contains only alphanumeric characters and spaces

```python
def is_alphanumeric_with_spaces(text):
    """Check if string contains only alphanumeric characters and spaces."""
    return all(c.isalnum() or c.isspace() for c in text)


text = "Hello 123 World"
result = is_alphanumeric_with_spaces(text)
print(result)  # True
```

!!! note "Notes"
    - Uses all() with generator expression
    - Allows spaces in text
    - Handles mixed content
    - Useful for names with numbers

<hr class="snippet-divider">

## Complex

###  Check if string is alphanumeric with custom characters

`string` `alphanumeric` `custom` `characters` `validation` `text`

Check if string contains alphanumeric characters and custom allowed characters

```python
def is_alphanumeric_custom(text, allowed_chars=""):
    """Check if string contains only alphanumeric characters and custom allowed characters."""
    return all(c.isalnum() or c in allowed_chars for c in text)


text = "User123-Name"
result = is_alphanumeric_custom(text, "-_")
print(result)  # True

text2 = "Product@Name"
result2 = is_alphanumeric_custom(text2, "-_")
print(result2)  # False
```

!!! note "Notes"
    - Flexible character allowance
    - Handles usernames with hyphens/underscores
    - Customizable validation
    - Useful for identifier validation

<hr class="snippet-divider">

### Check if string contains at least one letter and one digit

`string` `alphanumeric` `letter` `digit` `validation` `text`

Check if string contains at least one letter and one digit

```python
def has_letter_and_digit(text):
    """Check if string contains at least one letter and one digit."""
    has_letter = any(c.isalpha() for c in text)
    has_digit = any(c.isdigit() for c in text)
    return has_letter and has_digit


text = "Hello123"
result = has_letter_and_digit(text)
print(result)  # True

text2 = "Hello"
result2 = has_letter_and_digit(text2)
print(result2)  # False
```

!!! note "Notes"
    - Requires both letters and digits
    - Uses any() with generator expressions
    - Useful for password validation
    - Ensures mixed character types

<hr class="snippet-divider">

### Check if string is alphanumeric with minimum length

`string` `alphanumeric` `length` `minimum` `validation` `text`

Check if string is alphanumeric with minimum length requirement

```python
def is_alphanumeric_min_length(text, min_length=1):
    """Check if string is alphanumeric with minimum length requirement."""
    return text.isalnum() and len(text) >= min_length


text = "Hello123"
result = is_alphanumeric_min_length(text, 5)
print(result)  # True

text2 = "Hi1"
result2 = is_alphanumeric_min_length(text2, 5)
print(result2)  # False
```

!!! note "Notes"
    - Combines alphanumeric check with length
    - Configurable minimum length
    - Useful for form validation
    - Prevents short inputs

<hr class="snippet-divider">

### Check if string is alphanumeric with maximum length

`string` `alphanumeric` `length` `maximum` `validation` `text`

Check if string is alphanumeric with maximum length requirement

```python
def is_alphanumeric_max_length(text, max_length):
    """Check if string is alphanumeric with maximum length requirement."""
    return text.isalnum() and len(text) <= max_length


text = "Hello123"
result = is_alphanumeric_max_length(text, 10)
print(result)  # True

text2 = "VeryLongAlphanumericString123"
result2 = is_alphanumeric_max_length(text2, 10)
print(result2)  # False
```

!!! note "Notes"
    - Combines alphanumeric check with length
    - Configurable maximum length
    - Useful for form validation
    - Prevents overly long inputs

<hr class="snippet-divider">

### Check if string is alphanumeric with length range

`string` `alphanumeric` `length` `range` `validation` `text`

Check if string is alphanumeric within specified length range

```python
def is_alphanumeric_length_range(text, min_length=1, max_length=None):
    """Check if string is alphanumeric within length range."""
    if not text.isalnum():
        return False

    length = len(text)
    if length < min_length:
        return False

    if max_length is not None and length > max_length:
        return False

    return True


text = "Hello123"
result = is_alphanumeric_length_range(text, 5, 15)
print(result)  # True

text2 = "Hi1"
result2 = is_alphanumeric_length_range(text2, 5, 15)
print(result2)  # False
```

!!! note "Notes"
    - Flexible length range checking
    - Optional maximum length
    - Comprehensive validation
    - Useful for form validation

<hr class="snippet-divider">

### Check if string starts with alphanumeric

`string` `alphanumeric` `start` `validation` `text`

Check if string starts with an alphanumeric character

```python
def starts_with_alphanumeric(text):
    """Check if string starts with an alphanumeric character."""
    return bool(text and text[0].isalnum())


text = "Hello123"
result = starts_with_alphanumeric(text)
print(result)  # True

text2 = "!Hello123"
result2 = starts_with_alphanumeric(text2)
print(result2)  # False
```

!!! note "Notes"
    - Checks first character only
    - Handles empty strings
    - Simple position check
    - Useful for validation

<hr class="snippet-divider">

### Check if string ends with alphanumeric

`string` `alphanumeric` `end` `validation` `text`

Check if string ends with an alphanumeric character

```python
def ends_with_alphanumeric(text):
    """Check if string ends with an alphanumeric character."""
    return bool(text and text[-1].isalnum())


text = "Hello123"
result = ends_with_alphanumeric(text)
print(result)  # True

text2 = "Hello123!"
result2 = ends_with_alphanumeric(text2)
print(result2)  # False
```

!!! note "Notes"
    - Checks last character only
    - Handles empty strings
    - Simple position check
    - Useful for validation

<hr class="snippet-divider">

### Check if string contains specific alphanumeric pattern

`string` `alphanumeric` `pattern` `regex` `validation` `text`

Check if string matches specific alphanumeric pattern

```python
def matches_alphanumeric_pattern(text, pattern):
    """Check if string matches alphanumeric pattern."""
    import re

    return bool(re.match(pattern, text))


text = "Hello123"
result = matches_alphanumeric_pattern(text, r"^[A-Za-z]+\d+$")
print(result)  # True

text2 = "123Hello"
result2 = matches_alphanumeric_pattern(text2, r"^[A-Za-z]+\d+$")
print(result2)  # False
```

!!! note "Notes"
    - Uses regex pattern matching
    - Flexible pattern definition
    - Powerful validation
    - Useful for complex rules

<hr class="snippet-divider">

### Check if string is valid identifier

`string` `alphanumeric` `identifier` `validation` `text`

Check if string is a valid Python identifier

```python
def is_valid_identifier(text):
    """Check if string is a valid Python identifier."""
    return text.isidentifier()


text = "hello_123"
result = is_valid_identifier(text)
print(result)  # True

text2 = "123hello"
result2 = is_valid_identifier(text2)
print(result2)  # False
```

!!! note "Notes"
    - Uses str.isidentifier() method
    - Follows Python naming rules
    - Cannot start with digit
    - Useful for variable names

<hr class="snippet-divider">

### Check if string is valid username

`string` `alphanumeric` `username` `validation` `text`

Check if string is a valid username

```python
def is_valid_username(text, min_length=3, max_length=20):
    """Check if string is a valid username."""
    if not text:
        return False

    # Check length
    if len(text) < min_length or len(text) > max_length:
        return False

    # Check if starts with letter
    if not text[0].isalpha():
        return False

    # Check if contains only alphanumeric and underscore
    return all(c.isalnum() or c == "_" for c in text)


text = "user_123"
result = is_valid_username(text)
print(result)  # True

text2 = "123user"
result2 = is_valid_username(text2)
print(result2)  # False
```

!!! note "Notes"
    - Custom username validation rules
    - Starts with letter requirement
    - Allows underscores
    - Configurable length limits

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Is Alpha](./is_alpha.md)
- **Reference**: See [📂 Is Numeric](./is_numeric.md)

## 🏷️ Tags

`string`, `alphanumeric`, `isalnum`, `validation`, `text`

## 📝 Notes

- Use str.isalnum() to check for alphanumeric strings
- Returns True if all characters are letters or digits
- Useful for input validation and parsing
