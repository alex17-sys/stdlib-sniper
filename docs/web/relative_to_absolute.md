---
title: Convert Relative URL to Absolute URL
description: Zero-dependency Python snippets for converting relative URLs to absolute URLs using the standard library.
keywords: absolute, dot, edge-case, empty, join, malformed, relative, url, urljoin, web
---

# Convert Relative URL to Absolute URL

Zero-dependency Python snippets for converting relative URLs to absolute URLs using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Convert relative URL to absolute using base

`url` `relative` `absolute` `join` `urljoin` `web`

Convert relative URL to absolute using base

```python
from urllib.parse import urljoin

base = 'https://example.com/docs/'
relative = 'about/contact.html'
absolute = urljoin(base, relative)
print(absolute)  # https://example.com/docs/about/contact.html
```

!!! note "Notes"
    - urljoin resolves relative URLs against a base

<hr class="snippet-divider">

### Convert with dot segments (.. and .)

`url` `relative` `absolute` `dot` `urljoin` `web`

Convert with dot segments

```python
from urllib.parse import urljoin

base = 'https://example.com/docs/tutorials/'
relative = '../about/./contact.html'
absolute = urljoin(base, relative)
print(absolute)  # https://example.com/about/contact.html
```

!!! note "Notes"
    - .. moves up one directory, . stays in the same directory

<hr class="snippet-divider">

## Complex

###  Convert already absolute URL

`url` `relative` `absolute` `urljoin` `web`

Convert already absolute URL

```python
from urllib.parse import urljoin

base = 'https://example.com/docs/'
relative = 'https://other.com/page'
absolute = urljoin(base, relative)
print(absolute)  # https://other.com/page
```

!!! note "Notes"
    - If relative is already absolute, it replaces the base

<hr class="snippet-divider">

## Edge Cases

###  Convert with empty base or malformed URLs

`url` `relative` `absolute` `edge-case` `empty` `malformed` `urljoin` `web`

Convert with empty base or malformed URLs

```python
# Code is defined in another file (URL Join (Join with empty base or malformed URLs)) cited below
```

!!! note "Notes"
    - If base is empty or malformed, returns the relative URL as-is

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 URL Join](./url_join.md)
- **Reference**: See [📂 Build URL](./build_url.md)
- **Reference**: See [📂 Parse URL](./parse_url.md)

## 🏷️ Tags

`url`, `relative`, `absolute`, `join`, `dot`, `edge-case`, `web`, `urljoin`

## 📝 Notes

- Use urljoin for robust conversion of relative to absolute URLs
- Always validate and normalize URLs before use
- For advanced manipulation, see urllib.parse docs
