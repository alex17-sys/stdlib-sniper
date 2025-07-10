---
title: Parse URL
description: Zero-dependency Python snippets for parsing URLs using the standard library.
keywords: components, edge-case, extract, ftp, ipv6, params, parse, password, port, query, relative, scheme, url, urllib, user, web
---

# Parse URL

Zero-dependency Python snippets for parsing URLs using the standard library.

6 snippets available in this sub-category.

---

## Simple

###  Parse URL into components

`url` `parse` `components` `urllib` `web`

Parse URL into components

```python
from urllib.parse import urlparse

def parse_url(url):
    """Parse a URL and return its components."""
    parsed = urlparse(url)
    return parsed

# Example usage
url = "https://user:pass@example.com:8080/path/to/page?query=python#section"
parsed = parse_url(url)
print(parsed)
# ParseResult(scheme='https', netloc='user:pass@example.com:8080', path='/path/to/page', params='', query='query=python', fragment='section')
```

!!! note "Notes"
    - Returns a ParseResult with attributes: scheme, netloc, path, params, query, fragment
    - Use dot notation to access each part

<hr class="snippet-divider">

### Extract individual URL components

`url` `parse` `extract` `components` `web`

Extract individual URL components

```python
from urllib.parse import urlparse

url = "https://user:pass@example.com:8080/path/to/page?query=python#section"
parsed = urlparse(url)
print("Scheme:", parsed.scheme)
print("Netloc:", parsed.netloc)
print("Path:", parsed.path)
print("Params:", parsed.params)
print("Query:", parsed.query)
print("Fragment:", parsed.fragment)
```

!!! note "Notes"
    - Useful for routing, validation, and analytics

<hr class="snippet-divider">

### Parse query parameters from URL

`url` `parse` `query` `params` `web`

Parse query parameters from URL

```python
from urllib.parse import urlparse, parse_qs

url = "https://example.com/search?q=python&lang=en&lang=fr"
parsed = urlparse(url)
query_params = parse_qs(parsed.query)
print(query_params)
# {'q': ['python'], 'lang': ['en', 'fr']}
```

!!! note "Notes"
    - `parse_qs` returns a dict with lists of values
    - Handles repeated parameters

<hr class="snippet-divider">

## Complex

###  Handle missing scheme and relative URLs

`url` `parse` `scheme` `relative` `edge-case` `web`

Handle missing scheme and relative URLs

```python
from urllib.parse import urlparse

# Missing scheme
url = "www.example.com/path"
parsed = urlparse(url)
print(parsed)
# ParseResult(scheme='', netloc='', path='www.example.com/path', params='', query='', fragment='')

# Relative URL
url2 = "/about/contact"
parsed2 = urlparse(url2)
print(parsed2)
# ParseResult(scheme='', netloc='', path='/about/contact', params='', query='', fragment='')
```

!!! note "Notes"
    - If scheme is missing, netloc is empty and path contains the whole string
    - Relative URLs are parsed as path only

<hr class="snippet-divider">

### Parse non-standard ports and user info

`url` `parse` `port` `user` `password` `ftp` `web`

Parse non-standard ports and user info

```python
from urllib.parse import urlparse

url = "ftp://user:pass@ftp.example.com:2121/files"
parsed = urlparse(url)
print("Scheme:", parsed.scheme)
print("Netloc:", parsed.netloc)
print("Path:", parsed.path)

# Extract user, password, host, port manually
userinfo, hostport = parsed.netloc.split('@') if '@' in parsed.netloc else ('', parsed.netloc)
user, password = userinfo.split(':') if ':' in userinfo else (userinfo, '')
host, port = hostport.split(':') if ':' in hostport else (hostport, '')
print("User:", user)
print("Password:", password)
print("Host:", host)
print("Port:", port)
```

!!! note "Notes"
    - urlparse does not split user/pass/host/port automatically
    - Manual parsing is needed for advanced use cases

<hr class="snippet-divider">

## Edge Cases

###  Parse URL with IPv6 address

`url` `parse` `ipv6` `edge-case` `web`

Parse URL with IPv6 address

```python
from urllib.parse import urlparse

url = "http://[2001:db8::1]:8080/index.html"
parsed = urlparse(url)
print(parsed)
# ParseResult(scheme='http', netloc='[2001:db8::1]:8080', path='/index.html', params='', query='', fragment='')
```

!!! note "Notes"
    - IPv6 addresses are enclosed in square brackets
    - Port follows after colon

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Build URL](./build_url.md)
- **Reference**: See [📂 Parse Query Params](./parse_query_params.md)
- **Reference**: See [📂 URL Encode String](./url_encode.md)

## 🏷️ Tags

`url`, `parse`, `components`, `query`, `params`, `edge-case`, `web`, `ipv6`, `ftp`

## 📝 Notes

- Use `urlparse` for robust URL parsing
- For joining or building URLs, see `urljoin` and `urlunparse`
- Always validate URLs before using in production
