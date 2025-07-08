# Validate Credit Card Number

Zero-dependency Python snippets using only the standard library.

9 snippets available in this sub-category.

---

## Simple

###  Basic credit card validation

`string` `credit` `card` `luhn` `validation` `text`

Basic credit card validation using Luhn algorithm

```python
def validate_credit_card(card_number):
    """Basic credit card validation using Luhn algorithm."""
    # Remove spaces and dashes
    card_number = card_number.replace(" ", "").replace("-", "")

    # Check if all characters are digits
    if not card_number.isdigit():
        return False

    # Check length (most cards are 13-19 digits)
    if len(card_number) < 13 or len(card_number) > 19:
        return False

    # Luhn algorithm
    total = 0
    is_even = False

    # Process from right to left
    for digit in reversed(card_number):
        d = int(digit)
        if is_even:
            d *= 2
            if d > 9:
                d -= 9
        total += d
        is_even = not is_even

    return total % 10 == 0


card = "4532015112830366"
result = validate_credit_card(card)
print(result)  # True
```

!!! note "Notes"
    - Uses Luhn algorithm
    - Removes spaces and dashes
    - Checks digit length
    - Returns boolean

<hr class="snippet-divider">

### Credit card validation with format check

`string` `credit` `card` `format` `validation` `text`

Credit card validation with format checking

```python
def validate_credit_card_format(card_number):
    """Credit card validation with format checking."""
    # Remove spaces and dashes
    card_number = card_number.replace(" ", "").replace("-", "")

    # Check if all characters are digits
    if not card_number.isdigit():
        return False

    # Check length
    if len(card_number) < 13 or len(card_number) > 19:
        return False

    # Luhn algorithm
    total = 0
    is_even = False

    for digit in reversed(card_number):
        d = int(digit)
        if is_even:
            d *= 2
            if d > 9:
                d -= 9
        total += d
        is_even = not is_even

    return total % 10 == 0


card = "4532 0151 1283 0366"
result = validate_credit_card_format(card)
print(result)  # True
```

!!! note "Notes"
    - Handles formatted input
    - Removes common separators
    - Validates format
    - More user-friendly

<hr class="snippet-divider">

## Complex

###  Credit card validation with card type detection

`string` `credit` `card` `type` `detection` `validation` `text`

Credit card validation with card type detection

```python
import re


def validate_credit_card_with_type(card_number):
    """Credit card validation with card type detection."""
    # Remove spaces and dashes
    card_number = card_number.replace(" ", "").replace("-", "")

    # Check if all characters are digits
    if not card_number.isdigit():
        return False, "Invalid characters"

    # Check length
    if len(card_number) < 13 or len(card_number) > 19:
        return False, "Invalid length"

    # Card type detection
    card_type = "Unknown"
    if re.match(r"^4[0-9]{12}(?:[0-9]{3})?$", card_number):
        card_type = "Visa"
    elif re.match(r"^5[1-5][0-9]{14}$", card_number):
        card_type = "MasterCard"
    elif re.match(r"^3[47][0-9]{13}$", card_number):
        card_type = "American Express"
    elif re.match(r"^6(?:011|5[0-9]{2})[0-9]{12}$", card_number):
        card_type = "Discover"

    # Luhn algorithm
    total = 0
    is_even = False

    for digit in reversed(card_number):
        d = int(digit)
        if is_even:
            d *= 2
            if d > 9:
                d -= 9
        total += d
        is_even = not is_even

    is_valid = total % 10 == 0
    return is_valid, card_type


card = "4532015112830366"
result, card_type = validate_credit_card_with_type(card)
print(f"Valid: {result}, Type: {card_type}")  # Valid: True, Type: Visa
```

!!! note "Notes"
    - Detects major card types
    - Uses regex patterns
    - Returns validation and type
    - Comprehensive validation

<hr class="snippet-divider">

### Credit card validation with detailed error reporting

`string` `credit` `card` `error` `reporting` `validation` `text`

Credit card validation with detailed error reporting

