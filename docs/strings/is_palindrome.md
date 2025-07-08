# Check if String is Palindrome

Zero-dependency Python snippets using only the standard library.

11 snippets available in this sub-category.

---

## Simple

###  Basic palindrome check

`string` `palindrome` `reverse` `validation` `text`

Basic palindrome check using string reversal

```python
def is_palindrome(text):
    """Check if string is a palindrome."""
    return text == text[::-1]


text = "racecar"
result = is_palindrome(text)
print(result)  # True
```

!!! note "Notes"
    - Uses string slicing with step -1
    - Simple and efficient
    - Returns boolean
    - Case-sensitive

<hr class="snippet-divider">

### Case-insensitive palindrome check

`string` `palindrome` `case-insensitive` `validation` `text`

Case-insensitive palindrome check

```python
def is_palindrome_ignore_case(text):
    """Check if string is a palindrome ignoring case."""
    text_lower = text.lower()
    return text_lower == text_lower[::-1]


text = "Racecar"
result = is_palindrome_ignore_case(text)
print(result)  # True
```

!!! note "Notes"
    - Converts to lowercase first
    - Handles mixed case text
    - Maintains original text
    - More flexible validation

<hr class="snippet-divider">

## Complex

###  Palindrome check with punctuation removal

`string` `palindrome` `punctuation` `regex` `validation` `text`

Palindrome check with punctuation and space removal

```python
import re


def is_palindrome_clean(text):
    """Check if string is a palindrome after removing punctuation and spaces."""
    # Remove punctuation and spaces, convert to lowercase
    clean_text = re.sub(r"[^a-zA-Z0-9]", "", text.lower())
    return clean_text == clean_text[::-1]


text = "A man, a plan, a canal: Panama!"
result = is_palindrome_clean(text)
print(result)  # True
```

!!! note "Notes"
    - Removes all non-alphanumeric characters
    - Converts to lowercase
    - Handles complex text
    - Useful for real-world text

<hr class="snippet-divider">

### Palindrome check with custom character filtering

`string` `palindrome` `custom` `filter` `validation` `text`

Palindrome check with custom character filtering

```python
def is_palindrome_custom_filter(text, filter_chars=""):
    """Check if string is a palindrome with custom character filtering."""
    # Remove specified characters and convert to lowercase
    filtered_text = "".join(c.lower() for c in text if c not in filter_chars)
    return filtered_text == filtered_text[::-1]


text = "Madam, I'm Adam"
result = is_palindrome_custom_filter(text, " ,'")
print(result)  # True
```

!!! note "Notes"
    - Flexible character filtering
    - Configurable filter set
    - Maintains case handling
    - Useful for specific requirements

<hr class="snippet-divider">

### Palindrome check with word boundaries

`string` `palindrome` `words` `boundaries` `validation` `text`

Palindrome check at word level

```python
def is_palindrome_words(text):
    """Check if string is a palindrome at word level."""
    words = text.lower().split()
    return words == words[::-1]


text = "fall leaves after leaves fall"
result = is_palindrome_words(text)
print(result)  # True
```

!!! note "Notes"
    - Checks word-level palindrome
    - Splits on whitespace
    - Case-insensitive
    - Useful for sentences

<hr class="snippet-divider">

### Palindrome check with position tracking

`string` `palindrome` `positions` `tracking` `validation` `text`

Palindrome check with position tracking

```python
def is_palindrome_with_positions(text):
    """Check if string is palindrome and return positions of mismatches."""
    mismatches = []
    length = len(text)

    for i in range(length // 2):
        if text[i] != text[length - 1 - i]:
            mismatches.append((i, length - 1 - i))

    return len(mismatches) == 0, mismatches


text = "racecar"
result, mismatches = is_palindrome_with_positions(text)
print(result)  # True
print(mismatches)  # []

text2 = "hello"
result2, mismatches2 = is_palindrome_with_positions(text2)
print(result2)  # False
print(mismatches2)  # [(0, 4), (1, 3)]
```

!!! note "Notes"
    - Returns mismatch positions
    - Useful for debugging
    - Shows where differences occur
    - Educational tool

<hr class="snippet-divider">

### Palindrome check with minimum length

