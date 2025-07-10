---
title: URL Join
description: Zero-dependency Python snippets for joining URLs using the standard library.
keywords: absolute, base, dot, edge-case, empty, fragment, join, malformed, query, relative, segments, trailing-slash, url, urljoin, web
---

# URL Join

Zero-dependency Python snippets for joining URLs using the standard library.

6 snippets available in this sub-category.

---

## Simple

###  Join base and relative URLs

`url` `join` `base` `relative` `urljoin` `web`

Join base and relative URLs

```python
from urllib.parse import urljoin

base = 'https://example.com/docs/'
relative = 'about/contact.html'
full_url = urljoin(base, relative)
print(full_url)  # https://example.com/docs/about/contact.html
```

!!! note "Notes"
    - urljoin resolves relative paths against a base URL
    - Handles missing or extra slashes

<hr class="snippet-divider">

### Join with dot segments (.. and .)

`url` `join` `dot` `segments` `urljoin` `web`

Join with dot segments

```python
from urllib.parse import urljoin

base = 'https://example.com/docs/tutorials/'
relative = '../about/./contact.html'
full_url = urljoin(base, relative)
print(full_url)  # https://example.com/about/contact.html
```

!!! note "Notes"
    - .. moves up one directory, . stays in the same directory

<hr class="snippet-divider">

### Join with/without trailing slashes

`url` `join` `trailing-slash` `urljoin` `web`

Join with/without trailing slashes

```python
from urllib.parse import urljoin

base1 = 'https://example.com/docs'
relative1 = 'page.html'
print(urljoin(base1, relative1))  # https://example.com/page.html

base2 = 'https://example.com/docs/'
relative2 = 'page.html'
print(urljoin(base2, relative2))  # https://example.com/docs/page.html
```

!!! note "Notes"
    - Trailing slash on base affects the result
    - No slash: replaces last segment; slash: appends to directory

<hr class="snippet-divider">

## Complex

###  Join with query and fragment

`url` `join` `query` `fragment` `urljoin` `web`

Join with query and fragment

```python
from urllib.parse import urljoin

base = 'https://example.com/search?q=python'
relative = 'results#section2'
full_url = urljoin(base, relative)
print(full_url)  # https://example.com/results#section2
```

!!! note "Notes"
    - Relative URL can override query and fragment of base

<hr class="snippet-divider">

### Join with absolute relative URL

`url` `join` `absolute` `urljoin` `web`

Join with absolute relative URL

```python
from urllib.parse import urljoin

base = 'https://example.com/docs/'
relative = 'https://other.com/page'
full_url = urljoin(base, relative)
print(full_url)  # https://other.com/page
```

!!! note "Notes"
    - If relative is absolute, it replaces the base

<hr class="snippet-divider">

## Edge Cases

###  Join with empty base or malformed URLs

`url` `join` `edge-case` `empty` `malformed` `urljoin` `web`

Join with empty base or malformed URLs

```python
from urllib.parse import urljoin

# Empty base
print(urljoin('', 'page.html'))  # page.html

# Malformed base
print(urljoin('not-a-url', 'page.html'))  # page.html
```

!!! note "Notes"
    - If base is empty or malformed, returns the relative URL as-is

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Build URL](./build_url.md)
- **Reference**: See [📂 Parse URL](./parse_url.md)
- **Reference**: See [📂 URL Encode String](./url_encode.md)

## 🏷️ Tags

`url`, `join`, `base`, `relative`, `query`, `fragment`, `dot`, `trailing-slash`, `edge-case`, `web`, `urljoin`

## 📝 Notes

- Use `urljoin` for robust URL joining and resolution
- Always validate and normalize URLs before use
- For advanced manipulation, see `urllib.parse` docs
