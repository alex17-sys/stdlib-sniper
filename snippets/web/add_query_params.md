# Add Query Parameters to URL

Zero-dependency Python snippets for adding query parameters to URLs using the standard library.

## Simple

### 🧩 Add new query parameters to URL

```python
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def add_query_params(url, params):
    """Add new query parameters to a URL."""
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    query.update(params)
    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))

# Example usage
url = 'https://example.com/search?q=python'
new_url = add_query_params(url, {'lang': 'en', 'page': 2})
print(new_url)  # https://example.com/search?q=python&lang=en&page=2
```

📂 Add new query parameters to URL

🏷️ Tags: url, add, query, params, urlencode, web
📝 Notes:
- Existing parameters are preserved
- New parameters are appended

### 🧩 Replace existing query parameters

```python
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def replace_query_param(url, key, value):
    """Replace a single query parameter in a URL."""
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    query[key] = [value]
    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))

# Example usage
url = 'https://example.com/search?q=python&lang=en'
new_url = replace_query_param(url, 'q', 'ai')
print(new_url)  # https://example.com/search?q=ai&lang=en
```

📂 Replace existing query parameters

🏷️ Tags: url, replace, query, params, urlencode, web
📝 Notes:
- Only the specified key is replaced
- Other parameters remain unchanged

## Complex

### 🧩 Add multiple values for a single key

```python
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def add_multi_value_param(url, key, values):
    """Add multiple values for a single query key."""
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    query[key] = values
    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))

# Example usage
url = 'https://example.com/search'
new_url = add_multi_value_param(url, 'tag', ['python', 'web', 'snippets'])
print(new_url)  # https://example.com/search?tag=python&tag=web&tag=snippets
```

📂 Add multiple values for a single key

🏷️ Tags: url, add, query, params, multi-value, urlencode, web
📝 Notes:
- doseq=True encodes each value as a separate key

## Edge Cases

### 🧩 Add to URL with empty or no query string

```python
from urllib.parse import urlparse, urlencode, urlunparse

def add_query_to_empty(url, params):
    """Add query parameters to a URL with no query string."""
    parsed = urlparse(url)
    new_query = urlencode(params)
    return urlunparse(parsed._replace(query=new_query))

# Example usage
url = 'https://example.com/'
new_url = add_query_to_empty(url, {'q': 'python'})
print(new_url)  # https://example.com/?q=python
```

📂 Add to URL with empty or no query string

🏷️ Tags: url, add, query, params, empty, urlencode, web
📝 Notes:
- Works even if original URL has no query string

## 🔗 Cross-References

- **Reference**: See [📂 Parse Query Params](./parse_query_params.md)
- **Reference**: See [📂 Remove Query Params](./remove_query_params.md)
- **Reference**: See [📂 URL Encode String](./url_encode.md)

## 🏷️ Tags

`url`, `add`, `query`, `params`, `replace`, `multi-value`, `empty`, `web`, `urlencode`

## 📝 Notes

- Use urlencode with doseq=True for multi-value keys
- Always validate and encode user input in URLs
- For removing or modifying queries, see parse_qs and urlunparse
