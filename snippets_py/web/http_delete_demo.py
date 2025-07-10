# 🧩 Simple HTTP DELETE request
import urllib.request


def http_delete(url):
    """Perform a simple HTTP DELETE request."""
    req = urllib.request.Request(url, method="DELETE")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


# Example usage
# url = "https://httpbin.org/delete"
# result = http_delete(url)
# print(result)


# 🧩 HTTP DELETE with custom headers
import urllib.request


def http_delete_with_headers(url, headers=None):
    """HTTP DELETE request with custom headers."""
    req = urllib.request.Request(url, headers=headers or {}, method="DELETE")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


# Example usage
# url = "https://httpbin.org/delete"
# headers = {"User-Agent": "stdlib-sniper/1.0", "X-Test": "true"}
# result = http_delete_with_headers(url, headers)
# print(result)


# 🧩 HTTP DELETE with query parameters
import urllib.request
import urllib.parse


def http_delete_with_params(url, params):
    """HTTP DELETE request with query parameters."""
    query = urllib.parse.urlencode(params)
    full_url = f"{url}?{query}" if params else url
    req = urllib.request.Request(full_url, method="DELETE")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


# Example usage
# url = "https://httpbin.org/delete"
# params = {"id": 123, "force": "yes"}
# result = http_delete_with_params(url, params)
# print(result)


# 🧩 HTTP DELETE with authentication (Basic Auth)
import urllib.request
import base64


def http_delete_basic_auth(url, username, password):
    """HTTP DELETE request with Basic Authentication."""
    credentials = f"{username}:{password}".encode("utf-8")
    encoded_credentials = base64.b64encode(credentials).decode("utf-8")
    headers = {"Authorization": f"Basic {encoded_credentials}"}
    req = urllib.request.Request(url, headers=headers, method="DELETE")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


# Example usage
# url = "https://httpbin.org/delete"
# result = http_delete_basic_auth(url, "user", "pass")
# print(result)


# 🧩 HTTP DELETE with error handling
import urllib.request
import urllib.error


def http_delete_safe(url, headers=None):
    """HTTP DELETE request with error handling."""
    try:
        req = urllib.request.Request(url, headers=headers or {}, method="DELETE")
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
# result = http_delete_safe(url)
# print(result)


# 🧩 Invalid URL, unsupported method, missing authentication
# Function is defined in one of the above code block (http_delete_safe)


# Edge case: Invalid URL
try:
    http_delete_safe("not-a-url")
except Exception as e:
    print(f"Error: {e}")

# Edge case: Unsupported method (server returns 405)
# Edge case: Missing authentication (server returns 401/403)
