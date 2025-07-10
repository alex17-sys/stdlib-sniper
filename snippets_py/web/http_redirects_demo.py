# 🧩 Default redirect handling (automatic)
import urllib.request


def http_get_follow_redirects(url):
    """HTTP GET request (follows redirects by default)."""
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")


# Example usage
# url = "http://httpbin.org/redirect/2"  # Redirects twice
# result = http_get_follow_redirects(url)
# print(result)


# 🧩 Disable redirects (block all)
import urllib.request


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def http_get_no_redirect(url):
    """HTTP GET request (does not follow redirects)."""
    opener = urllib.request.build_opener(NoRedirectHandler)
    try:
        with opener.open(url) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} {e.reason}")
        print(f"Redirect location: {e.headers.get('Location')}")
    return None


# Example usage
# url = "http://httpbin.org/redirect/1"
# result = http_get_no_redirect(url)
# print(result)


# 🧩 Custom redirect handler (limit number of redirects)
import urllib.request


class LimitedRedirectHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self, max_redirects=3):
        super().__init__()
        self.max_redirects = max_redirects
        self.redirect_count = 0

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.redirect_count += 1
        if self.redirect_count > self.max_redirects:
            raise urllib.error.HTTPError(newurl, code, "Too many redirects", headers, fp)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def http_get_limited_redirects(url, max_redirects=3):
    """HTTP GET with a custom limit on redirects."""
    handler = LimitedRedirectHandler(max_redirects)
    opener = urllib.request.build_opener(handler)
    try:
        with opener.open(url) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} {e.reason}")
    return None


# Example usage
# url = "http://httpbin.org/redirect/5"
# result = http_get_limited_redirects(url, max_redirects=2)
# print(result)


# 🧩 Capture redirect chain (history)
import urllib.request


class CaptureRedirectHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self):
        super().__init__()
        self.redirects = []

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.redirects.append((code, newurl))
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def http_get_with_redirect_history(url):
    """HTTP GET and capture the full redirect chain."""
    handler = CaptureRedirectHandler()
    opener = urllib.request.build_opener(handler)
    with opener.open(url) as response:
        body = response.read().decode("utf-8")
    return handler.redirects, body


# Example usage
# url = "http://httpbin.org/redirect/3"
# redirects, result = http_get_with_redirect_history(url)
# print("Redirect chain:", redirects)
# print(result)


# 🧩 POST/PUT/DELETE with redirects
import urllib.request


def http_post_follow_redirect(url, data):
    """HTTP POST that follows redirects (default behavior)."""
    req = urllib.request.Request(url, data=data.encode("utf-8"), method="POST")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


# Example usage
# url = "http://httpbin.org/redirect-to?url=/post"
# result = http_post_follow_redirect(url, "test")
# print(result)


# 🧩 Redirect loop and too many redirects
import urllib.request

# Edge case: Redirect loop
try:
    url = "http://httpbin.org/absolute-redirect/20"  # 20 redirects
    with urllib.request.urlopen(url) as response:
        print(response.read().decode("utf-8"))
except Exception as e:
    print(f"Error: {e}")

# Edge case: Manual detection with custom handler (see above)
