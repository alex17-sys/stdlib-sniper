---
title: Parse Query Parameters from URL
description: Zero-dependency Python snippets for parsing query parameters from URLs using the standard library.
keywords: dict, empty, encoded, missing, params, parse, query, repeated, single, url, web
---

# Parse Query Parameters from URL

Zero-dependency Python snippets for parsing query parameters from URLs using the standard library.

5 snippets available in this sub-category.

---

## Simple

###  Extract all query parameters as a dictionary

`url` `parse` `query` `params` `dict` `web`

Extract all query parameters as a dictionary

```python
from urllib.parse import urlparse, parse_qs

url = 'https://example.com/search?q=python&lang=en&page=1'
parsed = urlparse(url)
params = parse_qs(parsed.query)
print(params)  # {'q': ['python'], 'lang': ['en'], 'page': ['1']}
```

!!! note "Notes"
    - parse_qs returns a dict with lists of values
    - Handles repeated keys as lists

<hr class="snippet-divider">

### Extract single-value query parameters

`url` `parse` `query` `params` `single` `web`

Extract single-value query parameters

```python
from urllib.parse import urlparse, parse_qs

url = 'https://example.com/search?q=python&lang=en&page=1'
params = parse_qs(urlparse(url).query)
single_params = {k: v[0] for k, v in params.items()}
print(single_params)  # {'q': 'python', 'lang': 'en', 'page': '1'}
```

!!! note "Notes"
    - Only use if you know each key appears once

<hr class="snippet-divider">

### Handle repeated keys in query string

`url` `parse` `query` `params` `repeated` `web`

Handle repeated keys in query string

```python
from urllib.parse import urlparse, parse_qs

url = 'https://example.com/search?tag=python&tag=web&tag=snippets'
params = parse_qs(urlparse(url).query)
print(params)  # {'tag': ['python', 'web', 'snippets']}
```

!!! note "Notes"
    - parse_qs always returns lists, even for single values

<hr class="snippet-divider">

## Complex

###  Parse query string with missing values and encoded values

`url` `parse` `query` `params` `missing` `encoded` `web`

Parse query string with missing and encoded values

```python
from urllib.parse import urlparse, parse_qs

url = 'https://example.com/search?q=&lang=en%20US&empty'
params = parse_qs(urlparse(url).query)
print(params)  # {'q': [''], 'lang': ['en US'], 'empty': ['']}
```

!!! note "Notes"
    - Keys with no value are mapped to ['']
    - Encoded values are automatically decoded

<hr class="snippet-divider">

## Edge Cases

###  Parse empty query string

`url` `parse` `query` `params` `empty` `web`

Parse empty query string

```python
from urllib.parse import urlparse, parse_qs

url = 'https://example.com/'
params = parse_qs(urlparse(url).query)
print(params)  # {}
```

!!! note "Notes"
    - Returns empty dict if no query string present

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Add Query Params](./add_query_params.md)
- **Reference**: See [📂 Remove Query Params](./remove_query_params.md)
- **Reference**: See [📂 URL Encode String](./url_encode.md)

## 🏷️ Tags

`url`, `parse`, `query`, `params`, `dict`, `repeated`, `encoded`, `empty`, `web`

## 📝 Notes

- Use parse_qs for robust query parameter parsing
- Always handle lists for repeated keys
- For building or modifying queries, see urlencode and urlunparse
