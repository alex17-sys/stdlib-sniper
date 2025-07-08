# Get File Size

Zero-dependency Python snippets for getting file sizes using the standard library.

## Simple

### 🧩 Get file size in bytes

```python
import os

size = os.path.getsize("file.txt")
print(f"File size: {size} bytes")
```

📂 Get the size of a file in bytes

🏷️ Tags: file, size, bytes, os
📝 Notes:
- Returns size in bytes
- Raises OSError if file doesn't exist
- Works for any file type

### 🧩 Get file size safely

```python
import os

try:
    size = os.path.getsize("file.txt")
    print(f"File size: {size} bytes")
except FileNotFoundError:
    print("File does not exist")
```

📂 Get file size with error handling

🏷️ Tags: file, size, error-handling, os
📝 Notes:
- Handles case where file doesn't exist
- Provides clear error message
- Safe for scripts

## Complex

### 🧩 Get file size in human readable format

```python
import os


def get_file_size_human(filename):
    """Get file size in human readable format."""
    if not os.path.exists(filename):
        return "File does not exist"

    size_bytes = os.path.getsize(filename)

    # Convert to appropriate unit
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0

    return f"{size_bytes:.1f} PB"


size = get_file_size_human("large_file.txt")
print(f"File size: {size}")
```

📂 Get file size in human readable format (B, KB, MB, etc.)

🏷️ Tags: file, size, human-readable, format, os
📝 Notes:
- Automatically converts to appropriate unit
- Handles files up to petabytes
- Easy to read and understand
- Useful for user interfaces

### 🧩 Get directory size recursively

```python
import os


def get_directory_size(directory):
    """Calculate total size of directory and all subdirectories."""
    total_size = 0
    file_count = 0

    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                total_size += os.path.getsize(filepath)
                file_count += 1
            except (OSError, FileNotFoundError):
                # Skip files that can't be accessed
                continue

    return total_size, file_count


size_bytes, count = get_directory_size("/path/to/directory")
print(f"Directory contains {count} files")
print(f"Total size: {size_bytes:,} bytes")
```

📂 Calculate total size of directory and all subdirectories

🏷️ Tags: file, size, directory, recursive, walk, os
📝 Notes:
- Walks through all subdirectories
- Counts total files and size
- Handles permission errors gracefully

## 🔗 Cross Reference

- **Reference**: See [📂 List Files](get_current_directory.md)
- **Reference**: See [📂 File Exists](file_exists.md)

## 🏷️ Tags

`file`, `size`, `bytes`, `error-handling`, `human-readable`, `format`, `directory`, `recursive`, `walk`, `os`

## 📝 Notes
- Returns size in bytes or human-readable units
- Handles missing files and permission errors
- Useful for scripts, reporting, and user interfaces
