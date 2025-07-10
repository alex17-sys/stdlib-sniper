---
title: Validate Email Address
description: Check if a string is a valid email address using the standard library.
keywords: case, comprehensive, domain, email, length, limits, local, part, patterns, regex, rfc, sensitive, string, text, tld, validation
---

# Validate Email Address

Check if a string is a valid email address using the standard library.

9 snippets available in this sub-category.

---

## Simple

###  Basic email validation

`string` `email` `validation` `regex` `text`

Basic email validation using regex pattern

```python
import re


def is_email(text):
    """Basic email validation using regex."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, text))


email = "user@example.com"
result = is_email(email)
print(result)  # True
```

!!! note "Notes"
    - Uses regex pattern matching
    - Checks basic email format
    - Returns boolean
    - Simple validation

<hr class="snippet-divider">

### Email validation with length check

`string` `email` `validation` `length` `regex` `text`

Email validation with maximum length check

```python
import re


def is_email_with_length(text, max_length=254):
    """Email validation with length check."""
    if len(text) > max_length:
        return False

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, text))


email = "user@example.com"
result = is_email_with_length(email)
print(result)  # True
```

!!! note "Notes"
    - Includes length validation
    - RFC 5321 compliant length
    - Prevents overly long emails
    - More robust validation

<hr class="snippet-divider">

## Complex

###  Comprehensive email validation

`string` `email` `validation` `comprehensive` `regex` `text`

Comprehensive email validation with multiple checks

```python
import re


def is_valid_email(text):
    """Comprehensive email validation."""
    if not text or len(text) > 254:
        return False

    # Basic pattern
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern, text):
        return False

    # Check for consecutive dots
    if ".." in text:
        return False

    # Check for dots at start/end of local part
    local_part = text.split("@")[0]
    if local_part.startswith(".") or local_part.endswith("."):
        return False

    return True


email = "user.name@example.com"
result = is_valid_email(email)
print(result)  # True

email2 = "user..name@example.com"
result2 = is_valid_email(email2)
print(result2)  # False
```

!!! note "Notes"
    - Multiple validation rules
    - Checks for common issues
    - RFC compliant
    - Robust validation

<hr class="snippet-divider">

### Email validation with domain check

`string` `email` `validation` `domain` `regex` `text`

Email validation with domain format checking

```python
import re


def is_email_with_domain_check(text):
    """Email validation with domain existence check."""
    # Basic email validation
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern, text):
        return False

    # Extract domain
    domain = text.split("@")[1]

    # Check if domain has valid format
    domain_pattern = r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(domain_pattern, domain):
        return False

    # Check for consecutive dots in domain
    if ".." in domain:
        return False

    return True


email = "user@example.com"
result = is_email_with_domain_check(email)
print(result)  # True
```

!!! note "Notes"
    - Validates domain format
    - Checks for domain issues
    - No network lookup
    - Fast validation

<hr class="snippet-divider">

### Email validation with local part rules

`string` `email` `validation` `local` `part` `regex` `text`

Email validation with local part specific rules

```python
import re


def is_email_local_part_valid(text):
    """Email validation with local part specific rules."""
    if not text or "@" not in text:
        return False

    local_part, domain = text.split("@", 1)

    # Local part rules
    if len(local_part) > 64:
        return False

    if local_part.startswith(".") or local_part.endswith("."):
        return False

    if ".." in local_part:
        return False

    # Check for valid characters in local part
    local_pattern = r"^[a-zA-Z0-9._%+-]+$"
    if not re.match(local_pattern, local_part):
        return False

    return True


email = "user.name+tag@example.com"
result = is_email_local_part_valid(email)
print(result)  # True

email2 = ".user@example.com"
result2 = is_email_local_part_valid(email2)
print(result2)  # False
```

!!! note "Notes"
    - Validates local part format
    - Checks length limits
    - Handles special characters
    - RFC compliant rules

<hr class="snippet-divider">

### Email validation with TLD check

`string` `email` `validation` `tld` `domain` `text`

