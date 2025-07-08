# 🧩 Create temporary file
import tempfile

with tempfile.NamedTemporaryFile() as f:
    f.write(b"Hello, World!")
    print(f"Temp file: {f.name}")


# 🧩 Create temporary file with suffix
import tempfile

with tempfile.NamedTemporaryFile(suffix=".txt") as f:
    f.write(b"Hello, World!")
    print(f"Temp file: {f.name}")


# 🧩 Create temporary file with custom directory
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


# 🧩 Create temporary file with cleanup
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
