# Reverse String

Zero-dependency Python snippets for reversing strings using the standard library.

## Simple

### 🧩 Reverse string with slicing

```python
text = "Hello, World!"
reversed_text = text[::-1]
print(reversed_text)
```

📂 Reverse a string using slice notation

🏷️ Tags: string, reverse, slice, text
📝 Notes:
- Uses [::-1] slice to reverse
- Most Pythonic and efficient method
- Works with any string length
- Preserves original string

### 🧩 Reverse string with reversed()

```python
text = "Hello, World!"
reversed_text = "".join(reversed(text))
print(reversed_text)
```

📂 Reverse string using reversed() function

🏷️ Tags: string, reverse, reversed, join, text
📝 Notes:
- Uses reversed() function and join()
- More explicit than slicing
- Works with any iterable
- Memory efficient for large strings

## Complex

### 🧩 Reverse string with word preservation

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

📂 Reverse each word in string while preserving word order

🏷️ Tags: string, reverse, words, preserve, split, join
📝 Notes:
- Reverses individual words
- Keeps words in original order
- Handles multiple spaces correctly
- Useful for text processing

### 🧩 Reverse string with custom characters

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

📂 Reverse string with selective character reversal

🏷️ Tags: string, reverse, custom, characters, selective, text
📝 Notes:
- Can reverse only specific character types
- Preserves non-reversed characters
- Useful for preserving punctuation
- Flexible character selection

## 🔗 Cross-References

- **Reference**: See [📂 Is Palindrome](./is_palindrome.md)
- **Reference**: See [📂 Is Anagram](./is_anagram.md)

## 🏷️ Tags

`string`, `reverse`, `slice`, `reversed`, `custom`, `text`

## 📝 Notes

- Use slicing [::-1] for most efficient reversal
- reversed() and join() work for iterables
- Useful for palindromes, puzzles, and text processing
