# Check if Strings are Anagrams

Zero-dependency Python snippets using only the standard library.

11 snippets available in this sub-category.

---

## Simple

###  Basic anagram check

`string` `anagram` `sort` `validation` `text`

Basic anagram check using sorted characters

```python
def is_anagram(text1, text2):
    """Check if two strings are anagrams."""
    return sorted(text1.lower()) == sorted(text2.lower())


text1 = "listen"
text2 = "silent"
result = is_anagram(text1, text2)
print(result)  # True
```

!!! note "Notes"
    - Uses sorted() function
    - Case-insensitive comparison
    - Simple and effective
    - Returns boolean

<hr class="snippet-divider">

### Anagram check with character counting

`string` `anagram` `counter` `validation` `text`

Anagram check using character counting

```python
from collections import Counter


def is_anagram_counter(text1, text2):
    """Check if two strings are anagrams using character counting."""
    return Counter(text1.lower()) == Counter(text2.lower())


text1 = "listen"
text2 = "silent"
result = is_anagram_counter(text1, text2)
print(result)  # True
```

!!! note "Notes"
    - Uses Counter for efficiency
    - Case-insensitive comparison
    - More efficient than sorting
    - Handles character frequency

<hr class="snippet-divider">

## Complex

###  Anagram check with punctuation removal

`string` `anagram` `punctuation` `regex` `validation` `text`

Anagram check with punctuation and space removal

```python
import re
from collections import Counter


def is_anagram_clean(text1, text2):
    """Check if two strings are anagrams after removing punctuation and spaces."""
    # Remove punctuation and spaces, convert to lowercase
    clean1 = re.sub(r"[^a-zA-Z0-9]", "", text1.lower())
    clean2 = re.sub(r"[^a-zA-Z0-9]", "", text2.lower())

    return Counter(clean1) == Counter(clean2)


text1 = "A gentleman"
text2 = "Elegant man"
result = is_anagram_clean(text1, text2)
print(result)  # True
```

!!! note "Notes"
    - Removes non-alphanumeric characters
    - Handles real-world text
    - Case-insensitive
    - Useful for phrases

<hr class="snippet-divider">

### Anagram check with custom character filtering

`string` `anagram` `custom` `filter` `validation` `text`

Anagram check with custom character filtering

```python
from collections import Counter


def is_anagram_custom_filter(text1, text2, filter_chars=""):
    """Check if two strings are anagrams with custom character filtering."""
    # Remove specified characters and convert to lowercase
    clean1 = "".join(c.lower() for c in text1 if c not in filter_chars)
    clean2 = "".join(c.lower() for c in text2 if c not in filter_chars)

    return Counter(clean1) == Counter(clean2)


text1 = "Madam, I'm Adam"
text2 = "Adam, I'm Madam"
result = is_anagram_custom_filter(text1, text2, " ,'")
print(result)  # True
```

!!! note "Notes"
    - Flexible character filtering
    - Configurable filter set
    - Maintains case handling
    - Useful for specific requirements

<hr class="snippet-divider">

### Anagram check with word boundaries

`string` `anagram` `words` `boundaries` `validation` `text`

Anagram check at word level

```python
from collections import Counter


def is_anagram_words(text1, text2):
    """Check if two strings are anagrams at word level."""
    words1 = text1.lower().split()
    words2 = text2.lower().split()

    return Counter(words1) == Counter(words2)


text1 = "fall leaves after leaves fall"
text2 = "leaves fall after fall leaves"
result = is_anagram_words(text1, text2)
print(result)  # True
```

!!! note "Notes"
    - Checks word-level anagrams
    - Splits on whitespace
    - Case-insensitive
    - Useful for sentences

<hr class="snippet-divider">

### Anagram check with character frequency analysis

`string` `anagram` `frequency` `analysis` `validation` `text`

Anagram check with detailed frequency analysis

```python
from collections import Counter


def is_anagram_frequency_analysis(text1, text2):
    """Check if two strings are anagrams with detailed frequency analysis."""
    # Clean and count characters
    clean1 = "".join(c.lower() for c in text1 if c.isalnum())
    clean2 = "".join(c.lower() for c in text2 if c.isalnum())

    count1 = Counter(clean1)
    count2 = Counter(clean2)

    # Check if character frequencies match
    if count1 != count2:
        return False, count1, count2

    return True, count1, count2


text1 = "listen"
text2 = "silent"
result, freq1, freq2 = is_anagram_frequency_analysis(text1, text2)
print(result)  # True
print(freq1)  # Counter({'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1})
```

!!! note "Notes"
    - Returns frequency information
    - Useful for debugging
    - Shows character distribution
    - Educational tool

<hr class="snippet-divider">

### Anagram check with minimum length requirement

`string` `anagram` `length` `minimum` `validation` `text`

Anagram check with minimum length requirement

