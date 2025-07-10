# 🧩 Simple file download
import urllib.request


def download_file(url, dest_path):
    """Download a file from a URL to a local path."""
    with urllib.request.urlopen(url) as response, open(dest_path, "wb") as out_file:
        out_file.write(response.read())


# Example usage
url = "https://httpbin.org/image/png"
download_file(url, "output.png")


# 🧩 Download file with progress bar
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
                print(
                    f"Downloaded {downloaded}/{total} bytes ({downloaded * 100 // total}%)",
                    end="\r",
                )
        print()


# Example usage
url = "https://httpbin.org/bytes/1048576"  # 1 MB file
download_file_with_progress(url, "output.bin")


# 🧩 Download with custom headers and error handling
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


# 🧩 Download large file (streaming, low memory)
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


# 🧩 Invalid URL and disk full
# Function is defined in one of the above code block (download_file_safe)

# Edge case: Invalid URL
try:
    download_file_safe("not-a-url", "output.txt")
except Exception as e:
    print(f"Error: {e}")

# Edge case: Disk full (simulate by writing to a full disk or read-only location)
# This will raise an OSError or IOError
