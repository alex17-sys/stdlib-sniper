# HTTP GET Request

Zero-dependency Python snippets for making HTTP GET requests using the standard library.

## Simple

### 🧩 Simple HTTP GET request

```python
import urllib.request

def http_get(url):
    """Perform a simple HTTP GET request and return the response as a string."""
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")

# Example usage
url = "https://httpbin.org/get"
result = http_get(url)
print(result)  # Prints the response body as a string
```

📂 Simple HTTP GET request

🏷️ Tags: http, get, request, web, urllib, network
📝 Notes:
- Uses only the Python standard library (`urllib.request`)
- Handles basic GET requests
- Returns response as a string
- For binary data, see the streaming example below

### 🧩 HTTP GET with custom headers

```python
import urllib.request

def http_get_with_headers(url, headers=None):
    """Perform an HTTP GET request with custom headers."""
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
url = "https://httpbin.org/headers"
headers = {"User-Agent": "stdlib-sniper/1.0"}
result = http_get_with_headers(url, headers)
print(result)
```

📂 HTTP GET request with custom headers

🏷️ Tags: http, get, headers, request, web, urllib
📝 Notes:
- Allows setting custom headers (e.g., User-Agent, Authorization)
- Useful for APIs requiring authentication or custom identification

### 🧩 HTTP GET with error handling

```python
import urllib.request
import urllib.error

def http_get_safe(url):
    """Perform an HTTP GET request with error handling."""
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

# Example usage
url = "https://httpbin.org/status/404"
result = http_get_safe(url)
print(result)  # None, with error message printed
```

📂 HTTP GET request with error handling

🏷️ Tags: http, get, error, handling, request, web
📝 Notes:
- Catches HTTP and URL errors
- Prints error messages and returns None on failure
- Recommended for production code

### 🧩 HTTP GET streaming (binary data)

```python
import urllib.request

def http_get_binary(url, chunk_size=1024):
    """Download binary data from a URL in chunks (streaming)."""
    with urllib.request.urlopen(url) as response:
        while True:
            chunk = response.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Example usage: Download an image
url = "https://httpbin.org/image/png"
with open("output.png", "wb") as f:
    for chunk in http_get_binary(url):
        f.write(chunk)
```

📂 HTTP GET request for binary/streaming data

🏷️ Tags: http, get, binary, streaming, download, web
📝 Notes:
- Suitable for large files or binary data (images, PDFs, etc.)
- Reads data in chunks to avoid high memory usage
- Use in a `with open(..., 'wb')` block for file downloads

## Complex

### 🧩 HTTP GET with timeout and redirect handling

```python
import urllib.request
import urllib.error

def http_get_with_timeout(url, timeout=5):
    """HTTP GET with timeout and redirect handling."""
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

# Example usage
url = "https://httpbin.org/redirect/2"
result = http_get_with_timeout(url, timeout=2)
print(result)
```

📂 HTTP GET with timeout and redirect handling

🏷️ Tags: http, get, timeout, redirect, error, web
📝 Notes:
- Handles server redirects automatically (default urllib behavior)
- Timeout is in seconds; raises error if exceeded

### 🧩 HTTP GET with proxy support

```python
import urllib.request

def http_get_with_proxy(url, proxy_url):
    """HTTP GET using an HTTP proxy."""
    proxy_handler = urllib.request.ProxyHandler({'http': proxy_url, 'https': proxy_url})
    opener = urllib.request.build_opener(proxy_handler)
    with opener.open(url) as response:
        return response.read().decode("utf-8")

# Example usage
# proxy = "http://localhost:8080"
# url = "http://httpbin.org/get"
# result = http_get_with_proxy(url, proxy)
# print(result)
```

📂 HTTP GET with proxy support

🏷️ Tags: http, get, proxy, network, web
📝 Notes:
- Useful for environments behind a proxy or for debugging

### 🧩 HTTP GET ignoring SSL certificate errors

```python
import urllib.request
import ssl

def http_get_ignore_ssl(url):
    """HTTP GET ignoring SSL certificate errors (not recommended for production)."""
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=context) as response:
        return response.read().decode("utf-8")

# Example usage (for self-signed certs)
# url = "https://self-signed.badssl.com/"
# result = http_get_ignore_ssl(url)
# print(result)
```

📂 HTTP GET ignoring SSL certificate errors

🏷️ Tags: http, get, ssl, certificate, error, web
📝 Notes:
- Use only for testing or in trusted environments
- Disables SSL verification (security risk in production)

## 🔗 Cross-References

- **Reference**: See [📂 HTTP POST Request](./http_post.md)
- **Reference**: See [📂 Download File](./download_file.md)
- **Reference**: See [📂 URL Encode String](./url_encode.md)

## 🏷️ Tags

`http`, `get`, `request`, `web`, `urllib`, `network`, `headers`, `error`, `binary`, `streaming`

## 📝 Notes

- For HTTPS, works with valid SSL certificates by default
- For timeouts, pass `timeout=seconds` to `urlopen`
- For advanced authentication, see HTTP Basic Auth snippet
- For JSON APIs, use `json.loads(response.read().decode())`
- Always handle exceptions in production code
