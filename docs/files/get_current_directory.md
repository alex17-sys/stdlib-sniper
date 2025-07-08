# Get Current Directory

Zero-dependency Python snippets using only the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Get current working directory

`directory` `current` `working` `getcwd` `os`

Get the current working directory path

```python
import os

current_dir = os.getcwd()
print(current_dir)
```

!!! note "Notes"
    - Returns absolute path to current directory
    - Returns string path
    - Useful for relative path operations

<hr class="snippet-divider">

### Get current directory safely

`directory` `current` `working` `getcwd` `error-handling` `os`

Get current working directory with error handling

```python
import os

try:
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")
except OSError as e:
    print(f"Error getting current directory: {e}")
```

!!! note "Notes"
    - Handles rare cases where directory is inaccessible
    - Provides clear error messages
    - Safe for all environments

<hr class="snippet-divider">

## Complex

###  Get current directory with validation

`directory` `current` `working` `validation` `permissions` `getcwd` `os`

Get current directory with existence and permission validation

```python
import os


def get_current_directory_validated():
    """Get current directory with existence validation."""
    try:
        current_dir = os.getcwd()

        # Validate that the directory still exists
        if not os.path.exists(current_dir):
            print(f"Warning: Current directory '{current_dir}' no longer exists")
            return None

        # Check if we have read permissions
        if not os.access(current_dir, os.R_OK):
            print(f"Warning: No read access to current directory '{current_dir}'")
            return None

        return current_dir
    except OSError as e:
        print(f"Error getting current directory: {e}")
        return None


current_dir = get_current_directory_validated()
if current_dir:
    print(f"Current directory: {current_dir}")
```

!!! note "Notes"
    - Validates directory still exists
    - Checks read permissions
    - Returns None on validation failure
    - Useful for robust applications

<hr class="snippet-divider">

### Get current directory with path analysis

`directory` `current` `working` `analysis` `path` `components` `getcwd` `os`

Get current directory with comprehensive path analysis

```python
import os


def analyze_current_directory():
    """Get current directory with detailed path analysis."""
    try:
        current_dir = os.getcwd()

        # Get path components
        path_parts = current_dir.split(os.sep)

        # Get directory info
        dir_info = {
            "full_path": current_dir,
            "basename": os.path.basename(current_dir),
            "dirname": os.path.dirname(current_dir),
            "depth": len([p for p in path_parts if p]),
            "is_root": current_dir == os.sep or (os.name == "nt" and len(current_dir) <= 3),
            "exists": os.path.exists(current_dir),
            "readable": os.access(current_dir, os.R_OK),
            "writable": os.access(current_dir, os.W_OK),
        }

        return dir_info
    except OSError as e:
        print(f"Error analyzing current directory: {e}")
        return None


info = analyze_current_directory()
if info:
    print(f"Current directory: {info['full_path']}")
    print(f"Directory name: {info['basename']}")
    print(f"Parent directory: {info['dirname']}")
    print(f"Path depth: {info['depth']}")
    print(f"Is root: {info['is_root']}")
    print(f"Readable: {info['readable']}")
    print(f"Writable: {info['writable']}")
```

!!! note "Notes"
    - Provides detailed path information
    - Analyzes permissions and existence
    - Cross-platform compatible
    - Useful for path manipulation

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Change Directory](./change_directory.md)
- **Reference**: See [📂 List Directory](./list_directory.md)

## 🏷️ Tags

`file`, `directory`, `cwd`, `os`, `get`, `io`

## 📝 Notes

- Use os.getcwd() to get the current working directory
- Useful for relative file operations and scripts
- Related: changing and listing directories
