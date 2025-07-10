---
title: Download File via HTTP
description: Zero-dependency Python snippets for downloading files via HTTP using the standard library.
keywords: binary, download, edge-case, error, file, get, headers, http, large, progress, streaming, web
---

# Download File via HTTP

Zero-dependency Python snippets for downloading files via HTTP using the standard library.

5 snippets available in this sub-category.

---

## Simple

###  Simple file download

`http` `download` `file` `get` `binary` `web`

Simple file download

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

!!! note "Notes"
    - Downloads the entire file into memory before writing
    - Use streaming for large files (see below)

<hr class="snippet-divider">

### Download file with progress bar

`http` `download` `file` `progress` `binary` `web`

Download file with progress bar

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

!!! note "Notes"
    - Shows progress if Content-Length is available
    - For very large files, consider chunk sizes of 64KB or more

<hr class="snippet-divider">

## Complex

###  Download with custom headers and error handling

`http` `download` `file` `headers` `error` `web`

Download file with custom headers and error handling

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

!!! note "Notes"
    - Handles HTTP and URL errors
    - Custom headers for authentication, user-agent, etc.

<hr class="snippet-divider">

### Download large file (streaming, low memory)

`http` `download` `file` `streaming` `large` `binary` `web`

Download large file (streaming)

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

!!! note "Notes"
    - Reads and writes in chunks (default 64KB)
    - Suitable for very large files

<hr class="snippet-divider">

## Edge Cases

###  Invalid URL and disk full

`http` `download` `file` `error` `edge-case` `web`

Edge cases: invalid URL and disk full

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

!!! note "Notes"
    - Invalid URLs raise URLError or ValueError
    - Disk full or permission errors raise OSError/IOError

<hr class="snippet-divider">

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
