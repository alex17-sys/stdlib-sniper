# Count Substring Occurrences

Count the number of times a substring appears in a string using the standard library.

## Simple

### 🧩 Count substring occurrences

```python
def count_substring(text, substring):
    """Count occurrences of substring in text."""
    return text.count(substring)


text = "hello world hello python hello"
count = count_substring(text, "hello")
print(count)  # 3
```

📂 Count occurrences of a substring in a string

🏷️ Tags: string, count, substring, occurrences, text
📝 Notes:
- Uses str.count() method
- Case-sensitive matching
- Returns integer count
- Simple and efficient

### 🧩 Count with case-insensitive matching

```python
def count_substring_ignore_case(text, substring):
    """Count substring occurrences ignoring case."""
    return text.lower().count(substring.lower())


text = "Hello World HELLO Python hello"
count = count_substring_ignore_case(text, "hello")
print(count)  # 3
```

📂 Count substring occurrences ignoring case differences

🏷️ Tags: string, count, substring, case-insensitive, text
📝 Notes:
- Converts both strings to lowercase
- Handles mixed case text
- Useful for user input matching
- Maintains original text

## Complex

### 🧩 Count overlapping substrings

```python
def count_overlapping_substrings(text, substring):
    """Count overlapping substring occurrences."""
    count = 0
    start = 0
    while True:
        pos = text.find(substring, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1
    return count


text = "aaaa"
count = count_overlapping_substrings(text, "aa")
print(count)  # 3 (positions: 0, 1, 2)
```

📂 Count overlapping substring occurrences

🏷️ Tags: string, count, substring, overlapping, find, text
📝 Notes:
- Handles overlapping matches
- Uses str.find() with start position
- More complex than str.count()
- Useful for pattern analysis

### 🧩 Count with word boundaries

```python
import re


def count_word_occurrences(text, word):
    """Count word occurrences with word boundaries."""
    pattern = r"\b" + re.escape(word) + r"\b"
    matches = re.findall(pattern, text)
    return len(matches)


text = "hello world hello python hello-world"
count = count_word_occurrences(text, "hello")
print(count)  # 2 (excludes "hello-world")
```

📂 Count word occurrences with proper boundaries

🏷️ Tags: string, count, word, boundaries, regex, text
📝 Notes:
- Uses regex word boundaries
- Excludes partial matches
- Handles punctuation
- More precise than simple count

### 🧩 Count multiple substrings

```python
def count_multiple_substrings(text, substrings):
    """Count occurrences of multiple substrings."""
    results = {}
    for substring in substrings:
        results[substring] = text.count(substring)
    return results


text = "hello world hello python world"
substrings = ["hello", "world", "python"]
counts = count_multiple_substrings(text, substrings)
print(counts)  # {'hello': 2, 'world': 2, 'python': 1}
```

📂 Count occurrences of multiple substrings at once

🏷️ Tags: string, count, multiple, substrings, dictionary, text
📝 Notes:
- Returns dictionary of counts
- Efficient for multiple searches
- Useful for text analysis
- Batch processing approach

### 🧩 Count with position tracking

```python
def count_substring_positions(text, substring):
    """Count substring and return all positions."""
    positions = []
    start = 0
    while True:
        pos = text.find(substring, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return len(positions), positions


text = "hello world hello python hello"
count, positions = count_substring_positions(text, "hello")
print(f"Count: {count}, Positions: {positions}")
# Count: 3, Positions: [0, 12, 24]
```

📂 Count substring and track all occurrence positions

🏷️ Tags: string, count, substring, positions, tracking, text
📝 Notes:
- Returns both count and positions
- Useful for text processing
- Enables position-based operations
- Combines counting and finding

## 🔗 Cross-References

- **Reference**: See [📂 Find String](./find_string.md)
- **Reference**: See [📂 Is Anagram](./is_anagram.md)

## 🏷️ Tags

`string`, `count`, `substring`, `find`, `frequency`, `text`

## 📝 Notes

- Use str.count() for non-overlapping substring counts
- Use regex for overlapping or complex patterns
- Useful for text analysis and validation
