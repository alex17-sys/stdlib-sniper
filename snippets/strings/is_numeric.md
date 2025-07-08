# Check if String is Numeric

Check if a string contains numeric values using the standard library.

## Simple

### 🧩 Check if string is numeric

```python
def is_numeric(text):
    """Check if string contains only numeric characters."""
    return text.isdigit()


text = "12345"
result = is_numeric(text)
print(result)  # True
```

📂 Check if string contains only numeric characters

🏷️ Tags: string, numeric, isdigit, validation, text
📝 Notes:
- Uses str.isdigit() method
- Checks for digits only
- Returns boolean
- Simple validation

### 🧩 Check if string is decimal

```python
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
```

📂 Check if string represents a decimal number

🏷️ Tags: string, decimal, float, validation, text
📝 Notes:
- Uses float() conversion
- Handles decimal points
- Includes error handling
- More flexible than isdigit

## Complex

### 🧩 Check if string is integer

```python
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
```

📂 Check if string represents an integer

🏷️ Tags: string, integer, int, validation, text
📝 Notes:
- Uses int() conversion
- Rejects decimal numbers
- Includes error handling
- Strict integer validation

### 🧩 Check if string is positive number

```python
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
```

📂 Check if string represents a positive number

🏷️ Tags: string, positive, numbers, validation, text
📝 Notes:
- Combines float conversion and comparison
- Checks for positive values
- Handles both integers and decimals
- Useful for input validation

### 🧩 Check if string is in range

```python
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
```

📂 Check if string represents a number within specified range

🏷️ Tags: string, ranges validation, min, max, text
📝 Notes:
- Flexible range checking
- Optional min/max bounds
- Handles edge cases
- Useful for form validation

### 🧩 Check if string is hexadecimal

```python
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
```

📂 Check if string represents a hexadecimal number

🏷️ Tags: string, hexadecimal, hex, validation, text
📝 Notes:
- Uses int() with base 16
- Handles hex digits (0-9, A-F)
- Case-insensitive
- Useful for color codes

### 🧩 Check if string is binary

```python
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
```

📂 Check if string represents a binary number

🏷️ Tags: string, binary, bin, validation, text
📝 Notes:
- Uses int() with base 2
- Handles binary digits (0-1)
- Strict binary validation
- Useful for bit operations

### 🧩 Check if string is octal

```python
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
```

📂 Check if string represents an octal number

🏷️ Tags: string, octal, oct, validation, text
📝 Notes:
- Uses int() with base 8
- Handles octal digits (0-7)
- Strict octal validation
- Useful for permissions

### 🧩 Check if string is scientific notation

```python
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
```

📂 Check if string represents scientific notation

🏷️ Tags: string, scientific, notation, regex, validation, text
📝 Notes:
- Uses regex pattern matching
- Handles e/E notation
- Supports optional signs
- Useful for scientific data

### 🧩 Check if string is currency

```python
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
```

📂 Check if string represents a currency amount

🏷️ Tags: string, currency, money, regex, validation, text
📝 Notes:
- Uses regex pattern matching
- Supports common currencies
- Handles thousands separators
- Useful for financial data

### 🧩 Check if string is percentage

```python
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
```

📂 Check if string represents a percentage

🏷️ Tags: string, percentage, percent, regex, validation, text
📝 Notes:
- Uses regex pattern matching
- Requires % symbol
- Supports decimal values
- Useful for statistics

## 🔗 Cross-References

- **Reference**: See [📂 Is Alpha](./is_alpha.md)
- **Reference**: See [📂 Is Alphanumeric](./is_alphanumeric.md)
- **Reference**: See [📂 Validate Credit Card](./validate_credit_card.md)

## 🏷️ Tags

`string`, `numeric`, `isnumeric`, `isdigit`, `number`, `validation`, `text`

## 📝 Notes

- Use str.isnumeric(), str.isdigit(), or str.isdecimal() for numeric checks
- Handles Unicode digits and special cases
- Useful for input validation and parsing
