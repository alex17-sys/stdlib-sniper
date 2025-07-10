# Download File via HTTP

Zero-dependency Python snippets for downloading files via HTTP using the standard library.

## Simple

### 🧩 Simple file download

```python
import urllib.request

def download_file(url, dest_path):
    """Download a file from a URL to a local path."""
    with urllib.request.urlopen(url) as response, open(dest_path, "wb") as out_file:
        out_file.write(response.read())

# Example usage
url = "https://httpbin.org/image/png"
download_file(url, "output.png")
```

📂 Simple file download

🏷️ Tags: http, download, file, get, binary, web
📝 Notes:
- Downloads the entire file into memory before writing
- Use streaming for large files (see below)

### 🧩 Download file with progress bar

```python
import urllib.request

def download_file_with_progress(url, dest_path, chunk_size=8192):
    """Download a file with a simple progress indicator."""
    with urllib.request.urlopen(url) as response, open(dest_path, "wb") as out_file:
        total = int(response.getheader("Content-Length", 0))
        downloaded = 0
        while True:
            chunk = response.read(chunk_size)
            if not chunk:
                break
            out_file.write(chunk)
            downloaded += len(chunk)
            if total:
                print(f"Downloaded {downloaded}/{total} bytes ({downloaded*100//total}%)", end="\r")
        print()

# Example usage
url = "https://httpbin.org/bytes/1048576"  # 1 MB file
download_file_with_progress(url, "output.bin")
```

📂 Download file with progress bar

🏷️ Tags: http, download, file, progress, binary, web
📝 Notes:
- Shows progress if Content-Length is available
- For very large files, consider chunk sizes of 64KB or more

## Complex

### 🧩 Download with custom headers and error handling

```python
import urllib.request
import urllib.error

def download_file_safe(url, dest_path, headers=None):
    """Download a file with custom headers and error handling."""
    try:
        req = urllib.request.Request(url, headers=headers or {})
        with urllib.request.urlopen(req) as response, open(dest_path, "wb") as out_file:
            out_file.write(response.read())
        print(f"Downloaded to {dest_path}")
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
url = "https://httpbin.org/image/jpeg"
headers = {"User-Agent": "stdlib-sniper/1.0"}
download_file_safe(url, "output.jpg", headers)
```

📂 Download file with custom headers and error handling

🏷️ Tags: http, download, file, headers, error, web
📝 Notes:
- Handles HTTP and URL errors
- Custom headers for authentication, user-agent, etc.

### 🧩 Download large file (streaming, low memory)

```python
import urllib.request

def download_large_file(url, dest_path, chunk_size=65536):
    """Download large file in chunks to minimize memory usage."""
    with urllib.request.urlopen(url) as response, open(dest_path, "wb") as out_file:
        while True:
            chunk = response.read(chunk_size)
            if not chunk:
                break
            out_file.write(chunk)

# Example usage
url = "https://httpbin.org/stream-bytes/10485760"  # 10 MB file
download_large_file(url, "large_output.bin")
```

📂 Download large file (streaming)

🏷️ Tags: http, download, file, streaming, large, binary, web
📝 Notes:
- Reads and writes in chunks (default 64KB)
- Suitable for very large files

## Edge Cases

### 🧩 Invalid URL and disk full

```python
def download_file_safe(url, dest_path, headers=None):
    # Function is defined in one of the above code block
    pass

# Edge case: Invalid URL
try:
    download_file_safe("not-a-url", "output.txt")
except Exception as e:
    print(f"Error: {e}")

# Edge case: Disk full (simulate by writing to a full disk or read-only location)
# This will raise an OSError or IOError
```

📂 Edge cases: invalid URL and disk full

🏷️ Tags: http, download, file, error, edge-case, web
📝 Notes:
- Invalid URLs raise URLError or ValueError
- Disk full or permission errors raise OSError/IOError

## 🔗 Cross-References

- **Reference**: See [📂 HTTP GET Request](./http_get.md)
- **Reference**: See [📂 HTTP POST Request](./http_post.md)
- **Reference**: See [📂 HTTP Headers](./http_headers.md)
- **Reference**: See [📂 HTTP Timeout](./http_timeout.md)

## 🏷️ Tags

`http`, `download`, `file`, `progress`, `streaming`, `headers`, `error`, `edge-case`, `web`, `binary`

## 📝 Notes

- Always validate URLs and file paths before downloading
- For resumable downloads, use Range headers (advanced)
- For FTP/SFTP, use `ftplib` or third-party libraries
- For async downloads, consider `asyncio` or external tools