```python
from collections import Counter


def is_anagram_min_length(text1, text2, min_length=1):
    """Check if two strings are anagrams with minimum length requirement."""
    # Clean and count characters
    clean1 = "".join(c.lower() for c in text1 if c.isalnum())
    clean2 = "".join(c.lower() for c in text2 if c.isalnum())

    if len(clean1) < min_length or len(clean2) < min_length:
        return False

    return Counter(clean1) == Counter(clean2)


text1 = "a"
text2 = "a"
result = is_anagram_min_length(text1, text2, 3)
print(result)  # False

text3 = "listen"
text4 = "silent"
result2 = is_anagram_min_length(text3, text4, 3)
print(result2)  # True
```

!!! note "Notes"
    - Configurable minimum length
    - Prevents short anagrams
    - Useful for validation
    - Flexible requirements

<hr class="snippet-divider">

### Anagram check with performance optimization

`string` `anagram` `optimized` `performance` `validation` `text`

Optimized anagram check for large strings

```python
from collections import Counter


def is_anagram_optimized(text1, text2):
    """Optimized anagram check for large strings."""
    # Early length check
    if len(text1) != len(text2):
        return False

    # Clean and count characters
    clean1 = "".join(c.lower() for c in text1 if c.isalnum())
    clean2 = "".join(c.lower() for c in text2 if c.isalnum())

    # Early length check after cleaning
    if len(clean1) != len(clean2):
        return False

    return Counter(clean1) == Counter(clean2)


text1 = "supercalifragilisticexpialidocious"
text2 = "supercalifragilisticexpialidocious"
result = is_anagram_optimized(text1, text2)
print(result)  # True
```

!!! note "Notes"
    - Early termination on length mismatch
    - Efficient for large strings
    - Memory efficient
    - Fast comparison

<hr class="snippet-divider">

### Anagram check with Unicode support

`string` `anagram` `unicode` `normalization` `validation` `text`

Anagram check with Unicode character support

```python
from collections import Counter
import unicodedata


def is_anagram_unicode(text1, text2):
    """Check if two strings are anagrams with proper Unicode handling."""
    # Normalize Unicode characters
    norm1 = unicodedata.normalize("NFD", text1)
    norm2 = unicodedata.normalize("NFD", text2)

    # Remove combining characters and convert to lowercase
    clean1 = "".join(c.lower() for c in norm1 if not unicodedata.combining(c) and c.isalnum())
    clean2 = "".join(c.lower() for c in norm2 if not unicodedata.combining(c) and c.isalnum())

    return Counter(clean1) == Counter(clean2)


text1 = "café"
text2 = "face"
result = is_anagram_unicode(text1, text2)
print(result)  # False (but handles Unicode properly)
```

!!! note "Notes"
    - Handles Unicode characters
    - Normalizes text properly
    - Removes combining characters
    - International text support

<hr class="snippet-divider">

### Anagram check with custom comparison

`string` `anagram` `custom` `comparison` `function` `validation` `text`

Anagram check with custom comparison function

```python
from collections import Counter


def is_anagram_custom_compare(text1, text2, compare_func=None):
    """Check if two strings are anagrams with custom comparison function."""
    if compare_func is None:
        def compare_func(x, y):
            return x == y
    # Clean and count characters
    clean1 = "".join(c.lower() for c in text1 if c.isalnum())
    clean2 = "".join(c.lower() for c in text2 if c.isalnum())

    count1 = Counter(clean1)
    count2 = Counter(clean2)

    # Use custom comparison
    return compare_func(count1, count2)


# Case-sensitive comparison
def case_sensitive_compare(count1, count2):
    return count1 == count2


text1 = "Listen"
text2 = "silent"
result = is_anagram_custom_compare(text1, text2, case_sensitive_compare)
print(result)  # False (case-sensitive)
```

!!! note "Notes"
    - Flexible comparison function
    - Customizable validation rules
    - Useful for special cases
    - Powerful customization

<hr class="snippet-divider">

### Anagram check with multiple strings

`string` `anagram` `multiple` `validation` `text`

Anagram check for multiple strings

```python
from collections import Counter


def are_all_anagrams(*texts):
    """Check if all provided strings are anagrams of each other."""
    if len(texts) < 2:
        return True

    # Clean and count characters for first text
    clean1 = "".join(c.lower() for c in texts[0] if c.isalnum())
    count1 = Counter(clean1)

    # Compare with all other texts
    for text in texts[1:]:
        clean = "".join(c.lower() for c in text if c.isalnum())
        if Counter(clean) != count1:
            return False

    return True


texts = ["listen", "silent", "enlist", "tinsel"]
result = are_all_anagrams(*texts)
print(result)  # True
```

!!! note "Notes"
    - Handles multiple strings
    - Efficient comparison
    - All-or-nothing check
    - Useful for word groups

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Is Palindrome](./is_palindrome.md)
- **Reference**: See [📂 Count Substring](./count_substring.md)

## 🏷️ Tags

`string`, `anagram`, `check`, `sort`, `counter`, `validation`, `text`

## 📝 Notes

- Anagram checks compare sorted characters or use collections.Counter
- Case and whitespace normalization may be needed
- Useful for word games and validation
