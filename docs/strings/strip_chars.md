---
title: Strip Characters from String
description: Remove specific characters from the beginning and end of a string using the standard library.
keywords: character, characters, classes, condition, custom, function, left, lstrip, multiple, pattern, positions, regex, right, rstrip, sets, string, string module, strip, sub, text, tracking, trim, whitespace
---

# Strip Characters from String

Remove specific characters from the beginning and end of a string using the standard library.

9 snippets available in this sub-category.

---

## Simple

###  Strip whitespace from ends

`string` `strip` `whitespace` `trim` `text`

Remove whitespace from string ends

```python
def strip_whitespace(text):
    """Strip whitespace from beginning and end of string."""
    return text.strip()


text = "  Hello World  "
result = strip_whitespace(text)
print(result)  # "Hello World"
```

!!! note "Notes"
    - Uses str.strip() method
    - Removes leading and trailing spaces
    - Returns cleaned string
    - Common text cleaning operation

<hr class="snippet-divider">

### Strip specific characters

`string` `strip` `characters` `custom` `text`

Remove specific characters from string ends

```python
def strip_chars(text, chars):
    """Strip specific characters from string ends."""
    return text.strip(chars)


text = "***Hello World***"
result = strip_chars(text, "*")
print(result)  # "Hello World"
```

!!! note "Notes"
    - Uses str.strip() with character set
    - Removes specified characters
    - Handles multiple characters
    - Useful for cleaning data

<hr class="snippet-divider">

## Complex

###  Strip from left only

`string` `strip` `left` `lstrip` `text`

Remove characters from left side only

```python
def strip_left(text, chars=None):
    """Strip characters from left side only."""
    if chars is None:
        return text.lstrip()
    return text.lstrip(chars)


text = "***Hello World***"
result = strip_left(text, "*")
print(result)  # "Hello World***"
```

!!! note "Notes"
    - Uses str.lstrip() method
    - Preserves right side
    - Optional character set
    - Useful for prefix removal

<hr class="snippet-divider">

### Strip from right only

`string` `strip` `right` `rstrip` `text`

Remove characters from right side only

```python
def strip_right(text, chars=None):
    """Strip characters from right side only."""
    if chars is None:
        return text.rstrip()
    return text.rstrip(chars)


text = "***Hello World***"
result = strip_right(text, "*")
print(result)  # "***Hello World"
```

!!! note "Notes"
    - Uses str.rstrip() method
    - Preserves left side
    - Optional character set
    - Useful for suffix removal

<hr class="snippet-divider">

### Strip multiple character sets

`string` `strip` `multiple` `sets` `characters` `text`

Remove multiple character sets from string ends

```python
def strip_multiple(text, char_sets):
    """Strip multiple character sets from string."""
    result = text
    for chars in char_sets:
        result = result.strip(chars)
    return result


text = "***Hello World!!!"
char_sets = ["*", "!", " "]
result = strip_multiple(text, char_sets)
print(result)  # "Hello World"
```

!!! note "Notes"
    - Iterative stripping
    - Handles complex patterns
    - Flexible character removal
    - Useful for data cleaning

<hr class="snippet-divider">

### Strip with custom function

`string` `strip` `custom` `function` `condition` `text`

Strip characters using custom condition function

```python
def strip_custom(text, condition_func):
    """Strip characters based on custom condition."""
    start = 0
    end = len(text)

    # Find start position
    while start < end and condition_func(text[start]):
        start += 1

    # Find end position
    while end > start and condition_func(text[end - 1]):
        end -= 1

    return text[start:end]


text = "123Hello World456"
result = strip_custom(text, str.isdigit)
print(result)  # "Hello World"
```

!!! note "Notes"
    - Uses custom condition function
    - Flexible character selection
    - Manual position tracking
    - Powerful customization

<hr class="snippet-divider">

### Strip with regex pattern

`string` `strip` `regex` `pattern` `sub` `text`

Strip characters matching regex pattern

```python
import re


def strip_regex(text, pattern):
    """Strip characters matching regex pattern from ends."""
    # Strip from start
    text = re.sub(f"^{pattern}+", "", text)
    # Strip from end
    text = re.sub(f"{pattern}+$", "", text)
    return text


text = "***Hello World!!!"
result = strip_regex(text, r"[!*]")
print(result)  # "Hello World"
```

!!! note "Notes"
    - Uses regex substitution
    - Supports complex patterns
    - Handles multiple matches
    - Powerful pattern matching

<hr class="snippet-divider">

### Strip with character classes

`string` `strip` `character` `classes` `string module` `text`

Strip characters from predefined character classes

```python
def strip_character_classes(text, classes):
    """Strip characters from specific character classes."""
    import string

    chars_to_strip = ""
    for char_class in classes:
        if char_class == "digits":
            chars_to_strip += string.digits
        elif char_class == "letters":
            chars_to_strip += string.ascii_letters
        elif char_class == "punctuation":
            chars_to_strip += string.punctuation
        elif char_class == "whitespace":
            chars_to_strip += string.whitespace
        elif char_class == "printable":
            chars_to_strip += string.printable

    return text.strip(chars_to_strip)


text = "123Hello World!!!"
result = strip_character_classes(text, ["digits", "punctuation"])
print(result)  # "Hello World"
```

!!! note "Notes"
    - Uses string module constants
    - Predefined character sets
    - Flexible class selection
    - Useful for data cleaning

<hr class="snippet-divider">

### Strip with position tracking

`string` `strip` `positions` `tracking` `text`

Strip characters and track positions

```python
def strip_with_positions(text, chars=None):
    """Strip characters and return positions."""
    if chars is None:
        chars = " \t\n\r\f\v"

    start = 0
    end = len(text)

    # Find start position
    while start < end and text[start] in chars:
        start += 1

    # Find end position
    while end > start and text[end - 1] in chars:
        end -= 1

    stripped = text[start:end]
    return stripped, start, end


text = "  Hello World  "
result, start_pos, end_pos = strip_with_positions(text)
print(f"'{result}' (positions {start_pos}-{end_pos})")
# 'Hello World' (positions 2-12)
```

!!! note "Notes"
    - Returns stripped text and positions
    - Useful for text processing
    - Enables position-based operations
    - Combines stripping and tracking

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Remove Whitespace](./remove_whitespace.md)
- **Reference**: See [📂 Normalize Whitespace](./normalize_whitespace.md)

## 🏷️ Tags

`string`, `strip`, `positions`, `tracking`, `text`

## 📝 Notes

- Use str.strip(), str.lstrip(), and str.rstrip() for character removal
- Position tracking is useful for advanced text processing
- Related: whitespace normalization and removal
