---
title: HTTP Session (Persistent Cookies & Headers)
description: Zero-dependency Python snippets for HTTP sessions (persistent cookies, headers) using the standard library.
keywords: cookies, edge-case, error, get, headers, http, login, manual, opener, post, session, web
---

# HTTP Session (Persistent Cookies & Headers)

Zero-dependency Python snippets for HTTP sessions (persistent cookies, headers) using the standard library.

5 snippets available in this sub-category.

---

## Simple

###  Simple HTTP session with cookies

`http` `session` `cookies` `get` `opener` `web`

Simple HTTP session with cookies

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

!!! note "Notes"
    - Uses `http.cookiejar.CookieJar` for cookie persistence
    - `opener` handles all requests with shared cookies

<hr class="snippet-divider">

### HTTP session with custom headers

`http` `session` `headers` `cookies` `opener` `web`

HTTP session with custom headers

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

!!! note "Notes"
    - Custom headers can be set per request
    - Cookies persist across requests

<hr class="snippet-divider">

## Complex

###  Simulate login and session persistence

`http` `session` `login` `cookies` `post` `opener` `web`

Simulate login and session persistence

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

!!! note "Notes"
    - In real scenarios, send credentials in `login_data`
    - Session cookies persist for the opener's lifetime

<hr class="snippet-divider">

### Error handling and edge cases

`http` `session` `error` `cookies` `opener` `web`

HTTP session error handling

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

!!! note "Notes"
    - Always handle HTTPError and general exceptions
    - Session persists even after errors unless reset

<hr class="snippet-divider">

## Edge Cases

###  Session reset and manual cookie management

`http` `session` `cookies` `manual` `edge-case` `web`

Session reset and manual cookie management

```python
import http.cookiejar

# Resetting session (new CookieJar)
cookie_jar = http.cookiejar.CookieJar()  # New session, no cookies

# Manual cookie manipulation
for cookie in cookie_jar:
    print(cookie.name, cookie.value)
# You can add/remove cookies manually if needed
```

!!! note "Notes"
    - Creating a new CookieJar resets the session
    - Manual cookie management is rarely needed but possible

<hr class="snippet-divider">

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
