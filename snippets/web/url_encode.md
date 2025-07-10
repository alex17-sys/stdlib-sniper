# URL Encode String

Zero-dependency Python snippets for URL encoding using the standard library.

## Simple

### 🧩 Encode query string parameters

```python
from urllib.parse import urlencode

params = {'q': 'python programming', 'lang': 'en', 'page': 1}
encoded = urlencode(params)
print(encoded)  # q=python+programming&lang=en&page=1
```

📂 Encode query string parameters

🏷️ Tags: url, encode, query, params, urlencode, web
📝 Notes:
- Spaces are encoded as + by default in query strings
- Use for GET/POST data

### 🧩 Encode path segment

```python
from urllib.parse import quote

segment = 'Café & Bistro/2024'
encoded = quote(segment)
print(encoded)  # Caf%C3%A9%20%26%20Bistro/2024

# To encode slashes as well:
encoded_strict = quote(segment, safe='')
print(encoded_strict)  # Caf%C3%A9%20%26%20Bistro%2F2024
```

📂 Encode path segment

🏷️ Tags: url, encode, path, quote, web
📝 Notes:
- quote() encodes special and non-ASCII characters
- Use safe='' to encode all reserved characters

### 🧩 Encode form data for POST

```python
from urllib.parse import urlencode

data = {'name': 'John Doe', 'email': 'john@example.com', 'message': 'Hello!'}
encoded = urlencode(data)
print(encoded)  # name=John+Doe&email=john%40example.com&message=Hello%21
```

📂 Encode form data for POST

🏷️ Tags: url, encode, form, post, urlencode, web
📝 Notes:
- Use for application/x-www-form-urlencoded POST bodies

## Complex

### 🧩 Encode with Unicode and reserved characters

```python
from urllib.parse import quote, urlencode

text = 'emoji: 😃 & symbols: @#%'
encoded = quote(text)
print(encoded)  # emoji%3A%20%F0%9F%98%83%20%26%20symbols%3A%20%40%23%25

params = {'q': 'café', 'emoji': '😃'}
encoded_params = urlencode(params)
print(encoded_params)  # q=caf%C3%A9&emoji=%F0%9F%98%83
```

📂 Encode with Unicode and reserved characters

🏷️ Tags: url, encode, unicode, reserved, web
📝 Notes:
- Unicode and emoji are percent-encoded
- Reserved characters (e.g., @, #, %) are encoded

## Edge Cases

### 🧩 Encode already-encoded strings and empty values

```python
from urllib.parse import quote

already_encoded = 'hello%20world'
encoded = quote(already_encoded)
print(encoded)  # hello%2520world (double-encoded)

empty = ''
print(quote(empty))  # ''
```

📂 Encode already-encoded strings and empty values

🏷️ Tags: url, encode, edge-case, double, empty, web
📝 Notes:
- Double-encoding can occur if input is already percent-encoded
- Empty strings remain empty

## 🔗 Cross-References

- **Reference**: See [📂 URL Decode String](./url_decode.md)
- **Reference**: See [📂 Parse URL](./parse_url.md)
- **Reference**: See [📂 Build URL](./build_url.md)

## 🏷️ Tags

`url`, `encode`, `query`, `params`, `form`, `unicode`, `reserved`, `edge-case`, `web`, `quote`, `urlencode`

## 📝 Notes

- Use `quote` for path segments, `urlencode` for query/form data
- Always encode user input before including in URLs
- For decoding, see `urllib.parse.unquote` and `parse_qs`
