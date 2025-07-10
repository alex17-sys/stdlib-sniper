---
title: HTTP DELETE Request
description: Zero-dependency Python snippets for making HTTP DELETE requests using the standard library.
keywords: authentication, basic-auth, delete, edge-case, error, handling, headers, http, params, query, request, urllib, web
---

# HTTP DELETE Request

Zero-dependency Python snippets for making HTTP DELETE requests using the standard library.

6 snippets available in this sub-category.

---

## Simple

###  Simple HTTP DELETE request

`http` `delete` `request` `web` `urllib`

Simple HTTP DELETE request

```python
import urllib.request

def http_delete(url):
    """Perform a simple HTTP DELETE request."""
    req = urllib.request.Request(url, method="DELETE")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
# url = "https://httpbin.org/delete"
# result = http_delete(url)
# print(result)
```

!!! note "Notes"
    - DELETE is used to remove resources
    - Not all servers support DELETE

<hr class="snippet-divider">

### HTTP DELETE with custom headers

`http` `delete` `headers` `request` `web` `urllib`

HTTP DELETE request with custom headers

```python
import urllib.request

def http_delete_with_headers(url, headers=None):
    """HTTP DELETE request with custom headers."""
    req = urllib.request.Request(url, headers=headers or {}, method="DELETE")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
# url = "https://httpbin.org/delete"
# headers = {"User-Agent": "stdlib-sniper/1.0", "X-Test": "true"}
# result = http_delete_with_headers(url, headers)
# print(result)
```

!!! note "Notes"
    - Useful for APIs requiring authentication or custom identification

<hr class="snippet-divider">

### HTTP DELETE with query parameters

`http` `delete` `params` `query` `request` `web`

HTTP DELETE request with query parameters

```python
import urllib.request
import urllib.parse

def http_delete_with_params(url, params):
    """HTTP DELETE request with query parameters."""
    query = urllib.parse.urlencode(params)
    full_url = f"{url}?{query}" if params else url
    req = urllib.request.Request(full_url, method="DELETE")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
# url = "https://httpbin.org/delete"
# params = {"id": 123, "force": "yes"}
# result = http_delete_with_params(url, params)
# print(result)
```

!!! note "Notes"
    - Query parameters are appended to the URL
    - Useful for RESTful APIs

<hr class="snippet-divider">

## Complex

###  HTTP DELETE with authentication (Basic Auth)

`http` `delete` `basic-auth` `authentication` `headers` `web`

HTTP DELETE request with Basic Authentication

```python
import urllib.request
import base64

def http_delete_basic_auth(url, username, password):
    """HTTP DELETE request with Basic Authentication."""
    credentials = f"{username}:{password}".encode("utf-8")
    encoded_credentials = base64.b64encode(credentials).decode("utf-8")
    headers = {"Authorization": f"Basic {encoded_credentials}"}
    req = urllib.request.Request(url, headers=headers, method="DELETE")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
# url = "https://httpbin.org/delete"
# result = http_delete_basic_auth(url, "user", "pass")
# print(result)
```

!!! note "Notes"
    - Encodes credentials as base64
    - Use for endpoints requiring authentication

<hr class="snippet-divider">

### HTTP DELETE with error handling

`http` `delete` `error` `handling` `request` `web`

HTTP DELETE request with error handling

```python
import urllib.request
import urllib.error

def http_delete_safe(url, headers=None):
    """HTTP DELETE request with error handling."""
    try:
        req = urllib.request.Request(url, headers=headers or {}, method="DELETE")
        with urllib.request.urlopen(req) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

# Example usage
# url = "https://httpbin.org/status/405"  # Method Not Allowed
# result = http_delete_safe(url)
# print(result)
```

!!! note "Notes"
    - Handles HTTP and URL errors
    - Returns None on failure

<hr class="snippet-divider">

## Edge Cases

###  Invalid URL, unsupported method, missing authentication

`http` `delete` `error` `edge-case` `authentication` `web`

Edge cases: invalid URL, unsupported method, missing authentication

```python
def http_delete_safe(url, headers=None):
    # Function is defined in one of the above code block
    pass


# Edge case: Invalid URL
try:
    http_delete_safe("not-a-url")
except Exception as e:
    print(f"Error: {e}")

# Edge case: Unsupported method (server returns 405)
# Edge case: Missing authentication (server returns 401/403)
```

!!! note "Notes"
    - Invalid URLs raise URLError or ValueError
    - Some servers do not support DELETE (405 Method Not Allowed)
    - Missing authentication may result in 401/403 errors

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 HTTP GET Request](./http_get.md)
- **Reference**: See [📂 HTTP POST Request](./http_post.md)
- **Reference**: See [📂 HTTP Headers](./http_headers.md)
- **Reference**: See [📂 HTTP Basic Auth](./http_basic_auth.md)

## 🏷️ Tags

`http`, `delete`, `request`, `headers`, `params`, `basic-auth`, `authentication`, `error`, `edge-case`, `web`

## 📝 Notes

- DELETE is not idempotent on all servers (check API docs)
- For soft deletes, use PATCH or custom endpoints
- Always check server documentation for supported methods
- For async or batch deletes, consider `asyncio` or third-party libraries
