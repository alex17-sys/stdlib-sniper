---
title: HTTP GET Request
description: Zero-dependency Python snippets for making HTTP GET requests using the standard library.
keywords: binary, certificate, download, error, get, handling, headers, http, network, proxy, redirect, request, ssl, streaming, timeout, urllib, web
---

# HTTP GET Request

Zero-dependency Python snippets for making HTTP GET requests using the standard library.

7 snippets available in this sub-category.

---

## Simple

###  Simple HTTP GET request

`http` `get` `request` `web` `urllib` `network`

Simple HTTP GET request

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

!!! note "Notes"
    - Uses only the Python standard library (`urllib.request`)
    - Handles basic GET requests
    - Returns response as a string
    - For binary data, see the streaming example below

<hr class="snippet-divider">

### HTTP GET with custom headers

`http` `get` `headers` `request` `web` `urllib`

HTTP GET request with custom headers

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

!!! note "Notes"
    - Allows setting custom headers (e.g., User-Agent, Authorization)
    - Useful for APIs requiring authentication or custom identification

<hr class="snippet-divider">

### HTTP GET with error handling

`http` `get` `error` `handling` `request` `web`

HTTP GET request with error handling

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

!!! note "Notes"
    - Catches HTTP and URL errors
    - Prints error messages and returns None on failure
    - Recommended for production code

<hr class="snippet-divider">

### HTTP GET streaming (binary data)

`http` `get` `binary` `streaming` `download` `web`

HTTP GET request for binary/streaming data

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

!!! note "Notes"
    - Suitable for large files or binary data (images, PDFs, etc.)
    - Reads data in chunks to avoid high memory usage
    - Use in a `with open(..., 'wb')` block for file downloads

<hr class="snippet-divider">

## Complex

###  HTTP GET with timeout and redirect handling

`http` `get` `timeout` `redirect` `error` `web`

HTTP GET with timeout and redirect handling

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

!!! note "Notes"
    - Handles server redirects automatically (default urllib behavior)
    - Timeout is in seconds; raises error if exceeded

<hr class="snippet-divider">

### HTTP GET with proxy support

`http` `get` `proxy` `network` `web`

HTTP GET with proxy support

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

!!! note "Notes"
    - Useful for environments behind a proxy or for debugging

<hr class="snippet-divider">

### HTTP GET ignoring SSL certificate errors

`http` `get` `ssl` `certificate` `error` `web`

HTTP GET ignoring SSL certificate errors

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

!!! note "Notes"
    - Use only for testing or in trusted environments
    - Disables SSL verification (security risk in production)

<hr class="snippet-divider">

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
