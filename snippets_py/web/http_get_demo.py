# 🧩 Simple HTTP GET request
import urllib.request


def http_get(url):
    """Perform a simple HTTP GET request and return the response as a string."""
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")


# Example usage
url = "https://httpbin.org/get"
result = http_get(url)
print(result)  # Prints the response body as a string


# 🧩 HTTP GET with custom headers
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


# 🧩 HTTP GET with error handling
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


# 🧩 HTTP GET streaming (binary data)
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


# 🧩 HTTP GET with timeout and redirect handling
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


# 🧩 HTTP GET with proxy support
import urllib.request


def http_get_with_proxy(url, proxy_url):
    """HTTP GET using an HTTP proxy."""
    proxy_handler = urllib.request.ProxyHandler({"http": proxy_url, "https": proxy_url})
    opener = urllib.request.build_opener(proxy_handler)
    with opener.open(url) as response:
        return response.read().decode("utf-8")


# Example usage
# proxy = "http://localhost:8080"
# url = "http://httpbin.org/get"
# result = http_get_with_proxy(url, proxy)
# print(result)


# 🧩 HTTP GET ignoring SSL certificate errors
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
