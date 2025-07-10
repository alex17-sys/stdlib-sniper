---
title: Read Binary File
description: Zero-dependency Python snippets for reading binary files using the standard library.
keywords: binary, bytes, chunks, decode, encoding, error-handling, file, memory-efficient, open, parsing, read, struct, structured
---

# Read Binary File

Zero-dependency Python snippets for reading binary files using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Read binary file

`file` `read` `binary` `bytes` `open`

Read entire binary file into bytes object

```python
with open("file.bin", "rb") as f:
    data = f.read()
print(f"Read {len(data)} bytes")
```

!!! note "Notes"
    - Use 'rb' mode for binary files
    - Returns bytes object
    - Loads entire file into memory

<hr class="snippet-divider">

### Read binary file in chunks

`file` `read` `binary` `chunks` `memory-efficient`

Read binary file in chunks to manage memory

```python
with open("file.bin", "rb") as f:
    chunk = f.read(1024)  # Read 1KB at a time
    while chunk:
        print(f"Read {len(chunk)} bytes")
        chunk = f.read(1024)
```

!!! note "Notes"
    - Reads file in smaller chunks
    - Useful for large binary files
    - Prevents memory issues

<hr class="snippet-divider">

## Complex

###  Read binary file with specific encoding

`file` `read` `binary` `decode` `encoding` `error-handling`

Read binary file and decode as text with error handling

```python
def read_binary_as_text(filename, encoding="utf-8"):
    """Read binary file and decode as text."""
    try:
        with open(filename, "rb") as f:
            data = f.read()
            return data.decode(encoding)
    except UnicodeDecodeError:
        print(f"Cannot decode file with {encoding} encoding")
        return None


text = read_binary_as_text("file.bin", "utf-8")
if text:
    print(text)
```

!!! note "Notes"
    - Attempts to decode binary data as text
    - Handles encoding errors gracefully
    - Supports different encodings
    - Useful for mixed binary/text files

<hr class="snippet-divider">

### Read binary file with structure parsing

`file` `read` `binary` `struct` `parsing` `structured`

Read binary file with structured data parsing

```python
import struct


def read_binary_structure(filename):
    """Read binary file with structured data parsing."""
    with open(filename, "rb") as f:
        # Read header (4 bytes for length, 4 bytes for type)
        header = f.read(8)
        if len(header) < 8:
            return None

        # Unpack header using struct
        length, data_type = struct.unpack(">II", header)

        # Read data based on type
        if data_type == 1:  # String
            data = f.read(length).decode("utf-8")
        elif data_type == 2:  # Integer
            data = struct.unpack(">I", f.read(4))[0]
        elif data_type == 3:  # Float
            data = struct.unpack(">f", f.read(4))[0]
        else:
            data = f.read(length)

        return {"length": length, "type": data_type, "data": data}


result = read_binary_structure("structured.bin")
if result:
    print(f"Type: {result['type']}, Data: {result['data']}")
```

!!! note "Notes"
    - Uses struct module for binary parsing
    - Handles different data types
    - Supports custom binary formats
    - Useful for binary protocols and formats

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Write Binary File](./write_binary_file.md)
- **Reference**: See [📂 Read File](./read_file.md)

## 🏷️ Tags

`file`, `binary`, `read`, `bytes`, `io`

## 📝 Notes

- Use open() with mode 'rb' to read binary files
- Returns bytes, not strings
- Useful for images, executables, and non-text data
