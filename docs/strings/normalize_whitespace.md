---
title: Normalize Whitespace
description: Zero-dependency Python snippets for normalizing whitespace in strings using the standard library.
keywords: advanced, all, custom, newlines, normalize, preserve, regex, rules, spaces, string, text, whitespace
---

# Normalize Whitespace

Zero-dependency Python snippets for normalizing whitespace in strings using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Normalize multiple spaces to single

`string` `whitespace` `normalize` `regex` `spaces` `text`

Replace multiple consecutive spaces with single space

```python
import re

text = "Hello   World    Python"
normalized = re.sub(r" +", " ", text)
print(normalized)
```

!!! note "Notes"
    - Uses regex to find multiple spaces
    - Replaces with single space
    - Preserves other characters
    - Simple and efficient

<hr class="snippet-divider">

### Normalize all whitespace

`string` `whitespace` `normalize` `regex` `all` `text`

Normalize all whitespace characters to single spaces

```python
import re

text = "Hello\t\tWorld\n\nPython\r\nProgramming"
normalized = re.sub(r"\s+", " ", text).strip()
print(normalized)
```

!!! note "Notes"
    - Handles all whitespace types
    - Normalizes to single spaces
    - Removes leading/trailing whitespace
    - Comprehensive whitespace cleaning

<hr class="snippet-divider">

## Complex

###  Normalize whitespace with preservation

`string` `whitespace` `normalize` `preserve` `newlines` `regex` `text`

Normalize whitespace with option to preserve newlines

```python
import re


def normalize_whitespace_preserve(text, preserve_newlines=True):
    """Normalize whitespace while optionally preserving newlines."""
    if preserve_newlines:
        # Replace multiple spaces/tabs with single space
        text = re.sub(r"[ \t]+", " ", text)
        # Replace multiple newlines with single newline
        text = re.sub(r"\n+", "\n", text)
        # Remove leading/trailing whitespace from each line
        lines = [line.strip() for line in text.split("\n")]
        return "\n".join(lines)
    else:
        # Normalize all whitespace to single spaces
        return re.sub(r"\s+", " ", text).strip()


text = "  Hello   World\n\nPython\t\tProgramming  "
result = normalize_whitespace_preserve(text, preserve_newlines=True)
print(result)  # "Hello World\nPython Programming"
```

!!! note "Notes"
    - Option to preserve paragraph structure
    - Handles mixed whitespace types
    - Cleans line-by-line
    - Useful for text formatting

<hr class="snippet-divider">

### Normalize whitespace with custom rules

`string` `whitespace` `normalize` `rules` `custom` `advanced` `text`

Normalize whitespace with customizable rules

```python
import re


def normalize_whitespace_advanced(text, rules=None):
    """Normalize whitespace with custom rules."""
    if rules is None:
        rules = {
            "spaces": "single",  # 'single', 'remove', 'preserve'
            "tabs": "spaces",  # 'spaces', 'remove', 'preserve'
            "newlines": "single",  # 'single', 'remove', 'preserve'
            "leading_trailing": True,  # Remove leading/trailing whitespace
        }

    result = text

    # Handle spaces
    if rules["spaces"] == "single":
        result = re.sub(r" +", " ", result)
    elif rules["spaces"] == "remove":
        result = result.replace(" ", "")

    # Handle tabs
    if rules["tabs"] == "spaces":
        result = result.replace("\t", " ")
    elif rules["tabs"] == "remove":
        result = result.replace("\t", "")

    # Handle newlines
    if rules["newlines"] == "single":
        result = re.sub(r"\n+", "\n", result)
    elif rules["newlines"] == "remove":
        result = result.replace("\n", " ")

    # Handle leading/trailing whitespace
    if rules["leading_trailing"]:
        result = result.strip()

    return result


# Custom normalization rules
text = "  Hello\t\tWorld\n\nPython\r\nProgramming  "
rules = {"spaces": "single", "tabs": "spaces", "newlines": "remove", "leading_trailing": True}
result = normalize_whitespace_advanced(text, rules)
print(result)  # "Hello World Python Programming"
```

!!! note "Notes"
    - Configurable behavior for each whitespace type
    - Flexible rule system
    - Handles complex formatting needs
    - Useful for different text processing requirements

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Strip Characters](./strip_chars.md)
- **Reference**: See [📂 Remove Whitespace](./remove_whitespace.md)

## 🏷️ Tags

`string`, `whitespace`, `normalize`, `regex`, `spaces`, `text`

## 📝 Notes

- Use regex for advanced whitespace normalization
- Handles all whitespace types, including tabs and newlines
- Related: stripping and removing whitespace
