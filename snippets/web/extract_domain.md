# Extract Domain from URL

Zero-dependency Python snippets for extracting the domain from URLs using the standard library.

## Simple

### 🧩 Extract netloc (host:port) from URL

```python
from urllib.parse import urlparse

url = 'https://sub.example.com:8080/path?query=1'
parsed = urlparse(url)
print(parsed.netloc)  # sub.example.com:8080
```

📂 Extract netloc (host:port) from URL

🏷️ Tags: url, extract, domain, netloc, host, web
📝 Notes:
- netloc includes subdomains and port if present

### 🧩 Extract host (domain) only (without port)

```python
from urllib.parse import urlparse

url = 'https://sub.example.com:8080/path'
parsed = urlparse(url)
host = parsed.hostname
print(host)  # sub.example.com
```

📂 Extract host (domain) only

🏷️ Tags: url, extract, domain, host, web
📝 Notes:
- hostname omits port and brackets for IPv6

### 🧩 Extract port from URL

```python
from urllib.parse import urlparse

url = 'https://example.com:8443/path'
parsed = urlparse(url)
port = parsed.port
print(port)  # 8443
```

📂 Extract port from URL

🏷️ Tags: url, extract, port, web
📝 Notes:
- Returns None if no port is specified

## Complex

### 🧩 Extract registered domain (TLD split, basic)

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

📂 Extract registered domain (basic TLD split)

🏷️ Tags: url, extract, domain, tld, registered, web
📝 Notes:
- This is a basic split; for public suffix awareness, use tldextract (third-party)

### 🧩 Extract domain from IPv6 URL

```python
from urllib.parse import urlparse

url = 'http://[2001:db8::1]:8080/index.html'
parsed = urlparse(url)
print(parsed.hostname)  # 2001:db8::1
print(parsed.netloc)    # [2001:db8::1]:8080
```

📂 Extract domain from IPv6 URL

🏷️ Tags: url, extract, domain, ipv6, netloc, web
📝 Notes:
- hostname omits brackets for IPv6
- netloc includes brackets and port

## Edge Cases

### 🧩 Extract from URL with missing netloc or malformed URL

```python
from urllib.parse import urlparse

url = 'not-a-url'
parsed = urlparse(url)
print(parsed.netloc)  # ''
print(parsed.hostname)  # None
```

📂 Extract from URL with missing netloc or malformed URL

🏷️ Tags: url, extract, domain, edge-case, malformed, web
📝 Notes:
- Returns empty string or None if not present

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
