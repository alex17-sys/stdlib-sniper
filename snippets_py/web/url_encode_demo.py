# 🧩 Encode query string parameters
from urllib.parse import urlencode

params = {"q": "python programming", "lang": "en", "page": 1}
encoded = urlencode(params)
print(encoded)  # q=python+programming&lang=en&page=1


# 🧩 Encode path segment
from urllib.parse import quote

segment = "Café & Bistro/2024"
encoded = quote(segment)
print(encoded)  # Caf%C3%A9%20%26%20Bistro/2024

# To encode slashes as well:
encoded_strict = quote(segment, safe="")
print(encoded_strict)  # Caf%C3%A9%20%26%20Bistro%2F2024


# 🧩 Encode form data for POST
from urllib.parse import urlencode

data = {"name": "John Doe", "email": "john@example.com", "message": "Hello!"}
encoded = urlencode(data)
print(encoded)  # name=John+Doe&email=john%40example.com&message=Hello%21


# 🧩 Encode with Unicode and reserved characters
from urllib.parse import quote, urlencode

text = "emoji: 😃 & symbols: @#%"
encoded = quote(text)
print(encoded)  # emoji%3A%20%F0%9F%98%83%20%26%20symbols%3A%20%40%23%25

params = {"q": "café", "emoji": "😃"}
encoded_params = urlencode(params)
print(encoded_params)  # q=caf%C3%A9&emoji=%F0%9F%98%83


# 🧩 Encode already-encoded strings and empty values
from urllib.parse import quote

already_encoded = "hello%20world"
encoded = quote(already_encoded)
print(encoded)  # hello%2520world (double-encoded)

empty = ""
print(quote(empty))  # ''
