# 🧩 Build URL from components
from urllib.parse import urlunparse


def build_url(scheme, netloc, path, params="", query="", fragment=""):
    """Build a URL from its components."""
    return urlunparse((scheme, netloc, path, params, query, fragment))


# Example usage
url = build_url("https", "example.com", "/search", "", "q=python", "section")
print(url)  # https://example.com/search?q=python#section


# 🧩 Add or replace query parameters in URL
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


def add_query_params(url, params):
    """Add or replace query parameters in a URL."""
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    query.update(params)
    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))


# Example usage
url = "https://example.com/search?q=python"
new_url = add_query_params(url, {"lang": "en", "q": "ai"})
print(new_url)  # https://example.com/search?q=ai&lang=en


# 🧩 Join base and relative URLs
from urllib.parse import urljoin

base = "https://example.com/docs/"
relative = "../about/contact.html"
full_url = urljoin(base, relative)
print(full_url)  # https://example.com/about/contact.html


# 🧩 Build URL with user, password, and port
from urllib.parse import urlunparse


def build_url_with_auth(scheme, user, password, host, port, path):
    """Build a URL with user, password, and port."""
    netloc = f"{user}:{password}@{host}:{port}" if user and password else f"{host}:{port}"
    return urlunparse((scheme, netloc, path, "", "", ""))


# Example usage
url = build_url_with_auth("ftp", "user", "pass", "ftp.example.com", 2121, "/files")
print(url)  # ftp://user:pass@ftp.example.com:2121/files


# 🧩 Build URL with fragment and params
from urllib.parse import urlunparse

url = urlunparse(("https", "example.com", "/page", "", "", "section2"))
print(url)  # https://example.com/page#section2

url2 = urlunparse(("http", "example.com", "/api", "action", "", ""))
print(url2)  # http://example.com/api;action


# 🧩 Build URL with missing parts and double slashes
from urllib.parse import urlunparse

# Missing netloc (relative URL)
url = urlunparse(("https", "", "/about", "", "", ""))
print(url)  # https:///about

# Double slashes in path
url2 = urlunparse(("https", "example.com", "//double/slash", "", "", ""))
print(url2)  # https://example.com//double/slash
