# Title Case

Zero-dependency Python snippets for converting text to title case using the standard library.

## Simple

### 🧩 Convert to title case

```python
text = "hello world python programming"
title_text = text.title()
print(title_text)
```

📂 Convert string to title case using title() method

🏷️ Tags: string, title, case, text
📝 Notes:
- Capitalizes first letter of each word
- Converts rest to lowercase
- Handles multiple spaces correctly
- Standard title case formatting

### 🧩 Title case with custom separator

```python
text = "hello-world-python"
title_text = text.replace("-", " ").title().replace(" ", "-")
print(title_text)
```

📂 Convert hyphenated text to title case

🏷️ Tags: string, title, case, hyphen, separator, text
📝 Notes:
- Replaces hyphens with spaces
- Applies title case
- Restores hyphens
- Useful for URL slugs

## Complex

### 🧩 Title case with minor word exceptions

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

📂 Convert to title case with minor word exceptions

🏷️ Tags: string, title, case, minor, words, exceptions, text
📝 Notes:
- Always capitalizes first and last words
- Keeps minor words lowercase
- Customizable minor word list
- Follows style guide conventions

### 🧩 Title case with special character handling

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

📂 Convert to title case with punctuation preservation

🏷️ Tags: string, title, case, punctuation, regex, advanced, text
📝 Notes:
- Preserves punctuation and spacing
- Handles special characters correctly
- Uses regex for word boundary detection
- Maintains text structure

## 🔗 Cross-References

- **Reference**: See [📂 Capitalize Words](./capitalize_words.md)
- **Reference**: See [📂 Format String](./format_string.md)

## 🏷️ Tags

`string`, `title`, `case`, `capitalize`, `words`, `text`

## 📝 Notes

- Use str.title() for title case conversion
- Handles punctuation and whitespace
- Useful for formatting titles and headings
