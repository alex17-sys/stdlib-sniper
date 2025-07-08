# 🧩 Check if string starts with prefix
def starts_with(text, prefix):
    """Check if string starts with prefix."""
    return text.startswith(prefix)


text = "Hello World"
result = starts_with(text, "Hello")
print(result)  # True


# 🧩 Check with case-insensitive matching
def starts_with_ignore_case(text, prefix):
    """Check if string starts with prefix ignoring case."""
    return text.lower().startswith(prefix.lower())


text = "Hello World"
result = starts_with_ignore_case(text, "hello")
print(result)  # True


# 🧩 Check multiple prefixes
def starts_with_any(text, prefixes):
    """Check if string starts with any of the prefixes."""
    return text.startswith(tuple(prefixes))


text = "Hello World"
prefixes = ["Hello", "Hi", "Hey"]
result = starts_with_any(text, prefixes)
print(result)  # True


# 🧩 Check with position offset
def starts_with_at_position(text, prefix, start=0, end=None):
    """Check if string starts with prefix at specific position."""
    return text.startswith(prefix, start, end)


text = "Hello World Python"
result = starts_with_at_position(text, "World", 6)
print(result)  # True


# 🧩 Check with regex pattern
import re


def starts_with_pattern(text, pattern):
    """Check if string starts with regex pattern."""
    return bool(re.match(pattern, text))


text = "Hello123World"
result = starts_with_pattern(text, r"Hello\d+")
print(result)  # True


# 🧩 Check with custom function
def starts_with_custom(text, check_func):
    """Check if string starts with custom condition."""
    if not text:
        return False
    return check_func(text[0])


text = "Hello World"
result = starts_with_custom(text, str.isupper)
print(result)  # True (starts with uppercase)


# 🧩 Check with multiple conditions
def starts_with_conditions(text, conditions):
    """Check if string starts with multiple conditions."""
    if not text:
        return False

    first_char = text[0]
    return all(condition(first_char) for condition in conditions)


text = "Hello World"
conditions = [str.isupper, lambda c: c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
result = starts_with_conditions(text, conditions)
print(result)  # True
