---
title: Justify Text Alignment
description: Justify text with left, right, or center alignment using the standard library.
keywords: alignment, bias, center, characters, custom, ellipsis, flexible, function, justify, left, lines, ljust, multiline, right, rjust, string, text, textwrap, truncate, unicode, width, wrap
---

# Justify Text Alignment

Justify text with left, right, or center alignment using the standard library.

10 snippets available in this sub-category.

---

## Simple

###  Left justify text

`string` `justify` `left` `ljust` `width` `text`

Left justify text to specified width

```python
def left_justify(text, width, char=" "):
    """Left justify text to specified width."""
    return text.ljust(width, char)


text = "Hello"
result = left_justify(text, 15, "*")
print(f"'{result}'")  # 'Hello**********'
```

!!! note "Notes"
    - Uses str.ljust() method
    - Aligns text to left
    - Pads with specified character
    - Common text formatting

<hr class="snippet-divider">

### Right justify text

`string` `justify` `right` `rjust` `width` `text`

Right justify text to specified width

```python
def right_justify(text, width, char=" "):
    """Right justify text to specified width."""
    return text.rjust(width, char)


text = "Hello"
result = right_justify(text, 15, "*")
print(f"'{result}'")  # '**********Hello'
```

!!! note "Notes"
    - Uses str.rjust() method
    - Aligns text to right
    - Pads with specified character
    - Useful for number formatting

<hr class="snippet-divider">

### Center justify text

`string` `justify` `center` `center` `width` `text`

Center justify text to specified width

```python
def center_justify(text, width, char=" "):
    """Center justify text to specified width."""
    return text.center(width, char)


text = "Hello"
result = center_justify(text, 15, "*")
print(f"'{result}'")  # '*****Hello*****'
```

!!! note "Notes"
    - Uses str.center() method
    - Aligns text to center
    - Pads with specified character
    - Balanced formatting

<hr class="snippet-divider">

## Complex

###  Justify with custom alignment

`string` `justify` `alignment` `flexible` `width` `text`

Justify text with flexible alignment options

```python
def justify_text(text, width, align="left", char=" "):
    """Justify text with specified alignment."""
    if align == "left":
        return text.ljust(width, char)
    elif align == "right":
        return text.rjust(width, char)
    elif align == "center":
        return text.center(width, char)
    else:
        raise ValueError("Alignment must be 'left', 'right', or 'center'")


text = "Hello"
result = justify_text(text, 15, "right", "*")
print(result)  # "**********Hello"
```

!!! note "Notes"
    - Single function for all alignments
    - Error handling for invalid alignment
    - Consistent interface
    - Easy to use

<hr class="snippet-divider">

### Justify multiline text

`string` `justify` `multiline` `lines` `width` `text`

Justify each line of multiline text

```python
def justify_multiline(text, width, align="left", char=" "):
    """Justify each line of multiline text."""
    lines = text.split("\n")
    justified_lines = []

    for line in lines:
        if align == "left":
            justified_lines.append(line.ljust(width, char))
        elif align == "right":
            justified_lines.append(line.rjust(width, char))
        elif align == "center":
            justified_lines.append(line.center(width, char))

    return "\n".join(justified_lines)


text = "Hello\nWorld\nPython"
result = justify_multiline(text, 20, "right", "*")
print(result)
# "***************Hello"
# "***************World"
# "**************Python"
```

!!! note "Notes"
    - Processes each line separately
    - Maintains line breaks
    - Consistent alignment per line
    - Useful for text blocks

<hr class="snippet-divider">

### Justify with word wrapping

`string` `justify` `wrap` `textwrap` `width` `text`

Justify text with word wrapping

```python
import textwrap


def justify_wrapped_text(text, width, align="left", char=" "):
    """Justify text with word wrapping."""
    # Wrap text to fit width
    wrapped_lines = textwrap.wrap(text, width=width)

    # Justify each wrapped line
    justified_lines = []
    for line in wrapped_lines:
        if align == "left":
            justified_lines.append(line.ljust(width, char))
        elif align == "right":
            justified_lines.append(line.rjust(width, char))
        elif align == "center":
            justified_lines.append(line.center(width, char))

    return "\n".join(justified_lines)


text = "This is a long text that needs to be wrapped and justified properly"
result = justify_wrapped_text(text, 30, "center", "*")
print(result)
```

!!! note "Notes"
    - Combines wrapping and justification
    - Handles long text gracefully
    - Maintains readability
    - Complex text formatting

