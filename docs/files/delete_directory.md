---
title: Delete Directory
description: Zero-dependency Python snippets for deleting directories using the standard library.
keywords: check, confirmation, delete, directory, empty, error-handling, os, rmdir
---

# Delete Directory

Zero-dependency Python snippets for deleting directories using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Delete empty directory

`directory` `delete` `rmdir` `os`

Delete an empty directory

```python
import os

os.rmdir("empty_directory")
```

!!! note "Notes"
    - Only works for empty directories
    - Raises OSError if directory is not empty
    - Raises OSError if directory doesn't exist

<hr class="snippet-divider">

### Delete empty directory safely

`directory` `delete` `rmdir` `error-handling` `os`

Delete empty directory with error handling

```python
import os

try:
    os.rmdir("empty_directory")
    print("Directory deleted successfully")
except FileNotFoundError:
    print("Directory does not exist")
except OSError as e:
    print(f"Error deleting directory: {e}")
```

!!! note "Notes"
    - Handles case where directory doesn't exist
    - Handles case where directory is not empty
    - Provides clear error messages
    - Safe for scripts

<hr class="snippet-divider">

## Complex

###  Delete directory if empty

`directory` `delete` `empty` `check` `rmdir` `os`

Delete directory only if it's empty

```python
import os


def delete_directory_if_empty(directory):
    """Delete directory only if it's empty."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist")
        return False

    if not os.path.isdir(directory):
        print(f"'{directory}' is not a directory")
        return False

    try:
        # Check if directory is empty
        if not os.listdir(directory):
            os.rmdir(directory)
            print(f"Deleted empty directory: {directory}")
            return True
        else:
            print(f"Directory '{directory}' is not empty")
            return False
    except OSError as e:
        print(f"Error deleting directory '{directory}': {e}")
        return False


delete_directory_if_empty("my_directory")
```

!!! note "Notes"
    - Checks if directory is empty before deleting
    - Validates directory existence and type
    - Returns success/failure status
    - Useful for cleanup operations

<hr class="snippet-divider">

### Delete directory with confirmation

`directory` `delete` `confirmation` `empty` `rmdir` `os`

Delete empty directory with user confirmation

```python
import os


def delete_directory_with_confirmation(directory):
    """Delete empty directory with user confirmation."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist")
        return False

    if not os.path.isdir(directory):
        print(f"'{directory}' is not a directory")
        return False

    # Check if directory is empty
    contents = os.listdir(directory)
    if contents:
        print(f"Directory '{directory}' contains: {contents}")
        print("Cannot delete non-empty directory")
        return False

    # Ask for confirmation
    response = input(f"Delete empty directory '{directory}'? (y/N): ")
    if response.lower() in ["y", "yes"]:
        try:
            os.rmdir(directory)
            print(f"Deleted directory: {directory}")
            return True
        except OSError as e:
            print(f"Error deleting directory: {e}")
            return False
    else:
        print("Deletion cancelled")
        return False


delete_directory_with_confirmation("temp_directory")
```

!!! note "Notes"
    - Shows directory contents if not empty
    - Asks for user confirmation
    - Handles all error cases
    - Safe for important directories

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Delete File](./delete_file.md)
- **Reference**: See [📂 Create Directory](./create_directory.md)

## 🏷️ Tags

`file`, `directory`, `delete`, `os`, `remove`, `io`

## 📝 Notes

- Use os.rmdir() to delete empty directories
- For non-empty directories, use shutil.rmtree()
- Useful for cleanup and automation
