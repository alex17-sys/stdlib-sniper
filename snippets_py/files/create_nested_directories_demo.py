# 🧩 Create nested directories
import os

os.makedirs("parent/child/grandchild")


# 🧩 Create nested directories safely
import os

try:
    os.makedirs("parent/child/grandchild")
    print("Nested directories created successfully")
except FileExistsError:
    print("Some directories already exist")
except OSError as e:
    print(f"Error creating directories: {e}")


# 🧩 Create nested directories if not exist
import os


def create_nested_directories_if_not_exist(directory_path):
    """Create nested directories only if they don't exist."""
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
            print(f"Created directory structure: {directory_path}")
            return True
        except OSError as e:
            print(f"Error creating directories '{directory_path}': {e}")
            return False
    else:
        print(f"Directory structure already exists: {directory_path}")
        return True


create_nested_directories_if_not_exist("projects/python/utils")


# 🧩 Create nested directories with custom permissions
import os


def create_nested_directories_with_permissions(directory_path, mode=0o755):
    """Create nested directories with specific permissions."""
    if os.path.exists(directory_path):
        print(f"Directory structure already exists: {directory_path}")
        return True

    try:
        # Create directories with specified permissions
        os.makedirs(directory_path, mode=mode)
        print(f"Created directory structure: {directory_path}")
        print(f"Permissions: {oct(mode)}")
        return True
    except OSError as e:
        print(f"Error creating directories '{directory_path}': {e}")
        return False


# Create nested directories with restrictive permissions
create_nested_directories_with_permissions("private/data/logs", 0o700)
