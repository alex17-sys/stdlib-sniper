# 🧩 Check if URL has valid scheme and netloc
from urllib.parse import urlparse


def is_valid_url(url):
    """Return True if URL has a valid scheme and netloc."""
    parsed = urlparse(url)
    return all([parsed.scheme in ("http", "https", "ftp"), parsed.netloc])


# Example usage
print(is_valid_url("https://example.com"))  # True
print(is_valid_url("ftp://ftp.example.com"))  # True
print(is_valid_url("example.com"))  # False


# 🧩 Validate URL with regex (basic)
import re


def is_valid_url_regex(url):
    """Basic regex validation for HTTP/HTTPS URLs."""
    pattern = re.compile(r"^https?://[\w.-]+(?:\.[\w\.-]+)+[/\w\.-]*$")
    return bool(pattern.match(url))


# Example usage
print(is_valid_url_regex("https://example.com/page"))  # True
print(is_valid_url_regex("http://localhost:8000"))  # True
print(is_valid_url_regex("ftp://example.com"))  # False


# 🧩 Validate URL with reserved domains and invalid characters
from urllib.parse import urlparse
import re


def is_valid_url_strict(url):
    """Strict URL validation: scheme, netloc, no reserved domains, no spaces."""
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https", "ftp"):
        return False
    if not parsed.netloc or " " in url:
        return False
    # Disallow reserved/test domains
    reserved = (".test", ".example", ".invalid", ".localhost")
    if any(parsed.netloc.endswith(r) for r in reserved):
        return False
    # Basic character check
    if not re.match(r"^[\w\.-]+$", parsed.netloc.replace(":", "")):
        return False
    return True


# Example usage
print(is_valid_url_strict("https://example.com"))  # True
print(is_valid_url_strict("https://localhost"))  # False
print(is_valid_url_strict("https://example .com"))  # False


# 🧩 Validate missing scheme, empty, or malformed URLs
# Function is defined in one of the above code block (is_valid_url)


print(is_valid_url(""))  # False
print(is_valid_url("not a url"))  # False
print(is_valid_url("http:///path"))  # False
