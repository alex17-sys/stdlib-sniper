# 🧩 Count substring occurrences
def count_substring(text, substring):
    """Count occurrences of substring in text."""
    return text.count(substring)


text = "hello world hello python hello"
count = count_substring(text, "hello")
print(count)  # 3


# 🧩 Count with case-insensitive matching
def count_substring_ignore_case(text, substring):
    """Count substring occurrences ignoring case."""
    return text.lower().count(substring.lower())


text = "Hello World HELLO Python hello"
count = count_substring_ignore_case(text, "hello")
print(count)  # 3


# 🧩 Count overlapping substrings
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


# 🧩 Count with word boundaries
import re


def count_word_occurrences(text, word):
    """Count word occurrences with word boundaries."""
    pattern = r"\b" + re.escape(word) + r"\b"
    matches = re.findall(pattern, text)
    return len(matches)


text = "hello world hello python hello-world"
count = count_word_occurrences(text, "hello")
print(count)  # 2 (excludes "hello-world")


# 🧩 Count multiple substrings
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


# 🧩 Count with position tracking
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
