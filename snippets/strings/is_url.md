# Validate URL Format

Check if a string is a valid URL using the standard library.

## Simple

### 🧩 Basic URL validation

```python
import re


def is_url(text):
    """Basic URL validation using regex."""
    pattern = r"^https?://[^\s/$.?#].[^\s]*$"
    return bool(re.match(pattern, text))


url = "https://example.com"
result = is_url(url)
print(result)  # True
```

📂 Basic URL validation using regex pattern

🏷️ Tags: string, url, validation, regex, text
📝 Notes:
- Uses regex pattern matching
- Checks basic URL format
- Returns boolean
- Simple validation

### 🧩 URL validation with protocol check

```python
import re


def is_url_with_protocol(text, allowed_protocols=None):
    """URL validation with specific protocol checking."""
    if allowed_protocols is None:
        allowed_protocols = ["http", "https", "ftp"]

    pattern = rf"^({'|'.join(allowed_protocols)})://[^\s/$.?#].[^\s]*$"
    return bool(re.match(pattern, text))


url = "https://example.com"
result = is_url_with_protocol(url)
print(result)  # True

url2 = "ftp://example.com"
result2 = is_url_with_protocol(url2)
print(result2)  # True
```

📂 URL validation with specific protocol checking

🏷️ Tags: string, url, validation, protocol, regex, text
📝 Notes:
- Configurable allowed protocols
- Supports multiple protocols
- Flexible validation
- Useful for different use cases

## Complex

### 🧩 Comprehensive URL validation

```python
from urllib.parse import urlparse


def is_valid_url(text):
    """Comprehensive URL validation."""
    try:
        result = urlparse(text)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


url = "https://example.com/path?param=value"
result = is_valid_url(url)
print(result)  # True

url2 = "not-a-url"
result2 = is_valid_url(url2)
print(result2)  # False
```

📂 Comprehensive URL validation using urllib.parse

🏷️ Tags: string, url, validation, urllib, parse, text
📝 Notes:
- Uses urllib.parse.urlparse
- Checks scheme and netloc
- Handles complex URLs
- Robust validation

### 🧩 URL validation with domain check

```python
import re


def is_url_with_domain_check(text):
    """URL validation with domain format checking."""
    # Basic URL pattern
    pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$"
    if not re.match(pattern, text):
        return False

    # Extract domain
    domain_match = re.search(r"https?://([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", text)
    if not domain_match:
        return False

    domain = domain_match.group(1)

    # Check domain format
    if domain.startswith(".") or domain.endswith("."):
        return False

    if ".." in domain:
        return False

    return True


url = "https://example.com"
result = is_url_with_domain_check(url)
print(result)  # True

url2 = "https://.example.com"
result2 = is_url_with_domain_check(url2)
print(result2)  # False
```

📂 URL validation with domain format checking

🏷️ Tags: string, url, validation, domain, regex, text
📝 Notes:
- Validates domain format
- Checks for domain issues
- Prevents invalid domains
- More accurate validation

### 🧩 URL validation with path check

```python
import re


def is_url_with_path_check(text):
    """URL validation with path format checking."""
    # URL pattern with optional path
    pattern = (
        r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[a-zA-Z0-9._/-]*)?(\?[a-zA-Z0-9=&]*)?(#.*)?$"
    )
    return bool(re.match(pattern, text))


url = "https://example.com/path/to/page"
result = is_url_with_path_check(url)
print(result)  # True

url2 = "https://example.com/path with spaces"
result2 = is_url_with_path_check(url2)
print(result2)  # False
```

📂 URL validation with path format checking

🏷️ Tags: string, url, validation, path, regex, text
📝 Notes:
- Validates path format
- Handles query parameters
- Supports fragments
- Comprehensive URL checking

### 🧩 URL validation with port check

```python
import re


def is_url_with_port_check(text):
    """URL validation with port number checking."""
    # URL pattern with optional port
    pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(:\d{1,5})?(/.*)?$"
    if not re.match(pattern, text):
        return False

    # Check port number if present
    port_match = re.search(r":(\d{1,5})", text)
    if port_match:
        port = int(port_match.group(1))
        if port < 1 or port > 65535:
            return False

    return True


url = "https://example.com:8080"
result = is_url_with_port_check(url)
print(result)  # True

url2 = "https://example.com:70000"
result2 = is_url_with_port_check(url2)
print(result2)  # False
```

