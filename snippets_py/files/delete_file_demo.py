# 🧩 Delete a file
import os

os.remove("file.txt")


# 🧩 Delete file safely
import os

try:
    os.remove("file.txt")
    print("File deleted successfully")
except FileNotFoundError:
    print("File does not exist")


# 🧩 Delete file with confirmation
import os


def delete_file_safe(filename):
    """Delete file with existence check and confirmation."""
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist")
        return False

    if not os.path.isfile(filename):
        print(f"'{filename}' is not a regular file")
        return False

    # Show file info before deletion
    size = os.path.getsize(filename)
    print(f"File: {filename}")
    print(f"Size: {size} bytes")

    # Ask for confirmation
    response = input("Are you sure you want to delete this file? (y/N): ")
    if response.lower() in ["y", "yes"]:
        try:
            os.remove(filename)
            print(f"File '{filename}' deleted successfully")
            return True
        except PermissionError:
            print(f"Permission denied: cannot delete '{filename}'")
            return False
    else:
        print("Deletion cancelled")
        return False


delete_file_safe("important.txt")


# 🧩 Delete multiple files
import os
import glob


def delete_files_pattern(pattern):
    """Delete multiple files matching a pattern."""
    files = glob.glob(pattern)
    if not files:
        print(f"No files found matching '{pattern}'")
        return

    print(f"Found {len(files)} files:")
    for file in files:
        print(f"  - {file}")

    response = input("Delete all these files? (y/N): ")
    if response.lower() in ["y", "yes"]:
        deleted_count = 0
        for file in files:
            try:
                os.remove(file)
                print(f"Deleted: {file}")
                deleted_count += 1
            except OSError as e:
                print(f"Error deleting {file}: {e}")

        print(f"Successfully deleted {deleted_count} files")
    else:
        print("Deletion cancelled")


# Delete all .tmp files
delete_files_pattern("*.tmp")
