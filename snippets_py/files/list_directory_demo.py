# 🧩 List files in directory
import os

files = os.listdir(".")
print(files)


# 🧩 List files in specific directory
import os

files = os.listdir("/path/to/directory")
for file in files:
    print(file)


# 🧩 List files with details
import os


def list_directory_detailed(directory="."):
    """List directory contents with file details."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist")
        return

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            print(f"📄 {item} ({size} bytes)")
        elif os.path.isdir(item_path):
            print(f"📁 {item}/")
        else:
            print(f"🔗 {item}")


list_directory_detailed()


# 🧩 List files with filtering
import os
import glob


def list_files_filtered(directory=".", pattern="*"):
    """List files matching specific pattern."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist")
        return []

    # Use glob for pattern matching
    pattern_path = os.path.join(directory, pattern)
    matching_files = glob.glob(pattern_path)

    # Filter out directories, keep only files
    files_only = [f for f in matching_files if os.path.isfile(f)]

    return files_only


# List only .txt files
txt_files = list_files_filtered(".", "*.txt")
print("Text files:", txt_files)

# List only .py files
py_files = list_files_filtered(".", "*.py")
print("Python files:", py_files)