```python
def validate_credit_card_detailed(card_number):
    """Credit card validation with detailed error reporting."""
    errors = []

    # Remove spaces and dashes
    card_number = card_number.replace(" ", "").replace("-", "")

    # Check if all characters are digits
    if not card_number.isdigit():
        errors.append("Contains non-digit characters")

    # Check length
    if len(card_number) < 13:
        errors.append("Too short (minimum 13 digits)")
    elif len(card_number) > 19:
        errors.append("Too long (maximum 19 digits)")

    # Luhn algorithm
    if card_number.isdigit() and 13 <= len(card_number) <= 19:
        total = 0
        is_even = False

        for digit in reversed(card_number):
            d = int(digit)
            if is_even:
                d *= 2
                if d > 9:
                    d -= 9
            total += d
            is_even = not is_even

        if total % 10 != 0:
            errors.append("Failed Luhn algorithm check")

    is_valid = len(errors) == 0
    return is_valid, errors


card = "4532 0151 1283 0366"
result, errors = validate_credit_card_detailed(card)
print(f"Valid: {result}")
if errors:
    print(f"Errors: {errors}")
```

!!! note "Notes"
    - Returns specific error messages
    - Multiple validation checks
    - User-friendly feedback
    - Debugging support

<hr class="snippet-divider">

### Credit card validation with security features

`string` `credit` `card` `security` `mask` `validation` `text`

Credit card validation with security features

```python
def validate_credit_card_secure(card_number, mask_output=True):
    """Credit card validation with security features."""
    # Remove spaces and dashes
    card_number = card_number.replace(" ", "").replace("-", "")

    # Check if all characters are digits
    if not card_number.isdigit():
        return False, "Invalid characters"

    # Check length
    if len(card_number) < 13 or len(card_number) > 19:
        return False, "Invalid length"

    # Luhn algorithm
    total = 0
    is_even = False

    for digit in reversed(card_number):
        d = int(digit)
        if is_even:
            d *= 2
            if d > 9:
                d -= 9
        total += d
        is_even = not is_even

    is_valid = total % 10 == 0

    # Mask output for security
    if mask_output and is_valid:
        return True, f"Valid card ending in {card_number[-4:]}"

    return is_valid, "Invalid card number"


card = "4532015112830366"
result, message = validate_credit_card_secure(card)
print(f"Result: {result}, Message: {message}")
```

!!! note "Notes"
    - Masks sensitive output
    - Security-conscious design
    - Prevents data exposure
    - Safe for logging

<hr class="snippet-divider">

### Credit card validation with country detection

`string` `credit` `card` `country` `region` `validation` `text`

Credit card validation with country/region detection

```python
import re


def validate_credit_card_country(card_number):
    """Credit card validation with country/region detection."""
    # Remove spaces and dashes
    card_number = card_number.replace(" ", "").replace("-", "")

    # Check if all characters are digits
    if not card_number.isdigit():
        return False, "Invalid characters", "Unknown"

    # Check length
    if len(card_number) < 13 or len(card_number) > 19:
        return False, "Invalid length", "Unknown"

    # Country/region detection based on IIN (Issuer Identification Number)
    iin = card_number[:6]
    country = "Unknown"

    # Major card networks and their IIN ranges
    if re.match(r"^4[0-9]{5}$", iin):
        country = "International (Visa)"
    elif re.match(r"^5[1-5][0-9]{4}$", iin):
        country = "International (MasterCard)"
    elif re.match(r"^3[47][0-9]{4}$", iin):
        country = "International (American Express)"
    elif re.match(r"^6(?:011|5[0-9]{2})[0-9]{2}$", iin):
        country = "International (Discover)"

    # Luhn algorithm
    total = 0
    is_even = False

    for digit in reversed(card_number):
        d = int(digit)
        if is_even:
            d *= 2
            if d > 9:
                d -= 9
        total += d
        is_even = not is_even

    is_valid = total % 10 == 0
    return is_valid, "Valid" if is_valid else "Invalid", country


card = "4532015112830366"
result, status, country = validate_credit_card_country(card)
print(f"Valid: {result}, Status: {status}, Country: {country}")
```

!!! note "Notes"
    - Detects card network/region
    - Uses IIN ranges
    - International support
    - Network identification

<hr class="snippet-divider">

### Credit card validation with expiration check

`string` `credit` `card` `expiration` `date` `validation` `text`

Credit card validation with expiration date check

