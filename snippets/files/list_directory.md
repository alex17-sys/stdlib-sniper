# List Directory

Zero-dependency Python snippets for listing directory contents using the standard library.

## Simple

### 🧩 List files in directory

```python
import os

files = os.listdir(".")
print(files)
```

📂 List all files and directories in current directory

🏷️ Tags: directory, list, file, os
📝 Notes:
- Returns list of filenames
- Includes both files and directories
- Uses current directory ('.') by default

### 🧩 List files in specific directory

```python
import os

files = os.listdir("/path/to/directory")
for file in files:
    print(file)
```

📂 List all files and directories in specific directory

🏷️ Tags: directory, list, file, path, os
📝 Notes:
- Specify full path to directory
- Raises OSError if directory doesn't exist
- Returns relative filenames only

## Complex

### 🧩 List files with details

```python
import os


def list_directory_detailed(directory="."):
    """List directory contents with file details."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist")
        return

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            print(f"📄 {item} ({size} bytes)")
        elif os.path.isdir(item_path):
            print(f"📁 {item}/")
        else:
            print(f"🔗 {item}")


list_directory_detailed()
```

📂 List directory contents with file types and sizes

🏷️ Tags: directory, list, details, file-types, size, os
📝 Notes:
- Distinguishes between files and directories
- Shows file sizes for regular files
- Uses emojis for visual clarity
- Handles non-existent directories

### 🧩 List files with filtering

```python
import os
import glob


def list_files_filtered(directory=".", pattern="*"):
    """List files matching specific pattern."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist")
        return []

    # Use glob for pattern matching
    pattern_path = os.path.join(directory, pattern)
    matching_files = glob.glob(pattern_path)

    # Filter out directories, keep only files
    files_only = [f for f in matching_files if os.path.isfile(f)]

    return files_only


# List only .txt files
txt_files = list_files_filtered(".", "*.txt")
print("Text files:", txt_files)

# List only .py files
py_files = list_files_filtered(".", "*.py")
print("Python files:", py_files)
```

📂 List files matching specific patterns (extensions, names)

🏷️ Tags: directory, list, filter, pattern, glob, os
📝 Notes:
- Uses glob patterns for filtering
- Supports wildcards and extensions
- Returns only regular files
- Useful for specific file types

## 🔗 Cross-References

- **Reference**: See [📂 List Directory Recursive](./list_directory_recursive.md)
- **Reference**: See [📂 Directory Exists](./directory_exists.md)

## 🏷️ Tags

`file`, `directory`, `list`, `os`, `io`

## 📝 Notes

- Use os.listdir() to list files and directories
- Returns names in the given directory
- Useful for file management and automation
