# 🧩 Decode query string parameters
from urllib.parse import parse_qs

query = "q=python+programming&lang=en&page=1"
params = parse_qs(query)
print(params)  # {'q': ['python programming'], 'lang': ['en'], 'page': ['1']}


# 🧩 Decode path segment
from urllib.parse import unquote

encoded = "Caf%C3%A9%20%26%20Bistro%2F2024"
decoded = unquote(encoded)
print(decoded)  # Café & Bistro/2024


# 🧩 Decode form data from POST
from urllib.parse import parse_qs

encoded = "name=John+Doe&email=john%40example.com&message=Hello%21"
params = parse_qs(encoded)
print(params)  # {'name': ['John Doe'], 'email': ['john@example.com'], 'message': ['Hello!']}


# 🧩 Decode with Unicode and reserved characters
from urllib.parse import unquote

encoded = "emoji%3A%20%F0%9F%98%83%20%26%20symbols%3A%20%40%23%25"
decoded = unquote(encoded)
print(decoded)  # emoji: 😃 & symbols: @#%


# 🧩 Double decoding and empty values
from urllib.parse import unquote

# Double-encoded string
double_encoded = "hello%2520world"
first = unquote(double_encoded)
second = unquote(first)
print(first)  # hello%20world
print(second)  # hello world

# Empty string
print(unquote(""))  # ''
