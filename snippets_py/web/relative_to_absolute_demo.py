# 🧩 Convert relative URL to absolute using base
from urllib.parse import urljoin

base = "https://example.com/docs/"
relative = "about/contact.html"
absolute = urljoin(base, relative)
print(absolute)  # https://example.com/docs/about/contact.html


# 🧩 Convert with dot segments (.. and .)
from urllib.parse import urljoin

base = "https://example.com/docs/tutorials/"
relative = "../about/./contact.html"
absolute = urljoin(base, relative)
print(absolute)  # https://example.com/about/contact.html


# 🧩 Convert already absolute URL
from urllib.parse import urljoin

base = "https://example.com/docs/"
relative = "https://other.com/page"
absolute = urljoin(base, relative)
print(absolute)  # https://other.com/page


# 🧩 Convert with empty base or malformed URLs
# Code is defined in another file (URL Join (Join with empty base or malformed URLs)) cited below