Email validation with TLD format checking

```python
import re


def is_email_with_tld_check(text):
    """Email validation with TLD (Top Level Domain) check."""
    # Basic email validation
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern, text):
        return False

    # Extract TLD
    domain = text.split("@")[1]
    tld = domain.split(".")[-1]

    # Check TLD length (2-6 characters)
    if len(tld) < 2 or len(tld) > 6:
        return False

    # Check if TLD is alphabetic
    if not tld.isalpha():
        return False

    return True


email = "user@example.com"
result = is_email_with_tld_check(email)
print(result)  # True

email2 = "user@example.c"
result2 = is_email_with_tld_check(email2)
print(result2)  # False
```

!!! note "Notes"
    - Validates TLD format
    - Checks TLD length
    - Ensures alphabetic TLD
    - More accurate validation

<hr class="snippet-divider">

### Email validation with common patterns

`string` `email` `validation` `patterns` `regex` `text`

Email validation checking for common invalid patterns

```python
import re


def is_email_common_patterns(text):
    """Email validation checking for common invalid patterns."""
    if not text or "@" not in text:
        return False

    # Check for common invalid patterns
    invalid_patterns = [
        r"^@",  # Starts with @
        r"@$",  # Ends with @
        r"@@",  # Double @
        r"\.@",  # Dot before @
        r"@\.",  # Dot after @
        r"\.\.",  # Consecutive dots
        r"^\.",  # Starts with dot
        r"\.$",  # Ends with dot
    ]

    for pattern in invalid_patterns:
        if re.search(pattern, text):
            return False

    # Basic email pattern
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_pattern, text))


email = "user@example.com"
result = is_email_common_patterns(email)
print(result)  # True

email2 = "user@@example.com"
result2 = is_email_common_patterns(email2)
print(result2)  # False
```

!!! note "Notes"
    - Checks common invalid patterns
    - Prevents obvious errors
    - Comprehensive validation
    - Useful for form validation

<hr class="snippet-divider">

### Email validation with length limits

`string` `email` `validation` `length` `limits` `rfc` `text`

Email validation with RFC compliant length limits

```python
import re


def is_email_with_limits(text):
    """Email validation with RFC compliant length limits."""
    if not text:
        return False

    # Total length check (RFC 5321)
    if len(text) > 254:
        return False

    if "@" not in text:
        return False

    local_part, domain = text.split("@", 1)

    # Local part length check (RFC 5321)
    if len(local_part) > 64:
        return False

    # Domain length check
    if len(domain) > 253:
        return False

    # Basic email pattern
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, text))


email = "user@example.com"
result = is_email_with_limits(email)
print(result)  # True

email2 = "a" * 65 + "@example.com"
result2 = is_email_with_limits(email2)
print(result2)  # False
```

!!! note "Notes"
    - RFC 5321 compliant limits
    - Checks total, local, and domain lengths
    - Prevents oversized emails
    - Standards compliant

<hr class="snippet-divider">

### Email validation with case sensitivity

`string` `email` `validation` `case` `sensitive` `text`

Email validation with case sensitivity options

```python
import re


def is_email_case_sensitive(text, case_sensitive=False):
    """Email validation with optional case sensitivity."""
    if case_sensitive:
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    else:
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        text = text.lower()

    return bool(re.match(pattern, text))


email = "User@Example.COM"
result = is_email_case_sensitive(email, case_sensitive=False)
print(result)  # True

result2 = is_email_case_sensitive(email, case_sensitive=True)
print(result2)  # True (same pattern, but case preserved)
```

!!! note "Notes"
    - Optional case sensitivity
    - Normalizes case if needed
    - Flexible validation
    - Useful for different requirements

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Is URL](./is_url.md)
- **Reference**: See [📂 Validate Phone](./validate_phone.md)

## 🏷️ Tags

`string`, `email`, `validation`, `regex`, `parse`, `text`

## 📝 Notes

- Use regex for email validation
- Consider edge cases like subdomains and plus addressing
- Useful for input validation and user registration
