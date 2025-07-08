# Write Binary File

Zero-dependency Python snippets using only the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Write binary file

`file` `write` `binary` `bytes` `open`

Write bytes to a binary file

```python
with open("file.bin", "wb") as f:
    f.write(b"Hello, World!")
```

!!! note "Notes"
    - Use 'wb' mode for binary writing
    - Overwrites existing file
    - Writes bytes object directly

<hr class="snippet-divider">

### Write binary file from string

`file` `write` `binary` `encode` `string`

Write string as binary data with encoding

```python
text = "Hello, World!"
with open("file.bin", "wb") as f:
    f.write(text.encode("utf-8"))
```

!!! note "Notes"
    - Encodes string to bytes before writing
    - UTF-8 is the most common encoding
    - Handles international characters

<hr class="snippet-divider">

## Complex

###  Write binary file with structured data

`file` `write` `binary` `struct` `structured` `data-types`

Write structured binary data with headers and type information

```python
import struct


def write_binary_structure(filename, data_type, data):
    """Write structured binary data to file."""
    with open(filename, "wb") as f:
        if data_type == "string":
            data_bytes = data.encode("utf-8")
            length = len(data_bytes)
            # Write header: length (4 bytes) + type (4 bytes)
            f.write(struct.pack(">II", length, 1))
            f.write(data_bytes)
        elif data_type == "integer":
            f.write(struct.pack(">II", 4, 2))  # length=4, type=2
            f.write(struct.pack(">I", data))
        elif data_type == "float":
            f.write(struct.pack(">II", 4, 3))  # length=4, type=3
            f.write(struct.pack(">f", data))


# Write different data types
write_binary_structure("data.bin", "string", "Hello, World!")
write_binary_structure("data.bin", "integer", 42)
write_binary_structure("data.bin", "float", 3.14)
```

!!! note "Notes"
    - Uses struct module for binary packing
    - Includes length and type headers
    - Supports multiple data types
    - Useful for custom binary formats

<hr class="snippet-divider">

### Write binary file with checksum

`file` `write` `binary` `checksum` `md5` `struct`

Write binary file with checksum for integrity

```python
import hashlib
import struct


def write_binary_with_checksum(filename, data):
    """Write binary data to file with checksum for integrity."""
    checksum = hashlib.md5(data).hexdigest()
    with open(filename, "wb") as f:
        # Write checksum length and checksum
        checksum_bytes = checksum.encode("utf-8")
        f.write(struct.pack(">I", len(checksum_bytes)))
        f.write(checksum_bytes)
        # Write data length and data
        f.write(struct.pack(">I", len(data)))
        f.write(data)

write_binary_with_checksum("data_with_checksum.bin", b"important binary data")
```

!!! note "Notes"
    - Stores checksum and data length for verification
    - Useful for data integrity and validation
    - Uses struct for binary packing

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Read Binary File](./read_binary_file.md)
- **Reference**: See [📂 Write File](./write_file.md)

## 🏷️ Tags

`file`, `binary`, `write`, `bytes`, `io`

## 📝 Notes

- Use open() with mode 'wb' to write binary files
- Overwrites existing content by default
- Useful for images, executables, and non-text data
