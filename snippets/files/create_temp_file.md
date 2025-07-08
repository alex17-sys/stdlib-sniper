# Create Temp File

Zero-dependency Python snippets for creating temporary files using the standard library.

## Simple

### 🧩 Create temporary file

```python
import tempfile

with tempfile.NamedTemporaryFile() as f:
    f.write(b"Hello, World!")
    print(f"Temp file: {f.name}")
```

📂 Create a temporary file that's automatically deleted

🏷️ Tags: file, temp, temporary, tempfile
📝 Notes:
- File is automatically deleted when closed
- Returns file object and filename
- Safe for temporary data

### 🧩 Create temporary file with suffix

```python
import tempfile

with tempfile.NamedTemporaryFile(suffix=".txt") as f:
    f.write(b"Hello, World!")
    print(f"Temp file: {f.name}")
```

📂 Create temporary file with specific file extension

🏷️ Tags: file, temp, temporary, suffix, tempfile
📝 Notes:
- Adds .txt extension to filename
- Useful for specific file types
- Helps with file identification

## Complex

### 🧩 Create temporary file with custom directory

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

📂 Create temporary file in specific directory with custom content

🏷️ Tags: file, temp, temporary, directory, custom, tempfile
📝 Notes:
- Creates directory if it doesn't exist
- Allows custom content and suffix
- Returns filename for later use
- Useful for organized temp files

### 🧩 Create temporary file with cleanup

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

📂 Create temporary files with automatic cleanup on program exit

🏷️ Tags: file, temp, temporary, cleanup, manager, atexit, tempfile
📝 Notes:
- Tracks all created temporary files
- Automatically cleans up on program exit
- Handles cleanup errors gracefully
- Useful for long-running programs

## 🔗 Cross-References

- **Reference**: See [📂 Write File](./write_file.md)
- **Reference**: See [📂 Delete File](./delete_file.md)

## 🏷️ Tags

`file`, `tempfile`, `temporary`, `create`, `delete`, `io`

## 📝 Notes

- Use tempfile module for secure temporary files
- Temporary files are deleted automatically unless specified
- Useful for intermediate data and testing
