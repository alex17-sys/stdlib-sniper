# Snake to Camel Case

Zero-dependency Python snippets using only the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Convert snake_case to camelCase

`string` `snake` `camel` `case` `convert` `text`

Convert snake_case string to camelCase

```python
def snake_to_camel(text):
    """Convert snake_case to camelCase."""
    words = text.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])


text = "snake_case_example"
result = snake_to_camel(text)
print(result)  # "snakeCaseExample"
```

!!! note "Notes"
    - Splits by underscore
    - Capitalizes all words except first
    - Joins without separators
    - Handles multiple underscores

<hr class="snippet-divider">

### Convert with underscore cleaning

`string` `snake` `camel` `case` `clean` `regex` `text`

Convert snake_case to camelCase with underscore cleaning

```python
import re


def snake_to_camel_clean(text):
    """Convert snake_case to camelCase, handling multiple underscores."""
    # Remove leading/trailing underscores and replace multiple with single
    clean_text = re.sub(r"_+", "_", text.strip("_"))
    words = clean_text.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])


text = "__snake___case__example__"
result = snake_to_camel_clean(text)
print(result)  # "snakeCaseExample"
```

!!! note "Notes"
    - Removes leading/trailing underscores
    - Handles multiple consecutive underscores
    - Produces clean camelCase
    - Useful for data cleaning

<hr class="snippet-divider">

## Complex

###  Convert with acronym preservation

`string` `snake` `camel` `case` `acronyms` `preserve` `text`

Convert snake_case to camelCase with acronym preservation

```python
def snake_to_camel_with_acronyms(text):
    """Convert snake_case to camelCase with acronym preservation."""
    words = text.split("_")
    result = [words[0]]

    for word in words[1:]:
        if word.isupper():
            # Preserve acronyms as-is
            result.append(word)
        else:
            # Capitalize regular words
            result.append(word.capitalize())

    return "".join(result)


text = "http_request_url"
result = snake_to_camel_with_acronyms(text)
print(result)  # "httpRequestUrl"

text = "xml_parser_api"
result = snake_to_camel_with_acronyms(text)
print(result)  # "xmlParserApi"
```

!!! note "Notes"
    - Preserves existing acronyms
    - Handles mixed case words
    - Maintains readability
    - Useful for API conversions

<hr class="snippet-divider">

### Convert with custom options

`string` `snake` `case` `convert` `multiple` `formats` `text`

Convert snake_case to various case formats

```python
def snake_to_case(text, case="camel", separator=""):
    """Convert snake_case to various case formats."""
    words = text.split("_")

    if case == "camel":
        # camelCase: first word lowercase, rest capitalized
        return words[0] + "".join(word.capitalize() for word in words[1:])
    elif case == "pascal":
        # PascalCase: all words capitalized
        return "".join(word.capitalize() for word in words)
    elif case == "kebab":
        # kebab-case: lowercase with hyphens
        return "-".join(word.lower() for word in words)
    elif case == "title":
        # Title Case: capitalized with spaces
        return " ".join(word.capitalize() for word in words)
    else:
        return text


# Convert to different cases
text = "snake_case_example"

camel = snake_to_case(text, "camel")
print(camel)  # "snakeCaseExample"

pascal = snake_to_case(text, "pascal")
print(pascal)  # "SnakeCaseExample"

kebab = snake_to_case(text, "kebab")
print(kebab)  # "snake-case-example"

title = snake_to_case(text, "title")
print(title)  # "Snake Case Example"
```

!!! note "Notes"
    - Supports multiple case formats
    - Flexible conversion options
    - Handles different naming conventions
    - Useful for code generation

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Camel to Snake](./camel_to_snake.md)

## 🏷️ Tags

`string`, `snake`, `camel`, `case`, `convert`, `acronyms`, `formats`, `text`

## 📝 Notes

- Use for converting snake_case to camelCase and other formats
- Preserves acronyms and handles multiple naming conventions
- See related snippet for reverse conversion
