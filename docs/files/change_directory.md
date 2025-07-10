---
title: Change Directory
description: Zero-dependency Python snippets for changing the working directory using the standard library.
keywords: change, chdir, context-manager, directory, error-handling, os, permissions, temporary, validation
---

# Change Directory

Zero-dependency Python snippets for changing the working directory using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Change working directory

`directory` `change` `chdir` `os`

Change the current working directory

```python
import os

os.chdir("/path/to/new/directory")
```

!!! note "Notes"
    - Changes current working directory
    - Raises OSError if directory doesn't exist
    - Affects all subsequent relative path operations

<hr class="snippet-divider">

### Change directory safely

`directory` `change` `chdir` `error-handling` `os`

Change working directory with error handling

```python
import os

try:
    os.chdir("/path/to/new/directory")
    print("Directory changed successfully")
except FileNotFoundError:
    print("Directory does not exist")
except OSError as e:
    print(f"Error changing directory: {e}")
```

!!! note "Notes"
    - Handles case where directory doesn't exist
    - Provides clear error messages
    - Safe for scripts

<hr class="snippet-divider">

## Complex

###  Change directory with validation

`directory` `change` `chdir` `validation` `permissions` `os`

Change directory with comprehensive validation

```python
import os


def change_directory_safe(directory):
    """Change directory with existence and permission validation."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist")
        return False

    if not os.path.isdir(directory):
        print(f"'{directory}' is not a directory")
        return False

    if not os.access(directory, os.R_OK | os.X_OK):
        print(f"No access to directory '{directory}'")
        return False

    try:
        old_dir = os.getcwd()
        os.chdir(directory)
        new_dir = os.getcwd()
        print(f"Changed directory: {old_dir} -> {new_dir}")
        return True
    except OSError as e:
        print(f"Error changing directory: {e}")
        return False


change_directory_safe("/path/to/new/directory")
```

!!! note "Notes"
    - Validates directory existence and type
    - Checks read and execute permissions
    - Shows before/after directory paths
    - Returns success/failure status

<hr class="snippet-divider">

### Change directory with context manager

`directory` `change` `chdir` `context-manager` `temporary` `os`

Change directory temporarily using context manager

```python
import os
from contextlib import contextmanager


@contextmanager
def change_directory(directory):
    """Context manager for temporarily changing directory."""
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist")

    if not os.path.isdir(directory):
        raise NotADirectoryError(f"'{directory}' is not a directory")

    original_dir = os.getcwd()
    try:
        os.chdir(directory)
        yield
    finally:
        os.chdir(original_dir)


# Use as context manager
with change_directory("/path/to/project"):
    print(f"Working in: {os.getcwd()}")
    # Do work in the new directory
    files = os.listdir(".")
    print(f"Files: {files}")
# Automatically returns to original directory
print(f"Back in: {os.getcwd()}")
```

!!! note "Notes"
    - Automatically returns to original directory
    - Safe for temporary directory changes
    - Handles errors gracefully
    - Useful for operations in specific directories

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Get Current Directory](./get_current_directory.md)
- **Reference**: See [📂 Directory Exists](./directory_exists.md)

## 🏷️ Tags

`file`, `directory`, `change`, `os`, `chdir`, `io`

## 📝 Notes

- Use os.chdir() to change the current working directory
- Always check if the directory exists before changing
- Useful for scripts and automation
