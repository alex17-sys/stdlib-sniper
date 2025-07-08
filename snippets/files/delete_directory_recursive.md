# Delete Directory Recursive

Zero-dependency Python snippets for deleting directories and their contents recursively using the standard library.

## Simple

### 🧩 Delete directory and contents with shutil

```python
import shutil

shutil.rmtree("directory_to_delete")
```

📂 Delete directory and all its contents recursively

🏷️ Tags: directory, delete, recursive, rmtree, shutil
📝 Notes:
- Deletes directory and all subdirectories
- Deletes all files within the directory tree
- Raises OSError if directory doesn't exist
- Use with caution - permanent deletion

### 🧩 Delete directory safely

```python
import shutil

try:
    shutil.rmtree("directory_to_delete")
    print("Directory and contents deleted successfully")
except FileNotFoundError:
    print("Directory does not exist")
except OSError as e:
    print(f"Error deleting directory: {e}")
```

📂 Delete directory recursively with error handling

🏷️ Tags: directory, delete, recursive, rmtree, error-handling, shutil
📝 Notes:
- Handles case where directory doesn't exist
- Provides clear error messages
- Safe for scripts that may run multiple times

## Complex

### 🧩 Delete directory with confirmation

```python
import shutil
import os


def delete_directory_recursive_with_confirmation(directory):
    """Delete directory and contents with user confirmation."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist")
        return False

    if not os.path.isdir(directory):
        print(f"'{directory}' is not a directory")
        return False

    # Count files and directories
    file_count = 0
    dir_count = 0

    for root, dirs, files in os.walk(directory):
        file_count += len(files)
        dir_count += len(dirs)

    print(f"Directory '{directory}' contains:")
    print(f"  - {file_count} files")
    print(f"  - {dir_count} directories")

    # Ask for confirmation
    response = input(f"Delete directory '{directory}' and all contents? (y/N): ")
    if response.lower() in ["y", "yes"]:
        try:
            shutil.rmtree(directory)
            print(f"Deleted directory and all contents: {directory}")
            return True
        except OSError as e:
            print(f"Error deleting directory: {e}")
            return False
    else:
        print("Deletion cancelled")
        return False


delete_directory_recursive_with_confirmation("temp_project")
```

📂 Delete directory recursively with confirmation and file count

🏷️ Tags: directory, delete, recursive, confirmation, count, rmtree, shutil
📝 Notes:
- Shows file and directory count before deletion
- Asks for user confirmation
- Provides detailed information
- Safe for important directories

### 🧩 Delete directory with backup

```python
import shutil
import os
from datetime import datetime


def delete_directory_with_backup(directory, backup_dir=None):
    """Delete directory with optional backup."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist")
        return False

    if not os.path.isdir(directory):
        print(f"'{directory}' is not a directory")
        return False

    # Create backup if requested
    if backup_dir:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{os.path.basename(directory)}_{timestamp}"
        backup_path = os.path.join(backup_dir, backup_name)

        try:
            shutil.copytree(directory, backup_path)
            print(f"Created backup: {backup_path}")
        except OSError as e:
            print(f"Error creating backup: {e}")
            return False

    # Delete the directory
    try:
        shutil.rmtree(directory)
        print(f"Deleted directory: {directory}")
        return True
    except OSError as e:
        print(f"Error deleting directory: {e}")
        return False


# Delete with backup
delete_directory_with_backup("old_project", "/backups")
```

📂 Delete directory recursively with optional backup

🏷️ Tags: directory, delete, recursive, backup, timestamp, rmtree, shutil
📝 Notes:
- Creates timestamped backup before deletion
- Preserves data in backup location
- Handles backup and deletion errors
- Useful for safe cleanup operations

## 🔗 Cross-References

- **Reference**: See [📂 Delete Directory](./delete_directory.md)
- **Reference**: See [📂 List Directory Recursive](./list_directory_recursive.md)

## 🏷️ Tags

`file`, `directory`, `delete`, `recursive`, `shutil`, `os`, `io`

## 📝 Notes

- Use shutil.rmtree() to delete non-empty directories
- Useful for cleanup and automation
- Always use with caution to avoid data loss
