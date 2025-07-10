---
title: Capitalize Words
description: Zero-dependency Python snippets for capitalizing words in strings using the standard library.
keywords: capitalize, contractions, custom, exceptions, first, hyphens, regex, string, text, title, words
---

# Capitalize Words

Zero-dependency Python snippets for capitalizing words in strings using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Capitalize first letter of each word

`string` `capitalize` `title` `words` `text`

Capitalize first letter of each word using title()

```python
text = "hello world python"
capitalized = text.title()
print(capitalized)
```

!!! note "Notes"
    - Uses str.title() method
    - Capitalizes first letter of each word
    - Handles multiple spaces correctly
    - Converts rest of letters to lowercase

<hr class="snippet-divider">

### Capitalize first letter only

`string` `capitalize` `first` `text`

Capitalize only the first letter of the string

```python
text = "hello world python"
capitalized = text.capitalize()
print(capitalized)
```

!!! note "Notes"
    - Uses str.capitalize() method
    - Capitalizes only first letter
    - Converts rest to lowercase
    - Useful for sentence formatting

<hr class="snippet-divider">

## Complex

###  Capitalize words with custom exceptions

`string` `capitalize` `words` `exceptions` `custom` `text`

Capitalize words with custom exception list

```python
def capitalize_words_custom(text, exceptions=None):
    """Capitalize words except for specified exceptions."""
    if exceptions is None:
        exceptions = {
            "a",
            "an",
            "the",
            "and",
            "or",
            "but",
            "in",
            "on",
            "at",
            "to",
            "for",
            "of",
            "with",
            "by",
        }

    words = text.lower().split()
    result = []

    for i, word in enumerate(words):
        if i == 0 or word not in exceptions:
            result.append(word.capitalize())
        else:
            result.append(word)

    return " ".join(result)


text = "the quick brown fox jumps over the lazy dog"
result = capitalize_words_custom(text)
print(result)  # "The Quick Brown Fox Jumps over the Lazy Dog"
```

!!! note "Notes"
    - Skips common articles and prepositions
    - Always capitalizes first word
    - Customizable exception list
    - Useful for title formatting

<hr class="snippet-divider">

### Capitalize words with special handling

`string` `capitalize` `words` `contractions` `hyphens` `regex` `text`

Capitalize words with special handling for contractions and hyphens

```python
import re


def capitalize_words_advanced(text):
    """Capitalize words with special handling for contractions and hyphens."""
    # Handle contractions (don't, can't, etc.)
    text = re.sub(
        r"\b(\w+)\'(\w+)\b", lambda m: m.group(1).capitalize() + "'" + m.group(2).lower(), text
    )

    # Handle hyphenated words
    text = re.sub(
        r"\b(\w+)-(\w+)\b", lambda m: m.group(1).capitalize() + "-" + m.group(2).capitalize(), text
    )

    # Handle regular words
    words = text.split()
    result = []

    for word in words:
        if not re.match(r".*[\'-].*", word):  # Not a contraction or hyphenated
            result.append(word.capitalize())
        else:
            result.append(word)

    return " ".join(result)


text = "don't forget the e-mail and co-worker"
result = capitalize_words_advanced(text)
print(result)  # "Don't Forget the E-Mail and Co-Worker"
```

!!! note "Notes"
    - Handles contractions properly
    - Capitalizes both parts of hyphenated words
    - Uses regex for pattern matching
    - Preserves special characters

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Title Case](./title_case.md)
- **Reference**: See [📂 Format String](./format_string.md)

## 🏷️ Tags

`string`, `capitalize`, `words`, `title`, `case`, `text`

## 📝 Notes

- Use str.title() or str.capitalize() for word capitalization
- Handles punctuation and whitespace
- Useful for formatting names and titles
