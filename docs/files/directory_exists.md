---
title: Directory Exists
description: Zero-dependency Python snippets for checking directory existence using the standard library.
keywords: accessibility, check, directory, exists, isdir, os, path, permissions, status, validate
---

# Directory Exists

Zero-dependency Python snippets for checking directory existence using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Check if directory exists

`directory` `exists` `check` `os` `path`

Check if a directory exists in the filesystem

```python
import os

if os.path.exists("directory_name"):
    print("Directory exists")
else:
    print("Directory does not exist")
```

!!! note "Notes"
    - Returns True if path exists (file or directory)
    - Returns False if path doesn't exist
    - Works for any path type

<hr class="snippet-divider">

### Check if path is a directory

`directory` `isdir` `check` `os` `path`

Check if path is specifically a directory

```python
import os

if os.path.isdir("directory_name"):
    print("It is a directory")
else:
    print("Not a directory")
```

!!! note "Notes"
    - Returns True only for directories
    - Returns False for files, symlinks, etc.
    - More specific than exists()

<hr class="snippet-divider">

## Complex

###  Check directory with detailed status

`directory` `exists` `check` `status` `permissions` `os`

Check directory existence with detailed status and permissions

```python
import os


def check_directory_status(directory):
    """Check directory existence and type with detailed status."""
    if not os.path.exists(directory):
        return "Directory does not exist"

    if os.path.isdir(directory):
        # Check permissions
        permissions = []
        if os.access(directory, os.R_OK):
            permissions.append("readable")
        if os.access(directory, os.W_OK):
            permissions.append("writable")
        if os.access(directory, os.X_OK):
            permissions.append("executable")

        return f"Directory exists and is {', '.join(permissions)}"

    elif os.path.isfile(directory):
        return "Path exists but is a file, not a directory"

    elif os.path.islink(directory):
        return "Path exists but is a symbolic link"

    else:
        return "Path exists but is not a regular directory"


status = check_directory_status("my_directory")
print(status)
```

!!! note "Notes"
    - Distinguishes between different path types
    - Checks read, write, and execute permissions
    - Provides detailed status information
    - Useful for validation and debugging

<hr class="snippet-divider">

### Check directory with validation

`directory` `exists` `validate` `permissions` `accessibility` `os`

Validate directory with comprehensive existence and permission checks

```python
import os


def validate_directory(directory, check_permissions=True):
    """Validate directory existence and accessibility."""
    validation_result = {
        "exists": False,
        "is_directory": False,
        "readable": False,
        "writable": False,
        "executable": False,
        "errors": [],
    }

    # Check existence
    if not os.path.exists(directory):
        validation_result["errors"].append(f"Directory '{directory}' does not exist")
        return validation_result

    validation_result["exists"] = True

    # Check if it's a directory
    if not os.path.isdir(directory):
        validation_result["errors"].append(f"'{directory}' is not a directory")
        return validation_result

    validation_result["is_directory"] = True

    # Check permissions if requested
    if check_permissions:
        if os.access(directory, os.R_OK):
            validation_result["readable"] = True
        else:
            validation_result["errors"].append("Directory is not readable")

        if os.access(directory, os.W_OK):
            validation_result["writable"] = True
        else:
            validation_result["errors"].append("Directory is not writable")

        if os.access(directory, os.X_OK):
            validation_result["executable"] = True
        else:
            validation_result["errors"].append("Directory is not executable")

    return validation_result


# Validate directory
result = validate_directory("/path/to/directory")
if result["errors"]:
    print("Validation errors:")
    for error in result["errors"]:
        print(f"  - {error}")
else:
    print("Directory is valid and accessible")
```

!!! note "Notes"
    - Returns detailed validation results
    - Checks all relevant permissions
    - Provides specific error messages
    - Useful for setup and configuration scripts

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 File Exists](./file_exists.md)
- **Reference**: See [📂 Create Directory](./create_directory.md)

## 🏷️ Tags

`file`, `directory`, `exists`, `os`, `check`, `io`

## 📝 Notes

- Use os.path.isdir() to check for directory existence
- Useful for safe directory operations
- Related: file existence and creation
