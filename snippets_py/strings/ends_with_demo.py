# 🧩 Check if string ends with suffix
def ends_with(text, suffix):
    """Check if string ends with suffix."""
    return text.endswith(suffix)


text = "Hello World"
result = ends_with(text, "World")
print(result)  # True


# 🧩 Check with case-insensitive matching
def ends_with_ignore_case(text, suffix):
    """Check if string ends with suffix ignoring case."""
    return text.lower().endswith(suffix.lower())


text = "Hello World"
result = ends_with_ignore_case(text, "world")
print(result)  # True


# 🧩 Check multiple suffixes
def ends_with_any(text, suffixes):
    """Check if string ends with any of the suffixes."""
    return text.endswith(tuple(suffixes))


text = "Hello World"
suffixes = ["World", "Python", "Java"]
result = ends_with_any(text, suffixes)
print(result)  # True


# 🧩 Check with position offset
def ends_with_at_position(text, suffix, start=0, end=None):
    """Check if string ends with suffix at specific position."""
    return text.endswith(suffix, start, end)


text = "Hello World Python"
result = ends_with_at_position(text, "World", 0, 11)
print(result)  # True


# 🧩 Check file extensions
def has_file_extension(filename, extensions):
    """Check if filename has specific extension(s)."""
    return filename.lower().endswith(tuple(ext.lower() for ext in extensions))


filename = "document.PDF"
extensions = [".pdf", ".doc", ".txt"]
result = has_file_extension(filename, extensions)
print(result)  # True


# 🧩 Check with regex pattern
import re


def ends_with_pattern(text, pattern):
    """Check if string ends with regex pattern."""
    return bool(re.search(pattern + "$", text))


text = "Hello123World"
result = ends_with_pattern(text, r"\d+World$")
print(result)  # True


# 🧩 Check with custom function
def ends_with_custom(text, check_func):
    """Check if string ends with custom condition."""
    if not text:
        return False
    return check_func(text[-1])


text = "Hello World"
result = ends_with_custom(text, str.isalpha)
print(result)  # True (ends with letter)


# 🧩 Check with multiple conditions
def ends_with_conditions(text, conditions):
    """Check if string ends with multiple conditions."""
    if not text:
        return False

    last_char = text[-1]
    return all(condition(last_char) for condition in conditions)


text = "Hello World"
conditions = [str.isalpha, lambda c: c in "abcdefghijklmnopqrstuvwxyz"]
result = ends_with_conditions(text, conditions)
print(result)  # True


# 🧩 Check with word boundaries
import re


def ends_with_word(text, word):
    """Check if string ends with complete word."""
    pattern = r"\b" + re.escape(word) + r"$"
    return bool(re.search(pattern, text))


text = "Hello World"
result = ends_with_word(text, "World")
print(result)  # True

text2 = "Hello World!"
result2 = ends_with_word(text2, "World")
print(result2)  # False (ends with punctuation)
