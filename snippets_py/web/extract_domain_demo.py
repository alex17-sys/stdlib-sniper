# 🧩 Extract netloc (host:port) from URL
from urllib.parse import urlparse

url = "https://sub.example.com:8080/path?query=1"
parsed = urlparse(url)
print(parsed.netloc)  # sub.example.com:8080


# 🧩 Extract host (domain) only (without port)
from urllib.parse import urlparse

url = "https://sub.example.com:8080/path"
parsed = urlparse(url)
host = parsed.hostname
print(host)  # sub.example.com


# 🧩 Extract port from URL
from urllib.parse import urlparse

url = "https://example.com:8443/path"
parsed = urlparse(url)
port = parsed.port
print(port)  # 8443


# 🧩 Extract registered domain (TLD split, basic)
from urllib.parse import urlparse


def get_registered_domain(url):
    """Extract the registered domain (e.g., example.com) from a URL."""
    host = urlparse(url).hostname or ""
    parts = host.split(".")
    if len(parts) >= 2:
        return ".".join(parts[-2:])
    return host


# Example usage
print(get_registered_domain("https://sub.example.co.uk"))  # co.uk (basic, not public suffix aware)
print(get_registered_domain("https://sub.example.com"))  # example.com


# 🧩 Extract domain from IPv6 URL
from urllib.parse import urlparse

url = "http://[2001:db8::1]:8080/index.html"
parsed = urlparse(url)
print(parsed.hostname)  # 2001:db8::1
print(parsed.netloc)  # [2001:db8::1]:8080


# 🧩 Extract from URL with missing netloc or malformed URL
from urllib.parse import urlparse

url = "not-a-url"
parsed = urlparse(url)
print(parsed.netloc)  # ''
print(parsed.hostname)  # None
