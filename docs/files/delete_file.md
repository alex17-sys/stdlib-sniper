---
title: Delete File
description: Zero-dependency Python snippets for deleting files using the standard library.
keywords: confirmation, delete, error-handling, file, glob, multiple, os, pattern, remove
---

# Delete File

Zero-dependency Python snippets for deleting files using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Delete a file

`file` `delete` `remove` `os`

Delete a single file from the filesystem

```python
import os

os.remove("file.txt")
```

!!! note "Notes"
    - Removes the file if it exists
    - Raises FileNotFoundError if file doesn't exist
    - Cannot delete directories (use rmdir for that)

<hr class="snippet-divider">

### Delete file safely

`file` `delete` `remove` `error-handling` `os`

Delete file with error handling for missing files

```python
import os

try:
    os.remove("file.txt")
    print("File deleted successfully")
except FileNotFoundError:
    print("File does not exist")
```

!!! note "Notes"
    - Handles case where file doesn't exist
    - Provides feedback on operation result
    - Safe for scripts that may run multiple times

<hr class="snippet-divider">

## Complex

###  Delete file with confirmation

`file` `delete` `confirmation` `error-handling` `os`

Delete file with confirmation and detailed error handling

```python
import os


def delete_file_safe(filename):
    """Delete file with existence check and confirmation."""
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist")
        return False

    if not os.path.isfile(filename):
        print(f"'{filename}' is not a regular file")
        return False

    # Show file info before deletion
    size = os.path.getsize(filename)
    print(f"File: {filename}")
    print(f"Size: {size} bytes")

    # Ask for confirmation
    response = input("Are you sure you want to delete this file? (y/N): ")
    if response.lower() in ["y", "yes"]:
        try:
            os.remove(filename)
            print(f"File '{filename}' deleted successfully")
            return True
        except PermissionError:
            print(f"Permission denied: cannot delete '{filename}'")
            return False
    else:
        print("Deletion cancelled")
        return False


delete_file_safe("important.txt")
```

!!! note "Notes"
    - Shows file information before deletion
    - Asks for user confirmation
    - Handles permission errors
    - Safe for important files

<hr class="snippet-divider">

### Delete multiple files

`file` `delete` `multiple` `pattern` `glob` `confirmation`

Delete multiple files matching a pattern with confirmation

```python
import os
import glob


def delete_files_pattern(pattern):
    """Delete multiple files matching a pattern."""
    files = glob.glob(pattern)
    if not files:
        print(f"No files found matching '{pattern}'")
        return

    print(f"Found {len(files)} files:")
    for file in files:
        print(f"  - {file}")

    response = input("Delete all these files? (y/N): ")
    if response.lower() in ["y", "yes"]:
        deleted_count = 0
        for file in files:
            try:
                os.remove(file)
                print(f"Deleted: {file}")
                deleted_count += 1
            except OSError as e:
                print(f"Error deleting {file}: {e}")

        print(f"Successfully deleted {deleted_count} files")
    else:
        print("Deletion cancelled")


# Delete all .tmp files
delete_files_pattern("*.tmp")
```

!!! note "Notes"
    - Uses glob patterns for file matching
    - Shows list of files before deletion
    - Handles errors for individual files
    - Useful for cleanup operations

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Delete Directory](./delete_directory.md)
- **Reference**: See [📂 File Exists](./file_exists.md)

## 🏷️ Tags

`file`, `delete`, `remove`, `os`, `exists`, `io`

## 📝 Notes

- Use os.remove() to delete files
- Always check file existence before deleting
- Useful for cleanup and automation
