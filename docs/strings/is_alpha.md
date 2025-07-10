---
title: Check if String is Alphabetic
description: Check if a string contains alphabetic characters using the standard library.
keywords: alpha, characters, contains, custom, end, isalpha, islower, istitle, isupper, length, letter, letters, lowercase, maximum, minimum, range, spaces, start, string, text, title, uppercase, validation
---

# Check if String is Alphabetic

Check if a string contains alphabetic characters using the standard library.

12 snippets available in this sub-category.

---

## Simple

###  Check if string is alphabetic

`string` `alpha` `isalpha` `validation` `text`

Check if string contains only alphabetic characters

```python
def is_alpha(text):
    """Check if string contains only alphabetic characters."""
    return text.isalpha()


text = "Hello"
result = is_alpha(text)
print(result)  # True
```

!!! note "Notes"
    - Uses str.isalpha() method
    - Checks for letters only
    - Returns boolean
    - Simple validation

<hr class="snippet-divider">

### Check if string is alphabetic with spaces

`string` `alpha` `spaces` `validation` `text`

Check if string contains only alphabetic characters and spaces

```python
def is_alpha_with_spaces(text):
    """Check if string contains only alphabetic characters and spaces."""
    return all(c.isalpha() or c.isspace() for c in text)


text = "Hello World"
result = is_alpha_with_spaces(text)
print(result)  # True
```

!!! note "Notes"
    - Uses all() with generator expression
    - Allows spaces in text
    - Handles mixed content
    - Useful for names

<hr class="snippet-divider">

## Complex

###  Check if string is alphabetic with custom characters

`string` `alpha` `custom` `characters` `validation` `text`

Check if string contains alphabetic characters and custom allowed characters

```python
def is_alpha_custom(text, allowed_chars=""):
    """Check if string contains only alphabetic characters and custom allowed characters."""
    return all(c.isalpha() or c in allowed_chars for c in text)


text = "O'Connor"
result = is_alpha_custom(text, "'-")
print(result)  # True

text2 = "Smith-Jones"
result2 = is_alpha_custom(text2, "'-")
print(result2)  # True
```

!!! note "Notes"
    - Flexible character allowance
    - Handles names with hyphens/apostrophes
    - Customizable validation
    - Useful for name validation

<hr class="snippet-divider">

### Check if string starts with letter

`string` `alpha` `start` `letter` `validation` `text`

Check if string starts with an alphabetic character

```python
def starts_with_letter(text):
    """Check if string starts with an alphabetic character."""
    return bool(text and text[0].isalpha())


text = "Hello"
result = starts_with_letter(text)
print(result)  # True

text2 = "123Hello"
result2 = starts_with_letter(text2)
print(result2)  # False
```

!!! note "Notes"
    - Checks first character only
    - Handles empty strings
    - Simple position check
    - Useful for validation

<hr class="snippet-divider">

### Check if string ends with letter

`string` `alpha` `end` `letter` `validation` `text`

Check if string ends with an alphabetic character

```python
def ends_with_letter(text):
    """Check if string ends with an alphabetic character."""
    return bool(text and text[-1].isalpha())


text = "Hello"
result = ends_with_letter(text)
print(result)  # True

text2 = "Hello123"
result2 = ends_with_letter(text2)
print(result2)  # False
```

!!! note "Notes"
    - Checks last character only
    - Handles empty strings
    - Simple position check
    - Useful for validation

<hr class="snippet-divider">

### Check if string contains only uppercase letters

`string` `alpha` `uppercase` `isupper` `validation` `text`

Check if string contains only uppercase alphabetic characters

```python
def is_uppercase_alpha(text):
    """Check if string contains only uppercase alphabetic characters."""
    return text.isupper() and text.isalpha()


text = "HELLO"
result = is_uppercase_alpha(text)
print(result)  # True

text2 = "Hello"
result2 = is_uppercase_alpha(text2)
print(result2)  # False
```

!!! note "Notes"
    - Combines isupper() and isalpha()
    - Requires all uppercase letters
    - No mixed case allowed
    - Useful for acronyms

<hr class="snippet-divider">

### Check if string contains only lowercase letters

`string` `alpha` `lowercase` `islower` `validation` `text`

Check if string contains only lowercase alphabetic characters

