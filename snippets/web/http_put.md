# HTTP PUT Request

Zero-dependency Python snippets for making HTTP PUT requests using the standard library.

## Simple

### 🧩 Simple HTTP PUT request (string data)

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

📂 Simple HTTP PUT request (string data)

🏷️ Tags: http, put, request, web, string, urllib
📝 Notes:
- Data must be bytes (encode string to utf-8)
- PUT is used for updating/replacing resources

### 🧩 HTTP PUT with custom headers

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

📂 HTTP PUT request with custom headers

🏷️ Tags: http, put, headers, request, web, urllib
📝 Notes:
- Useful for APIs requiring authentication or custom identification

## Complex

### 🧩 HTTP PUT with JSON body

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

📂 HTTP PUT request with JSON body

🏷️ Tags: http, put, json, request, web, api
📝 Notes:
- Sets `Content-Type: application/json`
- Serializes data with `json.dumps`
- Use for REST APIs and webhooks

### 🧩 HTTP PUT file upload (binary data)

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

📂 HTTP PUT file upload (binary data)

🏷️ Tags: http, put, file, upload, binary, request, web
📝 Notes:
- Uploads file as raw binary data (not multipart)
- For large files, consider chunked upload

### 🧩 HTTP PUT with error handling

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

📂 HTTP PUT request with error handling

🏷️ Tags: http, put, error, handling, request, web
📝 Notes:
- Handles HTTP and URL errors
- Returns None on failure

## Edge Cases

### 🧩 Invalid URL, large file, unsupported method

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

📂 Edge cases: invalid URL, large file, unsupported method

🏷️ Tags: http, put, error, edge-case, file, web
📝 Notes:
- Invalid URLs raise URLError or ValueError
- Large files may require chunked upload
- Some servers do not support PUT (405 Method Not Allowed)

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
