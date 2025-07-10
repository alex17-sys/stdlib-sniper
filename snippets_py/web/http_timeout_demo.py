# 🧩 HTTP GET with timeout
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


# 🧩 HTTP POST with timeout
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


# 🧩 Custom timeout and edge cases
import urllib.request
import urllib.error

# Function is defined in one of the above code block (http_get_with_timeout)


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
