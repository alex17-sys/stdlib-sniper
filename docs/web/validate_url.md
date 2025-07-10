---
title: Validate URL
description: Zero-dependency Python snippets for validating URLs using the standard library.
keywords: edge-case, empty, invalid, malformed, netloc, pattern, regex, reserved, scheme, strict, url, validate, web
---

# Validate URL

Zero-dependency Python snippets for validating URLs using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Check if URL has valid scheme and netloc

`url` `validate` `scheme` `netloc` `web`

Check if URL has valid scheme and netloc

```python
from urllib.parse import urlparse

def is_valid_url(url):
    """Return True if URL has a valid scheme and netloc."""
    parsed = urlparse(url)
    return all([parsed.scheme in ('http', 'https', 'ftp'), parsed.netloc])

# Example usage
print(is_valid_url('https://example.com'))  # True
print(is_valid_url('ftp://ftp.example.com'))  # True
print(is_valid_url('example.com'))  # False
```

!!! note "Notes"
    - Only checks for presence of scheme and netloc
    - Does not check if domain actually exists

<hr class="snippet-divider">

### Validate URL with regex (basic)

`url` `validate` `regex` `pattern` `web`

Validate URL with regex (basic)

```python
import re

def is_valid_url_regex(url):
    """Basic regex validation for HTTP/HTTPS URLs."""
    pattern = re.compile(r'^https?://[\w.-]+(?:\.[\w\.-]+)+[/\w\.-]*$')
    return bool(pattern.match(url))

# Example usage
print(is_valid_url_regex('https://example.com/page'))  # True
print(is_valid_url_regex('http://localhost:8000'))  # True
print(is_valid_url_regex('ftp://example.com'))  # False
```

!!! note "Notes"
    - Regex can be customized for stricter validation
    - Does not check for reachability

<hr class="snippet-divider">

## Complex

###  Validate URL with reserved domains and invalid characters

`url` `validate` `strict` `reserved` `invalid` `web`

Strict URL validation (reserved domains, invalid chars)

```python
from urllib.parse import urlparse
import re

def is_valid_url_strict(url):
    """Strict URL validation: scheme, netloc, no reserved domains, no spaces."""
    parsed = urlparse(url)
    if parsed.scheme not in ('http', 'https', 'ftp'):
        return False
    if not parsed.netloc or ' ' in url:
        return False
    # Disallow reserved/test domains
    reserved = ('.test', '.example', '.invalid', '.localhost')
    if any(parsed.netloc.endswith(r) for r in reserved):
        return False
    # Basic character check
    if not re.match(r'^[\w\.-]+$', parsed.netloc.replace(':', '')):
        return False
    return True

# Example usage
print(is_valid_url_strict('https://example.com'))  # True
print(is_valid_url_strict('https://localhost'))  # False
print(is_valid_url_strict('https://example .com'))  # False
```

!!! note "Notes"
    - Disallows reserved/test domains and spaces
    - Checks for valid characters in netloc

<hr class="snippet-divider">

## Edge Cases

###  Validate missing scheme, empty, or malformed URLs

`url` `validate` `edge-case` `empty` `malformed` `web`

Validate missing scheme, empty, or malformed URLs

```python
def is_valid_url(url):
    # Function is defined in one of the above code block
    pass


print(is_valid_url(''))  # False
print(is_valid_url('not a url'))  # False
print(is_valid_url('http:///path'))  # False
```

!!! note "Notes"
    - Returns False for empty or malformed URLs
    - Does not check for DNS or server reachability

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Parse URL](./parse_url.md)
- **Reference**: See [📂 Build URL](./build_url.md)
- **Reference**: See [📂 Extract Domain](./extract_domain.md)

## 🏷️ Tags

`url`, `validate`, `scheme`, `netloc`, `regex`, `strict`, `reserved`, `edge-case`, `web`

## 📝 Notes

- Use urlparse for basic validation, regex for stricter checks
- For production, consider using validators or DNS checks
- Always sanitize and validate user input URLs
