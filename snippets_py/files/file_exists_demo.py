# 🧩 Check if file exists
import os

if os.path.exists("file.txt"):
    print("File exists")
else:
    print("File does not exist")


# 🧩 Check if file is a regular file
import os

if os.path.isfile("file.txt"):
    print("It is a regular file")
else:
    print("Not a regular file")


# 🧩 Check file with multiple conditions
import os


def check_file_status(filename):
    """Check file existence and type with detailed status."""
    if not os.path.exists(filename):
        return "File does not exist"

    if os.path.isfile(filename):
        size = os.path.getsize(filename)
        return f"Regular file, size: {size} bytes"

    if os.path.isdir(filename):
        return "It is a directory"

    if os.path.islink(filename):
        return "It is a symbolic link"

    return "Unknown file type"


status = check_file_status("file.txt")
print(status)


# 🧩 Check file with permissions
import os


def check_file_access(filename):
    """Check file existence and access permissions."""
    if not os.path.exists(filename):
        return "File does not exist"

    checks = []

    # Check read permission
    if os.access(filename, os.R_OK):
        checks.append("readable")
    else:
        checks.append("not readable")

    # Check write permission
    if os.access(filename, os.W_OK):
        checks.append("writable")
    else:
        checks.append("not writable")

    # Check execute permission
    if os.access(filename, os.X_OK):
        checks.append("executable")
    else:
        checks.append("not executable")

    return f"File exists: {', '.join(checks)}"


access = check_file_access("file.txt")
print(access)
