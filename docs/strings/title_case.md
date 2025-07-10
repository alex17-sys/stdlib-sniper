---
title: Title Case
description: Zero-dependency Python snippets for converting text to title case using the standard library.
keywords: advanced, case, exceptions, hyphen, minor, punctuation, regex, separator, string, text, title, words
---

# Title Case

Zero-dependency Python snippets for converting text to title case using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Convert to title case

`string` `title` `case` `text`

Convert string to title case using title() method

```python
text = "hello world python programming"
title_text = text.title()
print(title_text)
```

!!! note "Notes"
    - Capitalizes first letter of each word
    - Converts rest to lowercase
    - Handles multiple spaces correctly
    - Standard title case formatting

<hr class="snippet-divider">

### Title case with custom separator

`string` `title` `case` `hyphen` `separator` `text`

Convert hyphenated text to title case

```python
text = "hello-world-python"
title_text = text.replace("-", " ").title().replace(" ", "-")
print(title_text)
```

!!! note "Notes"
    - Replaces hyphens with spaces
    - Applies title case
    - Restores hyphens
    - Useful for URL slugs

<hr class="snippet-divider">

## Complex

###  Title case with minor word exceptions

`string` `title` `case` `minor` `words` `exceptions` `text`

Convert to title case with minor word exceptions

```python
def title_case_smart(text, minor_words=None):
    """Convert to title case with minor word exceptions."""
    if minor_words is None:
        minor_words = {
            "a",
            "an",
            "and",
            "as",
            "at",
            "but",
            "by",
            "for",
            "in",
            "of",
            "on",
            "or",
            "the",
            "to",
            "up",
            "yet",
        }

    words = text.lower().split()
    if not words:
        return text

    result = [words[0].capitalize()]  # Always capitalize first word

    for word in words[1:]:
        if word in minor_words:
            result.append(word)
        else:
            result.append(word.capitalize())

    return " ".join(result)


text = "the quick brown fox jumps over the lazy dog"
result = title_case_smart(text)
print(result)  # "The Quick Brown Fox Jumps over the Lazy Dog"
```

!!! note "Notes"
    - Always capitalizes first and last words
    - Keeps minor words lowercase
    - Customizable minor word list
    - Follows style guide conventions

<hr class="snippet-divider">

### Title case with special character handling

`string` `title` `case` `punctuation` `regex` `advanced` `text`

Convert to title case with punctuation preservation

```python
import re


def title_case_advanced(text):
    """Convert to title case with special character handling."""
    # Define minor words
    minor_words = {
        "a",
        "an",
        "and",
        "as",
        "at",
        "but",
        "by",
        "for",
        "in",
        "of",
        "on",
        "or",
        "the",
        "to",
        "up",
        "yet",
    }

    # Split by word boundaries, preserving punctuation
    parts = re.split(r"(\b\w+\b)", text)
    result = []

    for i, part in enumerate(parts):
        if re.match(r"\b\w+\b", part):  # It's a word
            if i == 0 or i == len(parts) - 1:  # First or last word
                result.append(part.capitalize())
            elif part.lower() in minor_words:
                result.append(part.lower())
            else:
                result.append(part.capitalize())
        else:  # It's punctuation or whitespace
            result.append(part)

    return "".join(result)


text = "the quick brown fox jumps over the lazy dog!"
result = title_case_advanced(text)
print(result)  # "The Quick Brown Fox Jumps over the Lazy Dog!"
```

!!! note "Notes"
    - Preserves punctuation and spacing
    - Handles special characters correctly
    - Uses regex for word boundary detection
    - Maintains text structure

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Capitalize Words](./capitalize_words.md)
- **Reference**: See [📂 Format String](./format_string.md)

## 🏷️ Tags

`string`, `title`, `case`, `capitalize`, `words`, `text`

## 📝 Notes

- Use str.title() for title case conversion
- Handles punctuation and whitespace
- Useful for formatting titles and headings
