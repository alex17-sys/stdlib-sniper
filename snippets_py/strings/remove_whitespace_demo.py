# 🧩 Remove all whitespace
text = "  Hello   World  Python  "
no_whitespace = text.replace(" ", "").replace("\t", "").replace("\n", "")
print(no_whitespace)


# 🧩 Remove leading and trailing whitespace
text = "  Hello World  "
cleaned = text.strip()
print(cleaned)


# 🧩 Remove whitespace with custom characters
def remove_whitespace_custom(text, chars=None):
    """Remove specified whitespace characters from string."""
    if chars is None:
        chars = " \t\n\r\f\v"  # All whitespace characters

    result = text
    for char in chars:
        result = result.replace(char, "")
    return result


text = "  Hello\tWorld\nPython\r\n"
result = remove_whitespace_custom(text)
print(result)  # "HelloWorldPython"

# Remove only spaces and tabs
result = remove_whitespace_custom(text, " \t")
print(result)  # "HelloWorld\nPython\r\n"


# 🧩 Remove whitespace with normalization
import re


def normalize_whitespace(text, replace_with=" "):
    """Remove all whitespace and normalize to single spaces."""
    # Replace all whitespace sequences with single space
    normalized = re.sub(r"\s+", replace_with, text)
    # Remove leading/trailing whitespace
    return normalized.strip()


text = "  Hello   World\n\nPython\t\tProgramming  "
result = normalize_whitespace(text)
print(result)  # "Hello World Python Programming"

# Normalize to single character
result = normalize_whitespace(text, "")
print(result)  # "HelloWorldPythonProgramming"


# 🧩 Check if string is empty
def is_empty(text):
    """Check if string is empty or whitespace only."""
    return not text or not text.strip()


# Examples
print(is_empty(""))  # True
print(is_empty("   "))  # True
print(is_empty("Hello"))  # False
print(is_empty("\t\n"))  # True
