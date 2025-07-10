# 🧩 Simple HTTP session with cookies
import urllib.request
import http.cookiejar

# Create a CookieJar to store cookies
cookie_jar = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(handler)

# Perform a GET request (cookies will be stored)
url = "https://httpbin.org/cookies/set?mycookie=value"
response = opener.open(url)
print(response.read().decode("utf-8"))

# Perform another request (cookies sent automatically)
url2 = "https://httpbin.org/cookies"
response2 = opener.open(url2)
print(response2.read().decode("utf-8"))


# 🧩 HTTP session with custom headers
import urllib.request
import http.cookiejar

cookie_jar = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(handler)

url = "https://httpbin.org/headers"
headers = {"User-Agent": "stdlib-sniper/1.0", "X-Test": "session"}
req = urllib.request.Request(url, headers=headers)
response = opener.open(req)
print(response.read().decode("utf-8"))


# 🧩 Simulate login and session persistence
import urllib.request
import urllib.parse
import http.cookiejar

cookie_jar = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(handler)

# Simulate login (POST)
login_url = "https://httpbin.org/cookies/set/sessioncookie/123456"
login_data = {}  # No data needed for httpbin, but typically you'd send credentials
opener.open(login_url, data=urllib.parse.urlencode(login_data).encode("utf-8"))

# Access a page that requires the session cookie
protected_url = "https://httpbin.org/cookies"
response = opener.open(protected_url)
print(response.read().decode("utf-8"))


# 🧩 Error handling and edge cases
import urllib.request
import http.cookiejar

cookie_jar = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(handler)

try:
    url = "https://httpbin.org/status/403"
    response = opener.open(url)
    print(response.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    print(f"HTTP error: {e.code} {e.reason}")
except Exception as e:
    print(f"Unexpected error: {e}")


# 🧩 Session reset and manual cookie management
import http.cookiejar

# Resetting session (new CookieJar)
cookie_jar = http.cookiejar.CookieJar()  # New session, no cookies

# Manual cookie manipulation
for cookie in cookie_jar:
    print(cookie.name, cookie.value)
# You can add/remove cookies manually if needed
