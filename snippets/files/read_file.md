# Read File

Zero-dependency Python snippets for reading files using the standard library.

## Simple

### 🧩 Read entire file as string

```python
with open("file.txt", "r") as f:
    content = f.read()
print(content)
```

📂 Read entire file content as a single string

🏷️ Tags: file, read, string, open
📝 Notes:
- Use 'r' mode for text files
- File is automatically closed after reading
- Returns empty string if file is empty

### 🧩 Read file with encoding

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)
```

📂 Read file with specific encoding

🏷️ Tags: file, read, encoding, utf-8
📝 Notes:
- Always specify encoding for international text
- UTF-8 is the most common encoding
- Handles special characters properly

## Complex

### 🧩 Read file with error handling

```python
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
```

📂 Read file with comprehensive error handling and encoding support

🏷️ Tags: file, read, error-handling, function, encoding
📝 Notes:
- Handles common file reading errors
- Returns None on error for easy checking
- Supports custom encoding
- Provides helpful error messages

### 🧩 Read file in chunks

```python
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
```

📂 Read large files in chunks to manage memory efficiently

🏷️ Tags: file, read, chunks, generator, memory-efficient
📝 Notes:
- Uses generator to yield chunks
- Prevents loading entire large file into memory
- Customizable chunk size
- Useful for processing large log files or datasets

## 🔗 Cross-References

- **Reference**: See [📂 Write File](./write_file.md)
- **Reference**: See [📂 Read File Lines](./read_file_lines.md)

## 🏷️ Tags

`file`, `read`, `text`, `io`

## 📝 Notes

- Use open() with mode 'r' to read text files
- Returns file content as a string
- Useful for configuration, data, and logs
