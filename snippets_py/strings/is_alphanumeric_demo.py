# 🧩 Check if string is alphanumeric
def is_alphanumeric(text):
    """Check if string contains only alphanumeric characters."""
    return text.isalnum()


text = "Hello123"
result = is_alphanumeric(text)
print(result)  # True


# 🧩 Check if string is alphanumeric with spaces
def is_alphanumeric_with_spaces(text):
    """Check if string contains only alphanumeric characters and spaces."""
    return all(c.isalnum() or c.isspace() for c in text)


text = "Hello 123 World"
result = is_alphanumeric_with_spaces(text)
print(result)  # True


# 🧩 Check if string is alphanumeric with custom characters
def is_alphanumeric_custom(text, allowed_chars=""):
    """Check if string contains only alphanumeric characters and custom allowed characters."""
    return all(c.isalnum() or c in allowed_chars for c in text)


text = "User123-Name"
result = is_alphanumeric_custom(text, "-_")
print(result)  # True

text2 = "Product@Name"
result2 = is_alphanumeric_custom(text2, "-_")
print(result2)  # False


# 🧩 Check if string contains at least one letter and one digit
def has_letter_and_digit(text):
    """Check if string contains at least one letter and one digit."""
    has_letter = any(c.isalpha() for c in text)
    has_digit = any(c.isdigit() for c in text)
    return has_letter and has_digit


text = "Hello123"
result = has_letter_and_digit(text)
print(result)  # True

text2 = "Hello"
result2 = has_letter_and_digit(text2)
print(result2)  # False


# 🧩 Check if string is alphanumeric with minimum length
def is_alphanumeric_min_length(text, min_length=1):
    """Check if string is alphanumeric with minimum length requirement."""
    return text.isalnum() and len(text) >= min_length


text = "Hello123"
result = is_alphanumeric_min_length(text, 5)
print(result)  # True

text2 = "Hi1"
result2 = is_alphanumeric_min_length(text2, 5)
print(result2)  # False


# 🧩 Check if string is alphanumeric with maximum length
def is_alphanumeric_max_length(text, max_length):
    """Check if string is alphanumeric with maximum length requirement."""
    return text.isalnum() and len(text) <= max_length


text = "Hello123"
result = is_alphanumeric_max_length(text, 10)
print(result)  # True

text2 = "VeryLongAlphanumericString123"
result2 = is_alphanumeric_max_length(text2, 10)
print(result2)  # False


# 🧩 Check if string is alphanumeric with length range
def is_alphanumeric_length_range(text, min_length=1, max_length=None):
    """Check if string is alphanumeric within length range."""
    if not text.isalnum():
        return False

    length = len(text)
    if length < min_length:
        return False

    if max_length is not None and length > max_length:
        return False

    return True


text = "Hello123"
result = is_alphanumeric_length_range(text, 5, 15)
print(result)  # True

text2 = "Hi1"
result2 = is_alphanumeric_length_range(text2, 5, 15)
print(result2)  # False


# 🧩 Check if string starts with alphanumeric
def starts_with_alphanumeric(text):
    """Check if string starts with an alphanumeric character."""
    return bool(text and text[0].isalnum())


text = "Hello123"
result = starts_with_alphanumeric(text)
print(result)  # True

text2 = "!Hello123"
result2 = starts_with_alphanumeric(text2)
print(result2)  # False


# 🧩 Check if string ends with alphanumeric
def ends_with_alphanumeric(text):
    """Check if string ends with an alphanumeric character."""
    return bool(text and text[-1].isalnum())


text = "Hello123"
result = ends_with_alphanumeric(text)
print(result)  # True

text2 = "Hello123!"
result2 = ends_with_alphanumeric(text2)
print(result2)  # False


# 🧩 Check if string contains specific alphanumeric pattern
def matches_alphanumeric_pattern(text, pattern):
    """Check if string matches alphanumeric pattern."""
    import re

    return bool(re.match(pattern, text))


text = "Hello123"
result = matches_alphanumeric_pattern(text, r"^[A-Za-z]+\d+$")
print(result)  # True

text2 = "123Hello"
result2 = matches_alphanumeric_pattern(text2, r"^[A-Za-z]+\d+$")
print(result2)  # False


# 🧩 Check if string is valid identifier
def is_valid_identifier(text):
    """Check if string is a valid Python identifier."""
    return text.isidentifier()


text = "hello_123"
result = is_valid_identifier(text)
print(result)  # True

text2 = "123hello"
result2 = is_valid_identifier(text2)
print(result2)  # False


# 🧩 Check if string is valid username
def is_valid_username(text, min_length=3, max_length=20):
    """Check if string is a valid username."""
    if not text:
        return False

    # Check length
    if len(text) < min_length or len(text) > max_length:
        return False

    # Check if starts with letter
    if not text[0].isalpha():
        return False

    # Check if contains only alphanumeric and underscore
    return all(c.isalnum() or c == "_" for c in text)


text = "user_123"
result = is_valid_username(text)
print(result)  # True

text2 = "123user"
result2 = is_valid_username(text2)
print(result2)  # False
