# 🧩 Pad string with spaces
def pad_string(text, width, align="left"):
    """Pad string to specified width with spaces."""
    if align == "left":
        return text.ljust(width)
    elif align == "right":
        return text.rjust(width)
    else:  # center
        return text.center(width)


text = "Hello"
result = pad_string(text, 10, "left")
print(f"'{result}'")  # 'Hello     '


# 🧩 Pad with custom character
def pad_with_char(text, width, char=" ", align="left"):
    """Pad string with custom character."""
    if align == "left":
        return text.ljust(width, char)
    elif align == "right":
        return text.rjust(width, char)
    else:  # center
        return text.center(width, char)


text = "Hello"
result = pad_with_char(text, 10, "*", "center")
print(result)  # "**Hello***"


# 🧩 Pad with multiple characters
def pad_with_pattern(text, width, pattern, align="left"):
    """Pad string with repeating pattern."""
    if len(pattern) == 0:
        pattern = " "

    # Calculate how much padding is needed
    padding_needed = width - len(text)
    if padding_needed <= 0:
        return text

    # Create padding by repeating pattern
    full_patterns = padding_needed // len(pattern)
    remaining = padding_needed % len(pattern)
    padding = pattern * full_patterns + pattern[:remaining]

    if align == "left":
        return text + padding
    elif align == "right":
        return padding + text
    else:  # center
        left_pad = padding[: len(padding) // 2]
        right_pad = padding[len(padding) // 2 :]
        return left_pad + text + right_pad


text = "Hello"
result = pad_with_pattern(text, 12, "*-", "center")
print(result)  # "*-*-Hello*-*"


# 🧩 Pad with truncation
# See above defined function (pad_with_char)


def pad_or_truncate(text, width, char=" ", align="left", truncate_char="..."):
    """Pad string or truncate if too long."""
    if len(text) > width:
        if align == "left":
            return text[: width - len(truncate_char)] + truncate_char
        elif align == "right":
            return truncate_char + text[-(width - len(truncate_char)) :]
        else:  # center
            half_width = (width - len(truncate_char)) // 2
            return text[:half_width] + truncate_char + text[-(half_width):]
    else:
        return pad_with_char(text, width, char, align)


text = "This is a very long string"
result = pad_or_truncate(text, 15, "*", "center")
print(result)  # "This is...string"


# 🧩 Pad with color codes
def pad_with_color(text, width, color_code="", align="left"):
    """Pad string while preserving color codes."""
    # Remove color codes for length calculation
    import re

    clean_text = re.sub(r"\x1b\[[0-9;]*m", "", text)

    # Calculate padding needed
    padding_needed = width - len(clean_text)
    if padding_needed <= 0:
        return text

    padding = " " * padding_needed

    if align == "left":
        return text + padding
    elif align == "right":
        return padding + text
    else:  # center
        left_pad = padding[: len(padding) // 2]
        right_pad = padding[len(padding) // 2 :]
        return left_pad + text + right_pad


# Example with ANSI color codes
colored_text = "\033[32mHello\033[0m"  # Green text
result = pad_with_color(colored_text, 15, align="center")
print(f"'{result}'")  # '     Hello     ' (with color preserved)


# 🧩 Pad with Unicode characters
def pad_with_unicode(text, width, char=" ", align="left"):
    """Pad string handling Unicode characters properly."""
    # Use str methods that handle Unicode correctly
    if align == "left":
        return text.ljust(width, char)
    elif align == "right":
        return text.rjust(width, char)
    else:  # center
        return text.center(width, char)


text = "Hello世界"  # Contains Unicode
result = pad_with_unicode(text, 12, "·", "center")
print(result)  # "··Hello世界···"


# 🧩 Pad with custom alignment
def pad_custom_alignment(text, width, char=" ", alignment="left", offset=0):
    """Pad string with custom alignment and offset."""
    if alignment == "left":
        return text.ljust(width, char)
    elif alignment == "right":
        return text.rjust(width, char)
    elif alignment == "center":
        return text.center(width, char)
    elif alignment == "custom":
        # Custom alignment with offset
        padding_needed = width - len(text)
        if padding_needed <= 0:
            return text

        left_pad = min(offset, padding_needed)
        right_pad = padding_needed - left_pad

        return char * left_pad + text + char * right_pad
    else:
        return text


text = "Hello"
result = pad_custom_alignment(text, 15, "*", "custom", 5)
print(result)  # "*****Hello*****"


# 🧩 Pad with number formatting
# See above defined function (pad_with_char)


def pad_number(number, width, char=" ", align="right"):
    """Pad number to specified width."""
    text = str(number)
    return pad_with_char(text, width, char, align)


numbers = [1, 12, 123, 1234]
for num in numbers:
    result = pad_number(num, 6, "0", "right")
    print(result)
# "000001"
# "000012"
# "000123"
# "001234"
