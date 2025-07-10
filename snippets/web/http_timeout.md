# HTTP Request Timeout

Zero-dependency Python snippets for using timeouts in HTTP requests with the standard library.

## Simple

### 🧩 HTTP GET with timeout

```python
import urllib.request
import urllib.error

def http_get_with_timeout(url, timeout=5):
    """HTTP GET request with a timeout (in seconds)."""
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            return response.read().decode("utf-8")
    except urllib.error.URLError as e:
        print(f"Timeout or URL error: {e.reason}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

# Example usage
url = "https://httpbin.org/delay/2"  # Delays response by 2 seconds
result = http_get_with_timeout(url, timeout=1)
print(result)  # None, with timeout error printed
```

📂 HTTP GET request with timeout

🏷️ Tags: http, get, timeout, request, web, urllib
📝 Notes:
- Timeout is in seconds (float or int)
- Raises URLError if the server does not respond in time
- Always handle exceptions for production code

### 🧩 HTTP POST with timeout

```python
import urllib.request
import urllib.parse
import urllib.error

def http_post_with_timeout(url, data, timeout=5):
    """HTTP POST request with a timeout (in seconds)."""
    try:
        encoded_data = urllib.parse.urlencode(data).encode("utf-8")
        with urllib.request.urlopen(url, data=encoded_data, timeout=timeout) as response:
            return response.read().decode("utf-8")
    except urllib.error.URLError as e:
        print(f"Timeout or URL error: {e.reason}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

# Example usage
url = "https://httpbin.org/delay/3"
data = {"test": 123}
result = http_post_with_timeout(url, data, timeout=1)
print(result)  # None, with timeout error printed
```

📂 HTTP POST request with timeout

🏷️ Tags: http, post, timeout, request, web, urllib
📝 Notes:
- Timeout applies to the entire request (connect + read)
- Use try/except to handle timeouts gracefully

## Complex

### 🧩 Custom timeout and edge cases

```python
import urllib.request
import urllib.error

def http_get_with_timeout(url, timeout=5):
    # Function is defined in one of the above code block
    pass


def http_get_with_short_timeout(url):
    """HTTP GET with a very short timeout (edge case)."""
    try:
        with urllib.request.urlopen(url, timeout=0.001) as response:
            return response.read().decode("utf-8")
    except urllib.error.URLError as e:
        print(f"Likely timeout: {e.reason}")
    return None

# Example usage
url = "https://httpbin.org/get"
result = http_get_with_short_timeout(url)
print(result)  # None, with likely timeout error

# Edge case: Unreachable server
url = "http://10.255.255.1"  # Non-routable IP
result = http_get_with_timeout(url, timeout=2)
print(result)  # None, with timeout or unreachable error
```

📂 HTTP GET with custom/short timeout and unreachable server

🏷️ Tags: http, get, timeout, edge-case, error, web
📝 Notes:
- Very short timeouts almost always fail
- Unreachable servers raise URLError (timeout or connection refused)

## 🔗 Cross-References

- **Reference**: See [📂 HTTP GET Request](./http_get.md)
- **Reference**: See [📂 HTTP POST Request](./http_post.md)
- **Reference**: See [📂 HTTP Headers](./http_headers.md)

## 🏷️ Tags

`http`, `timeout`, `get`, `post`, `request`, `web`, `error`, `edge-case`, `urllib`

## 📝 Notes

- Timeout is not a guarantee; network conditions may vary
- For more granular control, use `socket.setdefaulttimeout()` (affects all requests)
- Always test timeouts in your deployment environment
- For async or non-blocking requests, consider `asyncio` or third-party libraries
