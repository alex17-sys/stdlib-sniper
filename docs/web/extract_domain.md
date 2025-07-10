---
title: Extract Domain from URL
description: Zero-dependency Python snippets for extracting the domain from URLs using the standard library.
keywords: domain, edge-case, extract, host, ipv6, malformed, netloc, port, registered, tld, url, web
---

# Extract Domain from URL

Zero-dependency Python snippets for extracting the domain from URLs using the standard library.

6 snippets available in this sub-category.

---

## Simple

###  Extract netloc (host:port) from URL

`url` `extract` `domain` `netloc` `host` `web`

Extract netloc (host:port) from URL

```python
from urllib.parse import urlparse

url = 'https://sub.example.com:8080/path?query=1'
parsed = urlparse(url)
print(parsed.netloc)  # sub.example.com:8080
```

!!! note "Notes"
    - netloc includes subdomains and port if present

<hr class="snippet-divider">

### Extract host (domain) only (without port)

`url` `extract` `domain` `host` `web`

Extract host (domain) only

```python
from urllib.parse import urlparse

url = 'https://sub.example.com:8080/path'
parsed = urlparse(url)
host = parsed.hostname
print(host)  # sub.example.com
```

!!! note "Notes"
    - hostname omits port and brackets for IPv6

<hr class="snippet-divider">

### Extract port from URL

`url` `extract` `port` `web`

Extract port from URL

```python
from urllib.parse import urlparse

url = 'https://example.com:8443/path'
parsed = urlparse(url)
port = parsed.port
print(port)  # 8443
```

!!! note "Notes"
    - Returns None if no port is specified

<hr class="snippet-divider">

## Complex

###  Extract registered domain (TLD split, basic)

`url` `extract` `domain` `tld` `registered` `web`

Extract registered domain (basic TLD split)

```python
from urllib.parse import urlparse

def get_registered_domain(url):
    """Extract the registered domain (e.g., example.com) from a URL."""
    host = urlparse(url).hostname or ''
    parts = host.split('.')
    if len(parts) >= 2:
        return '.'.join(parts[-2:])
    return host

# Example usage
print(get_registered_domain('https://sub.example.co.uk'))  # co.uk (basic, not public suffix aware)
print(get_registered_domain('https://sub.example.com'))    # example.com
```

!!! note "Notes"
    - This is a basic split; for public suffix awareness, use tldextract (third-party)

<hr class="snippet-divider">

### Extract domain from IPv6 URL

`url` `extract` `domain` `ipv6` `netloc` `web`

Extract domain from IPv6 URL

```python
from urllib.parse import urlparse

url = 'http://[2001:db8::1]:8080/index.html'
parsed = urlparse(url)
print(parsed.hostname)  # 2001:db8::1
print(parsed.netloc)    # [2001:db8::1]:8080
```

!!! note "Notes"
    - hostname omits brackets for IPv6
    - netloc includes brackets and port

<hr class="snippet-divider">

## Edge Cases

###  Extract from URL with missing netloc or malformed URL

`url` `extract` `domain` `edge-case` `malformed` `web`

Extract from URL with missing netloc or malformed URL

```python
from urllib.parse import urlparse

url = 'not-a-url'
parsed = urlparse(url)
print(parsed.netloc)  # ''
print(parsed.hostname)  # None
```

!!! note "Notes"
    - Returns empty string or None if not present

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Parse URL](./parse_url.md)
- **Reference**: See [📂 Validate URL](./validate_url.md)
- **Reference**: See [📂 Build URL](./build_url.md)

## 🏷️ Tags

`url`, `extract`, `domain`, `host`, `port`, `tld`, `ipv6`, `edge-case`, `web`, `netloc`

## 📝 Notes

- Use urlparse for robust domain extraction
- For public suffix/registered domain, use tldextract (third-party) for accuracy
- Always validate URLs before extracting domains
