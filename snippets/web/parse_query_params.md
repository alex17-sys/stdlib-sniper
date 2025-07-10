# Parse Query Parameters from URL

Zero-dependency Python snippets for parsing query parameters from URLs using the standard library.

## Simple

### 🧩 Extract all query parameters as a dictionary

```python
from urllib.parse import urlparse, parse_qs

url = 'https://example.com/search?q=python&lang=en&page=1'
parsed = urlparse(url)
params = parse_qs(parsed.query)
print(params)  # {'q': ['python'], 'lang': ['en'], 'page': ['1']}
```

📂 Extract all query parameters as a dictionary

🏷️ Tags: url, parse, query, params, dict, web
📝 Notes:
- parse_qs returns a dict with lists of values
- Handles repeated keys as lists

### 🧩 Extract single-value query parameters

```python
from urllib.parse import urlparse, parse_qs

url = 'https://example.com/search?q=python&lang=en&page=1'
params = parse_qs(urlparse(url).query)
single_params = {k: v[0] for k, v in params.items()}
print(single_params)  # {'q': 'python', 'lang': 'en', 'page': '1'}
```

📂 Extract single-value query parameters

🏷️ Tags: url, parse, query, params, single, web
📝 Notes:
- Only use if you know each key appears once

### 🧩 Handle repeated keys in query string

```python
from urllib.parse import urlparse, parse_qs

url = 'https://example.com/search?tag=python&tag=web&tag=snippets'
params = parse_qs(urlparse(url).query)
print(params)  # {'tag': ['python', 'web', 'snippets']}
```

📂 Handle repeated keys in query string

🏷️ Tags: url, parse, query, params, repeated, web
📝 Notes:
- parse_qs always returns lists, even for single values

## Complex

### 🧩 Parse query string with missing values and encoded values

```python
from urllib.parse import urlparse, parse_qs

url = 'https://example.com/search?q=&lang=en%20US&empty'
params = parse_qs(urlparse(url).query)
print(params)  # {'q': [''], 'lang': ['en US'], 'empty': ['']}
```

📂 Parse query string with missing and encoded values

🏷️ Tags: url, parse, query, params, missing, encoded, web
📝 Notes:
- Keys with no value are mapped to ['']
- Encoded values are automatically decoded

## Edge Cases

### 🧩 Parse empty query string

```python
from urllib.parse import urlparse, parse_qs

url = 'https://example.com/'
params = parse_qs(urlparse(url).query)
print(params)  # {}
```

📂 Parse empty query string

🏷️ Tags: url, parse, query, params, empty, web
📝 Notes:
- Returns empty dict if no query string present

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
