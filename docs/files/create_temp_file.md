# Create Temp File

Zero-dependency Python snippets using only the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Create temporary file

`file` `temp` `temporary` `tempfile`

Create a temporary file that's automatically deleted

```python
import tempfile

with tempfile.NamedTemporaryFile() as f:
    f.write(b"Hello, World!")
    print(f"Temp file: {f.name}")
```

!!! note "Notes"
    - File is automatically deleted when closed
    - Returns file object and filename
    - Safe for temporary data

<hr class="snippet-divider">

### Create temporary file with suffix

`file` `temp` `temporary` `suffix` `tempfile`

Create temporary file with specific file extension

```python
import tempfile

with tempfile.NamedTemporaryFile(suffix=".txt") as f:
    f.write(b"Hello, World!")
    print(f"Temp file: {f.name}")
```

!!! note "Notes"
    - Adds .txt extension to filename
    - Useful for specific file types
    - Helps with file identification

<hr class="snippet-divider">

## Complex

###  Create temporary file with custom directory

`file` `temp` `temporary` `directory` `custom` `tempfile`

Create temporary file in specific directory with custom content

```python
import tempfile
import os


def create_temp_file_in_dir(directory, content, suffix=""):
    """Create temporary file in specific directory."""
    if not os.path.exists(directory):
        os.makedirs(directory)

    with tempfile.NamedTemporaryFile(mode="w", dir=directory, suffix=suffix, delete=False) as f:
        f.write(content)
        return f.name


temp_file = create_temp_file_in_dir("/tmp/my_temp", "Hello, World!", ".txt")
print(f"Created: {temp_file}")
```

!!! note "Notes"
    - Creates directory if it doesn't exist
    - Allows custom content and suffix
    - Returns filename for later use
    - Useful for organized temp files

<hr class="snippet-divider">

### Create temporary file with cleanup

`file` `temp` `temporary` `cleanup` `manager` `atexit` `tempfile`

Create temporary files with automatic cleanup on program exit

```python
import tempfile
import os
import atexit


class TempFileManager:
    """Manage temporary files with automatic cleanup."""

    def __init__(self):
        self.temp_files = []
        atexit.register(self.cleanup)

    def create_temp_file(self, content="", suffix=""):
        """Create temporary file and track it for cleanup."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=suffix, delete=False) as f:
            f.write(content)
            self.temp_files.append(f.name)
            return f.name

    def cleanup(self):
        """Remove all tracked temporary files."""
        for temp_file in self.temp_files:
            try:
                if os.path.exists(temp_file):
                    os.unlink(temp_file)
                    print(f"Cleaned up: {temp_file}")
            except OSError as e:
                print(f"Error cleaning up {temp_file}: {e}")


# Usage
temp_manager = TempFileManager()
file1 = temp_manager.create_temp_file("Data 1", ".txt")
file2 = temp_manager.create_temp_file("Data 2", ".log")
print(f"Created: {file1}, {file2}")
# Files will be automatically cleaned up when program exits
```

!!! note "Notes"
    - Tracks all created temporary files
    - Automatically cleans up on program exit
    - Handles cleanup errors gracefully
    - Useful for long-running programs

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Write File](./write_file.md)
- **Reference**: See [📂 Delete File](./delete_file.md)

## 🏷️ Tags

`file`, `tempfile`, `temporary`, `create`, `delete`, `io`

## 📝 Notes

- Use tempfile module for secure temporary files
- Temporary files are deleted automatically unless specified
- Useful for intermediate data and testing
