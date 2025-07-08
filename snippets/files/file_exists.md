# File Exists

Zero-dependency Python snippets for checking file existence using the standard library.

## Simple

### 🧩 Check if file exists

```python
import os

if os.path.exists("file.txt"):
    print("File exists")
else:
    print("File does not exist")
```

📂 Check if a file exists in the filesystem

🏷️ Tags: file, exists, os, path
📝 Notes:
- Returns True if file exists, False otherwise
- Works for files, directories, and symlinks
- Simple and straightforward check

### 🧩 Check if file is a regular file

```python
import os

if os.path.isfile("file.txt"):
    print("It is a regular file")
else:
    print("Not a regular file")
```

📂 Check if path is a regular file (not directory)

🏷️ Tags: file, isfile, os, path
📝 Notes:
- Returns True only for regular files
- Returns False for directories, symlinks, etc.
- More specific than exists()

## Complex

### 🧩 Check file with multiple conditions

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

📂 Comprehensive file status check with size information

🏷️ Tags: file, exists, isfile, isdir, islink, size
📝 Notes:
- Distinguishes between file types
- Provides file size for regular files
- Handles all common file types
- Useful for file validation

### 🧩 Check file with permissions

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

📂 Check file existence and access permissions

🏷️ Tags: file, exists, access, permissions, os
📝 Notes:
- Checks read, write, and execute permissions
- Uses os.access() for permission checking
- Provides detailed access information
- Useful for security and file handling

## 🔗 Cross-References

- **Reference**: See [📂 Directory Exists](./directory_exists.md)
- **Reference**: See [📂 Delete File](./delete_file.md)

## 🏷️ Tags

`file`, `exists`, `os`, `check`, `io`

## 📝 Notes

- Use os.path.isfile() to check for file existence
- Useful for safe file operations
- Related: directory existence and deletion
