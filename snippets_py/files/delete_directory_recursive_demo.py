# 🧩 Delete directory and contents with shutil
import shutil

shutil.rmtree("directory_to_delete")


# 🧩 Delete directory safely
import shutil

try:
    shutil.rmtree("directory_to_delete")
    print("Directory and contents deleted successfully")
except FileNotFoundError:
    print("Directory does not exist")
except OSError as e:
    print(f"Error deleting directory: {e}")


# 🧩 Delete directory with confirmation
import shutil
import os


def delete_directory_recursive_with_confirmation(directory):
    """Delete directory and contents with user confirmation."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist")
        return False

    if not os.path.isdir(directory):
        print(f"'{directory}' is not a directory")
        return False

    # Count files and directories
    file_count = 0
    dir_count = 0

    for root, dirs, files in os.walk(directory):
        file_count += len(files)
        dir_count += len(dirs)

    print(f"Directory '{directory}' contains:")
    print(f"  - {file_count} files")
    print(f"  - {dir_count} directories")

    # Ask for confirmation
    response = input(f"Delete directory '{directory}' and all contents? (y/N): ")
    if response.lower() in ["y", "yes"]:
        try:
            shutil.rmtree(directory)
            print(f"Deleted directory and all contents: {directory}")
            return True
        except OSError as e:
            print(f"Error deleting directory: {e}")
            return False
    else:
        print("Deletion cancelled")
        return False


delete_directory_recursive_with_confirmation("temp_project")


# 🧩 Delete directory with backup
import shutil
import os
from datetime import datetime


def delete_directory_with_backup(directory, backup_dir=None):
    """Delete directory with optional backup."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist")
        return False

    if not os.path.isdir(directory):
        print(f"'{directory}' is not a directory")
        return False

    # Create backup if requested
    if backup_dir:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{os.path.basename(directory)}_{timestamp}"
        backup_path = os.path.join(backup_dir, backup_name)

        try:
            shutil.copytree(directory, backup_path)
            print(f"Created backup: {backup_path}")
        except OSError as e:
            print(f"Error creating backup: {e}")
            return False

    # Delete the directory
    try:
        shutil.rmtree(directory)
        print(f"Deleted directory: {directory}")
        return True
    except OSError as e:
        print(f"Error deleting directory: {e}")
        return False


# Delete with backup
delete_directory_with_backup("old_project", "/backups")
