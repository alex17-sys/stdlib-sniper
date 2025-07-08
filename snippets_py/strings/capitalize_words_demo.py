# 🧩 Capitalize first letter of each word
text = "hello world python"
capitalized = text.title()
print(capitalized)


# 🧩 Capitalize first letter only
text = "hello world python"
capitalized = text.capitalize()
print(capitalized)


# 🧩 Capitalize words with custom exceptions
def capitalize_words_custom(text, exceptions=None):
    """Capitalize words except for specified exceptions."""
    if exceptions is None:
        exceptions = {
            "a",
            "an",
            "the",
            "and",
            "or",
            "but",
            "in",
            "on",
            "at",
            "to",
            "for",
            "of",
            "with",
            "by",
        }

    words = text.lower().split()
    result = []

    for i, word in enumerate(words):
        if i == 0 or word not in exceptions:
            result.append(word.capitalize())
        else:
            result.append(word)

    return " ".join(result)


text = "the quick brown fox jumps over the lazy dog"
result = capitalize_words_custom(text)
print(result)  # "The Quick Brown Fox Jumps over the Lazy Dog"


# 🧩 Capitalize words with special handling
import re


def capitalize_words_advanced(text):
    """Capitalize words with special handling for contractions and hyphens."""
    # Handle contractions (don't, can't, etc.)
    text = re.sub(
        r"\b(\w+)\'(\w+)\b", lambda m: m.group(1).capitalize() + "'" + m.group(2).lower(), text
    )

    # Handle hyphenated words
    text = re.sub(
        r"\b(\w+)-(\w+)\b", lambda m: m.group(1).capitalize() + "-" + m.group(2).capitalize(), text
    )

    # Handle regular words
    words = text.split()
    result = []

    for word in words:
        if not re.match(r".*[\'-].*", word):  # Not a contraction or hyphenated
            result.append(word.capitalize())
        else:
            result.append(word)

    return " ".join(result)


text = "don't forget the e-mail and co-worker"
result = capitalize_words_advanced(text)
print(result)  # "Don't Forget the E-Mail and Co-Worker"
