---
title: Build URL
description: Zero-dependency Python snippets for building URLs using the standard library.
keywords: base, build, components, double-slash, edge-case, fragment, ftp, join, missing, params, password, port, query, relative, url, urlunparse, user, web
---

# Build URL

Zero-dependency Python snippets for building URLs using the standard library.

6 snippets available in this sub-category.

---

## Simple

###  Build URL from components

`url` `build` `components` `urlunparse` `web`

Build URL from components

```python
from urllib.parse import urlunparse

def build_url(scheme, netloc, path, params='', query='', fragment=''):
    """Build a URL from its components."""
    return urlunparse((scheme, netloc, path, params, query, fragment))

# Example usage
url = build_url('https', 'example.com', '/search', '', 'q=python', 'section')
print(url)  # https://example.com/search?q=python#section
```

!!! note "Notes"
    - urlunparse takes a 6-tuple: (scheme, netloc, path, params, query, fragment)
    - Use empty strings for missing parts

<hr class="snippet-divider">

### Add or replace query parameters in URL

`url` `build` `query` `params` `web`

Add or replace query parameters in URL

```python
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def add_query_params(url, params):
    """Add or replace query parameters in a URL."""
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    query.update(params)
    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))

# Example usage
url = "https://example.com/search?q=python"
new_url = add_query_params(url, {"lang": "en", "q": "ai"})
print(new_url)  # https://example.com/search?q=ai&lang=en
```

!!! note "Notes"
    - `doseq=True` allows multiple values per key
    - Existing parameters are replaced if keys match

<hr class="snippet-divider">

### Join base and relative URLs

`url` `build` `join` `base` `relative` `web`

Join base and relative URLs

```python
from urllib.parse import urljoin

base = "https://example.com/docs/"
relative = "../about/contact.html"
full_url = urljoin(base, relative)
print(full_url)  # https://example.com/about/contact.html
```

!!! note "Notes"
    - urljoin resolves relative paths against a base URL
    - Handles .., ., and missing slashes

<hr class="snippet-divider">

## Complex

###  Build URL with user, password, and port

`url` `build` `user` `password` `port` `ftp` `web`

Build URL with user, password, and port

```python
from urllib.parse import urlunparse

def build_url_with_auth(scheme, user, password, host, port, path):
    """Build a URL with user, password, and port."""
    netloc = f"{user}:{password}@{host}:{port}" if user and password else f"{host}:{port}"
    return urlunparse((scheme, netloc, path, '', '', ''))

# Example usage
url = build_url_with_auth('ftp', 'user', 'pass', 'ftp.example.com', 2121, '/files')
print(url)  # ftp://user:pass@ftp.example.com:2121/files
```

!!! note "Notes"
    - Useful for FTP, SFTP, and authenticated endpoints

<hr class="snippet-divider">

### Build URL with fragment and params

`url` `build` `fragment` `params` `web`

Build URL with fragment and params

```python
from urllib.parse import urlunparse

url = urlunparse(('https', 'example.com', '/page', '', '', 'section2'))
print(url)  # https://example.com/page#section2

url2 = urlunparse(('http', 'example.com', '/api', 'action', '', ''))
print(url2)  # http://example.com/api;action
```

!!! note "Notes"
    - Fragments follow #, params follow ; in the path

<hr class="snippet-divider">

## Edge Cases

###  Build URL with missing parts and double slashes

`url` `build` `edge-case` `missing` `double-slash` `web`

Build URL with missing parts and double slashes

```python
from urllib.parse import urlunparse

# Missing netloc (relative URL)
url = urlunparse(('https', '', '/about', '', '', ''))
print(url)  # https:///about

# Double slashes in path
url2 = urlunparse(('https', 'example.com', '//double/slash', '', '', ''))
print(url2)  # https://example.com//double/slash
```

!!! note "Notes"
    - urlunparse does not normalize double slashes in path
    - Missing netloc results in scheme:///path

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Parse URL](./parse_url.md)
- **Reference**: See [📂 URL Join](./url_join.md)
- **Reference**: See [📂 URL Encode String](./url_encode.md)

## 🏷️ Tags

`url`, `build`, `join`, `query`, `params`, `fragment`, `edge-case`, `web`, `ftp`

## 📝 Notes

- Use `urlunparse` and `urljoin` for robust URL building
- Always validate and encode user input in URLs
- For more advanced manipulation, see `urllib.parse` docs
