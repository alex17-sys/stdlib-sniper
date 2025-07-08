# 🧩 List all files recursively
import os

for root, dirs, files in os.walk("."):
    for file in files:
        print(os.path.join(root, file))


# 🧩 List directories recursively
import os

for root, dirs, files in os.walk("."):
    for dir in dirs:
        print(os.path.join(root, dir))


# 🧩 List files with relative paths
import os


def list_files_recursive(directory=".", relative=True):
    """List all files recursively with optional relative paths."""
    files = []

    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            if relative:
                # Make path relative to starting directory
                rel_path = os.path.relpath(full_path, directory)
                files.append(rel_path)
            else:
                files.append(full_path)

    return files


# Get relative paths
relative_files = list_files_recursive(".")
for file in relative_files:
    print(file)

# Get absolute paths
absolute_files = list_files_recursive(".", relative=False)
for file in absolute_files:
    print(file)


# 🧩 List files with depth limit
import os


def list_files_with_depth(directory=".", max_depth=2):
    """List files recursively with depth limit."""
    files = []

    for root, dirs, filenames in os.walk(directory):
        # Calculate current depth
        depth = root.replace(directory, "").count(os.sep)

        if depth >= max_depth:
            # Don't traverse deeper
            dirs.clear()
            continue

        for filename in filenames:
            rel_path = os.path.relpath(os.path.join(root, filename), directory)
            files.append(rel_path)

    return files


# List files up to 2 levels deep
shallow_files = list_files_with_depth(".", max_depth=2)
for file in shallow_files:
    print(file)
