# File Checksum

Zero-dependency Python snippets using only the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Calculate MD5 checksum

`file` `checksum` `md5` `hashlib`

Calculate MD5 checksum of a file

```python
import hashlib

with open("file.txt", "rb") as f:
    data = f.read()
    md5_hash = hashlib.md5(data).hexdigest()
print(f"MD5: {md5_hash}")
```

!!! note "Notes"
    - Reads entire file into memory
    - Returns hexadecimal string
    - Useful for file integrity verification

<hr class="snippet-divider">

### Calculate SHA-256 checksum

`file` `checksum` `sha256` `hashlib`

Calculate SHA-256 checksum of a file

```python
import hashlib

with open("file.txt", "rb") as f:
    data = f.read()
    sha256_hash = hashlib.sha256(data).hexdigest()
print(f"SHA-256: {sha256_hash}")
```

!!! note "Notes"
    - More secure than MD5
    - Longer hash (64 characters)
    - Recommended for security applications

<hr class="snippet-divider">

## Complex

###  Calculate checksum for large files

`file` `checksum` `large-files` `chunks` `memory-efficient` `hashlib`

Calculate checksums for large files using memory-efficient chunks

```python
import hashlib


def calculate_file_checksum(filename, algorithm="md5"):
    """Calculate checksum for large files in chunks."""
    if algorithm == "md5":
        hash_obj = hashlib.md5()
    elif algorithm == "sha256":
        hash_obj = hashlib.sha256()
    elif algorithm == "sha1":
        hash_obj = hashlib.sha1()
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    with open(filename, "rb") as f:
        while True:
            chunk = f.read(8192)  # Read 8KB chunks
            if not chunk:
                break
            hash_obj.update(chunk)

    return hash_obj.hexdigest()


# Calculate different checksums
md5_hash = calculate_file_checksum("large_file.txt", "md5")
sha256_hash = calculate_file_checksum("large_file.txt", "sha256")
print(f"MD5: {md5_hash}")
print(f"SHA-256: {sha256_hash}")
```

!!! note "Notes"
    - Processes file in chunks to save memory
    - Supports multiple hash algorithms
    - Handles large files efficiently
    - Useful for big files

<hr class="snippet-divider">

### Verify file integrity with checksum

`file` `checksum` `verify` `integrity` `comparison` `hashlib`

Verify file integrity by comparing with expected checksum

```python
import hashlib
import os


def verify_file_integrity(filename, expected_checksum, algorithm="md5"):
    """Verify file integrity against expected checksum."""
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist")
        return False

    # Calculate actual checksum
    if algorithm == "md5":
        hash_obj = hashlib.md5()
    elif algorithm == "sha256":
        hash_obj = hashlib.sha256()
    else:
        print(f"Unsupported algorithm: {algorithm}")
        return False

    with open(filename, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            hash_obj.update(chunk)

    actual_checksum = hash_obj.hexdigest()

    # Compare checksums
    if actual_checksum.lower() == expected_checksum.lower():
        print(f"✓ File integrity verified ({algorithm})")
        return True
    else:
        print("✗ File integrity check failed!")
        print(f"Expected: {expected_checksum}")
        print(f"Actual:   {actual_checksum}")
        return False


# Verify file integrity
expected_md5 = "d41d8cd98f00b204e9800998ecf8427e"
verify_file_integrity("file.txt", expected_md5, "md5")
```

!!! note "Notes"
    - Compares calculated checksum with expected value
    - Case-insensitive comparison
    - Provides clear success/failure feedback
    - Useful for download verification

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Read File](./read_file.md)
- **Reference**: See [📂 Write File](./write_file.md)

## 🏷️ Tags

`file`, `checksum`, `hash`, `md5`, `sha256`, `integrity`, `io`

## 📝 Notes

- Use hashlib for file checksums (md5, sha256, etc.)
- Useful for verifying file integrity
- Always use secure hashes for security-sensitive data
