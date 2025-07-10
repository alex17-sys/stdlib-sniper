# 🧩 Get status code from response
import urllib.request


def get_status_code(url):
    """Perform a GET request and return the HTTP status code."""
    with urllib.request.urlopen(url) as response:
        return response.status


# Example usage
# url = "https://httpbin.org/status/200"
# code = get_status_code(url)
# print(code)  # 200


# 🧩 Handle specific status codes (success, redirect, error)
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


# 🧩 Custom error handling for 401, 403, 500
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


# 🧩 Map status codes to messages
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


# 🧩 Check for success/failure
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


# 🧩 Non-standard codes and missing status
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
