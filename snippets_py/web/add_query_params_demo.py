# 🧩 Add new query parameters to URL
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


def add_query_params(url, params):
    """Add new query parameters to a URL."""
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    query.update(params)
    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))


# Example usage
url = "https://example.com/search?q=python"
new_url = add_query_params(url, {"lang": "en", "page": 2})
print(new_url)  # https://example.com/search?q=python&lang=en&page=2


# 🧩 Replace existing query parameters
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


def replace_query_param(url, key, value):
    """Replace a single query parameter in a URL."""
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    query[key] = [value]
    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))


# Example usage
url = "https://example.com/search?q=python&lang=en"
new_url = replace_query_param(url, "q", "ai")
print(new_url)  # https://example.com/search?q=ai&lang=en


# 🧩 Add multiple values for a single key
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


def add_multi_value_param(url, key, values):
    """Add multiple values for a single query key."""
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    query[key] = values
    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))


# Example usage
url = "https://example.com/search"
new_url = add_multi_value_param(url, "tag", ["python", "web", "snippets"])
print(new_url)  # https://example.com/search?tag=python&tag=web&tag=snippets


# 🧩 Add to URL with empty or no query string
from urllib.parse import urlparse, urlencode, urlunparse


def add_query_to_empty(url, params):
    """Add query parameters to a URL with no query string."""
    parsed = urlparse(url)
    new_query = urlencode(params)
    return urlunparse(parsed._replace(query=new_query))


# Example usage
url = "https://example.com/"
new_url = add_query_to_empty(url, {"q": "python"})
print(new_url)  # https://example.com/?q=python
