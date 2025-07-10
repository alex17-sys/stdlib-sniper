---
title: File Exists
description: Zero-dependency Python snippets for checking file existence using the standard library.
keywords: access, exists, file, isdir, isfile, islink, os, path, permissions, size
---

# File Exists

Zero-dependency Python snippets for checking file existence using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Check if file exists

`file` `exists` `os` `path`

Check if a file exists in the filesystem

```python
import os

if os.path.exists("file.txt"):
    print("File exists")
else:
    print("File does not exist")
```

!!! note "Notes"
    - Returns True if file exists, False otherwise
    - Works for files, directories, and symlinks
    - Simple and straightforward check

<hr class="snippet-divider">

### Check if file is a regular file

`file` `isfile` `os` `path`

Check if path is a regular file (not directory)

```python
import os

if os.path.isfile("file.txt"):
    print("It is a regular file")
else:
    print("Not a regular file")
```

!!! note "Notes"
    - Returns True only for regular files
    - Returns False for directories, symlinks, etc.
    - More specific than exists()

<hr class="snippet-divider">

## Complex

###  Check file with multiple conditions

`file` `exists` `isfile` `isdir` `islink` `size`

Comprehensive file status check with size information

```python
import os


def check_file_status(filename):
    """Check file existence and type with detailed status."""
    if not os.path.exists(filename):
        return "File does not exist"

    if os.path.isfile(filename):
        size = os.path.getsize(filename)
        return f"Regular file, size: {size} bytes"

    if os.path.isdir(filename):
        return "It is a directory"

    if os.path.islink(filename):
        return "It is a symbolic link"

    return "Unknown file type"


status = check_file_status("file.txt")
print(status)
```

!!! note "Notes"
    - Distinguishes between file types
    - Provides file size for regular files
    - Handles all common file types
    - Useful for file validation

<hr class="snippet-divider">

### Check file with permissions

`file` `exists` `access` `permissions` `os`

Check file existence and access permissions

```python
import os


def check_file_access(filename):
    """Check file existence and access permissions."""
    if not os.path.exists(filename):
        return "File does not exist"

    checks = []

    # Check read permission
    if os.access(filename, os.R_OK):
        checks.append("readable")
    else:
        checks.append("not readable")

    # Check write permission
    if os.access(filename, os.W_OK):
        checks.append("writable")
    else:
        checks.append("not writable")

    # Check execute permission
    if os.access(filename, os.X_OK):
        checks.append("executable")
    else:
        checks.append("not executable")

    return f"File exists: {', '.join(checks)}"


access = check_file_access("file.txt")
print(access)
```

!!! note "Notes"
    - Checks read, write, and execute permissions
    - Uses os.access() for permission checking
    - Provides detailed access information
    - Useful for security and file handling

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Directory Exists](./directory_exists.md)
- **Reference**: See [📂 Delete File](./delete_file.md)

## 🏷️ Tags

`file`, `exists`, `os`, `check`, `io`

## 📝 Notes

- Use os.path.isfile() to check for file existence
- Useful for safe file operations
- Related: directory existence and deletion
