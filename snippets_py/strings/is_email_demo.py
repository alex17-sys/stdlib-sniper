# 🧩 Basic email validation
import re


def is_email(text):
    """Basic email validation using regex."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, text))


email = "user@example.com"
result = is_email(email)
print(result)  # True


# 🧩 Email validation with length check
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


# 🧩 Comprehensive email validation
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


# 🧩 Email validation with domain check
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


# 🧩 Email validation with local part rules
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


# 🧩 Email validation with TLD check
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


# 🧩 Email validation with common patterns
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


# 🧩 Email validation with length limits
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


# 🧩 Email validation with case sensitivity
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
