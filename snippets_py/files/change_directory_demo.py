# 🧩 Change working directory
import os

os.chdir("/path/to/new/directory")


# 🧩 Change directory safely
import os

try:
    os.chdir("/path/to/new/directory")
    print("Directory changed successfully")
except FileNotFoundError:
    print("Directory does not exist")
except OSError as e:
    print(f"Error changing directory: {e}")


# 🧩 Change directory with validation
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


# 🧩 Change directory with context manager
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
