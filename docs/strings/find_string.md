---
title: Find String
description: Zero-dependency Python snippets for finding strings using the standard library.
keywords: all, case, contains, context, end, exists, find, insensitive, limit, multiple, occurrences, pattern, patterns, position, positions, range, regex, search, start, string, substring, surrounding, text
---

# Find String

Zero-dependency Python snippets for finding strings using the standard library.

9 snippets available in this sub-category.

---

## Simple

###  Find substring position

`string` `find` `substring` `position` `text`

Find first occurrence of substring

```python
text = "Hello World Python"
position = text.find("World")
print(position)  # 6
```

!!! note "Notes"
    - Uses str.find() method
    - Returns first occurrence index
    - Returns -1 if not found
    - Case-sensitive search

<hr class="snippet-divider">

### Find from specific position

`string` `find` `position` `start` `text`

Find substring starting from position

```python
text = "Hello World Hello Python"
position = text.find("Hello", 5)
print(position)  # 12
```

!!! note "Notes"
    - Starts search from specified index
    - Skips earlier occurrences
    - Useful for finding subsequent matches
    - Bounds checking included

<hr class="snippet-divider">

### Find with end limit

`string` `find` `range` `end` `limit` `text`

Find substring within range

```python
text = "Hello World Python"
position = text.find("World", 0, 10)
print(position)  # 6

position = text.find("Python", 0, 10)
print(position)  # -1 (not found in range)
```

!!! note "Notes"
    - Limits search to specific range
    - End index is exclusive
    - Useful for bounded searches
    - Efficient for large strings

<hr class="snippet-divider">

### Check if substring exists

`string` `find` `contains` `exists` `text`

Check for substring existence

```python
text = "Hello World Python"
if "World" in text:
    print("Found!")
else:
    print("Not found")
```

!!! note "Notes"
    - Uses 'in' operator
    - Returns boolean result
    - More readable than find() != -1
    - Common pattern for existence checks

<hr class="snippet-divider">

## Complex

###  Find all occurrences

`string` `find` `all` `occurrences` `positions` `text`

Find all positions of substring

```python
def find_all_occurrences(text, substring):
    """Find all positions of substring."""
    positions = []
    start = 0

    while True:
        pos = text.find(substring, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1

    return positions


text = "Hello World Hello Python Hello"
positions = find_all_occurrences(text, "Hello")
print(positions)  # [0, 12, 24]
```

!!! note "Notes"
    - Returns list of all positions
    - Handles overlapping matches
    - Efficient iteration
    - Useful for comprehensive search

<hr class="snippet-divider">

### Find with case-insensitive search

`string` `find` `case` `insensitive` `text`

Find substring ignoring case

```python
def find_case_insensitive(text, substring):
    """Find substring case-insensitively."""
    return text.lower().find(substring.lower())


text = "Hello WORLD Python"
position = find_case_insensitive(text, "world")
print(position)  # 6
```

!!! note "Notes"
    - Converts both strings to lowercase
    - Handles mixed case variations
    - Returns position in original string
    - Simple case-insensitive search

<hr class="snippet-divider">

### Find with regex pattern

`string` `find` `regex` `pattern` `search` `text`

Find text using regex patterns

```python
import re


def find_regex_pattern(text, pattern):
    """Find text using regex pattern."""
    match = re.search(pattern, text)
    if match:
        return match.start(), match.end(), match.group()
    return None


text = "Hello 123 World 456 Python"

# Find first number
result = find_regex_pattern(text, r"\d+")
if result:
    start, end, match = result
    print(f"Found '{match}' at position {start}-{end}")

# Find word starting with 'P'
result = find_regex_pattern(text, r"\bP\w+")
if result:
    start, end, match = result
    print(f"Found '{match}' at position {start}-{end}")
```

!!! note "Notes"
    - Uses regex for complex patterns
    - Returns start, end, and matched text
    - Flexible pattern matching
    - Powerful search capabilities

<hr class="snippet-divider">

### Find with context

`string` `find` `context` `surrounding` `text`

Find substring with surrounding context

```python
def find_with_context(text, substring, context_chars=10):
    """Find substring with surrounding context."""
    position = text.find(substring)
    if position == -1:
        return None

    start = max(0, position - context_chars)
    end = min(len(text), position + len(substring) + context_chars)

    context = text[start:end]
    return {"position": position, "context": context, "context_start": start, "context_end": end}


text = "This is a long text with Hello World in the middle"
result = find_with_context(text, "Hello World", 15)
if result:
    print(f"Found at position {result['position']}")
    print(f"Context: ...{result['context']}...")
```

!!! note "Notes"
    - Returns surrounding text
    - Configurable context size
    - Handles string boundaries
    - Useful for text analysis

<hr class="snippet-divider">

### Find with multiple patterns

`string` `find` `multiple` `patterns` `text`

Find multiple patterns simultaneously

```python
def find_multiple_patterns(text, patterns):
    """Find multiple patterns in text."""
    results = {}

    for pattern_name, pattern in patterns.items():
        position = text.find(pattern)
        results[pattern_name] = position if position != -1 else None

    return results


text = "Hello World Python Programming"

patterns = {
    "greeting": "Hello",
    "language": "Python",
    "action": "Programming",
    "missing": "JavaScript",
}

results = find_multiple_patterns(text, patterns)
for pattern, position in results.items():
    if position is not None:
        print(f"'{pattern}' found at position {position}")
    else:
        print(f"'{pattern}' not found")
```

!!! note "Notes"
    - Searches for multiple patterns
    - Returns dictionary of results
    - Efficient single pass through text
    - Useful for pattern analysis

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Replace String](./replace_string.md)

## 🏷️ Tags

`string`, `find`, `context`, `surrounding`, `multiple`, `patterns`, `text`

## 📝 Notes

- Use str.find() for substring search
- Can search for multiple patterns at once
- Context extraction is useful for text analysis
- See related snippet for replacing found text
