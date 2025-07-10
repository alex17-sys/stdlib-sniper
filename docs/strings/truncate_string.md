---
title: Truncate String
description: Zero-dependency Python snippets for truncating strings using the standard library.
keywords: advanced, boundary, directions, ellipsis, length, max, min, options, range, slice, string, text, truncate, validate, word
---

# Truncate String

Zero-dependency Python snippets for truncating strings using the standard library.

5 snippets available in this sub-category.

---

## Simple

###  Truncate string to length

`string` `truncate` `length` `slice` `text`

Truncate string to specified maximum length

```python
def truncate_string(text, max_length):
    """Truncate string to specified length."""
    if len(text) <= max_length:
        return text
    return text[:max_length]


text = "This is a very long string that needs to be truncated"
result = truncate_string(text, 20)
print(result)  # "This is a very long"
```

!!! note "Notes"
    - Simple length-based truncation
    - Preserves original if within limit
    - Uses slice notation
    - No ellipsis added

<hr class="snippet-divider">

### Truncate with ellipsis

`string` `truncate` `ellipsis` `length` `text`

Truncate string and add ellipsis indicator

```python
def truncate_with_ellipsis(text, max_length, ellipsis="..."):
    """Truncate string and add ellipsis if needed."""
    if len(text) <= max_length:
        return text

    # Account for ellipsis length
    truncate_length = max_length - len(ellipsis)
    if truncate_length < 0:
        return ellipsis[:max_length]

    return text[:truncate_length] + ellipsis


text = "This is a very long string that needs to be truncated"
result = truncate_with_ellipsis(text, 20)
print(result)  # "This is a very..."
```

!!! note "Notes"
    - Adds ellipsis when truncated
    - Accounts for ellipsis length
    - Handles edge cases
    - Common UI pattern

<hr class="snippet-divider">

## Complex

###  Truncate at word boundary

`string` `truncate` `word` `boundary` `ellipsis` `text`

Truncate string at word boundary to avoid cutting words

```python
def truncate_at_word(text, max_length, ellipsis="..."):
    """Truncate string at word boundary."""
    if len(text) <= max_length:
        return text

    # Find the last space within the limit
    truncated = text[:max_length]
    last_space = truncated.rfind(" ")

    if last_space > 0:
        # Truncate at word boundary
        result = truncated[:last_space]
    else:
        # No space found, truncate at character boundary
        result = truncated

    # Add ellipsis if truncated
    if len(result) < len(text):
        result += ellipsis

    return result


text = "This is a very long string that needs to be truncated"
result = truncate_at_word(text, 25)
print(result)  # "This is a very long..."
```

!!! note "Notes"
    - Prevents word cutting
    - Falls back to character truncation
    - Maintains readability
    - Useful for UI text display

<hr class="snippet-divider">

### Truncate with custom rules

`string` `truncate` `advanced` `options` `directions` `text`

Truncate string with advanced options and directions

```python
def truncate_advanced(text, max_length, options=None):
    """Truncate string with advanced options."""
    if options is None:
        options = {
            "ellipsis": "...",
            "at_word": True,
            "preserve_html": False,
            "direction": "end",  # 'start', 'end', 'middle'
        }

    if len(text) <= max_length:
        return text

    ellipsis = options.get("ellipsis", "...")
    at_word = options.get("at_word", True)
    direction = options.get("direction", "end")

    # Calculate available length for text
    available_length = max_length - len(ellipsis)

    if direction == "start":
        # Truncate from start
        if at_word:
            truncated = text[-(available_length):]
            first_space = truncated.find(" ")
            if first_space > 0:
                truncated = truncated[first_space:]
        else:
            truncated = text[-(available_length):]
        return ellipsis + truncated

    elif direction == "middle":
        # Truncate from middle
        half_length = available_length // 2
        start = text[:half_length]
        end = text[-(half_length):]
        return start + ellipsis + end

    else:  # direction == 'end'
        # Truncate from end
        if at_word:
            truncated = text[:available_length]
            last_space = truncated.rfind(" ")
            if last_space > 0:
                truncated = truncated[:last_space]
        else:
            truncated = text[:available_length]
        return truncated + ellipsis


# Examples
text = "This is a very long string that needs to be truncated"

# Truncate from start
result = truncate_advanced(text, 25, {"direction": "start"})
print(result)  # "...long string that needs"

# Truncate from middle
result = truncate_advanced(text, 25, {"direction": "middle"})
print(result)  # "This is a...truncated"
```

!!! note "Notes"
    - Multiple truncation directions
    - Word boundary preservation
    - Configurable ellipsis
    - Flexible truncation rules

<hr class="snippet-divider">

### Validate string length

`string` `validate` `length` `range` `min` `max` `text`

Validate string length within specified range

```python
def validate_length(text, min_length=0, max_length=None):
    """Validate string length within range."""
    if not text:
        return len(text) >= min_length

    if max_length is None:
        return len(text) >= min_length
    else:
        return min_length <= len(text) <= max_length


# Examples
print(validate_length("Hello", 3, 10))  # True
print(validate_length("Hi", 5, 10))  # False
print(validate_length("Very long text", max_length=5))  # False
print(validate_length("", 0, 10))  # True
print(validate_length("", 1, 10))  # False
```

!!! note "Notes"
    - Configurable min/max length
    - Flexible validation rules
    - Handles edge cases
    - Common form validation

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Pad String](./pad_string.md)
- **Reference**: See [📂 Format String](./format_string.md)

## 🏷️ Tags

`string`, `truncate`, `ellipsis`, `length`, `options`, `text`

## 📝 Notes
- Use slicing or textwrap.shorten for truncation
- Configurable ellipsis and word boundary options
- Useful for UI, previews, and summaries