`string` `palindrome` `length` `minimum` `validation` `text`

Palindrome check with minimum length requirement

```python
def is_palindrome_min_length(text, min_length=1):
    """Check if string is palindrome with minimum length requirement."""
    if len(text) < min_length:
        return False
    return text == text[::-1]


text = "aa"
result = is_palindrome_min_length(text, 3)
print(result)  # False

text2 = "racecar"
result2 = is_palindrome_min_length(text2, 3)
print(result2)  # True
```

!!! note "Notes"
    - Configurable minimum length
    - Prevents short palindromes
    - Useful for validation
    - Flexible requirements

<hr class="snippet-divider">

### Palindrome check with character counting

`string` `palindrome` `character` `count` `counter` `validation` `text`

Palindrome check using character counting

```python
from collections import Counter


def is_palindrome_character_count(text):
    """Check if string can form a palindrome by character counting."""
    # Remove spaces and convert to lowercase
    clean_text = "".join(c.lower() for c in text if c.isalnum())

    # Count characters
    char_count = Counter(clean_text)

    # Check if at most one character has odd count
    odd_count = sum(1 for count in char_count.values() if count % 2 == 1)
    return odd_count <= 1


text = "racecar"
result = is_palindrome_character_count(text)
print(result)  # True

text2 = "hello"
result2 = is_palindrome_character_count(text2)
print(result2)  # False
```

!!! note "Notes"
    - Uses character frequency
    - Checks if palindrome is possible
    - Handles rearrangements
    - Useful for anagram-like problems

<hr class="snippet-divider">

### Palindrome check with custom comparison

`string` `palindrome` `custom` `comparison` `function` `validation` `text`

Palindrome check with custom comparison function

```python
def is_palindrome_custom_compare(text, compare_func=None):
    """Check if string is palindrome with custom comparison function."""
    if compare_func is None:
        def compare_func(x, y):
            return x == y

    length = len(text)
    for i in range(length // 2):
        if not compare_func(text[i], text[length - 1 - i]):
            return False
    return True


# Case-insensitive comparison
def case_insensitive_compare(a, b):
    return a.lower() == b.lower()


text = "Racecar"
result = is_palindrome_custom_compare(text, case_insensitive_compare)
print(result)  # True
```

!!! note "Notes"
    - Flexible comparison function
    - Customizable validation rules
    - Useful for special cases
    - Powerful customization

<hr class="snippet-divider">

### Palindrome check with Unicode support

`string` `palindrome` `unicode` `normalization` `validation` `text`

Palindrome check with Unicode character support

```python
def is_palindrome_unicode(text):
    """Check if string is palindrome with proper Unicode handling."""
    # Normalize Unicode characters
    import unicodedata

    normalized = unicodedata.normalize("NFD", text)

    # Remove combining characters
    clean_text = "".join(c for c in normalized if not unicodedata.combining(c))

    return clean_text == clean_text[::-1]


text = "café"
result = is_palindrome_unicode(text)
print(result)  # False (but handles Unicode properly)
```

!!! note "Notes"
    - Handles Unicode characters
    - Normalizes text properly
    - Removes combining characters
    - International text support

<hr class="snippet-divider">

### Palindrome check with performance optimization

`string` `palindrome` `optimized` `performance` `validation` `text`

Optimized palindrome check for large strings

```python
def is_palindrome_optimized(text):
    """Optimized palindrome check for large strings."""
    length = len(text)
    # Only check half the string
    for i in range(length // 2):
        if text[i] != text[length - 1 - i]:
            return False
    return True


text = "a" * 10000 + "b" + "a" * 10000
result = is_palindrome_optimized(text)
print(result)  # False (but optimized for large strings)
```

!!! note "Notes"
    - Early termination on mismatch
    - Only checks half the string
    - Memory efficient
    - Fast for large strings

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Reverse String](./reverse_string.md)
- **Reference**: See [📂 Is Anagram](./is_anagram.md)

## 🏷️ Tags

`string`, `palindrome`, `check`, `reverse`, `validation`, `performance`, `text`

## 📝 Notes

- Palindrome checks compare a string to its reverse
- Efficient algorithms can short-circuit on mismatch
- Useful for text validation and puzzles
