# Center String in Width

Center a string within a specified width using the standard library.

## Simple

### 🧩 Center string with spaces

```python
def center_string(text, width):
    """Center string within specified width using spaces."""
    return text.center(width)


text = "Hello"
result = center_string(text, 15)
print(f"'{result}'")  # '     Hello     '
```

📂 Center string within specified width

🏷️ Tags: string, center, width, spaces, alignment, text
📝 Notes:
- Uses str.center() method
- Pads with spaces by default
- Simple centering operation
- Common text formatting

### 🧩 Center with custom character

```python
def center_with_char(text, width, char=" "):
    """Center string with custom padding character."""
    return text.center(width, char)


text = "Hello"
result = center_with_char(text, 15, "*")
print(result)  # "*****Hello*****"
```

📂 Center string with custom padding character

🏷️ Tags: string, center, custom, character, width, text
📝 Notes:
- Uses custom padding character
- Visual separation
- Maintains centering
- Useful for formatting

## Complex

### 🧩 Center with truncation

```python
def center_or_truncate(text, width, char=" ", truncate_char="..."):
    """Center string or truncate if too long."""
    if len(text) > width:
        # Truncate from middle
        half_width = (width - len(truncate_char)) // 2
        start = text[:half_width]
        end = text[-(half_width):]
        return start + truncate_char + end
    else:
        return text.center(width, char)


text = "This is a very long string that needs truncation"
result = center_or_truncate(text, 20, "*")
print(result)  # "This is...truncation"
```

📂 Center string or truncate if too long

🏷️ Tags: string, center, truncate, width, ellipsis, text
📝 Notes:
- Handles strings longer than width
- Truncates from middle
- Uses ellipsis indicator
- Prevents overflow

### 🧩 Center with custom alignment bias

```python
def center_with_bias(text, width, char=" ", bias="left"):
    """Center string with bias towards left or right."""
    padding_needed = width - len(text)
    if padding_needed <= 0:
        return text

    if bias == "left":
        # Bias towards left (more padding on right)
        left_pad = padding_needed // 2
        right_pad = padding_needed - left_pad
    elif bias == "right":
        # Bias towards right (more padding on left)
        right_pad = padding_needed // 2
        left_pad = padding_needed - right_pad
    else:  # bias == 'center'
        # Perfect centering
        left_pad = padding_needed // 2
        right_pad = padding_needed - left_pad

    return char * left_pad + text + char * right_pad


text = "Hello"
result = center_with_bias(text, 15, "*", "left")
print(result)  # "*****Hello******"
```

📂 Center string with alignment bias

🏷️ Tags: string, center, bias, alignment, width, text
📝 Notes:
- Custom centering bias
- Left/right/center bias options
- Manual padding calculation
- Flexible positioning

### 🧩 Center with multiple lines

```python
def center_multiline(text, width, char=" "):
    """Center each line of multiline text."""
    lines = text.split("\n")
    centered_lines = [line.center(width, char) for line in lines]
    return "\n".join(centered_lines)


text = "Hello\nWorld\nPython"
result = center_multiline(text, 20, "*")
print(result)
# "*******Hello********"
# "*******World********"
# "******Python********"
```

📂 Center each line of multiline text

🏷️ Tags: string, center, multiline, lines, width, text
📝 Notes:
- Processes each line separately
- Maintains line breaks
- Consistent width per line
- Useful for text blocks

### 🧩 Center with word wrapping

```python
import textwrap


def center_wrapped_text(text, width, char=" "):
    """Center text with word wrapping."""
    # Wrap text to fit width
    wrapped_lines = textwrap.wrap(text, width=width)

    # Center each wrapped line
    centered_lines = []
    for line in wrapped_lines:
        # Calculate actual width needed for this line
        line_width = max(len(line), width)
        centered_lines.append(line.center(line_width, char))

    return "\n".join(centered_lines)


text = "This is a long text that needs to be wrapped and centered properly"
result = center_wrapped_text(text, 30, "*")
print(result)
```

📂 Center text with word wrapping

🏷️ Tags: string, center, wrap, textwrap, width, text
📝 Notes:
- Combines wrapping and centering
- Handles long text gracefully
- Maintains readability
- Complex text formatting

### 🧩 Center with color preservation

```python
def center_with_color(text, width, char=" "):
    """Center string while preserving color codes."""
    import re

    # Remove color codes for length calculation
    clean_text = re.sub(r"\x1b\[[0-9;]*m", "", text)

    # Calculate padding needed
    padding_needed = width - len(clean_text)
    if padding_needed <= 0:
        return text

    # Create padding
    left_pad = padding_needed // 2
    right_pad = padding_needed - left_pad

    return char * left_pad + text + char * right_pad


# Example with ANSI color codes
colored_text = "\033[32mHello\033[0m"  # Green text
result = center_with_color(colored_text, 15)
print(f"'{result}'")  # '     Hello     ' (with color preserved)
```

📂 Center string while preserving color codes

🏷️ Tags: string, center, color, codes, ansi, text
📝 Notes:
- Preserves ANSI color codes
- Calculates length without codes
- Maintains visual formatting
- Useful for terminal output

### 🧩 Center with Unicode support

```python
def center_unicode(text, width, char=" "):
    """Center string with proper Unicode handling."""
    return text.center(width, char)


text = "Hello世界"  # Contains Unicode
result = center_unicode(text, 15, "·")
print(result)  # "····Hello世界····"
```

📂 Center string with Unicode character support

🏷️ Tags: string, center, unicode, characters, width, text
📝 Notes:
- Handles Unicode characters correctly
- Uses built-in str.center()
- Supports Unicode padding chars
- International text support

### 🧩 Center with custom width calculation

```python
def center_custom_width(text, width, char=" ", width_func=len):
    """Center string using custom width calculation."""
    # Calculate width using custom function
    text_width = width_func(text)

    # Calculate padding
    padding_needed = width - text_width
    if padding_needed <= 0:
        return text

    left_pad = padding_needed // 2
    right_pad = padding_needed - left_pad

    return char * left_pad + text + char * right_pad


# Example: Center with visual width (ignoring control characters)
def visual_width(text):
    """Calculate visual width ignoring control characters."""
    import re

    clean_text = re.sub(r"\x1b\[[0-9;]*m", "", text)
    return len(clean_text)


colored_text = "\033[32mHello\033[0m"
result = center_custom_width(colored_text, 15, width_func=visual_width)
print(f"'{result}'")  # '     Hello     '
```

📂 Center string using custom width calculation

🏷️ Tags: string, center, custom, width, function, text
📝 Notes:
- Custom width calculation
- Flexible width function
- Useful for special cases
- Advanced formatting control

## 🔗 Cross-References

- **Reference**: See [📂 Justify Text Alignment](./justify_text.md)
- **Reference**: See [📂 Pad String](./pad_string.md)

## 🏷️ Tags

`string`, `center`, `justify`, `alignment`, `width`, `text`

## 📝 Notes

- Use str.center() for centering text
- Useful for formatting tables and output
- Related: justifying and padding text
