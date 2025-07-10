# URL Decode String

Zero-dependency Python snippets for URL decoding using the standard library.

## Simple

### 🧩 Decode query string parameters

```python
from urllib.parse import parse_qs

query = 'q=python+programming&lang=en&page=1'
params = parse_qs(query)
print(params)  # {'q': ['python programming'], 'lang': ['en'], 'page': ['1']}
```

📂 Decode query string parameters

🏷️ Tags: url, decode, query, params, parse_qs, web
📝 Notes:
- parse_qs decodes + as space and percent-encoded characters
- Returns dict with lists of values

### 🧩 Decode path segment

```python
from urllib.parse import unquote

encoded = 'Caf%C3%A9%20%26%20Bistro%2F2024'
decoded = unquote(encoded)
print(decoded)  # Café & Bistro/2024
```

📂 Decode path segment

🏷️ Tags: url, decode, path, unquote, web
📝 Notes:
- unquote decodes percent-encoded and non-ASCII characters

### 🧩 Decode form data from POST

```python
from urllib.parse import parse_qs

encoded = 'name=John+Doe&email=john%40example.com&message=Hello%21'
params = parse_qs(encoded)
print(params)  # {'name': ['John Doe'], 'email': ['john@example.com'], 'message': ['Hello!']}
```

📂 Decode form data from POST

🏷️ Tags: url, decode, form, post, parse_qs, web
📝 Notes:
- Use for application/x-www-form-urlencoded POST bodies

## Complex

### 🧩 Decode with Unicode and reserved characters

```python
from urllib.parse import unquote

encoded = 'emoji%3A%20%F0%9F%98%83%20%26%20symbols%3A%20%40%23%25'
decoded = unquote(encoded)
print(decoded)  # emoji: 😃 & symbols: @#%
```

📂 Decode with Unicode and reserved characters

🏷️ Tags: url, decode, unicode, reserved, web
📝 Notes:
- Handles emoji and special symbols
- Decodes all percent-encoded bytes

## Edge Cases

### 🧩 Double decoding and empty values

```python
from urllib.parse import unquote

# Double-encoded string
double_encoded = 'hello%2520world'
first = unquote(double_encoded)
second = unquote(first)
print(first)   # hello%20world
print(second) # hello world

# Empty string
print(unquote(''))  # ''
```

📂 Double decoding and empty values

🏷️ Tags: url, decode, edge-case, double, empty, web
📝 Notes:
- Double decoding may be needed if input was encoded multiple times
- Empty strings remain empty

## 🔗 Cross-References

- **Reference**: See [📂 URL Encode String](./url_encode.md)
- **Reference**: See [📂 Parse URL](./parse_url.md)
- **Reference**: See [📂 Build URL](./build_url.md)

## 🏷️ Tags

`url`, `decode`, `query`, `params`, `form`, `unicode`, `reserved`, `edge-case`, `web`, `unquote`, `parse_qs`

## 📝 Notes

- Use `unquote` for path segments, `parse_qs` for query/form data
- Always decode user input before processing
- For encoding, see `urllib.parse.quote` and `urlencode`
