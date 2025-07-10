# Convert Relative URL to Absolute URL

Zero-dependency Python snippets for converting relative URLs to absolute URLs using the standard library.

## Simple

### 🧩 Convert relative URL to absolute using base

```python
from urllib.parse import urljoin

base = 'https://example.com/docs/'
relative = 'about/contact.html'
absolute = urljoin(base, relative)
print(absolute)  # https://example.com/docs/about/contact.html
```

📂 Convert relative URL to absolute using base

🏷️ Tags: url, relative, absolute, join, urljoin, web
📝 Notes:
- urljoin resolves relative URLs against a base

### 🧩 Convert with dot segments (.. and .)

```python
from urllib.parse import urljoin

base = 'https://example.com/docs/tutorials/'
relative = '../about/./contact.html'
absolute = urljoin(base, relative)
print(absolute)  # https://example.com/about/contact.html
```

📂 Convert with dot segments

🏷️ Tags: url, relative, absolute, dot, urljoin, web
📝 Notes:
- .. moves up one directory, . stays in the same directory

## Complex

### 🧩 Convert already absolute URL

```python
from urllib.parse import urljoin

base = 'https://example.com/docs/'
relative = 'https://other.com/page'
absolute = urljoin(base, relative)
print(absolute)  # https://other.com/page
```

📂 Convert already absolute URL

🏷️ Tags: url, relative, absolute, urljoin, web
📝 Notes:
- If relative is already absolute, it replaces the base

## Edge Cases

### 🧩 Convert with empty base or malformed URLs

```python
    # Code is defined in another file (URL Join (Join with empty base or malformed URLs)) cited below
```

📂 Convert with empty base or malformed URLs

🏷️ Tags: url, relative, absolute, edge-case, empty, malformed, urljoin, web
📝 Notes:
- If base is empty or malformed, returns the relative URL as-is

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
