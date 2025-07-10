# HTTP Session (Persistent Cookies & Headers)

Zero-dependency Python snippets for HTTP sessions (persistent cookies, headers) using the standard library.

## Simple

### 🧩 Simple HTTP session with cookies

```python
import urllib.request
import http.cookiejar

# Create a CookieJar to store cookies
cookie_jar = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(handler)

# Perform a GET request (cookies will be stored)
url = "https://httpbin.org/cookies/set?mycookie=value"
response = opener.open(url)
print(response.read().decode("utf-8"))

# Perform another request (cookies sent automatically)
url2 = "https://httpbin.org/cookies"
response2 = opener.open(url2)
print(response2.read().decode("utf-8"))
```

📂 Simple HTTP session with cookies

🏷️ Tags: http, session, cookies, get, opener, web
📝 Notes:
- Uses `http.cookiejar.CookieJar` for cookie persistence
- `opener` handles all requests with shared cookies

### 🧩 HTTP session with custom headers

```python
import urllib.request
import http.cookiejar

cookie_jar = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(handler)

url = "https://httpbin.org/headers"
headers = {"User-Agent": "stdlib-sniper/1.0", "X-Test": "session"}
req = urllib.request.Request(url, headers=headers)
response = opener.open(req)
print(response.read().decode("utf-8"))
```

📂 HTTP session with custom headers

🏷️ Tags: http, session, headers, cookies, opener, web
📝 Notes:
- Custom headers can be set per request
- Cookies persist across requests

## Complex

### 🧩 Simulate login and session persistence

```python
import urllib.request
import urllib.parse
import http.cookiejar

cookie_jar = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(handler)

# Simulate login (POST)
login_url = "https://httpbin.org/cookies/set/sessioncookie/123456"
login_data = {}  # No data needed for httpbin, but typically you'd send credentials
opener.open(login_url, data=urllib.parse.urlencode(login_data).encode("utf-8"))

# Access a page that requires the session cookie
protected_url = "https://httpbin.org/cookies"
response = opener.open(protected_url)
print(response.read().decode("utf-8"))
```

📂 Simulate login and session persistence

🏷️ Tags: http, session, login, cookies, post, opener, web
📝 Notes:
- In real scenarios, send credentials in `login_data`
- Session cookies persist for the opener's lifetime

### 🧩 Error handling and edge cases

```python
import urllib.request
import http.cookiejar

cookie_jar = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(handler)

try:
    url = "https://httpbin.org/status/403"
    response = opener.open(url)
    print(response.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    print(f"HTTP error: {e.code} {e.reason}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

📂 HTTP session error handling

🏷️ Tags: http, session, error, cookies, opener, web
📝 Notes:
- Always handle HTTPError and general exceptions
- Session persists even after errors unless reset

## Edge Cases

### 🧩 Session reset and manual cookie management

```python
import http.cookiejar

# Resetting session (new CookieJar)
cookie_jar = http.cookiejar.CookieJar()  # New session, no cookies

# Manual cookie manipulation
for cookie in cookie_jar:
    print(cookie.name, cookie.value)
# You can add/remove cookies manually if needed
```

📂 Session reset and manual cookie management

🏷️ Tags: http, session, cookies, manual, edge-case, web
📝 Notes:
- Creating a new CookieJar resets the session
- Manual cookie management is rarely needed but possible

## 🔗 Cross-References

- **Reference**: See [📂 HTTP GET Request](./http_get.md)
- **Reference**: See [📂 HTTP POST Request](./http_post.md)
- **Reference**: See [📂 HTTP Headers](./http_headers.md)

## 🏷️ Tags

`http`, `session`, `cookies`, `headers`, `login`, `opener`, `error`, `manual`, `edge-case`, `web`

## 📝 Notes

- Sessions are useful for login, authentication, and stateful APIs
- For advanced cookie handling, see `http.cookiejar` docs
- For thread safety, use a separate opener per thread
- For persistent cookies across runs, use `MozillaCookieJar` or `LWPCookieJar`
