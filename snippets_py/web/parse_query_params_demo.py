# 🧩 Extract all query parameters as a dictionary
from urllib.parse import urlparse, parse_qs

url = "https://example.com/search?q=python&lang=en&page=1"
parsed = urlparse(url)
params = parse_qs(parsed.query)
print(params)  # {'q': ['python'], 'lang': ['en'], 'page': ['1']}


# 🧩 Extract single-value query parameters
from urllib.parse import urlparse, parse_qs

url = "https://example.com/search?q=python&lang=en&page=1"
params = parse_qs(urlparse(url).query)
single_params = {k: v[0] for k, v in params.items()}
print(single_params)  # {'q': 'python', 'lang': 'en', 'page': '1'}


# 🧩 Handle repeated keys in query string
from urllib.parse import urlparse, parse_qs

url = "https://example.com/search?tag=python&tag=web&tag=snippets"
params = parse_qs(urlparse(url).query)
print(params)  # {'tag': ['python', 'web', 'snippets']}


# 🧩 Parse query string with missing values and encoded values
from urllib.parse import urlparse, parse_qs

url = "https://example.com/search?q=&lang=en%20US&empty"
params = parse_qs(urlparse(url).query)
print(params)  # {'q': [''], 'lang': ['en US'], 'empty': ['']}


# 🧩 Parse empty query string
from urllib.parse import urlparse, parse_qs

url = "https://example.com/"
params = parse_qs(urlparse(url).query)
print(params)  # {}
