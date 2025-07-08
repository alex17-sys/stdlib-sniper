# 🧩 Check if string is numeric
def is_numeric(text):
    """Check if string contains only numeric characters."""
    return text.isdigit()


text = "12345"
result = is_numeric(text)
print(result)  # True


# 🧩 Check if string is decimal
def is_decimal(text):
    """Check if string represents a decimal number."""
    try:
        float(text)
        return True
    except ValueError:
        return False


text = "123.45"
result = is_decimal(text)
print(result)  # True


# 🧩 Check if string is integer
def is_integer(text):
    """Check if string represents an integer."""
    try:
        int(text)
        return True
    except ValueError:
        return False


text = "123"
result = is_integer(text)
print(result)  # True

text2 = "123.45"
result2 = is_integer(text2)
print(result2)  # False


# 🧩 Check if string is positive number
def is_positive_number(text):
    """Check if string represents a positive number."""
    try:
        num = float(text)
        return num > 0
    except ValueError:
        return False


text = "123.45"
result = is_positive_number(text)
print(result)  # True

text2 = "-123"
result2 = is_positive_number(text2)
print(result2)  # False


# 🧩 Check if string is in range
def is_number_in_range(text, min_val=None, max_val=None):
    """Check if string represents a number within range."""
    try:
        num = float(text)

        if min_val is not None and num < min_val:
            return False
        if max_val is not None and num > max_val:
            return False

        return True
    except ValueError:
        return False


text = "50"
result = is_number_in_range(text, 0, 100)
print(result)  # True

text2 = "150"
result2 = is_number_in_range(text2, 0, 100)
print(result2)  # False


# 🧩 Check if string is hexadecimal
def is_hexadecimal(text):
    """Check if string represents a hexadecimal number."""
    try:
        int(text, 16)
        return True
    except ValueError:
        return False


text = "1A2B3C"
result = is_hexadecimal(text)
print(result)  # True

text2 = "1A2B3G"
result2 = is_hexadecimal(text2)
print(result2)  # False


# 🧩 Check if string is binary
def is_binary(text):
    """Check if string represents a binary number."""
    try:
        int(text, 2)
        return True
    except ValueError:
        return False


text = "101010"
result = is_binary(text)
print(result)  # True

text2 = "101012"
result2 = is_binary(text2)
print(result2)  # False


# 🧩 Check if string is octal
def is_octal(text):
    """Check if string represents an octal number."""
    try:
        int(text, 8)
        return True
    except ValueError:
        return False


text = "123"
result = is_octal(text)
print(result)  # True

text2 = "129"
result2 = is_octal(text2)
print(result2)  # False


# 🧩 Check if string is scientific notation
import re


def is_scientific_notation(text):
    """Check if string represents scientific notation."""
    pattern = r"^[+-]?(\d+\.?\d*|\.\d+)[eE][+-]?\d+$"
    return bool(re.match(pattern, text))


text = "1.23e-4"
result = is_scientific_notation(text)
print(result)  # True

text2 = "1.23"
result2 = is_scientific_notation(text2)
print(result2)  # False


# 🧩 Check if string is currency
import re


def is_currency(text):
    """Check if string represents a currency amount."""
    pattern = r"^[$€£¥]?\s*\d{1,3}(,\d{3})*(\.\d{2})?$"
    return bool(re.match(pattern, text))


text = "$1,234.56"
result = is_currency(text)
print(result)  # True

text2 = "1234.567"
result2 = is_currency(text2)
print(result2)  # False


# 🧩 Check if string is percentage
import re


def is_percentage(text):
    """Check if string represents a percentage."""
    pattern = r"^[+-]?\d+\.?\d*\s*%$"
    return bool(re.match(pattern, text))


text = "25.5%"
result = is_percentage(text)
print(result)  # True

text2 = "25.5"
result2 = is_percentage(text2)
print(result2)  # False
