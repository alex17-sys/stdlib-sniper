# 🧩 Convert camelCase to snake_case
import re


def camel_to_snake(text):
    """Convert camelCase to snake_case."""
    return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()


text = "camelCaseExample"
result = camel_to_snake(text)
print(result)  # "camel_case_example"


# 🧩 Convert with underscore handling
import re


def camel_to_snake_clean(text):
    """Convert camelCase to snake_case, handling existing underscores."""
    # First convert to snake_case
    snake = re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()
    # Remove duplicate underscores
    return re.sub(r"_+", "_", snake)


text = "camelCase_Example"
result = camel_to_snake_clean(text)
print(result)  # "camel_case_example"


# 🧩 Convert with acronym handling
import re


def camel_to_snake_with_acronyms(text):
    """Convert camelCase to snake_case with proper acronym handling."""
    # Handle consecutive uppercase letters (acronyms)
    text = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", text)
    # Handle single uppercase letters
    text = re.sub(r"([a-z])([A-Z])", r"\1_\2", text)
    # Convert to lowercase
    return text.lower()


text = "HTTPRequest"
result = camel_to_snake_with_acronyms(text)
print(result)  # "http_request"

text = "XMLParser"
result = camel_to_snake_with_acronyms(text)
print(result)  # "xml_parser"


# 🧩 Convert with custom separators
import re


def camel_to_case(text, separator="_", case="lower"):
    """Convert camelCase to custom case with specified separator."""
    # Convert camelCase to snake_case first
    snake = re.sub(r"(?<!^)(?=[A-Z])", "_", text)

    # Apply case conversion
    if case == "lower":
        result = snake.lower()
    elif case == "upper":
        result = snake.upper()
    elif case == "title":
        result = snake.title()
    else:
        result = snake

    # Replace underscores with custom separator
    if separator != "_":
        result = result.replace("_", separator)

    return result


# Convert to kebab-case
text = "camelCaseExample"
kebab = camel_to_case(text, separator="-", case="lower")
print(kebab)  # "camel-case-example"

# Convert to UPPER_SNAKE_CASE
upper_snake = camel_to_case(text, separator="_", case="upper")
print(upper_snake)  # "CAMEL_CASE_EXAMPLE"
