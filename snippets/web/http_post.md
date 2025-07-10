# HTTP POST Request

Zero-dependency Python snippets for making HTTP POST requests using the standard library.

## Simple

### 🧩 Simple HTTP POST request (form data)

```python
import urllib.request
import urllib.parse

def http_post(url, data):
    """Perform a simple HTTP POST request with form data."""
    encoded_data = urllib.parse.urlencode(data).encode("utf-8")
    with urllib.request.urlopen(url, data=encoded_data) as response:
        return response.read().decode("utf-8")

# Example usage
url = "https://httpbin.org/post"
data = {"name": "stdlib-sniper", "type": "example"}
result = http_post(url, data)
print(result)
```

📂 Simple HTTP POST request with form data

🏷️ Tags: http, post, request, web, urllib, form
📝 Notes:
- Uses `urllib.request` and `urllib.parse` from the standard library
- Data must be a dictionary (form fields)
- Encodes data as `application/x-www-form-urlencoded`

### 🧩 HTTP POST with custom headers

```python
import urllib.request
import urllib.parse

def http_post_with_headers(url, data, headers=None):
    """HTTP POST with custom headers."""
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
- Allows setting custom headers (e.g., User-Agent, Content-Type)
- Useful for APIs requiring authentication or custom identification

### 🧩 HTTP POST with JSON body

```python
import urllib.request
import json

def http_post_json(url, json_data, headers=None):
    """HTTP POST with JSON body."""
    data = json.dumps(json_data).encode("utf-8")
    req_headers = {"Content-Type": "application/json"}
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, data=data, headers=req_headers, method="POST")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
url = "https://httpbin.org/post"
data = {"foo": "bar"}
result = http_post_json(url, data)
print(result)
```

📂 HTTP POST request with JSON body

🏷️ Tags: http, post, json, request, web, api
📝 Notes:
- Sets `Content-Type: application/json`
- Serializes data with `json.dumps`
- Use for REST APIs and webhooks

### 🧩 HTTP POST with error handling

```python
import urllib.request
import urllib.parse
import urllib.error

def http_post_safe(url, data):
    """HTTP POST with error handling."""
    try:
        encoded_data = urllib.parse.urlencode(data).encode("utf-8")
        with urllib.request.urlopen(url, data=encoded_data) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

# Example usage
url = "https://httpbin.org/status/400"
data = {"fail": True}
result = http_post_safe(url, data)
print(result)  # None, with error message printed
```

📂 HTTP POST request with error handling

🏷️ Tags: http, post, error, handling, request, web
📝 Notes:
- Catches HTTP and URL errors
- Prints error messages and returns None on failure
- Recommended for production code

## Complex

### 🧩 HTTP POST file upload (multipart/form-data)

```python
import urllib.request
import mimetypes
import uuid

def http_post_file(url, file_path, field_name="file"):
    """HTTP POST file upload using multipart/form-data."""
    boundary = uuid.uuid4().hex
    content_type = f"multipart/form-data; boundary={boundary}"
    with open(file_path, "rb") as f:
        file_content = f.read()
    filename = file_path.split("/")[-1]
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"\r\n'
        f"Content-Type: {mimetypes.guess_type(filename)[0] or 'application/octet-stream'}\r\n\r\n"
    ).encode() + file_content + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", content_type)
    req.add_header("Content-Length", str(len(body)))
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
# url = "https://httpbin.org/post"
# file_path = "example.txt"
# result = http_post_file(url, file_path)
# print(result)
```

📂 HTTP POST file upload (multipart/form-data)

🏷️ Tags: http, post, file, upload, multipart, web
📝 Notes:
- Manually constructs multipart/form-data body
- Handles binary file uploads
- For multiple files/fields, extend the body construction

### 🧩 HTTP POST with timeout and proxy

```python
import urllib.request
import urllib.parse

def http_post_with_timeout_proxy(url, data, timeout=5, proxy_url=None):
    """HTTP POST with timeout and optional proxy."""
    encoded_data = urllib.parse.urlencode(data).encode("utf-8")
    if proxy_url:
        proxy_handler = urllib.request.ProxyHandler({'http': proxy_url, 'https': proxy_url})
        opener = urllib.request.build_opener(proxy_handler)
        with opener.open(url, data=encoded_data, timeout=timeout) as response:
            return response.read().decode("utf-8")
    else:
        with urllib.request.urlopen(url, data=encoded_data, timeout=timeout) as response:
            return response.read().decode("utf-8")

# Example usage
# url = "https://httpbin.org/post"
# data = {"test": 123}
# proxy = "http://localhost:8080"
# result = http_post_with_timeout_proxy(url, data, timeout=3, proxy_url=proxy)
# print(result)
```

📂 HTTP POST with timeout and proxy

🏷️ Tags: http, post, timeout, proxy, request, web
📝 Notes:
- Supports both direct and proxied requests
- Timeout is in seconds

## 🔗 Cross-References

- **Reference**: See [📂 HTTP GET Request](./http_get.md)
- **Reference**: See [📂 Download File](./download_file.md)
- **Reference**: See [📂 URL Encode String](./url_encode.md)

## 🏷️ Tags

`http`, `post`, `request`, `web`, `urllib`, `form`, `json`, `file`, `upload`, `timeout`, `proxy`, `error`, `headers`, `api`

## 📝 Notes

- For HTTPS, works with valid SSL certificates by default
- For advanced authentication, see HTTP Basic Auth snippet
- Always handle exceptions in production code
- For large file uploads, consider streaming or chunked uploads
