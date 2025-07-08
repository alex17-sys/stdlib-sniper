# 🧩 Delete empty directory
import os

os.rmdir("empty_directory")


# 🧩 Delete empty directory safely
import os

try:
    os.rmdir("empty_directory")
    print("Directory deleted successfully")
except FileNotFoundError:
    print("Directory does not exist")
except OSError as e:
    print(f"Error deleting directory: {e}")


# 🧩 Delete directory if empty
import os


def delete_directory_if_empty(directory):
    """Delete directory only if it's empty."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist")
        return False

    if not os.path.isdir(directory):
        print(f"'{directory}' is not a directory")
        return False

    try:
        # Check if directory is empty
        if not os.listdir(directory):
            os.rmdir(directory)
            print(f"Deleted empty directory: {directory}")
            return True
        else:
            print(f"Directory '{directory}' is not empty")
            return False
    except OSError as e:
        print(f"Error deleting directory '{directory}': {e}")
        return False


delete_directory_if_empty("my_directory")


# 🧩 Delete directory with confirmation
import os


def delete_directory_with_confirmation(directory):
    """Delete empty directory with user confirmation."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist")
        return False

    if not os.path.isdir(directory):
        print(f"'{directory}' is not a directory")
        return False

    # Check if directory is empty
    contents = os.listdir(directory)
    if contents:
        print(f"Directory '{directory}' contains: {contents}")
        print("Cannot delete non-empty directory")
        return False

    # Ask for confirmation
    response = input(f"Delete empty directory '{directory}'? (y/N): ")
    if response.lower() in ["y", "yes"]:
        try:
            os.rmdir(directory)
            print(f"Deleted directory: {directory}")
            return True
        except OSError as e:
            print(f"Error deleting directory: {e}")
            return False
    else:
        print("Deletion cancelled")
        return False


delete_directory_with_confirmation("temp_directory")
