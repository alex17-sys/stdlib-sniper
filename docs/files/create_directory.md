---
title: Create Directory
description: Zero-dependency Python snippets for creating directories using the standard library.
keywords: check, create, directory, error-handling, exists, mkdir, mode, os, permissions, stat
---

# Create Directory

Zero-dependency Python snippets for creating directories using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Create single directory

`directory` `create` `mkdir` `os`

Create a single directory

```python
import os

os.mkdir("new_directory")
```

!!! note "Notes"
    - Creates one directory level
    - Raises OSError if directory exists
    - Raises OSError if parent doesn't exist

<hr class="snippet-divider">

### Create directory safely

`directory` `create` `mkdir` `error-handling` `os`

Create directory with error handling

```python
import os

try:
    os.mkdir("new_directory")
    print("Directory created successfully")
except FileExistsError:
    print("Directory already exists")
except OSError as e:
    print(f"Error creating directory: {e}")
```

!!! note "Notes"
    - Handles case where directory exists
    - Provides clear error messages
    - Safe for scripts that may run multiple times

<hr class="snippet-divider">

## Complex

###  Create directory if not exists

`directory` `create` `exists` `check` `os`

Create directory only if it doesn't already exist

```python
import os


def create_directory_if_not_exists(directory):
    """Create directory only if it doesn't exist."""
    if not os.path.exists(directory):
        try:
            os.mkdir(directory)
            print(f"Directory '{directory}' created successfully")
            return True
        except OSError as e:
            print(f"Error creating directory '{directory}': {e}")
            return False
    else:
        print(f"Directory '{directory}' already exists")
        return True


create_directory_if_not_exists("my_directory")
```

!!! note "Notes"
    - Checks existence before creating
    - Prevents errors from existing directories
    - Returns success/failure status
    - Useful for setup scripts

<hr class="snippet-divider">

### Create directory with permissions

`directory` `create` `permissions` `mode` `stat` `os`

Create directory with specific file permissions

```python
import os


def create_directory_with_permissions(directory, mode=0o755):
    """Create directory with specific permissions."""
    try:
        os.mkdir(directory, mode)
        print(f"Directory '{directory}' created with permissions {oct(mode)}")
        return True
    except FileExistsError:
        print(f"Directory '{directory}' already exists")
        return True
    except OSError as e:
        print(f"Error creating directory '{directory}': {e}")
        return False


# Create directory with read/write/execute for owner, read/execute for others
create_directory_with_permissions("secure_dir", 0o755)

# Create directory with read/write for owner only
create_directory_with_permissions("private_dir", 0o700)
```

!!! note "Notes"
    - Sets specific file permissions
    - 0o755 = rwxr-xr-x (common for directories)
    - 0o700 = rwx------ (private directory)
    - Useful for security-conscious applications

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Directory Exists](./directory_exists.md)
- **Reference**: See [📂 Create Nested Directories](./create_nested_directories.md)

## 🏷️ Tags

`file`, `directory`, `create`, `os`, `mkdir`, `io`

## 📝 Notes

- Use os.mkdir() to create a single directory
- Use os.makedirs() for nested directories
- Useful for setup and automation
