# Delete File

Zero-dependency Python snippets for deleting files using the standard library.

## Simple

### 🧩 Delete a file

```python
import os

os.remove("file.txt")
```

📂 Delete a single file from the filesystem

🏷️ Tags: file, delete, remove, os
📝 Notes:
- Removes the file if it exists
- Raises FileNotFoundError if file doesn't exist
- Cannot delete directories (use rmdir for that)

### 🧩 Delete file safely

```python
import os

try:
    os.remove("file.txt")
    print("File deleted successfully")
except FileNotFoundError:
    print("File does not exist")
```

📂 Delete file with error handling for missing files

🏷️ Tags: file, delete, remove, error-handling, os
📝 Notes:
- Handles case where file doesn't exist
- Provides feedback on operation result
- Safe for scripts that may run multiple times

## Complex

### 🧩 Delete file with confirmation

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

📂 Delete file with confirmation and detailed error handling

🏷️ Tags: file, delete, confirmation, error-handling, os
📝 Notes:
- Shows file information before deletion
- Asks for user confirmation
- Handles permission errors
- Safe for important files

### 🧩 Delete multiple files

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

📂 Delete multiple files matching a pattern with confirmation

🏷️ Tags: file, delete, multiple, pattern, glob, confirmation
📝 Notes:
- Uses glob patterns for file matching
- Shows list of files before deletion
- Handles errors for individual files
- Useful for cleanup operations

## 🔗 Cross-References

- **Reference**: See [📂 Delete Directory](./delete_directory.md)
- **Reference**: See [📂 File Exists](./file_exists.md)

## 🏷️ Tags

`file`, `delete`, `remove`, `os`, `exists`, `io`

## 📝 Notes

- Use os.remove() to delete files
- Always check file existence before deleting
- Useful for cleanup and automation
