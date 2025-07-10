---
title: Validate Password Strength
description: Check password strength and enforce password policies using the standard library.
keywords: age, basic, class, entropy, math, password, policy, randomness, regex, reuse, scoring, security, strength, validation
---

# Validate Password Strength

Check password strength and enforce password policies using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Basic Password Validation

`validation` `password` `regex` `basic` `security`

Validate that a password meets minimum length and character requirements (uppercase, lowercase, digit, special character)

```python
def is_valid_password(password):
    """Check if password meets basic requirements."""
    import re

    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True
```

!!! note "Notes"
    - Returns True if all requirements are met
    - Minimum 8 characters, at least one uppercase, one lowercase, one digit, one special character
    - Uses regular expressions for checks

<hr class="snippet-divider">

### Password Strength Checker

`validation` `password` `strength` `scoring` `regex`

Score password strength and provide feedback on missing requirements

```python
def check_password_strength(password):
    """Check password strength and return score and feedback."""
    import re

    score = 0
    feedback = []
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter")
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character")
    if score <= 2:
        strength = "Weak"
    elif score <= 3:
        strength = "Fair"
    elif score <= 4:
        strength = "Good"
    else:
        strength = "Strong"
    return {"score": score, "strength": strength, "feedback": feedback}


# Examples
passwords = ["abc123", "Password", "Password123", "Password123!"]
for pwd in passwords:
    result = check_password_strength(pwd)
    print(f"{pwd}: {result['strength']} (Score: {result['score']})")
    if result["feedback"]:
        print(f"  Issues: {', '.join(result['feedback'])}")
```

!!! note "Notes"
    - Returns a dictionary with score, strength, and feedback
    - Score is based on length and character variety
    - Feedback lists missing requirements

<hr class="snippet-divider">

## Complex

###  Advanced Password Validation

`password` `entropy` `randomness` `security` `math`

Calculate the entropy (randomness) of a password in bits

```python
def validate_password_advanced(password):
    """Advanced password validation with detailed checks and warnings."""
    import re

    errors = []
    warnings = []
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")
    elif len(password) < 12:
        warnings.append("Consider using a password longer than 12 characters")
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    if not has_upper:
        errors.append("Password must contain at least one uppercase letter")
    if not has_lower:
        errors.append("Password must contain at least one lowercase letter")
    if not has_digit:
        errors.append("Password must contain at least one digit")
    if not has_special:
        errors.append("Password must contain at least one special character")
    if re.search(r"(.)\1{2,}", password):
        warnings.append("Avoid repeating characters (e.g., 'aaa')")
    if re.search(r"(123|abc|qwe|password|admin)", password.lower()):
        errors.append("Password contains common patterns")
    keyboard_patterns = ["qwerty", "asdfgh", "zxcvbn", "123456"]
    for pattern in keyboard_patterns:
        if pattern in password.lower():
            errors.append("Password contains keyboard patterns")
            break
    char_types = sum([has_upper, has_lower, has_digit, has_special])
    if char_types < 3:
        warnings.append("Consider using more variety of character types")
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "score": calculate_password_score(password),
    }


def calculate_password_score(password):
    """Calculate password strength score (0-100)."""
    import re

    score = 0
    score += min(len(password) * 4, 40)
    char_types = 0
    if re.search(r"[A-Z]", password):
        char_types += 1
    if re.search(r"[a-z]", password):
        char_types += 1
    if re.search(r"\d", password):
        char_types += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        char_types += 1
    score += char_types * 10
    if re.search(r"(.)\1{2,}", password):
        score -= 10
    if re.search(r"(123|abc|qwe|password|admin)", password.lower()):
        score -= 20
    return max(0, min(100, score))
```

# Examples
test_passwords = [
    "weak",
    "Password123",
    "MySecureP@ssw0rd!",
    "qwerty123",
    "aaaBBB123!",
    "SuperLongAndSecurePassword123!"
]
📂 Advanced password validation with detailed error and warning messages, and a strength score


🏷️ Tags: validation, password, advanced, security, scoring, regex, warnings
📝 Notes:
- Returns a dictionary with validity, errors, warnings, and score
- Checks for common patterns and keyboard sequences
- Encourages longer and more complex passwords

### 🧩 Password Entropy Calculator

```python
def calculate_password_entropy(password):
    """Calculate password entropy (bits of randomness)."""
    import math

    lowercase = set("abcdefghijklmnopqrstuvwxyz")
    uppercase = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digits = set("0123456789")
    special = set('!@#$%^&*(),.?":{}|<>')
    pool_size = 0
    if any(c in lowercase for c in password):
        pool_size += 26
    if any(c in uppercase for c in password):
        pool_size += 26
    if any(c in digits for c in password):
        pool_size += 10
    if any(c in special for c in password):
        pool_size += 20
    entropy = len(password) * math.log2(pool_size)
    return entropy
```

!!! note "Notes"
    - Higher entropy means a stronger password
    - Entropy is based on length and character variety
    - Useful for estimating password strength

<hr class="snippet-divider">

### Password Policy Enforcer

`password` `policy` `validation` `security` `class` `reuse` `age`

Enforce password policy rules and validate passwords against history and age

```python
class PasswordPolicy:
    def __init__(
        self,
        min_length=8,
        require_upper=True,
        require_lower=True,
        require_digit=True,
        require_special=True,
        max_age_days=90,
        prevent_reuse=5,
    ):
        self.min_length = min_length
        self.require_upper = require_upper
        self.require_lower = require_lower
        self.require_digit = require_digit
        self.require_special = require_special
        self.max_age_days = max_age_days
        self.prevent_reuse = prevent_reuse

    def validate_password(self, password, user_history=None):
        import re

        errors = []
        warnings = []
        if len(password) < self.min_length:
            errors.append(f"Password must be at least {self.min_length} characters")
        if self.require_upper and not re.search(r"[A-Z]", password):
            errors.append("Password must contain uppercase letter")
        if self.require_lower and not re.search(r"[a-z]", password):
            errors.append("Password must contain lowercase letter")
        if self.require_digit and not re.search(r"\d", password):
            errors.append("Password must contain digit")
        if self.require_special and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            errors.append("Password must contain special character")
        if user_history and password in user_history:
            errors.append("Password has been used recently")
        if re.search(r"(.)\1{2,}", password):
            warnings.append("Avoid repeating characters")
        return {"valid": len(errors) == 0, "errors": errors, "warnings": warnings}

    def check_password_age(self, last_changed):
        from datetime import datetime

        if not last_changed:
            return True
        days_old = (datetime.now() - last_changed).days
        return days_old > self.max_age_days
```

!!! note "Notes"
    - Use to enforce organizational password policies
    - Supports history and age checks
    - Returns errors and warnings for policy violations

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Is Email](./is_email.md)
- **Reference**: See [📂 Is URL](./is_url.md)
- **Reference**: See [📂 Validate Phone](./validate_phone.md)
- **Reference**: See [📂 Validate Credit Card](./validate_credit_card.md)
- **Reference**: See [📂 Strip Characters](./strip_chars.md)
- **Reference**: See [📂 Remove Whitespace](./remove_whitespace.md)

## 🏷️ Tags

`validation`, `password`, `security`, `strength`, `entropy`, `policy`, `regex`, `complexity`

## 📝 Notes

- Password strength is relative to the attack method
- Consider using password managers for generating strong passwords
- Implement rate limiting for password attempts
- Store password hashes, never plain text
- Use bcrypt or similar for password hashing in production
- Regular password changes may not improve security
- Consider implementing password breach checking
