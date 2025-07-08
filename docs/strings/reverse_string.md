# Reverse String

Zero-dependency Python snippets using only the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Reverse string with slicing

`string` `reverse` `slice` `text`

Reverse a string using slice notation

```python
text = "Hello, World!"
reversed_text = text[::-1]
print(reversed_text)
```

!!! note "Notes"
    - Uses [::-1] slice to reverse
    - Most Pythonic and efficient method
    - Works with any string length
    - Preserves original string

<hr class="snippet-divider">

### Reverse string with reversed()

`string` `reverse` `reversed` `join` `text`

Reverse string using reversed() function

```python
text = "Hello, World!"
reversed_text = "".join(reversed(text))
print(reversed_text)
```

!!! note "Notes"
    - Uses reversed() function and join()
    - More explicit than slicing
    - Works with any iterable
    - Memory efficient for large strings

<hr class="snippet-divider">

## Complex

###  Reverse string with word preservation

`string` `reverse` `words` `preserve` `split` `join`

Reverse each word in string while preserving word order

```python
def reverse_string_preserve_words(text):
    """Reverse string while preserving word order."""
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)


text = "Hello World Python"
result = reverse_string_preserve_words(text)
print(result)  # "olleH dlroW nohtyP"
```

!!! note "Notes"
    - Reverses individual words
    - Keeps words in original order
    - Handles multiple spaces correctly
    - Useful for text processing

<hr class="snippet-divider">

### Reverse string with custom characters

`string` `reverse` `custom` `characters` `selective` `text`

Reverse string with selective character reversal

```python
def reverse_string_custom(text, reverse_chars=None):
    """Reverse string with option to reverse only specific characters."""
    if reverse_chars is None:
        return text[::-1]

    result = []
    for char in text:
        if char in reverse_chars:
            result.append(char)
        else:
            result.append(char)

    return "".join(result[::-1])


# Reverse only letters, keep punctuation in place
text = "Hello, World! How are you?"
result = reverse_string_custom(text, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(result)  # "uoy era woH !dlroW ,olleH"
```

!!! note "Notes"
    - Can reverse only specific character types
    - Preserves non-reversed characters
    - Useful for preserving punctuation
    - Flexible character selection

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Is Palindrome](./is_palindrome.md)
- **Reference**: See [📂 Is Anagram](./is_anagram.md)

## 🏷️ Tags

`string`, `reverse`, `slice`, `reversed`, `custom`, `text`

## 📝 Notes

- Use slicing [::-1] for most efficient reversal
- reversed() and join() work for iterables
- Useful for palindromes, puzzles, and text processing
