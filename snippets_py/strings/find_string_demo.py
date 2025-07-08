# 🧩 Find substring position
text = "Hello World Python"
position = text.find("World")
print(position)  # 6


# 🧩 Find from specific position
text = "Hello World Hello Python"
position = text.find("Hello", 5)
print(position)  # 12


# 🧩 Find with end limit
text = "Hello World Python"
position = text.find("World", 0, 10)
print(position)  # 6

position = text.find("Python", 0, 10)
print(position)  # -1 (not found in range)


# 🧩 Check if substring exists
text = "Hello World Python"
if "World" in text:
    print("Found!")
else:
    print("Not found")


# 🧩 Find all occurrences
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


# 🧩 Find with case-insensitive search
def find_case_insensitive(text, substring):
    """Find substring case-insensitively."""
    return text.lower().find(substring.lower())


text = "Hello WORLD Python"
position = find_case_insensitive(text, "world")
print(position)  # 6


# 🧩 Find with regex pattern
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


# 🧩 Find with context
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


# 🧩 Find with multiple patterns
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
