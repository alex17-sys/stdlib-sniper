# Upload File via HTTP (multipart/form-data)

Zero-dependency Python snippets for uploading files via HTTP using the standard library.

## Simple

### 🧩 Simple file upload (multipart/form-data)

```python
import urllib.request
import mimetypes
import uuid

def upload_file(url, file_path, field_name="file"):
    """Upload a file using multipart/form-data."""
    boundary = uuid.uuid4().hex
    content_type = f"multipart/form-data; boundary={boundary}"
    with open(file_path, "rb") as f:
        file_content = f.read()
    filename = file_path.split("/")[-1]
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"\r\n'
        f"Content-Type: {mimetypes.guess_type(filename)[0] or 'application/octet-stream'}\r\n\r\n"
    ).encode() + file_content + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", content_type)
    req.add_header("Content-Length", str(len(body)))
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
# url = "https://httpbin.org/post"
# file_path = "example.txt"
# result = upload_file(url, file_path)
# print(result)
```

📂 Simple file upload (multipart/form-data)

🏷️ Tags: http, upload, file, multipart, post, web
📝 Notes:
- Manually constructs multipart/form-data body
- Handles binary file uploads
- For multiple files/fields, see below

## Complex

### 🧩 Upload file with custom headers and error handling

```python
import urllib.request
import mimetypes
import uuid
import urllib.error

def upload_file_safe(url, file_path, field_name="file", headers=None):
    """Upload a file with custom headers and error handling."""
    boundary = uuid.uuid4().hex
    content_type = f"multipart/form-data; boundary={boundary}"
    with open(file_path, "rb") as f:
        file_content = f.read()
    filename = file_path.split("/")[-1]
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"\r\n'
        f"Content-Type: {mimetypes.guess_type(filename)[0] or 'application/octet-stream'}\r\n\r\n"
    ).encode() + file_content + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", content_type)
    req.add_header("Content-Length", str(len(body)))
    if headers:
        for k, v in headers.items():
            req.add_header(k, v)
    try:
        with urllib.request.urlopen(req) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

# Example usage
# url = "https://httpbin.org/post"
# file_path = "example.txt"
# headers = {"User-Agent": "stdlib-sniper/1.0"}
# result = upload_file_safe(url, file_path, headers=headers)
# print(result)
```

📂 File upload with custom headers and error handling

🏷️ Tags: http, upload, file, headers, error, multipart, post, web
📝 Notes:
- Handles HTTP and URL errors
- Custom headers for authentication, user-agent, etc.

### 🧩 Upload multiple files (multipart/form-data)

```python
import urllib.request
import mimetypes
import uuid

def upload_multiple_files(url, files, field_name="file"):
    """Upload multiple files using multipart/form-data."""
    boundary = uuid.uuid4().hex
    content_type = f"multipart/form-data; boundary={boundary}"
    body = b""
    for file_path in files:
        with open(file_path, "rb") as f:
            file_content = f.read()
        filename = file_path.split("/")[-1]
        body += (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"\r\n'
            f"Content-Type: {mimetypes.guess_type(filename)[0] or 'application/octet-stream'}\r\n\r\n"
        ).encode() + file_content + b"\r\n"
    body += f"--{boundary}--\r\n".encode()
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", content_type)
    req.add_header("Content-Length", str(len(body)))
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

# Example usage
# url = "https://httpbin.org/post"
# files = ["file1.txt", "file2.txt"]
# result = upload_multiple_files(url, files)
# print(result)
```

📂 Upload multiple files (multipart/form-data)

🏷️ Tags: http, upload, files, multipart, post, web
📝 Notes:
- Each file is added as a separate part in the multipart body
- Field name can be the same or different for each file

### 🧩 Upload file with progress reporting

```python
import urllib.request
import mimetypes
import uuid
import os

def upload_file_with_progress(url, file_path, field_name="file", chunk_size=65536):
    """Upload a file with progress reporting (manual chunked upload)."""
    boundary = uuid.uuid4().hex
    content_type = f"multipart/form-data; boundary={boundary}"
    file_size = os.path.getsize(file_path)
    with open(file_path, "rb") as f:
        filename = file_path.split("/")[-1]
        preamble = (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"\r\n'
            f"Content-Type: {mimetypes.guess_type(filename)[0] or 'application/octet-stream'}\r\n\r\n"
        ).encode()
        postamble = f"\r\n--{boundary}--\r\n".encode()
        total = len(preamble) + file_size + len(postamble)
        req = urllib.request.Request(url, method="POST")
        req.add_header("Content-Type", content_type)
        req.add_header("Content-Length", str(total))
        # Manually build the body in chunks
        def body_iter():
            yield preamble
            sent = 0
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                sent += len(chunk)
                print(f"Uploaded {sent}/{file_size} bytes ({sent*100//file_size}%)", end="\r")
                yield chunk
            yield postamble
        # Combine all parts and send
        data = b"".join(body_iter())
        with urllib.request.urlopen(req, data=data) as response:
            print()
            return response.read().decode("utf-8")

# Example usage
# url = "https://httpbin.org/post"
# file_path = "largefile.bin"
# result = upload_file_with_progress(url, file_path)
# print(result)
```

📂 File upload with progress reporting

🏷️ Tags: http, upload, file, progress, multipart, post, web
📝 Notes:
- Shows upload progress for large files
- For true streaming, use lower-level sockets or third-party libraries

## Edge Cases

### 🧩 Large/unsupported files and permission errors

```python
def upload_file_safe(url, file_path, field_name="file", headers=None):
    # Function is defined in one of the above code block
    pass


# Edge case: Large file (may hit server or memory limits)
# Edge case: Unsupported file type (server may reject)
# Edge case: Permission error (file not readable)
try:
    upload_file_safe("https://httpbin.org/post", "/root/secret.txt")
except Exception as e:
    print(f"Error: {e}")
```

📂 Edge cases: large/unsupported files and permission errors

🏷️ Tags: http, upload, file, error, edge-case, multipart, post, web
📝 Notes:
- Large files may require chunked/streaming upload
- Unsupported file types may be rejected by the server
- Permission errors raise OSError/IOError

## 🔗 Cross-References

- **Reference**: See [📂 Download File](./download_file.md)
- **Reference**: See [📂 HTTP POST Request](./http_post.md)
- **Reference**: See [📂 HTTP Headers](./http_headers.md)

## 🏷️ Tags

`http`, `upload`, `file`, `multipart`, `post`, `progress`, `headers`, `error`, `edge-case`, `web`, `binary`

## 📝 Notes

- Always validate file paths and types before uploading
- For resumable uploads, use Range headers or third-party libraries
- For async uploads, consider `asyncio` or external tools
- For advanced multipart, see RFC 7578 or use `requests` library