```python
from datetime import datetime


def validate_credit_card_with_expiry(card_number, expiry_month, expiry_year):
    """Credit card validation with expiration date check."""
    # Basic card validation
    card_number = card_number.replace(" ", "").replace("-", "")

    if not card_number.isdigit():
        return False, "Invalid card number"

    if len(card_number) < 13 or len(card_number) > 19:
        return False, "Invalid card length"

    # Luhn algorithm
    total = 0
    is_even = False

    for digit in reversed(card_number):
        d = int(digit)
        if is_even:
            d *= 2
            if d > 9:
                d -= 9
        total += d
        is_even = not is_even

    if total % 10 != 0:
        return False, "Invalid card number"

    # Expiration date validation
    try:
        month = int(expiry_month)
        year = int(expiry_year)

        if month < 1 or month > 12:
            return False, "Invalid expiration month"

        # Convert to 4-digit year if needed
        if year < 100:
            year += 2000

        # Check if expired
        current_date = datetime.now()
        expiry_date = datetime(year, month, 1)

        if expiry_date < current_date:
            return False, "Card has expired"

        return True, "Valid card"

    except ValueError:
        return False, "Invalid expiration date format"


card = "4532015112830366"
result, message = validate_credit_card_with_expiry(card, "12", "25")
print(f"Result: {result}, Message: {message}")
```

!!! note "Notes"
    - Checks expiration date
    - Handles date formatting
    - Prevents expired cards
    - Comprehensive validation

<hr class="snippet-divider">

### Credit card validation with CVV check

`string` `credit` `card` `cvv` `security` `validation` `text`

Credit card validation with CVV check

```python
def validate_credit_card_with_cvv(card_number, cvv):
    """Credit card validation with CVV check."""
    # Basic card validation
    card_number = card_number.replace(" ", "").replace("-", "")

    if not card_number.isdigit():
        return False, "Invalid card number"

    if len(card_number) < 13 or len(card_number) > 19:
        return False, "Invalid card length"

    # Luhn algorithm
    total = 0
    is_even = False

    for digit in reversed(card_number):
        d = int(digit)
        if is_even:
            d *= 2
            if d > 9:
                d -= 9
        total += d
        is_even = not is_even

    if total % 10 != 0:
        return False, "Invalid card number"

    # CVV validation
    if not cvv.isdigit():
        return False, "Invalid CVV format"

    cvv_length = len(cvv)
    if cvv_length < 3 or cvv_length > 4:
        return False, "Invalid CVV length"

    # CVV length should match card type
    if len(card_number) == 15 and cvv_length != 4:  # American Express
        return False, "CVV should be 4 digits for American Express"
    elif len(card_number) != 15 and cvv_length != 3:  # Other cards
        return False, "CVV should be 3 digits"

    return True, "Valid card and CVV"


card = "4532015112830366"
cvv = "123"
result, message = validate_credit_card_with_cvv(card, cvv)
print(f"Result: {result}, Message: {message}")
```

!!! note "Notes"
    - Validates CVV format
    - Checks CVV length
    - Card type specific validation
    - Security enhancement

<hr class="snippet-divider">

### Credit card validation with batch processing

`string` `credit` `card` `batch` `processing` `validation` `text`

Credit card validation with batch processing

```python
def validate_credit_cards_batch(card_list):
    """Validate multiple credit card numbers in batch."""
    results = []

    for i, card in enumerate(card_list):
        # Basic validation
        card_clean = card.replace(" ", "").replace("-", "")

        if not card_clean.isdigit():
            results.append((i, card, False, "Invalid characters"))
            continue

        if len(card_clean) < 13 or len(card_clean) > 19:
            results.append((i, card, False, "Invalid length"))
            continue

        # Luhn algorithm
        total = 0
        is_even = False

        for digit in reversed(card_clean):
            d = int(digit)
            if is_even:
                d *= 2
                if d > 9:
                    d -= 9
            total += d
            is_even = not is_even

        is_valid = total % 10 == 0
        message = "Valid" if is_valid else "Failed Luhn check"
        results.append((i, card, is_valid, message))

    return results


cards = [
    "4532015112830366",
    "4532015112830367",  # Invalid
    "4532 0151 1283 0366",
]

results = validate_credit_cards_batch(cards)
for index, card, valid, message in results:
    print(f"Card {index}: {valid} - {message}")
```

!!! note "Notes"
    - Processes multiple cards
    - Returns detailed results
    - Efficient batch validation
    - Useful for data processing

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Validate Phone](./validate_phone.md)
- **Reference**: See [📂 Is Email](./is_email.md)
- **Reference**: See [📂 Is Numeric](./is_numeric.md)

## 🏷️ Tags

`validation`, `credit card`, `luhn`, `regex`, `country`, `region`, `text`

## 📝 Notes

- Luhn algorithm is standard for credit card validation
- Regex can check format and length
- Country/region detection uses IIN ranges
- Always use secure libraries for production
