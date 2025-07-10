# Set Custom HTTP Headers

Zero-dependency Python snippets for setting custom HTTP headers in requests using the standard library.

## Simple

### 🧩 HTTP GET with custom headers

```python
import urllib.request

def http_get_with_headers(url, headers=None):
    """HTTP GET request with custom headers."""
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
url = "https://httpbin.org/headers"
headers = {"User-Agent": "stdlib-sniper/1.0", "X-Test": "true"}
result = http_get_with_headers(url, headers)
print(result)
```

📂 HTTP GET request with custom headers

🏷️ Tags: http, get, headers, request, web, urllib
📝 Notes:
- Headers must be a dictionary (case-insensitive)
- Common headers: User-Agent, Authorization, Accept, Content-Type

### 🧩 HTTP POST with custom headers

```python
import urllib.request
import urllib.parse

def http_post_with_headers(url, data, headers=None):
    """HTTP POST request with custom headers."""
    encoded_data = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=encoded_data, headers=headers or {}, method="POST")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
url = "https://httpbin.org/post"
data = {"key": "value"}
headers = {"User-Agent": "stdlib-sniper/1.0", "X-Test": "true"}
result = http_post_with_headers(url, data, headers)
print(result)
```

📂 HTTP POST request with custom headers

🏷️ Tags: http, post, headers, request, web, urllib
📝 Notes:
- Useful for APIs requiring authentication or custom identification
- Can set Content-Type, Accept, etc.

## Complex

### 🧩 HTTP GET with Authorization header (Bearer token)

```python
import urllib.request

def http_get_with_auth(url, token):
    """HTTP GET request with Bearer token authorization."""
    headers = {"Authorization": f"Bearer {token}"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
# url = "https://httpbin.org/bearer"
# token = "your_token_here"
# result = http_get_with_auth(url, token)
# print(result)
```

📂 HTTP GET with Bearer token authorization

🏷️ Tags: http, get, headers, authorization, bearer, token, web
📝 Notes:
- For APIs requiring Bearer or custom tokens
- Never hardcode secrets in code

### 🧩 HTTP GET with custom User-Agent and Accept headers

```python
import urllib.request

def http_get_with_user_agent(url, user_agent, accept=None):
    """HTTP GET with custom User-Agent and optional Accept header."""
    headers = {"User-Agent": user_agent}
    if accept:
        headers["Accept"] = accept
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
url = "https://httpbin.org/headers"
result = http_get_with_user_agent(url, "stdlib-sniper/2.0", accept="application/json")
print(result)
```

📂 HTTP GET with custom User-Agent and Accept headers

🏷️ Tags: http, get, headers, user-agent, accept, web
📝 Notes:
- Some servers require a User-Agent header
- Accept header can specify response format (e.g., JSON, XML)

### 🧩 Case-insensitivity and invalid headers

```python
import urllib.request

def http_get_case_insensitive(url, headers):
    """HTTP GET with headers (case-insensitive keys)."""
    # Python's urllib handles headers case-insensitively
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
url = "https://httpbin.org/headers"
headers = {"user-agent": "stdlib-sniper/3.0", "ACCEPT": "application/json"}
result = http_get_case_insensitive(url, headers)
print(result)

# Edge case: Invalid header (empty key)
try:
    bad_headers = {"": "value"}
    http_get_case_insensitive(url, bad_headers)
except Exception as e:
    print(f"Error: {e}")
```

📂 HTTP GET with case-insensitive and invalid headers

🏷️ Tags: http, get, headers, case-insensitive, error, web
📝 Notes:
- Header keys are case-insensitive in HTTP/urllib
- Invalid headers (empty key) raise ValueError

## Edge Cases

### 🧩 Missing or None headers

```python
def http_get_with_headers(url, headers=None):
    # Function is defined in one of the above code block
    pass


# Edge case: None headers (should default to empty dict)
url = "https://httpbin.org/headers"
result = http_get_with_headers(url, None)
print(result)

# Edge case: Missing required header (e.g., Authorization)
try:
    url = "https://httpbin.org/bearer"
    result = http_get_with_headers(url, {})
    print(result)
except Exception as e:
    print(f"Error: {e}")
```

📂 Edge cases for missing or None headers

🏷️ Tags: http, get, headers, edge-case, error, web
📝 Notes:
- Passing None for headers is safe (defaults to empty dict)
- Some APIs require specific headers; missing them may cause 401/403 errors

## 🔗 Cross-References

- **Reference**: See [📂 HTTP GET Request](./http_get.md)
- **Reference**: See [📂 HTTP POST Request](./http_post.md)
- **Reference**: See [📂 HTTP Basic Auth](./http_basic_auth.md)

## 🏷️ Tags

`http`, `headers`, `request`, `web`, `user-agent`, `authorization`, `accept`, `error`, `case-insensitive`, `edge-case`

## 📝 Notes

- Always validate and sanitize header values
- Never log or expose sensitive headers (e.g., Authorization)
- For cookies, use the Cookie header or `http.cookiejar`
- For advanced authentication, see HTTP Basic Auth snippet
- Some servers may reject requests with missing or malformed headers