<hr class="snippet-divider">

### Justify with truncation

`string` `justify` `truncate` `width` `ellipsis` `text`

Justify text or truncate if too long

```python
def justify_text(text, width, align="left", char=" "):
    # See above defined dunction
    pass

def justify_or_truncate(text, width, align="left", char=" ", truncate_char="..."):
    """Justify text or truncate if too long."""
    if len(text) > width:
        if align == "left":
            return text[: width - len(truncate_char)] + truncate_char
        elif align == "right":
            return truncate_char + text[-(width - len(truncate_char)) :]
        else:  # center
            half_width = (width - len(truncate_char)) // 2
            return text[:half_width] + truncate_char + text[-(half_width):]
    else:
        return justify_text(text, width, align, char)


text = "This is a very long string that needs truncation"
result = justify_or_truncate(text, 20, "center", "*")
print(result)  # "This is...truncation"
```

!!! note "Notes"
    - Uses justify_text
    - Handles strings longer than width
    - Uses ellipsis for truncation
    - Maintains alignment preference
    - Prevents overflow

<hr class="snippet-divider">

### Justify with custom width calculation

`string` `justify` `custom` `width` `function` `text`

Justify text using custom width calculation

```python
def justify_custom_width(text, width, align="left", char=" ", width_func=len):
    """Justify text using custom width calculation."""
    # Calculate width using custom function
    text_width = width_func(text)

    # Calculate padding needed
    padding_needed = width - text_width
    if padding_needed <= 0:
        return text

    if align == "left":
        return text + char * padding_needed
    elif align == "right":
        return char * padding_needed + text
    else:  # center
        left_pad = padding_needed // 2
        right_pad = padding_needed - left_pad
        return char * left_pad + text + char * right_pad


# Example: Justify with visual width (ignoring control characters)
def visual_width(text):
    """Calculate visual width ignoring control characters."""
    import re

    clean_text = re.sub(r"\x1b\[[0-9;]*m", "", text)
    return len(clean_text)


colored_text = "\033[32mHello\033[0m"
result = justify_custom_width(colored_text, 15, "center", width_func=visual_width)
print(f"'{result}'")  # '     Hello     '
```

!!! note "Notes"
    - Custom width calculation
    - Flexible width function
    - Useful for special cases
    - Advanced formatting control

<hr class="snippet-divider">

### Justify with alignment bias

`string` `justify` `bias` `alignment` `width` `text`

Justify text with alignment bias

```python
def justify_with_bias(text, width, align="left", char=" ", bias=0):
    """Justify text with alignment bias."""
    padding_needed = width - len(text)
    if padding_needed <= 0:
        return text

    if align == "left":
        return text + char * padding_needed
    elif align == "right":
        return char * padding_needed + text
    else:  # center
        # Apply bias to centering
        base_left = padding_needed // 2
        left_pad = max(0, min(padding_needed, base_left + bias))
        right_pad = padding_needed - left_pad
        return char * left_pad + text + char * right_pad


text = "Hello"
result = justify_with_bias(text, 15, "center", "*", bias=2)
print(result)  # "*******Hello****"
```

!!! note "Notes"
    - Custom alignment bias
    - Fine-tune positioning
    - Useful for visual balance
    - Advanced formatting

<hr class="snippet-divider">

### Justify with Unicode support

`string` `justify` `unicode` `characters` `width` `text`

Justify text with Unicode character support

```python
def justify_unicode(text, width, align="left", char=" "):
    """Justify text with proper Unicode handling."""
    if align == "left":
        return text.ljust(width, char)
    elif align == "right":
        return text.rjust(width, char)
    else:  # center
        return text.center(width, char)


text = "Hello世界"  # Contains Unicode
result = justify_unicode(text, 15, "center", "·")
print(result)  # "····Hello世界····"
```

!!! note "Notes"
    - Handles Unicode characters correctly
    - Uses built-in str methods
    - Supports Unicode padding chars
    - International text support

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Format String](./format_string.md)
- **Reference**: See [📂 Wrap Text](./wrap_text.md)

## 🏷️ Tags

`string`, `justify`, `left`, `right`, `center`, `alignment`, `multiline`, `width`, `text`

## 📝 Notes

- Use str.ljust(), str.rjust(), and str.center() for alignment
- Multiline and flexible alignment supported
- Related: formatting and wrapping text
