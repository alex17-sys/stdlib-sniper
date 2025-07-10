---
title: Split String
description: Zero-dependency Python snippets for splitting strings using the standard library.
keywords: comma, delimiter, delimiters, limit, max, multiple, pattern, regex, split, splits, string, text, whitespace, words
---

# Split String

Zero-dependency Python snippets for splitting strings using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Split string by delimiter

`string` `split` `delimiter` `comma` `text`

Split string by comma delimiter

```python
text = "apple,banana,orange,grape"
fruits = text.split(",")
print(fruits)
```

!!! note "Notes"
    - Uses str.split() method
    - Returns list of substrings
    - Removes delimiter from result
    - Handles consecutive delimiters

<hr class="snippet-divider">

### Split string by whitespace

`string` `split` `whitespace` `words` `text`

Split string by whitespace (default)

```python
text = "Hello   World   Python"
words = text.split()
print(words)
```

!!! note "Notes"
    - Default split behavior
    - Handles multiple spaces
    - Removes leading/trailing whitespace
    - Most common string splitting

<hr class="snippet-divider">

## Complex

###  Split string with max splits

`string` `split` `limit` `max` `splits` `text`

Split string with limit on number of splits

```python
def split_string_limited(text, delimiter=None, max_splits=-1):
    """Split string with limit on number of splits."""
    if delimiter is None:
        return text.split(maxsplit=max_splits)
    else:
        return text.split(delimiter, max_splits)


text = "one:two:three:four:five"

# Split into 3 parts
result = split_string_limited(text, ":", 2)
print(result)  # ['one', 'two', 'three:four:five']

# Split by whitespace, max 2 parts
text = "Hello World Python Programming"
result = split_string_limited(text, max_splits=2)
print(result)  # ['Hello', 'World', 'Python Programming']
```

!!! note "Notes"
    - Controls number of splits
    - Useful for parsing structured data
    - Preserves remaining text
    - Flexible delimiter options

<hr class="snippet-divider">

### Split string with regex

`string` `split` `regex` `pattern` `multiple` `delimiters` `text`

Split string using regex patterns

```python
import re


def split_string_regex(text, pattern, flags=0):
    """Split string using regex pattern."""
    return re.split(pattern, text, flags=flags)


text = "Hello,World;Python:Programming"

# Split by multiple delimiters
result = split_string_regex(text, r"[,;:]")
print(result)  # ['Hello', 'World', 'Python', 'Programming']

# Split by whitespace and punctuation
text = "Hello, World! How are you?"
result = split_string_regex(text, r"[\s,!?]+")
print(result)  # ['Hello', 'World', 'How', 'are', 'you', '']
```

!!! note "Notes"
    - Uses regex for complex patterns
    - Multiple delimiter support
    - Flexible pattern matching
    - Powerful splitting capabilities

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Join Strings](./join_strings.md)
- **Reference**: See [📂 Format String](./format_string.md)
- **Reference**: See [📂 Replace String](./replace_string.md)

## 🏷️ Tags

`string`, `split`, `delimiter`, `whitespace`, `limit`, `regex`, `text`

## 📝 Notes

- str.split() is the standard way to break strings into lists
- Regex splitting allows for complex delimiters
- Max splits and whitespace handling are common needs
- See related snippets for joining and replacing strings
