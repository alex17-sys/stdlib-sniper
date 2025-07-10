# 🧩 Simple HTTP PUT request (string data)
import urllib.request


def http_put(url, data):
    """Perform a simple HTTP PUT request with string data."""
    req = urllib.request.Request(url, data=data.encode("utf-8"), method="PUT")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


# Example usage
# url = "https://httpbin.org/put"
# data = "Hello, PUT!"
# result = http_put(url, data)
# print(result)


# 🧩 HTTP PUT with custom headers
import urllib.request


def http_put_with_headers(url, data, headers=None):
    """HTTP PUT request with custom headers."""
    req = urllib.request.Request(
        url, data=data.encode("utf-8"), headers=headers or {}, method="PUT"
    )
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


# Example usage
# url = "https://httpbin.org/put"
# data = "Test PUT with headers"
# headers = {"User-Agent": "stdlib-sniper/1.0", "X-Test": "true"}
# result = http_put_with_headers(url, data, headers)
# print(result)


# 🧩 HTTP PUT with JSON body
import urllib.request
import json


def http_put_json(url, json_data, headers=None):
    """HTTP PUT request with JSON body."""
    data = json.dumps(json_data).encode("utf-8")
    req_headers = {"Content-Type": "application/json"}
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, data=data, headers=req_headers, method="PUT")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


# Example usage
# url = "https://httpbin.org/put"
# data = {"foo": "bar"}
# result = http_put_json(url, data)
# print(result)


# 🧩 HTTP PUT file upload (binary data)
import urllib.request


def http_put_file(url, file_path, headers=None):
    """HTTP PUT request to upload a file as binary data."""
    with open(file_path, "rb") as f:
        data = f.read()
    req = urllib.request.Request(url, data=data, headers=headers or {}, method="PUT")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


# Example usage
# url = "https://httpbin.org/put"
# file_path = "example.txt"
# result = http_put_file(url, file_path)
# print(result)


# 🧩 HTTP PUT with error handling
import urllib.request
import urllib.error


def http_put_safe(url, data, headers=None):
    """HTTP PUT request with error handling."""
    try:
        req = urllib.request.Request(
            url, data=data.encode("utf-8"), headers=headers or {}, method="PUT"
        )
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
# data = "test"
# result = http_put_safe(url, data)
# print(result)


# 🧩 Invalid URL, large file, unsupported method
# Function is defined in one of the above code block (http_put_safe)


# Edge case: Invalid URL
try:
    http_put_safe("not-a-url", "data")
except Exception as e:
    print(f"Error: {e}")

# Edge case: Large file (may hit server or memory limits)
# Edge case: Unsupported method (server returns 405)