```python
def is_lowercase_alpha(text):
    """Check if string contains only lowercase alphabetic characters."""
    return text.islower() and text.isalpha()


text = "hello"
result = is_lowercase_alpha(text)
print(result)  # True

text2 = "Hello"
result2 = is_lowercase_alpha(text2)
print(result2)  # False
```

!!! note "Notes"
    - Combines islower() and isalpha()
    - Requires all lowercase letters
    - No mixed case allowed
    - Useful for validation

<hr class="snippet-divider">

### Check if string is title case

`string` `alpha` `title` `istitle` `validation` `text`

Check if string is in title case format

```python
def is_title_case(text):
    """Check if string is in title case (first letter of each word capitalized)."""
    return text.istitle()


text = "Hello World"
result = is_title_case(text)
print(result)  # True

text2 = "hello world"
result2 = is_title_case(text2)
print(result2)  # False
```

!!! note "Notes"
    - Uses str.istitle() method
    - Checks word capitalization
    - Handles multiple words
    - Useful for formatting validation

<hr class="snippet-divider">

### Check if string contains specific letters

`string` `alpha` `contains` `letters` `validation` `text`

Check if string contains all specified letters

```python
def contains_specific_letters(text, required_letters):
    """Check if string contains all specified letters."""
    text_lower = text.lower()
    return all(letter.lower() in text_lower for letter in required_letters)


text = "Hello World"
result = contains_specific_letters(text, "hlw")
print(result)  # True

text2 = "Python"
result2 = contains_specific_letters(text2, "xyz")
print(result2)  # False
```

!!! note "Notes"
    - Case-insensitive matching
    - Checks for all required letters
    - Flexible letter requirements
    - Useful for word games

<hr class="snippet-divider">

### Check if string is alphabetic with minimum length

`string` `alpha` `length` `minimum` `validation` `text`

Check if string is alphabetic with minimum length requirement

```python
def is_alpha_min_length(text, min_length=1):
    """Check if string is alphabetic with minimum length requirement."""
    return text.isalpha() and len(text) >= min_length


text = "Hello"
result = is_alpha_min_length(text, 3)
print(result)  # True

text2 = "Hi"
result2 = is_alpha_min_length(text2, 3)
print(result2)  # False
```

!!! note "Notes"
    - Combines alphabetic check with length
    - Configurable minimum length
    - Useful for form validation
    - Prevents short inputs

<hr class="snippet-divider">

### Check if string is alphabetic with maximum length

`string` `alpha` `length` `maximum` `validation` `text`

Check if string is alphabetic with maximum length requirement

```python
def is_alpha_max_length(text, max_length):
    """Check if string is alphabetic with maximum length requirement."""
    return text.isalpha() and len(text) <= max_length


text = "Hello"
result = is_alpha_max_length(text, 10)
print(result)  # True

text2 = "Supercalifragilisticexpialidocious"
result2 = is_alpha_max_length(text2, 10)
print(result2)  # False
```

!!! note "Notes"
    - Combines alphabetic check with length
    - Configurable maximum length
    - Useful for form validation
    - Prevents overly long inputs

<hr class="snippet-divider">

### Check if string is alphabetic with length range

`string` `alpha` `length` `range` `validation` `text`

Check if string is alphabetic within specified length range

```python
def is_alpha_length_range(text, min_length=1, max_length=None):
    """Check if string is alphabetic within length range."""
    if not text.isalpha():
        return False

    length = len(text)
    if length < min_length:
        return False

    if max_length is not None and length > max_length:
        return False

    return True


text = "Hello"
result = is_alpha_length_range(text, 3, 10)
print(result)  # True

text2 = "Hi"
result2 = is_alpha_length_range(text2, 3, 10)
print(result2)  # False
```

!!! note "Notes"
    - Flexible length range checking
    - Optional maximum length
    - Comprehensive validation
    - Useful for form validation

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Is Alphanumeric](./is_alphanumeric.md)
- **Reference**: See [📂 Is Numeric](./is_numeric.md)

## 🏷️ Tags

`string`, `alpha`, `isalpha`, `validation`, `text`

## 📝 Notes

- Use str.isalpha() to check for alphabetic strings
- Returns True if all characters are letters
- Useful for input validation and parsing
