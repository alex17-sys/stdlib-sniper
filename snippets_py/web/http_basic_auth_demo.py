# 🧩 HTTP GET with Basic Auth
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


# 🧩 HTTP POST with Basic Auth
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


# 🧩 HTTP GET with Basic Auth using HTTPPasswordMgr
import urllib.request

# Set up a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
url = "https://httpbin.org/basic-auth/user/pass"
password_mgr.add_password(None, url, "user", "pass")

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)

response = opener.open(url)
print(response.read().decode("utf-8"))


# 🧩 Error handling and invalid credentials
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


# 🧩 Missing or malformed Authorization header
import urllib.request

# Function is defined in one of the above code block (http_get_basic_auth)


# Edge case: Missing Authorization header
try:
    req = urllib.request.Request("https://httpbin.org/basic-auth/user/pass")
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
except Exception as e:
    print(f"Error: {e}")

# Edge case: Malformed header (not base64)
try:
    req = urllib.request.Request(
        "https://httpbin.org/basic-auth/user/pass", headers={"Authorization": "Basic notbase64!"}
    )
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
except Exception as e:
    print(f"Error: {e}")