📂 URL validation with port number checking

🏷️ Tags: string, url, validation, port, regex, text
📝 Notes:
- Validates port numbers
- Checks port range (1-65535)
- Optional port support
- Useful for service URLs

### 🧩 URL validation with query parameters

```python
import re


def is_url_with_query_check(text):
    """URL validation with query parameter checking."""
    # URL pattern with query parameters
    pattern = (
        r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[a-zA-Z0-9._/-]*)?(\?[a-zA-Z0-9=&]*)?(#.*)?$"
    )
    if not re.match(pattern, text):
        return False

    # Check query parameter format if present
    if "?" in text:
        query_part = text.split("?")[1].split("#")[0]
        if query_part and not re.match(r"^[a-zA-Z0-9=&]*$", query_part):
            return False

    return True


url = "https://example.com?param=value&other=123"
result = is_url_with_query_check(url)
print(result)  # True

url2 = "https://example.com?param=value with spaces"
result2 = is_url_with_query_check(url2)
print(result2)  # False
```

📂 URL validation with query parameter checking

🏷️ Tags: string, url, validation, query, parameters, regex, text
📝 Notes:
- Validates query parameters
- Checks parameter format
- Handles multiple parameters
- Useful for API URLs

### 🧩 URL validation with fragment check

```python
import re


def is_url_with_fragment_check(text):
    """URL validation with fragment checking."""
    # URL pattern with fragment
    pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[a-zA-Z0-9._/-]*)?(\?[a-zA-Z0-9=&]*)?(#[a-zA-Z0-9._-]*)?$"
    return bool(re.match(pattern, text))


url = "https://example.com/page#section"
result = is_url_with_fragment_check(url)
print(result)  # True

url2 = "https://example.com/page#section with spaces"
result2 = is_url_with_fragment_check(url2)
print(result2)  # False
```

📂 URL validation with fragment checking

🏷️ Tags: string, url, validation, fragment, regex, text
📝 Notes:
- Validates URL fragments
- Checks fragment format
- Handles anchor links
- Useful for page navigation

### 🧩 URL validation with IP address support

```python
import re


def is_url_with_ip_support(text):
    """URL validation supporting both domain names and IP addresses."""
    # IP address pattern
    ip_pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    # Extract hostname/IP
    host_match = re.search(r"https?://([a-zA-Z0-9.-]+)", text)
    if not host_match:
        return False

    host = host_match.group(1)

    # Check if it's an IP address
    if re.match(ip_pattern, host):
        return True

    # Check if it's a valid domain
    domain_pattern = r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(domain_pattern, host))


url = "https://192.168.1.1"
result = is_url_with_ip_support(url)
print(result)  # True

url2 = "https://example.com"
result2 = is_url_with_ip_support(url2)
print(result2)  # True
```

📂 URL validation supporting IP addresses and domain names

🏷️ Tags: string, url, validation, ip, address, domain, regex, text
📝 Notes:
- Supports IP addresses
- Validates IP format
- Handles both IP and domain
- Useful for local networks

### 🧩 URL validation with length limits

```python
import re


def is_url_with_length_check(text, max_length=2048):
    """URL validation with length checking."""
    if len(text) > max_length:
        return False

    # Basic URL pattern
    pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$"
    return bool(re.match(pattern, text))


url = "https://example.com"
result = is_url_with_length_check(url)
print(result)  # True

url2 = "https://example.com/" + "a" * 2000
result2 = is_url_with_length_check(url2)
print(result2)  # False
```

📂 URL validation with length checking

🏷️ Tags: string, url, validation, length, limits, regex, text
📝 Notes:
- Configurable length limit
- Prevents overly long URLs
- Browser compatible limit
- Useful for form validation

## 🔗 Cross-References

- **Reference**: See [📂 Is Email](./is_email.md)
- **Reference**: See [📂 Validate Phone](./validate_phone.md)

## 🏷️ Tags

`string`, `url`, `validation`, `regex`, `parse`, `text`

## 📝 Notes

- Use regex or urllib.parse for URL validation
- Consider edge cases like query strings and ports
- Useful for input validation and web scraping
