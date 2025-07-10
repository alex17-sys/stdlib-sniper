# 🧩 Parse URL into components
from urllib.parse import urlparse


def parse_url(url):
    """Parse a URL and return its components."""
    parsed = urlparse(url)
    return parsed


# Example usage
url = "https://user:pass@example.com:8080/path/to/page?query=python#section"
parsed = parse_url(url)
print(parsed)
# ParseResult(scheme='https', netloc='user:pass@example.com:8080', path='/path/to/page', params='', query='query=python', fragment='section')


# 🧩 Extract individual URL components
from urllib.parse import urlparse

url = "https://user:pass@example.com:8080/path/to/page?query=python#section"
parsed = urlparse(url)
print("Scheme:", parsed.scheme)
print("Netloc:", parsed.netloc)
print("Path:", parsed.path)
print("Params:", parsed.params)
print("Query:", parsed.query)
print("Fragment:", parsed.fragment)


# 🧩 Parse query parameters from URL
from urllib.parse import urlparse, parse_qs

url = "https://example.com/search?q=python&lang=en&lang=fr"
parsed = urlparse(url)
query_params = parse_qs(parsed.query)
print(query_params)
# {'q': ['python'], 'lang': ['en', 'fr']}


# 🧩 Handle missing scheme and relative URLs
from urllib.parse import urlparse

# Missing scheme
url = "www.example.com/path"
parsed = urlparse(url)
print(parsed)
# ParseResult(scheme='', netloc='', path='www.example.com/path', params='', query='', fragment='')

# Relative URL
url2 = "/about/contact"
parsed2 = urlparse(url2)
print(parsed2)
# ParseResult(scheme='', netloc='', path='/about/contact', params='', query='', fragment='')


# 🧩 Parse non-standard ports and user info
from urllib.parse import urlparse

url = "ftp://user:pass@ftp.example.com:2121/files"
parsed = urlparse(url)
print("Scheme:", parsed.scheme)
print("Netloc:", parsed.netloc)
print("Path:", parsed.path)

# Extract user, password, host, port manually
userinfo, hostport = parsed.netloc.split("@") if "@" in parsed.netloc else ("", parsed.netloc)
user, password = userinfo.split(":") if ":" in userinfo else (userinfo, "")
host, port = hostport.split(":") if ":" in hostport else (hostport, "")
print("User:", user)
print("Password:", password)
print("Host:", host)
print("Port:", port)


# 🧩 Parse URL with IPv6 address
from urllib.parse import urlparse

url = "http://[2001:db8::1]:8080/index.html"
parsed = urlparse(url)
print(parsed)
# ParseResult(scheme='http', netloc='[2001:db8::1]:8080', path='/index.html', params='', query='', fragment='')
