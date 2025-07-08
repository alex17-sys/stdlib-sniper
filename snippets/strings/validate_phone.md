# Validate Phone Number

Validate phone number formats using regular expressions and string manipulation.

## Simple

### 🧩 Basic Phone Validation

```python
def is_valid_phone(phone):
    """Check if phone number is valid (basic format)."""
    import re

    # Remove all non-digit characters
    digits = re.sub(r"\D", "", phone)
    # Check if it's 10-15 digits (international standard)
    return 10 <= len(digits) <= 15


# Examples
print(is_valid_phone("123-456-7890"))  # True
print(is_valid_phone("(123) 456-7890"))  # True
print(is_valid_phone("123.456.7890"))  # True
print(is_valid_phone("1234567890"))  # True
print(is_valid_phone("123"))  # False (too short)
print(is_valid_phone("abc-def-ghij"))  # False (no digits)
```

📂 Validate if a phone number contains 10-15 digits after removing non-digit characters

🏷️ Tags: validation, phone, regex, basic
📝 Notes:
- Accepts various formats (dashes, spaces, parentheses)
- Only checks digit count, not country code
- Useful for quick validation

### 🧩 US Phone Number Validation

```python
def is_valid_us_phone(phone):
    """Validate US phone number format."""
    import re

    # Pattern for common US formats
    pattern = r"^(\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})$"
    return bool(re.match(pattern, phone))


# Examples
print(is_valid_us_phone("123-456-7890"))  # True
print(is_valid_us_phone("(123) 456-7890"))  # True
print(is_valid_us_phone("123.456.7890"))  # True
print(is_valid_us_phone("+1 123-456-7890"))  # True
print(is_valid_us_phone("1234567890"))  # True
print(is_valid_us_phone("123-45-6789"))  # False (invalid format)
```

📂 Validate US phone number format using regular expressions

🏷️ Tags: validation, phone, regex, US, formatting
📝 Notes:
- Accepts various US formats
- Checks for 10-digit US numbers, with or without country code
- Does not validate area code or exchange code

## Complex

### 🧩 International Phone Validation

```python
def is_valid_international_phone(phone):
    """Validate international phone number with country code."""
    import re

    # Remove all non-digit characters except +
    cleaned = re.sub(r"[^\d+]", "", phone)
    # Check if it starts with + and has country code
    if not cleaned.startswith("+"):
        return False
    # Remove + and check length (country code + number)
    digits = cleaned[1:]
    return 7 <= len(digits) <= 15
```

📂 Validate international phone number with country code

🏷️ Tags: validation, phone, regex, international
📝 Notes:
- Checks for leading + and digit count
- Does not validate specific country codes
- Useful for global applications

### 🧩 Format International Phone Number

```python
def format_international_phone(phone):
    """Format phone number to international standard."""
    import re

    # Remove all non-digit characters
    digits = re.sub(r"\D", "", phone)
    if len(digits) == 10:
        # Assume US number, add +1
        return f"+1-{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits.startswith("1"):
        # US number with country code
        return f"+{digits[:1]}-{digits[1:4]}-{digits[4:7]}-{digits[7:]}"
    elif len(digits) >= 7:
        # International number
        return f"+{digits}"
    else:
        return None
```

📂 Format a phone number to international standard (+country-code)

🏷️ Tags: phone, formatting, international, standard
📝 Notes:
- Assumes US number if 10 digits
- Returns None if not enough digits
- Useful for storing numbers in a consistent format

### 🧩 Parse Phone Number with Extension

```python
def parse_phone_with_extension(phone):
    """Parse phone number with optional extension."""
    import re

    # Pattern for phone with extension
    pattern = r"^(\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})(\s*(?:ext|x|extension)\s*([0-9]+))?$"
    match = re.match(pattern, phone, re.IGNORECASE)
    if match:
        groups = match.groups()
        main_number = f"{groups[1]}-{groups[2]}-{groups[3]}"
        extension = groups[5] if groups[5] else None
        return {
            "number": main_number,
            "extension": extension,
            "full": f"{main_number} ext {extension}" if extension else main_number,
        }
    return None
```

📂 Parse phone number and extract extension if present

🏷️ Tags: phone, extension, parsing, regex
📝 Notes:
- Supports ext, x, or extension keywords
- Returns a dictionary with number and extension
- Returns None if not matched

### 🧩 Validate Phone Number Extension

```python
def parse_phone_with_extension(phone):
    # See above defined function
    pass

def validate_phone_extension(phone):
    """Validate phone number with extension."""
    parsed = parse_phone_with_extension(phone)
    if not parsed:
        return False
    # Validate extension length (typically 1-5 digits)
    if parsed["extension"]:
        return 1 <= len(parsed["extension"]) <= 5
    return True
```

📂 Validate phone number extension (1-5 digits allowed)

🏷️ Tags: phone, extension, validation
📝 Notes:
- Uses parse_phone_with_extension
- Returns True if extension is valid or not present
- Returns False if parsing fails

### 🧩 Normalize Phone Number

```python
def normalize_phone_number(phone):
    """Normalize phone number to standard format."""
    import re

    # Remove all non-digit characters
    digits = re.sub(r"\D", "", phone)
    if len(digits) == 10:
        # US number without country code
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits.startswith("1"):
        # US number with country code
        return f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    elif len(digits) >= 7:
        # International number
        return f"+{digits}"
    else:
        return None
```

📂 Normalize phone number to a standard readable format

🏷️ Tags: phone, normalization, formatting, standard
📝 Notes:
- Handles US and international numbers
- Returns None if not enough digits
- Useful for display and storage

### 🧩 Extract Phone Numbers from Text

```python
def normalize_phone_number(phone):
    # See above defined function
    pass

def extract_phone_numbers(text):
    """Extract phone numbers from text."""
    import re

    # Pattern to find phone numbers in text
    pattern = r"(\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})"
    matches = re.finditer(pattern, text)
    phones = []
    for match in matches:
        full_match = match.group(0)
        normalized = normalize_phone_number(full_match)
        if normalized:
            phones.append(
                {"original": full_match, "normalized": normalized, "position": match.span()}
            )
    return phones
```

📂 Extract and normalize phone numbers from a block of text

🏷️ Tags: phone, extraction, normalization, regex, text
📝 Notes:
- Uses normalize_phone_number
- Finds all phone numbers in text
- Returns list of dictionaries with original and normalized numbers
- Useful for parsing contact info

## 🔗 Cross-References

- **Reference**: See [📂 Is Email](./is_email.md)
- **Reference**: See [📂 Is URL](./is_url.md)
- **Reference**: See [📂 Validate Credit Card](./validate_credit_card.md)
- **Reference**: See [📂 Strip Characters](./strip_chars.md)
- **Reference**: See [📂 Remove Whitespace](./remove_whitespace.md)

## 🏷️ Tags

`validation`, `phone`, `regex`, `formatting`, `international`, `extension`, `normalization`

## 📝 Notes

- Phone number validation varies by country and region
- Consider using libraries like phonenumbers for production applications
- Always validate phone numbers before sending SMS or making calls
- Store phone numbers in normalized format for consistency
- Be aware of different international formats and country codes
