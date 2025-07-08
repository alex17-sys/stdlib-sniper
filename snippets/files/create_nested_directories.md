# Create Nested Directories

Zero-dependency Python snippets for creating nested directories using the standard library.

## Simple

### 🧩 Create nested directories

```python
import os

os.makedirs("parent/child/grandchild")
```

📂 Create nested directory structure

🏷️ Tags: directory, create, nested, makedirs, os
📝 Notes:
- Creates all parent directories as needed
- Raises OSError if any directory exists
- Creates complete path in one operation

### 🧩 Create nested directories safely

```python
import os

try:
    os.makedirs("parent/child/grandchild")
    print("Nested directories created successfully")
except FileExistsError:
    print("Some directories already exist")
except OSError as e:
    print(f"Error creating directories: {e}")
```

📂 Create nested directories with error handling

🏷️ Tags: directory, create, nested, makedirs, error-handling, os
📝 Notes:
- Handles case where directories exist
- Provides clear error messages
- Safe for scripts that may run multiple times

## Complex

### 🧩 Create nested directories if not exist

```python
import os


def create_nested_directories_if_not_exist(directory_path):
    """Create nested directories only if they don't exist."""
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
            print(f"Created directory structure: {directory_path}")
            return True
        except OSError as e:
            print(f"Error creating directories '{directory_path}': {e}")
            return False
    else:
        print(f"Directory structure already exists: {directory_path}")
        return True


create_nested_directories_if_not_exist("projects/python/utils")
```

📂 Create nested directories only if they don't already exist

🏷️ Tags: directory, create, nested, exists, check, makedirs, os
📝 Notes:
- Checks existence before creating
- Prevents errors from existing directories
- Returns success/failure status
- Useful for project setup

### 🧩 Create nested directories with custom permissions

```python
import os


def create_nested_directories_with_permissions(directory_path, mode=0o755):
    """Create nested directories with specific permissions."""
    if os.path.exists(directory_path):
        print(f"Directory structure already exists: {directory_path}")
        return True

    try:
        # Create directories with specified permissions
        os.makedirs(directory_path, mode=mode)
        print(f"Created directory structure: {directory_path}")
        print(f"Permissions: {oct(mode)}")
        return True
    except OSError as e:
        print(f"Error creating directories '{directory_path}': {e}")
        return False


# Create nested directories with restrictive permissions
create_nested_directories_with_permissions("private/data/logs", 0o700)
```

📂 Create nested directories with specific file permissions

🏷️ Tags: directory, create, nested, permissions, mode, makedirs, os
📝 Notes:
- Sets permissions for all created directories
- 0o700 = rwx------ (private)
- 0o755 = rwxr-xr-x (standard)

## 🔗 Cross Reference

- **Reference**: See [📂 Copy Directory](copy_directory.md)
- **Reference**: See [📂 Move File](move_file.md)

## 🏷️ Tags

`directory`, `create`, `nested`, `makedirs`, `exists`, `check`, `permissions`, `mode`, `error-handling`, `os`

## 📝 Notes
- Use os.makedirs for recursive directory creation
- Handle errors and permissions as needed
- Useful for project setup and automation
