# HTTP Redirects

Zero-dependency Python snippets for handling HTTP redirects using the standard library.

## Simple

### 🧩 Default redirect handling (automatic)

```python
import urllib.request

def http_get_follow_redirects(url):
    """HTTP GET request (follows redirects by default)."""
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")

# Example usage
# url = "http://httpbin.org/redirect/2"  # Redirects twice
# result = http_get_follow_redirects(url)
# print(result)
```

📂 HTTP GET with default redirect handling

🏷️ Tags: http, get, redirect, follow, web
📝 Notes:
- urllib follows up to 10 redirects by default
- Most requests handle redirects automatically

### 🧩 Disable redirects (block all)

```python
import urllib.request

class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def http_get_no_redirect(url):
    """HTTP GET request (does not follow redirects)."""
    opener = urllib.request.build_opener(NoRedirectHandler)
    try:
        with opener.open(url) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} {e.reason}")
        print(f"Redirect location: {e.headers.get('Location')}")
    return None

# Example usage
# url = "http://httpbin.org/redirect/1"
# result = http_get_no_redirect(url)
# print(result)
```

📂 HTTP GET with redirects disabled

🏷️ Tags: http, get, redirect, disable, handler, web
📝 Notes:
- Raises HTTPError for 3xx responses
- Useful for manual redirect handling

## Complex

### 🧩 Custom redirect handler (limit number of redirects)

```python
import urllib.request

class LimitedRedirectHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self, max_redirects=3):
        super().__init__()
        self.max_redirects = max_redirects
        self.redirect_count = 0
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.redirect_count += 1
        if self.redirect_count > self.max_redirects:
            raise urllib.error.HTTPError(newurl, code, "Too many redirects", headers, fp)
        return super().redirect_request(req, fp, code, msg, headers, newurl)

def http_get_limited_redirects(url, max_redirects=3):
    """HTTP GET with a custom limit on redirects."""
    handler = LimitedRedirectHandler(max_redirects)
    opener = urllib.request.build_opener(handler)
    try:
        with opener.open(url) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} {e.reason}")
    return None

# Example usage
# url = "http://httpbin.org/redirect/5"
# result = http_get_limited_redirects(url, max_redirects=2)
# print(result)
```

📂 HTTP GET with limited redirects

🏷️ Tags: http, get, redirect, limit, handler, web
📝 Notes:
- Raises HTTPError if redirect limit is exceeded
- Customizable for different use cases

### 🧩 Capture redirect chain (history)

```python
import urllib.request

class CaptureRedirectHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self):
        super().__init__()
        self.redirects = []
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.redirects.append((code, newurl))
        return super().redirect_request(req, fp, code, msg, headers, newurl)

def http_get_with_redirect_history(url):
    """HTTP GET and capture the full redirect chain."""
    handler = CaptureRedirectHandler()
    opener = urllib.request.build_opener(handler)
    with opener.open(url) as response:
        body = response.read().decode("utf-8")
    return handler.redirects, body

# Example usage
# url = "http://httpbin.org/redirect/3"
# redirects, result = http_get_with_redirect_history(url)
# print("Redirect chain:", redirects)
# print(result)
```

📂 HTTP GET with redirect chain capture

🏷️ Tags: http, get, redirect, history, handler, web
📝 Notes:
- Stores (code, newurl) for each redirect
- Useful for debugging and analytics

### 🧩 POST/PUT/DELETE with redirects

```python
import urllib.request

def http_post_follow_redirect(url, data):
    """HTTP POST that follows redirects (default behavior)."""
    req = urllib.request.Request(url, data=data.encode("utf-8"), method="POST")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
# url = "http://httpbin.org/redirect-to?url=/post"
# result = http_post_follow_redirect(url, "test")
# print(result)
```

📂 HTTP POST with redirect following

🏷️ Tags: http, post, redirect, follow, web
📝 Notes:
- urllib will change POST to GET on 302/303 by default (per RFC)
- For strict POST/PUT/DELETE, use custom handlers

## Edge Cases

### 🧩 Redirect loop and too many redirects

```python
import urllib.request

# Edge case: Redirect loop
try:
    url = "http://httpbin.org/absolute-redirect/20"  # 20 redirects
    with urllib.request.urlopen(url) as response:
        print(response.read().decode("utf-8"))
except Exception as e:
    print(f"Error: {e}")

# Edge case: Manual detection with custom handler (see above)
```

📂 Edge cases: redirect loop and too many redirects

🏷️ Tags: http, get, redirect, loop, error, edge-case, web
📝 Notes:
- urllib raises HTTPError for too many redirects (default 10)
- Custom handlers can set stricter or looser limits

## 🔗 Cross-References

- **Reference**: See [📂 HTTP GET Request](./http_get.md)
- **Reference**: See [📂 HTTP POST Request](./http_post.md)
- **Reference**: See [📂 HTTP Headers](./http_headers.md)
- **Reference**: See [📂 HTTP Status Code](./http_status_code.md)

## 🏷️ Tags

`http`, `redirect`, `handler`, `limit`, `history`, `error`, `edge-case`, `web`, `post`, `get`

## 📝 Notes

- Most HTTP libraries follow redirects by default
- For security, always validate final destination URL
- For advanced redirect logic, use custom handlers
- For async or batch requests, consider `asyncio` or third-party libraries
