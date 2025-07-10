---
title: Camel to Snake Case
description: Zero-dependency Python snippets for converting camelCase to snake_case using the standard library.
keywords: acronyms, camel, case, clean, convert, custom, regex, separator, snake, string, text
---

# Camel to Snake Case

Zero-dependency Python snippets for converting camelCase to snake_case using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Convert camelCase to snake_case

`string` `camel` `snake` `case` `convert` `regex` `text`

Convert camelCase string to snake_case

```python
import re


def camel_to_snake(text):
    """Convert camelCase to snake_case."""
    return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()


text = "camelCaseExample"
result = camel_to_snake(text)
print(result)  # "camel_case_example"
```

!!! note "Notes"
    - Uses regex to find capital letters
    - Inserts underscore before capitals
    - Converts to lowercase
    - Handles consecutive capitals correctly

<hr class="snippet-divider">

### Convert with underscore handling

`string` `camel` `snake` `case` `clean` `regex` `text`

Convert camelCase to snake_case with duplicate underscore removal

```python
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
```

!!! note "Notes"
    - Handles existing underscores
    - Removes duplicate underscores
    - Produces clean snake_case
    - Useful for variable name conversion

<hr class="snippet-divider">

## Complex

###  Convert with acronym handling

`string` `camel` `snake` `case` `acronyms` `regex` `text`

Convert camelCase to snake_case with acronym preservation

```python
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
```

!!! note "Notes"
    - Preserves acronyms as single units
    - Handles consecutive uppercase letters
    - Maintains readability
    - Useful for API naming conventions

<hr class="snippet-divider">

### Convert with custom separators

`string` `camel` `case` `convert` `separator` `custom` `text`

Convert camelCase to various case formats with custom separators

```python
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
```

!!! note "Notes"
    - Supports multiple case formats
    - Customizable separators
    - Flexible conversion options
    - Useful for different naming conventions

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Snake to Camel](./snake_to_camel.md)

## 🏷️ Tags

`string`, `camel`, `snake`, `case`, `convert`, `regex`, `text`

## 📝 Notes

- Use for converting camelCase to snake_case
- Handles acronyms and consecutive capitals
- See related snippet for reverse conversion
