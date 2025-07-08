# 🧩 Get file size in bytes
import os

size = os.path.getsize("file.txt")
print(f"File size: {size} bytes")


# 🧩 Get file size safely
import os

try:
    size = os.path.getsize("file.txt")
    print(f"File size: {size} bytes")
except FileNotFoundError:
    print("File does not exist")


# 🧩 Get file size in human readable format
import os


def get_file_size_human(filename):
    """Get file size in human readable format."""
    if not os.path.exists(filename):
        return "File does not exist"

    size_bytes = os.path.getsize(filename)

    # Convert to appropriate unit
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0

    return f"{size_bytes:.1f} PB"


size = get_file_size_human("large_file.txt")
print(f"File size: {size}")


# 🧩 Get directory size recursively
import os


def get_directory_size(directory):
    """Calculate total size of directory and all subdirectories."""
    total_size = 0
    file_count = 0

    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                total_size += os.path.getsize(filepath)
                file_count += 1
            except (OSError, FileNotFoundError):
                # Skip files that can't be accessed
                continue

    return total_size, file_count


size_bytes, count = get_directory_size("/path/to/directory")
print(f"Directory contains {count} files")
print(f"Total size: {size_bytes:,} bytes")
