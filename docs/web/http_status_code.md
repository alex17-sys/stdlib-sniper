---
title: HTTP Status Code Handling
description: Zero-dependency Python snippets for handling HTTP status codes using the standard library.
keywords: auth, code, edge-case, error, get, http, mapping, message, response, server, status, success, web
---

# HTTP Status Code Handling

Zero-dependency Python snippets for handling HTTP status codes using the standard library.

6 snippets available in this sub-category.

---

## Simple

###  Get status code from response

`http` `status` `code` `get` `response` `web`

Get HTTP status code from response

```python
import urllib.request

def get_status_code(url):
    """Perform a GET request and return the HTTP status code."""
    with urllib.request.urlopen(url) as response:
        return response.status

# Example usage
# url = "https://httpbin.org/status/200"
# code = get_status_code(url)
# print(code)  # 200
```

!!! note "Notes"
    - `response.status` gives the HTTP status code (int)
    - Works for all successful requests

<hr class="snippet-divider">

### Handle specific status codes (success, redirect, error)

`http` `status` `code` `error` `response` `web`

Handle specific HTTP status codes

```python
import urllib.request
import urllib.error

def handle_status_code(url):
    """GET request and handle specific status codes."""
    try:
        with urllib.request.urlopen(url) as response:
            code = response.status
            if code == 200:
                print("Success!")
            elif code == 301:
                print("Redirected!")
            elif code == 404:
                print("Not found!")
            else:
                print(f"Status code: {code}")
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} {e.reason}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
# url = "https://httpbin.org/status/404"
# handle_status_code(url)
```

!!! note "Notes"
    - Handles 200, 301, 404, and others
    - HTTPError is raised for 4xx/5xx codes

<hr class="snippet-divider">

## Complex

###  Custom error handling for 401, 403, 500

`http` `status` `code` `error` `auth` `server` `web`

Custom error handling for 401, 403, 500

```python
import urllib.request
import urllib.error

def handle_auth_and_server_errors(url):
    """GET request and handle 401, 403, 500 errors."""
    try:
        with urllib.request.urlopen(url) as response:
            print(f"Status: {response.status}")
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print("Unauthorized (401): Check credentials.")
        elif e.code == 403:
            print("Forbidden (403): Access denied.")
        elif e.code == 500:
            print("Server error (500): Try again later.")
        else:
            print(f"HTTP error: {e.code} {e.reason}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
# url = "https://httpbin.org/status/401"
# handle_auth_and_server_errors(url)
```

!!! note "Notes"
    - Handles authentication and server errors
    - Prints user-friendly messages

<hr class="snippet-divider">

### Map status codes to messages

`http` `status` `code` `message` `mapping` `web`

Map HTTP status codes to messages

```python
import http

def status_code_message(code):
    """Map HTTP status code to standard message."""
    try:
        return http.HTTPStatus(code).phrase
    except ValueError:
        return "Unknown status code"

# Example usage
# print(status_code_message(200))  # OK
# print(status_code_message(404))  # Not Found
# print(status_code_message(418))  # I'm a teapot
# print(status_code_message(999))  # Unknown status code
```

!!! note "Notes"
    - Uses `http.HTTPStatus` (Python 3.5+)
    - Handles standard and non-standard codes

<hr class="snippet-divider">

### Check for success/failure

`http` `status` `code` `success` `error` `web`

Check for successful HTTP status codes

```python
import urllib.request
import urllib.error

def is_successful(url):
    """Return True if GET request is successful (2xx), else False."""
    try:
        with urllib.request.urlopen(url) as response:
            return 200 <= response.status < 300
    except urllib.error.HTTPError:
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

# Example usage
# url = "https://httpbin.org/status/204"
# print(is_successful(url))  # True
# url = "https://httpbin.org/status/404"
# print(is_successful(url))  # False
```

!!! note "Notes"
    - 2xx codes are considered successful
    - Returns False for HTTPError or exceptions

<hr class="snippet-divider">

## Edge Cases

###  Non-standard codes and missing status

`http` `status` `code` `edge-case` `error` `web`

Edge cases: non-standard codes and missing status

```python
import urllib.request
import urllib.error

def get_status_code_safe(url):
    """GET request, handle missing or non-standard status codes."""
    try:
        with urllib.request.urlopen(url) as response:
            return response.status
    except urllib.error.HTTPError as e:
        return e.code  # HTTPError has .code attribute
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Example usage
# url = "https://httpbin.org/status/418"  # I'm a teapot
# print(get_status_code_safe(url))  # 418
# url = "not-a-url"
# print(get_status_code_safe(url))  # None
```

!!! note "Notes"
    - HTTPError exposes .code for error responses
    - Non-standard codes may not have a standard message

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 HTTP GET Request](./http_get.md)
- **Reference**: See [📂 HTTP POST Request](./http_post.md)
- **Reference**: See [📂 HTTP Redirects](./http_redirects.md)

## 🏷️ Tags

`http`, `status`, `code`, `error`, `success`, `mapping`, `edge-case`, `web`, `response`

## 📝 Notes

- Always check status codes for robust error handling
- For custom APIs, document non-standard codes
- For async or batch requests, consider `asyncio` or third-party libraries
