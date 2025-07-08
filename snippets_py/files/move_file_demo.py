# 🧩 Move/rename file
import shutil

shutil.move("old_name.txt", "new_name.txt")


# 🧩 Move file with os.rename
import os

os.rename("old_name.txt", "new_name.txt")


# 🧩 Move file with backup
import shutil
import os
from datetime import datetime


def move_file_with_backup(src, dst):
    """Move file with automatic backup if destination exists."""
    if not os.path.exists(src):
        print(f"Source file '{src}' does not exist")
        return False

    if os.path.exists(dst):
        # Create backup with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{dst}.backup_{timestamp}"
        shutil.move(dst, backup_name)
        print(f"Created backup: {backup_name}")

    try:
        shutil.move(src, dst)
        print(f"File moved successfully: {src} -> {dst}")
        return True
    except Exception as e:
        print(f"Error moving file: {e}")
        return False


move_file_with_backup("source.txt", "destination.txt")


# 🧩 Move file with validation
import shutil
import os


def move_file_validated(src, dst):
    """Move file with source validation and destination confirmation."""
    # Validate source
    if not os.path.exists(src):
        print(f"Source file '{src}' does not exist")
        return False

    if not os.path.isfile(src):
        print(f"'{src}' is not a regular file")
        return False

    # Check destination
    if os.path.exists(dst):
        if os.path.isdir(dst):
            # If destination is directory, append filename
            dst = os.path.join(dst, os.path.basename(src))

        if os.path.exists(dst):
            response = input(f"'{dst}' already exists. Overwrite? (y/N): ")
            if response.lower() not in ["y", "yes"]:
                print("Move cancelled")
                return False

    # Perform move
    try:
        shutil.move(src, dst)
        print(f"File moved successfully: {src} -> {dst}")
        return True
    except Exception as e:
        print(f"Error moving file: {e}")
        return False


move_file_validated("source.txt", "destination.txt")
