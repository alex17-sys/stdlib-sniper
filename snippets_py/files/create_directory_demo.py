# 🧩 Create single directory
import os

os.mkdir("new_directory")


# 🧩 Create directory safely
import os

try:
    os.mkdir("new_directory")
    print("Directory created successfully")
except FileExistsError:
    print("Directory already exists")
except OSError as e:
    print(f"Error creating directory: {e}")


# 🧩 Create directory if not exists
import os


def create_directory_if_not_exists(directory):
    """Create directory only if it doesn't exist."""
    if not os.path.exists(directory):
        try:
            os.mkdir(directory)
            print(f"Directory '{directory}' created successfully")
            return True
        except OSError as e:
            print(f"Error creating directory '{directory}': {e}")
            return False
    else:
        print(f"Directory '{directory}' already exists")
        return True


create_directory_if_not_exists("my_directory")


# 🧩 Create directory with permissions
import os


def create_directory_with_permissions(directory, mode=0o755):
    """Create directory with specific permissions."""
    try:
        os.mkdir(directory, mode)
        print(f"Directory '{directory}' created with permissions {oct(mode)}")
        return True
    except FileExistsError:
        print(f"Directory '{directory}' already exists")
        return True
    except OSError as e:
        print(f"Error creating directory '{directory}': {e}")
        return False


# Create directory with read/write/execute for owner, read/execute for others
create_directory_with_permissions("secure_dir", 0o755)

# Create directory with read/write for owner only
create_directory_with_permissions("private_dir", 0o700)
