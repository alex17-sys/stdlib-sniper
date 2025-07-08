# 🧩 Normalize multiple spaces to single
import re

text = "Hello   World    Python"
normalized = re.sub(r" +", " ", text)
print(normalized)


# 🧩 Normalize all whitespace
import re

text = "Hello\t\tWorld\n\nPython\r\nProgramming"
normalized = re.sub(r"\s+", " ", text).strip()
print(normalized)


# 🧩 Normalize whitespace with preservation
import re


def normalize_whitespace_preserve(text, preserve_newlines=True):
    """Normalize whitespace while optionally preserving newlines."""
    if preserve_newlines:
        # Replace multiple spaces/tabs with single space
        text = re.sub(r"[ \t]+", " ", text)
        # Replace multiple newlines with single newline
        text = re.sub(r"\n+", "\n", text)
        # Remove leading/trailing whitespace from each line
        lines = [line.strip() for line in text.split("\n")]
        return "\n".join(lines)
    else:
        # Normalize all whitespace to single spaces
        return re.sub(r"\s+", " ", text).strip()


text = "  Hello   World\n\nPython\t\tProgramming  "
result = normalize_whitespace_preserve(text, preserve_newlines=True)
print(result)  # "Hello World\nPython Programming"


# 🧩 Normalize whitespace with custom rules
import re


def normalize_whitespace_advanced(text, rules=None):
    """Normalize whitespace with custom rules."""
    if rules is None:
        rules = {
            "spaces": "single",  # 'single', 'remove', 'preserve'
            "tabs": "spaces",  # 'spaces', 'remove', 'preserve'
            "newlines": "single",  # 'single', 'remove', 'preserve'
            "leading_trailing": True,  # Remove leading/trailing whitespace
        }

    result = text

    # Handle spaces
    if rules["spaces"] == "single":
        result = re.sub(r" +", " ", result)
    elif rules["spaces"] == "remove":
        result = result.replace(" ", "")

    # Handle tabs
    if rules["tabs"] == "spaces":
        result = result.replace("\t", " ")
    elif rules["tabs"] == "remove":
        result = result.replace("\t", "")

    # Handle newlines
    if rules["newlines"] == "single":
        result = re.sub(r"\n+", "\n", result)
    elif rules["newlines"] == "remove":
        result = result.replace("\n", " ")

    # Handle leading/trailing whitespace
    if rules["leading_trailing"]:
        result = result.strip()

    return result


# Custom normalization rules
text = "  Hello\t\tWorld\n\nPython\r\nProgramming  "
rules = {"spaces": "single", "tabs": "spaces", "newlines": "remove", "leading_trailing": True}
result = normalize_whitespace_advanced(text, rules)
print(result)  # "Hello World Python Programming"
