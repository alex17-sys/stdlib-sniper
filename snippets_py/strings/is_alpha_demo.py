# 🧩 Check if string is alphabetic
def is_alpha(text):
    """Check if string contains only alphabetic characters."""
    return text.isalpha()


text = "Hello"
result = is_alpha(text)
print(result)  # True


# 🧩 Check if string is alphabetic with spaces
def is_alpha_with_spaces(text):
    """Check if string contains only alphabetic characters and spaces."""
    return all(c.isalpha() or c.isspace() for c in text)


text = "Hello World"
result = is_alpha_with_spaces(text)
print(result)  # True


# 🧩 Check if string is alphabetic with custom characters
def is_alpha_custom(text, allowed_chars=""):
    """Check if string contains only alphabetic characters and custom allowed characters."""
    return all(c.isalpha() or c in allowed_chars for c in text)


text = "O'Connor"
result = is_alpha_custom(text, "'-")
print(result)  # True

text2 = "Smith-Jones"
result2 = is_alpha_custom(text2, "'-")
print(result2)  # True


# 🧩 Check if string starts with letter
def starts_with_letter(text):
    """Check if string starts with an alphabetic character."""
    return bool(text and text[0].isalpha())


text = "Hello"
result = starts_with_letter(text)
print(result)  # True

text2 = "123Hello"
result2 = starts_with_letter(text2)
print(result2)  # False


# 🧩 Check if string ends with letter
def ends_with_letter(text):
    """Check if string ends with an alphabetic character."""
    return bool(text and text[-1].isalpha())


text = "Hello"
result = ends_with_letter(text)
print(result)  # True

text2 = "Hello123"
result2 = ends_with_letter(text2)
print(result2)  # False


# 🧩 Check if string contains only uppercase letters
def is_uppercase_alpha(text):
    """Check if string contains only uppercase alphabetic characters."""
    return text.isupper() and text.isalpha()


text = "HELLO"
result = is_uppercase_alpha(text)
print(result)  # True

text2 = "Hello"
result2 = is_uppercase_alpha(text2)
print(result2)  # False


# 🧩 Check if string contains only lowercase letters
def is_lowercase_alpha(text):
    """Check if string contains only lowercase alphabetic characters."""
    return text.islower() and text.isalpha()


text = "hello"
result = is_lowercase_alpha(text)
print(result)  # True

text2 = "Hello"
result2 = is_lowercase_alpha(text2)
print(result2)  # False


# 🧩 Check if string is title case
def is_title_case(text):
    """Check if string is in title case (first letter of each word capitalized)."""
    return text.istitle()


text = "Hello World"
result = is_title_case(text)
print(result)  # True

text2 = "hello world"
result2 = is_title_case(text2)
print(result2)  # False


# 🧩 Check if string contains specific letters
def contains_specific_letters(text, required_letters):
    """Check if string contains all specified letters."""
    text_lower = text.lower()
    return all(letter.lower() in text_lower for letter in required_letters)


text = "Hello World"
result = contains_specific_letters(text, "hlw")
print(result)  # True

text2 = "Python"
result2 = contains_specific_letters(text2, "xyz")
print(result2)  # False


# 🧩 Check if string is alphabetic with minimum length
def is_alpha_min_length(text, min_length=1):
    """Check if string is alphabetic with minimum length requirement."""
    return text.isalpha() and len(text) >= min_length


text = "Hello"
result = is_alpha_min_length(text, 3)
print(result)  # True

text2 = "Hi"
result2 = is_alpha_min_length(text2, 3)
print(result2)  # False


# 🧩 Check if string is alphabetic with maximum length
def is_alpha_max_length(text, max_length):
    """Check if string is alphabetic with maximum length requirement."""
    return text.isalpha() and len(text) <= max_length


text = "Hello"
result = is_alpha_max_length(text, 10)
print(result)  # True

text2 = "Supercalifragilisticexpialidocious"
result2 = is_alpha_max_length(text2, 10)
print(result2)  # False


# 🧩 Check if string is alphabetic with length range
def is_alpha_length_range(text, min_length=1, max_length=None):
    """Check if string is alphabetic within length range."""
    if not text.isalpha():
        return False

    length = len(text)
    if length < min_length:
        return False

    if max_length is not None and length > max_length:
        return False

    return True


text = "Hello"
result = is_alpha_length_range(text, 3, 10)
print(result)  # True

text2 = "Hi"
result2 = is_alpha_length_range(text2, 3, 10)
print(result2)  # False
