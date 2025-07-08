# Split String

Zero-dependency Python snippets for splitting strings using the standard library.

## Simple

### 🧩 Split string by delimiter

```python
text = "apple,banana,orange,grape"
fruits = text.split(",")
print(fruits)
```

📂 Split string by comma delimiter

🏷️ Tags: string, split, delimiter, comma, text
📝 Notes:
- Uses str.split() method
- Returns list of substrings
- Removes delimiter from result
- Handles consecutive delimiters

### 🧩 Split string by whitespace

```python
text = "Hello   World   Python"
words = text.split()
print(words)
```

📂 Split string by whitespace (default)

🏷️ Tags: string, split, whitespace, words, text
📝 Notes:
- Default split behavior
- Handles multiple spaces
- Removes leading/trailing whitespace
- Most common string splitting

## Complex

### 🧩 Split string with max splits

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

📂 Split string with limit on number of splits

🏷️ Tags: string, split, limit, max, splits, text
📝 Notes:
- Controls number of splits
- Useful for parsing structured data
- Preserves remaining text
- Flexible delimiter options

### 🧩 Split string with regex

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

📂 Split string using regex patterns

🏷️ Tags: string, split, regex, pattern, multiple, delimiters, text
📝 Notes:
- Uses regex for complex patterns
- Multiple delimiter support
- Flexible pattern matching
- Powerful splitting capabilities

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
