# 🧩 Split string by delimiter
text = "apple,banana,orange,grape"
fruits = text.split(",")
print(fruits)


# 🧩 Split string by whitespace
text = "Hello   World   Python"
words = text.split()
print(words)


# 🧩 Split string with max splits
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


# 🧩 Split string with regex
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
