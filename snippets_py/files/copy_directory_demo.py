# 🧩 Copy directory tree
import shutil

shutil.copytree("source_directory", "destination_directory")


# 🧩 Copy directory safely
import shutil

try:
    shutil.copytree("source_directory", "destination_directory")
    print("Directory copied successfully")
except FileExistsError:
    print("Destination directory already exists")
except OSError as e:
    print(f"Error copying directory: {e}")


# 🧩 Copy directory with overwrite
import shutil
import os


def copy_directory_with_overwrite(src, dst):
    """Copy directory tree with overwrite option."""
    if not os.path.exists(src):
        print(f"Source directory '{src}' does not exist")
        return False

    if not os.path.isdir(src):
        print(f"'{src}' is not a directory")
        return False

    # Remove destination if it exists
    if os.path.exists(dst):
        try:
            shutil.rmtree(dst)
            print(f"Removed existing destination: {dst}")
        except OSError as e:
            print(f"Error removing existing destination: {e}")
            return False

    # Copy the directory
    try:
        shutil.copytree(src, dst)
        print(f"Directory copied successfully: {src} -> {dst}")
        return True
    except OSError as e:
        print(f"Error copying directory: {e}")
        return False


copy_directory_with_overwrite("source_project", "backup_project")


# 🧩 Copy directory with filtering
import shutil
import os


def copy_directory_filtered(src, dst, ignore_patterns=None):
    """Copy directory tree with file filtering."""
    if not os.path.exists(src):
        print(f"Source directory '{src}' does not exist")
        return False

    # Default ignore patterns
    if ignore_patterns is None:
        ignore_patterns = ["__pycache__", "*.pyc", ".git", ".DS_Store"]

    def ignore_func(dir, files):
        """Filter function for shutil.copytree."""
        ignored = []
        for file in files:
            for pattern in ignore_patterns:
                if pattern in file or file.endswith(pattern.replace("*", "")):
                    ignored.append(file)
                    break
        return ignored

    try:
        shutil.copytree(src, dst, ignore=ignore_func)
        print(f"Directory copied with filtering: {src} -> {dst}")
        return True
    except OSError as e:
        print(f"Error copying directory: {e}")
        return False


# Copy directory excluding common unwanted files
copy_directory_filtered("source_project", "clean_backup")
