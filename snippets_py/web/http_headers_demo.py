# 🧩 HTTP GET with custom headers
import urllib.request


def http_get_with_headers(url, headers=None):
    """HTTP GET request with custom headers."""
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


# Example usage
url = "https://httpbin.org/headers"
headers = {"User-Agent": "stdlib-sniper/1.0", "X-Test": "true"}
result = http_get_with_headers(url, headers)
print(result)


# 🧩 HTTP POST with custom headers
import urllib.request
import urllib.parse


def http_post_with_headers(url, data, headers=None):
    """HTTP POST request with custom headers."""
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


# 🧩 HTTP GET with Authorization header (Bearer token)
import urllib.request


def http_get_with_auth(url, token):
    """HTTP GET request with Bearer token authorization."""
    headers = {"Authorization": f"Bearer {token}"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


# Example usage
# url = "https://httpbin.org/bearer"
# token = "your_token_here"
# result = http_get_with_auth(url, token)
# print(result)


# 🧩 HTTP GET with custom User-Agent and Accept headers
import urllib.request


def http_get_with_user_agent(url, user_agent, accept=None):
    """HTTP GET with custom User-Agent and optional Accept header."""
    headers = {"User-Agent": user_agent}
    if accept:
        headers["Accept"] = accept
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


# Example usage
url = "https://httpbin.org/headers"
result = http_get_with_user_agent(url, "stdlib-sniper/2.0", accept="application/json")
print(result)


# 🧩 Case-insensitivity and invalid headers
import urllib.request


def http_get_case_insensitive(url, headers):
    """HTTP GET with headers (case-insensitive keys)."""
    # Python's urllib handles headers case-insensitively
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


# Example usage
url = "https://httpbin.org/headers"
headers = {"user-agent": "stdlib-sniper/3.0", "ACCEPT": "application/json"}
result = http_get_case_insensitive(url, headers)
print(result)

# Edge case: Invalid header (empty key)
try:
    bad_headers = {"": "value"}
    http_get_case_insensitive(url, bad_headers)
except Exception as e:
    print(f"Error: {e}")


# 🧩 Missing or None headers
# Function is defined in one of the above code block (http_get_with_headers)


# Edge case: None headers (should default to empty dict)
url = "https://httpbin.org/headers"
result = http_get_with_headers(url, None)
print(result)

# Edge case: Missing required header (e.g., Authorization)
try:
    url = "https://httpbin.org/bearer"
    result = http_get_with_headers(url, {})
    print(result)
except Exception as e:
    print(f"Error: {e}")
