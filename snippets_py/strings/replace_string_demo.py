# 🧩 Replace substring
text = "Hello World"
result = text.replace("World", "Python")
print(result)  # "Hello Python"


# 🧩 Replace multiple occurrences
text = "Hello Hello Hello"
result = text.replace("Hello", "Hi")
print(result)  # "Hi Hi Hi"


# 🧩 Replace with count limit
text = "Hello Hello Hello"
result = text.replace("Hello", "Hi", 2)
print(result)  # "Hi Hi Hello"


# 🧩 Replace with case-insensitive matching
import re


def replace_case_insensitive(text, old, new):
    """Replace text case-insensitively."""
    pattern = re.compile(re.escape(old), re.IGNORECASE)
    return pattern.sub(new, text)


text = "Hello WORLD hello World"
result = replace_case_insensitive(text, "hello", "Hi")
print(result)  # "Hi WORLD Hi World"


# 🧩 Replace with custom function
import re


def replace_with_function(text, pattern, replacement_func):
    """Replace using custom function."""

    def replacer(match):
        return replacement_func(match.group(0))

    return re.sub(pattern, replacer, text)


text = "Hello 123 World 456 Python"


# Replace numbers with doubled values
def double_number(match):
    num = int(match.group(0))
    return str(num * 2)


result = replace_with_function(text, r"\d+", double_number)
print(result)  # "Hello 246 World 912 Python"


# 🧩 Replace with conditional logic
def replace_conditional(text, replacements, condition_func=None):
    """Replace text with conditional logic."""
    if condition_func is None:

        def condition_func(x):
            return True

    result = text
    for old, new in replacements.items():
        if condition_func(old):
            result = result.replace(old, new)

    return result


text = "Hello World Python"

# Replace only short words
replacements = {"Hello": "Hi", "World": "Earth", "Python": "Programming"}


def is_short_word(word):
    return len(word) <= 5


result = replace_conditional(text, replacements, is_short_word)
print(result)  # "Hi Earth Python"


# 🧩 Replace with context awareness
import re


def replace_with_context(text, target, replacement, context_chars=10):
    """Replace text with context awareness."""
    pattern = f".{{0,{context_chars}}}{re.escape(target)}.{{0,{context_chars}}}"

    def replacer(match):
        match_text = match.group(0)
        start = match_text.find(target)
        end = start + len(target)

        # Check context before replacing
        before = match_text[:start]
        after = match_text[end:]

        # Example: only replace if surrounded by spaces
        if before.strip() == "" and after.strip() == "":
            return match_text[:start] + replacement + match_text[end:]
        return match_text

    return re.sub(pattern, replacer, text)


text = "Hello World, HelloPython, Hello World"
result = replace_with_context(text, "Hello", "Hi")
print(result)  # "Hi World, HelloPython, Hi World"
