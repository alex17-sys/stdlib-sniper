# 🧩 Read entire file as string
with open("file.txt", "r") as f:
    content = f.read()
print(content)


# 🧩 Read file with encoding
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)


# 🧩 Read file with error handling
def read_file_safe(filename, encoding="utf-8"):
    """Read file with comprehensive error handling."""
    try:
        with open(filename, "r", encoding=encoding) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return None
    except UnicodeDecodeError:
        print(f"Error: Unable to decode '{filename}' with {encoding} encoding")
        return None


content = read_file_safe("file.txt")
if content:
    print(content)


# 🧩 Read file in chunks
def read_file_chunks(filename, chunk_size=1024):
    """Read file in chunks to handle large files efficiently."""
    with open(filename, "r") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk


# Process large file in chunks
for chunk in read_file_chunks("large_file.txt", chunk_size=4096):
    print(f"Processing chunk: {len(chunk)} characters")
    # Process chunk here
