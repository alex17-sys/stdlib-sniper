---
title: HTTP PUT Request
description: Zero-dependency Python snippets for making HTTP PUT requests using the standard library.
keywords: api, binary, edge-case, error, file, handling, headers, http, json, put, request, string, upload, urllib, web
---

# HTTP PUT Request

Zero-dependency Python snippets for making HTTP PUT requests using the standard library.

6 snippets available in this sub-category.

---

## Simple

###  Simple HTTP PUT request (string data)

`http` `put` `request` `web` `string` `urllib`

Simple HTTP PUT request (string data)

```python
import urllib.request

def http_put(url, data):
    """Perform a simple HTTP PUT request with string data."""
    req = urllib.request.Request(url, data=data.encode("utf-8"), method="PUT")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
# url = "https://httpbin.org/put"
# data = "Hello, PUT!"
# result = http_put(url, data)
# print(result)
```

!!! note "Notes"
    - Data must be bytes (encode string to utf-8)
    - PUT is used for updating/replacing resources

<hr class="snippet-divider">

### HTTP PUT with custom headers

`http` `put` `headers` `request` `web` `urllib`

HTTP PUT request with custom headers

```python
import urllib.request

def http_put_with_headers(url, data, headers=None):
    """HTTP PUT request with custom headers."""
    req = urllib.request.Request(url, data=data.encode("utf-8"), headers=headers or {}, method="PUT")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
# url = "https://httpbin.org/put"
# data = "Test PUT with headers"
# headers = {"User-Agent": "stdlib-sniper/1.0", "X-Test": "true"}
# result = http_put_with_headers(url, data, headers)
# print(result)
```

!!! note "Notes"
    - Useful for APIs requiring authentication or custom identification

<hr class="snippet-divider">

## Complex

###  HTTP PUT with JSON body

`http` `put` `json` `request` `web` `api`

HTTP PUT request with JSON body

```python
import urllib.request
import json

def http_put_json(url, json_data, headers=None):
    """HTTP PUT request with JSON body."""
    data = json.dumps(json_data).encode("utf-8")
    req_headers = {"Content-Type": "application/json"}
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, data=data, headers=req_headers, method="PUT")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
# url = "https://httpbin.org/put"
# data = {"foo": "bar"}
# result = http_put_json(url, data)
# print(result)
```

!!! note "Notes"
    - Sets `Content-Type: application/json`
    - Serializes data with `json.dumps`
    - Use for REST APIs and webhooks

<hr class="snippet-divider">

### HTTP PUT file upload (binary data)

`http` `put` `file` `upload` `binary` `request` `web`

HTTP PUT file upload (binary data)

```python
import urllib.request

def http_put_file(url, file_path, headers=None):
    """HTTP PUT request to upload a file as binary data."""
    with open(file_path, "rb") as f:
        data = f.read()
    req = urllib.request.Request(url, data=data, headers=headers or {}, method="PUT")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
# url = "https://httpbin.org/put"
# file_path = "example.txt"
# result = http_put_file(url, file_path)
# print(result)
```

!!! note "Notes"
    - Uploads file as raw binary data (not multipart)
    - For large files, consider chunked upload

<hr class="snippet-divider">

### HTTP PUT with error handling

`http` `put` `error` `handling` `request` `web`

HTTP PUT request with error handling

```python
import urllib.request
import urllib.error

def http_put_safe(url, data, headers=None):
    """HTTP PUT request with error handling."""
    try:
        req = urllib.request.Request(url, data=data.encode("utf-8"), headers=headers or {}, method="PUT")
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
# data = "test"
# result = http_put_safe(url, data)
# print(result)
```

!!! note "Notes"
    - Handles HTTP and URL errors
    - Returns None on failure

<hr class="snippet-divider">

## Edge Cases

###  Invalid URL, large file, unsupported method

`http` `put` `error` `edge-case` `file` `web`

Edge cases: invalid URL, large file, unsupported method

```python
def http_put_safe(url, data, headers=None):
    # Function is defined in one of the above code block
    pass


# Edge case: Invalid URL
try:
    http_put_safe("not-a-url", "data")
except Exception as e:
    print(f"Error: {e}")

# Edge case: Large file (may hit server or memory limits)
# Edge case: Unsupported method (server returns 405)
```

!!! note "Notes"
    - Invalid URLs raise URLError or ValueError
    - Large files may require chunked upload
    - Some servers do not support PUT (405 Method Not Allowed)

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 HTTP POST Request](./http_post.md)
- **Reference**: See [📂 Upload File](./upload_file.md)
- **Reference**: See [📂 HTTP Headers](./http_headers.md)

## 🏷️ Tags

`http`, `put`, `request`, `file`, `json`, `upload`, `headers`, `error`, `edge-case`, `web`, `binary`

## 📝 Notes

- PUT is idempotent (repeating the request has the same effect)
- For partial updates, use PATCH (not covered here)
- Always check server documentation for supported methods
- For async or chunked PUT, consider `asyncio` or third-party libraries
