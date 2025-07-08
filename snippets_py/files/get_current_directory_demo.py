# 🧩 Get current working directory
import os

current_dir = os.getcwd()
print(current_dir)


# 🧩 Get current directory safely
import os

try:
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")
except OSError as e:
    print(f"Error getting current directory: {e}")


# 🧩 Get current directory with validation
import os


def get_current_directory_validated():
    """Get current directory with existence validation."""
    try:
        current_dir = os.getcwd()

        # Validate that the directory still exists
        if not os.path.exists(current_dir):
            print(f"Warning: Current directory '{current_dir}' no longer exists")
            return None

        # Check if we have read permissions
        if not os.access(current_dir, os.R_OK):
            print(f"Warning: No read access to current directory '{current_dir}'")
            return None

        return current_dir
    except OSError as e:
        print(f"Error getting current directory: {e}")
        return None


current_dir = get_current_directory_validated()
if current_dir:
    print(f"Current directory: {current_dir}")


# 🧩 Get current directory with path analysis
import os


def analyze_current_directory():
    """Get current directory with detailed path analysis."""
    try:
        current_dir = os.getcwd()

        # Get path components
        path_parts = current_dir.split(os.sep)

        # Get directory info
        dir_info = {
            "full_path": current_dir,
            "basename": os.path.basename(current_dir),
            "dirname": os.path.dirname(current_dir),
            "depth": len([p for p in path_parts if p]),
            "is_root": current_dir == os.sep or (os.name == "nt" and len(current_dir) <= 3),
            "exists": os.path.exists(current_dir),
            "readable": os.access(current_dir, os.R_OK),
            "writable": os.access(current_dir, os.W_OK),
        }

        return dir_info
    except OSError as e:
        print(f"Error analyzing current directory: {e}")
        return None


info = analyze_current_directory()
if info:
    print(f"Current directory: {info['full_path']}")
    print(f"Directory name: {info['basename']}")
    print(f"Parent directory: {info['dirname']}")
    print(f"Path depth: {info['depth']}")
    print(f"Is root: {info['is_root']}")
    print(f"Readable: {info['readable']}")
    print(f"Writable: {info['writable']}")
