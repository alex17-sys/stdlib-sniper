# 🧩 Write string to file
with open("file.txt", "w") as f:
    f.write("Hello, World!")


# 🧩 Write with encoding
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Hello, 世界!")


# 🧩 Write file with error handling
def write_file_safe(filename, content, encoding="utf-8"):
    """Write content to file with comprehensive error handling."""
    try:
        with open(filename, "w", encoding=encoding) as f:
            f.write(content)
        return True
    except PermissionError:
        print(f"Error: No permission to write to '{filename}'")
        return False
    except OSError as e:
        print(f"Error writing to '{filename}': {e}")
        return False


success = write_file_safe("file.txt", "Hello, World!")
if success:
    print("File written successfully")


# 🧩 Write file atomically
import os
import tempfile


def write_file_atomic(filename, content, encoding="utf-8"):
    """Write file atomically to prevent corruption."""
    temp_file = tempfile.NamedTemporaryFile(
        mode="w", encoding=encoding, delete=False, dir=os.path.dirname(filename)
    )

    try:
        temp_file.write(content)
        temp_file.close()
        os.replace(temp_file.name, filename)
        return True
    except Exception as e:
        print(f"Error writing file: {e}")
        try:
            os.unlink(temp_file.name)
        except Exception:
            pass
        return False


write_file_atomic("important.txt", "Critical data")
