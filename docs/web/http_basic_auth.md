---
title: HTTP Basic Authentication
description: Zero-dependency Python snippets for HTTP Basic Authentication using the standard library.
keywords: authentication, basic-auth, edge-case, error, get, headers, http, opener, password-mgr, post, web
---

# HTTP Basic Authentication

Zero-dependency Python snippets for HTTP Basic Authentication using the standard library.

5 snippets available in this sub-category.

---

## Simple

###  HTTP GET with Basic Auth

`http` `get` `basic-auth` `authentication` `headers` `web`

HTTP GET with Basic Auth

```python
import urllib.request
import base64

def http_get_basic_auth(url, username, password):
    """HTTP GET request with Basic Authentication."""
    credentials = f"{username}:{password}".encode("utf-8")
    encoded_credentials = base64.b64encode(credentials).decode("utf-8")
    headers = {"Authorization": f"Basic {encoded_credentials}"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
# url = "https://httpbin.org/basic-auth/user/pass"
# result = http_get_basic_auth(url, "user", "pass")
# print(result)
```

!!! note "Notes"
    - Encodes credentials as base64 per RFC 7617
    - Authorization header is required for Basic Auth

<hr class="snippet-divider">

### HTTP POST with Basic Auth

`http` `post` `basic-auth` `authentication` `headers` `web`

HTTP POST with Basic Auth

```python
import urllib.request
import urllib.parse
import base64

def http_post_basic_auth(url, data, username, password):
    """HTTP POST request with Basic Authentication."""
    credentials = f"{username}:{password}".encode("utf-8")
    encoded_credentials = base64.b64encode(credentials).decode("utf-8")
    headers = {"Authorization": f"Basic {encoded_credentials}"}
    encoded_data = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=encoded_data, headers=headers, method="POST")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
# url = "https://httpbin.org/basic-auth/user/pass"
# data = {"foo": "bar"}
# result = http_post_basic_auth(url, data, "user", "pass")
# print(result)
```

!!! note "Notes"
    - Works for endpoints requiring POST with authentication
    - Data is sent as form-encoded

<hr class="snippet-divider">

## Complex

###  HTTP GET with Basic Auth using HTTPPasswordMgr

`http` `get` `basic-auth` `password-mgr` `opener` `web`

HTTP GET with Basic Auth using HTTPPasswordMgr

```python
import urllib.request

# Set up a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
url = "https://httpbin.org/basic-auth/user/pass"
password_mgr.add_password(None, url, "user", "pass")

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)

response = opener.open(url)
print(response.read().decode("utf-8"))
```

!!! note "Notes"
    - Uses HTTPPasswordMgrWithDefaultRealm for credential management
    - Opener handles authentication automatically for multiple requests

<hr class="snippet-divider">

### Error handling and invalid credentials

`http` `get` `basic-auth` `error` `authentication` `web`

HTTP GET with Basic Auth and error handling

```python
import urllib.request
import base64
import urllib.error

def http_get_basic_auth_safe(url, username, password):
    """HTTP GET with Basic Auth and error handling."""
    credentials = f"{username}:{password}".encode("utf-8")
    encoded_credentials = base64.b64encode(credentials).decode("utf-8")
    headers = {"Authorization": f"Basic {encoded_credentials}"}
    req = urllib.request.Request(url, headers=headers)
    try:
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
# url = "https://httpbin.org/basic-auth/user/pass"
# result = http_get_basic_auth_safe(url, "user", "wrongpass")
# print(result)
```

!!! note "Notes"
    - Handles HTTP 401 Unauthorized and other errors
    - Returns None on failure

<hr class="snippet-divider">

## Edge Cases

###  Missing or malformed Authorization header

`http` `get` `basic-auth` `error` `edge-case` `authentication` `web`

Edge cases: missing or malformed Authorization header

```python
import urllib.request

def http_get_basic_auth(url, username, password):
    # Function is defined in one of the above code block
    pass


# Edge case: Missing Authorization header
try:
    req = urllib.request.Request("https://httpbin.org/basic-auth/user/pass")
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
except Exception as e:
    print(f"Error: {e}")

# Edge case: Malformed header (not base64)
try:
    req = urllib.request.Request("https://httpbin.org/basic-auth/user/pass", headers={"Authorization": "Basic notbase64!"})
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
except Exception as e:
    print(f"Error: {e}")
```

!!! note "Notes"
    - Missing or malformed headers result in HTTP 401 or 400 errors
    - Always encode credentials properly

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 HTTP GET Request](./http_get.md)
- **Reference**: See [📂 HTTP POST Request](./http_post.md)
- **Reference**: See [📂 HTTP Headers](./http_headers.md)

## 🏷️ Tags

`http`, `basic-auth`, `authentication`, `headers`, `get`, `post`, `error`, `edge-case`, `web`, `opener`, `password-mgr`

## 📝 Notes

- Never log or expose credentials in code or output
- For advanced authentication (Digest, OAuth), use other handlers or third-party libraries
- For persistent sessions, combine with cookie handling
- Always use HTTPS for transmitting credentials
