---
title: Remove Query Parameters from URL
description: Zero-dependency Python snippets for removing query parameters from URLs using the standard library.
keywords: all, edge-case, empty, encoded, multi, params, query, remove, url, urlencode, web
---

# Remove Query Parameters from URL

Zero-dependency Python snippets for removing query parameters from URLs using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Remove a single query parameter

`url` `remove` `query` `params` `urlencode` `web`

Remove a single query parameter

```python
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def remove_query_param(url, key):
    """Remove a single query parameter from a URL."""
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    query.pop(key, None)
    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))

# Example usage
url = 'https://example.com/search?q=python&lang=en&page=1'
new_url = remove_query_param(url, 'lang')
print(new_url)  # https://example.com/search?q=python&page=1
```

!!! note "Notes"
    - If key is not present, URL is unchanged

<hr class="snippet-divider">

### Remove multiple query parameters

`url` `remove` `query` `params` `multi` `urlencode` `web`

Remove multiple query parameters

```python
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def remove_query_params(url, keys):
    """Remove multiple query parameters from a URL."""
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    for key in keys:
        query.pop(key, None)
    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))

# Example usage
url = 'https://example.com/search?q=python&lang=en&page=1'
new_url = remove_query_params(url, ['q', 'page'])
print(new_url)  # https://example.com/search?lang=en
```

!!! note "Notes"
    - Removes all specified keys if present

<hr class="snippet-divider">

## Complex

###  Remove all query parameters

`url` `remove` `query` `params` `all` `web`

Remove all query parameters

```python
from urllib.parse import urlparse, urlunparse

def remove_all_query_params(url):
    """Remove all query parameters from a URL."""
    parsed = urlparse(url)
    return urlunparse(parsed._replace(query=''))

# Example usage
url = 'https://example.com/search?q=python&lang=en&page=1'
new_url = remove_all_query_params(url)
print(new_url)  # https://example.com/search
```

!!! note "Notes"
    - Leaves only the base URL and path

<hr class="snippet-divider">

## Edge Cases

###  Remove non-existent or encoded keys, empty query

`url` `remove` `query` `params` `edge-case` `encoded` `empty` `web`

Remove non-existent or encoded keys, empty query

```python
def remove_query_param(url, key):
    # Function is defined in one of the above code block
    pass


# Remove non-existent key
url = 'https://example.com/search?q=python'
print(remove_query_param(url, 'lang'))  # https://example.com/search?q=python

# Remove encoded key
url2 = 'https://example.com/search?na%20me=John&q=python'
print(remove_query_param(url2, 'na me'))  # https://example.com/search?q=python

# Remove from URL with no query
url3 = 'https://example.com/'
print(remove_query_param(url3, 'q'))  # https://example.com/
```

!!! note "Notes"
    - Removing a key not present has no effect
    - Encoded keys must match decoded form
    - Removing from empty query leaves URL unchanged

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Parse Query Params](./parse_query_params.md)
- **Reference**: See [📂 Add Query Params](./add_query_params.md)
- **Reference**: See [📂 URL Encode String](./url_encode.md)

## 🏷️ Tags

`url`, `remove`, `query`, `params`, `multi`, `all`, `edge-case`, `encoded`, `empty`, `web`, `urlencode`

## 📝 Notes

- Use parse_qs and urlunparse for robust query manipulation
- Always validate and encode/decode keys as needed
- For adding or modifying queries, see urlencode and parse_qs
