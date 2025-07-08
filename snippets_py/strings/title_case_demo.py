# 🧩 Convert to title case
text = "hello world python programming"
title_text = text.title()
print(title_text)


# 🧩 Title case with custom separator
text = "hello-world-python"
title_text = text.replace("-", " ").title().replace(" ", "-")
print(title_text)


# 🧩 Title case with minor word exceptions
def title_case_smart(text, minor_words=None):
    """Convert to title case with minor word exceptions."""
    if minor_words is None:
        minor_words = {
            "a",
            "an",
            "and",
            "as",
            "at",
            "but",
            "by",
            "for",
            "in",
            "of",
            "on",
            "or",
            "the",
            "to",
            "up",
            "yet",
        }

    words = text.lower().split()
    if not words:
        return text

    result = [words[0].capitalize()]  # Always capitalize first word

    for word in words[1:]:
        if word in minor_words:
            result.append(word)
        else:
            result.append(word.capitalize())

    return " ".join(result)


text = "the quick brown fox jumps over the lazy dog"
result = title_case_smart(text)
print(result)  # "The Quick Brown Fox Jumps over the Lazy Dog"


# 🧩 Title case with special character handling
import re


def title_case_advanced(text):
    """Convert to title case with special character handling."""
    # Define minor words
    minor_words = {
        "a",
        "an",
        "and",
        "as",
        "at",
        "but",
        "by",
        "for",
        "in",
        "of",
        "on",
        "or",
        "the",
        "to",
        "up",
        "yet",
    }

    # Split by word boundaries, preserving punctuation
    parts = re.split(r"(\b\w+\b)", text)
    result = []

    for i, part in enumerate(parts):
        if re.match(r"\b\w+\b", part):  # It's a word
            if i == 0 or i == len(parts) - 1:  # First or last word
                result.append(part.capitalize())
            elif part.lower() in minor_words:
                result.append(part.lower())
            else:
                result.append(part.capitalize())
        else:  # It's punctuation or whitespace
            result.append(part)

    return "".join(result)


text = "the quick brown fox jumps over the lazy dog!"
result = title_case_advanced(text)
print(result)  # "The Quick Brown Fox Jumps over the Lazy Dog!"
