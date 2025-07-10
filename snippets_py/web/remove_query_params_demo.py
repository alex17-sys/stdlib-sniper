# 🧩 Remove a single query parameter
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


def remove_query_param(url, key):
    """Remove a single query parameter from a URL."""
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    query.pop(key, None)
    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))


# Example usage
url = "https://example.com/search?q=python&lang=en&page=1"
new_url = remove_query_param(url, "lang")
print(new_url)  # https://example.com/search?q=python&page=1


# 🧩 Remove multiple query parameters
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


def remove_query_params(url, keys):
    """Remove multiple query parameters from a URL."""
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    for key in keys:
        query.pop(key, None)
    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))


# Example usage
url = "https://example.com/search?q=python&lang=en&page=1"
new_url = remove_query_params(url, ["q", "page"])
print(new_url)  # https://example.com/search?lang=en


# 🧩 Remove all query parameters
from urllib.parse import urlparse, urlunparse


def remove_all_query_params(url):
    """Remove all query parameters from a URL."""
    parsed = urlparse(url)
    return urlunparse(parsed._replace(query=""))


# Example usage
url = "https://example.com/search?q=python&lang=en&page=1"
new_url = remove_all_query_params(url)
print(new_url)  # https://example.com/search


# 🧩 Remove non-existent or encoded keys, empty query
# Function is defined in one of the above code block (remove_query_param)


# Remove non-existent key
url = "https://example.com/search?q=python"
print(remove_query_param(url, "lang"))  # https://example.com/search?q=python

# Remove encoded key
url2 = "https://example.com/search?na%20me=John&q=python"
print(remove_query_param(url2, "na me"))  # https://example.com/search?q=python

# Remove from URL with no query
url3 = "https://example.com/"
print(remove_query_param(url3, "q"))  # https://example.com/
