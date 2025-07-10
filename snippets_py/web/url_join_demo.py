# 🧩 Join base and relative URLs
from urllib.parse import urljoin

base = "https://example.com/docs/"
relative = "about/contact.html"
full_url = urljoin(base, relative)
print(full_url)  # https://example.com/docs/about/contact.html


# 🧩 Join with dot segments (.. and .)
from urllib.parse import urljoin

base = "https://example.com/docs/tutorials/"
relative = "../about/./contact.html"
full_url = urljoin(base, relative)
print(full_url)  # https://example.com/about/contact.html


# 🧩 Join with/without trailing slashes
from urllib.parse import urljoin

base1 = "https://example.com/docs"
relative1 = "page.html"
print(urljoin(base1, relative1))  # https://example.com/page.html

base2 = "https://example.com/docs/"
relative2 = "page.html"
print(urljoin(base2, relative2))  # https://example.com/docs/page.html


# 🧩 Join with query and fragment
from urllib.parse import urljoin

base = "https://example.com/search?q=python"
relative = "results#section2"
full_url = urljoin(base, relative)
print(full_url)  # https://example.com/results#section2


# 🧩 Join with absolute relative URL
from urllib.parse import urljoin

base = "https://example.com/docs/"
relative = "https://other.com/page"
full_url = urljoin(base, relative)
print(full_url)  # https://other.com/page


# 🧩 Join with empty base or malformed URLs
from urllib.parse import urljoin

# Empty base
print(urljoin("", "page.html"))  # page.html

# Malformed base
print(urljoin("not-a-url", "page.html"))  # page.html
